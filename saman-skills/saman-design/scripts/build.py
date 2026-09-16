#!/usr/bin/env python3
"""
SAMAN DESIGN — build + export.

Usage:
    python3 scripts/build.py <design.html> static   # 4K PNG  (2160x2700)
    python3 scripts/build.py <design.html> motion   # MP4 + feed GIF
    python3 scripts/build.py <design.html> audit    # hand off to the craft autofix loop

Run it from inside the design folder — output lands next to the HTML.

static  -> base64-embeds fonts and avatar, renders at 4x and LANCZOS-downscales to
           2160x2700, then prints a geometry audit (canvas size, card widths,
           overflow, sub-12px text, corner pixel, spine presence).
motion  -> steps window.renderFrame(t), t in 0..1, screenshotting each frame, then
           muxes <name>-motion.mp4 (full res) and <name>-feed.gif (1080x1350).
           The HTML MUST expose window.renderFrame(t) and MUST NOT use CSS
           keyframes — a stepped screenshot does not advance them.

ASSETS ARE BUNDLED. This skill resolves its own assets/ folder first and never
reaches into another skill. Saman is never asked to upload a font or an avatar.
Override the search root with SAMAN_ASSETS if she moves them.

Placeholders:
    {{INTER_400}} {{INTER_500}} {{INTER_600}} {{INTER_700}} {{INTER_800}}
    {{AVATAR}}
"""
import base64, mimetypes, os, pathlib, shutil, subprocess, sys

CANVAS_W, CANVAS_H = 1080, 1350
EXPORT_W, EXPORT_H = 2160, 2700
HERE = pathlib.Path(__file__).resolve().parent
SKILL = HERE.parent

# Own assets FIRST. The sibling skills are a courtesy fallback for a partial
# install; nothing here ever points at another creator's skill folder.
ASSET_ROOTS = [
    pathlib.Path(os.environ["SAMAN_ASSETS"]) if os.environ.get("SAMAN_ASSETS") else None,
    SKILL / "assets",
    SKILL.parent / "saman-brand" / "assets",
    SKILL.parent / "saman-craft" / "assets",
]
ASSET_ROOTS = [r for r in ASSET_ROOTS if r and r.exists()]

PLACEHOLDERS = {
    "{{INTER_400}}": ["fonts/inter-latin-400-normal.woff2"],
    "{{INTER_500}}": ["fonts/inter-latin-500-normal.woff2"],
    "{{INTER_600}}": ["fonts/inter-latin-600-normal.woff2"],
    "{{INTER_700}}": ["fonts/inter-latin-700-normal.woff2"],
    "{{INTER_800}}": ["fonts/inter-latin-800-normal.woff2"],
    "{{AVATAR}}":    ["saman-avatar.png", "saman-avatar-placeholder.png"],
}

MIME = {".woff2": "font/woff2", ".woff": "font/woff", ".ttf": "font/ttf",
        ".png": "image/png", ".jpg": "image/jpeg", ".svg": "image/svg+xml"}


def find_asset(rels):
    for root in ASSET_ROOTS:
        for rel in rels:
            p = root / rel
            if p.exists():
                return p
    return None


def data_uri(p: pathlib.Path) -> str:
    mime = MIME.get(p.suffix.lower()) or mimetypes.guess_type(p.name)[0] or "application/octet-stream"
    return f"data:{mime};base64," + base64.b64encode(p.read_bytes()).decode()


def embed(src_html: pathlib.Path) -> pathlib.Path:
    """Inline every asset so the finished sheet is one portable file."""
    html = src_html.read_text()
    missing = []
    for token, rels in PLACEHOLDERS.items():
        if token not in html:
            continue
        path = find_asset(rels)
        if path is None:
            missing.append(token)
            continue
        html = html.replace(token, data_uri(path))
    if missing:
        # Fail loudly. A sheet that silently renders in a fallback font is worse
        # than no sheet — it looks almost right and ships off-brand.
        print("ASSET MISS:", ", ".join(missing))
        print("  searched:", [str(r) for r in ASSET_ROOTS])
        print("  fix: restore saman-design/assets/ or set SAMAN_ASSETS=<dir>")
        sys.exit(1)
    out = src_html.with_name("final-" + src_html.name)
    out.write_text(html)
    print(f"embedded  {out.stat().st_size // 1024} KB -> {out.name}")
    return out


def _ffmpeg():
    """A full ffmpeg, or None.

    Order matters. Playwright ships a stripped build with no H.264 encoder and
    no palette filters, so it is checked last and only accepted if it can
    actually encode — otherwise MP4 is skipped and the GIF (written by Pillow)
    still ships.
    """
    cands = []
    if os.environ.get("SAMAN_FFMPEG"):
        cands.append(os.environ["SAMAN_FFMPEG"])
    if shutil.which("ffmpeg"):
        cands.append(shutil.which("ffmpeg"))
    try:
        import imageio_ffmpeg
        cands.append(imageio_ffmpeg.get_ffmpeg_exe())
    except Exception:
        pass
    root = pathlib.Path(os.environ.get("PLAYWRIGHT_BROWSERS_PATH", "/opt/pw-browsers"))
    cands += [str(c) for c in sorted(root.glob("ffmpeg-*/ffmpeg-linux"))]
    for exe in cands:
        try:
            out = subprocess.run([exe, "-hide_banner", "-encoders"],
                                 capture_output=True, text=True, timeout=20).stdout
            if "libx264" in out:
                return exe
        except Exception:
            continue
    return None


def _chromium_exe():
    """A Chromium the installed Playwright can drive.

    Normally Playwright finds its own. When the pip package and the on-disk
    browser revision disagree (common in preconfigured containers, and in any
    environment where `playwright install` cannot reach the CDN), fall back to
    whatever Chromium is actually present. SAMAN_CHROMIUM overrides everything.
    """
    if os.environ.get("SAMAN_CHROMIUM"):
        return os.environ["SAMAN_CHROMIUM"]
    roots = [pathlib.Path(os.environ.get("PLAYWRIGHT_BROWSERS_PATH", "/opt/pw-browsers")),
             pathlib.Path.home() / ".cache/ms-playwright"]
    for root in roots:
        if not root.exists():
            continue
        for pat in ("chromium-*/chrome-linux/chrome",
                    "chromium_headless_shell-*/chrome-linux/headless_shell",
                    "chromium-*/chrome-mac/Chromium.app/Contents/MacOS/Chromium",
                    "chromium-*/chrome-win/chrome.exe"):
            hits = sorted(root.glob(pat))
            if hits:
                return str(hits[-1])
    for name in ("chromium", "chromium-browser", "google-chrome"):
        if shutil.which(name):
            return shutil.which(name)
    return None


def launch(p, args=None):
    """Launch Chromium, falling back to a discovered binary on a version clash."""
    args = args or []
    try:
        return p.chromium.launch(args=args)
    except Exception:
        exe = _chromium_exe()
        if not exe:
            print("no Chromium found — run `python -m playwright install chromium`,")
            print("or set SAMAN_CHROMIUM=/path/to/chrome")
            sys.exit(1)
        return p.chromium.launch(args=args, executable_path=exe)


AUDIT_JS = """() => {
  const cv = document.querySelector('.canvas');
  if (!cv) return {error:'no .canvas element'};
  const cr = cv.getBoundingClientRect();
  const cards = [...document.querySelectorAll('.card')].map(e => {
    const b = e.getBoundingClientRect();
    return {w:+b.width.toFixed(1), h:+b.height.toFixed(1),
            ov: e.scrollHeight - e.clientHeight};
  });
  const fe = document.querySelector('.footer');
  const f  = fe ? fe.getBoundingClientRect() : null;
  const small = [...document.querySelectorAll('.canvas *')].filter(e => {
    const fs = parseFloat(getComputedStyle(e).fontSize);
    return e.children.length === 0 && e.textContent.trim() && fs < 12;
  }).map(e => e.tagName + ':' + e.textContent.trim().slice(0, 18));
  // the spine is the brand law — a sheet without one is not hers
  const spine = document.querySelector('.spine path');
  let spineLen = 0;
  try { spineLen = spine ? Math.round(spine.getTotalLength()) : 0; } catch (e) {}
  return {
    canvas:  {w:+cr.width.toFixed(1), h:+cr.height.toFixed(1)},
    footer:  f ? {t:+(f.top-cr.top).toFixed(1), w:+f.width.toFixed(1)} : null,
    widths:  [...new Set(cards.map(c => c.w))],
    overflow: cards.filter(c => c.ov > 2).length,
    sub12:   small,
    spineLen: spineLen,
    nodes:   document.querySelectorAll('.node').length,
    pills:   document.querySelectorAll('.pill').length
  };
}"""


def _report(m, frame_hint=""):
    print("AUDIT", m)
    checks = [
        ("canvas 1080x1350", abs(m["canvas"]["w"] - CANVAS_W) < 2 and abs(m["canvas"]["h"] - CANVAS_H) < 2),
        ("footer pinned 1306 full width", bool(m["footer"]) and abs(m["footer"]["t"] - 1306) < 2
                                          and abs(m["footer"]["w"] - CANVAS_W) < 2),
        ("no card overflow", m["overflow"] == 0),
        ("no text under 12px", len(m["sub12"]) == 0),
        # Funnel narrows its cards on purpose — every other frame must be equal.
        ("card widths equal", len(m["widths"]) <= 1 or "funnel" in frame_hint.lower()),
        ("spine present", m["spineLen"] > 200),
        ("exactly one ink pill", m["pills"] == 1),
    ]
    for name, ok in checks:
        print(f"  {'PASS' if ok else 'FAIL'}  {name}")
    allok = all(ok for _, ok in checks)
    print("GEOMETRY", "PASS" if allok else "CHECK — run `build.py <file> audit` to autofix")
    return allok


def render_static(final: pathlib.Path, stem: str):
    from playwright.sync_api import sync_playwright
    from PIL import Image
    SCALE = 4  # render at 4x and downscale: 2x leaves hairlines and small type soft
    raw, out = f"{stem}-raw{SCALE}x.png", f"{stem}-4k.png"
    with sync_playwright() as p:
        b = launch(p, [
            f"--force-device-scale-factor={SCALE}", "--high-dpi-support=1",
            "--font-render-hinting=none", "--disable-lcd-text",
        ])
        pg = b.new_page(viewport={"width": CANVAS_W + 40, "height": CANVAS_H + 50},
                        device_scale_factor=SCALE)
        pg.goto(f"file://{final}")
        pg.wait_for_timeout(2600)                      # let the bundled fonts land
        pg.evaluate("window.renderFrame && window.renderFrame(1)")  # rest state
        pg.wait_for_timeout(300)
        pg.locator(".canvas").screenshot(path=raw)
        m = pg.evaluate(AUDIT_JS)
        b.close()
    Image.open(raw).resize((EXPORT_W, EXPORT_H), Image.LANCZOS).save(out, optimize=True)
    pathlib.Path(raw).unlink(missing_ok=True)
    img = Image.open(out)
    print(f"rendered  {out}  {img.size}  corner{img.getpixel((0, 0))}  "
          f"{pathlib.Path(out).stat().st_size // 1024} KB")
    img.resize((CANVAS_W, CANVAS_H), Image.LANCZOS).save(f"{stem}-preview.png")
    _report(m, stem)


def render_motion(final: pathlib.Path, stem: str):
    """12-16s budget: 9s of animation, 4.5s hold. The hold frames are copies of
    the rest frame — re-screenshotting identical pixels is wasted minutes.

    The GIF is written by Pillow so motion works with no ffmpeg at all. The MP4
    is a bonus when a real ffmpeg is present (LinkedIn prefers it over a GIF).
    """
    from playwright.sync_api import sync_playwright
    from PIL import Image
    FPS, SECONDS, HOLD = 24, 9, 4.5
    frames = pathlib.Path("frames")
    if frames.exists():
        shutil.rmtree(frames)
    frames.mkdir()
    total, hold_n = int(FPS * SECONDS), int(FPS * HOLD)
    with sync_playwright() as p:
        b = launch(p, ["--force-device-scale-factor=2", "--high-dpi-support=1"])
        pg = b.new_page(viewport={"width": CANVAS_W + 40, "height": CANVAS_H + 50},
                        device_scale_factor=2)
        pg.goto(f"file://{final}")
        pg.wait_for_timeout(2200)
        if not pg.evaluate("typeof window.renderFrame === 'function'"):
            print("no window.renderFrame(t) — motion needs it (and no CSS keyframes)")
            sys.exit(1)
        el, n = pg.locator(".canvas"), 0
        for f in range(total + 1):
            pg.evaluate(f"window.renderFrame({f / total})")
            el.screenshot(path=f"frames/f{n:04d}.png")
            n += 1
        pg.evaluate("window.renderFrame(1)")
        el.screenshot(path="frames/hold.png")
        b.close()
    for _ in range(hold_n):
        shutil.copy("frames/hold.png", f"frames/f{n:04d}.png")
        n += 1
    print(f"frames    {n}  ({SECONDS}s animation + {HOLD}s hold)")

    ff = _ffmpeg()

    # ---- GIF ----
    # ffmpeg's two-pass palette is both smaller and cleaner on flat brand colour,
    # so use it when a real ffmpeg is around. Pillow is the no-dependency
    # fallback so motion still ships on a bare machine.
    gif = f"{stem}-feed.gif"
    if ff:
        pal = str(pathlib.Path(gif).with_name("saman-palette.png"))
        vf = f"fps={FPS},scale={CANVAS_W}:{CANVAS_H}:flags=lanczos"
        subprocess.run([ff, "-y", "-loglevel", "error", "-framerate", str(FPS),
                        "-i", "frames/f%04d.png", "-vf",
                        f"{vf},palettegen=max_colors=128:stats_mode=diff", pal], check=True)
        subprocess.run([ff, "-y", "-loglevel", "error", "-framerate", str(FPS),
                        "-i", "frames/f%04d.png", "-i", pal, "-lavfi",
                        f"{vf}[x];[x][1:v]paletteuse=dither=bayer:bayer_scale=5:diff_mode=rectangle",
                        gif], check=True)
        pathlib.Path(pal).unlink(missing_ok=True)
    else:
        from PIL import Image
        paths = sorted(frames.glob("f*.png"))
        # Collapse the identical hold frames into one long frame — 100+ duplicate
        # frames is most of the file size for none of the motion.
        anim, hold_ms = paths[:total + 1], int(HOLD * 1000)
        master = Image.open("frames/hold.png").convert("RGB") \
                      .resize((CANVAS_W, CANVAS_H), Image.LANCZOS) \
                      .quantize(colors=128, method=Image.MEDIANCUT)
        seq = [Image.open(fp).convert("RGB").resize((CANVAS_W, CANVAS_H), Image.LANCZOS)
                 .quantize(palette=master, dither=Image.FLOYDSTEINBERG) for fp in anim]
        durations = [int(1000 / FPS)] * len(seq)
        durations[-1] = hold_ms
        seq[0].save(gif, save_all=True, append_images=seq[1:], loop=0,
                    duration=durations, optimize=True, disposal=1)
    kb = pathlib.Path(gif).stat().st_size // 1024
    print(f"rendered  {gif}  {kb} KB" + ("  (large — drop FPS or colours)" if kb > 8192 else ""))

    # ---- MP4, when a real ffmpeg is around (LinkedIn prefers it to a GIF) ----
    if ff:
        mp4 = f"{stem}-motion.mp4"
        subprocess.run([ff, "-y", "-loglevel", "error", "-framerate", str(FPS),
                        "-i", "frames/f%04d.png", "-c:v", "libx264", "-pix_fmt", "yuv420p",
                        "-crf", "17", "-vf", f"scale={CANVAS_W}:{CANVAS_H}:flags=lanczos",
                        mp4], check=True)
        print(f"rendered  {mp4}  {pathlib.Path(mp4).stat().st_size // 1024} KB")
    else:
        print("no full ffmpeg — GIF only. `pip install imageio-ffmpeg` adds the MP4.")
    shutil.rmtree(frames, ignore_errors=True)


def run_audit(src: pathlib.Path):
    """Hand the geometry fix-loop to /saman-craft. Never hand-nudge a row height."""
    for c in [SKILL.parent / "saman-craft" / "scripts" / "autofix.py",
              pathlib.Path.home() / ".claude/skills/saman-craft/scripts/autofix.py",
              pathlib.Path("/mnt/skills/user/saman-craft/scripts/autofix.py")]:
        if c.exists():
            sys.exit(subprocess.run([sys.executable, str(c), str(src)]).returncode)
    print("saman-craft autofix not found — install the /saman-craft skill next to this one")
    sys.exit(1)


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    src = pathlib.Path(sys.argv[1]).resolve()
    if not src.exists():
        print("no such file:", src)
        sys.exit(1)
    mode = sys.argv[2] if len(sys.argv) > 2 else "static"
    if mode == "audit":
        run_audit(src)
    final = embed(src)
    if mode == "static":
        render_static(final, src.stem)
    elif mode == "motion":
        render_motion(final, src.stem)
    else:
        print("unknown mode:", mode)
        sys.exit(1)


if __name__ == "__main__":
    main()

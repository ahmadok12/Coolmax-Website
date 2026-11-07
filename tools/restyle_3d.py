# Restyles a 3D viewer page in the site's design language (2026-11-07):
#   royal blue accent, cool off-white page with faint blue light, frosted glass cards, rounded corners,
#   floating glass header, Urbanist + Gloock type.
# Layout: the Live readout sits on top, right above the 3D stage, on desktop and phones (so it is always in view
# while someone plays with the cooler); Part details and How it works move below; the Cycles renders and the
# Snapshots strip are gone.
#
# Works on the website copies (site/3d/**/index.html) and on the viewer sources (web/viewer.html in the
# "Coolmax 3D Viewer" and "PureBreeze 3D Viewer" folders, page_template.html + viewer.js for the Mini Chiller), so a rebuild
# keeps the new look.  Usage: python tools/restyle_3d.py FILE [FILE ...]
import re, sys

MARK = "/* --- site skin (2026-11-07)"

SKIN = MARK + """: royal blue, glass cards, rounded corners; readout on top --- */
:root, :root:not([data-theme="light"]), :root[data-theme="dark"] {
  --navy: #2f5bd3; --navy-d: #1f44a8; --cyan: #4f7ef0; --gold: #e98a52;
  --ink: #0f1726; --muted: #536075; --line: #dbe1ea; --bg: #f5f7fa;
  --card: rgba(255, 255, 255, .62); --card-solid: #fbfcfe; --edge: rgba(255, 255, 255, .88);
  --stage-top: #ffffff; --stage-bot: #dfe5ee; --chip: rgba(234, 239, 247, .8);
  --on: #17a35a; --off: #d63a2f; --lcd-bg: #0b1730; --lcd-fg: #8fd1ff;
  --shadow: 0 1px 0 rgba(255, 255, 255, .8) inset, 0 12px 32px -18px rgba(15, 23, 38, .22);
  --font: "Urbanist", system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
  --display: "Gloock", Georgia, "Times New Roman", serif;
  --radius: 18px; --blur: saturate(1.5) blur(16px);
  color-scheme: light;
}
body { background: var(--bg); color: var(--ink); font-size: 15.5px; }
body::before { content: ""; position: fixed; inset: 0; z-index: -1; pointer-events: none;
  background: radial-gradient(42rem 32rem at 8% 12%, rgba(47, 91, 211, .10), transparent 70%),
    radial-gradient(38rem 30rem at 95% 45%, rgba(110, 160, 255, .16), transparent 70%),
    radial-gradient(40rem 30rem at 30% 95%, rgba(47, 91, 211, .08), transparent 70%); }
.page { gap: 14px; padding-top: 12px; }
.card { background: var(--card); border: 1px solid var(--edge); box-shadow: var(--shadow); -webkit-backdrop-filter: var(--blur); backdrop-filter: var(--blur); }
.card h2 { font-size: .7rem; letter-spacing: .14em; color: var(--muted); padding: 12px 18px 9px; border-bottom: 1px solid rgba(195, 204, 217, .55); }

/* floating glass header, like the site navbar */
header.top { position: sticky; top: 10px; z-index: 40; background: rgba(255, 255, 255, .72); border: 1px solid var(--edge); border-radius: 999px;
  box-shadow: var(--shadow); -webkit-backdrop-filter: var(--blur); backdrop-filter: var(--blur); padding: 8px 10px 8px 10px; gap: 12px; flex-wrap: nowrap; }
.mark { width: 42px; height: 42px; border-radius: 50%; background: var(--navy); box-shadow: 0 6px 16px -6px rgba(47, 91, 211, .6); }
.mark svg { width: 24px; height: 24px; }
.mark svg rect { stroke: #fff; } .mark svg circle { fill: #bcd0ff; } .mark svg path { stroke: #bcd0ff; }
a.mark { width: auto; height: 42px; padding: 0 16px; border-radius: 999px; background: #fff; border: 1px solid var(--line); box-shadow: none; }
a.mark img { display: block; width: auto; height: 19px; }
.brand { flex: 1 1 auto; }
.brand h1 { font-family: var(--display); font-weight: 400; font-size: 1.4rem; letter-spacing: 0; }
.brand p { font-size: .84rem; }
.back { color: var(--ink); font-weight: 600; padding: 9px 14px; border-radius: 999px; }
.back:hover { background: var(--chip); text-decoration: none; }
.buy { display: flex; gap: 8px; flex: none; }
.buy a { display: inline-flex; align-items: center; justify-content: center; gap: 6px; padding: 10px 18px; border-radius: 999px; font-weight: 700; font-size: .9rem; text-decoration: none; white-space: nowrap; transition: transform .15s, box-shadow .15s; }
.buy .q { background: var(--navy); color: #fff; box-shadow: 0 8px 18px -10px rgba(47, 91, 211, .9); }
.buy .q:hover { background: var(--navy-d); }
.buy .w { background: #0f7d44; color: #fff; }
.buy a:hover { transform: translateY(-1px); }
.filechip { display: none; }

/* main grid: parts list | control panel, live readout, 3D stage */
.grid { grid-template-columns: 244px minmax(0, 1fr); gap: 14px; }
.center { gap: 14px; }
.plist { position: sticky; top: 84px; max-height: calc(100vh - 100px); overflow: auto; }
.plist li button { border-radius: 12px; }
.plist li button[aria-current="true"] { background: rgba(47, 91, 211, .1); border-color: rgba(47, 91, 211, .45); }
.plist li button[aria-current="true"] .n { background: var(--navy); border-color: var(--navy); }
.plist small.in { color: var(--navy); }

.ctrlbar h2 { display: none; }
.ctrlbar .body { padding: 12px 16px; }
.power { background: radial-gradient(circle at 35% 30%, #3d5fc4, #14244f); box-shadow: inset 0 -3px 6px rgba(0,0,0,.4), 0 8px 18px -8px rgba(31, 68, 168, .8); }
.lcd { border-radius: 12px; }
.key, .seg button { border-radius: 12px; border-color: rgba(195, 204, 217, .7); background: var(--chip); }
.key:not(:disabled):hover, .seg button:hover { border-color: var(--navy); }
.key[aria-pressed="true"], .seg button[aria-pressed="true"] { background: var(--navy); border-color: var(--navy); box-shadow: 0 6px 14px -8px rgba(47, 91, 211, .9); }

/* live readout: one row of tiles right above the 3D stage, its title as a small label at the start */
.readout { display: grid; grid-template-columns: auto minmax(0, 1fr); align-items: center; }
.readout h2 { border: 0; padding: 0 4px 0 18px; display: flex; align-items: center; gap: 8px; writing-mode: horizontal-tb; max-width: 92px; line-height: 1.35; }
.readout h2::before { content: ""; flex: none; width: 8px; height: 8px; border-radius: 50%; background: var(--on); box-shadow: 0 0 0 4px rgba(23, 163, 90, .16); }
.readout .body { display: grid; grid-template-columns: repeat(auto-fit, minmax(112px, 1fr)); gap: 8px; padding: 10px; }
.readout .meter { display: grid; grid-template-columns: minmax(0, 1fr); grid-template-areas: "l" "v" "t"; gap: 3px; margin: 0; padding: 9px 11px 10px; border-radius: 12px; background: rgba(255, 255, 255, .7); border: 1px solid rgba(219, 225, 234, .9); }
.readout .meter > span:first-child { grid-area: l; font-size: .74rem; color: var(--muted); font-weight: 600; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.readout .meter .v { grid-area: v; text-align: start; font-size: 1.02rem; font-weight: 600; color: var(--ink); white-space: nowrap; }
.readout .meter .trk { grid-area: t; height: 5px; border: 0; background: rgba(195, 204, 217, .45); margin-top: 2px; }
.meter .trk i { background: linear-gradient(90deg, #5b8cff, var(--navy)); }
.meter.warm .trk i { background: linear-gradient(90deg, #f4b183, var(--gold)); }
.meter.elec .trk i { background: linear-gradient(90deg, #f08a7e, var(--off)); }

/* 3D stage */
.stage { height: clamp(420px, calc(100vh - 318px), 720px); min-height: 0; border: 1px solid var(--edge); box-shadow: var(--shadow);
  background: radial-gradient(120% 95% at 50% 36%, #ffffff 0%, #f0f3f8 55%, #dfe5ee 100%); }
.loading { background: radial-gradient(120% 95% at 50% 36%, #ffffff 0%, #f0f3f8 55%, #dfe5ee 100%); }
.stage .title h2 { font-family: var(--display); font-weight: 400; font-size: 1.75rem; letter-spacing: 0; }
.hint { background: rgba(255, 255, 255, .75); color: var(--ink); border: 1px solid var(--edge); border-radius: 12px; transform: none; -webkit-backdrop-filter: var(--blur); backdrop-filter: var(--blur); box-shadow: var(--shadow); }
.viewmode { background: rgba(255, 255, 255, .66); border: 1px solid var(--edge); border-radius: 16px; box-shadow: var(--shadow); -webkit-backdrop-filter: var(--blur); backdrop-filter: var(--blur); }
.tbgroup { background: rgba(255, 255, 255, .7); border: 1px solid var(--edge); border-radius: 999px; box-shadow: var(--shadow); -webkit-backdrop-filter: var(--blur); backdrop-filter: var(--blur); }
.tbgroup button { border-right-color: rgba(195, 204, 217, .55); padding: 9px 14px; }
.tbgroup button[aria-pressed="true"] { background: rgba(47, 91, 211, .12); color: var(--navy); }
.lbl { background: var(--card-solid); }
.lbl.sel { background: #e4ebfb; border-color: var(--navy); }
.lbl.sel .n, .labels circle.sel { background: var(--navy); fill: var(--navy); }
.badge-n { background: radial-gradient(circle at 35% 30%, #5b8cff, var(--navy-d)); }

/* part details and how it works, below the stage */
.info { display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); gap: 14px; align-items: start; }
.pd-head h3 { font-family: var(--display); font-weight: 400; font-size: 1.3rem; }
.notes .fun { border-top: 1px solid var(--line); }
footer { padding-top: 4px; }

@media (max-width: 1240px) {
  .grid { grid-template-columns: minmax(0, 1fr); }
  .plist { grid-column: auto; order: 3; position: static; max-height: none; }
}
@media (max-width: 980px) { .info { grid-template-columns: minmax(0, 1fr); } }

/* phones: readout, 3D stage and control panel all fit in the first screen */
@media (max-width: 760px) {
  .page { padding-top: 8px; gap: 10px; padding-bottom: calc(82px + env(safe-area-inset-bottom)); }
  /* no backdrop-filter here: it would trap the fixed quote bar inside the header */
  header.top { position: relative; top: 0; -webkit-backdrop-filter: none; backdrop-filter: none; background: rgba(255, 255, 255, .85); padding: 6px 8px; border-radius: 18px; gap: 10px; }
  .mark { width: 36px; height: 36px; }
  a.mark { width: auto; padding: 0 10px; } a.mark img { height: 15px; }
  .brand h1 { font-size: 1.12rem; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
  .brand p { display: none; }
  .back { font-size: .8rem; padding: 8px 10px; }
  .center { display: flex; flex-direction: column; gap: 10px; }
  .readout { order: -2; }
  .stage { order: -1; height: clamp(300px, calc(100svh - 500px), 560px); min-height: 0; max-height: none; }
  .readout { display: block; }
  .readout h2 { display: none; }
  .readout .body { grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 6px; padding: 8px; }
  .readout .meter { padding: 5px 8px 6px; gap: 1px; border-radius: 10px; }
  .readout .meter > span:first-child { font-size: .64rem; line-height: 1.3; }
  .readout .meter .trk { height: 4px; }
  /* compact view-mode panel: modes on one row, two switches under it */
  .viewmode { grid-template-columns: 1fr 1fr; padding: 6px; gap: 4px 10px; bottom: 60px; }
  .viewmode .seg button { min-height: 38px; padding: 4px 0; grid-auto-flow: column; align-items: center; justify-content: center; gap: 6px; }
  .viewmode .tog { min-height: 30px; }
  .viewmode label[for="t-all"] { display: none; }
  .readout .meter .v { font-family: var(--font); font-variant-numeric: tabular-nums; font-weight: 700; font-size: .84rem; letter-spacing: -.01em; }
  .ctrlbar .body { padding: 10px; }
  .ctrlbar .unit { grid-template-columns: auto minmax(0, 1fr); gap: 10px; }
  .ctrlbar .keys { grid-column: 1 / -1; grid-template-columns: repeat(6, minmax(0, 1fr)); gap: 6px; }
  .power { width: 54px; height: 54px; }
  .powerrow { gap: 10px; }
  .leds { font-size: .74rem; }
  .ctrlbar .lcd { min-height: 54px; }
  .key { min-height: 50px; padding: 6px 2px; font-size: .68rem; }
  .key svg { width: 16px; height: 16px; }
  .snaps, footer { display: none; }
  .buy { position: fixed; z-index: 50; inset-inline: 10px; bottom: calc(8px + env(safe-area-inset-bottom)); padding: 7px; border-radius: 999px;
    background: rgba(255, 255, 255, .78); border: 1px solid var(--edge); box-shadow: 0 14px 34px -14px rgba(15, 23, 38, .4); -webkit-backdrop-filter: var(--blur); backdrop-filter: var(--blur); }
  .buy a { flex: 1; min-height: 46px; font-size: .95rem; }
}
@media (max-width: 420px) {
  .powerrow .leds { display: none; }
}
"""

FONTS_OLD = "family=Manrope:wght@400;500;600;700;800&family=IBM+Plex+Mono:wght@400;500;600&display=swap"
FONTS_NEW = "family=Gloock&family=Urbanist:wght@400;500;600;700;800&family=IBM+Plex+Mono:wght@400;500;600&display=swap"


def cut(html, start, end_pat, what):
    """Remove from `start` (literal) up to and including the first `end_pat` (literal) after it."""
    i = html.find(start)
    if i < 0:
        raise SystemExit(f"not found: {what}")
    j = html.find(end_pat, i)
    if j < 0:
        raise SystemExit(f"no end for: {what}")
    j += len(end_pat)
    # also swallow the indentation before and the newline after
    k = html.rfind("\n", 0, i) + 1
    if html[k:i].strip() == "":
        i = k
    if html[j:j + 1] == "\n":
        j += 1
    return html[:i] + html[j:], html[i:j]


def drop_snapshot_code(js, required=True):
    m = re.search(r"// ---------- snapshots ----------\n.*?\n(?=// ---------- )", js, re.S)
    if not m:
        if required:
            raise SystemExit("snapshot code not found")
        return js
    return js[:m.start()] + js[m.end():]


NOTE_MARK = "/* --- readout note (2026-11-07)"
NOTE_CSS = NOTE_MARK + """: the readout values are approximate --- */
.readout { grid-template-rows: auto auto; }
.readout h2 { grid-row: 1; align-self: end; }
.readout .ro-note { grid-column: 1; grid-row: 2; align-self: start; margin: 4px 0 0; padding: 0 4px 0 34px; max-width: 108px; font-size: .66rem; line-height: 1.3; color: var(--muted); }
.readout .body { grid-column: 2; grid-row: 1 / span 2; }
@media (max-width: 760px) {
  .readout .ro-note { max-width: none; margin: 0; padding: 0 10px 7px; font-size: .64rem; text-align: center; }
  .stage { height: clamp(300px, calc(100svh - 514px), 560px); }
}
"""
NOTE_HTML = '<p class="ro-note">Approximate values, for illustration only</p>'


def add_readout_note(html):
    """Small disclaimer under the Live readout title (desktop) or under the tiles (phones)."""
    if NOTE_MARK in html:
        return html, False
    m = re.search(r'(<section class="card readout"[^>]*>.*?)(\n[ \t]*</section>)', html, re.S)
    if not m:
        raise SystemExit("readout section not found")
    html = html[:m.end(1)] + "\n          " + NOTE_HTML + html[m.end(1):]
    html = html.replace("</style>", NOTE_CSS + "</style>", 1)
    return html, True


def restyle(html):
    if MARK in html:
        return add_readout_note(html)
    html = html.replace(FONTS_OLD, FONTS_NEW)

    # 1. old phone/site block goes; the skin replaces it
    m = re.search(r"/\* --- site integration \(2026-10-31\).*?\n(?=</style>)", html, re.S)
    if m:
        html = html[:m.start()] + html[m.end():]
    html = html.replace("</style>", SKIN + "</style>", 1)

    # 2. Cycles renders and Snapshots sections, the Snapshot button and its code
    html, _ = cut(html, '<section class="card cycles"', "</section>", "cycles section")
    html, _ = cut(html, '<section class="card snaps">', "</section>", "snaps section")
    # remove the tbgroup that holds only the Snapshot button
    m = re.search(r'\n[ \t]*<div class="tbgroup">\s*<button id="b-snap".*?</button>\s*</div>', html, re.S)
    if not m:
        raise SystemExit("snapshot button group not found")
    html = html[:m.start()] + html[m.end():]
    html = drop_snapshot_code(html, required="/*VIEWER_JS*/" not in html)

    # 3. Live readout moves up, right after the control panel and above the stage
    m = re.search(r'\n[ \t]*<section class="card">\s*<h2>Live readout</h2>.*?</section>', html, re.S)
    if not m:
        raise SystemExit("live readout not found")
    readout = m.group(0).strip().replace('<section class="card">', '<section class="card readout" aria-label="Live readout">', 1)
    html = html[:m.start()] + html[m.end():]
    m = re.search(r'(<section class="card ctrlbar".*?</section>\n)', html, re.S)
    if not m:
        raise SystemExit("control panel not found")
    html = html[:m.end()] + "        " + readout + "\n" + html[m.end():]

    # 4. Part details and How it works leave the side column and sit under the grid, side by side
    m = re.search(r'\n[ \t]*<aside style="display:grid; gap:16px; min-width:0;">\n(.*?)\n[ \t]*</aside>\n([ \t]*</div>\n)', html, re.S)
    if not m:
        raise SystemExit("aside not found")
    inner = m.group(1)
    html = html[:m.start()] + "\n" + m.group(2) + "\n  <div class=\"info\">\n" + inner + "\n  </div>\n" + html[m.end():]
    html, _ = add_readout_note(html)
    return html, True


if __name__ == "__main__":
    for path in sys.argv[1:]:
        src = open(path, encoding="utf-8").read()
        if path.endswith(".js"):  # Mini Chiller source keeps its script in viewer.js
            out = drop_snapshot_code(src, required=False)
            changed = out != src
        else:
            out, changed = restyle(src)
        if changed:
            open(path, "w", encoding="utf-8", newline="").write(out)
        print(("restyled " if changed else "already done ") + path)

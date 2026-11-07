"""Builds the Aolan logo as crisp SVGs from the small PNG Ahmad sent (tools/art/aolan-logo-source.png).

The AOLAN wordmark is traced (navy letters and the light-blue O ring, each its own layer, upscaled 8x
before tracing so the edges are smooth). The tagline is too small to trace cleanly, so it is set again
in Liberation Sans and turned into outlines, scaled to the same width and position as in the original.

Writes to site/assets/img/brands/:
  aolan-logo.svg        full logo (wordmark + "Evaporative Cooling Systems"), for light backgrounds
  aolan-wordmark.svg    AOLAN only, for small spots (menus, cards)
  aolan-wordmark-light.svg  AOLAN in white with the blue O, for dark backgrounds (homepage hero)
Run:  pip install potracer fonttools && python3 tools/make_aolan_logo.py
"""
import os

import numpy as np
import potrace
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont
from PIL import Image, ImageFilter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "tools", "art", "aolan-logo-source.png")
OUT = os.path.join(ROOT, "site", "assets", "img", "brands")
FONT = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
NAVY, SKY = "#0c4799", "#63cdf6"
UP = 8  # upscale before tracing
TAG_TOP = 70  # source rows from here down are the tagline


def coverage(a):
    """Per-pixel share of navy and sky blue, unmixing each pixel against a white background."""
    white = np.array([255, 255, 255], float)
    m = np.stack([np.array([12, 71, 153], float) - white, np.array([99, 205, 246], float) - white], 1)  # 3x2
    d = a.reshape(-1, 3) - white
    sol, *_ = np.linalg.lstsq(m, d.T, rcond=None)
    sol = np.clip(sol.T, 0, 1).reshape(a.shape[0], a.shape[1], 2)
    return sol[..., 0], sol[..., 1]


def trace(alpha):
    big = Image.fromarray((alpha * 255).astype(np.uint8)).resize((alpha.shape[1] * UP, alpha.shape[0] * UP), Image.BICUBIC).filter(ImageFilter.GaussianBlur(UP * .5))
    bm = potrace.Bitmap(np.array(big) <= 127)  # potracer traces the falsy pixels
    path = bm.trace(turdsize=40, alphamax=1.0, opticurve=True, opttolerance=0.5)
    f = lambda p: f"{p.x / UP:.2f} {p.y / UP:.2f}"
    d = []
    for c in path:
        d.append(f"M{f(c.start_point)}")
        for s in c.segments:
            if s.is_corner:
                d.append(f"L{f(s.c)}L{f(s.end_point)}")
            else:
                d.append(f"C{f(s.c1)} {f(s.c2)} {f(s.end_point)}")
        d.append("Z")
    return "".join(d)


def tagline(x0, x1, y_base, cap_h):
    """'Evaporative Cooling Systems' as outlines, fitted between x0 and x1 with its baseline at y_base."""
    font = TTFont(FONT)
    gs, cmap, hmtx = font.getGlyphSet(), font.getBestCmap(), font["hmtx"]
    upm = font["head"].unitsPerEm
    text = "Evaporative Cooling Systems"
    adv = sum(hmtx[cmap[ord(ch)]][0] for ch in text)
    s = cap_h / font["OS/2"].sCapHeight  # scale so capitals are as tall as in the source
    track = ((x1 - x0) - adv * s) / (len(text) - 1)  # letter-spacing that makes the width match
    pen = SVGPathPen(gs)
    x = x0
    for ch in text:
        g = cmap[ord(ch)]
        gs[g].draw(TransformPen(pen, (s, 0, 0, -s, x, y_base)))
        x += hmtx[g][0] * s + track
    del upm
    return pen.getCommands()


def svg(w, h, vb, layers, title):
    paths = "".join(f'<path fill="{c}" fill-rule="evenodd" d="{d}"/>' for c, d in layers)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" width="{w}" height="{h}" role="img">'
            f"<title>{title}</title>{paths}</svg>\n")


def main():
    a = np.array(Image.open(SRC).convert("RGB")).astype(float)
    navy, sky = coverage(a)
    word_navy, word_sky = navy.copy(), sky.copy()
    word_navy[TAG_TOP:], word_sky[TAG_TOP:] = 0, 0
    d_navy, d_sky = trace(word_navy), trace(word_sky)

    # tagline box in the source
    tag = navy[TAG_TOP:] > .5
    ys, xs = np.where(tag)
    x0, x1 = xs.min(), xs.max() + 1
    # cap height: rows covered by the capital E at the left edge
    e_rows = np.where(tag[:, x0:x0 + 3].any(1))[0]
    cap_top, base = TAG_TOP + e_rows.min(), TAG_TOP + e_rows.max() + 1
    d_tag = tagline(x0, x1, base, base - cap_top)

    ys, xs = np.where((navy > .3) | (sky > .3))
    pad = 2
    bx0, by0, bx1, by1 = xs.min() - pad, ys.min() - pad, xs.max() + 1 + pad, ys.max() + 1 + pad
    os.makedirs(OUT, exist_ok=True)
    full_vb = f"{bx0} {by0} {bx1 - bx0} {by1 - by0}"
    with open(os.path.join(OUT, "aolan-logo.svg"), "w") as fh:
        fh.write(svg((bx1 - bx0) * 4, (by1 - by0) * 4, full_vb, [(NAVY, d_navy + d_tag), (SKY, d_sky)], "Aolan Evaporative Cooling Systems"))

    ys, xs = np.where((word_navy > .3) | (word_sky > .3))
    wx0, wy0, wx1, wy1 = xs.min() - 1, ys.min() - 1, xs.max() + 2, ys.max() + 2
    word_vb = f"{wx0} {wy0} {wx1 - wx0} {wy1 - wy0}"
    for name, letters in (("aolan-wordmark.svg", NAVY), ("aolan-wordmark-light.svg", "#ffffff")):
        with open(os.path.join(OUT, name), "w") as fh:
            fh.write(svg((wx1 - wx0) * 4, (wy1 - wy0) * 4, word_vb, [(letters, d_navy), (SKY, d_sky)], "Aolan"))
    print("wrote", full_vb, word_vb)


if __name__ == "__main__":
    main()

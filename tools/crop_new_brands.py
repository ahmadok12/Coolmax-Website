"""Crop Coolmax and PureBreeze product photos from the supplier catalogues (run once; output is committed).

Usage: python3 tools/crop_new_brands.py <dir with page images>
The page images are the full-page JPEGs extracted with `pdfimages -j`:
  <dir>/cmx/i-NNN.jpg  Coolmax catalogue (catalogue page p is i-(p+8))
  <dir>/pbx/i-NNN.jpg  PureBreeze catalogue
Supplier logos and lettering are left out of every crop (or blurred where moulded into the product).
"""
import os
import sys

from PIL import Image, ImageFilter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "site", "assets", "img")

# name: (pdf page, (x0, y0, x1, y1)) in pixels of the 3354×2291 page image
COOLMAX = {
    "n700": (8, (1284, 492, 1560, 945)),
    "n900": (8, (1272, 1026, 1578, 1506)),
    "n18": (8, (1968, 654, 2502, 1500)),
    "window-wsa": (9, (138, 432, 594, 942)),
    "window-09cm": (9, (984, 462, 1548, 912)),
    "window-wsc": (9, (384, 1008, 852, 1542)),
    "wsc-01s": (9, (1896, 594, 2514, 1326)),
    "600t": (10, (240, 420, 816, 1464)),
    "600ht": (10, (1854, 504, 2532, 1428)),
    "700t": (11, (246, 414, 768, 1476)),
    "700ht": (11, (1836, 540, 2586, 1398)),
    "wsc-02": (12, (168, 450, 840, 1440)),
    "wsc-03": (12, (1842, 576, 2538, 1380)),
    "900t": (13, (228, 462, 804, 1410)),
    "900ht": (13, (1854, 612, 2556, 1332)),
    "18tc": (14, (216, 420, 546, 714)),
    "18sc": (14, (216, 792, 546, 1086)),
    "18dc": (14, (216, 1158, 546, 1446)),
    "30tc": (14, (1860, 414, 2172, 762)),
    "50tc": (14, (2814, 384, 3150, 708)),
    "wsa-02": (15, (174, 456, 828, 1440)),
    "wsa-03": (15, (1842, 576, 2538, 1380)),
    "900at": (16, (240, 504, 762, 1344)),
    "900hat": (16, (960, 624, 1440, 1476)),
    "p22at": (16, (2280, 396, 2700, 1086)),
    "p18at": (16, (1830, 816, 2256, 1494)),
    "p30at": (16, (2724, 750, 3198, 1488)),
    "18ta": (17, (216, 432, 546, 774)),
    "18sa": (17, (216, 810, 546, 1152)),
    "30ta": (17, (1866, 414, 2178, 762)),
    "30sa": (17, (1860, 774, 2178, 1134)),
    "j-plastic": (19, (1272, 348, 1500, 774)),
    "j-plastic-2": (19, (696, 384, 906, 774)),
    "j-metal": (19, (153, 1611, 633, 2109)),
    "big-18000": (19, (1896, 426, 2256, 930)),
    "big-23000": (19, (2418, 420, 2796, 870)),
    "big-35000": (19, (1926, 1068, 2328, 1560)),
    "big-50000": (19, (2724, 1026, 3114, 1566)),
}

# name: (page image index, box, [areas to blur]) in pixels of the 2201×1500 page image
PUREBREEZE = {
    "bldc-hero": (1, (200, 470, 860, 1175), [(630, 860, 810, 1000), (470, 500, 580, 575)]),
    "bldc-88c": (1, (1200, 180, 1700, 735), [(1470, 690, 1535, 850)]),
    "bldc-98c": (1, (1195, 820, 1720, 1400), [(1470, 1100, 1535, 1260)]),
    "pb-75": (2, (745, 300, 1025, 900), []),
    "pb-75f": (2, (1790, 520, 2065, 900), []),
    "dt80": (3, (1355, 290, 1690, 945), []),
    "dt60": (3, (305, 355, 560, 895), []),
    "turbo-900": (4, (370, 255, 650, 1110), []),
    "turbo-900r": (4, (1710, 325, 1935, 910), []),
    "pb-28000": (6, (410, 300, 690, 710), []),
    "pb-28000b": (6, (90, 300, 385, 710), []),
    "gs-5800": (6, (1500, 300, 1735, 730), []),
    "g-8288": (6, (410, 900, 690, 1360), []),
    "g-5800": (6, (1190, 880, 1440, 1360), []),
    "ag-680": (5, (1190, 340, 1440, 790), []),
    "pb-3808": (7, (400, 270, 610, 730), []),
    "pb-500": (7, (120, 820, 260, 1380), []),
    "pb-380": (7, (1230, 310, 1480, 710), []),
    "pb-380ad": (7, (1230, 810, 1480, 1390), []),
}


def drop_captions(im):
    """Remove model-code captions printed under (or over) a product: small, narrow text runs split off by white space."""
    g = im.convert("L").point(lambda v: 255 if v < 225 else 0)
    w, h = g.size
    rows = [g.crop((0, y, w, y + 1)).getbbox() for y in range(h)]
    runs, start = [], None
    for y, b in enumerate(rows + [None]):
        if b and start is None:
            start = y
        elif not b and start is not None:
            runs.append((start, y))
            start = None
    def narrow(r):
        xs = [rows[y] for y in range(*r)]
        return r[1] - r[0] < 45 and max(b[2] for b in xs) - min(b[0] for b in xs) < 0.4 * w
    while len(runs) > 1 and narrow(runs[-1]):
        runs.pop()
    while len(runs) > 1 and narrow(runs[0]):
        runs.pop(0)
    return im.crop((0, max(runs[0][0] - 12, 0), w, min(runs[-1][1] + 12, h)))


def save(im, path):
    im.thumbnail((1400, 1400))
    im.save(path + ".webp", "WEBP", quality=82, method=6)


def main(src):
    os.makedirs(os.path.join(OUT, "coolmax"), exist_ok=True)
    os.makedirs(os.path.join(OUT, "purebreeze"), exist_ok=True)
    for name, (page, (x0, y0, x1, y1)) in COOLMAX.items():
        with Image.open(os.path.join(src, "cmx", f"i-{page + 8:03d}.jpg")) as im:
            pad = 24
            crop = drop_captions(im.convert("RGB").crop((x0 - pad, y0 - pad, x1 + pad, y1 + pad)))
            save(crop, os.path.join(OUT, "coolmax", name))
    for name, (idx, box, blurs) in PUREBREEZE.items():
        with Image.open(os.path.join(src, "pbx", f"i-{idx:03d}.jpg")) as im:
            im = im.convert("RGB")
            for b in blurs:
                im.paste(im.crop(b).filter(ImageFilter.GaussianBlur(14)), b[:2])
            save(im.crop(box), os.path.join(OUT, "purebreeze", name))


if __name__ == "__main__":
    main(sys.argv[1])

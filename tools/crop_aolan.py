"""Crop Aolan product photos from the catalogue PDF.

Usage: pdftoppm -r 220 -png catalogue.pdf <dir>/h ; python3 crop_aolan.py <dir> <out_dir>
Boxes are in 110-dpi page coordinates (half the 220-dpi render).
"""
import sys
from PIL import Image

BOXES = {
    # name: (page, x0, y0, x1, y1)
    "cover": (1, 920, 378, 1845, 835),
    "factory": (3, 0, 0, 1845, 500),
    "cooling-pad": (5, 240, 135, 490, 330),
    "principle": (5, 1140, 140, 1560, 440),
    "azl001-zc12ar": (6, 1065, 135, 1305, 390),
    "azl001-zc12ar-app": (6, 1045, 790, 1715, 1105),
    "azl010-ly13a": (7, 170, 125, 300, 392),
    "azl010-ly13a-app": (7, 130, 788, 805, 1105),
    "azl010-ly13b": (7, 1075, 125, 1200, 392),
    "azl010-ly13b-app": (7, 1045, 788, 1715, 1105),
    "azl012-ly13a": (8, 155, 95, 335, 392),
    "azl012-ly13a-app": (8, 130, 788, 805, 1105),
    "azl045-zy13a": (8, 1050, 90, 1230, 392),
    "azl045-zy13a-app": (8, 1045, 788, 1715, 1105),
    "azl035-ly13f": (9, 170, 95, 320, 392),
    "azl035-ly13f-app": (9, 130, 788, 805, 1105),
    "azl035-ly13g": (9, 1095, 90, 1225, 400),
    "azl035-ly13g-app": (9, 1045, 788, 1715, 1105),
    "azl06-zy13f": (10, 170, 95, 345, 395),
    "azl06-zy13f-app": (10, 120, 788, 805, 1105),
    "azl06-zy13g": (10, 1065, 95, 1240, 395),
    "azl06-zy13g-app": (10, 1045, 788, 1715, 1105),
    "azl08-zy13b": (11, 170, 95, 315, 395),
    "azl08-zy13b-app": (11, 130, 788, 805, 1105),
    "azl-180": (11, 1125, 85, 1330, 410),
    "azl-180-app": (11, 1045, 820, 1715, 1140),
    "azl-300": (12, 140, 105, 385, 405),
    "azl-300-app": (12, 145, 790, 800, 1110),
    "azl06-zc13a": (12, 1125, 95, 1315, 290),
    "azl06-zc13b": (12, 1130, 635, 1355, 850),
    "azl03-zc10az": (13, 140, 110, 370, 310),
    "azl06-zc10bd": (13, 185, 655, 415, 862),
    "azl06-zy10gd": (13, 1255, 125, 1530, 340),
    "wind-marshal": (14, 120, 175, 295, 345),
    "wind-marshal-row": (14, 120, 175, 835, 345),
    "wind-marshal-app": (14, 1240, 690, 1725, 1135),
    "wind-supremo": (15, 120, 170, 300, 345),
    "wind-supremo-row": (15, 120, 170, 850, 345),
    "wind-supremo-app": (15, 1240, 708, 1725, 1150),
    "wind-supremo-detail": (15, 1050, 315, 1710, 612),
    "dc-brushless": (16, 135, 165, 330, 335),
    "dc-brushless-row": (16, 135, 150, 790, 340),
    "dc-brushless-app": (16, 1240, 690, 1725, 1135),
    "wind-auramo": (17, 130, 155, 335, 370),
    "wind-auramo-row": (17, 130, 150, 810, 370),
    "wind-auramo-app": (17, 1240, 690, 1725, 1150),
    "wind-domination": (18, 140, 155, 330, 355),
    "wind-domination-row": (18, 140, 155, 810, 355),
    "wind-domination-app": (18, 1240, 690, 1725, 1135),
    "wind-superior": (19, 205, 148, 445, 385),
    "wind-superior-row": (19, 205, 148, 760, 385),
    "wind-emperor": (19, 1180, 160, 1525, 390),
    "group-control": (20, 130, 270, 820, 1060),
    "accessories": (20, 1060, 180, 1720, 1100),
    "extraction-fan": (21, 1035, 200, 1400, 375),
    "extraction-fan-app": (21, 125, 550, 810, 990),
    "projects-1": (23, 115, 230, 810, 1120),
    "projects-2": (23, 1040, 230, 1730, 1120),
}

src, out = sys.argv[1], sys.argv[2]
for name, (p, x0, y0, x1, y1) in BOXES.items():
    im = Image.open(f"{src}/h-{p:02d}.png").convert("RGB")
    c = im.crop((x0 * 2, y0 * 2, x1 * 2, y1 * 2))
    c.thumbnail((1400, 1400))
    c.save(f"{out}/{name}.webp", "WEBP", quality=80, method=6)
    print(name, c.size)

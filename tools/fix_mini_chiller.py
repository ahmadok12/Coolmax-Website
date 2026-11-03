"""Hand-fix two Mini Chiller cutouts the automatic BiRefNet cut (tools/cutout_bg.py) got wrong (run once; output is committed).

- mini-chiller-ceiling: the indoor ceiling unit is white on a white/grey wall, so the model tore its edges,
  dropped the right third and kept a loose piece of the blue arc. The unit is a plain rounded box, so it is cut
  here with a drawn mask (a rounded rectangle traced from the edges in the photo) from the untouched original.
- mini-chiller: a light strip of wall was left along the right side of the tall indoor unit; it is cleared.

Usage: python3 tools/fix_mini_chiller.py <original mini-chiller-ceiling image>
(the original is in git: `git show e87b18f:site/assets/img/aolan/mini-chiller-ceiling.webp`)
"""
import os
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFilter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = os.path.join(ROOT, "site", "assets", "img", "aolan")
SS = 4  # supersampling for a smooth anti-aliased mask edge


def save(out, name):
    out.save(os.path.join(IMG, name + ".webp"), "WEBP", quality=90, alpha_quality=90, method=6)
    sm = out.copy()
    sm.thumbnail((720, 720))
    sm.save(os.path.join(IMG, name + "-sm.webp"), "WEBP", quality=82, alpha_quality=85, method=6)
    print("wrote", name, out.size)


def ceiling(src):
    photo = Image.open(src).convert("RGB")
    w, h = photo.size  # 460 x 310
    # Unit outline traced from the photo: top edge ~y 11 (slight tilt to ~13 on the right), left x 4,
    # bottom of the cabinet lip ~y 296, right side runs to the edge of the photo.
    mask = Image.new("L", (w * SS, h * SS), 0)
    ImageDraw.Draw(mask).rounded_rectangle(
        (4.5 * SS, 11.5 * SS, (w + 20) * SS, 296 * SS), radius=9 * SS, fill=255)
    mask = mask.rotate(-0.3, resample=Image.BICUBIC, center=(0, 11.5 * SS))
    mask = mask.resize((w, h), Image.LANCZOS).filter(ImageFilter.GaussianBlur(0.4))
    out = photo.convert("RGBA")
    out.putalpha(mask)
    # Trim to the unit with a small transparent margin.
    pad = 8
    canvas = Image.new("RGBA", (w + 2 * pad, h + 2 * pad), (0, 0, 0, 0))
    canvas.alpha_composite(out, (pad, pad))
    box = canvas.getchannel("A").point(lambda v: 255 if v > 10 else 0).getbbox()
    canvas = canvas.crop((box[0] - pad, box[1] - pad, box[2] + pad, box[3] + pad))
    # The source is small (460 px); a 2x Lanczos upscale keeps it sharp next to the other gallery photos.
    big = canvas.resize((canvas.width * 2, canvas.height * 2), Image.LANCZOS)
    save(big, "mini-chiller-ceiling")


def main_photo():
    path = os.path.join(IMG, "mini-chiller.webp")
    im = np.asarray(Image.open(path).convert("RGBA")).copy()
    a = im[..., 3]
    r = im[..., 0].astype(int)
    # Light wall pixels kept to the right of the tall unit's grey side panel.
    region = np.zeros(a.shape, bool)
    region[150:1050, 1334:] = True
    a[region & (r > 195)] = 0
    im[..., 3] = a
    out = Image.fromarray(im, "RGBA")
    save(out, "mini-chiller")  # same size, so the page width/height attributes still match


if __name__ == "__main__":
    ceiling(sys.argv[1])
    main_photo()

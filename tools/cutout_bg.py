"""Remove the white/studio backgrounds from product photos (run once; output is committed).

Usage:
  pip install rembg
  python3 tools/cutout_bg.py mask  <cache dir> [names...]   # run the BiRefNet model, save one mask per photo
  python3 tools/cutout_bg.py apply <cache dir> [names...]   # cut, trim and write transparent .webp + -sm.webp

The masks step is slow (BiRefNet, about 30 s and up to 14 GB RAM per photo on CPU), so it is split from
`apply`, which only reads the cached masks. Photos that show a scene (applications, project cases,
factories, diagrams, lifestyle) are skipped and keep their backgrounds.
Originals are copied to <cache dir>/orig the first time, so re-running `apply` never cuts an already cut photo.
After `apply`, run tools/build.py so the width/height attributes in the pages match the trimmed photos.
"""
import os
import shutil
import sys

import numpy as np
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = os.path.join(ROOT, "site", "assets", "img")
FOLDERS = ("aolan", "coolmax", "purebreeze")

# Scene photos: keep their backgrounds.
SKIP = {
    "aolan/accessories", "aolan/cover", "aolan/factory", "aolan/factory-m", "aolan/hero-bg", "aolan/hero-bg-m",
    "aolan/group-control", "aolan/mini-chiller-cases", "aolan/mini-chiller-cases-m", "aolan/mini-chiller-principle",
    "aolan/principle", "aolan/projects-1", "aolan/projects-2", "aolan/wind-supremo-detail",
    "coolmax/lifestyle",
}


def all_names():
    out = []
    for folder in FOLDERS:
        for f in sorted(os.listdir(os.path.join(IMG, folder))):
            if f.endswith(".webp") and not f.endswith("-sm.webp"):
                name = f"{folder}/{f[:-5]}"
                if name not in SKIP and not name.endswith("-app"):
                    out.append(name)
    return out


def original(cache, name):
    """The untouched photo, copied into the cache before the first cut."""
    dst = os.path.join(cache, "orig", name + ".webp")
    if not os.path.exists(dst):
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy2(os.path.join(IMG, name + ".webp"), dst)
    return dst


def make_masks(cache, names):
    import onnxruntime as ort
    from rembg import new_session, remove

    opts = ort.SessionOptions()
    opts.enable_cpu_mem_arena = False
    session = new_session("birefnet-general", sess_opts=opts)
    for name in names:
        dst = os.path.join(cache, "mask", name + ".png")
        if os.path.exists(dst):
            continue
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        with Image.open(original(cache, name)) as im:
            remove(im.convert("RGB"), session=session, only_mask=True).save(dst)
        print("mask", name, flush=True)


def cut(photo, mask):
    """Photo + soft mask -> RGBA trimmed to the product with a small margin."""
    rgb = np.asarray(photo.convert("RGB")).astype(np.float32)
    a = np.asarray(mask.convert("L").resize(photo.size, Image.LANCZOS)).astype(np.float32) / 255
    # Firm up the matte: near-solid stays solid, faint haze goes.
    a = np.clip((a - 0.08) / 0.84, 0, 1)
    # Undo the white fringe on soft edges (photo was shot on white): c = (p - (1 - a) * 255) / a
    safe = np.maximum(a, 0.25)[..., None]
    rgb = np.where(a[..., None] < 0.98, np.clip((rgb - (1 - safe) * 255) / safe, 0, 255), rgb)
    out = Image.fromarray(np.dstack([rgb, a * 255]).astype(np.uint8), "RGBA")
    box = Image.fromarray((a > 0.1).astype(np.uint8) * 255).getbbox()
    if box:
        pad = round(max(box[2] - box[0], box[3] - box[1]) * 0.03)
        out = out.crop((box[0] - pad, box[1] - pad, box[2] + pad, box[3] + pad))
    return out


def apply(cache, names):
    for name in names:
        mpath = os.path.join(cache, "mask", name + ".png")
        if not os.path.exists(mpath):
            print("no mask, skipped", name)
            continue
        with Image.open(original(cache, name)) as photo, Image.open(mpath) as mask:
            out = cut(photo, mask)
        out.save(os.path.join(IMG, name + ".webp"), "WEBP", quality=88, alpha_quality=90, method=6)
        sm = out.copy()
        sm.thumbnail((720, 720))
        sm.save(os.path.join(IMG, name + "-sm.webp"), "WEBP", quality=80, alpha_quality=85, method=6)
        print("cut", name, out.size)


if __name__ == "__main__":
    step, cache, names = sys.argv[1], sys.argv[2], sys.argv[3:] or all_names()
    {"mask": make_masks, "apply": apply}[step](cache, names)

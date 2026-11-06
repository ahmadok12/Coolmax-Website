"""Build the cinematic home hero art from the Mini Chiller cutout (run once; output is committed).

Usage:  python3 tools/make_hero_art.py

Writes to site/assets/img/hero/:
  scene.webp / scene-rtl.webp / scene-m.webp   night-blue backdrop with cool haze (no product)
  mini-chiller-lit.webp / -sm.webp             the Mini Chiller pair with a blue glow, cold mist and a floor reflection,
                                               on a transparent canvas so it sits on the backdrop at any screen size
"""
import os

import numpy as np
from PIL import Image, ImageFilter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = os.path.join(ROOT, "site", "assets", "img")
OUT = os.path.join(IMG, "hero")
RNG = np.random.default_rng(7)

NAVY = np.array([8, 18, 52], float)        # deep night blue
NAVY_HI = np.array([24, 52, 140], float)   # lifted haze
BLUE = np.array([47, 91, 211], float)      # brand royal blue
ICE = np.array([170, 200, 255], float)     # cold mist


def noise(w, h, scale, octaves=4):
    """Cheap fractal noise in 0..1: random grids upscaled with bicubic and summed."""
    acc = np.zeros((h, w))
    amp, tot = 1.0, 0.0
    for o in range(octaves):
        gw, gh = max(2, int(w / scale * 2 ** o)), max(2, int(h / scale * 2 ** o))
        g = Image.fromarray((RNG.random((gh, gw)) * 255).astype(np.uint8)).resize((w, h), Image.BICUBIC)
        acc += amp * np.asarray(g, float) / 255
        tot += amp
        amp *= 0.5
    return acc / tot


def radial(w, h, cx, cy, rx, ry):
    y, x = np.mgrid[0:h, 0:w]
    d = np.sqrt(((x - cx) / rx) ** 2 + ((y - cy) / ry) ** 2)
    return np.clip(1 - d, 0, 1) ** 2


def scene(w, h, cx, cy):
    """Night backdrop: navy, a soft lift of blue haze around (cx, cy), darker edges, fine grain."""
    n = noise(w, h, w / 3)
    lift = radial(w, h, cx * w, cy * h, w * 0.75, h * 1.1) * (0.55 + 0.45 * n)
    rgb = NAVY[None, None] * (1 - lift[..., None]) + NAVY_HI[None, None] * lift[..., None]
    vign = radial(w, h, w / 2, h / 2, w * 0.95, h * 0.95)
    rgb *= (0.55 + 0.45 * np.clip(vign * 1.6, 0, 1))[..., None]
    rgb += (RNG.random((h, w)) - 0.5)[..., None] * 6
    return Image.fromarray(np.clip(rgb, 0, 255).astype(np.uint8))


def lit_product():
    src = Image.open(os.path.join(IMG, "aolan", "mini-chiller.webp")).convert("RGBA")
    pw, ph = src.size
    W, H = int(pw * 1.7), int(ph * 1.75)
    ox, oy = (W - pw) // 2, int(H * 0.12)
    bottom = np.nonzero(np.asarray(src)[..., 3].max(1) > 40)[0].max()  # last opaque row of the cutout

    # product, graded into the night: slightly cooler, darker towards the floor
    p = np.asarray(src, float)
    grade = np.linspace(1.0, 0.72, ph)[:, None, None]
    p[..., :3] = p[..., :3] * grade * np.array([0.92, 0.96, 1.04])
    p[..., :3] = np.clip(p[..., :3], 0, 255)
    prod = Image.fromarray(p.astype(np.uint8))

    canvas = np.zeros((H, W, 4), float)

    # blue glow behind the units
    g = radial(W, H, W / 2, oy + ph * 0.48, W * 0.5, ph * 0.72)
    canvas[..., :3] = BLUE
    canvas[..., 3] = g * 0.85 * 255

    def over(dst, layer):
        a = layer[..., 3:4] / 255
        da = dst[..., 3:4] / 255
        out_a = a + da * (1 - a)
        rgb = (layer[..., :3] * a + dst[..., :3] * da * (1 - a)) / np.maximum(out_a, 1e-6)
        return np.concatenate([rgb, out_a * 255], -1)

    # contact shadow
    sh = radial(W, H, W / 2, oy + bottom - ph * 0.01, pw * 0.62, ph * 0.035)
    shadow = np.zeros_like(canvas)
    shadow[..., 3] = np.clip(sh * 2.5, 0, 1) * 200
    canvas = over(canvas, shadow)

    # floor reflection: flipped, faded, softened
    refl = prod.transpose(Image.FLIP_TOP_BOTTOM).filter(ImageFilter.GaussianBlur(3))
    r = np.asarray(refl, float)[ph - 1 - bottom:].copy()  # start the mirror at the units' feet
    rh = r.shape[0]
    r[..., 3] *= np.clip(1 - np.linspace(0, 1, rh) / 0.3, 0, 1)[:, None] * 0.18
    r[..., :3] = r[..., :3] * 0.6 + BLUE * 0.4
    layer = np.zeros_like(canvas)
    ry = oy + bottom
    hh = min(rh, H - ry)
    layer[ry:ry + hh, ox:ox + pw] = r[:hh]
    canvas = over(canvas, layer)

    # the product itself
    layer = np.zeros_like(canvas)
    layer[oy:oy + ph, ox:ox + pw] = np.asarray(prod, float)
    canvas = over(canvas, layer)

    # cold mist drifting from the indoor unit's grille (the tall unit on the right of the photo)
    mx, my = ox + pw * 0.71, oy + ph * 0.16
    n = noise(W, H, W / 5, 5)
    plume = radial(W, H, mx - pw * 0.25, my + ph * 0.05, pw * 0.75, ph * 0.32)
    mist = np.clip((n - 0.42) * 2.4, 0, 1) * plume
    m = np.zeros_like(canvas)
    m[..., :3] = ICE
    m[..., 3] = np.clip(mist * 0.55, 0, 1) * 255
    m_img = Image.fromarray(m.astype(np.uint8)).filter(ImageFilter.GaussianBlur(14))
    canvas = over(canvas, np.asarray(m_img, float))

    out = Image.fromarray(np.clip(canvas, 0, 255).astype(np.uint8))
    return out.crop(out.getbbox())


def main():
    os.makedirs(OUT, exist_ok=True)
    s = scene(2400, 1350, 0.7, 0.55)
    s.save(os.path.join(OUT, "scene.webp"), quality=80)
    s.transpose(Image.FLIP_LEFT_RIGHT).save(os.path.join(OUT, "scene-rtl.webp"), quality=80)
    scene(900, 1800, 0.5, 0.72).save(os.path.join(OUT, "scene-m.webp"), quality=80)

    lp = lit_product()
    lp.save(os.path.join(OUT, "mini-chiller-lit.webp"), quality=86)
    sm = lp.resize((lp.width * 900 // lp.width, lp.height * 900 // lp.width), Image.LANCZOS)
    sm.save(os.path.join(OUT, "mini-chiller-lit-sm.webp"), quality=84)
    print("hero art:", lp.size, sm.size)


if __name__ == "__main__":
    main()

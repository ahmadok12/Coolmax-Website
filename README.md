# Coolmax Wholesale website (English + Arabic)

Static, SEO-ready website for wholesale evaporative air coolers. No framework and no server code:
`site/` is the finished website, `tools/` is the generator that writes it.

## Edit and rebuild
1. Business details (name, domain, WhatsApp, email, address, optional form endpoint): `tools/data_site.py` → `SITE`.
   All UI text in English and Arabic is in the same file (`T`).
2. Aolan products and specs: `tools/data_aolan.py` (transcribed from the 2026 Aolan catalogue).
3. Coolmax and the demo third brand ("DuneFrost"): `PLACEHOLDER_BRANDS` in `tools/data_site.py`.
   These pages are `noindex` until real catalogues are added.
4. Rebuild: `pip install pillow` once, then `python3 tools/build.py`.
5. Product photos were cropped from the catalogue PDF with `tools/crop_aolan.py`.

## 3D cooler viewer
`site/3d/` is a hand-made interactive 3D page for the Coolmax CM-18 top-discharge cooler (three.js + `coolmax_cm18.glb`).
The build script does not touch it. The CM-18/CM-30 product pages and the home page link to it ("Explore in 3D").
The Blender model and page source live outside this repo in the "Coolmax 3D Viewer" folder; run `make_outputs.py` there
to refresh `site/3d/`.

## Publish
Currently hosted on GitHub Pages: every push to `main` runs `.github/workflows/pages.yml`, which deploys the `site/` folder
to https://ahmadok12.github.io/Coolmax-Website/ (rebuild with `python3 tools/build.py` and commit `site/` first).

Other hosts:
Upload the `site/` folder to any static host (Netlify, Cloudflare Pages, Vercel, or cPanel `public_html`).
Then set `SITE["url"]` to the real domain, rebuild, and submit `sitemap.xml` in Google Search Console.

## Language behaviour
- `/` sends visitors to `/ar/` when the browser language is Arabic or the device time zone is in the Gulf / Arab world
  (Riyadh, Dubai, Doha, Kuwait, Muscat, Bahrain, Baghdad, Cairo...). Everyone else, including Pakistan, gets `/en/`.
- English pages do the same redirect for Middle East visitors who have not chosen a language yet.
- The English / العربية switch in the header remembers the visitor's choice, so detection never overrides it.
- Arabic pages use `dir="rtl"`, Arabic fonts (IBM Plex Sans Arabic) and Gulf search terms such as "مكيف صحراوي".

## SEO included
Per-page titles and descriptions in both languages, canonical + hreflang (en, ar, x-default), Open Graph images,
JSON-LD (Organization, WebSite, FAQPage, Product, BreadcrumbList, ItemList), `sitemap.xml` with language alternates,
`robots.txt`, semantic HTML, compressed WebP images with fixed dimensions and lazy loading.

## Inquiry form
With `form_endpoint` empty, the form opens WhatsApp with the inquiry pre-written (works on any host).
To receive inquiries by email instead, create a free Formspree form and paste its URL into `form_endpoint`.

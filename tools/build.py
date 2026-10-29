"""Static site generator for the Coolmax Wholesale website (English + Arabic).

Run:  python3 tools/build.py
Output goes to ./site — upload that folder to any static host (Netlify, Cloudflare Pages, cPanel...).
"""
import html
import json
import os
import re
import shutil
from datetime import date

from PIL import Image

from data_aolan import BRAND as AOLAN, CATEGORIES, PRODUCTS, SUPPLY_AIR
from data_site import MARKETS, PLACEHOLDER_BRANDS, SITE, SPEC_LABELS, T, VALUE_AR

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "site")
IMG = "assets/img/aolan"
LANGS = ["en", "ar"]
TODAY = date.today().isoformat()
# Path prefix when the site lives in a sub-folder (e.g. GitHub Pages project sites); "" on a root domain.
BASE = __import__("urllib.parse").parse.urlparse(SITE["url"]).path.rstrip("/")

ME_TIMEZONES = [
    "Asia/Riyadh", "Asia/Dubai", "Asia/Qatar", "Asia/Kuwait", "Asia/Bahrain", "Asia/Muscat", "Asia/Baghdad",
    "Asia/Amman", "Asia/Beirut", "Asia/Damascus", "Asia/Aden", "Asia/Gaza", "Asia/Hebron", "Africa/Cairo",
    "Africa/Tripoli", "Africa/Khartoum", "Africa/Algiers", "Africa/Tunis", "Africa/Casablanca", "Africa/Nouakchott",
]

CATEGORY_IMAGE = {"chiller": "mini-chiller", "industrial": "wind-domination", "outdoor": "azl-300", "home": "azl045-zy13a", "ventilation": "extraction-fan"}

CALC_OPTIONS = [
    ("wind-supremo", "Aolan Wind Supremo", 18000),
    ("wind-domination", "Aolan Wind Domination AZL30", 30000),
    ("wind-superior", "Aolan Wind Superior AZL50", 50000),
    ("azl-300", "Aolan AZL-300 (portable)", 30000),
    ("azl-180", "Aolan AZL-180 (portable)", 18000),
    ("azl08-azl12-zy13b", "Aolan AZL12-ZY13B (portable)", 12000),
]

SITEMAP = []  # (en_path, ar_path)
_size_cache = {}


# ---------------------------------------------------------------- helpers
def esc(s):
    return html.escape(str(s), quote=True)


def L(v, lang):
    return v.get(lang, v.get("en")) if isinstance(v, dict) else v


def t(key, lang, **kw):
    s = T[key][lang].replace("[[", "").replace("]]", "")
    return s.format(**kw) if kw else s


def hx(key, lang):
    """Heading text with [[accent]] words wrapped for the two-tone heading style."""
    return T[key][lang].replace("[[", '<span class="acc">').replace("]]", "</span>")


def sec_head(eyebrow, title, lead="", tag="h2"):
    lead_html = f'<p class="sub">{lead}</p>' if lead else ""
    return f"""<div class="sec-head"><span class="eyebrow">{eyebrow}</span><div><{tag} class="h2">{title}</{tag}>{lead_html}</div></div>"""


_VALUE_KEYS = sorted(VALUE_AR, key=len, reverse=True)


def tr_value(v, lang):
    v = L(v, lang)
    if lang != "ar":
        return v
    for k in _VALUE_KEYS:
        v = re.sub(r"(?<![A-Za-z])" + re.escape(k) + r"(?![A-Za-z])", VALUE_AR[k], v)
    return v.replace(", ", "، ")


def href(cur, target):
    rel = os.path.relpath(target, os.path.dirname(cur) or ".")
    return rel.replace(os.sep, "/")


def abs_url(path):
    path = path[: -len("index.html")] if path.endswith("index.html") else path
    return f"{SITE['url']}/{path}"


def other(lang):
    return "ar" if lang == "en" else "en"


def swap_lang(path, lang):
    return other(lang) + path[len(lang):]


def img_size(rel):
    if rel not in _size_cache:
        with Image.open(os.path.join(OUT, rel)) as im:
            _size_cache[rel] = im.size
    return _size_cache[rel]


def img(cur, name, alt, small=False, eager=False, cls=""):
    rel = f"{IMG}/{name}{'-sm' if small else ''}.webp"
    w, h = img_size(rel)
    loading = 'fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'
    c = f' class="{cls}"' if cls else ""
    return f'<img src="{href(cur, rel)}" alt="{esc(alt)}" width="{w}" height="{h}" {loading}{c}>'


def wa_link(text=""):
    from urllib.parse import quote

    return f"https://wa.me/{SITE['whatsapp']}" + (f"?text={quote(text)}" if text else "")


def first_num(s):
    m = re.search(r"\d[\d,]*\.?\d*", s)
    return float(m.group().replace(",", "")) if m else None


def spec(p, key):
    for k, vals in p.get("specs", []):
        if k == key:
            return vals
    return None


def airflow_range(p):
    vals = spec(p, "airflow")
    if not vals and p.get("table"):
        vals = [r[5] for r in p["table"]["rows"]]
    nums = [first_num(v) for v in vals or [] if first_num(v)]
    if not nums:
        return ""
    lo, hi = int(min(nums)), int(max(nums))
    return f"{lo:,}" if lo == hi else f"{lo:,}–{hi:,}"


def product_path(lang, p):
    return f"{lang}/brands/aolan/{p['slug']}.html"


def ld(obj):
    return f'<script type="application/ld+json">{json.dumps(obj, ensure_ascii=False)}</script>'


ICON = {
    "check": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20 6 9 17l-5-5" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "arrow": '<svg class="flip" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "wa": '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2Zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.7.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.2-.4.2-.4.7-1.3a.5.5 0 0 0 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.8 11.9 11.9 0 0 0 4.6 4c1.7.7 2.4.8 3.2.7a2.8 2.8 0 0 0 1.8-1.3 2.3 2.3 0 0 0 .2-1.3c-.1-.1-.3-.2-.5-.3Z"/></svg>',
    "ne": '<svg class="flip" viewBox="0 0 24 24" aria-hidden="true"><path d="M7 17 17 7M8 7h9v9" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "down": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 5v14M6 13l6 6 6-6" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "phone": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg>',
    "c1": '<svg viewBox="0 0 48 48" aria-hidden="true"><path d="M26 4 10 28h13l-3 16 18-26H25l1-14Z" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/></svg>',
    "c2": '<svg viewBox="0 0 48 48" aria-hidden="true"><path d="M6 16c8-6 14 6 22 0s14-6 14-6M6 26c8-6 14 6 22 0s14-6 14-6M6 36c8-6 14 6 22 0s14-6 14-6" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>',
    "c3": '<svg viewBox="0 0 48 48" aria-hidden="true"><circle cx="24" cy="24" r="8" fill="none" stroke="currentColor" stroke-width="2"/><path d="M24 4v6M24 38v6M4 24h6M38 24h6M10 10l4 4M34 34l4 4M10 38l4-4M34 14l4-4" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>',
    "c4": '<svg viewBox="0 0 48 48" aria-hidden="true"><ellipse cx="20" cy="14" rx="12" ry="5" fill="none" stroke="currentColor" stroke-width="2"/><path d="M8 14v10c0 3 5 5 12 5s12-2 12-5V14M8 24v10c0 3 5 5 12 5 3 0 6-.5 8-1.3" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="36" cy="34" r="7" fill="none" stroke="currentColor" stroke-width="2"/></svg>',
    "logo": '<svg viewBox="0 0 40 40" aria-hidden="true"><circle cx="20" cy="20" r="19" fill="#c79a55"/><g stroke="#161616" stroke-width="2.6" stroke-linecap="round" fill="none"><path d="M20 8v24M9.6 14l20.8 12M9.6 26l20.8-12"/><path d="M16.5 9.5 20 13l3.5-3.5M16.5 30.5 20 27l3.5 3.5"/></g></svg>',
}


# ---------------------------------------------------------------- layout
def header(cur, lang):
    home = href(cur, f"{lang}/index.html")
    brand_links = [(f"{lang}/brands/aolan/index.html", "Aolan")] + [
        (f"{lang}/brands/{b['slug']}/index.html", b["name"]) for b in PLACEHOLDER_BRANDS
    ]
    brands = "".join(f'<a href="{href(cur, p)}">{esc(n)}</a>' for p, n in brand_links)
    calc = href(cur, f"{lang}/cooler-sizing-calculator.html")
    contact = href(cur, f"{lang}/wholesale-inquiry.html")
    alt = href(cur, swap_lang(cur, lang))
    o = other(lang)
    nav = (
        f'<a href="{home}">{t("nav_home", lang)}</a>'
        f'<details class="dd"><summary>{t("nav_brands", lang)}</summary><div class="dd-menu">{brands}</div></details>'
        f'<a href="{calc}">{t("nav_calc", lang)}</a><a href="{contact}">{t("nav_contact", lang)}</a>'
    )
    return f"""<a class="skip" href="#main">{t('skip', lang)}</a>
<header class="site-header">
  <div id="geo-banner" class="geo-banner" hidden><span lang="{o}">{t('geo_banner', lang)}</span> <a href="{alt}" lang="{o}" data-setlang="{o}">{t('geo_banner_btn', lang)}</a><button type="button" class="geo-x" aria-label="Close">×</button></div>
  <div class="wrap header-in">
    <a class="logo" href="{home}">{ICON['logo']}<span>{esc(L(SITE['name'], lang))}</span></a>
    <nav class="main-nav" aria-label="Main">{nav}</nav>
    <a class="hdr-phone" href="{wa_link()}" rel="noopener"><span class="hdr-ico">{ICON['phone']}</span><span><small>{t('call_us', lang)}</small><b dir="ltr">{esc(SITE['phone_display'])}</b></span></a>
    <a class="lang-switch" href="{alt}" hreflang="{o}" lang="{o}" data-setlang="{o}" title="{esc(t('lang_switch_label', lang))}">{t('lang_switch', lang)}</a>
    <a class="btn btn-gold hdr-cta" href="{contact}">{t('cta_quote', lang)}</a>
    <details class="mnav"><summary aria-label="{t('menu', lang)}"><span></span><span></span><span></span></summary>
      <div class="mnav-panel"><a href="{home}">{t('nav_home', lang)}</a>{brands}<a href="{calc}">{t('nav_calc', lang)}</a><a href="{contact}">{t('nav_contact', lang)}</a></div>
    </details>
  </div>
</header>"""


def footer(cur, lang):
    brand_links = [(f"{lang}/brands/aolan/index.html", "Aolan")] + [
        (f"{lang}/brands/{b['slug']}/index.html", b["name"]) for b in PLACEHOLDER_BRANDS
    ]
    brands = "".join(f'<li><a href="{href(cur, p)}">{esc(n)}</a></li>' for p, n in brand_links)
    cats = "".join(
        f'<li><a href="{href(cur, f"{lang}/brands/aolan/index.html")}#{c["slug"]}">{esc(c[lang])}</a></li>' for c in CATEGORIES
    )
    markets = " · ".join(L(n, lang) for _, n in MARKETS)
    return f"""<footer class="site-footer">
  <div class="wrap footer-grid">
    <div><a class="logo logo-light" href="{href(cur, f'{lang}/index.html')}">{ICON['logo']}<span>{esc(L(SITE['name'], lang))}</span></a>
      <p>{t('footer_about', lang)}</p><p class="muted-light">{esc(markets)}</p></div>
    <div><h2>{t('nav_brands', lang)}</h2><ul>{brands}</ul></div>
    <div><h2>{t('cats_title', lang)}</h2><ul>{cats}</ul></div>
    <div><h2>{t('nav_contact', lang)}</h2><ul>
      <li><a href="{wa_link()}" rel="noopener">WhatsApp <span dir="ltr">{esc(SITE['phone_display'])}</span></a></li>
      <li><a href="mailto:{SITE['email']}">{esc(SITE['email'])}</a></li>
      <li>{esc(L(SITE['address'], lang))}</li>
      <li><a href="{href(cur, f'{lang}/cooler-sizing-calculator.html')}">{t('nav_calc', lang)}</a></li></ul></div>
  </div>
  <div class="footer-wm" aria-hidden="true">{esc(L(SITE['name'], lang)).split()[0]}</div>
  <div class="wrap footer-bottom">© 2026 {esc(L(SITE['name'], lang))}. {t('footer_rights', lang)}</div>
</footer>
<a class="wa-float" href="{wa_link()}" rel="noopener" aria-label="WhatsApp">{ICON['wa']}</a>"""


def page(cur, lang, title, desc, body, schema=(), noindex=False, og_image="assets/img/og.jpg", has_alt=True):
    alt_path = swap_lang(cur, lang)
    fonts = (
        "family=Urbanist:wght@400;500;600;700;800"
        if lang == "en"
        else "family=IBM+Plex+Sans+Arabic:wght@400;500;600;700&family=Urbanist:wght@600;700;800"
    )
    en_path, ar_path = (cur, alt_path) if lang == "en" else (alt_path, cur)
    x_default = "" if cur.endswith("/index.html") and cur.count("/") == 1 else en_path
    alternates = ""
    if has_alt:
        alternates = (
            f'<link rel="alternate" hreflang="en" href="{abs_url(en_path)}">'
            f'<link rel="alternate" hreflang="ar" href="{abs_url(ar_path)}">'
            f'<link rel="alternate" hreflang="x-default" href="{abs_url(x_default)}">'
        )
    if not noindex:
        SITEMAP.append((en_path, ar_path)) if lang == "en" else None
    robots = '<meta name="robots" content="noindex, follow">' if noindex else ""
    redirect = ""
    if lang == "en":
        # Middle East visitors (Arabic browser or Gulf/Arab time zone) with no saved choice go to the Arabic page.
        redirect = (
            "<script>(function(){try{if(localStorage.getItem('cm_lang'))return}catch(e){return}"
            f"var z={json.dumps(ME_TIMEZONES)},n=(navigator.languages||[navigator.language])[0]||'',tz='';"
            "try{tz=Intl.DateTimeFormat().resolvedOptions().timeZone}catch(e){}"
            f"if(/^ar/i.test(n)||z.indexOf(tz)>-1)location.replace({json.dumps(href(cur, alt_path))}+location.hash)}})()</script>"
        )
    schema_html = "".join(ld(s) for s in schema)
    locale = "en_US" if lang == "en" else "ar_AE"
    return f"""<!doctype html>
<html lang="{lang}" dir="{'rtl' if lang == 'ar' else 'ltr'}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
{redirect}
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{abs_url(cur)}">
{alternates}
{robots}
<meta property="og:type" content="website">
<meta property="og:site_name" content="{esc(L(SITE['name'], lang))}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{abs_url(cur)}">
<meta property="og:image" content="{SITE['url']}/{og_image}">
<meta property="og:locale" content="{locale}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#161616">
<link rel="icon" href="{href(cur, 'assets/favicon.svg')}" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?{fonts}&display=swap">
<link rel="stylesheet" href="{href(cur, 'assets/css/site.css')}">
{schema_html}
</head>
<body data-lang="{lang}" data-wa="{SITE['whatsapp']}" data-form="{esc(SITE['form_endpoint'])}">
{header(cur, lang)}
<main id="main">
{body}
</main>
{footer(cur, lang)}
<script src="{href(cur, 'assets/js/site.js')}" defer></script>
</body>
</html>
"""


def write(path, content):
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)


def breadcrumbs(cur, lang, items):
    """items: list of (path or None, label)."""
    parts = []
    schema = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": []}
    for i, (p, label) in enumerate(items, 1):
        if p:
            parts.append(f'<a href="{href(cur, p)}">{esc(label)}</a>')
        else:
            parts.append(f'<span aria-current="page">{esc(label)}</span>')
        schema["itemListElement"].append(
            {"@type": "ListItem", "position": i, "name": label, **({"item": abs_url(p)} if p else {})}
        )
    return f'<nav class="crumbs" aria-label="Breadcrumb">{" <span>/</span> ".join(parts)}</nav>', schema


# ---------------------------------------------------------------- shared blocks
def product_card(cur, lang, p):
    solar = f'<span class="chip chip-sun">{t("solar_badge", lang)}</span>' if p.get("solar") else ""
    feat = f'<span class="chip">{t("featured_kicker", lang)}</span>' if p.get("featured") else ""
    if p.get("new"):
        feat = f'<span class="chip chip-new">{t("new_badge", lang)}</span>'

    af = airflow_range(p)
    return f"""<a class="pcard" href="{href(cur, product_path(lang, p))}">
  <div class="pcard-img">{img(cur, p['image'], f"Aolan {p['name']}", small=True)}</div>
  <div class="pcard-body">{feat}{solar}<h3>{esc(p['name'])}</h3><p>{esc(L(p['headline'], lang))}</p>
  <p class="pcard-meta"><span>{t('airflow', lang)}</span> <b dir="ltr">{af} m³/h</b></p></div>
</a>"""


def calculator(cur, lang):
    opts = "".join(f'<option value="{v}">{esc(lbl)}</option>' for v, lbl in T["calc_use_opts"][lang])
    models = json.dumps(
        [{"name": n, "airflow": a, "href": href(cur, f"{lang}/brands/aolan/{s}.html")} for s, n, a in CALC_OPTIONS]
    )
    contact = href(cur, f"{lang}/wholesale-inquiry.html")
    return f"""<div class="calc card" data-models='{esc(models)}' data-contact="{contact}">
  <div class="calc-in">
    <label>{t('calc_area', lang)}<input type="number" name="area" min="10" step="10" value="1000" inputmode="numeric"></label>
    <label>{t('calc_height', lang)}<input type="number" name="height" min="2" step="0.5" value="4" inputmode="decimal"></label>
    <label class="span2">{t('calc_use', lang)}<select name="ach">{opts}</select></label>
  </div>
  <div class="calc-out">
    <p class="calc-need">{t('calc_need', lang)}: <b dir="ltr" data-out="need">—</b></p>
    <table class="calc-table"><thead><tr><th>{t('calc_option', lang)}</th><th>{t('airflow', lang)}</th><th>{t('calc_qty', lang)}</th></tr></thead><tbody data-out="rows"></tbody></table>
    <a class="btn btn-primary" data-out="send" href="{contact}">{t('calc_send', lang)} {ICON['arrow']}</a>
    <p class="small muted">{t('calc_note', lang)}</p>
  </div>
  <span hidden data-units="{t('calc_units', lang)}"></span>
</div>"""


def inquiry_form(cur, lang, model="", brand=""):
    countries = "".join(f'<option value="{esc(L(n, "en"))}">{esc(L(n, lang))}</option>' for _, n in MARKETS)
    countries += f'<option value="Other">{t("f_other", lang)}</option>'
    types = "".join(f'<option>{esc(x)}</option>' for x in T["f_types"][lang])
    brands = f'<option value="">{t("f_any", lang)}</option>' + "".join(
        f'<option{" selected" if b.lower() == brand else ""}>{b}</option>'
        for b in ["Aolan", "Coolmax", "DuneFrost"]
    )
    submit = t("f_submit", lang) if SITE["form_endpoint"] else t("f_submit_wa", lang)
    return f"""<form class="inq card" method="post" action="{esc(SITE['form_endpoint'] or '#')}" novalidate>
  <div class="grid2">
    <label>{t('f_name', lang)} *<input name="name" required autocomplete="name"></label>
    <label>{t('f_company', lang)}<input name="company" autocomplete="organization"></label>
    <label>{t('f_country', lang)} *<select name="country" required>{countries}</select></label>
    <label>{t('f_city', lang)}<input name="city"></label>
    <label>{t('f_phone', lang)} *<input name="phone" type="tel" required autocomplete="tel" dir="ltr"></label>
    <label>{t('f_email', lang)}<input name="email" type="email" autocomplete="email" dir="ltr"></label>
    <label>{t('f_type', lang)}<select name="buyer_type">{types}</select></label>
    <label>{t('f_brand', lang)}<select name="brand">{brands}</select></label>
    <label>{t('f_model', lang)}<input name="model" value="{esc(model)}" dir="auto"></label>
    <label>{t('f_qty', lang)}<input name="quantity" inputmode="numeric"></label>
    <label class="span2">{t('f_msg', lang)}<textarea name="message" rows="4" placeholder="{esc(t('f_msg_ph', lang))}"></textarea></label>
  </div>
  <input type="hidden" name="language" value="{lang}">
  <button class="btn btn-primary btn-lg" type="submit">{ICON['wa'] if not SITE['form_endpoint'] else ''}{submit}</button>
  <p class="form-status" role="status" data-ok="{esc(t('f_ok', lang))}" data-err="{esc(t('f_err', lang))}"></p>
</form>"""


def cta_band(cur, lang, title, lead, model="", brand=""):
    from urllib.parse import urlencode

    q = urlencode({k: v for k, v in (("model", model), ("brand", brand)) if v})
    contact = href(cur, f"{lang}/wholesale-inquiry.html") + (f"?{q}" if q else "")
    wa_text = f"{t('cta_quote', lang)}: {brand.title()} {model}".strip() if model else ""
    return f"""<section class="cta-band"><div class="wrap cta-in">
  <div><h2>{title if '<span' in title else esc(title)}</h2><p>{esc(lead)}</p></div>
  <div class="cta-btns"><a class="btn btn-gold" href="{contact}">{t('cta_quote', lang)}</a>
  <a class="btn btn-wa" href="{wa_link(wa_text)}" rel="noopener">{ICON['wa']}{t('cta_whatsapp', lang)}</a></div>
</div></section>"""


def supply_table(lang):
    head = "".join(f"<th>{rh}%</th>" for rh in SUPPLY_AIR["rh"])
    rows = ""
    for amb, vals in SUPPLY_AIR["rows"]:
        cells = "".join(f'<td class="{"hot" if v and amb - v >= 15 else ""}">{v if v else "—"}</td>' for v in vals)
        rows += f"<tr><th scope=\"row\">{amb}°</th>{cells}</tr>"
    return f"""<figure class="supply card"><figcaption><b>{t('supply_title', lang)}</b></figcaption>
<div class="tscroll"><table class="tbl tbl-center" dir="ltr"><thead><tr><th>{t('ambient', lang)} \\ {t('rh', lang)}</th>{head}</tr></thead><tbody>{rows}</tbody></table></div>
<p class="small muted">{t('supply_caption', lang)}</p></figure>"""


# ---------------------------------------------------------------- pages
def build_home(lang):
    cur = f"{lang}/index.html"
    contact = href(cur, f"{lang}/wholesale-inquiry.html")
    aolan_path = f"{lang}/brands/aolan/index.html"
    points = "".join(f"<li>{ICON['check']}{esc(x)}</li>" for x in T["hero_points"][lang])
    feat = next(p for p in PRODUCTS if p.get("featured"))
    newp = next(p for p in PRODUCTS if p.get("new"))
    new_stats = [
        (t("capacity", lang), "25–35 kW"),
        ("COP", "5"),
        (t("energy_saving", lang), "30–50%"),
        (t("airflow", lang), "6,000–7,000 m³/h"),
    ]
    new_stats_html = "".join(f'<div><span>{esc(k)}</span><b dir="auto">{esc(v)}</b></div>' for k, v in new_stats)
    new_spot = f"""<section class="sec new-spot"><div class="wrap feature">
  <div><span class="chip chip-new">{t('new_kicker', lang)}</span>
  <h2 class="h2"><span dir="ltr">Aolan Mini Chiller</span></h2>
  <p class="lead">{t('new_lead', lang)}</p>
  <div class="kv">{new_stats_html}</div>
  <div class="btns"><a class="btn btn-primary" href="{href(cur, product_path(lang, newp))}">{t('featured_cta', lang)} {ICON['arrow']}</a>
  <a class="btn btn-ghost" href="{contact}?model=Mini%20Chiller&amp;brand=aolan">{t('cta_quote', lang)}</a></div></div>
  <div class="feature-media">{img(cur, 'mini-chiller', 'Aolan Mini Chiller indoor and outdoor units', small=True)}</div>
</div></section>"""

    stats = [
        ("3", {"en": "Brands", "ar": "علامات تجارية"}),
        (f"{len(PRODUCTS)}+", {"en": "Model families", "ar": "فئة موديلات"}),
        ("80,000", {"en": "m³/h top airflow", "ar": "م³/ساعة أعلى تدفق هواء"}),
        (str(len(MARKETS)), {"en": "Core markets", "ar": "أسواق رئيسية"}),
    ]
    stats_html = "".join(f'<div><b dir="ltr">{n}</b><span>{L(l, lang)}</span></div>' for n, l in stats)

    # brand cards
    cards = f"""<a class="bcard" href="{href(cur, aolan_path)}">
  <div class="bcard-img">{img(cur, 'wind-supremo-row', 'Aolan industrial air coolers', small=True)}</div>
  <div class="bcard-body"><span class="chip chip-ok">{t('models_count', lang, n=len(PRODUCTS))}</span><h3>Aolan</h3>
  <p>{esc(L(AOLAN['tagline'], lang))}</p><span class="link">{t('view_range', lang)} {ICON['arrow']}</span></div></a>"""
    for b in PLACEHOLDER_BRANDS:
        badge = L(b["badge"], lang) if b.get("badge") else t("soon", lang)
        cards += f"""<a class="bcard bcard-{b['slug']}" href="{href(cur, f"{lang}/brands/{b['slug']}/index.html")}">
  <div class="bcard-img bcard-ph"><span>{esc(b['name'])}</span></div>
  <div class="bcard-body"><span class="chip{' chip-new' if b.get('badge') else ''}">{esc(badge)}</span><h3>{esc(b['name'])}</h3>
  <p>{esc(L(b['tagline'], lang))}</p><span class="link">{t('view_range', lang)} {ICON['arrow']}</span></div></a>"""

    cats = "".join(
        f"""<a class="ccard" href="{href(cur, aolan_path)}#{c['slug']}">{img(cur, CATEGORY_IMAGE[c['slug']], c[lang], small=True)}
<div><h3>{esc(c[lang])}</h3><p>{esc(L(c['desc'], lang))}</p></div></a>"""
        for c in CATEGORIES if c["slug"] != "chiller"
    )
    why = "".join(f"<div class=\"why\"><h3>{esc(h)}</h3><p>{esc(d)}</p></div>" for h, d in T["why_points"][lang])
    markets = "".join(f'<li><span class="flag">{code}</span>{esc(L(n, lang))}</li>' for code, n in MARKETS)
    steps = "".join(
        f'<li><span class="step-n">{i}</span><h3>{esc(h)}</h3><p>{esc(d)}</p></li>' for i, (h, d) in enumerate(T["process"][lang], 1)
    )
    faq = "".join(f"<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>" for q, a in T["faq"][lang])

    feat_stats = [
        (t("airflow", lang), "18,000 m³/h"),
        (t("power", lang), "1.1 kW"),
        (t("coverage", lang), feat["area"]),
        (t("loading", lang), {"en": "40 assembled · 70 SKD", "ar": "40 مجمّعة · 70 SKD"}),
    ]
    feat_stats_html = "".join(f"<div><span>{esc(k)}</span><b dir=\"auto\">{esc(L(v, lang))}</b></div>" for k, v in feat_stats)

    why_cards = "".join(
        f'<div class="icard"><div class="icard-top"><h3>{esc(h)}</h3><span class="icard-ico">{ICON["c" + str(i)]}</span></div><p>{esc(d)}</p></div>'
        for i, (h, d) in enumerate(T["why_points"][lang], 1)
    )
    svc_items = ""
    for i, c in enumerate(CATEGORIES, 1):
        im = f"{IMG}/{CATEGORY_IMAGE[c['slug']]}-sm.webp"
        svc_items += (
            f'<li><a href="{href(cur, aolan_path)}#{c["slug"]}" data-img="{href(cur, im)}" data-desc="{esc(L(c["desc"], lang))}">'
            f'<span class="svc-n">0{i}</span><span class="svc-t">{esc(c[lang])}</span><span class="svc-a">{ICON["ne"]}</span></a></li>'
        )
    first_cat = CATEGORIES[0]
    step_imgs = ["azl-180-app", "wind-supremo-detail", "projects-2", "projects-1"]
    steps = "".join(
        f'<li class="pstep">{img(cur, step_imgs[i - 1], "", small=True)}<div><h3><span class="acc">{i:02d}.</span> {esc(h)}</h3><p>{esc(d)}</p></div><span class="pstep-n" aria-hidden="true">{i:02d}</span></li>'
        for i, (h, d) in enumerate(T["process"][lang], 1)
    )
    new_ticks = "".join(f"<li>{ICON['check']}{esc(x.split(':')[0])}</li>" for x in newp["bullets"][lang][:4])
    wm = esc(L(SITE["name"], lang)).split()[0]

    body = f"""
<section class="hero hero-bg">
  <div class="wrap hero-in">
    <div class="hero-copy">
      <span class="eyebrow eyebrow-light">{t('hero_kicker', lang)}</span>
      <h1>{hx('hero_title', lang)}</h1>
      <p class="lead">{t('hero_lead', lang)}</p>
      <div class="btns"><a class="btn btn-pill" href="{contact}">{t('cta_quote', lang)}<span class="btn-dot">{ICON['ne']}</span></a>
      <a class="btn btn-wa" href="{wa_link()}" rel="noopener">{ICON['wa']}{t('cta_whatsapp', lang)}</a></div>
    </div>
    <div class="hero-side">
      <div class="glass"><b dir="ltr">{len(PRODUCTS)}+</b><span>{t('hero_card', lang)}</span>
        <ul>{''.join(f'<li>{esc(x)}</li>' for x in T['hero_points'][lang])}</ul></div>
      <a class="hero-thumb" href="{href(cur, product_path(lang, newp))}">{img(cur, 'mini-chiller', 'Aolan Mini Chiller', small=True)}<span class="chip chip-new">{t('new_badge', lang)}</span></a>
    </div>
  </div>
  <a class="scroll-dot" href="#why" aria-label="{t('scroll', lang)}">{ICON['down']}</a>
</section>

<section class="sec" id="why"><div class="wrap">
  {sec_head(t('eb_why', lang), hx('why_title', lang), t('why_lead', lang))}
  <div class="grid4 icards">{why_cards}</div>
</div></section>

<section class="dband"><div class="wrap dband-in">
  <div class="dband-copy">
    <span class="eyebrow eyebrow-light">{t('new_kicker', lang)}</span>
    <h2 class="h2">Aolan <span class="acc">Mini Chiller</span></h2>
    <ul class="ticks ticks-2">{new_ticks}</ul>
    <p>{t('new_lead', lang)}</p>
    <div class="kv kv-dark">{new_stats_html}</div>
    <div class="btns"><a class="btn btn-pill btn-pill-light" href="{href(cur, product_path(lang, newp))}">{t('featured_cta', lang)}<span class="btn-dot">{ICON['ne']}</span></a></div>
  </div>
  <div class="dband-media">{img(cur, 'mini-chiller', 'Aolan Mini Chiller indoor and outdoor units', small=True)}</div>
  <div class="wm wm-dark" aria-hidden="true">2026</div>
</div></section>

<section class="sec"><div class="wrap">
  {sec_head(t('eb_range', lang), hx('cats_title', lang), t('range_lead', lang))}
  <div class="svc">
    <figure class="svc-media">{img(cur, CATEGORY_IMAGE[first_cat['slug']], first_cat[lang], small=True)}<figcaption>{esc(L(first_cat['desc'], lang))}</figcaption></figure>
    <ol class="svc-list">{svc_items}</ol>
  </div>
  <div class="stats">{stats_html}</div>
</div></section>

<section class="sec sec-grey sec-wm"><div class="wm" aria-hidden="true">{wm}</div><div class="wrap">
  <div class="split-head"><div><span class="eyebrow">{t('eb_process', lang)}</span><h2 class="h2">{hx('process_title', lang)}</h2></div><p class="sub">{t('process_lead', lang)}</p></div>
  <ol class="psteps">{steps}</ol>
</div></section>

<section class="sec" id="brands"><div class="wrap">
  {sec_head(t('eb_brands', lang), hx('brands_title', lang), t('brands_lead', lang))}
  <div class="grid3">{cards}</div>
</div></section>

<section class="sec sec-grey"><div class="wrap feature">
  <div class="feature-media">{img(cur, feat['image'], 'Aolan Wind Supremo industrial evaporative air cooler', small=True)}</div>
  <div><span class="eyebrow">{t('eb_best', lang)} · Aolan</span><h2 class="h2">Wind <span class="acc">Supremo</span></h2>
  <p class="lead">{esc(L(feat['summary'], lang))}</p>
  <div class="kv">{feat_stats_html}</div>
  <div class="btns"><a class="btn btn-pill btn-pill-dark" href="{href(cur, product_path(lang, feat))}">{t('featured_cta', lang)}<span class="btn-dot">{ICON['ne']}</span></a>
  <a class="btn btn-ghost" href="{contact}?model=Wind%20Supremo&amp;brand=aolan">{t('cta_quote', lang)}</a></div></div>
</div></section>

<section class="sec" id="calculator"><div class="wrap">
  {sec_head(t('eb_tools', lang), hx('calc_title', lang), t('calc_lead', lang))}
  <div class="calc-wrap">{calculator(cur, lang)}{supply_table(lang)}</div>
</div></section>

<section class="sec sec-grey"><div class="wrap">
  {sec_head(t('eb_markets', lang), hx('markets_title', lang), t('markets_lead', lang))}
  <ul class="markets">{markets}</ul>
</div></section>

{cta_band(cur, lang, hx('cta_title', lang), t('cta_lead', lang))}

<section class="sec"><div class="wrap faq-wrap">
  <div><span class="eyebrow">{t('eb_faq', lang)}</span><h2 class="h2">{hx('faq_title', lang)}</h2><div class="faq">{faq}</div></div>
  <div id="inquiry"><span class="eyebrow">{t('eb_contact', lang)}</span><h2 class="h2">{hx('contact_title', lang)}</h2><p class="sub">{t('contact_lead', lang)}</p>{inquiry_form(cur, lang)}</div>
</div></section>
"""
    org = {
        "@context": "https://schema.org",
        "@type": "Organization",
        "name": L(SITE["name"], lang),
        "url": abs_url(cur),
        "logo": f"{SITE['url']}/assets/favicon.svg",
        "email": SITE["email"],
        "telephone": SITE["phone_display"],
        "areaServed": [L(n, "en") for _, n in MARKETS],
        "contactPoint": {"@type": "ContactPoint", "contactType": "sales", "telephone": SITE["phone_display"],
                         "availableLanguage": ["English", "Arabic", "Urdu"]},
    }
    website = {"@context": "https://schema.org", "@type": "WebSite", "name": L(SITE["name"], lang), "url": abs_url(cur), "inLanguage": lang}
    faq_ld = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in T["faq"][lang]],
    }
    title = {
        "en": "Evaporative Air Coolers Wholesale | Pakistan, Saudi, UAE | " + SITE["name"]["en"],
        "ar": "مكيفات صحراوية بالجملة | السعودية والإمارات والخليج | " + SITE["name"]["ar"],
    }[lang]
    desc = {
        "en": "Wholesale industrial, portable and solar evaporative air coolers from Aolan, Coolmax and more. Full specs, 40HQ loading and fast WhatsApp quotes for Pakistan and the Middle East.",
        "ar": "مكيفات صحراوية صناعية ومتنقلة وشمسية بالجملة من أولان وكولماكس وغيرها. مواصفات كاملة وكميات التحميل وعروض أسعار سريعة عبر واتساب للسعودية والإمارات والخليج وباكستان.",
    }[lang]
    write(cur, page(cur, lang, title, desc, body, schema=[org, website, faq_ld]))


def build_aolan_brand(lang):
    cur = f"{lang}/brands/aolan/index.html"
    crumbs, crumb_ld = breadcrumbs(cur, lang, [(f"{lang}/index.html", t("nav_home", lang)), (None, "Aolan")])
    facts = "".join(f'<div><b dir="ltr">{f["n"]}</b><span>{esc(f[lang])}</span></div>' for f in AOLAN["facts"])
    about = "".join(f"<p>{esc(x)}</p>" for x in AOLAN["about"][lang])
    sections = ""
    for c in CATEGORIES:
        items = [p for p in PRODUCTS if p["category"] == c["slug"]]
        cards = "".join(product_card(cur, lang, p) for p in items)
        sections += f"""<section class="sec" id="{c['slug']}"><div class="wrap">
<h2 class="h2">{esc(c[lang])}</h2><p class="sub">{esc(L(c['desc'], lang))}</p><div class="grid4 pgrid">{cards}</div></div></section>"""
    body = f"""
<section class="page-hero"><div class="wrap">
  {crumbs}
  <div class="brand-hero">
    <div><p class="kicker">{esc(AOLAN['legal'])} · {esc(L(AOLAN['origin'], lang))}</p>
    <h1>{'Aolan evaporative air coolers' if lang == 'en' else 'مكيفات أولان الصحراوية (Aolan)'}</h1>
    <p class="lead">{esc(L(AOLAN['tagline'], lang))}</p>
    <nav class="pills">{''.join(f'<a href="#{c["slug"]}">{esc(c[lang])}</a>' for c in CATEGORIES)}</nav></div>
    <div class="hero-media">{img(cur, 'cover', 'Aolan evaporative air cooler range', eager=True)}</div>
  </div>
  <div class="stats stats-inline">{facts}</div>
</div></section>
{sections}
<section class="sec sec-tint"><div class="wrap two">
  <div><h2 class="h2">{t('brand_about', lang, brand='Aolan')}</h2>{about}</div>
  <div>{img(cur, 'factory', 'Aolan Yixu Industry Park factory, Fuzhou', small=True, cls='rounded')}</div>
</div></section>
<section class="sec"><div class="wrap two">
  <div><h2 class="h2">{t('accessories', lang)}</h2><p>{t('accessories_lead', lang)}</p>{img(cur, 'group-control', 'Aolan group control with hub', small=True, cls='rounded')}</div>
  <div>{img(cur, 'accessories', 'Aolan evaporative cooler accessories', small=True, cls='rounded')}</div>
</div></section>
<section class="sec sec-tint"><div class="wrap">
  <h2 class="h2">{t('projects', lang)}</h2>
  <div class="grid2 gallery">{img(cur, 'projects-1', 'Aolan evaporative cooler project cases', small=True, cls='rounded')}{img(cur, 'projects-2', 'Aolan roof-top and wall installation cases', small=True, cls='rounded')}</div>
</div></section>
{cta_band(cur, lang, t('product_cta_title', lang, name='Aolan'), t('product_cta_lead', lang), brand='aolan')}
"""
    item_list = {
        "@context": "https://schema.org",
        "@type": "ItemList",
        "itemListElement": [
            {"@type": "ListItem", "position": i, "url": abs_url(product_path(lang, p)), "name": f"Aolan {p['name']}"}
            for i, p in enumerate(PRODUCTS, 1)
        ],
    }
    title = {
        "en": "Aolan Evaporative Air Coolers: Industrial, Portable & Solar | Wholesale",
        "ar": "مكيفات أولان الصحراوية: صناعية ومتنقلة وشمسية | بالجملة",
    }[lang]
    desc = {
        "en": f"All {len(PRODUCTS)} Aolan cooler families with full specifications: Wind Supremo, Wind Marshal, DC brushless, solar DC and home coolers. Wholesale to Pakistan and the Gulf.",
        "ar": f"جميع فئات مكيفات أولان ({len(PRODUCTS)}) بالمواصفات الكاملة: Wind Supremo وWind Marshal ومحرك DC والمكيفات الشمسية والمنزلية. بالجملة إلى الخليج وباكستان.",
    }[lang]
    write(cur, page(cur, lang, title, desc, body, schema=[crumb_ld, item_list]))


def specs_table(lang, p):
    if p.get("table"):
        tb = p["table"]
        head = "".join(f"<th>{esc(SPEC_LABELS[c][lang])}</th>" for c in tb["cols"])
        rows = "".join(
            "<tr>" + "".join(f'<{"th scope=row" if i == 0 else "td"}>{esc(tr_value(v, lang))}</{"th" if i == 0 else "td"}>' for i, v in enumerate(r)) + "</tr>"
            for r in tb["rows"]
        )
        return f'<div class="tscroll"><table class="tbl tbl-center"><thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table></div>'
    cols = ""
    for m in p["models"]:
        codes = [x for x in m if isinstance(x, str)]
        extra = "".join(f'<small>{esc(L(x, lang))}</small>' for x in m if isinstance(x, dict))
        cols += f'<th scope="col"><span dir="ltr">{"<br>".join(esc(c) for c in codes)}</span>{extra}</th>'
    rows = ""
    for key, vals in p["specs"]:
        if len(set(map(str, vals))) == 1 and len(vals) > 1:
            cells = f'<td colspan="{len(vals)}">{esc(tr_value(vals[0], lang))}</td>'
        else:
            cells = "".join(f"<td>{esc(tr_value(v, lang))}</td>" for v in vals)
        rows += f'<tr><th scope="row">{esc(SPEC_LABELS[key][lang])}</th>{cells}</tr>'
    return f'<div class="tscroll"><table class="tbl spec"><thead><tr><th scope="col">{t("model_col", lang)}</th>{cols}</tr></thead><tbody>{rows}</tbody></table></div>'


def build_product(lang, p):
    cur = product_path(lang, p)
    cat = next(c for c in CATEGORIES if c["slug"] == p["category"])
    crumbs, crumb_ld = breadcrumbs(cur, lang, [
        (f"{lang}/index.html", t("nav_home", lang)),
        (f"{lang}/brands/aolan/index.html", "Aolan"),
        (None, p["name"]),
    ])
    gallery = [p["image"]] + p.get("gallery", [])
    thumbs = ""
    if len(gallery) > 1:
        thumbs = '<div class="thumbs">' + "".join(
            f'<button type="button" data-src="{href(cur, f"{IMG}/{g}.webp")}" aria-label="{i + 1}">{img(cur, g, "", small=True)}</button>'
            for i, g in enumerate(gallery)
        ) + "</div>"
    af = airflow_range(p)
    kv = [(t("airflow", lang), f"{af} m³/h")]
    cap = spec(p, "capacity")
    if cap:
        kv.insert(0, (t("capacity", lang), f"{cap[0]}–{cap[-1]} kW"))
        kv.append(("COP", spec(p, "cop")[0]))
    pw = spec(p, "power")
    if pw:
        kv.append((t("power", lang), pw[0] if pw[0] == pw[-1] else f"{pw[0]} – {pw[-1]}"))
    if p.get("area"):
        kv.append((t("coverage", lang), p["area"]))
    q = spec(p, "qty40")
    if q:
        kv.append((t("loading", lang), q[0] if len(set(q)) == 1 else f"{min(q, key=first_num)}–{max(q, key=first_num)}"))
    kv_html = "".join(f'<div><span>{esc(k)}</span><b dir="auto">{esc(tr_value(v, lang))}</b></div>' for k, v in kv)
    models_list = ", ".join(dict.fromkeys(x for m in p.get("models", []) for x in m if isinstance(x, str))) or ", ".join(r[0] for r in p["table"]["rows"])
    bullets = ""
    if p.get("bullets"):
        bullets = "<ul class=\"ticks\">" + "".join(f"<li>{ICON['check']}{esc(b)}</li>" for b in p["bullets"][lang]) + "</ul>"
    note = f'<p class="small muted">{esc(L(p["note"], lang))}</p>' if p.get("note") else ""
    extra = ""
    if p.get("principle"):
        extra += f"""<section class="sec sec-tint"><div class="wrap two">
  <div><h2 class="h2">{t('how_it_works', lang)}</h2><p>{esc(L(p['principle'], lang))}</p></div>
  <div>{img(cur, 'mini-chiller-principle', 'Mini chiller working principle: indoor unit and evaporative outdoor unit', small=True, cls='rounded white-bg')}</div>
</div></section>"""
    if p.get("comparison"):
        cmp_ = p["comparison"]
        head = "".join(f"<th>{esc(c)}</th>" for c in cmp_["cols"][lang])
        rows = "".join("<tr>" + "".join(f'<{"th scope=row" if i == 0 else "td"}{" class=hl" if i == 3 else ""}>{esc(v)}</{"th" if i == 0 else "td"}>' for i, v in enumerate(r)) + "</tr>" for r in cmp_["rows"][lang])
        extra += f"""<section class="sec"><div class="wrap"><h2 class="h2">{t('compare_title', lang)}</h2>
<div class="tscroll"><table class="tbl compare"><thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table></div>
<h2 class="h2 mt">{t('projects_short', lang)}</h2>{img(cur, 'mini-chiller-cases', 'Aolan Mini Chiller installations in factories and warehouses', small=True, cls='rounded')}</div></section>"""
    related = [r for r in PRODUCTS if r["category"] == p["category"] and r is not p][:4]
    rel_html = "".join(product_card(cur, lang, r) for r in related)
    contact = href(cur, f"{lang}/wholesale-inquiry.html")
    from urllib.parse import quote

    wa_text = f"{t('cta_quote', lang)}: Aolan {p['name']}"
    solar = f'<span class="chip chip-sun">{t("solar_badge", lang)}</span>' if p.get("solar") else ""
    h1 = f"Aolan {p['name']}"
    if p.get("new"):
        solar = f'<span class="chip chip-new">{t("new_kicker", lang)}</span> ' + solar
    body = f"""
<section class="page-hero slim"><div class="wrap">{crumbs}</div></section>
<section class="sec pt0"><div class="wrap product">
  <div class="pgallery"><div class="pmain">{img(cur, p['image'], f"Aolan {p['name']} {L(p['headline'], 'en')}", eager=True)}</div>{thumbs}</div>
  <div class="pinfo">
    <p class="kicker"><a href="{href(cur, f'{lang}/brands/aolan/index.html')}#{cat['slug']}">{esc(cat[lang])}</a></p>
    <h1><span dir="ltr">{esc(h1)}</span></h1>
    <p class="subtitle">{solar}{esc(L(p['headline'], lang))}</p>
    <p>{esc(L(p['summary'], lang))}</p>
    <div class="kv">{kv_html}</div>
    <p class="small muted"><b>{t('model_col', lang)}:</b> <span dir="ltr">{esc(models_list)}</span></p>
    <div class="btns"><a class="btn btn-primary btn-lg" href="{contact}?model={quote(p['name'])}&amp;brand=aolan">{t('cta_quote', lang)}</a>
    <a class="btn btn-wa btn-lg" href="{wa_link(wa_text)}" rel="noopener">{ICON['wa']}{t('cta_whatsapp', lang)}</a></div>
  </div>
</div></section>
<section class="sec pt0"><div class="wrap">
  <h2 class="h2">{t('specs', lang)}</h2>
  {specs_table(lang, p)}
  {note}
  {f'<h2 class="h2 mt">{t("features", lang)}</h2>' if p.get("new") else ""}{bullets}
  <h2 class="h2 mt">{t('applications', lang)}</h2><p>{esc(L(p['apps'], lang))}</p>
  <p class="small muted">{t('spec_source', lang, brand='Aolan') if not p.get('source') else esc(L(p['source'], lang)) + '. ' + t('spec_source', lang, brand='Aolan').split('. ', 1)[1]}</p>
</div></section>
{extra}
{f'<section class="sec sec-tint"><div class="wrap"><h2 class="h2">{t("related", lang)}</h2><div class="grid4 pgrid">{rel_html}</div></div></section>' if rel_html else ''}
{cta_band(cur, lang, t('product_cta_title', lang, name=p['name']), t('product_cta_lead', lang), model=p['name'], brand='aolan')}
"""
    props = []
    for key in ("capacity", "airflow", "power", "voltage", "noise", "pressure", "water", "qty40"):
        vals = spec(p, key)
        if vals:
            props.append({"@type": "PropertyValue", "name": SPEC_LABELS[key]["en"], "value": " | ".join(dict.fromkeys(vals))})
    product_ld = {
        "@context": "https://schema.org",
        "@type": "Product",
        "name": f"Aolan {p['name']}",
        "description": L(p["summary"], lang),
        "image": [f"{SITE['url']}/{IMG}/{g}.webp" for g in gallery],
        "url": abs_url(cur),
        "brand": {"@type": "Brand", "name": "Aolan"},
        "manufacturer": {"@type": "Organization", "name": AOLAN["legal"]},
        "category": cat["en"],
        "model": models_list,
        "additionalProperty": props,
    }
    title = f"Aolan {p['name']}: {L(p['headline'], lang)} | {'Wholesale' if lang == 'en' else 'بالجملة'}"
    desc = L(p["summary"], lang)
    desc = desc if len(desc) < 158 else desc[:155].rsplit(" ", 1)[0] + "…"
    write(cur, page(cur, lang, title, desc, body, schema=[product_ld, crumb_ld], og_image=f"assets/img/og/{p['image']}.jpg"))


def build_placeholder_brand(lang, b):
    cur = f"{lang}/brands/{b['slug']}/index.html"
    crumbs, _ = breadcrumbs(cur, lang, [(f"{lang}/index.html", t("nav_home", lang)), (None, b["name"])])
    secs = ""
    for slug in b["sections"]:
        c = next(c for c in CATEGORIES if c["slug"] == slug)
        cards = "".join(
            f'<div class="pcard pcard-ph"><div class="pcard-img bcard-ph"><span>{esc(b["name"])}</span></div><div class="pcard-body"><h3>{esc(b["name"])} · {esc(c[lang])}</h3><p>{t("soon_card", lang)}</p></div></div>'
            for _ in range(3)
        )
        secs += f'<section class="sec" id="{slug}"><div class="wrap"><h2 class="h2">{esc(c[lang])}</h2><div class="grid3 pgrid">{cards}</div></div></section>'
    demo = f'<p class="demo-note">{t("demo_note", lang)}</p>' if b.get("demo") else ""
    badge = f'<span class="chip chip-new">{esc(L(b["badge"], lang))}</span>' if b.get("badge") else f'<span class="chip">{t("soon", lang)}</span>'
    btn = t("register", lang) if b.get("badge") else t("soon_cta", lang)
    wa_text = f"{btn}: {b['name']}"
    body = f"""
<section class="page-hero"><div class="wrap">{crumbs}
  <div class="brand-hero ph-hero"><div>{badge}<h1>{esc(L(b['tagline'], lang))}</h1><p class="lead">{esc(L(b['intro'], lang))}</p>
  <div class="btns"><a class="btn btn-wa btn-lg" href="{wa_link(wa_text)}" rel="noopener">{ICON['wa']}{esc(btn)}</a>
  <a class="btn btn-ghost btn-lg" href="{href(cur, f'{lang}/wholesale-inquiry.html')}?brand={b['slug']}">{t('cta_quote', lang)}</a></div>{demo}</div>
  <div class="bcard-ph big"><span>{esc(b['name'])}</span></div></div>
</div></section>
{secs}
{cta_band(cur, lang, t('product_cta_title', lang, name=b['name']), t('product_cta_lead', lang), brand=b['slug'])}
"""
    title = f"{b['name']} {'evaporative air coolers wholesale' if lang == 'en' else 'مكيفات صحراوية بالجملة'} | {L(SITE['name'], lang)}"
    write(cur, page(cur, lang, title, L(b["intro"], lang)[:155], body, noindex=True))


def build_calc_page(lang):
    cur = f"{lang}/cooler-sizing-calculator.html"
    crumbs, crumb_ld = breadcrumbs(cur, lang, [(f"{lang}/index.html", t("nav_home", lang)), (None, t("nav_calc", lang))])
    body = f"""
<section class="page-hero"><div class="wrap">{crumbs}<h1>{hx('calc_title', lang)}</h1><p class="lead">{t('calc_lead', lang)}</p></div></section>
<section class="sec pt0"><div class="wrap calc-wrap">{calculator(cur, lang)}{supply_table(lang)}</div></section>
{cta_band(cur, lang, hx('cta_title', lang), t('cta_lead', lang))}
"""
    title = {
        "en": "Evaporative Air Cooler Sizing Calculator: How Many Units Do You Need?",
        "ar": "حاسبة المكيفات الصحراوية: كم مكيفاً تحتاج لمساحتك؟",
    }[lang]
    desc = {
        "en": "Calculate how many industrial evaporative air coolers a factory, warehouse, hall or shop needs from floor area, ceiling height and air changes per hour.",
        "ar": "احسب عدد المكيفات الصحراوية الصناعية التي يحتاجها المصنع أو المستودع أو القاعة أو المحل حسب المساحة وارتفاع السقف ومعدل تغيير الهواء.",
    }[lang]
    write(cur, page(cur, lang, title, desc, body, schema=[crumb_ld]))


def build_contact(lang):
    cur = f"{lang}/wholesale-inquiry.html"
    crumbs, crumb_ld = breadcrumbs(cur, lang, [(f"{lang}/index.html", t("nav_home", lang)), (None, t("nav_contact", lang))])
    body = f"""
<section class="page-hero"><div class="wrap">{crumbs}<h1>{hx('contact_title', lang)}</h1><p class="lead">{t('contact_lead', lang)}</p></div></section>
<section class="sec pt0"><div class="wrap contact-grid">
  {inquiry_form(cur, lang)}
  <aside class="card contact-card"><h2>{t('f_direct', lang)}</h2>
    <a class="btn btn-wa btn-lg wide" href="{wa_link()}" rel="noopener">{ICON['wa']}<span dir="ltr">{esc(SITE['phone_display'])}</span></a>
    <p><a href="mailto:{SITE['email']}">{esc(SITE['email'])}</a></p><p>{esc(L(SITE['address'], lang))}</p>
    <ul class="ticks">{''.join(f"<li>{ICON['check']}{esc(x)}</li>" for x in T['hero_points'][lang])}</ul></aside>
</div></section>
"""
    title = {"en": "Wholesale Inquiry: Evaporative Air Cooler Price List", "ar": "طلب عرض سعر: أسعار المكيفات الصحراوية بالجملة"}[lang]
    desc = {
        "en": "Request wholesale prices, availability and container loading for industrial and portable evaporative air coolers. Fast replies on WhatsApp.",
        "ar": "اطلب أسعار الجملة والتوفر وكميات التحميل للمكيفات الصحراوية الصناعية والمتنقلة. رد سريع عبر واتساب.",
    }[lang]
    write(cur, page(cur, lang, title, desc, body, schema=[crumb_ld]))


def build_root():
    redirect = f"""<script>(function(){{var l='en';try{{var s=localStorage.getItem('cm_lang');if(s){{l=s}}else{{
var z={json.dumps(ME_TIMEZONES)},n=(navigator.languages||[navigator.language])[0]||'',tz='';
try{{tz=Intl.DateTimeFormat().resolvedOptions().timeZone}}catch(e){{}}if(/^ar/i.test(n)||z.indexOf(tz)>-1)l='ar'}}}}catch(e){{}}
location.replace(l+'/index.html')}})()</script>"""
    html_ = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{SITE['name']['en']} · {SITE['name']['ar']}</title>
<meta name="description" content="Wholesale evaporative air coolers for Pakistan and the Middle East. مكيفات صحراوية بالجملة.">
<link rel="canonical" href="{SITE['url']}/">
<link rel="alternate" hreflang="en" href="{SITE['url']}/en/"><link rel="alternate" hreflang="ar" href="{SITE['url']}/ar/">
<link rel="alternate" hreflang="x-default" href="{SITE['url']}/">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
{redirect}
<style>body{{font-family:system-ui,sans-serif;display:grid;place-items:center;min-height:100vh;margin:0;background:#0b3a6e;color:#fff}}
a{{color:#0b3a6e;background:#fff;padding:.8rem 1.4rem;border-radius:.6rem;margin:.4rem;text-decoration:none;font-weight:700;display:inline-block}}</style>
</head><body><div style="text-align:center"><p>{SITE['name']['en']}</p>
<a href="en/index.html" onclick="try{{localStorage.setItem('cm_lang','en')}}catch(e){{}}">English</a>
<a href="ar/index.html" lang="ar" onclick="try{{localStorage.setItem('cm_lang','ar')}}catch(e){{}}">العربية</a></div></body></html>
"""
    write("index.html", html_)


def build_404():
    cur = "en/404.html"
    body = f"""<section class="page-hero nf"><div class="wrap center"><h1>{t('nf_title', 'en')} · <span lang="ar">{t('nf_title', 'ar')}</span></h1>
<p class="lead">{t('nf_lead', 'en')}</p><p class="lead" lang="ar" dir="rtl">{t('nf_lead', 'ar')}</p>
<div class="btns center"><a class="btn btn-primary" href="{BASE}/en/index.html">English</a><a class="btn btn-ghost" href="{BASE}/ar/index.html">العربية</a></div></div></section>"""
    out = page(cur, "en", "404 · " + t("nf_title", "en"), t("nf_lead", "en"), body, noindex=True, has_alt=False)
    # 404 is served from any URL, so make asset links root-absolute.
    out = re.sub(r'(href|src)="\.\./assets/', r'\1="' + BASE + '/assets/', out)
    out = re.sub(r'href="(?!https?:|/|#|mailto:)([^"]+)"', r'href="' + BASE + r'/en/\1"', out).replace(f"{BASE}/en/../ar/404.html", f"{BASE}/ar/index.html")
    out = re.sub(r"<script>\(function\(\)\{try\{if\(localStorage.*?</script>", "", out, flags=re.S)
    write("404.html", out)


def build_sitemap():
    urls = ""
    for en, ar in SITEMAP:
        for loc in (en, ar):
            urls += (
                f"<url><loc>{abs_url(loc)}</loc><lastmod>{TODAY}</lastmod>"
                f'<xhtml:link rel="alternate" hreflang="en" href="{abs_url(en)}"/>'
                f'<xhtml:link rel="alternate" hreflang="ar" href="{abs_url(ar)}"/>'
                f'<xhtml:link rel="alternate" hreflang="x-default" href="{abs_url(en)}"/></url>\n'
            )
    write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
          'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + urls + "</urlset>\n")
    write("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {SITE['url']}/sitemap.xml\n")


def build_images():
    src = os.path.join(OUT, IMG)
    for f in os.listdir(src):
        if f.endswith(".webp") and not f.endswith("-sm.webp"):
            sm = os.path.join(src, f[:-5] + "-sm.webp")
            if not os.path.exists(sm):
                with Image.open(os.path.join(src, f)) as im:
                    im.thumbnail((720, 720))
                    im.save(sm, "WEBP", quality=78, method=6)
    og = os.path.join(OUT, "assets/img/og")
    os.makedirs(og, exist_ok=True)
    for p in PRODUCTS:
        dst = os.path.join(og, p["image"] + ".jpg")
        if not os.path.exists(dst):
            with Image.open(os.path.join(src, p["image"] + ".webp")) as im:
                canvas = Image.new("RGB", (1200, 630), "white")
                im = im.convert("RGB")
                im.thumbnail((1100, 580))
                canvas.paste(im, ((1200 - im.width) // 2, (630 - im.height) // 2))
                canvas.save(dst, "JPEG", quality=82)
    main_og = os.path.join(OUT, "assets/img/og.jpg")
    if not os.path.exists(main_og):
        with Image.open(os.path.join(src, "cover.webp")) as im:
            im.convert("RGB").resize((1200, 630)).save(main_og, "JPEG", quality=82)


def main():
    for d in LANGS:
        shutil.rmtree(os.path.join(OUT, d), ignore_errors=True)
    build_images()
    for lang in LANGS:
        build_home(lang)
        build_aolan_brand(lang)
        for p in PRODUCTS:
            build_product(lang, p)
        for b in PLACEHOLDER_BRANDS:
            build_placeholder_brand(lang, b)
        build_calc_page(lang)
        build_contact(lang)
    build_root()
    build_404()
    build_sitemap()
    n = sum(len(fs) for _, _, fs in os.walk(OUT) if True)
    print(f"Built {len(SITEMAP) * 2} indexable pages, {n} files in {OUT}")


if __name__ == "__main__":
    main()

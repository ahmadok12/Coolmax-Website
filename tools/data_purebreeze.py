"""PureBreeze product data, transcribed from the PureBreeze 2027 air cooler catalogue.

Same structure as data_aolan.py. Model codes use the PureBreeze "PB-" prefix; values are kept as printed.
Suffixes: R / C = remote control, A = mechanical, G = glass top cover.
"""

BRAND = {
    "slug": "purebreeze",
    "name": "PureBreeze",
    "logo": "brands/purebreeze-logo",
    "status": "new",
    "badge": {"en": "New · Canton Fair 2026", "ar": "جديد · معرض كانتون 2026"},
    "kicker": {"en": "Home air coolers · New for 2026", "ar": "مكيفات منزلية · جديد 2026"},
    "title": {"en": "PureBreeze air coolers", "ar": "مكيفات بيور بريز (PureBreeze)"},
    "tagline": {
        "en": "New BLDC cube coolers from the 2026 Canton Fair, plus tower and room coolers for every home",
        "ar": "مكيفات مكعبة جديدة بمحرك BLDC من معرض كانتون 2026، مع مكيفات برجية ومكيفات غرف لكل منزل",
    },
    "hero_image": "purebreeze/bldc-hero",
    "card_image": "purebreeze/bldc-hero",
    "facts": [
        {"n": "BLDC", "en": "Energy-saving motor on the new cube coolers", "ar": "محرك موفر للطاقة في المكيفات المكعبة الجديدة"},
        {"n": "28,000", "en": "m³/h top airflow", "ar": "م³/ساعة أعلى تدفق"},
        {"n": "8", "en": "Product series", "ar": "سلاسل منتجات"},
        {"n": "110–240 V", "en": "Works on Pakistan and Gulf power", "ar": "تعمل على كهرباء باكستان والخليج"},
    ],
    "about": {
        "en": [
            "PureBreeze is our new home cooler brand for 2026. Its hero product is the BLDC cube cooler shown for the first time at "
            "this year's Canton Fair: a centrifugal cooler with a brushless DC motor that draws 450–1,100 W, a booster air vent, "
            "120° wide-angle air supply and a high-density cooling pad.",
            "Around it sits a complete retail range: tall duct-top coolers up to 11,000 m³/h, a 28,000 m³/h big-room cooler, slim towers, "
            "glass-top room coolers and compact bedroom units. Every model runs on 110–240 V and is quoted with 40HQ loading quantities.",
        ],
        "ar": [
            "بيور بريز هي علامتنا الجديدة للمكيفات المنزلية لعام 2026. ومنتجها الرئيسي هو المكيف المكعب بمحرك BLDC الذي عُرض لأول مرة "
            "في معرض كانتون هذا العام: مكيف بمروحة طاردة ومحرك تيار مستمر بدون فرش باستهلاك 450–1,100 واط، مع فتحة هواء معززة، "
            "وتوزيع هواء بزاوية 120 درجة، ووسادة تبريد عالية الكثافة.",
            "وتكتمل التشكيلة بمكيفات للبيع بالتجزئة: مكيفات طويلة بمخرج علوي حتى 11,000 م³/ساعة، ومكيف للغرف الكبيرة بتدفق 28,000 م³/ساعة، "
            "ومكيفات برجية نحيفة، ومكيفات غرف بغطاء زجاجي، ووحدات صغيرة لغرف النوم. وتعمل جميع الموديلات على 110–240 فولت، ونقدم لها عروض أسعار مع كميات التحميل في حاوية 40 قدم.",
        ],
    },
    "about_image": "purebreeze/bldc-98c",
    "note": {"en": "R / C = remote control, A = mechanical control, G = glass top cover.", "ar": "R / C = ريموت، A = تحكم ميكانيكي، G = غطاء زجاجي."},
}

CATEGORIES = [
    {
        "slug": "bldc",
        "en": "BLDC cube coolers",
        "ar": "مكيفات مكعبة بمحرك BLDC",
        "image": "purebreeze/bldc-hero",
        "desc": {
            "en": "New for 2026: energy-saving brushless DC coolers with 120° air supply for halls, shops and large rooms.",
            "ar": "جديد 2026: مكيفات موفرة للطاقة بمحرك تيار مستمر بدون فرش وتوزيع هواء بزاوية 120 درجة للقاعات والمحلات والغرف الكبيرة.",
        },
    },
    {
        "slug": "large",
        "en": "Large portable coolers",
        "ar": "مكيفات متنقلة كبيرة",
        "image": "purebreeze/pb-75",
        "desc": {
            "en": "7,000–28,000 m³/h coolers on wheels with top or side discharge for shops, halls and outdoor seating.",
            "ar": "مكيفات على عجلات بتدفق 7,000–28,000 م³/ساعة بتصريف علوي أو جانبي للمحلات والقاعات والجلسات الخارجية.",
        },
    },
    {
        "slug": "home",
        "en": "Home & room coolers",
        "ar": "مكيفات المنازل والغرف",
        "image": "purebreeze/gs-5800",
        "desc": {
            "en": "Tower, glass-top and compact room coolers from 1,500 to 8,500 m³/h for homes, offices and retail shelves.",
            "ar": "مكيفات برجية وبغطاء زجاجي ومكيفات غرف صغيرة بتدفق من 1,500 إلى 8,500 م³/ساعة للمنازل والمكاتب ورفوف المحلات.",
        },
    },
]

V = "110–240 V, 50/60 Hz"
MR = "Mechanical or remote"
APPS_HOME = {
    "en": "Homes, offices, shops, clinics, cafés and small restaurants.",
    "ar": "المنازل والمكاتب والمحلات والعيادات والمقاهي والمطاعم الصغيرة.",
}
APPS_LARGE = {
    "en": "Shops, showrooms, halls, mosques, restaurants, workshops and outdoor seating.",
    "ar": "المحلات وصالات العرض والقاعات والمساجد والمطاعم والورش والجلسات الخارجية.",
}

PRODUCTS = [
    {
        "slug": "pb-bldc-cube",
        "category": "bldc",
        "name": "BLDC Cube Cooler",
        "new": True,
        "featured": True,
        "image": "purebreeze/bldc-hero",
        "gallery": ["purebreeze/bldc-88c", "purebreeze/bldc-98c"],
        "headline": {"en": "15,000–18,000 m³/h BLDC evaporative cooler, new for 2026", "ar": "مكيف صحراوي بمحرك BLDC بتدفق 15,000–18,000 م³/ساعة، جديد 2026"},
        "summary": {
            "en": "PureBreeze's new hero product, launched at the 2026 Canton Fair. A brushless DC motor gives industrial-size airflow from 450–1,100 W, "
                  "with a booster air vent, 120° wide-angle supply, a high-density cooling pad and a water filter. Two sizes ship SKD for efficient containers.",
            "ar": "المنتج الرئيسي الجديد من بيور بريز، أُطلق في معرض كانتون 2026. يمنح محرك التيار المستمر بدون فرش تدفق هواء بحجم صناعي باستهلاك 450–1,100 واط، "
                  "مع فتحة هواء معززة، وتوزيع هواء بزاوية 120 درجة، ووسادة تبريد عالية الكثافة، وفلتر مياه. مقاسان يُشحنان مفككين (SKD) لتحميل أكبر في الحاوية.",
        },
        "bullets": {
            "en": [
                "BLDC motor: high efficiency and lower electricity bills",
                "Booster air vent for a longer air throw",
                "Wide-angle 120° air supply",
                "High-density cooling pad",
                "Water filter keeps the pad and pump clean",
            ],
            "ar": [
                "محرك BLDC: كفاءة عالية وفاتورة كهرباء أقل",
                "فتحة هواء معززة لدفع الهواء لمسافة أبعد",
                "توزيع هواء بزاوية واسعة 120 درجة",
                "وسادة تبريد عالية الكثافة",
                "فلتر مياه يحافظ على نظافة الوسادة والمضخة",
            ],
        },
        "area": "80–120 m²",
        "apps": {
            "en": "Shops, showrooms, halls, restaurants, mosques, workshops and large living rooms.",
            "ar": "المحلات وصالات العرض والقاعات والمطاعم والمساجد والورش وغرف المعيشة الكبيرة.",
        },
        "models": [["PB-88C"], ["PB-98C"]],
        "specs": [
            ("airflow", ["15,000", "18,000"]),
            ("power", ["450–750 W", "650–1,100 W"]),
            ("motor", ["BLDC motor", "BLDC motor"]),
            ("voltage", ["110/240 V", "110/240 V"]),
            ("fanwheel", ["350 mm", "400 mm"]),
            ("water", ["40", "60"]),
            ("area", ["80–100 m²", "100–120 m²"]),
            ("dim", ["820×820×970", "980×980×1020"]),
            ("qty40hq", ["150 (SKD)", "100 (SKD)"]),
        ],
    },
    {
        "slug": "pb-top-discharge",
        "category": "large",
        "name": "PB-45 / 55 / 75 Top-Discharge",
        "image": "purebreeze/pb-75",
        "gallery": [],
        "headline": {"en": "7,000–11,000 m³/h portable cooler with ducted top outlet", "ar": "مكيف متنقل بمخرج علوي بتدفق 7,000–11,000 م³/ساعة"},
        "summary": {
            "en": "Tall portable coolers that blow cool air up and over a crowd through a top outlet. 285 mm fan wheel, 60 L tank, mechanical or remote control.",
            "ar": "مكيفات متنقلة طويلة تدفع الهواء البارد للأعلى وفوق الحضور عبر مخرج علوي. مروحة 285 مم، وخزان 60 لتراً، وتحكم ميكانيكي أو بالريموت.",
        },
        "area": "25–55 m²",
        "apps": APPS_LARGE,
        "models": [["PB-45", "PB-45R"], ["PB-55", "PB-55R"], ["PB-75", "PB-75R"]],
        "specs": [
            ("airflow", ["7,000", "9,000", "11,000"]),
            ("power", ["500 W", "750 W", "1,100 W"]),
            ("voltage", [V] * 3),
            ("controller", [MR] * 3),
            ("fanwheel", ["285 mm"] * 3),
            ("outletform", ["Blow-up"] * 3),
            ("water", ["60"] * 3),
            ("area", ["25–35 m²", "35–45 m²", "45–55 m²"]),
            ("nwgw", ["34 / 35.5", "40 / 42", "43 / 45"]),
            ("dim", ["720×720×1600", "720×720×1800", "720×720×2000"]),
            ("packing", ["725×730×1580", "725×730×1780", "725×730×1980"]),
            ("qty40hq", ["144", "114", "102"]),
        ],
    },
    {
        "slug": "pb-side-discharge",
        "category": "large",
        "name": "PB-45F / 55F / 75F Side-Discharge",
        "image": "purebreeze/pb-75f",
        "gallery": [],
        "headline": {"en": "7,000–11,000 m³/h portable cooler with side outlet", "ar": "مكيف متنقل بمخرج جانبي بتدفق 7,000–11,000 م³/ساعة"},
        "summary": {
            "en": "Side-blowing versions of the PB-45 to PB-75, lower in height for shops and terraces. 285 mm fan wheel, 60 L tank, mechanical or remote control.",
            "ar": "نسخ بتصريف جانبي من PB-45 حتى PB-75، بارتفاع أقل للمحلات والتراسات. مروحة 285 مم، وخزان 60 لتراً، وتحكم ميكانيكي أو بالريموت.",
        },
        "area": "25–55 m²",
        "apps": APPS_LARGE,
        "models": [["PB-45F", "PB-45FR"], ["PB-55F", "PB-55FR"], ["PB-75F", "PB-75FR"]],
        "specs": [
            ("airflow", ["7,000", "9,000", "11,000"]),
            ("power", ["500 W", "750 W", "1,100 W"]),
            ("voltage", [V] * 3),
            ("controller", [MR] * 3),
            ("fanwheel", ["285 mm"] * 3),
            ("outletform", ["Blow-side"] * 3),
            ("water", ["60"] * 3),
            ("area", ["25–35 m²", "35–45 m²", "45–55 m²"]),
            ("nwgw", ["34 / 35.5", "40 / 42", "43 / 45"]),
            ("dim", ["720×720×820", "720×720×1050", "720×720×1300"]),
            ("packing", ["725×730×800", "725×730×1030", "725×730×1280"]),
            ("qty40hq", ["144", "114", "102"]),
        ],
    },
    {
        "slug": "pb-28000",
        "category": "large",
        "name": "PB-28000",
        "image": "purebreeze/pb-28000",
        "gallery": ["purebreeze/pb-28000b"],
        "headline": {"en": "28,000 m³/h big-room portable cooler", "ar": "مكيف متنقل للغرف الكبيرة بتدفق 28,000 م³/ساعة"},
        "summary": {
            "en": "The most powerful PureBreeze cooler: 28,000 m³/h from 1,100 W with a 175 L tank for a full day of cooling. Mechanical or remote control.",
            "ar": "أقوى مكيفات بيور بريز: تدفق 28,000 م³/ساعة من 1,100 واط مع خزان 175 لتراً ليوم كامل من التبريد. تحكم ميكانيكي أو بالريموت.",
        },
        "area": "50–60 m²",
        "apps": APPS_LARGE,
        "models": [["PB-28000", "PB-28000R"]],
        "specs": [
            ("airflow", ["28,000"]),
            ("power", ["1,100 W"]),
            ("voltage", [V]),
            ("controller", [MR]),
            ("topcover", ["Plastic"]),
            ("water", ["175"]),
            ("area", ["50–60 m²"]),
            ("nwgw", ["32.6 / 36.0"]),
            ("dim", ["915×550×1555"]),
            ("packing", ["937×585×1530"]),
            ("qty40hq", ["77"]),
        ],
    },
    {
        "slug": "pb-dt-series",
        "category": "home",
        "name": "PB-DT60 / DT80",
        "image": "purebreeze/dt80",
        "gallery": ["purebreeze/dt60"],
        "headline": {"en": "6,500–8,500 m³/h room cooler with plastic or glass top", "ar": "مكيف غرف بتدفق 6,500–8,500 م³/ساعة بغطاء بلاستيكي أو زجاجي"},
        "summary": {
            "en": "Low-power room coolers with a removable 55 or 85 L tank: only 95–180 W, plastic or glass top, mechanical or remote control.",
            "ar": "مكيفات غرف منخفضة الاستهلاك بخزان قابل للفصل سعة 55 أو 85 لتراً: 95–180 واط فقط، بغطاء بلاستيكي أو زجاجي، وتحكم ميكانيكي أو بالريموت.",
        },
        "area": "45–75 m²",
        "apps": APPS_HOME,
        "models": [["PB-DT60/60G", "PB-DT60R/60GR"], ["PB-DT80/80G", "PB-DT80R/80GR"]],
        "specs": [
            ("airflow", ["6,500", "8,500"]),
            ("power", ["95 W", "180 W"]),
            ("voltage", ["220–240 V, 50/60 Hz"] * 2),
            ("controller", [MR] * 2),
            ("topcover", ["Plastic or glass"] * 2),
            ("water", ["55", "85"]),
            ("area", ["45–65 m²", "55–75 m²"]),
            ("dim", ["520×370×1100", "615×425×1250"]),
            ("packing", ["560×410×830", "665×468×860"]),
            ("qty40hq", ["370", "270"]),
        ],
    },
    {
        "slug": "pb-900-turbo",
        "category": "home",
        "name": "PB-900 Turbo Tower",
        "image": "purebreeze/turbo-900",
        "gallery": ["purebreeze/turbo-900r"],
        "headline": {"en": "7,000 m³/h slim tower cooler", "ar": "مكيف برجي نحيف بتدفق 7,000 م³/ساعة"},
        "summary": {
            "en": "Slim tower cooler with turbo airflow of 7,000 m³/h from 150 W and a 55 L tank. Mechanical (PB-900) or digital display with remote (PB-900R).",
            "ar": "مكيف برجي نحيف بتدفق قوي 7,000 م³/ساعة من 150 واط وخزان 55 لتراً. تحكم ميكانيكي (PB-900) أو شاشة رقمية مع ريموت (PB-900R).",
        },
        "area": "45–65 m²",
        "apps": APPS_HOME,
        "models": [["PB-900 Turbo", "PB-900R Turbo"]],
        "specs": [
            ("airflow", ["7,000"]),
            ("power", ["150 W"]),
            ("voltage", [V]),
            ("controller", ["Mechanical or digital"]),
            ("water", ["55"]),
            ("area", ["45–65 m²"]),
            ("nwgw", ["15.6 / 17.5"]),
            ("dim", ["415×434×1350"]),
            ("packing", ["465×475×1045"]),
            ("qty40hq", ["307"]),
        ],
    },
    {
        "slug": "pb-glass-top",
        "category": "home",
        "name": "PB Glass-Top Room Coolers",
        "image": "purebreeze/gs-5800",
        "gallery": ["purebreeze/g-8288", "purebreeze/ag-680", "purebreeze/g-5800"],
        "headline": {"en": "5,500–8,000 m³/h room cooler with glass top", "ar": "مكيف غرف بغطاء زجاجي بتدفق 5,500–8,000 م³/ساعة"},
        "summary": {
            "en": "Five glass-top room coolers that look good on a shop floor: 150–280 W, 45–60 L tanks and 194–310 units per 40HQ. Each comes in a mechanical and a remote version.",
            "ar": "خمسة مكيفات غرف بغطاء زجاجي بمظهر جذاب في المحل: 150–280 واط، وخزانات 45–60 لتراً، و194–310 وحدة في حاوية 40 قدم. ولكل موديل نسخة ميكانيكية ونسخة بالريموت.",
        },
        "area": "15–25 m²",
        "apps": APPS_HOME,
        "models": [["PB-680AG", "PB-680CG"], ["PB-780AG", "PB-780CG"], ["PB-8288AG", "PB-8288CG"], ["PB-5800GS", "PB-5800GSR"], ["PB-5800G", "PB-5800GR"]],
        "specs": [
            ("airflow", ["5,500", "5,500", "8,000", "6,000", "6,000"]),
            ("power", ["180 W", "180 W", "280 W", "150 W", "150 W"]),
            ("voltage", [V] * 5),
            ("controller", [MR] * 5),
            ("topcover", ["Glass"] * 5),
            ("water", ["45", "45", "60", "45", "45"]),
            ("area", ["15–25 m²"] * 5),
            ("nwgw", ["13.5 / 15", "13.5 / 15", "17.5 / 20", "9.5 / 11.0", "9.5 / 11.0"]),
            ("dim", ["460×360×1055", "460×360×1055", "594×410×1150", "460×360×1100", "460×360×1055"]),
            ("packing", ["520×420×1055", "520×420×1055", "660×460×1150", "505×430×1075", "505×430×1000"]),
            ("qty40hq", ["310", "310", "194", "300", "300"]),
        ],
    },
    {
        "slug": "pb-compact",
        "category": "home",
        "name": "PB Compact Coolers",
        "image": "purebreeze/pb-3808",
        "gallery": ["purebreeze/pb-500", "purebreeze/pb-380", "purebreeze/pb-380ad"],
        "headline": {"en": "1,500–6,000 m³/h compact room cooler", "ar": "مكيف غرف صغير بتدفق 1,500–6,000 م³/ساعة"},
        "summary": {
            "en": "Small, light coolers for bedrooms, offices and counters: from 60 W, 8–30 L tanks and up to 1,250 units per 40HQ for high-volume retail.",
            "ar": "مكيفات صغيرة وخفيفة لغرف النوم والمكاتب والكاونترات: من 60 واط، وخزانات 8–30 لتراً، وحتى 1,250 وحدة في حاوية 40 قدم للبيع بكميات كبيرة.",
        },
        "area": "5–25 m²",
        "apps": APPS_HOME,
        "models": [["PB-3808G", "PB-3808GR"], ["PB-500A", "PB-500C"], ["PB-380A", "PB-380C"], ["PB-380AD", "PB-380CD"]],
        "specs": [
            ("airflow", ["3,000", "6,000", "1,500", "1,500"]),
            ("power", ["80 W", "200 W", "60 W", "120 W"]),
            ("voltage", [V] * 4),
            ("controller", [MR] * 4),
            ("topcover", ["Glass", "Plastic", "Plastic", "Plastic"]),
            ("water", ["15", "30", "8", "8"]),
            ("area", ["15–25 m²", "15–25 m²", "5–10 m²", "5–10 m²"]),
            ("nwgw", ["7 / 8.5", "9.5 / 11.0", "4.0 / 5.0", "6.6 / 8.2"]),
            ("dim", ["375×340×800", "385×350×1090", "350×200×570", "350×200×920"]),
            ("packing", ["422×382×825", "420×390×1140", "390×240×580", "410×270×940"]),
            ("qty40hq", ["465", "390", "1,250", "790"]),
        ],
    },
]

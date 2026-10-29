"""Coolmax product data, transcribed from the Coolmax 2026 air cooler catalogue.

Same structure as data_aolan.py. Model codes use the Coolmax "CM-" prefix. Sizes are converted from metres to mm;
everything else is kept as printed. Suffixes: T = top discharge, S = side, D = down; -L = large water tank.
"""

BRAND = {
    "slug": "coolmax",
    "name": "Coolmax",
    "logo": "brands/coolmax-logo",
    "status": "live",
    "kicker": {"en": "Ultimate Cooling, Ultimate Comfort", "ar": "تبريد أقصى، راحة أقصى"},
    "title": {"en": "Coolmax evaporative air coolers", "ar": "مكيفات كولماكس الصحراوية (Coolmax)"},
    "tagline": {
        "en": "Industrial, mobile, window and home evaporative coolers from 4,000 to 50,000 m³/h",
        "ar": "مكيفات صحراوية صناعية ومتنقلة وللنوافذ وللمنازل بتدفق من 4,000 إلى 50,000 م³/ساعة",
    },
    "hero_image": "coolmax/18tc",
    "card_image": "coolmax/18tc",
    "facts": [
        {"n": "24", "en": "Cooler series", "ar": "سلسلة مكيفات"},
        {"n": "50,000", "en": "m³/h top airflow", "ar": "م³/ساعة أعلى تدفق"},
        {"n": "250 m²", "en": "Cooling area per unit, up to", "ar": "مساحة تبريد للوحدة حتى"},
        {"n": "110–415 V", "en": "1-phase and 3-phase options", "ar": "خيارات أحادية وثلاثية الطور"},
    ],
    "about": {
        "en": [
            "Coolmax is the evaporative cooler range we sell every day from our store in Pakistan. It covers the full job list "
            "of a cooling dealer: compact window units, mobile coolers with a ducted top outlet, and roof or wall-mounted "
            "industrial machines up to 50,000 m³/h.",
            "Choose centrifugal models for quieter running and higher static pressure on duct runs, or axial models for the "
            "most air per watt. Most series come with top, side or down discharge, a standard or large water tank, and "
            "single-speed or inverter control, so one container can serve homes, shops, workshops and factories.",
        ],
        "ar": [
            "كولماكس هي تشكيلة المكيفات الصحراوية التي نبيعها يومياً من معرضنا في باكستان. وتغطي كل احتياجات تاجر التبريد: "
            "وحدات نوافذ صغيرة، ومكيفات متنقلة بمخرج علوي يوصل بمجاري الهواء، ووحدات صناعية تركب على السطح أو الجدار بتدفق يصل إلى 50,000 م³/ساعة.",
            "اختر الموديلات ذات المروحة الطاردة (Centrifugal) لتشغيل أهدأ وضغط أعلى في مجاري الهواء، أو الموديلات ذات المروحة المحورية (Axial) "
            "لأعلى تدفق هواء لكل واط. وتتوفر معظم السلاسل بتصريف علوي أو جانبي أو سفلي، وبخزان مياه عادي أو كبير، وبتحكم سرعة واحدة أو إنفرتر، "
            "لتخدم حاوية واحدة المنازل والمحلات والورش والمصانع.",
        ],
    },
    "about_image": "coolmax/lifestyle",
    "note": {
        "en": "T = top discharge, S = side, D = down discharge. -L = large water tank.",
        "ar": "T = تصريف علوي، S = جانبي، D = سفلي. ‎-L = خزان مياه كبير.",
    },
}

CATEGORIES = [
    {
        "slug": "industrial",
        "en": "Industrial mounted coolers",
        "ar": "مكيفات صحراوية صناعية ثابتة",
        "image": "coolmax/18tc",
        "desc": {
            "en": "Roof, wall and window-mounted units from 13,000 to 50,000 m³/h with centrifugal or axial fans, for factories, warehouses, halls and farms.",
            "ar": "وحدات تركب على السطح أو الجدار أو النافذة بتدفق من 13,000 إلى 50,000 م³/ساعة بمراوح طاردة أو محورية، للمصانع والمستودعات والقاعات والمزارع.",
        },
    },
    {
        "slug": "mobile",
        "en": "Mobile coolers with duct outlet",
        "ar": "مكيفات متنقلة بمخرج هواء",
        "image": "coolmax/700t",
        "desc": {
            "en": "Coolers on wheels from 4,000 to 50,000 m³/h. Most can also be fixed on a wall and ducted, with top or side outlet and a standard or large tank.",
            "ar": "مكيفات على عجلات بتدفق من 4,000 إلى 50,000 م³/ساعة، ويمكن تثبيت معظمها على الجدار وتوصيلها بمجاري الهواء، بمخرج علوي أو جانبي وخزان عادي أو كبير.",
        },
    },
    {
        "slug": "window",
        "en": "Window & compact coolers",
        "ar": "مكيفات النوافذ والمكيفات الصغيرة",
        "image": "coolmax/window-wsa",
        "desc": {
            "en": "5,000–10,000 m³/h window coolers for rooms, shops and offices, with LCD remote control.",
            "ar": "مكيفات نوافذ بتدفق 5,000–10,000 م³/ساعة للغرف والمحلات والمكاتب، مع شاشة LCD وريموت.",
        },
    },
    {
        "slug": "home",
        "en": "Home & shop coolers",
        "ar": "مكيفات المنازل والمحلات",
        "image": "coolmax/j-plastic",
        "desc": {
            "en": "Plastic and metal-body room coolers from 6,000 to 23,000 m³/h with manual or touch-screen remote control.",
            "ar": "مكيفات غرف بهيكل بلاستيكي أو معدني بتدفق من 6,000 إلى 23,000 م³/ساعة بتحكم يدوي أو شاشة لمس مع ريموت.",
        },
    },
]

V1 = "220 V, 50/60 Hz"
V3 = "110/220–240 V or 380–415 V, 50/60 Hz"
V3A = "110/220–240 V or 380–450 V, 50/60 Hz"
INV = "Frequency inverter"
SPD = "Single speed or frequency inverter"
LCD = "LCD with remote"
LCDM = "LCD with remote or manual controller"
MAN = "Manual controller"
CEN = "Centrifugal"
AX = "Axial"

APPS_IND = {
    "en": "Factories, warehouses, workshops, exhibition halls, poultry and livestock farms, greenhouses, markets.",
    "ar": "المصانع والمستودعات والورش وقاعات المعارض ومزارع الدواجن والماشية والبيوت المحمية والأسواق.",
}
APPS_MOB = {
    "en": "Shops, restaurants, halls, mosques, workshops, events and site offices; wall-mount and duct where a fixed install is wanted.",
    "ar": "المحلات والمطاعم والقاعات والمساجد والورش والفعاليات ومكاتب المواقع، مع إمكانية التثبيت على الجدار والتوصيل بمجاري الهواء.",
}
APPS_HOME = {
    "en": "Homes, offices, shops, clinics and small restaurants.",
    "ar": "المنازل والمكاتب والمحلات والعيادات والمطاعم الصغيرة.",
}


def fam(slug, category, name, image, gallery, kind, summary, models, specs, area, apps, **extra):
    """kind: (english noun phrase, arabic noun phrase) used for the headline."""
    af = [v for k, vals in specs if k == "airflow" for v in vals]
    nums = sorted({int(x.split("–")[0].replace(",", "")) for x in af} | {int(x.split("–")[-1].replace(",", "")) for x in af})
    rng = f"{nums[0]:,}" if nums[0] == nums[-1] else f"{nums[0]:,}–{nums[-1]:,}"
    return {
        "slug": slug, "category": category, "name": name, "image": image, "gallery": gallery,
        "headline": {"en": f"{rng} m³/h {kind[0]}", "ar": f"{kind[1]} بتدفق {rng} م³/ساعة"},
        "summary": summary, "models": models, "specs": specs, "area": area, "apps": apps, **extra,
    }


PRODUCTS = [
    # ---------------------------------------------------------------- industrial
    fam(
        "cm-18-25-centrifugal", "industrial", "CM-18 / 22 / 25 Centrifugal", "coolmax/18tc", ["coolmax/18sc", "coolmax/18dc", "coolmax/banner-cooler"],
        ("industrial centrifugal air cooler", "مكيف صحراوي صناعي بمروحة طاردة"),
        {
            "en": "Our best-selling Coolmax industrial cooler. Centrifugal fan with 210–255 Pa air pressure for long duct runs, 670×670 mm outlet, "
                  "and top, side or down discharge. Choose the new external-rotor motor for lower noise, 1-phase or 3-phase power, and a tank from 30 to 490 L.",
            "ar": "أكثر مكيفات كولماكس الصناعية مبيعاً. مروحة طاردة بضغط هواء 210–255 باسكال تناسب مجاري الهواء الطويلة، ومخرج 670×670 مم، "
                  "وتصريف علوي أو جانبي أو سفلي. اختر المحرك الجديد ذا الدوار الخارجي لضجيج أقل، وكهرباء أحادية أو ثلاثية الطور، وخزاناً من 30 إلى 490 لتراً.",
        },
        [["CM-18TC/SC/DC", {"en": "New · external rotor", "ar": "جديد · دوار خارجي"}], ["CM-22TC/SC/DC", {"en": "New · external rotor", "ar": "جديد · دوار خارجي"}],
         ["CM-18TC/SC/DC"], ["CM-22TC/SC/DC", {"en": "750 W", "ar": "750 واط"}], ["CM-22TC/SC/DC", {"en": "1100 W", "ar": "1100 واط"}], ["CM-25TC/DC"]],
        [
            ("power", ["950 W", "950 W", "750 W", "750 W", "1,100 W", "1,500 W"]),
            ("motor", ["External rotor motor", "External rotor motor", "Conventional motor", "Conventional motor", "Conventional motor", "Conventional motor"]),
            ("airflow", ["14,000", "15,000", "13,000", "15,000", "15,000", "17,000"]),
            ("voltage", [V3] * 6),
            ("speed", [INV] * 6),
            ("fan", [CEN] * 6),
            ("dim", ["1080×1080×980", "1080×1080×1180", "1080×1080×980", "1150×1150×1180", "1150×1150×1180", "1300×1300×980"]),
            ("area", ["90–110 m²", "130–160 m²", "120–150 m²", "120–150 m²", "120–150 m²", "150–180 m²"]),
            ("noise", ["60", "65", "65", "70", "70", "73"]),
            ("pressure", ["210", "230", "210", "235", "235", "255"]),
            ("weight", ["53", "58", "60", "80", "80", "95"]),
            ("outlet", ["670×670 mm"] * 6),
            ("water", ["30/120/260/360"] * 5 + ["45/260/490"]),
        ],
        "90–180 m²", APPS_IND, featured=True,
    ),
    fam(
        "cm-30-50-centrifugal", "industrial", "CM-30 / 40 / 50 Centrifugal", "coolmax/30tc", ["coolmax/50tc"],
        ("industrial centrifugal air cooler", "مكيف صحراوي صناعي بمروحة طاردة"),
        {
            "en": "Large centrifugal coolers for big halls and factories: 20,000–25,000 m³/h, up to 350 Pa air pressure, 800–900 mm outlets and up to 250 m² per unit.",
            "ar": "مكيفات طاردة كبيرة للقاعات والمصانع الكبيرة: تدفق 20,000–25,000 م³/ساعة، وضغط هواء حتى 350 باسكال، ومخارج 800–900 مم، ومساحة تبريد تصل إلى 250 م² للوحدة.",
        },
        [["CM-30TC/SC/DC"], ["CM-40TC/DC"], ["CM-50TC/SC/DC"]],
        [
            ("power", ["1,500 W", "1,500 W", "2,200 W"]),
            ("airflow", ["20,000", "23,000", "25,000"]),
            ("voltage", [V3] * 3),
            ("speed", [INV] * 3),
            ("fan", [CEN] * 3),
            ("dim", ["1300×1300×1180", "1300×1300×1500", "1500×1500×1500"]),
            ("area", ["150–200 m²", "180–200 m²", "200–250 m²"]),
            ("noise", ["70", "70", "75"]),
            ("pressure", ["300", "327", "350"]),
            ("weight", ["100", "120", "150"]),
            ("outlet", ["800×800 mm", "800×800 mm", "900×900 mm"]),
            ("water", ["45/260/490", "45/260/490", "60/620"]),
        ],
        "150–250 m²", APPS_IND,
    ),
    fam(
        "cm-18-25-axial", "industrial", "CM-18 / 22 / 25 Axial", "coolmax/18ta", ["coolmax/18sa"],
        ("industrial axial air cooler", "مكيف صحراوي صناعي بمروحة محورية"),
        {
            "en": "Axial-fan industrial coolers that move the most air per watt: 18,000–25,000 m³/h with top, side or down discharge and single-speed or inverter control.",
            "ar": "مكيفات صناعية بمروحة محورية توفر أعلى تدفق هواء لكل واط: 18,000–25,000 م³/ساعة بتصريف علوي أو جانبي أو سفلي وتحكم سرعة واحدة أو إنفرتر.",
        },
        [["CM-18TA/SA/DA"], ["CM-22TA/SA/DA"], ["CM-25TA/DA"]],
        [
            ("power", ["1,100 / 1,500 W", "1,500 W", "2,200 W"]),
            ("airflow", ["18,000–20,000", "22,000", "25,000"]),
            ("voltage", [V3A] * 3),
            ("speed", [SPD] * 3),
            ("fan", [AX] * 3),
            ("dim", ["1080×1080×980", "1080×1080×1180", "1300×1300×980"]),
            ("area", ["80–100 m²", "120–150 m²", "120–150 m²"]),
            ("noise", ["70", "70", "79"]),
            ("weight", ["55", "70", "85"]),
            ("outlet", ["670×670 mm", "670×670 mm", "800×800 mm"]),
            ("water", ["35/120/260/360", "35/120/260/360", "45/260/490"]),
        ],
        "80–150 m²", APPS_IND,
    ),
    fam(
        "cm-30-50-axial", "industrial", "CM-30 / 40 / 50 Axial", "coolmax/30ta", ["coolmax/30sa"],
        ("industrial axial air cooler", "مكيف صحراوي صناعي بمروحة محورية"),
        {
            "en": "The highest-airflow Coolmax units: 30,000–50,000 m³/h axial coolers for warehouses, farms and open-sided sheds, covering up to 250 m² each.",
            "ar": "أعلى وحدات كولماكس تدفقاً: مكيفات محورية بتدفق 30,000–50,000 م³/ساعة للمستودعات والمزارع والمظلات المفتوحة، تغطي حتى 250 م² للوحدة.",
        },
        [["CM-30TA/SA/DA"], ["CM-40TA/SA/DA"], ["CM-50TA/DA"]],
        [
            ("power", ["3,000 W", "3,500 W", "4,500 W"]),
            ("airflow", ["30,000", "40,000", "50,000"]),
            ("voltage", [V3A] * 3),
            ("speed", [SPD] * 3),
            ("fan", [AX] * 3),
            ("dim", ["1300×1300×1180", "1300×1300×1500", "1500×1500×1500"]),
            ("area", ["150–180 m²", "150–200 m²", "200–250 m²"]),
            ("noise", ["79", "79", "85"]),
            ("weight", ["100", "120", "125"]),
            ("outlet", ["800×800 mm", "800×800 mm", "900×900 mm"]),
            ("water", ["45/260/490", "45/260/490", "60/620"]),
        ],
        "150–250 m²", APPS_IND,
    ),
    # ---------------------------------------------------------------- mobile
    fam(
        "cm-n18", "mobile", "CM-N18 Centrifugal", "coolmax/n18", [],
        ("mobile centrifugal air cooler", "مكيف صحراوي متنقل بمروحة طاردة"),
        {
            "en": "The largest mobile Coolmax with dual evaporation pads: 13,000–14,000 m³/h, 670×670 mm duct outlet, 65 or 135 L tank, 1-phase or 3-phase.",
            "ar": "أكبر مكيف كولماكس متنقل بوسائد تبخير مزدوجة: تدفق 13,000–14,000 م³/ساعة، ومخرج 670×670 مم، وخزان 65 أو 135 لتراً، وكهرباء أحادية أو ثلاثية الطور.",
        },
        [["CM-N18TC"], ["CM-N18TC-L"], ["CM-N18SC"], ["CM-N18SC-L"]],
        [
            ("power", ["950 W", "950 W", "750 W", "750 W"]),
            ("motor", ["External rotor motor", "External rotor motor", "Conventional motor", "Conventional motor"]),
            ("airflow", ["14,000", "14,000", "13,000", "13,000"]),
            ("voltage", [V3] * 4),
            ("speed", [SPD] * 4),
            ("dim", ["1040×1040×920", "1040×1040×1060", "1040×1040×920", "1040×1040×1060"]),
            ("area", ["90–110 m²", "90–110 m²", "120–150 m²", "120–150 m²"]),
            ("noise", ["60", "60", "70", "70"]),
            ("weight", ["57", "57", "61", "61"]),
            ("outlet", ["670×670 mm"] * 4),
            ("water", ["65", "135", "65", "135"]),
        ],
        "90–150 m²", APPS_MOB,
    ),
    fam(
        "cm-n700", "mobile", "CM-N700", "coolmax/n700", [],
        ("mobile air cooler", "مكيف صحراوي متنقل"),
        {
            "en": "8,000 m³/h mobile cooler with dual evaporation pads and inverter control. Only 200 W, top or side outlet, 40 or 85 L tank.",
            "ar": "مكيف متنقل بتدفق 8,000 م³/ساعة بوسائد تبخير مزدوجة وتحكم إنفرتر. استهلاك 200 واط فقط، بمخرج علوي أو جانبي وخزان 40 أو 85 لتراً.",
        },
        [["CM-N700T"], ["CM-N700T-L"], ["CM-N700S"], ["CM-N700S-L"]],
        [
            ("power", ["200 W"] * 4),
            ("airflow", ["8,000"] * 4),
            ("voltage", [V1] * 4),
            ("speed", [INV] * 4),
            ("dim", ["820×820×930", "820×820×1000", "820×820×930", "820×820×1000"]),
            ("area", ["60–80 m²"] * 4),
            ("noise", ["50"] * 4),
            ("weight", ["32", "34", "32", "34"]),
            ("outlet", ["555×555 mm", "555×555 mm", "515×515 mm", "515×515 mm"]),
            ("water", ["40", "85", "40", "85"]),
        ],
        "60–80 m²", APPS_MOB,
    ),
    fam(
        "cm-n900", "mobile", "CM-N900", "coolmax/n900", [],
        ("mobile air cooler", "مكيف صحراوي متنقل"),
        {
            "en": "10,000–13,000 m³/h mobile cooler with dual evaporation pads, a choice of four motors and 1-phase or 3-phase power.",
            "ar": "مكيف متنقل بتدفق 10,000–13,000 م³/ساعة بوسائد تبخير مزدوجة، مع أربعة خيارات للمحرك وكهرباء أحادية أو ثلاثية الطور.",
        },
        [["CM-N900T"], ["CM-N900T-L"], ["CM-N900S"], ["CM-N900S-L"]],
        [
            ("power", ["250 W", "550 W", "750 W", "850 W"]),
            ("motor", ["3-speed motor", "Conventional motor", "Conventional motor", "External rotor motor"]),
            ("airflow", ["10,000", "12,000", "13,000", "12,000"]),
            ("voltage", [V3] * 4),
            ("speed", [INV] * 4),
            ("dim", ["920×920×910", "920×920×1000", "920×920×910", "920×920×1000"]),
            ("area", ["70–90 m²", "80–100 m²", "120–150 m²", "80–100 m²"]),
            ("noise", ["60", "65", "70", "70"]),
            ("weight", ["38", "40", "38", "40"]),
            ("outlet", ["555×555 mm", "555×555 mm", "515×515 mm", "515×515 mm"]),
            ("water", ["65", "135", "65", "135"]),
        ],
        "70–150 m²", APPS_MOB,
    ),
    fam(
        "cm-600", "mobile", "CM-600", "coolmax/600t", [],
        ("mobile air cooler", "مكيف صحراوي متنقل"),
        {
            "en": "Compact 4,000 m³/h centrifugal mobile cooler with LCD remote, top or side outlet and a 22 or 66 L tank. Ideal for shops and offices.",
            "ar": "مكيف متنقل صغير بمروحة طاردة وتدفق 4,000 م³/ساعة مع شاشة LCD وريموت، بمخرج علوي أو جانبي وخزان 22 أو 66 لتراً. مثالي للمحلات والمكاتب.",
        },
        [["CM-600T"], ["CM-600T-L"], ["CM-600S"], ["CM-600S-L"]],
        [
            ("power", ["350 W"] * 4),
            ("airflow", ["4,000"] * 4),
            ("voltage", [V1] * 4),
            ("controller", [LCD] * 4),
            ("dim", ["670×670×890", "670×670×1060", "670×670×890", "670×670×1060"]),
            ("area", ["40–60 m²"] * 4),
            ("noise", ["60"] * 4),
            ("weight", ["25", "27", "25", "27"]),
            ("outlet", ["365×365 mm"] * 4),
            ("water", ["22", "66", "22", "66"]),
        ],
        "40–60 m²", APPS_MOB,
    ),
    fam(
        "cm-600h", "mobile", "CM-600H", "coolmax/600ht", [],
        ("mobile air cooler", "مكيف صحراوي متنقل"),
        {
            "en": "Taller 600-series cooler with inverter control: 5,000 m³/h, 500 W, 365×365 mm outlet and a 22 or 66 L tank.",
            "ar": "نسخة أطول من سلسلة 600 بتحكم إنفرتر: تدفق 5,000 م³/ساعة، و500 واط، ومخرج 365×365 مم، وخزان 22 أو 66 لتراً.",
        },
        [["CM-600HT"], ["CM-600HT-L"], ["CM-600HS"], ["CM-600HS-L"]],
        [
            ("power", ["500 W"] * 4),
            ("airflow", ["5,000"] * 4),
            ("voltage", [V1] * 4),
            ("speed", [INV] * 4),
            ("dim", ["670×670×1090", "670×670×1260", "670×670×1090", "670×670×1260"]),
            ("area", ["40–60 m²"] * 4),
            ("noise", ["60"] * 4),
            ("weight", ["25", "27", "25", "27"]),
            ("outlet", ["365×365 mm"] * 4),
            ("water", ["22", "66", "22", "66"]),
        ],
        "40–60 m²", APPS_MOB,
    ),
    fam(
        "cm-700", "mobile", "CM-700", "coolmax/700t", [],
        ("mobile air cooler", "مكيف صحراوي متنقل"),
        {
            "en": "8,000 m³/h for just 200 W with inverter control and a quiet 50 dB. Top or side outlet and a 32 or 100 L tank.",
            "ar": "تدفق 8,000 م³/ساعة باستهلاك 200 واط فقط مع تحكم إنفرتر وضجيج هادئ 50 ديسيبل، بمخرج علوي أو جانبي وخزان 32 أو 100 لتر.",
        },
        [["CM-700T"], ["CM-700T-L"], ["CM-700S"], ["CM-700S-L"]],
        [
            ("power", ["200 W"] * 4),
            ("airflow", ["8,000"] * 4),
            ("voltage", [V1] * 4),
            ("speed", [INV] * 4),
            ("dim", ["780×780×915", "780×780×1100", "780×780×915", "780×780×1100"]),
            ("area", ["60–80 m²"] * 4),
            ("noise", ["50"] * 4),
            ("weight", ["31", "33", "31", "33"]),
            ("outlet", ["555×555 mm", "555×555 mm", "515×515 mm", "515×515 mm"]),
            ("water", ["32", "100", "32", "100"]),
        ],
        "60–80 m²", APPS_MOB,
    ),
    fam(
        "cm-700h", "mobile", "CM-700H", "coolmax/700ht", [],
        ("mobile air cooler", "مكيف صحراوي متنقل"),
        {
            "en": "12,000 m³/h from a 250 W inverter motor. Covers 80–100 m² with top or side outlet and a 33 or 109 L tank.",
            "ar": "تدفق 12,000 م³/ساعة من محرك إنفرتر بقدرة 250 واط. يغطي 80–100 م² بمخرج علوي أو جانبي وخزان 33 أو 109 لترات.",
        },
        [["CM-700HT"], ["CM-700HT-L"], ["CM-700HS"], ["CM-700HS-L"]],
        [
            ("power", ["250 W"] * 4),
            ("airflow", ["12,000"] * 4),
            ("voltage", [V1] * 4),
            ("speed", [INV] * 4),
            ("dim", ["780×780×1100", "780×780×1290", "780×780×1100", "780×780×1290"]),
            ("area", ["80–100 m²"] * 4),
            ("noise", ["58"] * 4),
            ("weight", ["33", "35", "33", "35"]),
            ("outlet", ["555×555 mm", "555×555 mm", "515×515 mm", "515×515 mm"]),
            ("water", ["33", "109", "33", "109"]),
        ],
        "80–100 m²", APPS_MOB,
    ),
    fam(
        "cm-900", "mobile", "CM-900", "coolmax/900t", [],
        ("mobile air cooler", "مكيف صحراوي متنقل"),
        {
            "en": "10,000–13,000 m³/h mobile cooler with inverter control, four motor options and a 30 or 135 L tank.",
            "ar": "مكيف متنقل بتدفق 10,000–13,000 م³/ساعة بتحكم إنفرتر وأربعة خيارات للمحرك وخزان 30 أو 135 لتراً.",
        },
        [["CM-900T"], ["CM-900T-L"], ["CM-900S"], ["CM-900S-L"]],
        [
            ("power", ["250 W", "550 W", "750 W", "850 W"]),
            ("motor", ["3-speed motor", "Conventional motor", "Conventional motor", "External rotor motor"]),
            ("airflow", ["10,000", "12,000", "13,000", "12,000"]),
            ("voltage", [V1] * 4),
            ("speed", [INV] * 4),
            ("dim", ["960×960×940", "960×960×1050", "960×960×940", "960×960×1050"]),
            ("area", ["70–90 m²", "80–100 m²", "120–150 m²", "80–100 m²"]),
            ("noise", ["60", "65", "70", "70"]),
            ("weight", ["38", "40", "38", "40"]),
            ("outlet", ["555×555 mm", "555×555 mm", "515×515 mm", "515×515 mm"]),
            ("water", ["30", "135", "30", "135"]),
        ],
        "70–150 m²", APPS_MOB,
    ),
    fam(
        "cm-900h", "mobile", "CM-900H", "coolmax/900ht", [],
        ("mobile air cooler", "مكيف صحراوي متنقل"),
        {
            "en": "Taller 900-series cooler: 12,000–13,000 m³/h, up to 150 m² per unit, inverter control and a 30 or 135 L tank.",
            "ar": "نسخة أطول من سلسلة 900: تدفق 12,000–13,000 م³/ساعة، ومساحة تبريد حتى 150 م² للوحدة، وتحكم إنفرتر، وخزان 30 أو 135 لتراً.",
        },
        [["CM-900HT"], ["CM-900HT-L"], ["CM-900HS"], ["CM-900HS-L"]],
        [
            ("power", ["550 W", "550 W", "750 W", "950 W"]),
            ("motor", ["Conventional motor", "Conventional motor", "Conventional motor", "External rotor motor"]),
            ("airflow", ["12,000", "12,000", "13,000", "12,000"]),
            ("voltage", [V1] * 4),
            ("speed", [INV] * 4),
            ("dim", ["960×960×1120", "960×960×1230", "960×960×1120", "960×960×1120"]),
            ("area", ["80–100 m²", "80–100 m²", "120–150 m²", "120–150 m²"]),
            ("noise", ["60", "60", "70", "70"]),
            ("weight", ["38", "40", "38", "40"]),
            ("outlet", ["555×555 mm", "555×555 mm", "515×515 mm", "515×515 mm"]),
            ("water", ["30", "135", "30", "135"]),
        ],
        "80–150 m²", APPS_MOB,
    ),
    fam(
        "cm-wsc-02", "mobile", "CM-WSC-02 Centrifugal", "coolmax/wsc-02", [],
        ("mobile centrifugal air cooler", "مكيف صحراوي متنقل بمروحة طاردة"),
        {
            "en": "Window-or-wheels centrifugal cooler: 8,000 m³/h at 200 W, LCD remote or manual control, 36 or 110 L tank.",
            "ar": "مكيف بمروحة طاردة يركب على النافذة أو يتحرك على عجلات: تدفق 8,000 م³/ساعة باستهلاك 200 واط، مع شاشة LCD وريموت أو تحكم يدوي، وخزان 36 أو 110 لترات.",
        },
        [["CM-WSC-02T"], ["CM-WSC-M02T"], ["CM-WSC-02S"], ["CM-WSC-M02S"]],
        [
            ("power", ["200 W"] * 4),
            ("airflow", ["8,000"] * 4),
            ("voltage", [V1] * 4),
            ("controller", [LCDM] * 4),
            ("fan", [CEN] * 4),
            ("dim", ["700×700×800", "700×700×1200", "700×700×800", "700×700×1200"]),
            ("area", ["60–80 m²"] * 4),
            ("noise", ["50"] * 4),
            ("weight", ["34", "36", "34", "36"]),
            ("outlet", ["555×555 mm", "555×555 mm", "515×515 mm", "515×515 mm"]),
            ("water", ["36", "110", "36", "110"]),
        ],
        "60–80 m²", APPS_MOB,
    ),
    fam(
        "cm-wsc-03", "mobile", "CM-WSC-03 Centrifugal", "coolmax/wsc-03", [],
        ("mobile centrifugal air cooler", "مكيف صحراوي متنقل بمروحة طاردة"),
        {
            "en": "12,000 m³/h centrifugal cooler from 250 W, for window mounting or on wheels, with LCD remote or manual control.",
            "ar": "مكيف بمروحة طاردة بتدفق 12,000 م³/ساعة من 250 واط، للتركيب على النافذة أو على عجلات، مع شاشة LCD وريموت أو تحكم يدوي.",
        },
        [["CM-WSC-03T"], ["CM-WSC-M03T"], ["CM-WSC-03S"], ["CM-WSC-M03S"]],
        [
            ("power", ["250 W"] * 4),
            ("airflow", ["12,000"] * 4),
            ("voltage", [V1] * 4),
            ("controller", [LCDM] * 4),
            ("fan", [CEN] * 4),
            ("dim", ["700×700×800", "700×700×1200", "700×700×800", "700×700×1200"]),
            ("area", ["60–80 m²"] * 4),
            ("noise", ["58"] * 4),
            ("weight", ["36", "38", "36", "38"]),
            ("outlet", ["555×555 mm", "555×555 mm", "515×515 mm", "515×515 mm"]),
            ("water", ["36", "110", "36", "110"]),
        ],
        "60–80 m²", APPS_MOB,
    ),
    fam(
        "cm-wsa-02", "mobile", "CM-WSA-02 Axial", "coolmax/wsa-02", [],
        ("mobile axial air cooler", "مكيف صحراوي متنقل بمروحة محورية"),
        {
            "en": "Axial version of the WSC-02: 8,000 m³/h at 200 W, LCD remote or manual control, window mount or wheels.",
            "ar": "النسخة المحورية من WSC-02: تدفق 8,000 م³/ساعة باستهلاك 200 واط، مع شاشة LCD وريموت أو تحكم يدوي، للتركيب على النافذة أو على عجلات.",
        },
        [["CM-WSA-02T"], ["CM-WSA-M02T"], ["CM-WSA-02S"], ["CM-WSA-M02S"]],
        [
            ("power", ["200 W"] * 4),
            ("airflow", ["8,000"] * 4),
            ("voltage", [V1] * 4),
            ("controller", [LCDM] * 4),
            ("fan", [AX] * 4),
            ("dim", ["700×700×800", "700×700×1200", "700×700×800", "700×700×1200"]),
            ("area", ["60–80 m²"] * 4),
            ("noise", ["50"] * 4),
            ("weight", ["34", "36", "34", "36"]),
            ("outlet", ["555×555 mm", "555×555 mm", "515×515 mm", "515×515 mm"]),
            ("water", ["36", "110", "36", "110"]),
        ],
        "60–80 m²", APPS_MOB,
    ),
    fam(
        "cm-wsa-03", "mobile", "CM-WSA-03 Axial", "coolmax/wsa-03", [],
        ("mobile axial air cooler", "مكيف صحراوي متنقل بمروحة محورية"),
        {
            "en": "Axial version of the WSC-03: 12,000 m³/h at 250 W with LCD remote or manual control and a 36 or 110 L tank.",
            "ar": "النسخة المحورية من WSC-03: تدفق 12,000 م³/ساعة باستهلاك 250 واط مع شاشة LCD وريموت أو تحكم يدوي وخزان 36 أو 110 لترات.",
        },
        [["CM-WSA-03T"], ["CM-WSA-M03T"], ["CM-WSA-03S"], ["CM-WSA-M03S"]],
        [
            ("power", ["250 W"] * 4),
            ("airflow", ["12,000"] * 4),
            ("voltage", [V1] * 4),
            ("controller", [LCDM] * 4),
            ("fan", [AX] * 4),
            ("dim", ["700×700×800", "700×700×1200", "700×700×800", "700×700×1200"]),
            ("area", ["60–80 m²"] * 4),
            ("noise", ["58"] * 4),
            ("weight", ["36", "38", "36", "38"]),
            ("outlet", ["555×555 mm", "555×555 mm", "515×515 mm", "515×515 mm"]),
            ("water", ["36", "110", "36", "110"]),
        ],
        "60–80 m²", APPS_MOB,
    ),
    fam(
        "cm-900at", "mobile", "CM-900AT Axial", "coolmax/900hat", ["coolmax/900at"],
        ("mobile axial air cooler", "مكيف صحراوي متنقل بمروحة محورية"),
        {
            "en": "Simple, rugged axial mobile cooler with a manual controller: 11,500–13,500 m³/h, 670×670 mm top outlet and a 135 L tank.",
            "ar": "مكيف متنقل محوري بسيط ومتين بتحكم يدوي: تدفق 11,500–13,500 م³/ساعة، ومخرج علوي 670×670 مم، وخزان 135 لتراً.",
        },
        [["CM-900AT"], ["CM-900HAT"]],
        [
            ("power", ["750 W", "1,100 W"]),
            ("airflow", ["11,500", "13,500"]),
            ("voltage", [V1] * 2),
            ("controller", [MAN] * 2),
            ("fan", [AX] * 2),
            ("dim", ["960×960×1050", "960×960×1230"]),
            ("area", ["50–80 m²", "80–150 m²"]),
            ("noise", ["65", "65"]),
            ("weight", ["32", "34"]),
            ("outlet", ["670×670 mm"] * 2),
            ("water", ["135", "135"]),
        ],
        "50–150 m²", APPS_MOB,
    ),
    fam(
        "cm-p-series", "mobile", "CM-P18 / P22 / P30 Axial", "coolmax/p22at", ["coolmax/p18at", "coolmax/p30at"],
        ("heavy-duty mobile air cooler", "مكيف صحراوي متنقل للخدمة الشاقة"),
        {
            "en": "Heavy-duty mobile coolers with a 260–300 L tank for long shifts: 18,000–30,000 m³/h, single-speed or inverter, 1-phase or 3-phase.",
            "ar": "مكيفات متنقلة للخدمة الشاقة بخزان 260–300 لتر للورديات الطويلة: تدفق 18,000–30,000 م³/ساعة، بسرعة واحدة أو إنفرتر، وكهرباء أحادية أو ثلاثية الطور.",
        },
        [["CM-P18AT", {"en": "1100 W", "ar": "1100 واط"}], ["CM-P18AT", {"en": "1500 W", "ar": "1500 واط"}], ["CM-P22AT"], ["CM-P30AT"]],
        [
            ("power", ["1,100 W", "1,500 W", "2,200 W", "3,000 W"]),
            ("airflow", ["18,000", "22,000", "25,000", "30,000"]),
            ("voltage", [V3A] * 4),
            ("speed", [SPD] * 4),
            ("fan", [AX] * 4),
            ("dim", ["1100×1100×1120 (1900 with outlet)", "1100×1100×1120 (1900 with outlet)", "1100×1100×1300 (2280 with outlet)", "1200×1200×1360 (2500 with outlet)"]),
            ("area", ["80–100 m²", "120–150 m²", "80–100 m²", "80–100 m²"]),
            ("noise", ["70", "70", "79", "79"]),
            ("weight", ["60", "60", "75", "125"]),
            ("water", ["260", "260", "260", "300"]),
        ],
        "80–150 m²", APPS_MOB,
    ),
    fam(
        "cm-big-portable", "mobile", "CM-18000 to CM-50000", "coolmax/big-35000", ["coolmax/big-18000", "coolmax/big-23000", "coolmax/big-50000"],
        ("large portable air cooler", "مكيف صحراوي متنقل كبير"),
        {
            "en": "Big-cabinet portable coolers for events, workshops and outdoor seating: 18,000–50,000 m³/h with a 150 L tank and no installation needed.",
            "ar": "مكيفات متنقلة كبيرة للفعاليات والورش والجلسات الخارجية: تدفق 18,000–50,000 م³/ساعة مع خزان 150 لتراً ودون حاجة إلى تركيب.",
        },
        [["CM-18000"], ["CM-23000"], ["CM-35000"], ["CM-50000"]],
        [
            ("power", ["550 W", "750 W", "750 W", "1,500 W"]),
            ("airflow", ["18,000", "23,000", "35,000", "50,000"]),
            ("controller", [MAN, LCDM, MAN, MAN]),
            ("dim", ["1050×690×1450", "1160×670×1450", "1160×670×1500", "1150×650×1600"]),
            ("area", ["80–100 m²", "100–120 m²", "120–140 m²", "150–200 m²"]),
            ("noise", ["68", "68", "70", "79"]),
            ("water", ["150"] * 4),
        ],
        "80–200 m²", APPS_MOB,
    ),
    # ---------------------------------------------------------------- window
    fam(
        "cm-window", "window", "CM-WSA / 09CM / WSC Window", "coolmax/window-wsa", ["coolmax/window-09cm", "coolmax/window-wsc"],
        ("window air cooler", "مكيف صحراوي للنوافذ"),
        {
            "en": "Window coolers for rooms, shops and offices: 5,000 m³/h axial or centrifugal at 150 W, or the 10,000 m³/h CM-09CM for larger spaces. LCD with remote on every model.",
            "ar": "مكيفات نوافذ للغرف والمحلات والمكاتب: 5,000 م³/ساعة بمروحة محورية أو طاردة باستهلاك 150 واط، أو CM-09CM بتدفق 10,000 م³/ساعة للمساحات الأكبر. شاشة LCD وريموت في جميع الموديلات.",
        },
        [["CM-WSA"], ["CM-09CM"], ["CM-WSC"]],
        [
            ("power", ["150 W", "450 W", "150 W"]),
            ("airflow", ["5,000", "10,000", "5,000"]),
            ("voltage", [V1] * 3),
            ("controller", [LCD] * 3),
            ("fan", [AX, AX, CEN]),
            ("dim", ["765×765×875", "1100×700×1030", "765×765×875"]),
            ("area", ["30–50 m²", "60–80 m²", "30–50 m²"]),
            ("noise", ["≤60", "≤60", "≤58"]),
            ("weight", ["35/36", "40", "35/36"]),
            ("water", ["20/45", "30", "20/45"]),
        ],
        "30–80 m²", APPS_HOME,
    ),
    fam(
        "cm-wsc-01", "window", "CM-WSC-01 Compact", "coolmax/wsc-01s", [],
        ("compact window air cooler", "مكيف صحراوي صغير للنوافذ"),
        {
            "en": "The smallest Coolmax: 5,000–5,800 m³/h centrifugal cooler at 100–180 W, quiet at 50 dB, for bedrooms, offices and kiosks.",
            "ar": "أصغر مكيفات كولماكس: مكيف بمروحة طاردة بتدفق 5,000–5,800 م³/ساعة باستهلاك 100–180 واط، وهادئ عند 50 ديسيبل، لغرف النوم والمكاتب والأكشاك.",
        },
        [["CM-WSC-01S"], ["CM-WSC-M01S-L"], ["CM-WSC-LM01S"], ["CM-WSC-LM01S-L"]],
        [
            ("power", ["100 W", "100 W", "180 W", "180 W"]),
            ("airflow", ["5,000", "5,000", "5,800", "5,800"]),
            ("voltage", [V1] * 4),
            ("controller", [LCD] * 4),
            ("fan", [CEN] * 4),
            ("dim", ["560×560×650", "560×560×650", "560×560×720", "560×560×1020"]),
            ("area", ["20–50 m²", "20–50 m²", "30–55 m²", "30–55 m²"]),
            ("noise", ["≤50"] * 4),
            ("weight", ["20", "21", "22", "23"]),
            ("water", ["20", "45", "20", "45"]),
        ],
        "20–55 m²", APPS_HOME,
    ),
    # ---------------------------------------------------------------- home
    fam(
        "cm-j-plastic", "home", "CM-J Plastic Series", "coolmax/j-plastic", ["coolmax/j-plastic-2"],
        ("home and shop air cooler", "مكيف صحراوي للمنازل والمحلات"),
        {
            "en": "Plastic-body room coolers in five sizes, from 6,000 to 23,000 m³/h, with manual or touch-screen remote control, ice-box slot and 50–120 L tanks.",
            "ar": "مكيفات غرف بهيكل بلاستيكي بخمسة مقاسات من 6,000 إلى 23,000 م³/ساعة، بتحكم يدوي أو شاشة لمس مع ريموت، ومكان لصناديق الثلج، وخزانات 50–120 لتراً.",
        },
        [["CM-J1050B"], ["CM-J1050"], ["CM-J1250"], ["CM-J1380"], ["CM-J1530"]],
        [
            ("power", ["160 W", "160 W", "230 W", "360 W", "480 W"]),
            ("airflow", ["6,000", "6,000", "9,000", "15,000", "23,000"]),
            ("voltage", [V1] * 5),
            ("controller", ["Manual controller or touch screen with remote"] * 5),
            ("dim", ["530×380×1050", "530×380×1050", "620×420×1250", "690×460×1380", "780×530×1530"]),
            ("area", ["20–50 m²", "20–50 m²", "50–80 m²", "70–100 m²", "100–130 m²"]),
            ("noise", ["45", "45", "50", "54", "58"]),
            ("weight", ["14.5", "13", "18.5", "21", "27"]),
            ("water", ["50", "50", "60", "80", "120"]),
        ],
        "20–130 m²", APPS_HOME,
    ),
    fam(
        "cm-j-metal", "home", "CM-J Metal Series", "coolmax/j-metal", [],
        ("metal-body air cooler", "مكيف صحراوي بهيكل معدني"),
        {
            "en": "Metal-body versions of the J series for shops and workshops that need a tougher cabinet: 6,000–9,000 m³/h with an 80 or 120 L tank.",
            "ar": "نسخ بهيكل معدني من سلسلة J للمحلات والورش التي تحتاج هيكلاً أقوى: تدفق 6,000–9,000 م³/ساعة مع خزان 80 أو 120 لتراً.",
        },
        [["CM-J1380T"], ["CM-J1530T"]],
        [
            ("power", ["360 W", "480 W"]),
            ("airflow", ["6,000", "9,000"]),
            ("voltage", [V1] * 2),
            ("controller", ["Manual controller or touch screen with remote"] * 2),
            ("dim", ["690×460×1380", "780×530×1530"]),
            ("area", ["70–100 m²", "100–200 m²"]),
            ("noise", ["54", "58"]),
            ("weight", ["25", "33"]),
            ("water", ["80", "120"]),
        ],
        "70–200 m²", APPS_HOME,
    ),
]

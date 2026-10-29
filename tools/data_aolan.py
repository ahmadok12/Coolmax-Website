"""Aolan product data, transcribed from the 2026 Aolan Evaporative Air Cooler catalogue.

Spec values are kept as printed in the catalogue. Plain strings are shared by both
languages; common words inside them (Axial, Optional, LED + remote, ...) are translated
by site.tr_value(). Use {"en": ..., "ar": ...} for anything that needs its own text.
"""

BRAND = {
    "slug": "aolan",
    "name": "Aolan",
    "legal": "Aolan (Fujian) Industry Co., Ltd",
    "logo_text": "AOLAN",
    "status": "live",
    "origin": {"en": "Fuzhou, China", "ar": "فوتشو، الصين"},
    "tagline": {
        "en": "Evaporative air coolers since 1998: home, outdoor and industrial ranges",
        "ar": "مكيفات صحراوية (مبردات هواء تبخيرية) منذ 1998 للمنازل والمساحات المفتوحة والمصانع",
    },
    "facts": [
        {"n": "1998", "en": "Making evaporative coolers since", "ar": "تصنيع المبردات التبخيرية منذ"},
        {"n": "70+", "en": "Export countries and regions", "ar": "دولة ومنطقة تصدير"},
        {"n": "40+", "en": "National patents", "ar": "براءة اختراع"},
        {"n": "CE · SASO · BV", "en": "International approvals", "ar": "شهادات دولية"},
    ],
    "about": {
        "en": [
            "Aolan (Fujian) Industry Co., Ltd researches, develops, manufactures and services evaporative air coolers, "
            "indirect evaporative (dew point) cooling systems and liquid desiccant air conditioning. Aolan brought "
            "energy-saving coolers to the Chinese market in 1998 and has since grown into a leading evaporative cooling manufacturer.",
            "The factory runs under ISO 9001, ISO 14001 and OHSAS 18001, holds more than 40 national patents, and its products "
            "carry CE, SASO and BV approvals. Aolan coolers are exported to more than 70 countries and regions across Europe, "
            "the Americas, Australia, the Middle East, Asia and Africa.",
        ],
        "ar": [
            "شركة أولان (فوجيان) للصناعة متخصصة في تطوير وتصنيع وصيانة المكيفات الصحراوية (مبردات الهواء التبخيرية) "
            "وأنظمة التبريد التبخيري غير المباشر وأنظمة التكييف بالمجففات السائلة. بدأت أولان إنتاج المبردات الموفرة للطاقة عام 1998 "
            "وأصبحت اليوم من الشركات الرائدة في مجال التبريد التبخيري.",
            "يعمل المصنع وفق معايير ISO 9001 وISO 14001 وOHSAS 18001، ويمتلك أكثر من 40 براءة اختراع، "
            "وتحمل منتجاته شهادات CE وSASO (المملكة العربية السعودية) وBV. تُصدَّر منتجات أولان إلى أكثر من 70 دولة "
            "في أوروبا والأمريكتين وأستراليا والشرق الأوسط وآسيا وأفريقيا.",
        ],
    },
}

CATEGORIES = [
    {
        "slug": "chiller",
        "en": "Mini chillers (evaporative AC)",
        "ar": "ميني تشيلر (تكييف تبخيري)",
        "desc": {
            "en": "New for 2026: compressor cooling with an evaporative-cooled outdoor unit, 25–35 kW, connected with PVC water pipes only.",
            "ar": "جديد 2026: تبريد بالكمبروسر مع وحدة خارجية مبردة تبخيرياً، بقدرة 25–35 كيلوواط، وتوصيل بأنابيب مياه PVC فقط.",
        },
    },
    {
        "slug": "industrial",
        "en": "Industrial air coolers",
        "ar": "مكيفات صحراوية صناعية",
        "desc": {
            "en": "Roof, wall and duct-mounted units from 10,000 to 80,000 m³/h for factories, warehouses, poultry and greenhouses.",
            "ar": "وحدات تركب على السطح أو الجدار أو مع مجاري الهواء بتدفق من 10,000 إلى 80,000 م³/ساعة للمصانع والمستودعات والدواجن والبيوت المحمية.",
        },
    },
    {
        "slug": "outdoor",
        "en": "Portable & outdoor coolers",
        "ar": "مكيفات صحراوية متنقلة وخارجية",
        "desc": {
            "en": "Mobile coolers from 6,000 to 30,000 m³/h for shops, halls, restaurants, construction sites and events, including solar DC models.",
            "ar": "مبردات متنقلة بتدفق من 6,000 إلى 30,000 م³/ساعة للمحلات والقاعات والمطاعم ومواقع البناء والفعاليات، ومنها موديلات تعمل بالطاقة الشمسية.",
        },
    },
    {
        "slug": "home",
        "en": "Home & office coolers",
        "ar": "مبردات هواء منزلية ومكتبية",
        "desc": {
            "en": "Compact room coolers from 200 to 4,500 m³/h for homes, offices, hotels and retail shelves.",
            "ar": "مبردات غرف صغيرة بتدفق من 200 إلى 4,500 م³/ساعة للمنازل والمكاتب والفنادق ومحلات التجزئة.",
        },
    },
    {
        "slug": "ventilation",
        "en": "Extraction fans & cooling pads",
        "ar": "شفاطات صناعية وخلايا تبريد",
        "desc": {
            "en": "Fan and pad systems for greenhouses, poultry houses and workshops.",
            "ar": "أنظمة الشفاطات وخلايا التبريد للبيوت المحمية ومزارع الدواجن والورش.",
        },
    },
]

OPT = "Optional"
DIS = {"en": "X = down, S = up, C = side discharge", "ar": "X = تصريف سفلي، S = تصريف علوي، C = تصريف جانبي"}

PRODUCTS = [
    # ------------------------------------------------------------------ mini chiller (2026 launch)
    {
        "slug": "mini-chiller",
        "category": "chiller",
        "name": "Mini Chiller",
        "new": True,
        "image": "mini-chiller",
        "gallery": ["mini-chiller-units", "mini-chiller-ceiling", "mini-chiller-cases"],
        "headline": {"en": "25–35 kW evaporative-condensed mini chiller", "ar": "ميني تشيلر بتكثيف تبخيري بقدرة 25–35 كيلوواط"},
        "summary": {
            "en": "Aolan's new Mini Chiller, launched at the 2026 Canton Fair, combines compressor refrigeration with evaporative cooling. "
            "The indoor unit cools the air like an air conditioner, and the heat is carried by circulating water to an outdoor unit "
            "that rejects it through wet cooling pads. The result is real AC-level cooling with a COP of 5 and 30–50% lower energy use "
            "than traditional air conditioning, installed with nothing more than PVC water pipes.",
            "ar": "الميني تشيلر الجديد من أولان، الذي أُطلق في معرض كانتون 2026، يجمع بين التبريد بالكمبروسر والتبريد التبخيري. "
            "تبرد الوحدة الداخلية الهواء مثل المكيف، وتُنقل الحرارة بالماء المتداول إلى وحدة خارجية تطردها عبر خلايا تبريد مبللة. "
            "والنتيجة تبريد حقيقي بمستوى المكيفات بمعامل أداء COP يبلغ 5 واستهلاك طاقة أقل بنسبة 30–50% من المكيفات التقليدية، "
            "مع تركيب بسيط بأنابيب مياه PVC فقط.",
        },
        "apps": {
            "en": "Industrial and commercial spaces: factory workshops, warehousing and logistics, pharmaceutical manufacturing, offices and showrooms.",
            "ar": "المساحات الصناعية والتجارية: الورش والمصانع، المستودعات والخدمات اللوجستية، مصانع الأدوية، المكاتب وصالات العرض.",
        },
        "models": [["AHK25-ZLB-3B"], ["AHK25-LDS-3B"], ["AHK35-ZLB-3B"], ["AHK35-LDS-3B"]],
        "specs": [
            ("capacity", ["25", "25", "35", "35"]),
            ("power", ["4.3 kW", "4.6 kW", "5.9 kW", "6.3 kW"]),
            ("voltage", ["380 V, 50 Hz"] * 4),
            ("airflow", ["6,000", "6,000", "7,000", "7,000"]),
            ("waterflow", ["4", "4", "4.5", "4.5"]),
            ("cop", ["5"] * 4),
            ("weight", ["Indoor 156, outdoor 110", "Indoor 190, outdoor 110", "Indoor 180, outdoor 110", "Indoor 210, outdoor 110"]),
            ("dim", ["Indoor 800×530×1860, outdoor 800×800×1400", "Indoor 1320×950×790, outdoor 800×800×1400"] * 2),
            ("controller", ["Manual, remote and mobile app"] * 4),
        ],
        "bullets": {
            "en": [
                "High efficiency: saves 30–50% energy compared with traditional air conditioning (COP 5 vs about 3 for air-cooled AC)",
                "Smart control: manual, remote and mobile-app control with on/off, cool/vent modes and fault alarms",
                "Easy to install: indoor and outdoor units connect with PVC water pipes only, no copper or steel piping",
                "Long service life and low maintenance, with an automatic self-cleaning system",
                "Big airflow and long air throw for large workshops and warehouses",
            ],
            "ar": [
                "كفاءة عالية: توفير 30–50% من الطاقة مقارنة بالمكيفات التقليدية (معامل أداء COP 5 مقابل نحو 3 للمكيف المبرد بالهواء)",
                "تحكم ذكي: يدوي وبالريموت وعبر تطبيق الجوال، مع التشغيل والإيقاف وأوضاع التبريد والتهوية وتنبيهات الأعطال",
                "تركيب سهل: توصيل الوحدتين الداخلية والخارجية بأنابيب مياه PVC فقط، بدون نحاس أو حديد",
                "عمر تشغيل طويل وصيانة قليلة مع نظام تنظيف ذاتي أوتوماتيكي",
                "تدفق هواء كبير ومسافة دفع طويلة للورش والمستودعات الكبيرة",
            ],
        },
        "principle": {
            "en": "The indoor unit works like an air conditioner: a compressor, evaporator and expansion valve cool the room air. "
            "Instead of a hot air-cooled condenser, the heat goes into circulating water, which a pump sends to the outdoor unit. "
            "There, outdoor air is drawn through wet cooling pads and the heat leaves by evaporation.",
            "ar": "تعمل الوحدة الداخلية مثل المكيف: كمبروسر ومبخر وصمام تمدد لتبريد هواء المكان. "
            "وبدلاً من مكثف حار مبرد بالهواء، تنتقل الحرارة إلى ماء متداول تدفعه مضخة إلى الوحدة الخارجية، "
            "حيث يُسحب الهواء الخارجي عبر خلايا تبريد مبللة وتخرج الحرارة بالتبخير.",
        },
        "comparison": {
            "cols": {
                "en": ["", "Air-cooled AC", "Water-cooled AC", "Mini Chiller"],
                "ar": ["", "مكيف مبرد بالهواء", "مكيف مبرد بالماء", "ميني تشيلر"],
            },
            "rows": {
                "en": [
                    ("Initial investment", "Low cost, for small production sites", "High cost, for big production sites", "Close to air-cooled AC for the same cooling"),
                    ("COP", "3", "4–4.5", "5"),
                    ("Installation", "Copper pipes welded indoors and outdoors by professionals", "Large, heavy metal pipelines for chilled and cooling water", "PVC pipes only, easy to install"),
                    ("Maintenance", "Filter cleaning, small workload", "Filters, descaling, evaporative fill: big workload", "Automatic self-cleaning; filter and pad care, moderate workload"),
                    ("Cooling effect", "Small airflow, low cooling rate", "Mostly small airflow, low cooling rate", "Big airflow, high cooling rate, longer air throw"),
                    ("Remote control", "Only on high-spec models", "Needs professionals to start, stop and control", "Manual and remote on/off, cool/vent, fault alarm"),
                ],
                "ar": [
                    ("الاستثمار الأولي", "تكلفة منخفضة، للمواقع الصغيرة", "تكلفة عالية، للمواقع الكبيرة", "قريب من المكيف المبرد بالهواء لنفس قدرة التبريد"),
                    ("معامل الأداء COP", "3", "4–4.5", "5"),
                    ("التركيب", "أنابيب نحاس تُلحم داخلياً وخارجياً بواسطة فنيين", "أنابيب معدنية كبيرة وثقيلة للمياه المبردة ومياه التبريد", "أنابيب PVC فقط، تركيب سهل"),
                    ("الصيانة", "تنظيف الفلتر، عمل قليل", "فلاتر وإزالة ترسبات وحشوات تبخير: عمل كبير", "تنظيف ذاتي أوتوماتيكي، وعناية بالفلتر والخلايا: عمل متوسط"),
                    ("أداء التبريد", "تدفق هواء صغير وتبريد ضعيف", "غالباً تدفق صغير وتبريد ضعيف", "تدفق هواء كبير وتبريد قوي ومسافة دفع أطول"),
                    ("التحكم عن بعد", "فقط في الموديلات المتقدمة", "يحتاج فنيين للتشغيل والإيقاف والتحكم", "تشغيل وإيقاف يدوي وعن بعد، تبريد/تهوية، تنبيه أعطال"),
                ],
            },
        },
        "source": {"en": "Aolan Mini Chiller brochure (2026)", "ar": "كتيب أولان ميني تشيلر (2026)"},
    },
    # ------------------------------------------------------------------ industrial
    {
        "slug": "wind-supremo",
        "category": "industrial",
        "name": "Wind Supremo",
        "featured": True,
        "image": "wind-supremo",
        "gallery": ["wind-supremo-row", "wind-supremo-detail", "wind-supremo-app"],
        "headline": {"en": "18,000 m³/h industrial evaporative air cooler", "ar": "مكيف صحراوي صناعي بتدفق 18,000 م³/ساعة"},
        "summary": {
            "en": "Aolan's best-selling 18,000 m³/h industrial cooler. Four-side air intake, 190 Pa static pressure for duct runs, "
            "and a choice of up, down or side discharge. Available with silicon-control or inverter fan speed, a 3-phase version, "
            "and a deep water tank for sites with unreliable water supply.",
            "ar": "أكثر مكيفات أولان الصناعية مبيعاً بتدفق 18,000 م³/ساعة. سحب هواء من الجهات الأربع وضغط استاتيكي 190 باسكال يناسب مجاري الهواء، "
            "مع إمكانية التصريف العلوي أو السفلي أو الجانبي. متوفر بتحكم سيليكون أو إنفرتر، وبنسخة ثلاثية الطور، وبخزان مياه عميق للمواقع "
            "ذات إمداد المياه غير المستقر.",
        },
        "area": "100–120 m²",
        "apps": {
            "en": "Industrial plants, semi-open spaces, exhibition halls, agriculture and animal husbandry, greenhouses, supermarkets.",
            "ar": "المصانع، المساحات شبه المفتوحة، قاعات المعارض، المزارع ومزارع الدواجن والماشية، البيوت المحمية، السوبرماركت.",
        },
        "note": DIS,
        "models": [
            ["AZL18-ZX10E", "AZL18-ZS10E", "AZL18-ZC10E"],
            ["AZL18-ZX10G", "AZL18-ZS10G", "AZL18-ZC10G"],
            ["AZL18-ZX32E", "AZL18-ZS32E", "AZL18-ZC32E"],
            ["AZL18-ZX10E", "AZL18-ZS10E", "AZL18-ZC10E", {"en": "Deep water tank", "ar": "خزان مياه عميق"}],
        ],
        "specs": [
            ("voltage", ["110/220 V, 50/60 Hz, 1-phase", "110/220 V, 50/60 Hz, 1-phase", "380–415 V, 50/60 Hz, 3-phase", "110/220 V, 50/60 Hz, 1-phase"]),
            ("power", ["1.1 kW", "1.1 kW", "1.1 / 0.37 kW", "1.1 kW"]),
            ("current", ["5.6", "4.8", "2.0 / 0.85", "5.6"]),
            ("airflow", ["18,000", "18,000", "18,000 / 11,000", "18,000"]),
            ("fan", ["Axial"] * 4),
            ("speed", ["Multi-speed, silicon control", "Multi-speed, inverter", "3-phase, 2-speed", "Multi-speed, silicon control"]),
            ("pressure", ["190", "190", "190 / 63", "190"]),
            ("vent", ["650×650 (down/up), 720×660 (side)"] * 4),
            ("noise", ["≤76"] * 4),
            ("dim", ["1150×1150×950 (down), 1150×1150×982 (up), 1205×1150×950 (side)"] * 3
             + ["1150×1150×1076 (down), 1150×1150×1103 (up), 1205×1150×1076 (side)"]),
            ("pad", ["620×825×100"] * 4),
            ("weight", ["76 (down), 86 (up), 79 (side)"] * 3 + ["86 (down), 91 (up), 90 (side)"]),
            ("opweight", ["106 (down), 110 (up), 119 (side)"] * 3 + ["186 (down), 191 (up), 190 (side)"]),
            ("controller", ["LCD control", "LCD control", "Button + knob switch", "LCD control"]),
            ("filter", [OPT] * 4),
            ("precool", [OPT] * 4),
            ("group", [OPT] * 4),
            ("exhaust", [OPT, OPT, "—", OPT]),
            ("damper", [OPT] * 4),
            ("thermo", [OPT] * 4),
            ("qty40", ["40"] * 4),
            ("qtyskd", ["70 (down), 60 (up), 60 (side)"] * 3 + ["—"]),
        ],
    },
    {
        "slug": "wind-marshal",
        "category": "industrial",
        "name": "Wind Marshal",
        "image": "wind-marshal",
        "gallery": ["wind-marshal-row", "wind-marshal-app"],
        "headline": {"en": "10,000–18,000 m³/h industrial air cooler", "ar": "مكيف صحراوي صناعي بتدفق 10,000–18,000 م³/ساعة"},
        "summary": {
            "en": "A lighter, value-focused industrial cooler with 18,000 m³/h and 10,000 m³/h versions. Four-side air supply, "
            "160 Pa static pressure, and silicon-control, inverter or 3-phase motor options. Strong container loading: 44 units per 40HQ assembled.",
            "ar": "مكيف صناعي اقتصادي وأخف وزناً بنسختين 18,000 و10,000 م³/ساعة. سحب هواء من أربع جهات وضغط 160 باسكال، "
            "مع خيارات تحكم سيليكون أو إنفرتر أو محرك ثلاثي الطور. تحميل ممتاز: 44 وحدة مجمّعة في حاوية 40HQ.",
        },
        "area": "100–120 m²",
        "apps": {
            "en": "Small and medium factories, offices, semi-open restaurants, outdoor exhibition venues.",
            "ar": "المصانع الصغيرة والمتوسطة، المكاتب، المطاعم شبه المفتوحة، أماكن المعارض الخارجية.",
        },
        "note": DIS,
        "models": [
            ["AZL18-ZX10J", "AZL18-ZS10J", "AZL18-ZC10J"],
            ["AZL18-ZX10JG", "AZL18-ZS10JG", "AZL18-ZC10JG"],
            ["AZL18-ZX31J", "AZL18-ZS31J", "AZL18-ZC31J"],
            ["AZL10-ZX10J", "AZL10-ZS10J"],
        ],
        "specs": [
            ("voltage", ["110/220 V, 50/60 Hz, 1-phase", "110/220 V, 50/60 Hz, 1-phase", "380–415 V, 50/60 Hz, 3-phase", "110/220 V, 50/60 Hz, 1-phase"]),
            ("power", ["0.75 kW", "0.75 kW", "0.75 kW", "0.52 kW"]),
            ("current", ["5.6", "4.0", "2.3", "2.8"]),
            ("airflow", ["18,000", "18,000", "18,000", "10,000"]),
            ("fan", ["Axial"] * 4),
            ("speed", ["Multi-speed, silicon control", "Multi-speed, inverter", "3-phase, 1-speed", "Multi-speed, silicon control"]),
            ("pressure", ["160", "160", "160", "80"]),
            ("vent", ["555×555 (down/up), 614×614 (side)"] * 3 + ["555×555"]),
            ("noise", ["≤65"] * 4),
            ("dim", ["1030×1030×883 (down), 1030×1030×968 (up), 1030×1345×883 (side)"] * 3
             + ["1030×1030×643 (down), 1030×1030×728 (up)"]),
            ("pad", ["638×738×100"] * 3 + ["395×498×100"]),
            ("weight", ["56 (down), 58 (up/side)"] * 3 + ["50 (down), 51 (up)"]),
            ("opweight", ["74 (down), 76 (up/side)"] * 3 + ["68 (down), 69 (up)"]),
            ("controller", ["LED control"] * 4),
            ("filter", [OPT] * 4),
            ("precool", [OPT] * 4),
            ("group", [OPT] * 4),
            ("thermo", [OPT] * 4),
            ("qty40", ["44", "44", "44", "66"]),
            ("qtyskd", ["87 (down), 75 (up), 85 (side)"] * 2 + ["85 (down), 75 (up), 85 (side)", "95 (down), 88 (up)"]),
        ],
    },
    {
        "slug": "dc-brushless-cooler",
        "category": "industrial",
        "name": "DC Brushless Motor Series",
        "image": "dc-brushless",
        "gallery": ["dc-brushless-row", "dc-brushless-app"],
        "headline": {"en": "Energy-saving 18,000 m³/h cooler with DC brushless motor", "ar": "مكيف صحراوي 18,000 م³/ساعة بمحرك DC بدون فرش موفر للطاقة"},
        "summary": {
            "en": "Aolan's newest industrial range with a DC brushless (EC) motor. The axial version moves 18,000 m³/h on just 0.65 kW, "
            "making it a strong choice where electricity is expensive or generator capacity is limited. A centrifugal version adds 183 Pa for longer duct runs.",
            "ar": "أحدث فئة صناعية من أولان بمحرك DC بدون فرش (EC). النسخة المحورية تعطي 18,000 م³/ساعة باستهلاك 0.65 كيلوواط فقط، "
            "ما يجعلها خياراً مثالياً حيث الكهرباء مرتفعة التكلفة أو قدرة المولد محدودة. وتوفر نسخة الطرد المركزي ضغط 183 باسكال لمجاري الهواء الطويلة.",
        },
        "area": "100–120 m²",
        "apps": {
            "en": "Industrial plants, factories, semi-open places, exhibition halls, textile, agriculture and animal husbandry, warehouses, greenhouses, supermarkets.",
            "ar": "المصانع، المساحات شبه المفتوحة، قاعات المعارض، مصانع النسيج، المزارع ومزارع الماشية، المستودعات، البيوت المحمية، السوبرماركت.",
        },
        "note": DIS,
        "models": [
            ["AZL18-ZX10EZH", "AZL18-ZS10EZH", "AZL18-ZC10EZH"],
            ["AZL18-LX10CZ", "AZL18-LS10CZ", "AZL18-LC10CZ"],
        ],
        "specs": [
            ("voltage", ["220–240 V, 50–60 Hz"] * 2),
            ("power", ["0.65 kW", "1.5 kW"]),
            ("motor", ["DC (220 V, 3-phase)"] * 2),
            ("current", ["2.65", "7.5"]),
            ("airflow", ["18,000", "18,000"]),
            ("fan", ["Axial", "Centrifugal"]),
            ("speed", ["Multi-speed, inverter"] * 2),
            ("pressure", ["190", "183"]),
            ("vent", ["650×650 (down/up), 720×660 (side)", "650×650 (down/up), 600×600 (side)"]),
            ("noise", ["≤70", "≤65"]),
            ("dim", ["1150×1150×950 (down), 1150×1150×982 (up), 1210×1150×950 (side)"] * 2),
            ("pad", ["620×825×100", "620×825×75 / 620×825×100"]),
            ("weight", ["72 (down), 76 (up), 75 (side)", "79"]),
            ("opweight", ["102 (down), 106 (up), 105 (side)", "109"]),
            ("controller", ["LCD control"] * 2),
            ("filter", [OPT] * 2),
            ("precool", [OPT] * 2),
            ("group", [OPT] * 2),
            ("exhaust", [OPT] * 2),
            ("damper", [OPT] * 2),
            ("thermo", [OPT] * 2),
            ("qty40", ["40", "40"]),
            ("qtyskd", ["70 (down), 60 (up), 60 (side)", "45"]),
        ],
    },
    {
        "slug": "wind-auramo",
        "category": "industrial",
        "name": "Wind Auramo",
        "image": "wind-auramo",
        "gallery": ["wind-auramo-row", "wind-auramo-app"],
        "headline": {"en": "16,000 m³/h industrial air cooler with 100 L tank", "ar": "مكيف صحراوي صناعي 16,000 م³/ساعة بخزان 100 لتر"},
        "summary": {
            "en": "A 16,000 m³/h cooler with a 100-litre water tank and plastic cabinet, offered with a centrifugal inverter fan (170 Pa) "
            "or an axial silicon-control fan. Voltage can be customised for the destination market.",
            "ar": "مكيف بتدفق 16,000 م³/ساعة مع خزان مياه 100 لتر وهيكل بلاستيكي، متوفر بمروحة طرد مركزي بإنفرتر (170 باسكال) "
            "أو مروحة محورية بتحكم سيليكون. يمكن تخصيص الجهد الكهربائي حسب بلد الاستيراد.",
        },
        "area": "90–100 m²",
        "apps": {
            "en": "Small and medium factories, offices, semi-open restaurants, outdoor exhibition venues.",
            "ar": "المصانع الصغيرة والمتوسطة، المكاتب، المطاعم شبه المفتوحة، أماكن المعارض الخارجية.",
        },
        "note": DIS,
        "models": [
            ["AZL16-LX10JZ", "AZL16-LS10JZ", "AZL16-LC10JZ"],
            ["AZL16-ZX10J", "AZL16-ZS10J", "AZL16-ZC10J"],
        ],
        "specs": [
            ("voltage", ["220 V, 1-phase, 50 Hz (customisable)"] * 2),
            ("power", ["1 kW", "0.75 kW"]),
            ("current", ["6.5", "4.0"]),
            ("airflow", ["16,000", "16,000"]),
            ("fan", ["Centrifugal", "Axial"]),
            ("speed", ["Multi-speed, inverter", "Multi-speed, silicon control"]),
            ("pressure", ["170", "160"]),
            ("vent", ["555×555"] * 2),
            ("noise", ["≤63", "≤65"]),
            ("dim", ["1078×1078×1020 (down), 1078×1078×1055 (up), 1104×1078×1020 (side)"] * 2),
            ("pad", ["(608+30)×732×100 / (608+30)×732×80", "(608+30)×732×100"]),
            ("weight", ["64 (down), 66 (up), 76 (side)", "56 (down), 58 (up), 68 (side)"]),
            ("water", ["100", "100"]),
            ("cabinet", ["Plastic", "Plastic"]),
            ("controller", [OPT] * 2),
            ("precool", [OPT] * 2),
            ("group", [OPT] * 2),
            ("thermo", [OPT] * 2),
            ("qty40", ["40", "40"]),
            ("qtyskd", ["87 (down), 75 (up), 85 (side)"] * 2),
        ],
    },
    {
        "slug": "wind-domination",
        "category": "industrial",
        "name": "Wind Domination",
        "image": "wind-domination",
        "gallery": ["wind-domination-row", "wind-domination-app"],
        "headline": {"en": "25,000–30,000 m³/h heavy-duty industrial air cooler", "ar": "مكيف صحراوي صناعي للخدمة الشاقة 25,000–30,000 م³/ساعة"},
        "summary": {
            "en": "High-capacity 3-phase coolers at 25,000 and 30,000 m³/h with up to 366 Pa static pressure, built for long duct runs "
            "in large workshops, logistics warehouses and public buildings. Two-speed or inverter control.",
            "ar": "مكيفات ثلاثية الطور عالية القدرة بتدفق 25,000 و30,000 م³/ساعة وضغط استاتيكي يصل إلى 366 باسكال، "
            "مصممة لمجاري الهواء الطويلة في الورش الكبيرة ومستودعات الخدمات اللوجستية والمباني العامة. تحكم بسرعتين أو إنفرتر.",
        },
        "area": "250–300 m²",
        "apps": {
            "en": "Public buildings, commercial buildings, industrial workshops, logistics warehousing.",
            "ar": "المباني العامة، المباني التجارية، الورش الصناعية، المستودعات اللوجستية.",
        },
        "note": DIS,
        "models": [
            ["AZL25-ZX32C", "AZL25-ZS32C", "AZL25-ZC32C"],
            ["AZL25-ZX30C", "AZL25-ZS30C", "AZL25-ZC30C"],
            ["AZL30-ZX32C", "AZL30-ZS32C", "AZL30-ZC32C"],
            ["AZL30-ZX30C", "AZL30-ZS30C", "AZL30-ZC30C"],
        ],
        "specs": [
            ("voltage", ["380–415 V, 50/60 Hz, 3-phase"] * 4),
            ("power", ["2.2 / 0.75 kW", "2.2 kW", "3.0 / 1.0 kW", "3.0 kW"]),
            ("current", ["5.4 / 2.7", "5.4", "7.1 / 3.5", "7.1"]),
            ("airflow", ["25,000 / 16,000", "25,000", "30,000 / 20,000", "30,000"]),
            ("fan", ["Axial"] * 4),
            ("speed", ["3-phase, 2-speed", "Multi-speed, inverter", "3-phase, 2-speed", "Multi-speed, inverter"]),
            ("pressure", ["306 / 128", "306", "366 / 160", "366"]),
            ("vent", ["765×765"] * 4),
            ("noise", ["≤78", "≤78", "≤80", "≤80"]),
            ("dim", ["1350×1350×1310 (down/side), 1350×1350×1426 (up)"] * 3 + ["1420×1350×1310 (down/side), 1350×1350×1426 (up)"]),
            ("pad", ["970×886×100"] * 4),
            ("weight", ["120 (down), 147 (up), 128 (side)"] * 2 + ["125 (down), 152 (up), 133 (side)"] * 2),
            ("opweight", ["175 (down), 202 (up), 183 (side)"] * 2 + ["180 (down), 207 (up), 188 (side)"] * 2),
            ("controller", ["LED control", "LCD control", "LED control", "LCD control"]),
            ("filter", [OPT] * 4),
            ("precool", [OPT] * 4),
            ("group", [OPT] * 4),
            ("thermo", [OPT] * 4),
            ("qty40", ["9"] * 4),
            ("qtyskd", ["45 (down), 39 (up), 42 (side)"] * 4),
        ],
    },
    {
        "slug": "wind-superior",
        "category": "industrial",
        "name": "Wind Superior",
        "image": "wind-superior",
        "gallery": ["wind-superior-row"],
        "headline": {"en": "25,000–50,000 m³/h centrifugal industrial cooler", "ar": "مكيف صحراوي صناعي بمروحة طرد مركزي 25,000–50,000 م³/ساعة"},
        "summary": {
            "en": "Cabinet-type centrifugal coolers from 25,000 to 50,000 m³/h with 240–500 Pa static pressure for ducted cooling of large "
            "plants. Five sizes, all 3-phase, with an optional aluminium-alloy shell for harsh or coastal sites.",
            "ar": "مكيفات خزانية بمروحة طرد مركزي من 25,000 إلى 50,000 م³/ساعة وضغط استاتيكي 240–500 باسكال لتبريد المصانع الكبيرة عبر مجاري الهواء. "
            "خمسة مقاسات، جميعها ثلاثية الطور، مع هيكل اختياري من سبائك الألمنيوم للمواقع الساحلية أو القاسية.",
        },
        "apps": {
            "en": "Large factories, logistics centres, public buildings and ducted cooling projects.",
            "ar": "المصانع الكبيرة، المراكز اللوجستية، المباني العامة، ومشاريع التبريد بمجاري الهواء.",
        },
        "note": DIS,
        "models": [
            ["AZL25-LX31F", "AZL25-LS31F", "AZL25-LC31F"],
            ["AZL30-LX31F", "AZL30-LS31F", "AZL30-LC31F"],
            ["AZL35-LX31F", "AZL35-LS31F", "AZL35-LC31F"],
            ["AZL40-LX31F", "AZL40-LS31F", "AZL40-LC31F"],
            ["AZL50-LX31F", "AZL50-LS31F", "AZL50-LC31F"],
        ],
        "specs": [
            ("voltage", ["380–415 V, 50/60 Hz, 3-phase"] * 5),
            ("power", ["3 kW", "4 kW", "5.5 kW", "7.5 kW", "15 kW"]),
            ("current", ["6.8", "8.8", "11.6", "15.9", "30.5"]),
            ("airflow", ["25,000", "30,000", "35,000", "40,000", "50,000"]),
            ("fan", ["Centrifugal"] * 5),
            ("speed", ["3-phase, 1-speed"] * 5),
            ("pressure", ["240", "280", "300", "320", "500"]),
            ("vent", ["707×645 (down), 772×707 (up/side)"] * 2 + ["803×718 (down), 843×747 (up/side)"] * 3),
            ("noise", ["≤74", "≤76", "≤81", "≤83", "≤85"]),
            ("dim", [
                "1385×1515×1400 (down), 1385×1515×1460 (up), 1450×1515×1400 (side)",
                "1385×1515×1400 (down), 1385×1515×1460 (up), 1450×1515×1400 (side)",
                "1600×1750×1550 (down), 1600×1750×1580 (up), 1635×1750×1550 (side)",
                "1600×1750×1550 (down), 1600×1750×1585 (up), 1635×1750×1550 (side)",
                "1600×1830×1750 (down), 1600×1830×1740 (up), 1635×1830×1705 (side)",
            ]),
            ("pad", ["1100×520×100 + 1100×465×120"] * 2 + ["1237×634×100 + 1237×573×120"] * 2 + ["1363×670×100 + 1363×568×120"]),
            ("weight", ["315", "320", "490", "505", "574"]),
            ("opweight", ["358", "363", "540", "555", "624"]),
            ("controller", ["Button + knob switch"] * 5),
            ("alushell", [OPT] * 5),
            ("qty40", ["8", "8", "7", "7", "7"]),
        ],
    },
    {
        "slug": "wind-emperor",
        "category": "industrial",
        "name": "Wind Emperor",
        "image": "wind-emperor",
        "gallery": [],
        "headline": {"en": "60,000–80,000 m³/h central evaporative cooling unit", "ar": "وحدة تبريد تبخيري مركزية 60,000–80,000 م³/ساعة"},
        "summary": {
            "en": "Aolan's largest units: 60,000 and 80,000 m³/h centrifugal coolers with up to 700 Pa static pressure and a control cabinet, "
            "for central ducted cooling of very large plants, stadium concourses and logistics hubs.",
            "ar": "أكبر وحدات أولان: مكيفات طرد مركزي بتدفق 60,000 و80,000 م³/ساعة وضغط استاتيكي يصل إلى 700 باسكال مع لوحة تحكم، "
            "للتبريد المركزي عبر مجاري الهواء في المصانع الضخمة والملاعب والمراكز اللوجستية.",
        },
        "apps": {
            "en": "Very large factories, logistics hubs, stadiums and central ducted cooling projects.",
            "ar": "المصانع الضخمة، المراكز اللوجستية، الملاعب، ومشاريع التبريد المركزي بمجاري الهواء.",
        },
        "note": DIS,
        "models": [["AZL60-LX32D", "AZL60-LS32D", "AZL60-LC32D"], ["AZL80-LC32B"]],
        "specs": [
            ("voltage", ["380–415 V, 50/60 Hz, 3-phase"] * 2),
            ("power", ["18.5 / 6 kW", "30 / 15 kW"]),
            ("current", ["37 / 15.7", "61.7 / 33.6"]),
            ("airflow", ["60,000 / 36,000", "80,000 / 58,000"]),
            ("fan", ["Centrifugal"] * 2),
            ("speed", ["3-phase, 2-speed"] * 2),
            ("pressure", ["520 / 242", "700 / 480"]),
            ("vent", ["810×956", "1355×1042"]),
            ("noise", ["≤85", "≤91"]),
            ("dim", ["2088×2070×1863 (down), 2088×2070×2011 (up), 2172×2070×1863 (side)", "3103×2202×2400"]),
            ("pad", ["1555×860×120", "—"]),
            ("weight", ["900", "1600"]),
            ("opweight", ["1000", "1762"]),
            ("controller", ["Button + knob switch"] * 2),
            ("alushell", [OPT] * 2),
            ("qty40", ["5", "3"]),
        ],
    },
    # ------------------------------------------------------------------ outdoor / portable
    {
        "slug": "azl-300",
        "category": "outdoor",
        "name": "AZL-300",
        "image": "azl-300",
        "gallery": ["azl-300-app"],
        "headline": {"en": "30,000 m³/h big-fan portable air cooler", "ar": "مكيف صحراوي متنقل بمروحة كبيرة 30,000 م³/ساعة"},
        "summary": {
            "en": "A heavy-duty mobile cooler with an 86 cm blade and a 200-litre tank, moving 30,000 m³/h on 750 W. Cools 200–260 m² "
            "of outdoor or half-open space with no installation, which makes it a favourite for events, workshops and outdoor dining.",
            "ar": "مكيف متنقل للخدمة الشاقة بمروحة قطرها 86 سم وخزان 200 لتر، يعطي 30,000 م³/ساعة باستهلاك 750 واط. "
            "يبرد 200–260 م² من المساحات الخارجية أو شبه المفتوحة دون تركيب، وهو الخيار المفضل للفعاليات والورش والجلسات الخارجية.",
        },
        "area": "200–260 m²",
        "apps": {
            "en": "Outdoor and half-open places: workshops, warehouses, exhibition halls, sports events, outdoor dining.",
            "ar": "المساحات الخارجية وشبه المفتوحة: الورش، المستودعات، قاعات المعارض، الفعاليات الرياضية، الجلسات والمطاعم الخارجية.",
        },
        "models": [["AZL-300"]],
        "specs": [
            ("airflow", ["30,000"]),
            ("power", ["750 W"]),
            ("voltage", ["110/220 V, 50/60 Hz"]),
            ("speed", ["1-phase, 3-speed"]),
            ("controller", ["LCD + remote"]),
            ("packing", ["1600×780×1800"]),
            ("weight", ["135"]),
            ("blade", ["86 cm"]),
            ("outlet", ["90 cm"]),
            ("water", ["200"]),
            ("uv", ["Yes"]),
            ("area", ["200–260 m²"]),
            ("qty40", ["30"]),
        ],
    },
    {
        "slug": "azl-180",
        "category": "outdoor",
        "name": "AZL-180",
        "image": "azl-180",
        "gallery": ["azl-180-app"],
        "headline": {"en": "18,000 m³/h portable evaporative air cooler", "ar": "مكيف صحراوي متنقل 18,000 م³/ساعة"},
        "summary": {
            "en": "A large mobile cooler with a 100-litre tank, UV light, LCD panel and remote. 18,000 m³/h covers 100–150 m² "
            "and the 4-inch castors make it easy to move between halls, courts and job sites.",
            "ar": "مكيف متنقل كبير بخزان 100 لتر ومصباح UV وشاشة LCD وريموت كنترول. تدفق 18,000 م³/ساعة يغطي 100–150 م² "
            "والعجلات مقاس 4 إنش تسهل نقله بين القاعات والملاعب ومواقع العمل.",
        },
        "area": "100–150 m²",
        "apps": {
            "en": "Shopping malls, hotels, golf ranges, construction sites, gymnasiums.",
            "ar": "المراكز التجارية، الفنادق، ملاعب الجولف، مواقع البناء، الصالات الرياضية.",
        },
        "models": [["AZL-180"]],
        "specs": [
            ("airflow", ["18,000"]),
            ("power", ["550 W"]),
            ("voltage", ["220/240 V, 50/60 Hz"]),
            ("speed", ["1-phase, 3-speed"]),
            ("controller", ["LCD + remote"]),
            ("packing", ["1130×680×1510"]),
            ("weight", ["55"]),
            ("water", ["100"]),
            ("uv", ["Yes"]),
            ("blade", ["750 mm"]),
            ("outlet", ["76×76 cm"]),
            ("wheel", ['4"']),
            ("area", ["100–150 m²"]),
            ("qty40", ["57"]),
        ],
    },
    {
        "slug": "azl08-azl12-zy13b",
        "category": "outdoor",
        "name": "AZL08 / AZL10 / AZL12-ZY13B",
        "image": "azl08-zy13b",
        "gallery": ["azl08-zy13b-app"],
        "headline": {"en": "8,000–12,000 m³/h portable air cooler, 90 L tank", "ar": "مكيف صحراوي متنقل 8,000–12,000 م³/ساعة بخزان 90 لتر"},
        "summary": {
            "en": "One body in three airflow ratings (8,000, 10,000 and 12,000 m³/h) with a 90-litre tank, pre-dust filter, LED panel and remote. "
            "A practical mid-size range for shops, kitchens, mosques and waiting halls.",
            "ar": "هيكل واحد بثلاث قدرات تدفق (8,000 و10,000 و12,000 م³/ساعة) مع خزان 90 لتر وفلتر غبار وشاشة LED وريموت. "
            "فئة متوسطة عملية للمحلات والمطابخ والمساجد وصالات الانتظار.",
        },
        "apps": {
            "en": "Churches and mosques, internet cafés, restaurant kitchens, auditoriums, railway stations.",
            "ar": "المساجد ودور العبادة، مقاهي الإنترنت، مطابخ المطاعم، القاعات، محطات القطارات.",
        },
        "models": [["AZL08-ZY13B"], ["AZL10-ZY13B"], ["AZL12-ZY13B"]],
        "specs": [
            ("airflow", ["8,000", "10,000", "12,000"]),
            ("pressure", ["90"] * 3),
            ("power", ["0.2 kW", "0.25 kW", "0.3 kW"]),
            ("voltage", ["110/220 V, 50/60 Hz"] * 3),
            ("current", ["2.2", "2.3", "2.5"]),
            ("fan", ["Axial"] * 3),
            ("vent", ["654×673"] * 3),
            ("speed", ["1-phase, 3-speed"] * 3),
            ("noise", ["≤60"] * 3),
            ("dim", ["842×532×1448"] * 3),
            ("pad", ["641×703×100 + 210×580×60"] * 3),
            ("weight", ["33"] * 3),
            ("water", ["90"] * 3),
            ("controller", ["LED + remote"] * 3),
            ("filter", ["Yes"] * 3),
            ("qty40", ["112"] * 3),
        ],
    },
    {
        "slug": "azl06-zy13f",
        "category": "outdoor",
        "name": "AZL06-ZY13F",
        "image": "azl06-zy13f",
        "gallery": ["azl06-zy13f-app"],
        "headline": {"en": "6,000 m³/h portable air cooler, 70/120 L tank", "ar": "مكيف صحراوي متنقل 6,000 م³/ساعة بخزان 70/120 لتر"},
        "summary": {
            "en": "A quiet (≤56 dBA) 6,000 m³/h mobile cooler using only 150 W, with a 70 or 120-litre tank, pre-dust filter and remote. "
            "Popular for schools, waiting rooms and hotel venues.",
            "ar": "مكيف متنقل هادئ (≤56 ديسيبل) بتدفق 6,000 م³/ساعة واستهلاك 150 واط فقط، بخزان 70 أو 120 لتر وفلتر غبار وريموت. "
            "مناسب للمدارس وصالات الانتظار وقاعات الفنادق.",
        },
        "apps": {
            "en": "Schools, station waiting rooms, exhibition centres, hotel venues.",
            "ar": "المدارس، صالات انتظار المحطات، مراكز المعارض، قاعات الفنادق.",
        },
        "models": [["AZL06-ZY13F"]],
        "specs": [
            ("airflow", ["6,000"]), ("pressure", ["60"]), ("power", ["0.15 kW"]), ("voltage", ["110/220 V, 50/60 Hz"]),
            ("current", ["1.25"]), ("fan", ["Axial"]), ("vent", ["540×540"]), ("speed", ["1-phase, 3-speed"]),
            ("noise", ["≤56"]), ("dim", ["750×550×1320"]), ("pad", ["660×665×100"]), ("weight", ["29"]),
            ("water", ["70 / 120"]), ("controller", ["LED + remote"]), ("filter", ["Yes"]), ("qty40", ["143"]),
        ],
    },
    {
        "slug": "azl06-zy13g",
        "category": "outdoor",
        "name": "AZL06-ZY13G",
        "image": "azl06-zy13g",
        "gallery": ["azl06-zy13g-app"],
        "headline": {"en": "6,000 m³/h portable air cooler with three-side pads", "ar": "مكيف صحراوي متنقل 6,000 م³/ساعة بخلايا تبريد من ثلاث جهات"},
        "summary": {
            "en": "The 6,000 m³/h portable cooler with extra side cooling pads for more evaporation in very hot, dry air. "
            "70/120-litre tank, pre-dust filter, LED panel and remote.",
            "ar": "مكيف متنقل بتدفق 6,000 م³/ساعة مع خلايا تبريد جانبية إضافية لتبخير أكثر في الأجواء شديدة الحرارة والجفاف. "
            "خزان 70/120 لتر وفلتر غبار وشاشة LED وريموت.",
        },
        "apps": {
            "en": "Shopping malls, hotels, golf ranges, construction sites, gymnasiums.",
            "ar": "المراكز التجارية، الفنادق، ملاعب الجولف، مواقع البناء، الصالات الرياضية.",
        },
        "models": [["AZL06-ZY13G"]],
        "specs": [
            ("airflow", ["6,000"]), ("pressure", ["60"]), ("power", ["0.15 kW"]), ("voltage", ["110/220 V, 50/60 Hz"]),
            ("current", ["1.25"]), ("fan", ["Axial"]), ("vent", ["540×540"]), ("speed", ["1-phase, 3-speed"]),
            ("noise", ["≤68"]), ("dim", ["795×550×1320"]), ("pad", ["660×665×100 + 495×132×50"]), ("weight", ["31"]),
            ("water", ["70 / 120"]), ("controller", ["LED + remote"]), ("filter", ["Yes"]), ("qty40", ["132 / 112"]),
        ],
    },
    {
        "slug": "azl06-zc13-window-cooler",
        "category": "outdoor",
        "name": "AZL06-ZC13A / ZC13B",
        "image": "azl06-zc13a",
        "gallery": ["azl06-zc13b"],
        "headline": {"en": "6,000 m³/h window / wall-mounted air cooler", "ar": "مكيف صحراوي شباك / جداري 6,000 م³/ساعة"},
        "summary": {
            "en": "A window or wall-mounted evaporative cooler that sits outside and blows cooled fresh air into the room, "
            "the classic format for homes, shops and site offices in hot, dry climates. The ZC13B adds side pads.",
            "ar": "مكيف صحراوي شباك أو جداري يركب خارج الغرفة ويدفع هواء نقياً مبرداً إلى الداخل، وهو الشكل التقليدي "
            "للمنازل والمحلات ومكاتب المواقع في الأجواء الحارة الجافة. موديل ZC13B مزود بخلايا تبريد جانبية إضافية.",
        },
        "apps": {
            "en": "Homes, shops, site offices, small workshops and guard rooms.",
            "ar": "المنازل، المحلات، مكاتب المواقع، الورش الصغيرة، غرف الحراسة.",
        },
        "models": [["AZL06-ZC13A"], ["AZL06-ZC13B"]],
        "specs": [
            ("airflow", ["6,000"] * 2), ("pressure", ["60"] * 2), ("power", ["0.15 kW"] * 2), ("voltage", ["110/220 V, 50/60 Hz"] * 2),
            ("current", ["1.25"] * 2), ("fan", ["Axial"] * 2), ("vent", ["489×400"] * 2), ("speed", ["1-phase, 3-speed"] * 2),
            ("noise", ["≤68"] * 2), ("dim", ["795×978×937"] * 2), ("pad", ["660×665×100", "660×665×100 + 495×132×50"]),
            ("weight", ["29", "31"]), ("opweight", ["69", "71"]), ("controller", ["LCD + remote"] * 2),
            ("filter", ["Yes"] * 2), ("precool", [OPT] * 2), ("qty40", ["129", "128"]),
        ],
    },
    {
        "slug": "azl03-zc10az-solar-cooler",
        "category": "outdoor",
        "name": "AZL03-ZC10AZ Solar DC",
        "solar": True,
        "image": "azl03-zc10az",
        "gallery": [],
        "headline": {"en": "3,000 m³/h DC solar window air cooler", "ar": "مكيف صحراوي شباك يعمل بالطاقة الشمسية (DC) 3,000 م³/ساعة"},
        "summary": {
            "en": "An 80 W DC window cooler that runs directly from a solar panel and battery (both optional), with continuously variable speed. "
            "Built for off-grid homes, farms and areas with long power cuts.",
            "ar": "مكيف شباك يعمل بالتيار المستمر بقدرة 80 واط فقط، يمكن تشغيله مباشرة من لوح شمسي وبطارية (اختياري)، مع سرعة متغيرة باستمرار. "
            "مصمم للمنازل والمزارع خارج الشبكة والمناطق التي تعاني من انقطاع الكهرباء الطويل.",
        },
        "apps": {
            "en": "Off-grid homes, farms, rooms in areas with load-shedding, site cabins.",
            "ar": "المنازل خارج الشبكة، المزارع، الغرف في المناطق ذات انقطاع الكهرباء، كبائن المواقع.",
        },
        "models": [["AZL03-ZC10AZ"]],
        "specs": [
            ("airflow", ["3,000"]), ("pressure", ["67"]), ("power", ["0.08 kW"]), ("voltage", ["DC"]),
            ("current", ["5.5"]), ("fan", ["Axial"]), ("vent", ["433×304"]), ("speed", ["Continuously variable"]),
            ("noise", ["≤59.1"]), ("dim", ["600×810×625"]), ("pad", ["240×240×80"]), ("weight", ["38"]),
            ("opweight", ["63"]), ("controller", ["LCD + remote"]), ("filter", ["Yes"]), ("precool", [OPT]),
            ("solar", [OPT]), ("qty40", ["170"]),
        ],
    },
    {
        "slug": "azl06-zc10-solar-window-cooler",
        "category": "outdoor",
        "name": "AZL06-ZC10BD / ZC10DA Solar",
        "solar": True,
        "image": "azl06-zc10bd",
        "gallery": [],
        "headline": {"en": "6,000 m³/h solar DC / AC window air cooler", "ar": "مكيف صحراوي شباك 6,000 م³/ساعة بالطاقة الشمسية (DC / AC)"},
        "summary": {
            "en": "The 6,000 m³/h window cooler in a solar version: ZC10BD runs on DC only, ZC10DA runs on both DC and AC mains, "
            "so it keeps cooling on solar or battery when grid power drops.",
            "ar": "مكيف الشباك 6,000 م³/ساعة بنسخة الطاقة الشمسية: موديل ZC10BD يعمل بالتيار المستمر فقط، وموديل ZC10DA يعمل بالتيار المستمر والمتردد معاً، "
            "فيستمر في التبريد عبر الطاقة الشمسية أو البطارية عند انقطاع الكهرباء.",
        },
        "apps": {
            "en": "Homes, shops and farms with unreliable grid power.",
            "ar": "المنازل والمحلات والمزارع ذات الكهرباء غير المستقرة.",
        },
        "models": [["AZL06-ZC10BD"], ["AZL06-ZC10DA"]],
        "specs": [
            ("airflow", ["6,000"] * 2), ("pressure", ["60"] * 2), ("power", ["0.15 kW"] * 2), ("voltage", ["DC only", "DC and AC"]),
            ("current", ["7"] * 2), ("fan", ["Axial"] * 2), ("vent", ["489×400"] * 2), ("speed", ["Continuously variable"] * 2),
            ("noise", ["≤68"] * 2), ("dim", ["795×978×937"] * 2), ("pad", ["660×665×100 + 495×132×50"] * 2),
            ("weight", ["29"] * 2), ("opweight", ["69"] * 2), ("controller", ["LCD + remote"] * 2), ("filter", ["Yes"] * 2),
            ("precool", [OPT] * 2), ("solar", [OPT] * 2), ("qty40", ["128"] * 2),
        ],
    },
    {
        "slug": "azl06-zy10-solar-portable-cooler",
        "category": "outdoor",
        "name": "AZL06-ZY10GD / ZY10GDA Solar",
        "solar": True,
        "image": "azl06-zy10gd",
        "gallery": [],
        "headline": {"en": "6,000 m³/h solar DC / AC portable air cooler", "ar": "مكيف صحراوي متنقل 6,000 م³/ساعة بالطاقة الشمسية (DC / AC)"},
        "summary": {
            "en": "A portable 6,000 m³/h cooler that runs on solar DC, with a DC + AC version that switches to mains power. "
            "Continuously variable speed, LCD panel and remote.",
            "ar": "مكيف متنقل 6,000 م³/ساعة يعمل بالتيار المستمر من الطاقة الشمسية، مع نسخة DC + AC تعمل أيضاً على كهرباء الشبكة. "
            "سرعة متغيرة باستمرار وشاشة LCD وريموت.",
        },
        "apps": {
            "en": "Farms, outdoor seating, shops and homes with load-shedding.",
            "ar": "المزارع، الجلسات الخارجية، المحلات والمنازل في مناطق انقطاع الكهرباء.",
        },
        "models": [["AZL06-ZY10GD"], ["AZL06-ZY10GDA"]],
        "specs": [
            ("airflow", ["6,000"] * 2), ("pressure", ["60"] * 2), ("power", ["0.15 kW"] * 2), ("voltage", ["DC only", "DC and AC"]),
            ("current", ["7"] * 2), ("fan", ["Axial"] * 2), ("vent", ["540×540"] * 2), ("speed", ["Continuously variable"] * 2),
            ("noise", ["≤68"] * 2), ("dim", ["795×500×1320"] * 2), ("pad", ["660×665×100 + 495×132×50"] * 2),
            ("weight", ["29"] * 2), ("opweight", ["99"] * 2), ("controller", ["LCD + remote"] * 2), ("filter", ["Yes"] * 2),
            ("precool", [OPT] * 2), ("solar", [OPT] * 2), ("qty40", ["132"] * 2),
        ],
    },
    # ------------------------------------------------------------------ home & office
    {
        "slug": "azl045-zy13a",
        "category": "home",
        "name": "AZL045-ZY13A",
        "image": "azl045-zy13a",
        "gallery": ["azl045-zy13a-app"],
        "headline": {"en": "4,500 m³/h home & shop air cooler, 35 L tank", "ar": "مبرد هواء للمنازل والمحلات 4,500 م³/ساعة بخزان 35 لتر"},
        "summary": {
            "en": "A powerful room cooler for larger lounges, shops and restaurants: 4,500 m³/h, 35-litre tank, 40 W, LED panel and remote.",
            "ar": "مبرد غرف قوي للصالات الكبيرة والمحلات والمطاعم: 4,500 م³/ساعة، خزان 35 لتر، 40 واط، شاشة LED وريموت.",
        },
        "apps": {"en": "Homes, offices, restaurants, hotels.", "ar": "المنازل، المكاتب، المطاعم، الفنادق."},
        "models": [["AZL045-ZY13A"]],
        "specs": [
            ("airflow", ["4,500"]), ("pressure", ["50"]), ("power", ["40 W"]), ("voltage", ["110/220 V, 50/60 Hz"]),
            ("current", ["0.7"]), ("fan", ["Axial"]), ("vent", ["420×420"]), ("speed", ["1-phase, 3-speed"]), ("noise", ["≤55"]),
            ("dim", ["550×330×990"]), ("pad", ["450×600×60 + 162×600×50"]), ("weight", ["14"]), ("water", ["35"]),
            ("controller", ["LED + remote"]), ("qty40", ["275"]),
        ],
    },
    {
        "slug": "azl035-ly13f",
        "category": "home",
        "name": "AZL035-LY13F",
        "image": "azl035-ly13f",
        "gallery": ["azl035-ly13f-app"],
        "headline": {"en": "3,500 m³/h tower air cooler, 40 L tank", "ar": "مبرد هواء عمودي 3,500 م³/ساعة بخزان 40 لتر"},
        "summary": {
            "en": "A slim tower cooler with a centrifugal fan (120 Pa), 40-litre tank, pre-dust filter and remote, sized for meeting rooms, cafés and hotel lobbies.",
            "ar": "مبرد عمودي نحيف بمروحة طرد مركزي (120 باسكال) وخزان 40 لتر وفلتر غبار وريموت، مناسب لقاعات الاجتماعات والمقاهي وردهات الفنادق.",
        },
        "apps": {"en": "Exhibition centres, meeting rooms, coffee shops, hotels.", "ar": "مراكز المعارض، قاعات الاجتماعات، المقاهي، الفنادق."},
        "models": [["AZL035-LY13F"]],
        "specs": [
            ("airflow", ["3,500"]), ("pressure", ["120"]), ("power", ["0.1 kW"]), ("voltage", ["110/220 V, 50/60 Hz"]),
            ("current", ["1.1"]), ("fan", ["Centrifugal"]), ("vent", ["500×336"]), ("speed", ["1-phase, 3-speed"]), ("noise", ["≤52.7"]),
            ("dim", ["600×430×1380"]), ("pad", ["433×858×65"]), ("weight", ["28"]), ("water", ["40"]),
            ("controller", ["LED + remote"]), ("filter", ["Yes"]), ("qty40", ["130"]),
        ],
    },
    {
        "slug": "azl035-ly13g",
        "category": "home",
        "name": "AZL035-LY13G",
        "image": "azl035-ly13g",
        "gallery": ["azl035-ly13g-app"],
        "headline": {"en": "3,500 m³/h tall tower air cooler, 40 L tank", "ar": "مبرد هواء عمودي طويل 3,500 م³/ساعة بخزان 40 لتر"},
        "summary": {
            "en": "The 1.68 m tall version of the LY13F tower cooler, delivering air above head height for classrooms, waiting rooms and hotel venues.",
            "ar": "النسخة الطويلة (1.68 م) من المبرد العمودي LY13F، تدفع الهواء فوق مستوى الرأس للفصول الدراسية وصالات الانتظار وقاعات الفنادق.",
        },
        "apps": {"en": "Schools, station waiting rooms, exhibition centres, hotel venues.", "ar": "المدارس، صالات انتظار المحطات، مراكز المعارض، قاعات الفنادق."},
        "models": [["AZL035-LY13G"]],
        "specs": [
            ("airflow", ["3,500"]), ("pressure", ["120"]), ("power", ["0.1 kW"]), ("voltage", ["110/220 V, 50/60 Hz"]),
            ("current", ["1.1"]), ("fan", ["Centrifugal"]), ("vent", ["500×336"]), ("speed", ["1-phase, 3-speed"]), ("noise", ["≤52.7"]),
            ("dim", ["600×430×1680"]), ("pad", ["433×858×65"]), ("weight", ["30"]), ("water", ["40"]),
            ("controller", ["LED + remote"]), ("filter", ["Yes"]), ("qty40", ["101"]),
        ],
    },
    {
        "slug": "azl012-ly13a",
        "category": "home",
        "name": "AZL012-LY13A / LY13AR",
        "image": "azl012-ly13a",
        "gallery": ["azl012-ly13a-app"],
        "headline": {"en": "1,200 m³/h room air cooler, 18 L tank", "ar": "مبرد هواء للغرف 1,200 م³/ساعة بخزان 18 لتر"},
        "summary": {
            "en": "A retail-friendly room cooler with an 18-litre tank, LED panel and remote. The LY13AR adds a heater for year-round use.",
            "ar": "مبرد غرف مناسب لمحلات التجزئة بخزان 18 لتر وشاشة LED وريموت. موديل LY13AR مزود بسخان للاستخدام طوال العام.",
        },
        "apps": {"en": "Living rooms, bedrooms, hotels, offices.", "ar": "غرف الجلوس، غرف النوم، الفنادق، المكاتب."},
        "models": [["AZL012-LY13A"], ["AZL012-LY13AR", {"en": "Heating & cooling", "ar": "تبريد وتدفئة"}]],
        "specs": [
            ("airflow", ["1,200"] * 2), ("pressure", ["30"] * 2), ("power", ["20 W", "20 W (cooling) / 1,000–1,850 W (heating)"]),
            ("voltage", ["110/220 V, 50/60 Hz"] * 2), ("current", ["0.22", "7.3"]), ("fan", ["Centrifugal"] * 2),
            ("vent", ["300×240"] * 2), ("speed", ["1-phase, 3-speed"] * 2), ("noise", ["≤52", "≤51.5 / 43.5"]),
            ("dim", ["385×315×750"] * 2), ("pad", ["290×300×40"] * 2), ("weight", ["8", "9"]), ("water", ["18"] * 2),
            ("controller", ["LED + remote"] * 2), ("qty40", ["523"] * 2),
        ],
    },
    {
        "slug": "azl010-ly13b",
        "category": "home",
        "name": "AZL010-LY13B / LY13BR",
        "image": "azl010-ly13b",
        "gallery": ["azl010-ly13b-app"],
        "headline": {"en": "1,000 m³/h room air cooler with remote", "ar": "مبرد هواء للغرف 1,000 م³/ساعة مع ريموت"},
        "summary": {
            "en": "A compact 1,000 m³/h cooler with a 6-litre tank, LED touch panel and remote. LY13B is cooling-only; LY13BR adds heating.",
            "ar": "مبرد صغير بتدفق 1,000 م³/ساعة وخزان 6 لتر ولوحة لمس LED وريموت. موديل LY13B للتبريد فقط وموديل LY13BR يضيف التدفئة.",
        },
        "apps": {"en": "Living rooms, hotels, bedrooms, offices.", "ar": "غرف الجلوس، الفنادق، غرف النوم، المكاتب."},
        "models": [["AZL010-LY13B", {"en": "Cooling only", "ar": "تبريد فقط"}], ["AZL010-LY13BR", {"en": "Heating & cooling", "ar": "تبريد وتدفئة"}]],
        "specs": [
            ("airflow", ["1,000"] * 2), ("pressure", ["20"] * 2), ("power", ["9 W", "1,709 W (with heater)"]),
            ("voltage", ["110/220 V, 50/60 Hz"] * 2), ("current", ["0.16", "7.49"]), ("fan", ["Centrifugal"] * 2),
            ("vent", ["200×320"] * 2), ("speed", ["1-phase, 3-speed"] * 2), ("noise", ["≤46", "≤42"]),
            ("dim", ["270×285×700"] * 2), ("pad", ["195×268×32"] * 2), ("weight", ["7", "8"]), ("water", ["6"] * 2),
            ("controller", ["LED + remote"] * 2), ("qty40", ["821"] * 2),
        ],
    },
    {
        "slug": "azl010-ly13a",
        "category": "home",
        "name": "AZL010-LY13A",
        "image": "azl010-ly13a",
        "gallery": ["azl010-ly13a-app"],
        "headline": {"en": "1,000 m³/h compact room air cooler", "ar": "مبرد هواء صغير للغرف 1,000 م³/ساعة"},
        "summary": {
            "en": "An entry-level 9 W room cooler with push-button controls and a 6-litre tank. 821 units per 40HQ make it an efficient retail volume item.",
            "ar": "مبرد غرف اقتصادي بقدرة 9 واط وأزرار تحكم وخزان 6 لتر. تحميل 821 وحدة في حاوية 40HQ يجعله منتجاً مثالياً لتجارة التجزئة بالكميات.",
        },
        "apps": {"en": "Homes, offices, bedrooms, hotels.", "ar": "المنازل، المكاتب، غرف النوم، الفنادق."},
        "models": [["AZL010-LY13A"]],
        "specs": [
            ("airflow", ["1,000"]), ("pressure", ["20"]), ("power", ["9 W"]), ("voltage", ["110/220 V, 50/60 Hz"]),
            ("current", ["0.12"]), ("fan", ["Centrifugal"]), ("vent", ["200×320"]), ("speed", ["1-phase, 3-speed"]), ("noise", ["≤46"]),
            ("dim", ["270×285×700"]), ("pad", ["195×268×32"]), ("weight", ["7"]), ("water", ["6"]),
            ("controller", ["Button"]), ("qty40", ["821"]),
        ],
    },
    {
        "slug": "azl001-zc12ar-desktop-cooler",
        "category": "home",
        "name": "AZL001-ZC12AR Desktop",
        "image": "azl001-zc12ar",
        "gallery": ["azl001-zc12ar-app"],
        "headline": {"en": "Desktop personal air cooler with optional heating", "ar": "مبرد هواء شخصي مكتبي مع تدفئة اختيارية"},
        "summary": {
            "en": "A 1.6 kg desktop cooler for a desk or bedside table: 200 m³/h, 27 W in cooling mode, ≤46 dBA, with an optional heating function.",
            "ar": "مبرد مكتبي بوزن 1.6 كجم للمكتب أو بجانب السرير: 200 م³/ساعة، 27 واط في وضع التبريد، ≤46 ديسيبل، مع وظيفة تدفئة اختيارية.",
        },
        "apps": {"en": "Homes, hotels, bedrooms, living rooms, studies, offices.", "ar": "المنازل، الفنادق، غرف النوم، غرف الجلوس، غرف الدراسة، المكاتب."},
        "models": [["AZL001-ZC12AR"]],
        "specs": [
            ("airflow", ["200"]), ("pressure", ["4"]), ("power", ["0.027 kW (cooling), 0.83 kW (heating)"]),
            ("voltage", ["110/220 V, 50/60 Hz"]), ("current", ["0.13 (cooling), 3.8 (heating)"]), ("fan", ["Axial"]),
            ("vent", ["138×138"]), ("speed", ["1-phase, 2-speed"]), ("noise", ["≤46"]), ("dim", ["175×185×175"]),
            ("pad", ["106×30×136"]), ("weight", ["1.6"]), ("water", ["0.4"]), ("controller", ["Button"]), ("heating", [OPT]),
        ],
    },
    # ------------------------------------------------------------------ ventilation
    {
        "slug": "extraction-fan-cooling-pad-system",
        "category": "ventilation",
        "name": "Extraction Fan & Cooling Pad System",
        "image": "extraction-fan",
        "gallery": ["extraction-fan-app", "cooling-pad"],
        "headline": {"en": "Exhaust fans and evaporative cooling pads (AFF series)", "ar": "شفاطات هواء صناعية وخلايا تبريد تبخيرية (فئة AFF)"},
        "summary": {
            "en": "Negative-pressure cooling for greenhouses, poultry houses and workshops: extraction fans pull air through wet cooling pads, "
            "replacing the air in about 30 seconds. Aolan rates the system at roughly one-third of the investment and one-tenth of the "
            "electricity of air conditioning. Fans run from 3,150 to 45,800 m³/h with stainless-steel impellers.",
            "ar": "تبريد بالضغط السالب للبيوت المحمية ومزارع الدواجن والورش: تسحب الشفاطات الهواء عبر خلايا تبريد مبللة "
            "فيتجدد الهواء خلال 30 ثانية تقريباً. وتقدّر أولان تكلفة النظام بنحو ثلث استثمار التكييف وعُشر استهلاكه للكهرباء. "
            "تدفق الشفاطات من 3,150 إلى 45,800 م³/ساعة مع مراوح من الستانلس ستيل.",
        },
        "apps": {
            "en": "Greenhouses, poultry and livestock houses, textile mills, workshops.",
            "ar": "البيوت المحمية، مزارع الدواجن والماشية، مصانع النسيج، الورش.",
        },
        "table": {
            "cols": ["model", "drive", "bladedia", "bladerpm", "motorrpm", "airflow", "pressure", "noise", "inputw", "ratedv", "h", "w", "t"],
            "rows": [
                ["AFF-300", "Direct", "200", "1400", "1400", "3,150", "55", "≤70", "80", "380", "400", "400", "320"],
                ["AFF-400", "Direct", "300", "1400", "1400", "3,850", "55", "≤70", "120", "380", "400", "400", "320"],
                ["AFF-500", "Direct", "400", "1400", "1400", "4,500", "55", "≤70", "180", "380", "500", "500", "320"],
                ["AFF-600", "Direct", "500", "1400", "1400", "5,100", "55", "≤70", "250", "380", "600", "600", "320"],
                ["AFF-700", "Direct", "600", "1400", "1400", "10,600", "75", "≤70", "370", "380", "700", "700", "380"],
                ["AFF-800", "Belt", "710", "455", "1400", "16,500", "60", "≤60", "370", "380", "800", "800", "380"],
                ["AFF-900", "Belt", "750", "455", "1400", "21,500", "65", "≤65", "370", "380", "900", "900", "380"],
                ["AFF-1000", "Belt", "900", "445", "1400", "24,500", "70", "≤70", "550", "380", "1000", "1000", "380"],
                ["AFF-1100", "Belt", "1000", "445", "1400", "31,500", "70", "≤70", "750", "380", "1100", "1100", "380"],
                ["AFF-1220", "Belt", "1100", "435", "1400", "35,500", "73", "≤70", "750", "380", "1220", "1200", "380"],
                ["AFF-1380", "Belt", "1250", "435", "1400", "40,500", "56", "≤70", "1100", "380", "1380", "1380", "380"],
                ["AFF-1530", "Belt", "1400", "435", "1400", "45,800", "60", "≤70", "1500", "380", "1530", "1530", "380"],
            ],
        },
        "bullets": {
            "en": [
                "Cooling pad: saturation in under 1 minute, evaporative efficiency above 82%",
                "Pad wind drag below 70 Pa at face velocity above 3 m/s, grade-1 fungus resistance, no odour",
                "Fan impeller in stainless steel; motor power can be customised",
                "Maintenance-free shutter bearings; optional automatic belt tensioner",
            ],
            "ar": [
                "خلية التبريد: تتشبع بالماء خلال أقل من دقيقة بكفاءة تبخير تزيد عن 82%",
                "مقاومة هواء أقل من 70 باسكال عند سرعة تزيد عن 3 م/ث، مقاومة للفطريات من الدرجة الأولى، بدون روائح",
                "مروحة من الستانلس ستيل وإمكانية تخصيص قدرة المحرك",
                "محامل الشتر لا تحتاج صيانة، مع شداد سير أوتوماتيكي اختياري",
            ],
        },
    },
]

# Supply air temperature (°C) from the catalogue, by ambient dry-bulb (rows) and relative humidity (columns).
SUPPLY_AIR = {
    "rh": [10, 20, 30, 40, 50, 60],
    "rows": [
        (25, [14.5, 16, 17, 18.5, 20, 21]),
        (30, [17.5, 19.5, 21, 22.5, 24, 25]),
        (35, [20, 23, 25, 26.5, 28.5, 30]),
        (40, [23, 26.5, 29, 31, 32.5, 34.5]),
        (45, [26, 29, 32.5, 35, None, None]),
        (50, [29, 32.5, 36.5, None, None, None]),
    ],
}

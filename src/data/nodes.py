"""Test datasets for Christofides algorithm."""
# Datasets are created with Claude 3.5. by asking largest cities in Finland and USA, and then converting their lat/lon coordinates with pyproj.

# Change this to switch dataset: "finland", "usa" or "own", if you add your own dataset below
DATASET = "finland"

# Add your own dataset here as (x, y) coordinates with pre-projected coordinates
nodes_own = [
    # (123456, 654321),
]

nodes_finland = [
    (385700, 6672127),  # 0  Helsinki
    (370484, 6681550),  # 1  Espoo
    (328105, 6822741),  # 2  Tampere
    (391645, 6685318),  # 3  Vantaa
    (427883, 7210442),  # 4  Oulu
    (239915, 6710875),  # 5  Turku
    (435047, 6901544),  # 6  Jyväskylä
    (427483, 6761301),  # 7  Lahti
    (534573, 6973516),  # 8  Kuopio
    (223215, 6827301),  # 9  Pori
    (483708, 6748345),  # 10 Kouvola
    (641679, 6944054),  # 11 Joensuu
    (564238, 6770054),  # 12 Lappeenranta
    (362603, 6764338),  # 13 Hämeenlinna
    (228154, 7008146),  # 14 Vaasa
    (287372, 6969078),  # 15 Seinäjoki
    (443493, 7376218),  # 16 Rovaniemi
    (514285, 6839676),  # 17 Mikkeli
    (496701, 6703757),  # 18 Kotka
    (286704, 6699998),  # 19 Salo
]

# 100 largest US cities in Web Mercator (EPSG:3857), unit: meters
nodes_usa = [
    (-8238756, 4969660),   #  0 New York, NY
    (-13162417, 4035518),  #  1 Los Angeles, CA
    (-9757153, 5138537),   #  2 Chicago, IL
    (-10616540, 3472737),  #  3 Houston, TX
    (-12475575, 3955187),  #  4 Phoenix, AZ
    (-8367886, 4858679),   #  5 Philadelphia, PA
    (-10963857, 3429212),  #  6 San Antonio, TX
    (-13041078, 3858197),  #  7 San Diego, CA
    (-10775727, 3866139),  #  8 Dallas, TX
    (-13568733, 4486605),  #  9 San Jose, CA
    (-10880367, 3538303),  # 10 Austin, TX
    (-9090350, 3546039),   # 11 Jacksonville, FL
    (-10834726, 3862167),  # 12 Fort Worth, TX
    (-9238405, 4860131),   # 13 Columbus, OH
    (-8999068, 4195181),   # 14 Charlotte, NC
    (-9591287, 4832575),   # 15 Indianapolis, IN
    (-13627732, 4546985),  # 16 San Francisco, CA
    (-13617713, 6042216),  # 17 Seattle, WA
    (-11686320, 4828231),  # 18 Denver, CO
    (-9660305, 4324038),   # 19 Nashville, TN
    (-10855877, 4227937),  # 20 Oklahoma City, OK
    (-11854413, 3731848),  # 21 El Paso, TX
    (-8572714, 4708788),   # 22 Washington, DC
    (-12817326, 4324038),  # 23 Las Vegas, NV
    (-9546760, 4614803),   # 24 Louisville, KY
    (-10024320, 4184284),  # 25 Memphis, TN
    (-13656675, 5703760),  # 26 Portland, OR
    (-8528186, 4763297),   # 27 Baltimore, MD
    (-9784983, 5318062),   # 28 Milwaukee, WI
    (-11872224, 4174758),  # 29 Albuquerque, NM
    (-12353124, 3792224),  # 30 Tucson, AZ
    (-13334962, 4402928),  # 31 Fresno, CA
    (-13524205, 4661687),  # 32 Sacramento, CA
    (-12448859, 3951186),  # 33 Mesa, AZ
    (-10528597, 4736006),  # 34 Kansas City, MO
    (-9394252, 3995282),   # 35 Atlanta, GA
    (-10679992, 5050768),  # 36 Omaha, NE
    (-11668509, 4697350),  # 37 Colorado Springs, CO
    (-8754165, 4270392),   # 38 Raleigh, NC
    (-13156851, 3997960),  # 39 Long Beach, CA
    (-8458055, 4418219),   # 40 Virginia Beach, VA
    (-10382769, 5618373),  # 41 Minneapolis, MN
    (-9179405, 3242671),   # 42 Tampa, FL
    (-10027660, 3497124),  # 43 New Orleans, LA
    (-10811349, 3855551),  # 44 Arlington, TX
    (-10835839, 4535725),  # 45 Wichita, KS
    (-13249246, 4214277),  # 46 Bakersfield, CA
    (-11669622, 4823889),  # 47 Aurora, CO
    (-13125681, 4007338),  # 48 Anaheim, CA
    (-13121228, 3995282),  # 49 Santa Ana, CA
    (-10842518, 3223782),  # 50 Corpus Christi, TX
    (-13068908, 4022090),  # 51 Riverside, CA
    (-10041018, 4668810),  # 52 St. Louis, MO
    (-9406497, 4585078),   # 53 Lexington, KY
    (-8904446, 4930089),   # 54 Pittsburgh, PA
    (-13501941, 4575189),  # 55 Stockton, CA
    (-10362731, 5612081),  # 56 Saint Paul, MN
    (-9407610, 4736006),   # 57 Cincinnati, OH
    (-8882182, 4310258),   # 58 Greensboro, NC
    (-9301857, 5110184),   # 59 Toledo, OH
    (-8256567, 4971129),   # 60 Newark, NJ
    (-10764595, 3897959),  # 61 Plano, TX
    (-12799515, 4306127),  # 62 Henderson, NV
    (-9059180, 3317228),   # 63 Orlando, FL
    (-12449972, 3935192),  # 64 Chandler, AZ
    (-9199443, 3220007),   # 65 St. Petersburg, FL
    (-11075176, 3188590),  # 66 Laredo, TX
    (-8492564, 4418219),   # 67 Norfolk, VA
    (-9951962, 5322633),   # 68 Madison, WI
    (-8783108, 4299245),   # 69 Durham, NC
    (-11337890, 3971209),  # 70 Lubbock, TX
    (-8932276, 4314390),   # 71 Winston-Salem, NC
    (-10757916, 3883364),  # 72 Garland, TX
    (-12488934, 3965866),  # 73 Glendale, AZ
    (-8936729, 2981752),   # 74 Hialeah, FL
    (-13337188, 4797876),  # 75 Reno, NV
    (-10144545, 3561525),  # 76 Baton Rouge, LA
    (-13110096, 3984577),  # 77 Irvine, CA
    (-8492564, 4407096),   # 78 Chesapeake, VA
    (-10792425, 3870112),  # 79 Irving, TX
    (-12459991, 3960525),  # 80 Scottsdale, AZ
    (-12815100, 4328176),  # 81 North Las Vegas, NV
    (-13579865, 4516050),  # 82 Fremont, CA
    (-12444406, 3941853),  # 83 Gilbert, AZ
    (-13056663, 4043582),  # 84 San Bernardino, CA
    (-9662532, 3964530),   # 85 Birmingham, AL
    (-8639506, 5336357),   # 86 Rochester, NY
    (-8622808, 4516050),   # 87 Richmond, VA
    (-13072248, 6050476),  # 88 Spokane, WA
    (-10421731, 5099760),  # 89 Des Moines, IA
    (-9606872, 3810660),   # 90 Montgomery, AL
    (-13468545, 4528694),  # 91 Modesto, CA
    (-8780881, 4170678),   # 92 Fayetteville, NC
    (-13629958, 5982976),  # 93 Tacoma, WA
    (-10436202, 3831764),  # 94 Shreveport, LA
    (-13072248, 4040893),  # 95 Fontana, CA
    (-13049984, 4019407),  # 96 Moreno Valley, CA
    (-13164643, 4047616),  # 97 Glendale, CA
    (-9074765, 5024149),   # 98 Akron, OH
    (-13135700, 3983239),  # 99 Huntington Beach, CA
]


if DATASET == "finland":
    nodes = nodes_finland
    CRS = "EPSG:3067"
if DATASET == "usa":
    nodes = nodes_usa
    CRS = "EPSG:3857"
if DATASET == "own":
    nodes = nodes_own
    CRS = "EPSG:xxxx"  # change to your EPSG code if you know it, or set to None if not sure

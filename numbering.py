# we follow the heorot.dk numbering throughout

FITT_BOUNDARIES = [
    (1, 52, 'Prologue'),  # prologue
    (53, 114, 'I'),  # 1
    (115, 188, 'II'),
    (189, 257, 'III'),
    (258, 319, 'IIII'),
    (320, 370, 'V'),  # 5
    (371, 455, 'VI'),
    (456, 498, 'VII'),
    (499, 558, 'VIII'),
    (559, 661, 'VIIII'),
    (662, 709, 'X'),  # 10
    (710, 790, 'XI'),
    (791, 836, 'XII'),
    (837, 924, 'XIII'),
    (925, 990, 'XIIII'),
    (991, 1049, 'XV'),  # 15
    (1050, 1124, 'XVI'),
    (1125, 1191, 'XVII'),
    (1192, 1250, 'XVIII'),
    (1251, 1320, 'XVIIII'),
    (1321, 1382, 'XX'),  # 20
    (1383, 1472, 'XXI'),
    (1473, 1556, 'XXII'),  # 22 -- there is no 24
    (1557, 1650, 'XXIII'),
    (0, 0, 'XXIIII'),  # 24 is not real, but having it in the array makes calcs easier
    (1651, 1739, 'XXV'),
    (1740, 1816, 'XXVI'),  # 26
    (1817, 1887, 'XXVII'),
    (1888, 1962, 'XXVIII'),
    (1963, 2038, 'XXVIIII'),
    (2039, 2143, 'XXX'),  # 30
    (2144, 2220, 'XXXI'),
    (2221, 2311, 'XXXII'),
    (2312, 2390, 'XXXIII'),
    (2391, 2459, 'XXXIIII'),
    (2460, 2601, 'XXXV'),  # 35
    (2602, 2693, 'XXXVI'),
    (2694, 2751, 'XXXVII'),
    (2752, 2820, 'XXXVIII'),
    (2821, 2891, 'XXXVIIII'),
    (2892, 2945, 'XL'),  # 40
    (2946, 3057, 'XLI'),
    (3058, 3136, 'XLII'),
    (3137, 3182, 'XLIII')
]

LINE_NUMBER_MARKERS = {
    5: 5, 10: 10, 15: 15, 20: 20, 25: 25, 30: 30, 35: 35, 40: 40, 45: 45, 50: 50, 55: 55, 60: 60, 65: 65,
    70: 70, 75: 75, 80: 80, 85: 85, 90: 90, 95: 95, 100: 100, 105: 105, 110: 110, 115: 115, 120: 120, 125: 125,
    130: 130, 135: 135, 140: 140, 145: 145, 150: 150, 155: 155, 160: 160, 165: 165, 170: 170, 175: 175,
    180: 180, 185: 185, 190: 190, 195: 195, 200: 200, 205: 205, 210: 210, 215: 215, 220: 220, 225: 225,
    230: 230, 235: 235, 240: 240, 245: 245, 250: 250, 255: 255, 260: 260, 265: 265, 270: 270, 275: 275,
    280: 280, 285: 285, 290: 290, 295: 295, 300: 300, 305: 305, 310: 310, 315: 315, 320: 320, 325: 325,
    330: 330, 335: 335, 340: 340, 345: 345, 350: 350, 355: 355, 360: 360, 365: 365, 370: 370, 375: 375,
    380: 380, 385: 385, 391: 391, 396: 396, 401: 401, 406: 406, 411: 411, 416: 416, 421: 421, 426: 426,
    431: 431, 436: 436, 441: 441, 446: 446, 451: 451, 456: 456, 461: 461, 466: 466, 471: 471, 476: 476,
    481: 481, 486: 486, 491: 491, 496: 496, 501: 501, 506: 506, 511: 511, 516: 516, 521: 521, 526: 526,
    531: 531, 536: 536, 541: 541, 546: 546, 551: 551, 556: 556, 561: 561, 566: 566, 571: 571, 576: 576,
    581: 581, 586: 586, 591: 591, 596: 596, 601: 601, 606: 606, 611: 611, 616: 616, 621: 621, 626: 626,
    631: 631, 636: 636, 641: 641, 646: 646, 651: 651, 656: 656, 661: 661, 666: 666, 671: 671, 676: 676,
    681: 681, 686: 686, 691: 691, 696: 696, 701: 701, 706: 706, 711: 711, 716: 716, 721: 721, 726: 726,
    731: 731, 736: 736, 741: 741, 746: 746, 751: 751, 756: 756, 761: 761, 766: 766, 771: 771, 776: 776,
    781: 781, 786: 786, 791: 791, 796: 796, 801: 801, 806: 806, 811: 811, 816: 816, 821: 821, 826: 826,
    831: 831, 836: 836, 841: 841, 846: 846, 851: 851, 856: 856, 861: 861, 866: 866, 871: 871, 876: 876,
    881: 881, 886: 886, 891: 891, 896: 896, 901: 901, 906: 906, 911: 911, 916: 916, 921: 921, 926: 926,
    931: 931, 936: 936, 941: 941, 946: 946, 951: 951, 956: 956, 961: 961, 966: 966, 971: 971, 976: 976,
    981: 981, 986: 986, 991: 991, 996: 996, 1001: 1001, 1006: 1006, 1011: 1011, 1016: 1016, 1021: 1021,
    1026: 1026, 1031: 1031, 1036: 1036, 1041: 1041, 1046: 1046, 1051: 1051, 1056: 1056, 1061: 1061, 1066: 1066,
    1071: 1071, 1076: 1076, 1081: 1081, 1086: 1086, 1091: 1091, 1096: 1096, 1101: 1101, 1106: 1106, 1111: 1111,
    1116: 1116, 1121: 1121, 1126: 1126, 1131: 1131, 1136: 1136, 1141: 1141, 1146: 1146, 1151: 1151, 1156: 1156,
    1161: 1161, 1166: 1166, 1173: 1173, 1178: 1178, 1183: 1183, 1188: 1188, 1193: 1193, 1198: 1198, 1203: 1203,
    1208: 1208, 1213: 1213, 1218: 1218, 1223: 1223, 1228: 1228, 1233: 1233, 1238: 1238, 1243: 1243, 1248: 1248,
    1253: 1253, 1258: 1258, 1263: 1263, 1268: 1268, 1273: 1273, 1278: 1278, 1283: 1283, 1288: 1288, 1293: 1293,
    1298: 1298, 1303: 1303, 1308: 1308, 1313: 1313, 1318: 1318, 1323: 1323, 1328: 1328, 1333: 1333, 1338: 1338,
    1343: 1343, 1348: 1348, 1353: 1353, 1358: 1358, 1363: 1363, 1368: 1368, 1373: 1373, 1378: 1378, 1383: 1383,
    1388: 1388, 1393: 1393, 1398: 1398, 1403: 1403, 1408: 1408, 1413: 1413, 1418: 1418, 1423: 1423, 1428: 1428,
    1433: 1433, 1438: 1438, 1443: 1443, 1448: 1448, 1453: 1453, 1458: 1458, 1463: 1463, 1468: 1468, 1473: 1473,
    1478: 1478, 1483: 1483, 1488: 1488, 1493: 1493, 1498: 1498, 1503: 1503, 1508: 1508, 1513: 1513, 1518: 1518,
    1523: 1523, 1528: 1528, 1533: 1533, 1538: 1538, 1543: 1543, 1548: 1548, 1553: 1553, 1558: 1558, 1563: 1563,
    1568: 1568, 1573: 1573, 1578: 1578, 1583: 1583, 1588: 1588, 1593: 1593, 1598: 1598, 1603: 1603, 1608: 1608,
    1613: 1613, 1618: 1618, 1623: 1623, 1628: 1628, 1633: 1633, 1638: 1638, 1643: 1643, 1648: 1648, 1653: 1653,
    1658: 1658, 1663: 1663, 1668: 1668, 1673: 1673, 1678: 1678, 1683: 1683, 1688: 1688, 1693: 1693, 1698: 1698,
    1703: 1703, 1707: 1707, 1712: 1712, 1717: 1717, 1722: 1722, 1727: 1727, 1732: 1732, 1737: 1737, 1742: 1742,
    1747: 1747, 1752: 1752, 1757: 1757, 1762: 1762, 1767: 1767, 1772: 1772, 1777: 1777, 1782: 1782, 1787: 1787,
    1792: 1792, 1797: 1797, 1802: 1802, 1807: 1807, 1812: 1812, 1817: 1817, 1822: 1822, 1827: 1827, 1832: 1832,
    1837: 1837, 1842: 1842, 1847: 1847, 1852: 1852, 1857: 1857, 1862: 1862, 1867: 1867, 1872: 1872, 1877: 1877,
    1882: 1882, 1887: 1887, 1892: 1892, 1897: 1897, 1902: 1902, 1907: 1907, 1912: 1912, 1917: 1917, 1922: 1922,
    1927: 1927, 1932: 1932, 1937: 1937, 1942: 1942, 1947: 1947, 1952: 1952, 1957: 1957, 1962: 1962, 1967: 1967,
    1972: 1972, 1977: 1977, 1982: 1982, 1987: 1987, 1992: 1992, 1997: 1997, 2002: 2002, 2007: 2007, 2012: 2012,
    2017: 2017, 2022: 2022, 2027: 2027, 2032: 2032, 2037: 2037, 2042: 2042, 2047: 2047, 2052: 2052, 2057: 2057,
    2062: 2062, 2067: 2067, 2072: 2072, 2077: 2077, 2082: 2082, 2087: 2087, 2092: 2092, 2097: 2097, 2102: 2102,
    2107: 2107, 2112: 2112, 2117: 2117, 2122: 2122, 2127: 2127, 2132: 2132, 2137: 2137, 2142: 2142, 2147: 2147,
    2152: 2152, 2157: 2157, 2162: 2162, 2167: 2167, 2172: 2172, 2177: 2177, 2182: 2182, 2187: 2187, 2192: 2192,
    2197: 2197, 2202: 2202, 2207: 2207, 2212: 2212, 2217: 2217, 2222: 2222, 2227: 2227, 2230: 2230, 2234: 2234,
    2239: 2239, 2244: 2244, 2249: 2249, 2254: 2254, 2259: 2259, 2264: 2264, 2269: 2269, 2274: 2274, 2279: 2279,
    2284: 2284, 2289: 2289, 2294: 2294, 2299: 2299, 2304: 2304, 2309: 2309, 2314: 2314, 2319: 2319, 2324: 2324,
    2329: 2329, 2334: 2334, 2339: 2339, 2344: 2344, 2349: 2349, 2354: 2354, 2359: 2359, 2364: 2364, 2369: 2369,
    2374: 2374, 2379: 2379, 2384: 2384, 2389: 2389, 2394: 2394, 2399: 2399, 2404: 2404, 2409: 2409, 2414: 2414,
    2419: 2419, 2424: 2424, 2429: 2429, 2434: 2434, 2439: 2439, 2444: 2444, 2449: 2449, 2454: 2454, 2459: 2459,
    2464: 2464, 2469: 2469, 2474: 2474, 2479: 2479, 2484: 2484, 2489: 2489, 2494: 2494, 2499: 2499, 2504: 2504,
    2509: 2509, 2514: 2514, 2519: 2519, 2524: 2524, 2529: 2529, 2534: 2534, 2539: 2539, 2544: 2544, 2549: 2549,
    2554: 2554, 2559: 2559, 2564: 2564, 2569: 2569, 2574: 2574, 2579: 2579, 2584: 2584, 2589: 2589, 2594: 2594,
    2599: 2599, 2604: 2604, 2609: 2609, 2614: 2614, 2619: 2619, 2624: 2624, 2629: 2629, 2634: 2634, 2639: 2639,
    2644: 2644, 2649: 2649, 2654: 2654, 2659: 2659, 2664: 2664, 2669: 2669, 2674: 2674, 2679: 2679, 2684: 2684,
    2689: 2689, 2694: 2694, 2699: 2699, 2704: 2704, 2709: 2709, 2714: 2714, 2719: 2719, 2724: 2724, 2729: 2729,
    2734: 2734, 2739: 2739, 2744: 2744, 2749: 2749, 2754: 2754, 2759: 2759, 2764: 2764, 2769: 2769, 2774: 2774,
    2779: 2779, 2784: 2784, 2789: 2789, 2794: 2794, 2799: 2799, 2804: 2804, 2809: 2809, 2814: 2814, 2819: 2819,
    2824: 2824, 2829: 2829, 2834: 2834, 2839: 2839, 2844: 2844, 2849: 2849, 2854: 2854, 2859: 2859, 2864: 2864,
    2869: 2869, 2874: 2874, 2879: 2879, 2884: 2884, 2889: 2889, 2894: 2894, 2899: 2899, 2904: 2904, 2909: 2909,
    2914: 2914, 2919: 2919, 2924: 2924, 2929: 2929, 2934: 2934, 2939: 2939, 2944: 2944, 2949: 2949, 2954: 2954,
    2959: 2959, 2964: 2964, 2969: 2969, 2974: 2974, 2979: 2979, 2984: 2984, 2989: 2989, 2994: 2994, 2998: 2998,
    3003: 3003, 3008: 3008, 3013: 3013, 3018: 3018, 3023: 3023, 3028: 3028, 3033: 3033, 3038: 3038, 3043: 3043,
    3048: 3048, 3053: 3053, 3058: 3058, 3063: 3063, 3068: 3068, 3073: 3073, 3078: 3078, 3083: 3083, 3088: 3088,
    3093: 3093, 3098: 3098, 3103: 3103, 3108: 3108, 3113: 3113, 3118: 3118, 3123: 3123, 3128: 3128, 3133: 3133,
    3138: 3138, 3143: 3143, 3148: 3148, 3153: 3153, 3158: 3158, 3163: 3163, 3168: 3168, 3173: 3173, 3178: 3178}
#
# number_markers = {}
# offset = 0
# for i in range(0, 3182):
#     if i == 386:
#         offset += 1
#     if i == 1167:
#         offset += 2
#     if i == 1704:
#         offset -= 1
#     if i == 2228:
#         offset -= 2
#     if i == 2231:
#         offset -= 1
#     if i == 2996:
#         offset = -2
#     if i > 0 and i % 5 == 0:
#         number_markers[i + offset] = i + offset
#
# print(number_markers)

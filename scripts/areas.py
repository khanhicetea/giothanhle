import re
import json


vn_areas = {
  "1": {
    "id": "1",
    "name": "An Giang",
    "code": "89",
    "parent_id": "0",
    "slug": "an giang"
  },
  "2": {
    "id": "2",
    "name": "Bà Rịa - Vũng Tàu",
    "code": "77",
    "parent_id": "0",
    "slug": "ba ria - vung tau"
  },
  "3": {
    "id": "3",
    "name": "Bắc Giang",
    "code": "24",
    "parent_id": "0",
    "slug": "bac giang"
  },
  "4": {
    "id": "4",
    "name": "Bắc Kạn",
    "code": "06",
    "parent_id": "0",
    "slug": "bac kan"
  },
  "5": {
    "id": "5",
    "name": "Bạc Liêu",
    "code": "95",
    "parent_id": "0",
    "slug": "bac lieu"
  },
  "6": {
    "id": "6",
    "name": "Bắc Ninh",
    "code": "27",
    "parent_id": "0",
    "slug": "bac ninh"
  },
  "7": {
    "id": "7",
    "name": "Bến Tre",
    "code": "83",
    "parent_id": "0",
    "slug": "ben tre"
  },
  "8": {
    "id": "8",
    "name": "Bình Định",
    "code": "52",
    "parent_id": "0",
    "slug": "binh dinh"
  },
  "9": {
    "id": "9",
    "name": "Bình Dương",
    "code": "74",
    "parent_id": "0",
    "slug": "binh duong"
  },
  "10": {
    "id": "10",
    "name": "Bình Phước",
    "code": "70",
    "parent_id": "0",
    "slug": "binh phuoc"
  },
  "11": {
    "id": "11",
    "name": "Bình Thuận",
    "code": "60",
    "parent_id": "0",
    "slug": "binh thuan"
  },
  "12": {
    "id": "12",
    "name": "Cà Mau",
    "code": "96",
    "parent_id": "0",
    "slug": "ca mau"
  },
  "13": {
    "id": "13",
    "name": "Cần Thơ",
    "code": "92",
    "parent_id": "0",
    "slug": "can tho"
  },
  "14": {
    "id": "14",
    "name": "Cao Bằng",
    "code": "04",
    "parent_id": "0",
    "slug": "cao bang"
  },
  "15": {
    "id": "15",
    "name": "Đà Nẵng",
    "code": "48",
    "parent_id": "0",
    "slug": "da nang"
  },
  "16": {
    "id": "16",
    "name": "Đắk Lắk",
    "code": "66",
    "parent_id": "0",
    "slug": "dak lak"
  },
  "17": {
    "id": "17",
    "name": "Đắk Nông",
    "code": "67",
    "parent_id": "0",
    "slug": "dak nong"
  },
  "18": {
    "id": "18",
    "name": "Điện Biên",
    "code": "11",
    "parent_id": "0",
    "slug": "dien bien"
  },
  "19": {
    "id": "19",
    "name": "Đồng Nai",
    "code": "75",
    "parent_id": "0",
    "slug": "dong nai"
  },
  "20": {
    "id": "20",
    "name": "Đồng Tháp",
    "code": "87",
    "parent_id": "0",
    "slug": "dong thap"
  },
  "21": {
    "id": "21",
    "name": "Gia Lai",
    "code": "64",
    "parent_id": "0",
    "slug": "gia lai"
  },
  "22": {
    "id": "22",
    "name": "Hà Giang",
    "code": "02",
    "parent_id": "0",
    "slug": "ha giang"
  },
  "23": {
    "id": "23",
    "name": "Hà Nam",
    "code": "35",
    "parent_id": "0",
    "slug": "ha nam"
  },
  "24": {
    "id": "24",
    "name": "Hà Nội",
    "code": "01",
    "parent_id": "0",
    "slug": "ha noi"
  },
  "25": {
    "id": "25",
    "name": "Hà Tĩnh",
    "code": "42",
    "parent_id": "0",
    "slug": "ha tinh"
  },
  "26": {
    "id": "26",
    "name": "Hải Dương",
    "code": "30",
    "parent_id": "0",
    "slug": "hai duong"
  },
  "27": {
    "id": "27",
    "name": "Hải Phòng",
    "code": "31",
    "parent_id": "0",
    "slug": "hai phong"
  },
  "28": {
    "id": "28",
    "name": "Hậu Giang",
    "code": "93",
    "parent_id": "0",
    "slug": "hau giang"
  },
  "29": {
    "id": "29",
    "name": "Hoà Bình",
    "code": "17",
    "parent_id": "0",
    "slug": "hoa binh"
  },
  "30": {
    "id": "30",
    "name": "Hồ Chí Minh",
    "code": "79",
    "parent_id": "0",
    "slug": "ho chi minh"
  },
  "31": {
    "id": "31",
    "name": "Hưng Yên",
    "code": "33",
    "parent_id": "0",
    "slug": "hung yen"
  },
  "32": {
    "id": "32",
    "name": "Khánh Hòa",
    "code": "56",
    "parent_id": "0",
    "slug": "khanh hoa"
  },
  "33": {
    "id": "33",
    "name": "Kiên Giang",
    "code": "91",
    "parent_id": "0",
    "slug": "kien giang"
  },
  "34": {
    "id": "34",
    "name": "Kon Tum",
    "code": "62",
    "parent_id": "0",
    "slug": "kon tum"
  },
  "35": {
    "id": "35",
    "name": "Lai Châu",
    "code": "12",
    "parent_id": "0",
    "slug": "lai chau"
  },
  "36": {
    "id": "36",
    "name": "Lâm Đồng",
    "code": "68",
    "parent_id": "0",
    "slug": "lam dong"
  },
  "37": {
    "id": "37",
    "name": "Lạng Sơn",
    "code": "20",
    "parent_id": "0",
    "slug": "lang son"
  },
  "38": {
    "id": "38",
    "name": "Lào Cai",
    "code": "10",
    "parent_id": "0",
    "slug": "lao cai"
  },
  "39": {
    "id": "39",
    "name": "Long An",
    "code": "80",
    "parent_id": "0",
    "slug": "long an"
  },
  "40": {
    "id": "40",
    "name": "Nam Định",
    "code": "36",
    "parent_id": "0",
    "slug": "nam dinh"
  },
  "41": {
    "id": "41",
    "name": "Nghệ An",
    "code": "40",
    "parent_id": "0",
    "slug": "nghe an"
  },
  "42": {
    "id": "42",
    "name": "Ninh Bình",
    "code": "37",
    "parent_id": "0",
    "slug": "ninh binh"
  },
  "43": {
    "id": "43",
    "name": "Ninh Thuận",
    "code": "58",
    "parent_id": "0",
    "slug": "ninh thuan"
  },
  "44": {
    "id": "44",
    "name": "Phú Thọ",
    "code": "25",
    "parent_id": "0",
    "slug": "phu tho"
  },
  "45": {
    "id": "45",
    "name": "Phú Yên",
    "code": "54",
    "parent_id": "0",
    "slug": "phu yen"
  },
  "46": {
    "id": "46",
    "name": "Quảng Bình",
    "code": "44",
    "parent_id": "0",
    "slug": "quang binh"
  },
  "47": {
    "id": "47",
    "name": "Quảng Nam",
    "code": "49",
    "parent_id": "0",
    "slug": "quang nam"
  },
  "48": {
    "id": "48",
    "name": "Quảng Ngãi",
    "code": "51",
    "parent_id": "0",
    "slug": "quang ngai"
  },
  "49": {
    "id": "49",
    "name": "Quảng Ninh",
    "code": "22",
    "parent_id": "0",
    "slug": "quang ninh"
  },
  "50": {
    "id": "50",
    "name": "Quảng Trị",
    "code": "45",
    "parent_id": "0",
    "slug": "quang tri"
  },
  "51": {
    "id": "51",
    "name": "Sóc Trăng",
    "code": "94",
    "parent_id": "0",
    "slug": "soc trang"
  },
  "52": {
    "id": "52",
    "name": "Sơn La",
    "code": "14",
    "parent_id": "0",
    "slug": "son la"
  },
  "53": {
    "id": "53",
    "name": "Tây Ninh",
    "code": "72",
    "parent_id": "0",
    "slug": "tay ninh"
  },
  "54": {
    "id": "54",
    "name": "Thái Bình",
    "code": "34",
    "parent_id": "0",
    "slug": "thai binh"
  },
  "55": {
    "id": "55",
    "name": "Thái Nguyên",
    "code": "19",
    "parent_id": "0",
    "slug": "thai nguyen"
  },
  "56": {
    "id": "56",
    "name": "Thanh Hóa",
    "code": "38",
    "parent_id": "0",
    "slug": "thanh hoa"
  },
  "57": {
    "id": "57",
    "name": "Thừa Thiên Huế",
    "code": "46",
    "parent_id": "0",
    "slug": "thua thien hue"
  },
  "58": {
    "id": "58",
    "name": "Tiền Giang",
    "code": "82",
    "parent_id": "0",
    "slug": "tien giang"
  },
  "59": {
    "id": "59",
    "name": "Trà Vinh",
    "code": "84",
    "parent_id": "0",
    "slug": "tra vinh"
  },
  "60": {
    "id": "60",
    "name": "Tuyên Quang",
    "code": "08",
    "parent_id": "0",
    "slug": "tuyen quang"
  },
  "61": {
    "id": "61",
    "name": "Vĩnh Long",
    "code": "86",
    "parent_id": "0",
    "slug": "vinh long"
  },
  "62": {
    "id": "62",
    "name": "Vĩnh Phúc",
    "code": "26",
    "parent_id": "0",
    "slug": "vinh phuc"
  },
  "63": {
    "id": "63",
    "name": "Yên Bái",
    "code": "15",
    "parent_id": "0",
    "slug": "yen bai"
  },
  "100": {
    "id": "100",
    "name": "Huyện An Phú",
    "code": "886",
    "parent_id": "1",
    "slug": "huyen an phu"
  },
  "101": {
    "id": "101",
    "name": "Huyện Châu Phú",
    "code": "889",
    "parent_id": "1",
    "slug": "huyen chau phu"
  },
  "102": {
    "id": "102",
    "name": "Huyện Châu Thành",
    "code": "892",
    "parent_id": "1",
    "slug": "huyen chau thanh"
  },
  "103": {
    "id": "103",
    "name": "Huyện Chợ Mới",
    "code": "893",
    "parent_id": "1",
    "slug": "huyen cho moi"
  },
  "104": {
    "id": "104",
    "name": "Huyện Phú Tân",
    "code": "888",
    "parent_id": "1",
    "slug": "huyen phu tan"
  },
  "105": {
    "id": "105",
    "name": "Huyện Thoại Sơn",
    "code": "894",
    "parent_id": "1",
    "slug": "huyen thoai son"
  },
  "106": {
    "id": "106",
    "name": "Huyện Tịnh Biên",
    "code": "890",
    "parent_id": "1",
    "slug": "huyen tinh bien"
  },
  "107": {
    "id": "107",
    "name": "Huyện Tri Tôn",
    "code": "891",
    "parent_id": "1",
    "slug": "huyen tri ton"
  },
  "108": {
    "id": "108",
    "name": "Thành phố Châu Đốc",
    "code": "884",
    "parent_id": "1",
    "slug": "thanh pho chau doc"
  },
  "109": {
    "id": "109",
    "name": "Thành phố Long Xuyên",
    "code": "883",
    "parent_id": "1",
    "slug": "thanh pho long xuyen"
  },
  "110": {
    "id": "110",
    "name": "Thị xã Tân Châu",
    "code": "887",
    "parent_id": "1",
    "slug": "thi xa tan chau"
  },
  "111": {
    "id": "111",
    "name": "Huyện Châu Đức",
    "code": "750",
    "parent_id": "2",
    "slug": "huyen chau duc"
  },
  "112": {
    "id": "112",
    "name": "Huyện Đất Đỏ",
    "code": "753",
    "parent_id": "2",
    "slug": "huyen dat do"
  },
  "113": {
    "id": "113",
    "name": "Huyện Long Điền",
    "code": "752",
    "parent_id": "2",
    "slug": "huyen long dien"
  },
  "114": {
    "id": "114",
    "name": "Huyện Tân Thành",
    "code": "754",
    "parent_id": "2",
    "slug": "huyen tan thanh"
  },
  "115": {
    "id": "115",
    "name": "Huyện Xuyên Mộc",
    "code": "751",
    "parent_id": "2",
    "slug": "huyen xuyen moc"
  },
  "116": {
    "id": "116",
    "name": "Thành phố Bà Rịa",
    "code": "748",
    "parent_id": "2",
    "slug": "thanh pho ba ria"
  },
  "117": {
    "id": "117",
    "name": "Thành phố Vũng Tàu",
    "code": "747",
    "parent_id": "2",
    "slug": "thanh pho vung tau"
  },
  "118": {
    "id": "118",
    "name": "Huyện Hiệp Hòa",
    "code": "223",
    "parent_id": "3",
    "slug": "huyen hiep hoa"
  },
  "119": {
    "id": "119",
    "name": "Huyện Lạng Giang",
    "code": "217",
    "parent_id": "3",
    "slug": "huyen lang giang"
  },
  "120": {
    "id": "120",
    "name": "Huyện Lục Nam",
    "code": "218",
    "parent_id": "3",
    "slug": "huyen luc nam"
  },
  "121": {
    "id": "121",
    "name": "Huyện Lục Ngạn",
    "code": "219",
    "parent_id": "3",
    "slug": "huyen luc ngan"
  },
  "122": {
    "id": "122",
    "name": "Huyện Sơn Động",
    "code": "220",
    "parent_id": "3",
    "slug": "huyen son dong"
  },
  "123": {
    "id": "123",
    "name": "Huyện Tân Yên",
    "code": "216",
    "parent_id": "3",
    "slug": "huyen tan yen"
  },
  "124": {
    "id": "124",
    "name": "Huyện Việt Yên",
    "code": "222",
    "parent_id": "3",
    "slug": "huyen viet yen"
  },
  "125": {
    "id": "125",
    "name": "Huyện Yên Dũng",
    "code": "221",
    "parent_id": "3",
    "slug": "huyen yen dung"
  },
  "126": {
    "id": "126",
    "name": "Huyện Yên Thế",
    "code": "215",
    "parent_id": "3",
    "slug": "huyen yen the"
  },
  "127": {
    "id": "127",
    "name": "Thành phố Bắc Giang",
    "code": "213",
    "parent_id": "3",
    "slug": "thanh pho bac giang"
  },
  "128": {
    "id": "128",
    "name": "Huyện Ba Bể",
    "code": "061",
    "parent_id": "4",
    "slug": "huyen ba be"
  },
  "129": {
    "id": "129",
    "name": "Huyện Bạch Thông",
    "code": "063",
    "parent_id": "4",
    "slug": "huyen bach thong"
  },
  "130": {
    "id": "130",
    "name": "Huyện Chợ Đồn",
    "code": "064",
    "parent_id": "4",
    "slug": "huyen cho don"
  },
  "131": {
    "id": "131",
    "name": "Huyện Chợ Mới",
    "code": "065",
    "parent_id": "4",
    "slug": "huyen cho moi"
  },
  "132": {
    "id": "132",
    "name": "Huyện Na Rì",
    "code": "066",
    "parent_id": "4",
    "slug": "huyen na ri"
  },
  "133": {
    "id": "133",
    "name": "Huyện Ngân Sơn",
    "code": "062",
    "parent_id": "4",
    "slug": "huyen ngan son"
  },
  "134": {
    "id": "134",
    "name": "Huyện Pác Nặm",
    "code": "060",
    "parent_id": "4",
    "slug": "huyen pac nam"
  },
  "135": {
    "id": "135",
    "name": "Thành Phố Bắc Kạn",
    "code": "058",
    "parent_id": "4",
    "slug": "thanh pho bac kan"
  },
  "136": {
    "id": "136",
    "name": "Huyện Đông Hải",
    "code": "960",
    "parent_id": "5",
    "slug": "huyen dong hai"
  },
  "137": {
    "id": "137",
    "name": "Huyện Hoà Bình",
    "code": "961",
    "parent_id": "5",
    "slug": "huyen hoa binh"
  },
  "138": {
    "id": "138",
    "name": "Huyện Hồng Dân",
    "code": "956",
    "parent_id": "5",
    "slug": "huyen hong dan"
  },
  "139": {
    "id": "139",
    "name": "Huyện Phước Long",
    "code": "957",
    "parent_id": "5",
    "slug": "huyen phuoc long"
  },
  "140": {
    "id": "140",
    "name": "Huyện Vĩnh Lợi",
    "code": "958",
    "parent_id": "5",
    "slug": "huyen vinh loi"
  },
  "141": {
    "id": "141",
    "name": "Thành phố Bạc Liêu",
    "code": "954",
    "parent_id": "5",
    "slug": "thanh pho bac lieu"
  },
  "142": {
    "id": "142",
    "name": "Thị xã Giá Rai",
    "code": "959",
    "parent_id": "5",
    "slug": "thi xa gia rai"
  },
  "143": {
    "id": "143",
    "name": "Huyện Gia Bình",
    "code": "263",
    "parent_id": "6",
    "slug": "huyen gia binh"
  },
  "144": {
    "id": "144",
    "name": "Huyện Lương Tài",
    "code": "264",
    "parent_id": "6",
    "slug": "huyen luong tai"
  },
  "145": {
    "id": "145",
    "name": "Huyện Quế Võ",
    "code": "259",
    "parent_id": "6",
    "slug": "huyen que vo"
  },
  "146": {
    "id": "146",
    "name": "Huyện Thuận Thành",
    "code": "262",
    "parent_id": "6",
    "slug": "huyen thuan thanh"
  },
  "147": {
    "id": "147",
    "name": "Huyện Tiên Du",
    "code": "260",
    "parent_id": "6",
    "slug": "huyen tien du"
  },
  "148": {
    "id": "148",
    "name": "Huyện Yên Phong",
    "code": "258",
    "parent_id": "6",
    "slug": "huyen yen phong"
  },
  "149": {
    "id": "149",
    "name": "Thành phố Bắc Ninh",
    "code": "256",
    "parent_id": "6",
    "slug": "thanh pho bac ninh"
  },
  "150": {
    "id": "150",
    "name": "Thị xã Từ Sơn",
    "code": "261",
    "parent_id": "6",
    "slug": "thi xa tu son"
  },
  "151": {
    "id": "151",
    "name": "Huyện Ba Tri",
    "code": "836",
    "parent_id": "7",
    "slug": "huyen ba tri"
  },
  "152": {
    "id": "152",
    "name": "Huyện Bình Đại",
    "code": "835",
    "parent_id": "7",
    "slug": "huyen binh dai"
  },
  "153": {
    "id": "153",
    "name": "Huyện Châu Thành",
    "code": "831",
    "parent_id": "7",
    "slug": "huyen chau thanh"
  },
  "154": {
    "id": "154",
    "name": "Huyện Chợ Lách",
    "code": "832",
    "parent_id": "7",
    "slug": "huyen cho lach"
  },
  "155": {
    "id": "155",
    "name": "Huyện Giồng Trôm",
    "code": "834",
    "parent_id": "7",
    "slug": "huyen giong trom"
  },
  "156": {
    "id": "156",
    "name": "Huyện Mỏ Cày Bắc",
    "code": "838",
    "parent_id": "7",
    "slug": "huyen mo cay bac"
  },
  "157": {
    "id": "157",
    "name": "Huyện Mỏ Cày Nam",
    "code": "833",
    "parent_id": "7",
    "slug": "huyen mo cay nam"
  },
  "158": {
    "id": "158",
    "name": "Huyện Thạnh Phú",
    "code": "837",
    "parent_id": "7",
    "slug": "huyen thanh phu"
  },
  "159": {
    "id": "159",
    "name": "Thành phố Bến Tre",
    "code": "829",
    "parent_id": "7",
    "slug": "thanh pho ben tre"
  },
  "160": {
    "id": "160",
    "name": "Huyện An Lão",
    "code": "542",
    "parent_id": "8",
    "slug": "huyen an lao"
  },
  "161": {
    "id": "161",
    "name": "Huyện Hoài Ân",
    "code": "544",
    "parent_id": "8",
    "slug": "huyen hoai an"
  },
  "162": {
    "id": "162",
    "name": "Huyện Hoài Nhơn",
    "code": "543",
    "parent_id": "8",
    "slug": "huyen hoai nhon"
  },
  "163": {
    "id": "163",
    "name": "Huyện Phù Cát",
    "code": "548",
    "parent_id": "8",
    "slug": "huyen phu cat"
  },
  "164": {
    "id": "164",
    "name": "Huyện Phù Mỹ",
    "code": "545",
    "parent_id": "8",
    "slug": "huyen phu my"
  },
  "165": {
    "id": "165",
    "name": "Huyện Tây Sơn",
    "code": "547",
    "parent_id": "8",
    "slug": "huyen tay son"
  },
  "166": {
    "id": "166",
    "name": "Huyện Tuy Phước",
    "code": "550",
    "parent_id": "8",
    "slug": "huyen tuy phuoc"
  },
  "167": {
    "id": "167",
    "name": "Huyện Vân Canh",
    "code": "551",
    "parent_id": "8",
    "slug": "huyen van canh"
  },
  "168": {
    "id": "168",
    "name": "Huyện Vĩnh Thạnh",
    "code": "546",
    "parent_id": "8",
    "slug": "huyen vinh thanh"
  },
  "169": {
    "id": "169",
    "name": "Thành phố Qui Nhơn",
    "code": "540",
    "parent_id": "8",
    "slug": "thanh pho qui nhon"
  },
  "170": {
    "id": "170",
    "name": "Thị xã An Nhơn",
    "code": "549",
    "parent_id": "8",
    "slug": "thi xa an nhon"
  },
  "171": {
    "id": "171",
    "name": "Huyện Bắc Tân Uyên",
    "code": "726",
    "parent_id": "9",
    "slug": "huyen bac tan uyen"
  },
  "172": {
    "id": "172",
    "name": "Huyện Bàu Bàng",
    "code": "719",
    "parent_id": "9",
    "slug": "huyen bau bang"
  },
  "173": {
    "id": "173",
    "name": "Huyện Dầu Tiếng",
    "code": "720",
    "parent_id": "9",
    "slug": "huyen dau tieng"
  },
  "174": {
    "id": "174",
    "name": "Huyện Phú Giáo",
    "code": "722",
    "parent_id": "9",
    "slug": "huyen phu giao"
  },
  "175": {
    "id": "175",
    "name": "Thành phố Thủ Dầu Một",
    "code": "718",
    "parent_id": "9",
    "slug": "thanh pho thu dau mot"
  },
  "176": {
    "id": "176",
    "name": "Thị xã Bến Cát",
    "code": "721",
    "parent_id": "9",
    "slug": "thi xa ben cat"
  },
  "177": {
    "id": "177",
    "name": "Thị xã Dĩ An",
    "code": "724",
    "parent_id": "9",
    "slug": "thi xa di an"
  },
  "178": {
    "id": "178",
    "name": "Thị xã Tân Uyên",
    "code": "723",
    "parent_id": "9",
    "slug": "thi xa tan uyen"
  },
  "179": {
    "id": "179",
    "name": "Thị xã Thuận An",
    "code": "725",
    "parent_id": "9",
    "slug": "thi xa thuan an"
  },
  "180": {
    "id": "180",
    "name": "Huyện Bù Đăng",
    "code": "696",
    "parent_id": "10",
    "slug": "huyen bu dang"
  },
  "181": {
    "id": "181",
    "name": "Huyện Bù Đốp",
    "code": "693",
    "parent_id": "10",
    "slug": "huyen bu dop"
  },
  "182": {
    "id": "182",
    "name": "Huyện Bù Gia Mập",
    "code": "691",
    "parent_id": "10",
    "slug": "huyen bu gia map"
  },
  "183": {
    "id": "183",
    "name": "Huyện Chơn Thành",
    "code": "697",
    "parent_id": "10",
    "slug": "huyen chon thanh"
  },
  "184": {
    "id": "184",
    "name": "Huyện Đồng Phù",
    "code": "695",
    "parent_id": "10",
    "slug": "huyen dong phu"
  },
  "185": {
    "id": "185",
    "name": "Huyện Hớn Quản",
    "code": "694",
    "parent_id": "10",
    "slug": "huyen hon quan"
  },
  "186": {
    "id": "186",
    "name": "Huyện Lộc Ninh",
    "code": "692",
    "parent_id": "10",
    "slug": "huyen loc ninh"
  },
  "187": {
    "id": "187",
    "name": "Huyện Phú Riềng",
    "code": "698",
    "parent_id": "10",
    "slug": "huyen phu rieng"
  },
  "188": {
    "id": "188",
    "name": "Thị xã Bình Long",
    "code": "690",
    "parent_id": "10",
    "slug": "thi xa binh long"
  },
  "189": {
    "id": "189",
    "name": "Thị xã Đồng Xoài",
    "code": "689",
    "parent_id": "10",
    "slug": "thi xa dong xoai"
  },
  "190": {
    "id": "190",
    "name": "Thị xã Phước Long",
    "code": "688",
    "parent_id": "10",
    "slug": "thi xa phuoc long"
  },
  "191": {
    "id": "191",
    "name": "Huyện Bắc Bình",
    "code": "596",
    "parent_id": "11",
    "slug": "huyen bac binh"
  },
  "192": {
    "id": "192",
    "name": "Huyện Đức Linh",
    "code": "600",
    "parent_id": "11",
    "slug": "huyen duc linh"
  },
  "193": {
    "id": "193",
    "name": "Huyện Hàm Tân",
    "code": "601",
    "parent_id": "11",
    "slug": "huyen ham tan"
  },
  "194": {
    "id": "194",
    "name": "Huyện Hàm Thuận Bắc",
    "code": "597",
    "parent_id": "11",
    "slug": "huyen ham thuan bac"
  },
  "195": {
    "id": "195",
    "name": "Huyện Hàm Thuận Nam",
    "code": "598",
    "parent_id": "11",
    "slug": "huyen ham thuan nam"
  },
  "196": {
    "id": "196",
    "name": "Huyện Phú Quí",
    "code": "602",
    "parent_id": "11",
    "slug": "huyen phu qui"
  },
  "197": {
    "id": "197",
    "name": "Huyện Tánh Linh",
    "code": "599",
    "parent_id": "11",
    "slug": "huyen tanh linh"
  },
  "198": {
    "id": "198",
    "name": "Huyện Tuy Phong",
    "code": "595",
    "parent_id": "11",
    "slug": "huyen tuy phong"
  },
  "199": {
    "id": "199",
    "name": "Thành phố Phan Thiết",
    "code": "593",
    "parent_id": "11",
    "slug": "thanh pho phan thiet"
  },
  "200": {
    "id": "200",
    "name": "Thị xã La Gi",
    "code": "594",
    "parent_id": "11",
    "slug": "thi xa la gi"
  },
  "201": {
    "id": "201",
    "name": "Huyện Cái Nước",
    "code": "969",
    "parent_id": "12",
    "slug": "huyen cai nuoc"
  },
  "202": {
    "id": "202",
    "name": "Huyện Đầm Dơi",
    "code": "970",
    "parent_id": "12",
    "slug": "huyen dam doi"
  },
  "203": {
    "id": "203",
    "name": "Huyện Năm Căn",
    "code": "971",
    "parent_id": "12",
    "slug": "huyen nam can"
  },
  "204": {
    "id": "204",
    "name": "Huyện Ngọc Hiển",
    "code": "973",
    "parent_id": "12",
    "slug": "huyen ngoc hien"
  },
  "205": {
    "id": "205",
    "name": "Huyện Phú Tân",
    "code": "972",
    "parent_id": "12",
    "slug": "huyen phu tan"
  },
  "206": {
    "id": "206",
    "name": "Huyện Thới Bình",
    "code": "967",
    "parent_id": "12",
    "slug": "huyen thoi binh"
  },
  "207": {
    "id": "207",
    "name": "Huyện Trần Văn Thời",
    "code": "968",
    "parent_id": "12",
    "slug": "huyen tran van thoi"
  },
  "208": {
    "id": "208",
    "name": "Huyện U Minh",
    "code": "966",
    "parent_id": "12",
    "slug": "huyen u minh"
  },
  "209": {
    "id": "209",
    "name": "Thành phố Cà Mau",
    "code": "964",
    "parent_id": "12",
    "slug": "thanh pho ca mau"
  },
  "210": {
    "id": "210",
    "name": "Huyện Cờ Đỏ",
    "code": "925",
    "parent_id": "13",
    "slug": "huyen co do"
  },
  "211": {
    "id": "211",
    "name": "Huyện Phong Điền",
    "code": "926",
    "parent_id": "13",
    "slug": "huyen phong dien"
  },
  "212": {
    "id": "212",
    "name": "Huyện Thới Lai",
    "code": "927",
    "parent_id": "13",
    "slug": "huyen thoi lai"
  },
  "213": {
    "id": "213",
    "name": "Huyện Vĩnh Thạnh",
    "code": "924",
    "parent_id": "13",
    "slug": "huyen vinh thanh"
  },
  "214": {
    "id": "214",
    "name": "Quận Bình Thuỷ",
    "code": "918",
    "parent_id": "13",
    "slug": "quan binh thuy"
  },
  "215": {
    "id": "215",
    "name": "Quận Cái Răng",
    "code": "919",
    "parent_id": "13",
    "slug": "quan cai rang"
  },
  "216": {
    "id": "216",
    "name": "Quận Ninh Kiều",
    "code": "916",
    "parent_id": "13",
    "slug": "quan ninh kieu"
  },
  "217": {
    "id": "217",
    "name": "Quận Ô Môn",
    "code": "917",
    "parent_id": "13",
    "slug": "quan o mon"
  },
  "218": {
    "id": "218",
    "name": "Quận Thốt Nốt",
    "code": "923",
    "parent_id": "13",
    "slug": "quan thot not"
  },
  "219": {
    "id": "219",
    "name": "Huyện Bảo Lạc",
    "code": "043",
    "parent_id": "14",
    "slug": "huyen bao lac"
  },
  "220": {
    "id": "220",
    "name": "Huyện Bảo Lâm",
    "code": "042",
    "parent_id": "14",
    "slug": "huyen bao lam"
  },
  "221": {
    "id": "221",
    "name": "Huyện Hạ Lang",
    "code": "048",
    "parent_id": "14",
    "slug": "huyen ha lang"
  },
  "222": {
    "id": "222",
    "name": "Huyện Hà Quảng",
    "code": "045",
    "parent_id": "14",
    "slug": "huyen ha quang"
  },
  "223": {
    "id": "223",
    "name": "Huyện Hoà An",
    "code": "051",
    "parent_id": "14",
    "slug": "huyen hoa an"
  },
  "224": {
    "id": "224",
    "name": "Huyện Nguyên Bình",
    "code": "052",
    "parent_id": "14",
    "slug": "huyen nguyen binh"
  },
  "225": {
    "id": "225",
    "name": "Huyện Phục Hoà",
    "code": "050",
    "parent_id": "14",
    "slug": "huyen phuc hoa"
  },
  "226": {
    "id": "226",
    "name": "Huyện Quảng Uyên",
    "code": "049",
    "parent_id": "14",
    "slug": "huyen quang uyen"
  },
  "227": {
    "id": "227",
    "name": "Huyện Thạch An",
    "code": "053",
    "parent_id": "14",
    "slug": "huyen thach an"
  },
  "228": {
    "id": "228",
    "name": "Huyện Thông Nông",
    "code": "044",
    "parent_id": "14",
    "slug": "huyen thong nong"
  },
  "229": {
    "id": "229",
    "name": "Huyện Trà Lĩnh",
    "code": "046",
    "parent_id": "14",
    "slug": "huyen tra linh"
  },
  "230": {
    "id": "230",
    "name": "Huyện Trùng Khánh",
    "code": "047",
    "parent_id": "14",
    "slug": "huyen trung khanh"
  },
  "231": {
    "id": "231",
    "name": "Thành phố Cao Bằng",
    "code": "040",
    "parent_id": "14",
    "slug": "thanh pho cao bang"
  },
  "232": {
    "id": "232",
    "name": "Huyện Hòa Vang",
    "code": "497",
    "parent_id": "15",
    "slug": "huyen hoa vang"
  },
  "233": {
    "id": "233",
    "name": "Quận Cẩm Lệ",
    "code": "495",
    "parent_id": "15",
    "slug": "quan cam le"
  },
  "234": {
    "id": "234",
    "name": "Quận Hải Châu",
    "code": "492",
    "parent_id": "15",
    "slug": "quan hai chau"
  },
  "235": {
    "id": "235",
    "name": "Quận Liên Chiểu",
    "code": "490",
    "parent_id": "15",
    "slug": "quan lien chieu"
  },
  "236": {
    "id": "236",
    "name": "Quận Ngũ Hành Sơn",
    "code": "494",
    "parent_id": "15",
    "slug": "quan ngu hanh son"
  },
  "237": {
    "id": "237",
    "name": "Quận Sơn Trà",
    "code": "493",
    "parent_id": "15",
    "slug": "quan son tra"
  },
  "238": {
    "id": "238",
    "name": "Quận Thanh Khê",
    "code": "491",
    "parent_id": "15",
    "slug": "quan thanh khe"
  },
  "239": {
    "id": "239",
    "name": "Huyện Buôn Đôn",
    "code": "647",
    "parent_id": "16",
    "slug": "huyen buon don"
  },
  "240": {
    "id": "240",
    "name": "Huyện Cư Kuin",
    "code": "657",
    "parent_id": "16",
    "slug": "huyen cu kuin"
  },
  "241": {
    "id": "241",
    "name": "Huyện Cư M'gar",
    "code": "648",
    "parent_id": "16",
    "slug": "huyen cu mgar"
  },
  "242": {
    "id": "242",
    "name": "Huyện Ea H'leo",
    "code": "645",
    "parent_id": "16",
    "slug": "huyen ea hleo"
  },
  "243": {
    "id": "243",
    "name": "Huyện Ea Kar",
    "code": "651",
    "parent_id": "16",
    "slug": "huyen ea kar"
  },
  "244": {
    "id": "244",
    "name": "Huyện Ea Súp",
    "code": "646",
    "parent_id": "16",
    "slug": "huyen ea sup"
  },
  "245": {
    "id": "245",
    "name": "Huyện Krông A Na",
    "code": "655",
    "parent_id": "16",
    "slug": "huyen krong a na"
  },
  "246": {
    "id": "246",
    "name": "Huyện Krông Bông",
    "code": "653",
    "parent_id": "16",
    "slug": "huyen krong bong"
  },
  "247": {
    "id": "247",
    "name": "Huyện Krông Búk",
    "code": "649",
    "parent_id": "16",
    "slug": "huyen krong buk"
  },
  "248": {
    "id": "248",
    "name": "Huyện Krông Năng",
    "code": "650",
    "parent_id": "16",
    "slug": "huyen krong nang"
  },
  "249": {
    "id": "249",
    "name": "Huyện Krông Pắc",
    "code": "654",
    "parent_id": "16",
    "slug": "huyen krong pac"
  },
  "250": {
    "id": "250",
    "name": "Huyện Lắk",
    "code": "656",
    "parent_id": "16",
    "slug": "huyen lak"
  },
  "251": {
    "id": "251",
    "name": "Huyện M'Đrắk",
    "code": "652",
    "parent_id": "16",
    "slug": "huyen mdrak"
  },
  "252": {
    "id": "252",
    "name": "Thành phố Buôn Ma Thuột",
    "code": "643",
    "parent_id": "16",
    "slug": "thanh pho buon ma thuot"
  },
  "253": {
    "id": "253",
    "name": "Thị Xã Buôn Hồ",
    "code": "644",
    "parent_id": "16",
    "slug": "thi xa buon ho"
  },
  "254": {
    "id": "254",
    "name": "Huyện Cư Jút",
    "code": "662",
    "parent_id": "17",
    "slug": "huyen cu jut"
  },
  "255": {
    "id": "255",
    "name": "Huyện Đăk Glong",
    "code": "661",
    "parent_id": "17",
    "slug": "huyen dak glong"
  },
  "256": {
    "id": "256",
    "name": "Huyện Đắk Mil",
    "code": "663",
    "parent_id": "17",
    "slug": "huyen dak mil"
  },
  "257": {
    "id": "257",
    "name": "Huyện Đắk R'Lấp",
    "code": "666",
    "parent_id": "17",
    "slug": "huyen dak rlap"
  },
  "258": {
    "id": "258",
    "name": "Huyện Đắk Song",
    "code": "665",
    "parent_id": "17",
    "slug": "huyen dak song"
  },
  "259": {
    "id": "259",
    "name": "Huyện Krông Nô",
    "code": "664",
    "parent_id": "17",
    "slug": "huyen krong no"
  },
  "260": {
    "id": "260",
    "name": "Huyện Tuy Đức",
    "code": "667",
    "parent_id": "17",
    "slug": "huyen tuy duc"
  },
  "261": {
    "id": "261",
    "name": "Thị xã Gia Nghĩa",
    "code": "660",
    "parent_id": "17",
    "slug": "thi xa gia nghia"
  },
  "262": {
    "id": "262",
    "name": "Huyện Điện Biên",
    "code": "100",
    "parent_id": "18",
    "slug": "huyen dien bien"
  },
  "263": {
    "id": "263",
    "name": "Huyện Điện Biên Đông",
    "code": "101",
    "parent_id": "18",
    "slug": "huyen dien bien dong"
  },
  "264": {
    "id": "264",
    "name": "Huyện Mường Ảng",
    "code": "102",
    "parent_id": "18",
    "slug": "huyen muong ang"
  },
  "265": {
    "id": "265",
    "name": "Huyện Mường Chà",
    "code": "097",
    "parent_id": "18",
    "slug": "huyen muong cha"
  },
  "266": {
    "id": "266",
    "name": "Huyện Mường Nhé",
    "code": "096",
    "parent_id": "18",
    "slug": "huyen muong nhe"
  },
  "267": {
    "id": "267",
    "name": "Huyện Nậm Pồ",
    "code": "103",
    "parent_id": "18",
    "slug": "huyen nam po"
  },
  "268": {
    "id": "268",
    "name": "Huyện Tủa Chùa",
    "code": "098",
    "parent_id": "18",
    "slug": "huyen tua chua"
  },
  "269": {
    "id": "269",
    "name": "Huyện Tuần Giáo",
    "code": "099",
    "parent_id": "18",
    "slug": "huyen tuan giao"
  },
  "270": {
    "id": "270",
    "name": "Thành phố Điện Biên Phủ",
    "code": "094",
    "parent_id": "18",
    "slug": "thanh pho dien bien phu"
  },
  "271": {
    "id": "271",
    "name": "Thị Xã Mường Lay",
    "code": "095",
    "parent_id": "18",
    "slug": "thi xa muong lay"
  },
  "272": {
    "id": "272",
    "name": "Huyện Cẩm Mỹ",
    "code": "739",
    "parent_id": "19",
    "slug": "huyen cam my"
  },
  "273": {
    "id": "273",
    "name": "Huyện Định Quán",
    "code": "736",
    "parent_id": "19",
    "slug": "huyen dinh quan"
  },
  "274": {
    "id": "274",
    "name": "Huyện Long Thành",
    "code": "740",
    "parent_id": "19",
    "slug": "huyen long thanh"
  },
  "275": {
    "id": "275",
    "name": "Huyện Nhơn Trạch",
    "code": "742",
    "parent_id": "19",
    "slug": "huyen nhon trach"
  },
  "276": {
    "id": "276",
    "name": "Huyện Tân Phú",
    "code": "734",
    "parent_id": "19",
    "slug": "huyen tan phu"
  },
  "277": {
    "id": "277",
    "name": "Huyện Thống Nhất",
    "code": "738",
    "parent_id": "19",
    "slug": "huyen thong nhat"
  },
  "278": {
    "id": "278",
    "name": "Huyện Trảng Bom",
    "code": "737",
    "parent_id": "19",
    "slug": "huyen trang bom"
  },
  "279": {
    "id": "279",
    "name": "Huyện Vĩnh Cửu",
    "code": "735",
    "parent_id": "19",
    "slug": "huyen vinh cuu"
  },
  "280": {
    "id": "280",
    "name": "Huyện Xuân Lộc",
    "code": "741",
    "parent_id": "19",
    "slug": "huyen xuan loc"
  },
  "281": {
    "id": "281",
    "name": "Thành phố Biên Hòa",
    "code": "731",
    "parent_id": "19",
    "slug": "thanh pho bien hoa"
  },
  "282": {
    "id": "282",
    "name": "Thị xã Long Khánh",
    "code": "732",
    "parent_id": "19",
    "slug": "thi xa long khanh"
  },
  "283": {
    "id": "283",
    "name": "Huyện Cao Lãnh",
    "code": "873",
    "parent_id": "20",
    "slug": "huyen cao lanh"
  },
  "284": {
    "id": "284",
    "name": "Huyện Châu Thành",
    "code": "877",
    "parent_id": "20",
    "slug": "huyen chau thanh"
  },
  "285": {
    "id": "285",
    "name": "Huyện Hồng Ngự",
    "code": "870",
    "parent_id": "20",
    "slug": "huyen hong ngu"
  },
  "286": {
    "id": "286",
    "name": "Huyện Lai Vung",
    "code": "876",
    "parent_id": "20",
    "slug": "huyen lai vung"
  },
  "287": {
    "id": "287",
    "name": "Huyện Lấp Vò",
    "code": "875",
    "parent_id": "20",
    "slug": "huyen lap vo"
  },
  "288": {
    "id": "288",
    "name": "Huyện Tam Nông",
    "code": "871",
    "parent_id": "20",
    "slug": "huyen tam nong"
  },
  "289": {
    "id": "289",
    "name": "Huyện Tân Hồng",
    "code": "869",
    "parent_id": "20",
    "slug": "huyen tan hong"
  },
  "290": {
    "id": "290",
    "name": "Huyện Thanh Bình",
    "code": "874",
    "parent_id": "20",
    "slug": "huyen thanh binh"
  },
  "291": {
    "id": "291",
    "name": "Huyện Tháp Mười",
    "code": "872",
    "parent_id": "20",
    "slug": "huyen thap muoi"
  },
  "292": {
    "id": "292",
    "name": "Thành phố Cao Lãnh",
    "code": "866",
    "parent_id": "20",
    "slug": "thanh pho cao lanh"
  },
  "293": {
    "id": "293",
    "name": "Thành phố Sa Đéc",
    "code": "867",
    "parent_id": "20",
    "slug": "thanh pho sa dec"
  },
  "294": {
    "id": "294",
    "name": "Thị xã Hồng Ngự",
    "code": "868",
    "parent_id": "20",
    "slug": "thi xa hong ngu"
  },
  "295": {
    "id": "295",
    "name": "Huyện Chư Păh",
    "code": "627",
    "parent_id": "21",
    "slug": "huyen chu pah"
  },
  "296": {
    "id": "296",
    "name": "Huyện Chư Prông",
    "code": "632",
    "parent_id": "21",
    "slug": "huyen chu prong"
  },
  "297": {
    "id": "297",
    "name": "Huyện Chư Pưh",
    "code": "639",
    "parent_id": "21",
    "slug": "huyen chu puh"
  },
  "298": {
    "id": "298",
    "name": "Huyện Chư Sê",
    "code": "633",
    "parent_id": "21",
    "slug": "huyen chu se"
  },
  "299": {
    "id": "299",
    "name": "Huyện Đăk Đoa",
    "code": "626",
    "parent_id": "21",
    "slug": "huyen dak doa"
  },
  "300": {
    "id": "300",
    "name": "Huyện Đăk Pơ",
    "code": "634",
    "parent_id": "21",
    "slug": "huyen dak po"
  },
  "301": {
    "id": "301",
    "name": "Huyện Đức Cơ",
    "code": "631",
    "parent_id": "21",
    "slug": "huyen duc co"
  },
  "302": {
    "id": "302",
    "name": "Huyện Ia Grai",
    "code": "628",
    "parent_id": "21",
    "slug": "huyen ia grai"
  },
  "303": {
    "id": "303",
    "name": "Huyện Ia Pa",
    "code": "635",
    "parent_id": "21",
    "slug": "huyen ia pa"
  },
  "304": {
    "id": "304",
    "name": "Huyện KBang",
    "code": "625",
    "parent_id": "21",
    "slug": "huyen kbang"
  },
  "305": {
    "id": "305",
    "name": "Huyện Kông Chro",
    "code": "630",
    "parent_id": "21",
    "slug": "huyen kong chro"
  },
  "306": {
    "id": "306",
    "name": "Huyện Krông Pa",
    "code": "637",
    "parent_id": "21",
    "slug": "huyen krong pa"
  },
  "307": {
    "id": "307",
    "name": "Huyện Mang Yang",
    "code": "629",
    "parent_id": "21",
    "slug": "huyen mang yang"
  },
  "308": {
    "id": "308",
    "name": "Huyện Phú Thiện",
    "code": "638",
    "parent_id": "21",
    "slug": "huyen phu thien"
  },
  "309": {
    "id": "309",
    "name": "Thành phố Pleiku",
    "code": "622",
    "parent_id": "21",
    "slug": "thanh pho pleiku"
  },
  "310": {
    "id": "310",
    "name": "Thị xã An Khê",
    "code": "623",
    "parent_id": "21",
    "slug": "thi xa an khe"
  },
  "311": {
    "id": "311",
    "name": "Thị xã Ayun Pa",
    "code": "624",
    "parent_id": "21",
    "slug": "thi xa ayun pa"
  },
  "312": {
    "id": "312",
    "name": "Huyện Bắc Mê",
    "code": "031",
    "parent_id": "22",
    "slug": "huyen bac me"
  },
  "313": {
    "id": "313",
    "name": "Huyện Bắc Quang",
    "code": "034",
    "parent_id": "22",
    "slug": "huyen bac quang"
  },
  "314": {
    "id": "314",
    "name": "Huyện Đồng Văn",
    "code": "026",
    "parent_id": "22",
    "slug": "huyen dong van"
  },
  "315": {
    "id": "315",
    "name": "Huyện Hoàng Su Phì",
    "code": "032",
    "parent_id": "22",
    "slug": "huyen hoang su phi"
  },
  "316": {
    "id": "316",
    "name": "Huyện Mèo Vạc",
    "code": "027",
    "parent_id": "22",
    "slug": "huyen meo vac"
  },
  "317": {
    "id": "317",
    "name": "Huyện Quản Bạ",
    "code": "029",
    "parent_id": "22",
    "slug": "huyen quan ba"
  },
  "318": {
    "id": "318",
    "name": "Huyện Quang Bình",
    "code": "035",
    "parent_id": "22",
    "slug": "huyen quang binh"
  },
  "319": {
    "id": "319",
    "name": "Huyện Vị Xuyên",
    "code": "030",
    "parent_id": "22",
    "slug": "huyen vi xuyen"
  },
  "320": {
    "id": "320",
    "name": "Huyện Xín Mần",
    "code": "033",
    "parent_id": "22",
    "slug": "huyen xin man"
  },
  "321": {
    "id": "321",
    "name": "Huyện Yên Minh",
    "code": "028",
    "parent_id": "22",
    "slug": "huyen yen minh"
  },
  "322": {
    "id": "322",
    "name": "Thành phố Hà Giang",
    "code": "024",
    "parent_id": "22",
    "slug": "thanh pho ha giang"
  },
  "323": {
    "id": "323",
    "name": "Huyện Bình Lục",
    "code": "352",
    "parent_id": "23",
    "slug": "huyen binh luc"
  },
  "324": {
    "id": "324",
    "name": "Huyện Duy Tiên",
    "code": "349",
    "parent_id": "23",
    "slug": "huyen duy tien"
  },
  "325": {
    "id": "325",
    "name": "Huyện Kim Bảng",
    "code": "350",
    "parent_id": "23",
    "slug": "huyen kim bang"
  },
  "326": {
    "id": "326",
    "name": "Huyện Lý Nhân",
    "code": "353",
    "parent_id": "23",
    "slug": "huyen ly nhan"
  },
  "327": {
    "id": "327",
    "name": "Huyện Thanh Liêm",
    "code": "351",
    "parent_id": "23",
    "slug": "huyen thanh liem"
  },
  "328": {
    "id": "328",
    "name": "Thành phố Phủ Lý",
    "code": "347",
    "parent_id": "23",
    "slug": "thanh pho phu ly"
  },
  "329": {
    "id": "329",
    "name": "Huyện Ba Vì",
    "code": "271",
    "parent_id": "24",
    "slug": "huyen ba vi"
  },
  "330": {
    "id": "330",
    "name": "Huyện Chương Mỹ",
    "code": "277",
    "parent_id": "24",
    "slug": "huyen chuong my"
  },
  "331": {
    "id": "331",
    "name": "Huyện Đan Phượng",
    "code": "273",
    "parent_id": "24",
    "slug": "huyen dan phuong"
  },
  "332": {
    "id": "332",
    "name": "Huyện Đông Anh",
    "code": "017",
    "parent_id": "24",
    "slug": "huyen dong anh"
  },
  "333": {
    "id": "333",
    "name": "Huyện Gia Lâm",
    "code": "018",
    "parent_id": "24",
    "slug": "huyen gia lam"
  },
  "334": {
    "id": "334",
    "name": "Huyện Hoài Đức",
    "code": "274",
    "parent_id": "24",
    "slug": "huyen hoai duc"
  },
  "335": {
    "id": "335",
    "name": "Huyện Mê Linh",
    "code": "250",
    "parent_id": "24",
    "slug": "huyen me linh"
  },
  "336": {
    "id": "336",
    "name": "Huyện Mỹ Đức",
    "code": "282",
    "parent_id": "24",
    "slug": "huyen my duc"
  },
  "337": {
    "id": "337",
    "name": "Huyện Phú Xuyên",
    "code": "280",
    "parent_id": "24",
    "slug": "huyen phu xuyen"
  },
  "338": {
    "id": "338",
    "name": "Huyện Phúc Thọ",
    "code": "272",
    "parent_id": "24",
    "slug": "huyen phuc tho"
  },
  "339": {
    "id": "339",
    "name": "Huyện Quốc Oai",
    "code": "275",
    "parent_id": "24",
    "slug": "huyen quoc oai"
  },
  "340": {
    "id": "340",
    "name": "Huyện Sóc Sơn",
    "code": "016",
    "parent_id": "24",
    "slug": "huyen soc son"
  },
  "341": {
    "id": "341",
    "name": "Huyện Thạch Thất",
    "code": "276",
    "parent_id": "24",
    "slug": "huyen thach that"
  },
  "342": {
    "id": "342",
    "name": "Huyện Thanh Oai",
    "code": "278",
    "parent_id": "24",
    "slug": "huyen thanh oai"
  },
  "343": {
    "id": "343",
    "name": "Huyện Thanh Trì",
    "code": "020",
    "parent_id": "24",
    "slug": "huyen thanh tri"
  },
  "344": {
    "id": "344",
    "name": "Huyện Thường Tín",
    "code": "279",
    "parent_id": "24",
    "slug": "huyen thuong tin"
  },
  "345": {
    "id": "345",
    "name": "Huyện Ứng Hòa",
    "code": "281",
    "parent_id": "24",
    "slug": "huyen ung hoa"
  },
  "346": {
    "id": "346",
    "name": "Quận Ba Đình",
    "code": "001",
    "parent_id": "24",
    "slug": "quan ba dinh"
  },
  "347": {
    "id": "347",
    "name": "Quận Bắc Từ Liêm",
    "code": "021",
    "parent_id": "24",
    "slug": "quan bac tu liem"
  },
  "348": {
    "id": "348",
    "name": "Quận Cầu Giấy",
    "code": "005",
    "parent_id": "24",
    "slug": "quan cau giay"
  },
  "349": {
    "id": "349",
    "name": "Quận Đống Đa",
    "code": "006",
    "parent_id": "24",
    "slug": "quan dong da"
  },
  "350": {
    "id": "350",
    "name": "Quận Hà Đông",
    "code": "268",
    "parent_id": "24",
    "slug": "quan ha dong"
  },
  "351": {
    "id": "351",
    "name": "Quận Hai Bà Trưng",
    "code": "007",
    "parent_id": "24",
    "slug": "quan hai ba trung"
  },
  "352": {
    "id": "352",
    "name": "Quận Hoàn Kiếm",
    "code": "002",
    "parent_id": "24",
    "slug": "quan hoan kiem"
  },
  "353": {
    "id": "353",
    "name": "Quận Hoàng Mai",
    "code": "008",
    "parent_id": "24",
    "slug": "quan hoang mai"
  },
  "354": {
    "id": "354",
    "name": "Quận Long Biên",
    "code": "004",
    "parent_id": "24",
    "slug": "quan long bien"
  },
  "355": {
    "id": "355",
    "name": "Quận Nam Từ Liêm",
    "code": "019",
    "parent_id": "24",
    "slug": "quan nam tu liem"
  },
  "356": {
    "id": "356",
    "name": "Quận Tây Hồ",
    "code": "003",
    "parent_id": "24",
    "slug": "quan tay ho"
  },
  "357": {
    "id": "357",
    "name": "Quận Thanh Xuân",
    "code": "009",
    "parent_id": "24",
    "slug": "quan thanh xuan"
  },
  "358": {
    "id": "358",
    "name": "Thị xã Sơn Tây",
    "code": "269",
    "parent_id": "24",
    "slug": "thi xa son tay"
  },
  "359": {
    "id": "359",
    "name": "Huyện Cẩm Xuyên",
    "code": "446",
    "parent_id": "25",
    "slug": "huyen cam xuyen"
  },
  "360": {
    "id": "360",
    "name": "Huyện Can Lộc",
    "code": "443",
    "parent_id": "25",
    "slug": "huyen can loc"
  },
  "361": {
    "id": "361",
    "name": "Huyện Đức Thọ",
    "code": "440",
    "parent_id": "25",
    "slug": "huyen duc tho"
  },
  "362": {
    "id": "362",
    "name": "Huyện Hương Khê",
    "code": "444",
    "parent_id": "25",
    "slug": "huyen huong khe"
  },
  "363": {
    "id": "363",
    "name": "Huyện Hương Sơn",
    "code": "439",
    "parent_id": "25",
    "slug": "huyen huong son"
  },
  "364": {
    "id": "364",
    "name": "Huyện Kỳ Anh",
    "code": "447",
    "parent_id": "25",
    "slug": "huyen ky anh"
  },
  "365": {
    "id": "365",
    "name": "Huyện Lộc Hà",
    "code": "448",
    "parent_id": "25",
    "slug": "huyen loc ha"
  },
  "366": {
    "id": "366",
    "name": "Huyện Nghi Xuân",
    "code": "442",
    "parent_id": "25",
    "slug": "huyen nghi xuan"
  },
  "367": {
    "id": "367",
    "name": "Huyện Thạch Hà",
    "code": "445",
    "parent_id": "25",
    "slug": "huyen thach ha"
  },
  "368": {
    "id": "368",
    "name": "Huyện Vũ Quang",
    "code": "441",
    "parent_id": "25",
    "slug": "huyen vu quang"
  },
  "369": {
    "id": "369",
    "name": "Thành phố Hà Tĩnh",
    "code": "436",
    "parent_id": "25",
    "slug": "thanh pho ha tinh"
  },
  "370": {
    "id": "370",
    "name": "Thị xã Hồng Lĩnh",
    "code": "437",
    "parent_id": "25",
    "slug": "thi xa hong linh"
  },
  "371": {
    "id": "371",
    "name": "Thị xã Kỳ Anh",
    "code": "449",
    "parent_id": "25",
    "slug": "thi xa ky anh"
  },
  "372": {
    "id": "372",
    "name": "Huyện Bình Giang",
    "code": "296",
    "parent_id": "26",
    "slug": "huyen binh giang"
  },
  "373": {
    "id": "373",
    "name": "Huyện Cẩm Giàng",
    "code": "295",
    "parent_id": "26",
    "slug": "huyen cam giang"
  },
  "374": {
    "id": "374",
    "name": "Huyện Gia Lộc",
    "code": "297",
    "parent_id": "26",
    "slug": "huyen gia loc"
  },
  "375": {
    "id": "375",
    "name": "Huyện Kim Thành",
    "code": "293",
    "parent_id": "26",
    "slug": "huyen kim thanh"
  },
  "376": {
    "id": "376",
    "name": "Huyện Kinh Môn",
    "code": "292",
    "parent_id": "26",
    "slug": "huyen kinh mon"
  },
  "377": {
    "id": "377",
    "name": "Huyện Nam Sách",
    "code": "291",
    "parent_id": "26",
    "slug": "huyen nam sach"
  },
  "378": {
    "id": "378",
    "name": "Huyện Ninh Giang",
    "code": "299",
    "parent_id": "26",
    "slug": "huyen ninh giang"
  },
  "379": {
    "id": "379",
    "name": "Huyện Thanh Hà",
    "code": "294",
    "parent_id": "26",
    "slug": "huyen thanh ha"
  },
  "380": {
    "id": "380",
    "name": "Huyện Thanh Miện",
    "code": "300",
    "parent_id": "26",
    "slug": "huyen thanh mien"
  },
  "381": {
    "id": "381",
    "name": "Huyện Tứ Kỳ",
    "code": "298",
    "parent_id": "26",
    "slug": "huyen tu ky"
  },
  "382": {
    "id": "382",
    "name": "Thành phố Hải Dương",
    "code": "288",
    "parent_id": "26",
    "slug": "thanh pho hai duong"
  },
  "383": {
    "id": "383",
    "name": "Thị xã Chí Linh",
    "code": "290",
    "parent_id": "26",
    "slug": "thi xa chi linh"
  },
  "384": {
    "id": "384",
    "name": "Huyện An Dương",
    "code": "312",
    "parent_id": "27",
    "slug": "huyen an duong"
  },
  "385": {
    "id": "385",
    "name": "Huyện An Lão",
    "code": "313",
    "parent_id": "27",
    "slug": "huyen an lao"
  },
  "386": {
    "id": "386",
    "name": "Huyện Cát Hải",
    "code": "317",
    "parent_id": "27",
    "slug": "huyen cat hai"
  },
  "387": {
    "id": "387",
    "name": "Huyện Kiến Thuỵ",
    "code": "314",
    "parent_id": "27",
    "slug": "huyen kien thuy"
  },
  "388": {
    "id": "388",
    "name": "Huyện Thuỷ Nguyên",
    "code": "311",
    "parent_id": "27",
    "slug": "huyen thuy nguyen"
  },
  "389": {
    "id": "389",
    "name": "Huyện Tiên Lãng",
    "code": "315",
    "parent_id": "27",
    "slug": "huyen tien lang"
  },
  "390": {
    "id": "390",
    "name": "Huyện Vĩnh Bảo",
    "code": "316",
    "parent_id": "27",
    "slug": "huyen vinh bao"
  },
  "391": {
    "id": "391",
    "name": "Quận Đồ Sơn",
    "code": "308",
    "parent_id": "27",
    "slug": "quan do son"
  },
  "392": {
    "id": "392",
    "name": "Quận Dương Kinh",
    "code": "309",
    "parent_id": "27",
    "slug": "quan duong kinh"
  },
  "393": {
    "id": "393",
    "name": "Quận Hải An",
    "code": "306",
    "parent_id": "27",
    "slug": "quan hai an"
  },
  "394": {
    "id": "394",
    "name": "Quận Hồng Bàng",
    "code": "303",
    "parent_id": "27",
    "slug": "quan hong bang"
  },
  "395": {
    "id": "395",
    "name": "Quận Kiến An",
    "code": "307",
    "parent_id": "27",
    "slug": "quan kien an"
  },
  "396": {
    "id": "396",
    "name": "Quận Lê Chân",
    "code": "305",
    "parent_id": "27",
    "slug": "quan le chan"
  },
  "397": {
    "id": "397",
    "name": "Quáº­n Ngô Quyền",
    "code": "304",
    "parent_id": "27",
    "slug": "quaº­n ngo quyen"
  },
  "398": {
    "id": "398",
    "name": "Huyện Châu Thành",
    "code": "933",
    "parent_id": "28",
    "slug": "huyen chau thanh"
  },
  "399": {
    "id": "399",
    "name": "Huyện Châu Thành A",
    "code": "932",
    "parent_id": "28",
    "slug": "huyen chau thanh a"
  },
  "400": {
    "id": "400",
    "name": "Huyện Long Mỹ",
    "code": "936",
    "parent_id": "28",
    "slug": "huyen long my"
  },
  "401": {
    "id": "401",
    "name": "Huyện Phụng Hiệp",
    "code": "934",
    "parent_id": "28",
    "slug": "huyen phung hiep"
  },
  "402": {
    "id": "402",
    "name": "Huyện Vị Thuỷ",
    "code": "935",
    "parent_id": "28",
    "slug": "huyen vi thuy"
  },
  "403": {
    "id": "403",
    "name": "Thành phố Vị Thanh",
    "code": "930",
    "parent_id": "28",
    "slug": "thanh pho vi thanh"
  },
  "404": {
    "id": "404",
    "name": "Thị xã Long Mỹ",
    "code": "937",
    "parent_id": "28",
    "slug": "thi xa long my"
  },
  "405": {
    "id": "405",
    "name": "Thị xã Ngã Bảy",
    "code": "931",
    "parent_id": "28",
    "slug": "thi xa nga bay"
  },
  "406": {
    "id": "406",
    "name": "Huyện Cao Phong",
    "code": "154",
    "parent_id": "29",
    "slug": "huyen cao phong"
  },
  "407": {
    "id": "407",
    "name": "Huyện Đà Bắc",
    "code": "150",
    "parent_id": "29",
    "slug": "huyen da bac"
  },
  "408": {
    "id": "408",
    "name": "Huyện Kim Bôi",
    "code": "153",
    "parent_id": "29",
    "slug": "huyen kim boi"
  },
  "409": {
    "id": "409",
    "name": "Huyện Kỳ Sơn",
    "code": "151",
    "parent_id": "29",
    "slug": "huyen ky son"
  },
  "410": {
    "id": "410",
    "name": "Huyện Lạc Sơn",
    "code": "157",
    "parent_id": "29",
    "slug": "huyen lac son"
  },
  "411": {
    "id": "411",
    "name": "Huyện Lạc Thủy",
    "code": "159",
    "parent_id": "29",
    "slug": "huyen lac thuy"
  },
  "412": {
    "id": "412",
    "name": "Huyện Lương Sơn",
    "code": "152",
    "parent_id": "29",
    "slug": "huyen luong son"
  },
  "413": {
    "id": "413",
    "name": "Huyện Mai Châu",
    "code": "156",
    "parent_id": "29",
    "slug": "huyen mai chau"
  },
  "414": {
    "id": "414",
    "name": "Huyện Tân Lạc",
    "code": "155",
    "parent_id": "29",
    "slug": "huyen tan lac"
  },
  "415": {
    "id": "415",
    "name": "Huyện Yên Thủy",
    "code": "158",
    "parent_id": "29",
    "slug": "huyen yen thuy"
  },
  "416": {
    "id": "416",
    "name": "Thành phố Hòa Bình",
    "code": "148",
    "parent_id": "29",
    "slug": "thanh pho hoa binh"
  },
  "417": {
    "id": "417",
    "name": "Quận 1",
    "code": "760",
    "parent_id": "30",
    "slug": "quan 1"
  },
  "418": {
    "id": "418",
    "name": "Quận 2",
    "code": "769",
    "parent_id": "30",
    "slug": "quan 2"
  },
  "419": {
    "id": "419",
    "name": "Quận 3",
    "code": "770",
    "parent_id": "30",
    "slug": "quan 3"
  },
  "420": {
    "id": "420",
    "name": "Quận 4",
    "code": "773",
    "parent_id": "30",
    "slug": "quan 4"
  },
  "421": {
    "id": "421",
    "name": "Quận 5",
    "code": "774",
    "parent_id": "30",
    "slug": "quan 5"
  },
  "422": {
    "id": "422",
    "name": "Quận 6",
    "code": "775",
    "parent_id": "30",
    "slug": "quan 6"
  },
  "423": {
    "id": "423",
    "name": "Quận 7",
    "code": "778",
    "parent_id": "30",
    "slug": "quan 7"
  },
  "424": {
    "id": "424",
    "name": "Quận 8",
    "code": "776",
    "parent_id": "30",
    "slug": "quan 8"
  },
  "425": {
    "id": "425",
    "name": "Quận 9",
    "code": "763",
    "parent_id": "30",
    "slug": "quan 9"
  },
  "426": {
    "id": "426",
    "name": "Quận 10",
    "code": "771",
    "parent_id": "30",
    "slug": "quan 10"
  },
  "427": {
    "id": "427",
    "name": "Quận 11",
    "code": "772",
    "parent_id": "30",
    "slug": "quan 11"
  },
  "428": {
    "id": "428",
    "name": "Quận 12",
    "code": "761",
    "parent_id": "30",
    "slug": "quan 12"
  },
  "429": {
    "id": "429",
    "name": "Quận Bình Tân",
    "code": "777",
    "parent_id": "30",
    "slug": "quan binh tan"
  },
  "430": {
    "id": "430",
    "name": "Quận Bình Thạnh",
    "code": "765",
    "parent_id": "30",
    "slug": "quan binh thanh"
  },
  "431": {
    "id": "431",
    "name": "Quận Gò Vấp",
    "code": "764",
    "parent_id": "30",
    "slug": "quan go vap"
  },
  "432": {
    "id": "432",
    "name": "Quận Phú Nhuận",
    "code": "768",
    "parent_id": "30",
    "slug": "quan phu nhuan"
  },
  "433": {
    "id": "433",
    "name": "Quận Tân Bình",
    "code": "766",
    "parent_id": "30",
    "slug": "quan tan binh"
  },
  "434": {
    "id": "434",
    "name": "Quận Tân Phú",
    "code": "767",
    "parent_id": "30",
    "slug": "quan tan phu"
  },
  "435": {
    "id": "435",
    "name": "Quận Thủ Đức",
    "code": "762",
    "parent_id": "30",
    "slug": "quan thu duc"
  },
  "436": {
    "id": "436",
    "name": "Huyện Bình Chánh",
    "code": "785",
    "parent_id": "30",
    "slug": "huyen binh chanh"
  },
  "437": {
    "id": "437",
    "name": "Huyện Cần Giờ",
    "code": "787",
    "parent_id": "30",
    "slug": "huyen can gio"
  },
  "438": {
    "id": "438",
    "name": "Huyện Củ Chi",
    "code": "783",
    "parent_id": "30",
    "slug": "huyen cu chi"
  },
  "439": {
    "id": "439",
    "name": "Huyện Hóc Môn",
    "code": "784",
    "parent_id": "30",
    "slug": "huyen hoc mon"
  },
  "440": {
    "id": "440",
    "name": "Huyện Nhà Bè",
    "code": "786",
    "parent_id": "30",
    "slug": "huyen nha be"
  },
  "441": {
    "id": "441",
    "name": "Huyện Ân Thi",
    "code": "329",
    "parent_id": "31",
    "slug": "huyen an thi"
  },
  "442": {
    "id": "442",
    "name": "Huyện Khoái Châu",
    "code": "330",
    "parent_id": "31",
    "slug": "huyen khoai chau"
  },
  "443": {
    "id": "443",
    "name": "Huyện Kim Động",
    "code": "331",
    "parent_id": "31",
    "slug": "huyen kim dong"
  },
  "444": {
    "id": "444",
    "name": "Huyện Mỹ Hào",
    "code": "328",
    "parent_id": "31",
    "slug": "huyen my hao"
  },
  "445": {
    "id": "445",
    "name": "Huyện Phù Cừ",
    "code": "333",
    "parent_id": "31",
    "slug": "huyen phu cu"
  },
  "446": {
    "id": "446",
    "name": "Huyện Tiên Lữ",
    "code": "332",
    "parent_id": "31",
    "slug": "huyen tien lu"
  },
  "447": {
    "id": "447",
    "name": "Huyện Văn Giang",
    "code": "326",
    "parent_id": "31",
    "slug": "huyen van giang"
  },
  "448": {
    "id": "448",
    "name": "Huyện Văn Lâm",
    "code": "325",
    "parent_id": "31",
    "slug": "huyen van lam"
  },
  "449": {
    "id": "449",
    "name": "Huyện Yên Mỹ",
    "code": "327",
    "parent_id": "31",
    "slug": "huyen yen my"
  },
  "450": {
    "id": "450",
    "name": "Thành phố Hưng Yên",
    "code": "323",
    "parent_id": "31",
    "slug": "thanh pho hung yen"
  },
  "451": {
    "id": "451",
    "name": "Huyện Cam Lâm",
    "code": "570",
    "parent_id": "32",
    "slug": "huyen cam lam"
  },
  "452": {
    "id": "452",
    "name": "Huyện Diên Khánh",
    "code": "574",
    "parent_id": "32",
    "slug": "huyen dien khanh"
  },
  "453": {
    "id": "453",
    "name": "Huyện Khánh Sơn",
    "code": "575",
    "parent_id": "32",
    "slug": "huyen khanh son"
  },
  "454": {
    "id": "454",
    "name": "Huyện Khánh Vĩnh",
    "code": "573",
    "parent_id": "32",
    "slug": "huyen khanh vinh"
  },
  "455": {
    "id": "455",
    "name": "Huyện Trường Sa",
    "code": "576",
    "parent_id": "32",
    "slug": "huyen truong sa"
  },
  "456": {
    "id": "456",
    "name": "Huyện Vạn Ninh",
    "code": "571",
    "parent_id": "32",
    "slug": "huyen van ninh"
  },
  "457": {
    "id": "457",
    "name": "Thành phố Cam Ranh",
    "code": "569",
    "parent_id": "32",
    "slug": "thanh pho cam ranh"
  },
  "458": {
    "id": "458",
    "name": "Thành phố Nha Trang",
    "code": "568",
    "parent_id": "32",
    "slug": "thanh pho nha trang"
  },
  "459": {
    "id": "459",
    "name": "Thị xã Ninh Hòa",
    "code": "572",
    "parent_id": "32",
    "slug": "thi xa ninh hoa"
  },
  "460": {
    "id": "460",
    "name": "Huyện An Biên",
    "code": "908",
    "parent_id": "33",
    "slug": "huyen an bien"
  },
  "461": {
    "id": "461",
    "name": "Huyện An Minh",
    "code": "909",
    "parent_id": "33",
    "slug": "huyen an minh"
  },
  "462": {
    "id": "462",
    "name": "Huyện Châu Thành",
    "code": "905",
    "parent_id": "33",
    "slug": "huyen chau thanh"
  },
  "463": {
    "id": "463",
    "name": "Huyện Giang Thành",
    "code": "914",
    "parent_id": "33",
    "slug": "huyen giang thanh"
  },
  "464": {
    "id": "464",
    "name": "Huyện Giồng Riềng",
    "code": "906",
    "parent_id": "33",
    "slug": "huyen giong rieng"
  },
  "465": {
    "id": "465",
    "name": "Huyện Gò Quao",
    "code": "907",
    "parent_id": "33",
    "slug": "huyen go quao"
  },
  "466": {
    "id": "466",
    "name": "Huyện Hòn Đất",
    "code": "903",
    "parent_id": "33",
    "slug": "huyen hon dat"
  },
  "467": {
    "id": "467",
    "name": "Huyện Kiên Hải",
    "code": "912",
    "parent_id": "33",
    "slug": "huyen kien hai"
  },
  "468": {
    "id": "468",
    "name": "Huyện Kiên Lương",
    "code": "902",
    "parent_id": "33",
    "slug": "huyen kien luong"
  },
  "469": {
    "id": "469",
    "name": "Huyện Phú Quốc",
    "code": "911",
    "parent_id": "33",
    "slug": "huyen phu quoc"
  },
  "470": {
    "id": "470",
    "name": "Huyện Tân Hiệp",
    "code": "904",
    "parent_id": "33",
    "slug": "huyen tan hiep"
  },
  "471": {
    "id": "471",
    "name": "Huyện U Minh Thượng",
    "code": "913",
    "parent_id": "33",
    "slug": "huyen u minh thuong"
  },
  "472": {
    "id": "472",
    "name": "Huyện Vĩnh Thuận",
    "code": "910",
    "parent_id": "33",
    "slug": "huyen vinh thuan"
  },
  "473": {
    "id": "473",
    "name": "Thành phố Rạch Giá",
    "code": "899",
    "parent_id": "33",
    "slug": "thanh pho rach gia"
  },
  "474": {
    "id": "474",
    "name": "Thị xã Hà Tiên",
    "code": "900",
    "parent_id": "33",
    "slug": "thi xa ha tien"
  },
  "475": {
    "id": "475",
    "name": "Huyện Đắk Glei",
    "code": "610",
    "parent_id": "34",
    "slug": "huyen dak glei"
  },
  "476": {
    "id": "476",
    "name": "Huyện Đắk Hà",
    "code": "615",
    "parent_id": "34",
    "slug": "huyen dak ha"
  },
  "477": {
    "id": "477",
    "name": "Huyện Đắk Tô",
    "code": "612",
    "parent_id": "34",
    "slug": "huyen dak to"
  },
  "478": {
    "id": "478",
    "name": "Huyện Ia H' Drai",
    "code": "618",
    "parent_id": "34",
    "slug": "huyen ia h drai"
  },
  "479": {
    "id": "479",
    "name": "Huyện Kon Plông",
    "code": "613",
    "parent_id": "34",
    "slug": "huyen kon plong"
  },
  "480": {
    "id": "480",
    "name": "Huyện Kon Rẫy",
    "code": "614",
    "parent_id": "34",
    "slug": "huyen kon ray"
  },
  "481": {
    "id": "481",
    "name": "Huyện Ngọc Hồi",
    "code": "611",
    "parent_id": "34",
    "slug": "huyen ngoc hoi"
  },
  "482": {
    "id": "482",
    "name": "Huyện Sa Thầy",
    "code": "616",
    "parent_id": "34",
    "slug": "huyen sa thay"
  },
  "483": {
    "id": "483",
    "name": "Huyện Tu Mơ Rông",
    "code": "617",
    "parent_id": "34",
    "slug": "huyen tu mo rong"
  },
  "484": {
    "id": "484",
    "name": "Thành phố Kon Tum",
    "code": "608",
    "parent_id": "34",
    "slug": "thanh pho kon tum"
  },
  "485": {
    "id": "485",
    "name": "Huyện Mường Tè",
    "code": "107",
    "parent_id": "35",
    "slug": "huyen muong te"
  },
  "486": {
    "id": "486",
    "name": "Huyện Nậm Nhùn",
    "code": "112",
    "parent_id": "35",
    "slug": "huyen nam nhun"
  },
  "487": {
    "id": "487",
    "name": "Huyện Phong Thổ",
    "code": "109",
    "parent_id": "35",
    "slug": "huyen phong tho"
  },
  "488": {
    "id": "488",
    "name": "Huyện Sìn Hồ",
    "code": "108",
    "parent_id": "35",
    "slug": "huyen sin ho"
  },
  "489": {
    "id": "489",
    "name": "Huyện Tam Đường",
    "code": "106",
    "parent_id": "35",
    "slug": "huyen tam duong"
  },
  "490": {
    "id": "490",
    "name": "Huyện Tân Uyên",
    "code": "111",
    "parent_id": "35",
    "slug": "huyen tan uyen"
  },
  "491": {
    "id": "491",
    "name": "Huyện Than Uyên",
    "code": "110",
    "parent_id": "35",
    "slug": "huyen than uyen"
  },
  "492": {
    "id": "492",
    "name": "Thành phố Lai Châu",
    "code": "105",
    "parent_id": "35",
    "slug": "thanh pho lai chau"
  },
  "493": {
    "id": "493",
    "name": "Huyện Bảo Lâm",
    "code": "680",
    "parent_id": "36",
    "slug": "huyen bao lam"
  },
  "494": {
    "id": "494",
    "name": "Huyện Cát Tiên",
    "code": "683",
    "parent_id": "36",
    "slug": "huyen cat tien"
  },
  "495": {
    "id": "495",
    "name": "Huyện Đạ Huoai",
    "code": "681",
    "parent_id": "36",
    "slug": "huyen da huoai"
  },
  "496": {
    "id": "496",
    "name": "Huyện Đạ Tẻh",
    "code": "682",
    "parent_id": "36",
    "slug": "huyen da teh"
  },
  "497": {
    "id": "497",
    "name": "Huyện Đam Rông",
    "code": "674",
    "parent_id": "36",
    "slug": "huyen dam rong"
  },
  "498": {
    "id": "498",
    "name": "Huyện Di Linh",
    "code": "679",
    "parent_id": "36",
    "slug": "huyen di linh"
  },
  "499": {
    "id": "499",
    "name": "Huyện Đơn Dương",
    "code": "677",
    "parent_id": "36",
    "slug": "huyen don duong"
  },
  "500": {
    "id": "500",
    "name": "Huyện Đức Trọng",
    "code": "678",
    "parent_id": "36",
    "slug": "huyen duc trong"
  },
  "501": {
    "id": "501",
    "name": "Huyện Lạc Dương",
    "code": "675",
    "parent_id": "36",
    "slug": "huyen lac duong"
  },
  "502": {
    "id": "502",
    "name": "Huyện Lâm Hà",
    "code": "676",
    "parent_id": "36",
    "slug": "huyen lam ha"
  },
  "503": {
    "id": "503",
    "name": "Thành phố Bảo Lộc",
    "code": "673",
    "parent_id": "36",
    "slug": "thanh pho bao loc"
  },
  "504": {
    "id": "504",
    "name": "Thành phố Đà Lạt",
    "code": "672",
    "parent_id": "36",
    "slug": "thanh pho da lat"
  },
  "505": {
    "id": "505",
    "name": "Huyện Bắc Sơn",
    "code": "185",
    "parent_id": "37",
    "slug": "huyen bac son"
  },
  "506": {
    "id": "506",
    "name": "Huyện Bình Gia",
    "code": "181",
    "parent_id": "37",
    "slug": "huyen binh gia"
  },
  "507": {
    "id": "507",
    "name": "Huyện Cao Lộc",
    "code": "183",
    "parent_id": "37",
    "slug": "huyen cao loc"
  },
  "508": {
    "id": "508",
    "name": "Huyện Chi Lăng",
    "code": "187",
    "parent_id": "37",
    "slug": "huyen chi lang"
  },
  "509": {
    "id": "509",
    "name": "Huyện Đình Lập",
    "code": "189",
    "parent_id": "37",
    "slug": "huyen dinh lap"
  },
  "510": {
    "id": "510",
    "name": "Huyện Hữu Lũng",
    "code": "186",
    "parent_id": "37",
    "slug": "huyen huu lung"
  },
  "511": {
    "id": "511",
    "name": "Huyện Lộc Bình",
    "code": "188",
    "parent_id": "37",
    "slug": "huyen loc binh"
  },
  "512": {
    "id": "512",
    "name": "Huyện Tràng Định",
    "code": "180",
    "parent_id": "37",
    "slug": "huyen trang dinh"
  },
  "513": {
    "id": "513",
    "name": "Huyện Văn Lãng",
    "code": "182",
    "parent_id": "37",
    "slug": "huyen van lang"
  },
  "514": {
    "id": "514",
    "name": "Huyện Văn Quan",
    "code": "184",
    "parent_id": "37",
    "slug": "huyen van quan"
  },
  "515": {
    "id": "515",
    "name": "Thành phố Lạng Sơn",
    "code": "178",
    "parent_id": "37",
    "slug": "thanh pho lang son"
  },
  "516": {
    "id": "516",
    "name": "Huyện Bắc Hà",
    "code": "085",
    "parent_id": "38",
    "slug": "huyen bac ha"
  },
  "517": {
    "id": "517",
    "name": "Huyện Bảo Thắng",
    "code": "086",
    "parent_id": "38",
    "slug": "huyen bao thang"
  },
  "518": {
    "id": "518",
    "name": "Huyện Bảo Yên",
    "code": "087",
    "parent_id": "38",
    "slug": "huyen bao yen"
  },
  "519": {
    "id": "519",
    "name": "Huyện Bát Xát",
    "code": "082",
    "parent_id": "38",
    "slug": "huyen bat xat"
  },
  "520": {
    "id": "520",
    "name": "Huyện Mường Khương",
    "code": "083",
    "parent_id": "38",
    "slug": "huyen muong khuong"
  },
  "521": {
    "id": "521",
    "name": "Huyện Sa Pa",
    "code": "088",
    "parent_id": "38",
    "slug": "huyen sa pa"
  },
  "522": {
    "id": "522",
    "name": "Huyện Si Ma Cai",
    "code": "084",
    "parent_id": "38",
    "slug": "huyen si ma cai"
  },
  "523": {
    "id": "523",
    "name": "Huyện Văn Bàn",
    "code": "089",
    "parent_id": "38",
    "slug": "huyen van ban"
  },
  "524": {
    "id": "524",
    "name": "Thành phố Lào Cai",
    "code": "080",
    "parent_id": "38",
    "slug": "thanh pho lao cai"
  },
  "525": {
    "id": "525",
    "name": "Huyện Bến Lức",
    "code": "803",
    "parent_id": "39",
    "slug": "huyen ben luc"
  },
  "526": {
    "id": "526",
    "name": "Huyện Cần Đước",
    "code": "806",
    "parent_id": "39",
    "slug": "huyen can duoc"
  },
  "527": {
    "id": "527",
    "name": "Huyện Cần Giuộc",
    "code": "807",
    "parent_id": "39",
    "slug": "huyen can giuoc"
  },
  "528": {
    "id": "528",
    "name": "Huyện Châu Thành",
    "code": "808",
    "parent_id": "39",
    "slug": "huyen chau thanh"
  },
  "529": {
    "id": "529",
    "name": "Huyện Đức Hòa",
    "code": "802",
    "parent_id": "39",
    "slug": "huyen duc hoa"
  },
  "530": {
    "id": "530",
    "name": "Huyện Đức Huệ",
    "code": "801",
    "parent_id": "39",
    "slug": "huyen duc hue"
  },
  "531": {
    "id": "531",
    "name": "Huyện Mộc Hóa",
    "code": "798",
    "parent_id": "39",
    "slug": "huyen moc hoa"
  },
  "532": {
    "id": "532",
    "name": "Huyện Tân Hưng",
    "code": "796",
    "parent_id": "39",
    "slug": "huyen tan hung"
  },
  "533": {
    "id": "533",
    "name": "Huyện Tân Thạnh",
    "code": "799",
    "parent_id": "39",
    "slug": "huyen tan thanh"
  },
  "534": {
    "id": "534",
    "name": "Huyện Tân Trụ",
    "code": "805",
    "parent_id": "39",
    "slug": "huyen tan tru"
  },
  "535": {
    "id": "535",
    "name": "Huyện Thạnh Hóa",
    "code": "800",
    "parent_id": "39",
    "slug": "huyen thanh hoa"
  },
  "536": {
    "id": "536",
    "name": "Huyện Thủ Thừa",
    "code": "804",
    "parent_id": "39",
    "slug": "huyen thu thua"
  },
  "537": {
    "id": "537",
    "name": "Huyện Vĩnh Hưng",
    "code": "797",
    "parent_id": "39",
    "slug": "huyen vinh hung"
  },
  "538": {
    "id": "538",
    "name": "Thành phố Tân An",
    "code": "794",
    "parent_id": "39",
    "slug": "thanh pho tan an"
  },
  "539": {
    "id": "539",
    "name": "Thị xã Kiến Tường",
    "code": "795",
    "parent_id": "39",
    "slug": "thi xa kien tuong"
  },
  "540": {
    "id": "540",
    "name": "Huyện Giao Thủy",
    "code": "365",
    "parent_id": "40",
    "slug": "huyen giao thuy"
  },
  "541": {
    "id": "541",
    "name": "Huyện Hải Hậu",
    "code": "366",
    "parent_id": "40",
    "slug": "huyen hai hau"
  },
  "542": {
    "id": "542",
    "name": "Huyện Mỹ Lộc",
    "code": "358",
    "parent_id": "40",
    "slug": "huyen my loc"
  },
  "543": {
    "id": "543",
    "name": "Huyện Nam Trực",
    "code": "362",
    "parent_id": "40",
    "slug": "huyen nam truc"
  },
  "544": {
    "id": "544",
    "name": "Huyện Nghĩa Hưng",
    "code": "361",
    "parent_id": "40",
    "slug": "huyen nghia hung"
  },
  "545": {
    "id": "545",
    "name": "Huyện Trực Ninh",
    "code": "363",
    "parent_id": "40",
    "slug": "huyen truc ninh"
  },
  "546": {
    "id": "546",
    "name": "Huyện Vụ Bản",
    "code": "359",
    "parent_id": "40",
    "slug": "huyen vu ban"
  },
  "547": {
    "id": "547",
    "name": "Huyện Xuân Trường",
    "code": "364",
    "parent_id": "40",
    "slug": "huyen xuan truong"
  },
  "548": {
    "id": "548",
    "name": "Huyện Ý Yên",
    "code": "360",
    "parent_id": "40",
    "slug": "huyen y yen"
  },
  "549": {
    "id": "549",
    "name": "Thành phố Nam Định",
    "code": "356",
    "parent_id": "40",
    "slug": "thanh pho nam dinh"
  },
  "550": {
    "id": "550",
    "name": "Huyện Anh Sơn",
    "code": "424",
    "parent_id": "41",
    "slug": "huyen anh son"
  },
  "551": {
    "id": "551",
    "name": "Huyện Con Cuông",
    "code": "422",
    "parent_id": "41",
    "slug": "huyen con cuong"
  },
  "552": {
    "id": "552",
    "name": "Huyện Diễn Châu",
    "code": "425",
    "parent_id": "41",
    "slug": "huyen dien chau"
  },
  "553": {
    "id": "553",
    "name": "Huyện Đô Lương",
    "code": "427",
    "parent_id": "41",
    "slug": "huyen do luong"
  },
  "554": {
    "id": "554",
    "name": "Huyện Hưng Nguyên",
    "code": "431",
    "parent_id": "41",
    "slug": "huyen hung nguyen"
  },
  "555": {
    "id": "555",
    "name": "Huyện Kỳ Sơn",
    "code": "417",
    "parent_id": "41",
    "slug": "huyen ky son"
  },
  "556": {
    "id": "556",
    "name": "Huyện Nam Đàn",
    "code": "430",
    "parent_id": "41",
    "slug": "huyen nam dan"
  },
  "557": {
    "id": "557",
    "name": "Huyện Nghi Lộc",
    "code": "429",
    "parent_id": "41",
    "slug": "huyen nghi loc"
  },
  "558": {
    "id": "558",
    "name": "Huyện Nghĩa Đàn",
    "code": "419",
    "parent_id": "41",
    "slug": "huyen nghia dan"
  },
  "559": {
    "id": "559",
    "name": "Huyện Quế Phong",
    "code": "415",
    "parent_id": "41",
    "slug": "huyen que phong"
  },
  "560": {
    "id": "560",
    "name": "Huyện Quỳ Châu",
    "code": "416",
    "parent_id": "41",
    "slug": "huyen quy chau"
  },
  "561": {
    "id": "561",
    "name": "Huyện Quỳ Hợp",
    "code": "420",
    "parent_id": "41",
    "slug": "huyen quy hop"
  },
  "562": {
    "id": "562",
    "name": "Huyện Quỳnh Lưu",
    "code": "421",
    "parent_id": "41",
    "slug": "huyen quynh luu"
  },
  "563": {
    "id": "563",
    "name": "Huyện Tân Kỳ",
    "code": "423",
    "parent_id": "41",
    "slug": "huyen tan ky"
  },
  "564": {
    "id": "564",
    "name": "Huyện Thanh Chương",
    "code": "428",
    "parent_id": "41",
    "slug": "huyen thanh chuong"
  },
  "565": {
    "id": "565",
    "name": "Huyện Tương Dương",
    "code": "418",
    "parent_id": "41",
    "slug": "huyen tuong duong"
  },
  "566": {
    "id": "566",
    "name": "Huyện Yên Thành",
    "code": "426",
    "parent_id": "41",
    "slug": "huyen yen thanh"
  },
  "567": {
    "id": "567",
    "name": "Thành phố Vinh",
    "code": "412",
    "parent_id": "41",
    "slug": "thanh pho vinh"
  },
  "568": {
    "id": "568",
    "name": "Thị xã Cửa Lò",
    "code": "413",
    "parent_id": "41",
    "slug": "thi xa cua lo"
  },
  "569": {
    "id": "569",
    "name": "Thị xã Hoàng Mai",
    "code": "432",
    "parent_id": "41",
    "slug": "thi xa hoang mai"
  },
  "570": {
    "id": "570",
    "name": "Thị xã Thái Hoà",
    "code": "414",
    "parent_id": "41",
    "slug": "thi xa thai hoa"
  },
  "571": {
    "id": "571",
    "name": "Huyện Gia Viễn",
    "code": "373",
    "parent_id": "42",
    "slug": "huyen gia vien"
  },
  "572": {
    "id": "572",
    "name": "Huyện Hoa Lư",
    "code": "374",
    "parent_id": "42",
    "slug": "huyen hoa lu"
  },
  "573": {
    "id": "573",
    "name": "Huyện Kim Sơn",
    "code": "376",
    "parent_id": "42",
    "slug": "huyen kim son"
  },
  "574": {
    "id": "574",
    "name": "Huyện Nho Quan",
    "code": "372",
    "parent_id": "42",
    "slug": "huyen nho quan"
  },
  "575": {
    "id": "575",
    "name": "Huyện Yên Khánh",
    "code": "375",
    "parent_id": "42",
    "slug": "huyen yen khanh"
  },
  "576": {
    "id": "576",
    "name": "Huyện Yên Mô",
    "code": "377",
    "parent_id": "42",
    "slug": "huyen yen mo"
  },
  "577": {
    "id": "577",
    "name": "Thành phố Ninh Bình",
    "code": "369",
    "parent_id": "42",
    "slug": "thanh pho ninh binh"
  },
  "578": {
    "id": "578",
    "name": "Thành phố Tam Điệp",
    "code": "370",
    "parent_id": "42",
    "slug": "thanh pho tam diep"
  },
  "579": {
    "id": "579",
    "name": "Huyện Bác Ái",
    "code": "584",
    "parent_id": "43",
    "slug": "huyen bac ai"
  },
  "580": {
    "id": "580",
    "name": "Huyện Ninh Hải",
    "code": "586",
    "parent_id": "43",
    "slug": "huyen ninh hai"
  },
  "581": {
    "id": "581",
    "name": "Huyện Ninh Phước",
    "code": "587",
    "parent_id": "43",
    "slug": "huyen ninh phuoc"
  },
  "582": {
    "id": "582",
    "name": "Huyện Ninh Sơn",
    "code": "585",
    "parent_id": "43",
    "slug": "huyen ninh son"
  },
  "583": {
    "id": "583",
    "name": "Huyện Thuận Bắc",
    "code": "588",
    "parent_id": "43",
    "slug": "huyen thuan bac"
  },
  "584": {
    "id": "584",
    "name": "Huyện Thuận Nam",
    "code": "589",
    "parent_id": "43",
    "slug": "huyen thuan nam"
  },
  "585": {
    "id": "585",
    "name": "Thành phố Phan Rang-Tháp Chàm",
    "code": "582",
    "parent_id": "43",
    "slug": "thanh pho phan rang-thap cham"
  },
  "586": {
    "id": "586",
    "name": "Huyện Cẩm Khê",
    "code": "235",
    "parent_id": "44",
    "slug": "huyen cam khe"
  },
  "587": {
    "id": "587",
    "name": "Huyện Đoan Hùng",
    "code": "230",
    "parent_id": "44",
    "slug": "huyen doan hung"
  },
  "588": {
    "id": "588",
    "name": "Huyện Hạ Hoà",
    "code": "231",
    "parent_id": "44",
    "slug": "huyen ha hoa"
  },
  "589": {
    "id": "589",
    "name": "Huyện Lâm Thao",
    "code": "237",
    "parent_id": "44",
    "slug": "huyen lam thao"
  },
  "590": {
    "id": "590",
    "name": "Huyện Phù Ninh",
    "code": "233",
    "parent_id": "44",
    "slug": "huyen phu ninh"
  },
  "591": {
    "id": "591",
    "name": "Huyện Tam Nông",
    "code": "236",
    "parent_id": "44",
    "slug": "huyen tam nong"
  },
  "592": {
    "id": "592",
    "name": "Huyện Tân Sơn",
    "code": "240",
    "parent_id": "44",
    "slug": "huyen tan son"
  },
  "593": {
    "id": "593",
    "name": "Huyện Thanh Ba",
    "code": "232",
    "parent_id": "44",
    "slug": "huyen thanh ba"
  },
  "594": {
    "id": "594",
    "name": "Huyện Thanh Sơn",
    "code": "238",
    "parent_id": "44",
    "slug": "huyen thanh son"
  },
  "595": {
    "id": "595",
    "name": "Huyện Thanh Thuỷ",
    "code": "239",
    "parent_id": "44",
    "slug": "huyen thanh thuy"
  },
  "596": {
    "id": "596",
    "name": "Huyện Yên Lập",
    "code": "234",
    "parent_id": "44",
    "slug": "huyen yen lap"
  },
  "597": {
    "id": "597",
    "name": "Thành phố Việt Trì",
    "code": "227",
    "parent_id": "44",
    "slug": "thanh pho viet tri"
  },
  "598": {
    "id": "598",
    "name": "Thị xã Phú Thọ",
    "code": "228",
    "parent_id": "44",
    "slug": "thi xa phu tho"
  },
  "599": {
    "id": "599",
    "name": "Huyện Đông Hòa",
    "code": "564",
    "parent_id": "45",
    "slug": "huyen dong hoa"
  },
  "600": {
    "id": "600",
    "name": "Huyện Đồng Xuân",
    "code": "558",
    "parent_id": "45",
    "slug": "huyen dong xuan"
  },
  "601": {
    "id": "601",
    "name": "Huyện Phú Hoà",
    "code": "563",
    "parent_id": "45",
    "slug": "huyen phu hoa"
  },
  "602": {
    "id": "602",
    "name": "Huyện Sơn Hòa",
    "code": "560",
    "parent_id": "45",
    "slug": "huyen son hoa"
  },
  "603": {
    "id": "603",
    "name": "Huyện Sông Hinh",
    "code": "561",
    "parent_id": "45",
    "slug": "huyen song hinh"
  },
  "604": {
    "id": "604",
    "name": "Huyện Tây Hoà",
    "code": "562",
    "parent_id": "45",
    "slug": "huyen tay hoa"
  },
  "605": {
    "id": "605",
    "name": "Huyện Tuy An",
    "code": "559",
    "parent_id": "45",
    "slug": "huyen tuy an"
  },
  "606": {
    "id": "606",
    "name": "Thành phố Tuy Hoà",
    "code": "555",
    "parent_id": "45",
    "slug": "thanh pho tuy hoa"
  },
  "607": {
    "id": "607",
    "name": "Thị xã Sông Cầu",
    "code": "557",
    "parent_id": "45",
    "slug": "thi xa song cau"
  },
  "608": {
    "id": "608",
    "name": "Huyện Bố Trạch",
    "code": "455",
    "parent_id": "46",
    "slug": "huyen bo trach"
  },
  "609": {
    "id": "609",
    "name": "Huyện Lệ Thủy",
    "code": "457",
    "parent_id": "46",
    "slug": "huyen le thuy"
  },
  "610": {
    "id": "610",
    "name": "Huyện Minh Hóa",
    "code": "452",
    "parent_id": "46",
    "slug": "huyen minh hoa"
  },
  "611": {
    "id": "611",
    "name": "Huyện Quảng Ninh",
    "code": "456",
    "parent_id": "46",
    "slug": "huyen quang ninh"
  },
  "612": {
    "id": "612",
    "name": "Huyện Quảng Trạch",
    "code": "458",
    "parent_id": "46",
    "slug": "huyen quang trach"
  },
  "613": {
    "id": "613",
    "name": "Huyện Tuyên Hóa",
    "code": "453",
    "parent_id": "46",
    "slug": "huyen tuyen hoa"
  },
  "614": {
    "id": "614",
    "name": "Thành Phố Đồng Hới",
    "code": "450",
    "parent_id": "46",
    "slug": "thanh pho dong hoi"
  },
  "615": {
    "id": "615",
    "name": "Thị xã Ba Đồn",
    "code": "454",
    "parent_id": "46",
    "slug": "thi xa ba don"
  },
  "616": {
    "id": "616",
    "name": "Huyện Bắc Trà My",
    "code": "515",
    "parent_id": "47",
    "slug": "huyen bac tra my"
  },
  "617": {
    "id": "617",
    "name": "Huyện Đại Lộc",
    "code": "506",
    "parent_id": "47",
    "slug": "huyen dai loc"
  },
  "618": {
    "id": "618",
    "name": "Huyện Đông Giang",
    "code": "505",
    "parent_id": "47",
    "slug": "huyen dong giang"
  },
  "619": {
    "id": "619",
    "name": "Huyện Duy Xuyên",
    "code": "508",
    "parent_id": "47",
    "slug": "huyen duy xuyen"
  },
  "620": {
    "id": "620",
    "name": "Huyện Hiệp Đức",
    "code": "512",
    "parent_id": "47",
    "slug": "huyen hiep duc"
  },
  "621": {
    "id": "621",
    "name": "Huyện Nam Giang",
    "code": "510",
    "parent_id": "47",
    "slug": "huyen nam giang"
  },
  "622": {
    "id": "622",
    "name": "Huyện Nam Trà My",
    "code": "516",
    "parent_id": "47",
    "slug": "huyen nam tra my"
  },
  "623": {
    "id": "623",
    "name": "Huyện Nông Sơn",
    "code": "519",
    "parent_id": "47",
    "slug": "huyen nong son"
  },
  "624": {
    "id": "624",
    "name": "Huyện Núi Thành",
    "code": "517",
    "parent_id": "47",
    "slug": "huyen nui thanh"
  },
  "625": {
    "id": "625",
    "name": "Huyện Phú Ninh",
    "code": "518",
    "parent_id": "47",
    "slug": "huyen phu ninh"
  },
  "626": {
    "id": "626",
    "name": "Huyện Phước Sơn",
    "code": "511",
    "parent_id": "47",
    "slug": "huyen phuoc son"
  },
  "627": {
    "id": "627",
    "name": "Huyện Quế Sơn",
    "code": "509",
    "parent_id": "47",
    "slug": "huyen que son"
  },
  "628": {
    "id": "628",
    "name": "Huyện Tây Giang",
    "code": "504",
    "parent_id": "47",
    "slug": "huyen tay giang"
  },
  "629": {
    "id": "629",
    "name": "Huyện Thăng Bình",
    "code": "513",
    "parent_id": "47",
    "slug": "huyen thang binh"
  },
  "630": {
    "id": "630",
    "name": "Huyện Tiên Phước",
    "code": "514",
    "parent_id": "47",
    "slug": "huyen tien phuoc"
  },
  "631": {
    "id": "631",
    "name": "Thành phố Hội An",
    "code": "503",
    "parent_id": "47",
    "slug": "thanh pho hoi an"
  },
  "632": {
    "id": "632",
    "name": "Thành phố Tam Kỳ",
    "code": "502",
    "parent_id": "47",
    "slug": "thanh pho tam ky"
  },
  "633": {
    "id": "633",
    "name": "Thị xã Điện Bàn",
    "code": "507",
    "parent_id": "47",
    "slug": "thi xa dien ban"
  },
  "634": {
    "id": "634",
    "name": "Huyện Ba Tơ",
    "code": "535",
    "parent_id": "48",
    "slug": "huyen ba to"
  },
  "635": {
    "id": "635",
    "name": "Huyện Bình Sơn",
    "code": "524",
    "parent_id": "48",
    "slug": "huyen binh son"
  },
  "636": {
    "id": "636",
    "name": "Huyện Đức Phổ",
    "code": "534",
    "parent_id": "48",
    "slug": "huyen duc pho"
  },
  "637": {
    "id": "637",
    "name": "Huyện Lý Sơn",
    "code": "536",
    "parent_id": "48",
    "slug": "huyen ly son"
  },
  "638": {
    "id": "638",
    "name": "Huyện Minh Long",
    "code": "531",
    "parent_id": "48",
    "slug": "huyen minh long"
  },
  "639": {
    "id": "639",
    "name": "Huyện Mộ Đức",
    "code": "533",
    "parent_id": "48",
    "slug": "huyen mo duc"
  },
  "640": {
    "id": "640",
    "name": "Huyện Nghĩa Hành",
    "code": "532",
    "parent_id": "48",
    "slug": "huyen nghia hanh"
  },
  "641": {
    "id": "641",
    "name": "Huyện Sơn Hà",
    "code": "529",
    "parent_id": "48",
    "slug": "huyen son ha"
  },
  "642": {
    "id": "642",
    "name": "Huyện Sơn Tây",
    "code": "530",
    "parent_id": "48",
    "slug": "huyen son tay"
  },
  "643": {
    "id": "643",
    "name": "Huyện Sơn Tịnh",
    "code": "527",
    "parent_id": "48",
    "slug": "huyen son tinh"
  },
  "644": {
    "id": "644",
    "name": "Huyện Tây Trà",
    "code": "526",
    "parent_id": "48",
    "slug": "huyen tay tra"
  },
  "645": {
    "id": "645",
    "name": "Huyện Trà Bồng",
    "code": "525",
    "parent_id": "48",
    "slug": "huyen tra bong"
  },
  "646": {
    "id": "646",
    "name": "Huyện Tư Nghĩa",
    "code": "528",
    "parent_id": "48",
    "slug": "huyen tu nghia"
  },
  "647": {
    "id": "647",
    "name": "Thành phố Quảng Ngãi",
    "code": "522",
    "parent_id": "48",
    "slug": "thanh pho quang ngai"
  },
  "648": {
    "id": "648",
    "name": "Huyện Ba Chẽ",
    "code": "202",
    "parent_id": "49",
    "slug": "huyen ba che"
  },
  "649": {
    "id": "649",
    "name": "Huyện Bình Liêu",
    "code": "198",
    "parent_id": "49",
    "slug": "huyen binh lieu"
  },
  "650": {
    "id": "650",
    "name": "Huyện Cô Tô",
    "code": "207",
    "parent_id": "49",
    "slug": "huyen co to"
  },
  "651": {
    "id": "651",
    "name": "Huyện Đầm Hà",
    "code": "200",
    "parent_id": "49",
    "slug": "huyen dam ha"
  },
  "652": {
    "id": "652",
    "name": "Huyện Hải Hà",
    "code": "201",
    "parent_id": "49",
    "slug": "huyen hai ha"
  },
  "653": {
    "id": "653",
    "name": "Huyện Hoành Bồ",
    "code": "204",
    "parent_id": "49",
    "slug": "huyen hoanh bo"
  },
  "654": {
    "id": "654",
    "name": "Huyện Tiên Yên",
    "code": "199",
    "parent_id": "49",
    "slug": "huyen tien yen"
  },
  "655": {
    "id": "655",
    "name": "Huyện Vân Đồn",
    "code": "203",
    "parent_id": "49",
    "slug": "huyen van don"
  },
  "656": {
    "id": "656",
    "name": "Thành phố Cẩm Phả",
    "code": "195",
    "parent_id": "49",
    "slug": "thanh pho cam pha"
  },
  "657": {
    "id": "657",
    "name": "Thành phố Hạ Long",
    "code": "193",
    "parent_id": "49",
    "slug": "thanh pho ha long"
  },
  "658": {
    "id": "658",
    "name": "Thành phố Móng Cái",
    "code": "194",
    "parent_id": "49",
    "slug": "thanh pho mong cai"
  },
  "659": {
    "id": "659",
    "name": "Thành phố Uông Bí",
    "code": "196",
    "parent_id": "49",
    "slug": "thanh pho uong bi"
  },
  "660": {
    "id": "660",
    "name": "Thị xã Đông Triều",
    "code": "205",
    "parent_id": "49",
    "slug": "thi xa dong trieu"
  },
  "661": {
    "id": "661",
    "name": "Thị xã Quảng Yên",
    "code": "206",
    "parent_id": "49",
    "slug": "thi xa quang yen"
  },
  "662": {
    "id": "662",
    "name": "Huyện Cam Lộ",
    "code": "468",
    "parent_id": "50",
    "slug": "huyen cam lo"
  },
  "663": {
    "id": "663",
    "name": "Huyện Đa Krông",
    "code": "467",
    "parent_id": "50",
    "slug": "huyen da krong"
  },
  "664": {
    "id": "664",
    "name": "Huyện Gio Linh",
    "code": "466",
    "parent_id": "50",
    "slug": "huyen gio linh"
  },
  "665": {
    "id": "665",
    "name": "Huyện Hải Lăng",
    "code": "470",
    "parent_id": "50",
    "slug": "huyen hai lang"
  },
  "666": {
    "id": "666",
    "name": "Huyện Hướng Hóa",
    "code": "465",
    "parent_id": "50",
    "slug": "huyen huong hoa"
  },
  "667": {
    "id": "667",
    "name": "Huyện Triệu Phong",
    "code": "469",
    "parent_id": "50",
    "slug": "huyen trieu phong"
  },
  "668": {
    "id": "668",
    "name": "Huyện Vĩnh Linh",
    "code": "464",
    "parent_id": "50",
    "slug": "huyen vinh linh"
  },
  "669": {
    "id": "669",
    "name": "Thành phố Đông Hà",
    "code": "461",
    "parent_id": "50",
    "slug": "thanh pho dong ha"
  },
  "670": {
    "id": "670",
    "name": "Thị xã Quảng Trị",
    "code": "462",
    "parent_id": "50",
    "slug": "thi xa quang tri"
  },
  "671": {
    "id": "671",
    "name": "Huyện Châu Thành",
    "code": "942",
    "parent_id": "51",
    "slug": "huyen chau thanh"
  },
  "672": {
    "id": "672",
    "name": "Huyện Cù Lao Dung",
    "code": "945",
    "parent_id": "51",
    "slug": "huyen cu lao dung"
  },
  "673": {
    "id": "673",
    "name": "Huyện Kế Sách",
    "code": "943",
    "parent_id": "51",
    "slug": "huyen ke sach"
  },
  "674": {
    "id": "674",
    "name": "Huyện Long Phú",
    "code": "946",
    "parent_id": "51",
    "slug": "huyen long phu"
  },
  "675": {
    "id": "675",
    "name": "Huyện Mỹ Tú",
    "code": "944",
    "parent_id": "51",
    "slug": "huyen my tu"
  },
  "676": {
    "id": "676",
    "name": "Huyện Mỹ Xuyên",
    "code": "947",
    "parent_id": "51",
    "slug": "huyen my xuyen"
  },
  "677": {
    "id": "677",
    "name": "Huyện Thạnh Trị",
    "code": "949",
    "parent_id": "51",
    "slug": "huyen thanh tri"
  },
  "678": {
    "id": "678",
    "name": "Huyện Trần Đề",
    "code": "951",
    "parent_id": "51",
    "slug": "huyen tran de"
  },
  "679": {
    "id": "679",
    "name": "Thành phố Sóc Trăng",
    "code": "941",
    "parent_id": "51",
    "slug": "thanh pho soc trang"
  },
  "680": {
    "id": "680",
    "name": "Thị xã Ngã Năm",
    "code": "948",
    "parent_id": "51",
    "slug": "thi xa nga nam"
  },
  "681": {
    "id": "681",
    "name": "Thị xã Vĩnh Châu",
    "code": "950",
    "parent_id": "51",
    "slug": "thi xa vinh chau"
  },
  "682": {
    "id": "682",
    "name": "Huyện Bắc Yên",
    "code": "121",
    "parent_id": "52",
    "slug": "huyen bac yen"
  },
  "683": {
    "id": "683",
    "name": "Huyện Mai Sơn",
    "code": "125",
    "parent_id": "52",
    "slug": "huyen mai son"
  },
  "684": {
    "id": "684",
    "name": "Huyện Mộc Châu",
    "code": "123",
    "parent_id": "52",
    "slug": "huyen moc chau"
  },
  "685": {
    "id": "685",
    "name": "Huyện Mường La",
    "code": "120",
    "parent_id": "52",
    "slug": "huyen muong la"
  },
  "686": {
    "id": "686",
    "name": "Huyện Phù Yên",
    "code": "122",
    "parent_id": "52",
    "slug": "huyen phu yen"
  },
  "687": {
    "id": "687",
    "name": "Huyện Quỳnh Nhai",
    "code": "118",
    "parent_id": "52",
    "slug": "huyen quynh nhai"
  },
  "688": {
    "id": "688",
    "name": "Huyện Sông Mã",
    "code": "126",
    "parent_id": "52",
    "slug": "huyen song ma"
  },
  "689": {
    "id": "689",
    "name": "Huyện Sốp Cộp",
    "code": "127",
    "parent_id": "52",
    "slug": "huyen sop cop"
  },
  "690": {
    "id": "690",
    "name": "Huyện Thuận Châu",
    "code": "119",
    "parent_id": "52",
    "slug": "huyen thuan chau"
  },
  "691": {
    "id": "691",
    "name": "Huyện Vân Hồ",
    "code": "128",
    "parent_id": "52",
    "slug": "huyen van ho"
  },
  "692": {
    "id": "692",
    "name": "Huyện Yên Châu",
    "code": "124",
    "parent_id": "52",
    "slug": "huyen yen chau"
  },
  "693": {
    "id": "693",
    "name": "Thành phố Sơn La",
    "code": "116",
    "parent_id": "52",
    "slug": "thanh pho son la"
  },
  "694": {
    "id": "694",
    "name": "Huyện Bến Cầu",
    "code": "711",
    "parent_id": "53",
    "slug": "huyen ben cau"
  },
  "695": {
    "id": "695",
    "name": "Huyện Châu Thành",
    "code": "708",
    "parent_id": "53",
    "slug": "huyen chau thanh"
  },
  "696": {
    "id": "696",
    "name": "Huyện Dương Minh Châu",
    "code": "707",
    "parent_id": "53",
    "slug": "huyen duong minh chau"
  },
  "697": {
    "id": "697",
    "name": "Huyện Gò Dầu",
    "code": "710",
    "parent_id": "53",
    "slug": "huyen go dau"
  },
  "698": {
    "id": "698",
    "name": "Huyện Hòa Thành",
    "code": "709",
    "parent_id": "53",
    "slug": "huyen hoa thanh"
  },
  "699": {
    "id": "699",
    "name": "Huyện Tân Biên",
    "code": "705",
    "parent_id": "53",
    "slug": "huyen tan bien"
  },
  "700": {
    "id": "700",
    "name": "Huyện Tân Châu",
    "code": "706",
    "parent_id": "53",
    "slug": "huyen tan chau"
  },
  "701": {
    "id": "701",
    "name": "Huyện Trảng Bàng",
    "code": "712",
    "parent_id": "53",
    "slug": "huyen trang bang"
  },
  "702": {
    "id": "702",
    "name": "Thành phố Tây Ninh",
    "code": "703",
    "parent_id": "53",
    "slug": "thanh pho tay ninh"
  },
  "703": {
    "id": "703",
    "name": "Huyện Đông Hưng",
    "code": "340",
    "parent_id": "54",
    "slug": "huyen dong hung"
  },
  "704": {
    "id": "704",
    "name": "Huyện Hưng Hà",
    "code": "339",
    "parent_id": "54",
    "slug": "huyen hung ha"
  },
  "705": {
    "id": "705",
    "name": "Huyện Kiến Xương",
    "code": "343",
    "parent_id": "54",
    "slug": "huyen kien xuong"
  },
  "706": {
    "id": "706",
    "name": "Huyện Quỳnh Phụ",
    "code": "338",
    "parent_id": "54",
    "slug": "huyen quynh phu"
  },
  "707": {
    "id": "707",
    "name": "Huyện Thái Thụy",
    "code": "341",
    "parent_id": "54",
    "slug": "huyen thai thuy"
  },
  "708": {
    "id": "708",
    "name": "Huyện Tiền Hải",
    "code": "342",
    "parent_id": "54",
    "slug": "huyen tien hai"
  },
  "709": {
    "id": "709",
    "name": "Huyện Vũ Thư",
    "code": "344",
    "parent_id": "54",
    "slug": "huyen vu thu"
  },
  "710": {
    "id": "710",
    "name": "Thành phố Thái Bình",
    "code": "336",
    "parent_id": "54",
    "slug": "thanh pho thai binh"
  },
  "711": {
    "id": "711",
    "name": "Huyện Đại Từ",
    "code": "171",
    "parent_id": "55",
    "slug": "huyen dai tu"
  },
  "712": {
    "id": "712",
    "name": "Huyện Định Hóa",
    "code": "167",
    "parent_id": "55",
    "slug": "huyen dinh hoa"
  },
  "713": {
    "id": "713",
    "name": "Huyện Đồng Hỷ",
    "code": "169",
    "parent_id": "55",
    "slug": "huyen dong hy"
  },
  "714": {
    "id": "714",
    "name": "Huyện Phú Bình",
    "code": "173",
    "parent_id": "55",
    "slug": "huyen phu binh"
  },
  "715": {
    "id": "715",
    "name": "Huyện Phú Lương",
    "code": "168",
    "parent_id": "55",
    "slug": "huyen phu luong"
  },
  "716": {
    "id": "716",
    "name": "Huyện Võ Nhai",
    "code": "170",
    "parent_id": "55",
    "slug": "huyen vo nhai"
  },
  "717": {
    "id": "717",
    "name": "Thành phố Sông Công",
    "code": "165",
    "parent_id": "55",
    "slug": "thanh pho song cong"
  },
  "718": {
    "id": "718",
    "name": "Thành phố Thái Nguyên",
    "code": "164",
    "parent_id": "55",
    "slug": "thanh pho thai nguyen"
  },
  "719": {
    "id": "719",
    "name": "Thị xã Phổ Yên",
    "code": "172",
    "parent_id": "55",
    "slug": "thi xa pho yen"
  },
  "720": {
    "id": "720",
    "name": "Huyện Bá Thước",
    "code": "386",
    "parent_id": "56",
    "slug": "huyen ba thuoc"
  },
  "721": {
    "id": "721",
    "name": "Huyện Cẩm Thủy",
    "code": "390",
    "parent_id": "56",
    "slug": "huyen cam thuy"
  },
  "722": {
    "id": "722",
    "name": "Huyện Đông Sơn",
    "code": "405",
    "parent_id": "56",
    "slug": "huyen dong son"
  },
  "723": {
    "id": "723",
    "name": "Huyện Hà Trung",
    "code": "392",
    "parent_id": "56",
    "slug": "huyen ha trung"
  },
  "724": {
    "id": "724",
    "name": "Huyện Hậu Lộc",
    "code": "400",
    "parent_id": "56",
    "slug": "huyen hau loc"
  },
  "725": {
    "id": "725",
    "name": "Huyện Hoằng Hóa",
    "code": "399",
    "parent_id": "56",
    "slug": "huyen hoang hoa"
  },
  "726": {
    "id": "726",
    "name": "Huyện Lang Chánh",
    "code": "388",
    "parent_id": "56",
    "slug": "huyen lang chanh"
  },
  "727": {
    "id": "727",
    "name": "Huyện Mường Lát",
    "code": "384",
    "parent_id": "56",
    "slug": "huyen muong lat"
  },
  "728": {
    "id": "728",
    "name": "Huyện Nga Sơn",
    "code": "401",
    "parent_id": "56",
    "slug": "huyen nga son"
  },
  "729": {
    "id": "729",
    "name": "Huyện Ngọc Lặc",
    "code": "389",
    "parent_id": "56",
    "slug": "huyen ngoc lac"
  },
  "730": {
    "id": "730",
    "name": "Huyện Như Thanh",
    "code": "403",
    "parent_id": "56",
    "slug": "huyen nhu thanh"
  },
  "731": {
    "id": "731",
    "name": "Huyện Như Xuân",
    "code": "402",
    "parent_id": "56",
    "slug": "huyen nhu xuan"
  },
  "732": {
    "id": "732",
    "name": "Huyện Nông Cống",
    "code": "404",
    "parent_id": "56",
    "slug": "huyen nong cong"
  },
  "733": {
    "id": "733",
    "name": "Huyện Quan Hóa",
    "code": "385",
    "parent_id": "56",
    "slug": "huyen quan hoa"
  },
  "734": {
    "id": "734",
    "name": "Huyện Quan Sơn",
    "code": "387",
    "parent_id": "56",
    "slug": "huyen quan son"
  },
  "735": {
    "id": "735",
    "name": "Huyện Quảng Xương",
    "code": "406",
    "parent_id": "56",
    "slug": "huyen quang xuong"
  },
  "736": {
    "id": "736",
    "name": "Huyện Thạch Thành",
    "code": "391",
    "parent_id": "56",
    "slug": "huyen thach thanh"
  },
  "737": {
    "id": "737",
    "name": "Huyện Thiệu Hóa",
    "code": "398",
    "parent_id": "56",
    "slug": "huyen thieu hoa"
  },
  "738": {
    "id": "738",
    "name": "Huyện Thọ Xuân",
    "code": "395",
    "parent_id": "56",
    "slug": "huyen tho xuan"
  },
  "739": {
    "id": "739",
    "name": "Huyện Thường Xuân",
    "code": "396",
    "parent_id": "56",
    "slug": "huyen thuong xuan"
  },
  "740": {
    "id": "740",
    "name": "Huyện Tĩnh Gia",
    "code": "407",
    "parent_id": "56",
    "slug": "huyen tinh gia"
  },
  "741": {
    "id": "741",
    "name": "Huyện Triệu Sơn",
    "code": "397",
    "parent_id": "56",
    "slug": "huyen trieu son"
  },
  "742": {
    "id": "742",
    "name": "Huyện Vĩnh Lộc",
    "code": "393",
    "parent_id": "56",
    "slug": "huyen vinh loc"
  },
  "743": {
    "id": "743",
    "name": "Huyện Yên Định",
    "code": "394",
    "parent_id": "56",
    "slug": "huyen yen dinh"
  },
  "744": {
    "id": "744",
    "name": "Thành phố Thanh Hóa",
    "code": "380",
    "parent_id": "56",
    "slug": "thanh pho thanh hoa"
  },
  "745": {
    "id": "745",
    "name": "Thị xã Bỉm Sơn",
    "code": "381",
    "parent_id": "56",
    "slug": "thi xa bim son"
  },
  "746": {
    "id": "746",
    "name": "Thị xã Sầm Sơn",
    "code": "382",
    "parent_id": "56",
    "slug": "thi xa sam son"
  },
  "747": {
    "id": "747",
    "name": "Huyện A Lưới",
    "code": "481",
    "parent_id": "57",
    "slug": "huyen a luoi"
  },
  "748": {
    "id": "748",
    "name": "Huyện Nam Đông",
    "code": "483",
    "parent_id": "57",
    "slug": "huyen nam dong"
  },
  "749": {
    "id": "749",
    "name": "Huyện Phong Điền",
    "code": "476",
    "parent_id": "57",
    "slug": "huyen phong dien"
  },
  "750": {
    "id": "750",
    "name": "Huyện Phú Lộc",
    "code": "482",
    "parent_id": "57",
    "slug": "huyen phu loc"
  },
  "751": {
    "id": "751",
    "name": "Huyện Phú Vang",
    "code": "478",
    "parent_id": "57",
    "slug": "huyen phu vang"
  },
  "752": {
    "id": "752",
    "name": "Huyện Quảng Điền",
    "code": "477",
    "parent_id": "57",
    "slug": "huyen quang dien"
  },
  "753": {
    "id": "753",
    "name": "Thành phố Huế",
    "code": "474",
    "parent_id": "57",
    "slug": "thanh pho hue"
  },
  "754": {
    "id": "754",
    "name": "Thị xã Hương Thủy",
    "code": "479",
    "parent_id": "57",
    "slug": "thi xa huong thuy"
  },
  "755": {
    "id": "755",
    "name": "Thị xã Hương Trà",
    "code": "480",
    "parent_id": "57",
    "slug": "thi xa huong tra"
  },
  "756": {
    "id": "756",
    "name": "Huyện Cái Bè",
    "code": "819",
    "parent_id": "58",
    "slug": "huyen cai be"
  },
  "757": {
    "id": "757",
    "name": "Huyện Cai Lậy",
    "code": "817",
    "parent_id": "58",
    "slug": "huyen cai lay"
  },
  "758": {
    "id": "758",
    "name": "Huyện Châu Thành",
    "code": "821",
    "parent_id": "58",
    "slug": "huyen chau thanh"
  },
  "759": {
    "id": "759",
    "name": "Huyện Chợ Gạo",
    "code": "822",
    "parent_id": "58",
    "slug": "huyen cho gao"
  },
  "760": {
    "id": "760",
    "name": "Huyện Gò Công Đông",
    "code": "824",
    "parent_id": "58",
    "slug": "huyen go cong dong"
  },
  "761": {
    "id": "761",
    "name": "Huyện Gò Công Tây",
    "code": "823",
    "parent_id": "58",
    "slug": "huyen go cong tay"
  },
  "762": {
    "id": "762",
    "name": "Huyện Tân Phú Đông",
    "code": "825",
    "parent_id": "58",
    "slug": "huyen tan phu dong"
  },
  "763": {
    "id": "763",
    "name": "Huyện Tân Phước",
    "code": "818",
    "parent_id": "58",
    "slug": "huyen tan phuoc"
  },
  "764": {
    "id": "764",
    "name": "Thành phố Mỹ Tho",
    "code": "815",
    "parent_id": "58",
    "slug": "thanh pho my tho"
  },
  "765": {
    "id": "765",
    "name": "Thị xã Cai Lậy",
    "code": "820",
    "parent_id": "58",
    "slug": "thi xa cai lay"
  },
  "766": {
    "id": "766",
    "name": "Thị xã Gò Công",
    "code": "816",
    "parent_id": "58",
    "slug": "thi xa go cong"
  },
  "767": {
    "id": "767",
    "name": "Huyện Càng Long",
    "code": "844",
    "parent_id": "59",
    "slug": "huyen cang long"
  },
  "768": {
    "id": "768",
    "name": "Huyện Cầu Kè",
    "code": "845",
    "parent_id": "59",
    "slug": "huyen cau ke"
  },
  "769": {
    "id": "769",
    "name": "Huyện Cầu Ngang",
    "code": "848",
    "parent_id": "59",
    "slug": "huyen cau ngang"
  },
  "770": {
    "id": "770",
    "name": "Huyện Châu Thành",
    "code": "847",
    "parent_id": "59",
    "slug": "huyen chau thanh"
  },
  "771": {
    "id": "771",
    "name": "Huyện Duyên Hải",
    "code": "850",
    "parent_id": "59",
    "slug": "huyen duyen hai"
  },
  "772": {
    "id": "772",
    "name": "Huyện Tiểu Cần",
    "code": "846",
    "parent_id": "59",
    "slug": "huyen tieu can"
  },
  "773": {
    "id": "773",
    "name": "Huyện Trà Cú",
    "code": "849",
    "parent_id": "59",
    "slug": "huyen tra cu"
  },
  "774": {
    "id": "774",
    "name": "Thành phố Trà Vinh",
    "code": "842",
    "parent_id": "59",
    "slug": "thanh pho tra vinh"
  },
  "775": {
    "id": "775",
    "name": "Thị xã Duyên Hải",
    "code": "851",
    "parent_id": "59",
    "slug": "thi xa duyen hai"
  },
  "776": {
    "id": "776",
    "name": "Huyện Chiêm Hóa",
    "code": "073",
    "parent_id": "60",
    "slug": "huyen chiem hoa"
  },
  "777": {
    "id": "777",
    "name": "Huyện Hàm Yên",
    "code": "074",
    "parent_id": "60",
    "slug": "huyen ham yen"
  },
  "778": {
    "id": "778",
    "name": "Huyện Lâm Bình",
    "code": "071",
    "parent_id": "60",
    "slug": "huyen lam binh"
  },
  "779": {
    "id": "779",
    "name": "Huyện Nà Hang",
    "code": "072",
    "parent_id": "60",
    "slug": "huyen na hang"
  },
  "780": {
    "id": "780",
    "name": "Huyện Sơn Dương",
    "code": "076",
    "parent_id": "60",
    "slug": "huyen son duong"
  },
  "781": {
    "id": "781",
    "name": "Huyện Yên Sơn",
    "code": "075",
    "parent_id": "60",
    "slug": "huyen yen son"
  },
  "782": {
    "id": "782",
    "name": "Thành phố Tuyên Quang",
    "code": "070",
    "parent_id": "60",
    "slug": "thanh pho tuyen quang"
  },
  "783": {
    "id": "783",
    "name": "Huyện Bình Tân",
    "code": "863",
    "parent_id": "61",
    "slug": "huyen binh tan"
  },
  "784": {
    "id": "784",
    "name": "Huyện Long Hồ",
    "code": "857",
    "parent_id": "61",
    "slug": "huyen long ho"
  },
  "785": {
    "id": "785",
    "name": "Huyện Mang Thít",
    "code": "858",
    "parent_id": "61",
    "slug": "huyen mang thit"
  },
  "786": {
    "id": "786",
    "name": "Huyện Tam Bình",
    "code": "860",
    "parent_id": "61",
    "slug": "huyen tam binh"
  },
  "787": {
    "id": "787",
    "name": "Huyện Trà Ôn",
    "code": "862",
    "parent_id": "61",
    "slug": "huyen tra on"
  },
  "788": {
    "id": "788",
    "name": "Huyện Vũng Liêm",
    "code": "859",
    "parent_id": "61",
    "slug": "huyen vung liem"
  },
  "789": {
    "id": "789",
    "name": "Thành phố Vĩnh Long",
    "code": "855",
    "parent_id": "61",
    "slug": "thanh pho vinh long"
  },
  "790": {
    "id": "790",
    "name": "Thị xã Bình Minh",
    "code": "861",
    "parent_id": "61",
    "slug": "thi xa binh minh"
  },
  "791": {
    "id": "791",
    "name": "Huyện Bình Xuyên",
    "code": "249",
    "parent_id": "62",
    "slug": "huyen binh xuyen"
  },
  "792": {
    "id": "792",
    "name": "Huyện Lập Thạch",
    "code": "246",
    "parent_id": "62",
    "slug": "huyen lap thach"
  },
  "793": {
    "id": "793",
    "name": "Huyện Sông Lô",
    "code": "253",
    "parent_id": "62",
    "slug": "huyen song lo"
  },
  "794": {
    "id": "794",
    "name": "Huyện Tam Đảo",
    "code": "248",
    "parent_id": "62",
    "slug": "huyen tam dao"
  },
  "795": {
    "id": "795",
    "name": "Huyện Tam Dương",
    "code": "247",
    "parent_id": "62",
    "slug": "huyen tam duong"
  },
  "796": {
    "id": "796",
    "name": "Huyện Vĩnh Tường",
    "code": "252",
    "parent_id": "62",
    "slug": "huyen vinh tuong"
  },
  "797": {
    "id": "797",
    "name": "Huyện Yên Lạc",
    "code": "251",
    "parent_id": "62",
    "slug": "huyen yen lac"
  },
  "798": {
    "id": "798",
    "name": "Thành phố Vĩnh Yên",
    "code": "243",
    "parent_id": "62",
    "slug": "thanh pho vinh yen"
  },
  "799": {
    "id": "799",
    "name": "Thị xã Phúc Yên",
    "code": "244",
    "parent_id": "62",
    "slug": "thi xa phuc yen"
  },
  "800": {
    "id": "800",
    "name": "Huyện Lục Yên",
    "code": "135",
    "parent_id": "63",
    "slug": "huyen luc yen"
  },
  "801": {
    "id": "801",
    "name": "Huyện Mù Căng Chải",
    "code": "137",
    "parent_id": "63",
    "slug": "huyen mu cang chai"
  },
  "802": {
    "id": "802",
    "name": "Huyện Trạm Tấu",
    "code": "139",
    "parent_id": "63",
    "slug": "huyen tram tau"
  },
  "803": {
    "id": "803",
    "name": "Huyện Trấn Yên",
    "code": "138",
    "parent_id": "63",
    "slug": "huyen tran yen"
  },
  "804": {
    "id": "804",
    "name": "Huyện Văn Chấn",
    "code": "140",
    "parent_id": "63",
    "slug": "huyen van chan"
  },
  "805": {
    "id": "805",
    "name": "Huyện Văn Yên",
    "code": "136",
    "parent_id": "63",
    "slug": "huyen van yen"
  },
  "806": {
    "id": "806",
    "name": "Huyện Yên Bình",
    "code": "141",
    "parent_id": "63",
    "slug": "huyen yen binh"
  },
  "807": {
    "id": "807",
    "name": "Thành phố Yên Bái",
    "code": "132",
    "parent_id": "63",
    "slug": "thanh pho yen bai"
  },
  "808": {
    "id": "808",
    "name": "Thị xã Nghĩa Lộ",
    "code": "133",
    "parent_id": "63",
    "slug": "thi xa nghia lo"
  }
}


if __name__ == '__main__':
    fixture_data = []
    for k in sorted(vn_areas):
        v = vn_areas[k]
        row = {
            "model": "backend.area",
            "pk": int(k),
            "fields": {
                "name": v['name'],
                "parent": int(v['parent_id']) if int(v['parent_id']) > 0 else None
            }
        }
        fixture_data.append(row)
    print(json.dumps(fixture_data, indent=4))
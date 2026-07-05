CATEGORY_DEPARTMENT_MAP = {
    "Yol ve kaldırım": "Fen İşleri Müdürlüğü",
    "Aydınlatma": "Aydınlatma ve Enerji İşleri",
    "Temizlik": "Temizlik İşleri Müdürlüğü",
    "Park ve yeşil alan": "Park ve Bahçeler Müdürlüğü",
    "Ulaşım": "Ulaşım Hizmetleri Müdürlüğü",
    "Gürültü": "Zabıta Müdürlüğü",
    "Güvenlik": "Zabıta Müdürlüğü",
    "Su ve altyapı": "Altyapı Koordinasyon Birimi",
    "Hayvanlar": "Veteriner İşleri Müdürlüğü",
    "Çevre kirliliği": "Çevre Koruma Müdürlüğü",
    "Diğer": "Çağrı Merkezi Ön İnceleme",
}


def route_department(category: str) -> dict:
    department = CATEGORY_DEPARTMENT_MAP.get(category, CATEGORY_DEPARTMENT_MAP["Diğer"])
    return {
        "department": department,
        "reason": f"{category} kategorisindeki talepler {department} birimine yönlendirilir.",
    }


if __name__ == "__main__":
    for item in CATEGORY_DEPARTMENT_MAP:
        print(item, "=>", route_department(item)["department"])

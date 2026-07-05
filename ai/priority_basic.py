HIGH_PRIORITY_KEYWORDS = [
    "acil",
    "tehlike",
    "tehlikeli",
    "kaza",
    "yangın",
    "yaralı",
    "patlak",
    "çöktü",
    "çukur",
    "elektrik kaçağı",
    "su bastı",
    "okul önü",
    "çocuklar",
    "karanlık",
]

MEDIUM_PRIORITY_KEYWORDS = [
    "3 gündür",
    "bir haftadır",
    "dolmuş",
    "aksıyor",
    "koku",
    "rahatsız",
    "bozuk",
    "kırık",
]

TURKISH_TRANSLATION = str.maketrans(
    {
        "ç": "c",
        "ğ": "g",
        "ı": "i",
        "ö": "o",
        "ş": "s",
        "ü": "u",
        "Ç": "c",
        "Ğ": "g",
        "İ": "i",
        "I": "i",
        "Ö": "o",
        "Ş": "s",
        "Ü": "u",
    }
)


def calculate_priority(text: str, category: str | None = None) -> dict:
    normalized = text.casefold()
    ascii_normalized = normalized.translate(TURKISH_TRANSLATION)
    high_hits = [
        keyword
        for keyword in HIGH_PRIORITY_KEYWORDS
        if keyword in normalized or keyword.casefold().translate(TURKISH_TRANSLATION) in ascii_normalized
    ]
    medium_hits = [
        keyword
        for keyword in MEDIUM_PRIORITY_KEYWORDS
        if keyword in normalized or keyword.casefold().translate(TURKISH_TRANSLATION) in ascii_normalized
    ]

    if high_hits:
        return {
            "priority_level": "Yüksek",
            "reason": "Öncelik yüksek seçildi; metinde risk/aciliyet belirten ifadeler var: " + ", ".join(high_hits[:3]) + ".",
        }

    if medium_hits or category in {"Temizlik", "Gürültü", "Ulaşım"}:
        reason = "Öncelik orta seçildi; talep takip gerektiren bir belediye hizmetiyle ilgili."
        if medium_hits:
            reason = "Öncelik orta seçildi; metinde tekrar/rahatsızlık belirten ifadeler var: " + ", ".join(medium_hits[:3]) + "."
        return {"priority_level": "Orta", "reason": reason}

    return {"priority_level": "Düşük", "reason": "Metinde acil risk veya tekrar vurgusu bulunmadığı için öncelik düşük seçildi."}

from dataclasses import dataclass


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


@dataclass(frozen=True)
class KeywordRule:
    keyword: str
    sub_category: str
    weight: int = 1


CATEGORY_RULES: dict[str, list[KeywordRule]] = {
    "Yol ve kaldırım": [
        KeywordRule("çukur", "Yol çukuru", 3),
        KeywordRule("kaldırım", "Kaldırım arızası", 2),
        KeywordRule("asfalt", "Asfalt bakım ihtiyacı", 2),
        KeywordRule("yol bozuk", "Yol bakım ihtiyacı", 3),
        KeywordRule("mazgal", "Mazgal sorunu", 2),
        KeywordRule("yol", "Yol bakım ihtiyacı", 1),
    ],
    "Aydınlatma": [
        KeywordRule("sokak lambası", "Sokak lambası arızası", 4),
        KeywordRule("lamba", "Sokak lambası arızası", 2),
        KeywordRule("yanmıyor", "Sokak lambası arızası", 3),
        KeywordRule("karanlık", "Yetersiz aydınlatma", 2),
        KeywordRule("aydınlatma", "Yetersiz aydınlatma", 2),
        KeywordRule("elektrik direği", "Aydınlatma ekipmanı", 2),
    ],
    "Temizlik": [
        KeywordRule("çöp", "Çöp birikmesi", 3),
        KeywordRule("konteyner", "Çöp konteyneri", 3),
        KeywordRule("temizlik", "Sokak temizliği", 2),
        KeywordRule("atık", "Atık toplama", 2),
        KeywordRule("pis", "Sokak temizliği", 1),
        KeywordRule("koku", "Kötü koku", 1),
    ],
    "Park ve yeşil alan": [
        KeywordRule("park", "Park bakım ihtiyacı", 3),
        KeywordRule("salıncak", "Oyun alanı arızası", 3),
        KeywordRule("oyun alanı", "Oyun alanı arızası", 3),
        KeywordRule("ağaç", "Ağaç bakımı", 2),
        KeywordRule("çim", "Yeşil alan bakımı", 2),
        KeywordRule("yeşil alan", "Yeşil alan bakımı", 2),
    ],
    "Ulaşım": [
        KeywordRule("otobüs", "Toplu taşıma seferi", 3),
        KeywordRule("durak", "Durak sorunu", 3),
        KeywordRule("sefer", "Sefer aksaması", 3),
        KeywordRule("trafik", "Trafik düzeni", 2),
        KeywordRule("minibüs", "Toplu taşıma düzeni", 2),
        KeywordRule("yolcu", "Toplu taşıma hizmeti", 1),
    ],
    "Gürültü": [
        KeywordRule("gürültü", "Gürültü şikayeti", 3),
        KeywordRule("yüksek ses", "Yüksek ses şikayeti", 3),
        KeywordRule("müzik", "Müzik gürültüsü", 2),
        KeywordRule("gece", "Gece gürültüsü", 1),
        KeywordRule("inşaat sesi", "İnşaat gürültüsü", 3),
        KeywordRule("rahatsız", "Rahatsızlık bildirimi", 1),
    ],
    "Güvenlik": [
        KeywordRule("güvenlik", "Güvenlik riski", 4),
        KeywordRule("tehlike", "Güvenlik riski", 4),
        KeywordRule("kavga", "Asayiş bildirimi", 4),
        KeywordRule("risk", "Güvenlik riski", 3),
        KeywordRule("güvensiz", "Güvenlik riski", 4),
        KeywordRule("madde", "Asayiş bildirimi", 1),
    ],
    "Su ve altyapı": [
        KeywordRule("su", "Su arızası", 1),
        KeywordRule("lağım", "Kanalizasyon arızası", 3),
        KeywordRule("kanalizasyon", "Kanalizasyon arızası", 3),
        KeywordRule("rögar", "Rögar sorunu", 3),
        KeywordRule("altyapı", "Altyapı arızası", 2),
        KeywordRule("patlak", "Su borusu arızası", 2),
    ],
    "Hayvanlar": [
        KeywordRule("sokak hayvanı", "Sokak hayvanı bildirimi", 3),
        KeywordRule("yaralı hayvan", "Yaralı hayvan", 4),
        KeywordRule("köpek", "Sokak hayvanı bildirimi", 2),
        KeywordRule("kedi", "Sokak hayvanı bildirimi", 2),
        KeywordRule("mama", "Besleme noktası", 1),
        KeywordRule("veteriner", "Veteriner desteği", 2),
    ],
    "Çevre kirliliği": [
        KeywordRule("çevre", "Çevre kirliliği", 2),
        KeywordRule("kirlilik", "Çevre kirliliği", 3),
        KeywordRule("dere", "Dere kirliliği", 2),
        KeywordRule("hava", "Hava kirliliği", 1),
        KeywordRule("kimyasal", "Tehlikeli atık", 3),
        KeywordRule("moloz", "Moloz/kaçak döküm", 2),
    ],
}


def normalize_for_match(value: str) -> str:
    return value.casefold().translate(TURKISH_TRANSLATION).strip()


def classify_ticket(text: str) -> dict:
    normalized = text.casefold().strip()
    ascii_normalized = normalize_for_match(text)
    scores: dict[str, int] = {}
    matches: dict[str, list[KeywordRule]] = {}

    for category, rules in CATEGORY_RULES.items():
        for rule in rules:
            keyword = rule.keyword.casefold()
            ascii_keyword = normalize_for_match(rule.keyword)
            if keyword in normalized or ascii_keyword in ascii_normalized:
                scores[category] = scores.get(category, 0) + rule.weight
                matches.setdefault(category, []).append(rule)

    if not scores:
        return {
            "category": "Diğer",
            "sub_category": "Ön inceleme",
            "confidence_score": 0.35,
            "reason": "Metinde tanımlı kategori anahtar kelimeleri bulunmadığı için kayıt ön incelemeye alındı.",
        }

    category = max(scores, key=scores.get)
    category_matches = matches[category]
    sub_category = max(category_matches, key=lambda item: item.weight).sub_category
    confidence_score = min(0.95, 0.45 + (scores[category] * 0.08))
    keywords = ", ".join(rule.keyword for rule in category_matches[:4])

    return {
        "category": category,
        "sub_category": sub_category,
        "confidence_score": round(confidence_score, 2),
        "reason": f"Metinde {keywords} ifadeleri geçtiği için {category} kategorisi seçildi.",
    }


if __name__ == "__main__":
    examples = [
        "Mahallemizdeki sokak lambası 3 gündür yanmıyor.",
        "Yolda büyük bir çukur var, araçlar zarar görüyor.",
        "Çöp konteynerleri dolmuş ve kötü koku yayıyor.",
    ]
    for example in examples:
        print(example, "=>", classify_ticket(example))

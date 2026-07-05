# API Sözleşmesi

## POST /tickets Request

```json
{
  "citizen_name": "Semih Bekdaş",
  "description": "Mahallemizdeki sokak lambası 3 gündür yanmıyor, akşamları sokak çok karanlık oluyor.",
  "district": "Kadıköy",
  "neighborhood": "Caferağa",
  "address": "Moda Caddesi 12. Sokak",
  "request_type": "Şikayet"
}
```

## POST /tickets Response

```json
{
  "id": 1,
  "citizen_name": "Semih Bekdaş",
  "description": "Mahallemizdeki sokak lambası 3 gündür yanmıyor, akşamları sokak çok karanlık oluyor.",
  "district": "Kadıköy",
  "neighborhood": "Caferağa",
  "address": "Moda Caddesi 12. Sokak",
  "request_type": "Şikayet",
  "category": "Aydınlatma",
  "sub_category": "Sokak lambası arızası",
  "department": "Aydınlatma ve Enerji İşleri",
  "confidence_score": 0.91,
  "priority_level": "Yüksek",
  "ai_reason": "Metinde sokak lambası, yanmıyor ve karanlık ifadeleri geçtiği için Aydınlatma kategorisi seçildi.",
  "status": "Yeni",
  "created_at": "2026-07-01T20:15:00",
  "updated_at": "2026-07-01T20:15:00"
}
```

## GET /tickets Response

```json
[
  {
    "id": 1,
    "description": "Mahallemizdeki sokak lambası 3 gündür yanmıyor...",
    "category": "Aydınlatma",
    "department": "Aydınlatma ve Enerji İşleri",
    "district": "Kadıköy",
    "neighborhood": "Caferağa",
    "priority_level": "Yüksek",
    "status": "Yeni",
    "created_at": "2026-07-01T20:15:00",
    "updated_at": "2026-07-01T20:15:00"
  }
]
```

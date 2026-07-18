# ŞehirPulse AI Backend

FastAPI tabanlı ticket API'sidir. Vatandaş talebini doğrular, AI modülü ile kategori/birim/öncelik analizi yapar, SQLite veritabanına kaydeder ve admin paneli için okuma endpointleri sunar.

## Kurulum

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Varsayilan API adresi: `http://localhost:8000`

Swagger: `http://localhost:8000/docs`

## Endpointler

| Method | Path | Aciklama |
| --- | --- | --- |
| GET | `/health` | Backend calisiyor mu kontrol eder. |
| POST | `/tickets` | Yeni talep olusturur ve AI sonucunu kaydeder. |
| GET | `/tickets` | Talepleri yeni kayittan eskiye listeler. |
| GET | `/tickets/{id}` | Tek talep detayini dondurur. |

Durum veya öncelik güncelleyen bir endpoint henüz yoktur. `PATCH /tickets/{id}` akışı Sprint 3 backlog'unda P0 olarak planlanmıştır.

## Ornek POST Body

```json
{
  "citizen_name": "Anonim",
  "description": "Mahallemizdeki sokak lambasi 3 gundur yanmiyor.",
  "district": "Kadikoy",
  "neighborhood": "Caferaga",
  "address": "Moda Caddesi",
  "request_type": "Sikayet"
}
```

## Ortam Degiskenleri

| Degisken | Varsayilan | Aciklama |
| --- | --- | --- |
| `DATABASE_URL` | `sqlite:///./sehirpulse.db` | SQLAlchemy veritabani adresi. |
| `FRONTEND_ORIGINS` | `http://localhost:5173,http://localhost:3000` | CORS izinli frontend adresleri. |

## Doğrulama

Sprint 2 smoke kontrolünde şu senaryolar başarıyla çalıştırılmıştır:

- `GET /health`
- `POST /tickets`
- `GET /tickets`
- `GET /tickets/{id}`
- Geçersiz ID için `404`

Kalıcı otomatik test dosyaları ve CI Sprint 3 planındadır.

# SehirPulse AI Backend

FastAPI tabanli ticket API. Sprint 1 kapsaminda vatandas talebini kaydeder, AI modulu ile kategori/birim tahmini yapar ve admin paneli icin listeleme endpointleri sunar.

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

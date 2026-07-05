# SehirPulse AI - Sprint 1 Uygulama Plani

## 1. Urun Ozeti

SehirPulse AI, vatandaslardan gelen talep, sikayet ve ihbarlari otomatik siniflandiran, ilgili belediye birimine yonlendiren ve belediye yetkililerine admin panelinden takip imkani veren bir MVP'dir.

Sprint 1 icin hedef kusursuz urun degil, uctan uca calisan temel akistir:

1. Vatandas `/report` sayfasindan talep girer.
2. Frontend `POST /tickets` ile backend'e veri yollar.
3. Backend aciklama metnini AI modulune verir.
4. AI kategori, alt kategori, ilgili birim ve guven skoru dondurur.
5. Backend ticket kaydini veritabanina yazar.
6. Admin `/admin/tickets` sayfasinda kayitlari listeler.

## 2. MVP Sinirlari

### Sprint 1'de yapilacaklar

- Talep formu.
- Ticket kaydetme API'si.
- Ticket listeleme API'si.
- Tek ticket getirme API'si.
- Kural tabanli AI kategori tahmini.
- Kategoriye gore belediye birimi routing'i.
- Admin ticket listesi.
- Scrum ve teslim dokumantasyonu.

### Sprint 1'de yapilmayacaklar

- Gercek kullanici hesabi ve yetkilendirme.
- Canli deployment.
- Gelismis harita/heatmap.
- Embedding tabanli benzer talep gruplama.
- Gelismis aciliyet skoru.
- LLM agent orkestrasyonu.

## 3. Mimari

```text
frontend/
  /report -> POST /tickets
  /admin/tickets -> GET /tickets

backend/
  FastAPI
  SQLAlchemy
  SQLite
  ai_adapter.py

ai/
  classify.py
  routing.py
  data/category_department_mapping.csv
  data/sample_tickets_tr.csv
```

## 4. Veri Modeli

Ticket alanlari:

- `id`: integer, otomatik.
- `citizen_name`: string, opsiyonel, bos ise `Anonim`.
- `description`: text, zorunlu.
- `district`: string, zorunlu.
- `neighborhood`: string, zorunlu.
- `address`: string, opsiyonel.
- `request_type`: string, `Talep`, `Sikayet` veya `Ihbar`.
- `category`: string, AI tahmini.
- `sub_category`: string, opsiyonel.
- `department`: string, routing sonucu.
- `confidence_score`: float, opsiyonel.
- `status`: string, varsayilan `Yeni`.
- `created_at`: datetime.
- `updated_at`: datetime.

## 5. API Sozlesmesi

### `GET /health`

Basarili yanit:

```json
{
  "status": "ok"
}
```

### `POST /tickets`

Request:

```json
{
  "citizen_name": "Semih Bekdas",
  "description": "Mahallemizdeki sokak lambasi 3 gundur yanmiyor.",
  "district": "Kadikoy",
  "neighborhood": "Caferaga",
  "address": "Moda Caddesi 12. Sokak",
  "request_type": "Sikayet"
}
```

Response `201`:

```json
{
  "id": 1,
  "citizen_name": "Semih Bekdas",
  "description": "Mahallemizdeki sokak lambasi 3 gundur yanmiyor.",
  "district": "Kadikoy",
  "neighborhood": "Caferaga",
  "address": "Moda Caddesi 12. Sokak",
  "request_type": "Sikayet",
  "category": "Aydinlatma",
  "sub_category": "Sokak lambasi arizasi",
  "department": "Aydinlatma ve Enerji Isleri",
  "confidence_score": 0.91,
  "status": "Yeni",
  "created_at": "2026-07-01T20:15:00"
}
```

### `GET /tickets`

Response `200`:

```json
[
  {
    "id": 1,
    "description": "Mahallemizdeki sokak lambasi 3 gundur yanmiyor.",
    "category": "Aydinlatma",
    "department": "Aydinlatma ve Enerji Isleri",
    "district": "Kadikoy",
    "neighborhood": "Caferaga",
    "status": "Yeni",
    "created_at": "2026-07-01T20:15:00"
  }
]
```

### `GET /tickets/{id}`

- Gecerli ID: ticket detayi.
- Gecersiz ID: `404`, `Talep bulunamadi.`

## 6. AI Kategori Plani

Sprint 1 karar: once rule-based.

Baslangic kategorileri:

- Yol ve kaldirim -> Fen Isleri Mudurlugu.
- Aydinlatma -> Aydinlatma ve Enerji Isleri.
- Temizlik -> Temizlik Isleri Mudurlugu.
- Park ve yesil alan -> Park ve Bahceler Mudurlugu.
- Ulasim -> Ulasim Hizmetleri Mudurlugu.
- Gurultu -> Zabita Mudurlugu.
- Guvenlik -> Zabita Mudurlugu.
- Su ve altyapi -> Altyapi Koordinasyon Birimi.
- Hayvanlar -> Veteriner Isleri Mudurlugu.
- Cevre kirliligi -> Cevre Koruma Mudurlugu.
- Diger -> Cagri Merkezi On Inceleme.

AI fonksiyon ciktilari:

```python
{
    "category": "Aydinlatma",
    "sub_category": "Sokak lambasi arizasi",
    "confidence_score": 0.91,
    "reason": "Metinde sokak lambasi ve yanmiyor ifadeleri gecti."
}
```

Routing fonksiyon ciktilari:

```python
{
    "department": "Aydinlatma ve Enerji Isleri",
    "reason": "Aydinlatma kategorisindeki talepler bu birime yonlendirilir."
}
```

## 7. Gun Gun Uygulama Sirası

| Gun | Takim hedefi | Cikti |
| --- | --- | --- |
| 1 | Baslangic ve kapsam | Repo iskeleti, README, kategori taslagi |
| 2 | Backlog ve sozlesme | Product backlog, issue/PR template, keyword listesi |
| 3 | Teknik iskelet | Frontend kurulumu, FastAPI kurulumu, ilk veri seti |
| 4 | Ilk ekran ve DB | Talep formu UI, DB modeli, 150 satira yaklasan veri |
| 5 | Ilk create akisi | Form validasyonu, `POST /tickets`, `classify_ticket` |
| 6 | Listeleme akisi | Form API baglantisi, `GET /tickets`, routing |
| 7 | Ilk entegrasyon | Admin liste UI, `GET /tickets/{id}`, AI testleri |
| 8 | AI-backend baglantisi | Admin liste gercek API, `ai_adapter.py` |
| 9 | Stabilizasyon | Loading/hata durumlari, CORS, yanlis tahmin duzeltmeleri |
| 10 | Demo akisi | Demo ekranlari, API hata yonetimi, demo ornekleri |
| 11 | Test ve dokuman | Ekran goruntuleri, API testleri, AI README |
| 12 | Review hazirligi | Sprint review taslagi, AI karar mantigi |
| 13 | Bug fix | PR temizligi, UI/backend/AI duzeltmeleri |
| 14 | Teslim | Review, retrospective, demo prova |

## 8. Test Plani

- T-01: Bos aciklama ile form gonderilememeli.
- T-02: Gecerli talep backend'e kaydedilmeli.
- T-03: `POST /tickets` Swagger/HTTP testi `201` donmeli.
- T-04: `GET /tickets` liste donmeli.
- T-05: "sokak lambasi yanmiyor" metni `Aydinlatma` donmeli.
- T-06: "yolda buyuk cukur var" metni `Yol ve kaldirim` donmeli.
- T-07: Yeni talep admin listesinde gorunmeli.
- T-08: Ticket kaydinda `category` ve `department` dolu olmali.

## 9. Definition of Done

- Ilgili is icin issue acik.
- Is ayri branch'te yapilmis.
- Kod lokal calisiyor.
- Backend isi Swagger veya HTTP client ile test edilmis.
- Frontend isi ekran goruntusuyle dogrulanmis.
- AI isi en az 5 ornek metinle denenmis.
- Dokumantasyon guncellenmis.
- PR acilmis, review alinmis ve merge sonrasi issue kapatilmis.

## 10. Baslangic Onceligi

Once proje iskeleti ve sozlesmeler tamamlanmali. Kodlamaya baslarken en verimli sira:

1. Klasor yapisi, README, `.gitignore`, docs sablonlari.
2. AI kategori mapping dosyasi.
3. Backend FastAPI iskeleti ve `/health`.
4. Ticket veri modeli.
5. `POST /tickets`.
6. Frontend `/report` formu.
7. `GET /tickets` ve admin liste.
8. AI-backend entegrasyonu.
9. Entegrasyon testleri ve demo dokumanlari.

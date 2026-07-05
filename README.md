# ŞehirPulse AI

ŞehirPulse AI, vatandaşlardan gelen talep, şikayet ve ihbarları otomatik sınıflandıran, ilgili belediye birimine yönlendiren ve admin panelinde görünür hale getiren Sprint 1 MVP projesidir.

## Bootcamp Notu

Bu repository, Yapay Zeka ve Teknoloji Akademisi Bootcamp 2026 sürecindeki proje yönetimi beklentilerine göre düzenlenmiştir. Bootcamp kılavuzunda standart ekip yapısı 5 kişi olarak belirtilse de, ekipten ayrılan/aktif devam etmeyen üyeler sonrası proje 3 aktif kişiyle sürdürülmektedir. Kılavuzda belirtildiği gibi Product Owner ve Scrum Master rolleri yalnızca süreç yönetimi değil, aktif geliştirme sorumluluğu da alır.

| Aktif Kişi | Scrum Rolü | Geliştirme Sorumluluğu |
| --- | --- | --- |
| Kişi 1 | Product Owner | Ürün kapsamı, backlog, frontend form ve admin ekranı |
| Kişi 2 | Scrum Master | İletişim, repo düzeni, FastAPI backend ve entegrasyon |
| Kişi 3 | Developer | AI/data modülü, kategori tahmini, routing ve test verisi |

## Sprint 1 Hedefi

Sprint sonunda çalışan temel akış hazırdır:

```text
Vatandaş talep formunu doldurur
Frontend POST /tickets isteği gönderir
Backend talebi AI modülüne analiz ettirir
AI kategori, alt kategori, birim ve öncelik üretir
Backend talebi SQLite veritabanına kaydeder
Admin paneli GET /tickets ile talepleri listeler
```

## Teknoloji Seti

| Katman | Teknoloji | Amaç |
| --- | --- | --- |
| Frontend | React + Vite | Talep formu ve admin liste ekranı |
| Backend | FastAPI | Ticket API ve AI entegrasyonu |
| Veritabanı | SQLite + SQLAlchemy | Sprint 1 lokal veri kaydı |
| AI | Python rule-based modüller | Kategori, routing ve temel öncelik |
| Dokümantasyon | Markdown | Backlog, sprint planı, review, retrospective |

## Klasör Yapısı

```text
.
├── ai/
│   ├── data/
│   ├── classify.py
│   ├── priority_basic.py
│   └── routing.py
├── backend/
│   ├── app/
│   └── requirements.txt
├── frontend/
│   ├── src/
│   └── package.json
├── docs/
├── screenshots/
└── README.md
```

## Hızlı Başlangıç

Backend:

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Frontend:

```bash
cd frontend
npm install
npm run dev
```

Adresler:

| Servis | URL |
| --- | --- |
| Frontend | `http://localhost:5173/report` |
| Admin Panel | `http://localhost:5173/admin/tickets` |
| Backend API | `http://localhost:8000` |
| Swagger | `http://localhost:8000/docs` |

## Demo Senaryosu

1. Backend ve frontend çalıştırılır.
2. `/report` ekranında örnek talep girilir: `Mahallemizdeki sokak lambası 3 gündür yanmıyor.`
3. Form gönderilir.
4. Backend talebi kaydeder ve AI sonucu üretir.
5. `/admin/tickets` ekranında talep `Aydınlatma` kategorisi ve `Aydınlatma ve Enerji İşleri` birimiyle görünür.

## Ana API Endpointleri

| Method | Path | Açıklama |
| --- | --- | --- |
| GET | `/health` | API sağlık kontrolü |
| POST | `/tickets` | Yeni talep oluşturma |
| GET | `/tickets` | Talepleri listeleme |
| GET | `/tickets/{id}` | Tek talep detayı |

## Sprint 1 Dokümanları

| Dosya | İçerik |
| --- | --- |
| `docs/product-definition.md` | Ürün tanımı, hedef kitle, MVP sınırı |
| `docs/product-backlog.md` | User story ve issue listesi |
| `docs/sprint-1.md` | Gün gün sprint uygulama planı |
| `docs/daily-notes.md` | Daily toplantı şablonu ve örnek notlar |
| `docs/sprint-review-1.md` | Review akışı ve demo notları |
| `docs/retrospective-1.md` | Retrospective şablonu |
| `docs/demo-notes.md` | Final demo konuşma planı |
| `docs/test-report.md` | Lokal doğrulama komutları ve sonuçları |
| `docs/bootcamp-compliance.md` | Bootcamp kılavuzu uyum kontrolü |

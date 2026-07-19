# Takım İsmi

Takım 124

---

# Ürün ile İlgili Bilgiler

## Takım Elemanları

- UmutCan Özgül – Product Owner
- Eren Altunay– Scrum Master
- Semih Bekdaş– Developer

## Ürün İsmi

**ŞehirPulse AI**

## Ürün Açıklaması

ŞehirPulse AI, vatandaşların şehir yaşamında karşılaştıkları sorunları (trafik, altyapı, çevre vb.) bildirebildiği, yapay zekâ destekli öneri ve önceliklendirme sistemiyle bu bildirimleri ilgili birimlere yönlendiren dijital bir platformdur. Proje, bir bootcamp bitirme projesi kapsamında Scrum metodolojisiyle geliştirilmektedir.

## Ürün Özellikleri

- Kullanıcıların şehir sorunlarını (kategori, konum, açıklama ile) bildirebilmesi
- AI destekli kategori ve öncelik önerisi
- Admin panelinden bildirimlerin görüntülenmesi, durum ve önceliklerinin güncellenmesi
- Swagger üzerinden API dokümantasyonu

## Hedef Kitle

- Şehir sakinleri
- Belediye/yerel yönetim birimleri
- Şehir altyapı ve hizmet takip ekipleri

## Product Backlog URL

[Miro Backlog Board]()

---

# Sprint 1

**Sprint Notu:** Bu proje, bootcamp bitirme projesi olarak Scrum süreciyle geliştirilmiştir. 1 haftalık sprint döngüsünde ürün backlog'u önceliklendirilerek geliştirme yapılmıştır.

**Tahmin Edilen Puan Tamamlanma Mantığı:** Sprint hedefine ulaşmak için gereken görevler backlog'dan seçilerek story point ile önceliklendirilmiştir.

**Daily Scrum:** Daily Scrum toplantıları takım içi iletişim kanalı üzerinden metin ve/veya sesli olarak, günlük olarak gerçekleştirilmiştir. Daily Scrum kayıtlarına [buradan]() ulaşılabilir.

## Uygulama Ekran Görüntüleri

Sprint 1 sonunda, planlanan MVP uçtan uca çalışır durumdadır. Aşağıda uygulamanın gerçek ekran görüntüleri yer almaktadır.

**Talep Formu**
![Talep Formu](docs/screenshots/report-form.png)

**Admin Paneli**
![Admin Paneli](docs/screenshots/admin-ticket-list.png)

---

## Sprint Hedefi

```
Kullanıcıların şehir sorunlarını bildirebileceği, AI destekli
öneri sistemine sahip MVP'nin geliştirilmesi.
```

## Teknoloji Seti

| Katman        | Teknoloji                   | Amaç                                      |
| ------------- | --------------------------- | ----------------------------------------- |
| Frontend      | React + Vite                | Hızlı ve modern kullanıcı arayüzü         |
| Backend       | FastAPI (Python)            | Hızlı ve hafif API sunucusu               |
| Veritabanı    | SQLite + SQLAlchemy         | Basit ilişkisel veritabanı ve ORM         |
| AI            | Python tabanlı öneri motoru | Kategori/öncelik öneri sistemi            |
| Dokümantasyon | Markdown                    | Raporlama, sprint planı, sunum içerikleri |

## Klasör Yapısı

```
sehirpulse-ai-main/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── ai_adapter.py
│   │   ├── models/
│   │   └── schemas/
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── components/
│   │   └── services/
│   └── package.json
├── ai/
│   └── ...
└── docs/
    └── screenshots/
```

## Hızlı Başlangıç

**Backend:**

```bash
cd backend
python -m venv .venv
.venv\Scripts\Activate.ps1      # macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

**Frontend:**

```bash
cd frontend
npm install
npm run dev
```

## Adresler

| Servis                       | URL                                 |
| ---------------------------- | ----------------------------------- |
| Frontend – Talep Formu       | http://localhost:5173/report        |
| Frontend – Admin Paneli      | http://localhost:5173/admin/tickets |
| Backend API                  | http://localhost:8000               |
| Swagger (API Dokümantasyonu) | http://localhost:8000/docs          |

## Demo Senaryosu

1. Kullanıcı arıza/sorun bildirir (kategori, konum, açıklama girer).
2. Form gönderilir.
3. Backend kaydı oluşturur ve AI servisi kategori/öncelik önerisi üretir.
4. Admin panelinden bildirimler görüntülenir; kategori, öncelik ve durum güncellenebilir.

## Ana API Endpointleri

| Method | Endpoint | Açıklama                                                 |
| ------ | -------- | -------------------------------------------------------- |
| GET    | /health  | API sağlık kontrolü                                      |
| GET    | /tickets | Tüm bildirimleri listeleme                               |
| POST   | /tickets | Yeni bildirim oluşturma (AI kategori/öncelik önerisiyle) |

## Sprint 1 Dokümanları

| Konu                                  | İçerik                                        |
| ------------------------------------- | --------------------------------------------- |
| Uygulama Ekran Görüntüleri            | Talep formu ve admin paneli ekran görüntüleri |
| User Story ve Backlog                 | Product backlog, user story listesi           |
| Ürün Planı ve Sprint Planlaması       | Sprint planlama dokümanı                      |
| Daily Scrum Kayıtları ve Retrospektif | Günlük toplantı notları, sprint retrospektif  |

---

## Sprint Review

_(Sprint 1 sonunda değerlendirilen kazanımlar, eksikler ve bir sonraki sprint için alınan kararlar buraya eklenecek.)_

## Sprint Retrospektif

_(Takımın süreç içinde iyi giden ve geliştirilmesi gereken noktalarına dair değerlendirmeler buraya eklenecek.)_

---

## Katkıda Bulunanlar

| İsim         | GitHub                                         |
| ------------ | ---------------------------------------------- |
| Semih Bekdaş | [@semihbekdas](https://github.com/semihbekdas) |
| Eren Altunay | [@EERREENN](https://github.com/EERREENN)       |
| Umut Can Özgül  | [@umutcanzgl](https://github.com/umutcanzgl)   |

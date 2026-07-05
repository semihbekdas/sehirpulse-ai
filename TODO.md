# SehirPulse AI - Sprint 1 Teslim Durumu

Bu dosya, `SehirPulse_AI_Sprint_1_Detayli_Plan (1).docx` belgesindeki Sprint 1 hedeflerinin uygulamadaki son durumunu takip eder.

## Sprint 1 Hedefi

Vatandas bir talep formu doldurur, frontend `POST /tickets` istegi gonderir, FastAPI backend talebi kaydeder, AI modulu kategori ve ilgili birimi tahmin eder, admin panelinde talep listelenir.

## Faz 0 - Proje Iskeleti ve Scrum Duzeni

- [x] Repo klasor yapisi olusturuldu: `frontend/`, `backend/`, `ai/`, `docs/`, `screenshots/`.
- [x] Koku aciklayan `README.md` dosyasi yazildi.
- [x] `.gitignore` eklendi.
- [x] `.github/ISSUE_TEMPLATE/` ve `.github/pull_request_template.md` eklendi.
- [x] `docs/product-definition.md` hazirlandi.
- [x] `docs/product-backlog.md` hazirlandi.
- [x] `docs/sprint-1.md` sprint hedefi, kapsam ve kabul kriterleriyle dolduruldu.
- [x] `docs/daily-notes.md` icin gunluk toplanti sablonu eklendi.

## Faz 1 - AI/Data Modulu

- [x] `ai/data/category_department_mapping.csv` dosyasi 11 kategoriyle olusturuldu.
- [x] `ai/data/sample_tickets_tr.csv` dosyasi 150 Turkce ornek taleple olusturuldu.
- [x] `ai/classify.py` icinde `classify_ticket(text: str) -> dict` fonksiyonu yazildi.
- [x] ASCII ve Turkce karakterli metinler icin dayanikli esleme eklendi.
- [x] `ai/routing.py` icinde `route_department(category: str) -> dict` fonksiyonu yazildi.
- [x] `ai/priority_basic.py` ile `Dusuk/Orta/Yuksek` oncelik tahmini eklendi.
- [x] Temel AI test metinleri calistirildi.
- [x] `ai/README.md` dosyasinda kategori mantigi, sinirliliklar ve ornek kullanimlar aciklandi.

## Faz 2 - Backend

- [x] `backend/app/main.py` ile FastAPI uygulamasi baslatildi.
- [x] `/health` endpointi eklendi.
- [x] `backend/app/database.py` ile SQLite/SQLAlchemy baglantisi kuruldu.
- [x] `backend/app/models/ticket.py` icinde Ticket modeli yazildi.
- [x] `backend/app/schemas/ticket.py` icinde request/response Pydantic semalari yazildi.
- [x] `backend/app/ai_adapter.py` ile AI fonksiyonlari backend'e baglandi.
- [x] `POST /tickets` endpointi yazildi.
- [x] `GET /tickets` endpointi yazildi.
- [x] `GET /tickets/{id}` endpointi yazildi.
- [x] CORS ayarlari frontend gelistirme adreslerine gore yapildi.
- [x] FastAPI TestClient ile endpoint smoke testleri calistirildi.

## Faz 3 - Frontend

- [x] `frontend/` React + Vite projesi kuruldu.
- [x] Sprint 1 icin ozel CSS tabanli responsive stil altyapisi eklendi.
- [x] `/report` sayfasinda vatandas talep formu UI'i olusturuldu.
- [x] Form alanlari eklendi: ad soyad, aciklama, ilce, mahalle, adres, talep turu.
- [x] Form validasyonlari eklendi: aciklama minimum 10 karakter, ilce/mahalle/talep turu zorunlu.
- [x] `POST /tickets` servis fonksiyonu yazildi.
- [x] Form gonderiminde loading, basari ve hata durumlari gosterildi.
- [x] `/admin/tickets` sayfasinda admin talep listesi UI'i olusturuldu.
- [x] `GET /tickets` servis fonksiyonu yazildi.
- [x] Admin listede ID, aciklama, kategori, ilgili birim, ilce/mahalle, oncelik, durum ve tarih gosterildi.
- [x] Admin listesi icin bos durum, loading ve hata durumlari eklendi.

## Faz 4 - Entegrasyon ve Demo

- [x] Backend create akisinda `category`, `sub_category`, `department`, `confidence_score` ve `priority_level` alanlari doluyor.
- [x] Yeni talebin admin listesi API'sinde gorundugu dogrulandi.
- [x] Demo icin guclu ornek talepler `docs/demo-notes.md` icinde hazirlandi.
- [x] `screenshots/README.md` ile ekran goruntusu teslim klasoru takip edilebilir hale getirildi.
- [x] `docs/sprint-review-1.md` demo akisi ve tamamlanan islerle dolduruldu.
- [x] `docs/retrospective-1.md` dolduruldu.
- [x] Frontend production build calistirildi.

## Kabul Kriterleri

- [x] Repo ve klasor yapisi duzenli.
- [x] README proje ozetini ve calistirma adimlarini iceriyor.
- [x] Product backlog ve sprint dokumanlari hazir.
- [x] Vatandas talep formu calisacak sekilde gelistirildi.
- [x] `POST /tickets` talep kaydediyor ve `201` donuyor.
- [x] `GET /tickets` talep listesini donuyor.
- [x] `GET /tickets/{id}` gecerli ID icin detay, hatali ID icin `404` donuyor.
- [x] AI kategori tahmini yapiyor.
- [x] AI routing sonucu backend kaydina ekleniyor.
- [x] Admin panelinde kaydedilen talepler gorunuyor.
- [x] Loading, hata ve bos durumlar temel seviyede ele alindi.
- [x] Sprint review ve retrospective dokumanlari hazir.

## Sprint 1 Disinda Kalacaklar

- Gelismis harita ve yogunluk analizi.
- Embedding ile benzer talep tespiti.
- Gelismis aciliyet skoru.
- AI agent orkestrasyonu.
- Canli deployment.
- Gercek kullanici hesap sistemi.

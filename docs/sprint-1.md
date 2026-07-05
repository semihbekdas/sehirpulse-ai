# Sprint 1 Planı

## Sprint Hedefi

Vatandaş talebi oluşturulabilen, backend'e kaydedilebilen, temel AI kategori/birim tahmini yapılabilen ve admin panelinde listelenebilen çalışan ilk ürün sürümünü ortaya çıkarmak.

## Takım Rolleri

Bootcamp kılavuzunda standart ekip yapısı Product Owner, Scrum Master ve 3 Developer olmak üzere 5 kişidir. Bu projede ekipten ayrılan/aktif devam etmeyen üyeler sonrası Sprint 1, 3 aktif kişiyle yürütülmüştür. Bu nedenle roller birleştirilmiş; Product Owner ve Scrum Master da aktif geliştirme sorumluluğu almıştır.

| Kişi | Rol | Ana Çıktı |
| --- | --- | --- |
| Kişi 1 | Product Owner + Frontend | Talep formu, admin liste, ürün dokümanları |
| Kişi 2 | Scrum Master + Backend | Repo düzeni, FastAPI API, veritabanı, sprint dokümanları |
| Kişi 3 | AI/Data | Kategori verisi, sınıflandırma, routing, AI README |

## Bootcamp Sprint Beklentileriyle Uyum

| Beklenti | Sprint 1 Karşılığı | Durum |
| --- | --- | --- |
| Product Backlog | `docs/product-backlog.md` | Tamamlandı |
| Daily Scrum Notları | `docs/daily-notes.md` | Tamamlandı |
| Sprint Board Updates | Issue listesi ve backlog tablosu | Hazır |
| Ürün Durumu | Çalışan frontend/backend/AI MVP | Hazır |
| Sprint Review | `docs/sprint-review-1.md` | Tamamlandı |
| Sprint Retrospective | `docs/retrospective-1.md` | Tamamlandı |

## Gün Gün Uygulama Planı

| Gün | Takım Hedefi | Kişi 1 | Kişi 2 | Kişi 3 |
| --- | --- | --- | --- | --- |
| 1 | Başlangıç ve kapsam | Ürün tanımı | Repo iskeleti | Kategori listesi |
| 2 | Backlog ve sözleşme | Product backlog | Issue/PR template | Keyword listesi |
| 3 | Teknik iskelet | Frontend kurulumu | FastAPI kurulumu | İlk veri seti |
| 4 | İlk ekran/model | Talep formu UI | DB ve model | Veri seti tamamlama |
| 5 | Create akışı | Validasyon | POST /tickets | classify_ticket |
| 6 | Listeleme akışı | Form API bağlantısı | GET /tickets | route_department |
| 7 | Entegrasyon | Admin UI | GET /tickets/{id} | AI testleri |
| 8 | AI-backend bağlantısı | Listeyi API'ye bağla | AI adapter | Output sözleşmesi |
| 9 | İyileştirme | Loading/error | CORS ve response | Yanlış tahmin düzeltme |
| 10 | Demo akışı | Ekran düzeni | Hata yönetimi | Demo örnekleri |
| 11 | Test/doküman | Ekran görüntüsü | API testleri | AI README |
| 12 | Review hazırlığı | Demo akışı | Review taslağı | Karar mantığı |
| 13 | Bug fix | UI düzeltmeleri | Merge/fix | AI fix |
| 14 | Review/retro | Demo sunumu | Scrum dokümanları | AI sunumu |

## Definition of Done

- İlgili iş backlog içinde yer alır.
- Kod lokal olarak çalışır.
- Backend işi Swagger veya curl ile test edilir.
- AI işi en az 5 örnek metinle test edilir.
- Frontend işi form/list ekranında denenir.
- Gerekli dokümantasyon güncellenir.
- Demo akışını bozacak hata kalmaz.

## Sprint 1 Kalite Kontrol Listesi

- [x] README proje özetini içeriyor.
- [x] `docs/product-definition.md` hazır.
- [x] `docs/product-backlog.md` hazır.
- [x] `docs/daily-notes.md` hazır.
- [x] Frontend talep formu geliştirildi.
- [x] Backend `POST /tickets` geliştirildi.
- [x] Backend `GET /tickets` geliştirildi.
- [x] AI kategori tahmini geliştirildi.
- [x] AI routing çıktısı backend kaydına bağlandı.
- [x] Admin liste ekranı geliştirildi.
- [x] Sprint review dokümanı hazır.
- [x] Retrospective dokümanı hazır.
- [x] Bootcamp kılavuzundaki sprint sonu kanıtları dokümante edildi.
- [x] Backend smoke test ve frontend production build doğrulandı.

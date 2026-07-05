# Product Backlog

## Sprint 1 User Story Listesi

| ID | User Story | Kabul Kriteri | Sorumlu | SP | Durum |
| --- | --- | --- | --- | --- | --- |
| US-01 | Bir vatandaş olarak belediyeye talep gönderebilmek istiyorum. | Formu doldurup başarılı mesajı görebilmeliyim. | Kişi 1 + Kişi 2 | 13 | Done |
| US-02 | Bir belediye yetkilisi olarak gelen talepleri listede görmek istiyorum. | Admin listesinde tüm talepler görünmeli. | Kişi 1 + Kişi 2 | 13 | Done |
| US-03 | Bir belediye yetkilisi olarak talebin kategorisini otomatik görmek istiyorum. | Her talepte kategori alanı dolu olmalı. | Kişi 3 + Kişi 2 | 13 | Done |
| US-04 | Bir belediye yetkilisi olarak talebin hangi birime gideceğini görmek istiyorum. | Her talepte department alanı dolu olmalı. | Kişi 3 | 8 | Done |
| US-05 | Bir takım üyesi olarak Sprint 1 ilerlemesini GitHub üzerinden takip etmek istiyorum. | Issue, branch ve PR düzeni kurulmalı. | Kişi 2 | 5 | Done |
| US-06 | Bir Product Owner olarak ürün kapsamını ve MVP sınırını dokümante etmek istiyorum. | Product definition ve backlog dosyaları hazır olmalı. | Kişi 1 | 8 | Done |

## Sprint 1 Issue Listesi

| Issue | Başlık | Çıktı | SP | Durum |
| --- | --- | --- | --- | --- |
| #1 | docs: ürün tanımı dokümanını oluştur | `docs/product-definition.md` | 3 | Done |
| #2 | docs: product backlog oluştur | `docs/product-backlog.md` | 5 | Done |
| #3 | chore: repo klasör yapısını kur | repo root | 3 | Done |
| #4 | docs: README ilk versiyonunu yaz | `README.md` | 3 | Done |
| #5 | chore: issue ve PR template ekle | `.github/` | 2 | Done |
| #6 | feat: frontend proje kurulumunu yap | `frontend/` | 3 | Done |
| #7 | feat: backend FastAPI kurulumunu yap | `backend/` | 3 | Done |
| #8 | data: kategori-birim eşleme tablosunu oluştur | `ai/data/category_department_mapping.csv` | 5 | Done |
| #9 | data: örnek Türkçe talep veri setini oluştur | `ai/data/sample_tickets_tr.csv` | 8 | Done |
| #10 | feat: talep formu UI geliştir | `/report` | 8 | Done |
| #11 | feat: Ticket veritabanı modelini yaz | `models/ticket.py` | 5 | Done |
| #12 | feat: classify_ticket fonksiyonunu yaz | `ai/classify.py` | 8 | Done |
| #13 | feat: route_department fonksiyonunu yaz | `ai/routing.py` | 5 | Done |
| #14 | feat: POST /tickets endpointini yaz | `POST /tickets` | 8 | Done |
| #15 | feat: formu POST /tickets endpointine bağla | frontend service | 5 | Done |
| #16 | feat: GET /tickets endpointini yaz | `GET /tickets` | 5 | Done |
| #17 | feat: admin ticket listesi UI geliştir | `/admin/tickets` | 8 | Done |
| #18 | feat: admin listeyi backend verisine bağla | `/admin/tickets` | 5 | Done |
| #19 | feat: AI modülünü backend create akışına bağla | `ai_adapter.py` | 8 | Done |
| #20 | test: API temel testlerini yap | FastAPI TestClient smoke test | 3 | Done |
| #21 | test: AI örnek metin testlerini yap | 3 örnek metin + 150 satır veri kontrolü | 3 | Done |
| #22 | fix: frontend hata/loading durumlarını düzenle | UI | 3 | Done |
| #23 | docs: sprint review 1 dokümanını hazırla | `docs/sprint-review-1.md` | 5 | Done |
| #24 | docs: retrospective 1 dokümanını hazırla | `docs/retrospective-1.md` | 3 | Done |
| #25 | demo: Sprint 1 demo senaryosunu hazırla | `docs/demo-notes.md` | 3 | Done |

## Önceliklendirme

| Öncelik | İş |
| --- | --- |
| P0 | Talep formu, ticket API, DB kayıt, AI kategori/routing, admin liste |
| P1 | Loading/error durumları, API testleri, AI testleri, sprint dokümanları |
| P2 | Detay ekranı, harita, gelişmiş aciliyet, benzer kayıt gruplama |

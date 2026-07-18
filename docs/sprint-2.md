# Sprint 2 - Stabilizasyon ve Kanıtlandırma

## Sprint Bilgileri

- Tarih: 6-19 Temmuz 2026
- Takım: Umut Can Özgül, Eren Altunay, Semih Bekdaş
- Sprint hedefi: Çalışan MVP'yi yeniden doğrulamak, teslim kanıtlarını tamamlamak ve final sprinti için ölçülebilir backlog hazırlamak.

## Kapsam Kararı

Sprint 1 sonunda vatandaş formu, ticket API'si, kural tabanlı AI analizi ve admin listesi çalışan durumdaydı. Sprint 2'de kontrolsüz özellik genişletmek yerine şu eksikler kapatıldı:

- Gerçek uygulama ekran görüntülerinin repository'ye eklenmesi.
- README'nin gerçek kod ve resmi bootcamp beklentileriyle uyumlu hâle getirilmesi.
- Frontend bağımlılıklarının kilitlenmesi, güvenlik güncellemesi ve Vite yapılandırması.
- Backend, AI ve frontend build kontrollerinin tekrar çalıştırılması.
- AI veri setinde kategori ve öncelik regresyon ölçümünün çıkarılması.
- Sprint 3 öncelik, kapasite, sorumluluk ve risk planının hazırlanması.

## Backlog ve Puan Tamamlama Mantığı

Story point değerleri görevin teknik riski, doğrulama ihtiyacı ve birden fazla katmanı etkileyip etkilememesine göre verildi. Sprint kapasitesi 31 SP olarak belirlendi.

| ID | İş | Sorumlu | SP | Durum | Kanıt |
| --- | --- | --- | ---: | --- | --- |
| S2-01 | Frontend araç zincirini ve Vite yapılandırmasını güncelle | Eren + Semih | 5 | Done | `frontend/package.json`, `frontend/package-lock.json`, `frontend/vite.config.js` |
| S2-02 | Talep formu ve admin paneli ekran görüntülerini ekle | Umut Can + Eren | 5 | Done | `docs/screenshots/` |
| S2-03 | README ve sprint kanıtlarını tamamla | Semih + ortak review | 8 | Done | `README.md`, `docs/sprint-2.md` |
| S2-04 | AI, backend ve frontend doğrulamalarını çalıştır | Semih + Eren | 8 | Done | `docs/test-report.md` |
| S2-05 | Sprint 3 planını ve final backlog'unu oluştur | Tüm takım | 5 | Done | `docs/sprint-3-plan.md` |
|  | **Toplam** |  | **31** | **31/31** |  |

## Sprint Board Güncellemesi

| To Do | In Progress | Done |
| --- | --- | --- |
| - | - | S2-01, S2-02, S2-03, S2-04, S2-05 |

Repository'de doğrulanmış harici bir Miro/Asana board bağlantısı bulunmadığı için sprint kanıtı bu tablo ve `docs/product-backlog.md` üzerinden tutulmuştur.

## Doğrulanan Ürün Durumu

| Kontrol | Sonuç |
| --- | --- |
| Python söz dizimi | `ai/` ve `backend/app/` başarılı |
| Backend smoke | Health, create, list, detail ve 404 senaryoları başarılı |
| AI demo smoke | 3/3 örnek beklenen kategoriye yönlendi |
| Veri seti kategori uyumu | 133/150 (%88,7) |
| Veri seti öncelik uyumu | 74/150 (%49,3) |
| Frontend production build | Başarılı |
| Frontend bağımlılık güvenliği | `npm audit`: 0 bilinen açık |

Kategori ve öncelik oranları aynı sentetik veri setindeki regresyon ölçümüdür; production başarımı veya bağımsız model doğrulaması olarak yorumlanmamalıdır.

## Ürün Ekranları

### Vatandaş talep formu

![Vatandaş talep formu](screenshots/report-form.png)

### Admin talep listesi

![Admin talep listesi](screenshots/admin-ticket-list.png)

## Daily Scrum

Takımın 18 Temmuz tarihli görüşmesinde Sprint 2 geliştirme çıktılarının hazır olduğu, README'nin tamamlanacağı ve final sprintinde daha yoğun çalışılarak projenin bitirileceği kararlaştırıldı. Kişisel telefon numaraları dokümana alınmadı. Ayrıntılı özet `docs/daily-notes.md` içindedir.

## Definition of Done

- İş backlog içinde tanımlıdır.
- Değişiklik gerçek kod veya doküman kanıtıyla eşleşir.
- Frontend build, backend smoke ve ilgili AI kontrolleri geçer.
- README'de henüz yapılmamış bir özellik tamamlanmış gibi anlatılmaz.
- Ekran görüntüleri repository içinden GitHub'da görüntülenebilir.
- Sprint Review ve Retrospective kararları Sprint 3 backlog'una yansıtılır.

## Sprint 3'e Taşınanlar

- Talep durumu/önceliği update API'si ve admin UI akışı.
- Ayrı doğrulama setiyle öncelik modelinin iyileştirilmesi.
- Otomatik test ve GitHub Actions.
- Docker/canlıya alınabilir yapı.
- Final video, demo provası ve teslim kontrolü.

Harita ve benzer talep tespiti yalnızca P0 işler tamamlanırsa stretch goal olacaktır.

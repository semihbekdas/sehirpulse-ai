# Sprint 2 - Branch Çıktıları ve Teslim Tamamlama

## Sprint Bilgileri

- Tarih: 6-19 Temmuz 2026
- Takım: Umut Can Özgül, Eren Altunay, Semih Bekdaş
- Sprint hedefi: Çalışan MVP'yi gerçek ekranlarla belgelemek, frontend çalıştırma yapılandırmasını tamamlamak, teslim kanıtlarını hazırlamak ve final sprinti için ölçülebilir backlog oluşturmak.

## Doğrulanmış Branch Temeli

Sprint 2 çalışmasının başlangıç noktası Eren Altunay tarafından hazırlanan `origin/sprint-2` branch'idir.

| Commit | Branch | Doğrulanmış çıktı |
| --- | --- | --- |
| `0f3f3a9` | `origin/sprint-2` | README taslağı, `docs/screenshots/` içindeki talep/admin ekranları, `frontend/vite.config.js` ve frontend bağımlılık düzeni |
| `bbbf9ec` | `origin/main` | README'deki admin paneli ekran görüntüsü düzeltmesi |
| `c4adc3e` | `agent/sprint-2-readme-sprint-3-plan` | Sprint 2 README/kanıt tamamlama, doğrulamalar ve Sprint 3 planı |

Git ancestry kontrolüne göre `origin/sprint-2`, `origin/main`in; `origin/main` de mevcut agent branch'inin atasıdır. Böylece Sprint 2 branch'inde yapılan işler eksiksiz korunarak geliştirilmiştir.

## Kapsam Kararı

Sprint 1 sonunda vatandaş formu, ticket API'si, kural tabanlı AI analizi ve admin listesi çalışan durumdaydı. Eren'in Sprint 2 branch'i bu ürünü görünür ve çalıştırılabilir hâle getiren README, ekran ve Vite çıktıları sağladı. Bu temel üzerinde şu eksikler kapatıldı:

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
| S2-01 | README taslağı, Vite yapılandırması ve frontend bağımlılık temelini oluştur | Eren | 8 | Done | `0f3f3a9`, `frontend/vite.config.js` |
| S2-02 | Gerçek talep/admin ekranlarını ekle ve admin görselini düzelt | Eren | 5 | Done | `docs/screenshots/`, `bbbf9ec` |
| S2-03 | README ve sprint kanıtlarını tamamla | Semih + ortak review | 8 | Done | `README.md`, `docs/sprint-2.md` |
| S2-04 | AI/backend/frontend doğrulaması ve güvenli bağımlılık güncellemesi | Semih | 5 | Done | `docs/test-report.md`, `frontend/package.json` |
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

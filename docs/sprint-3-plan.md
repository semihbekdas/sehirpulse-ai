# Sprint 3 Final Planı

## Sprint Çerçevesi

- Tarih: 20 Temmuz-2 Ağustos 2026
- Kod dondurma: 31 Temmuz 2026
- Final teslim: 2 Ağustos 2026, 23.59
- Planlanan kapasite: 55 SP
- Takım: Umut Can Özgül, Eren Altunay, Semih Bekdaş

## Sprint Hedefi

ŞehirPulse AI'ı yalnızca kayıt gösteren bir MVP'den; talep durumunun yönetilebildiği, AI önceliği ölçülmüş, otomatik test edilen ve temiz ortamda çalıştırılabilen jüri sunumuna hazır bir ürüne dönüştürmek.

## Öncelik Kuralı

P0 işler bitmeden harita, embedding tabanlı benzer kayıt tespiti veya yeni görsel özellik alınmayacaktır. Final sprintinde ürün bütünlüğü, kanıt ve teslim güvenliği yeni özellik sayısından daha önemlidir.

## Sprint Backlog

| ID | Öncelik | User Story / İş | Sorumlu | SP | Bağımlılık |
| --- | --- | --- | --- | ---: | --- |
| S3-01 | P0 | Belediye yetkilisi olarak talebin durumunu ve gerektiğinde önceliğini güncellemek istiyorum. | Eren | 8 | Mevcut Ticket modeli |
| S3-02 | P0 | Belediye yetkilisi olarak talepleri aramak, filtrelemek ve detayını görmek istiyorum. | Umut Can | 8 | S3-01 API sözleşmesi |
| S3-03 | P0 | Takım olarak öncelik sonucunun ölçülebilir ve daha güvenilir olmasını istiyoruz. | Semih | 13 | Ayrı validation seti |
| S3-04 | P0 | Takım olarak her değişiklikte API, AI ve frontend build hatalarını otomatik görmek istiyoruz. | Eren + Semih | 8 | Kalıcı test dosyaları |
| S3-05 | P0 | Jüri olarak projeyi temiz bir ortamda kolayca çalıştırabilmek istiyorum. | Eren + Umut Can | 8 | Docker/env yapılandırması |
| S3-06 | P1 | Kullanıcı olarak mobilde ve hata durumlarında anlaşılır bir arayüz görmek istiyorum. | Umut Can | 5 | Admin akışı |
| S3-07 | P0 | Takım olarak final video ve teslim paketini eksiksiz sunmak istiyoruz. | Tüm takım | 5 | Kod dondurma |
|  |  | **Toplam** |  | **55** |  |

## Kabul Kriterleri

### S3-01 - Ticket update API

- `PATCH /tickets/{id}` yalnızca izin verilen `status` ve `priority_level` alanlarını günceller.
- Geçerli durumlar açık bir enum ile sınırlandırılır.
- Geçersiz ID `404`, geçersiz değer `422` döndürür.
- `updated_at` değişir ve güncelleme veritabanında kalıcıdır.
- API sözleşmesi ve otomatik testler güncellenir.

### S3-02 - Admin yönetim akışı

- Metin, kategori, birim, öncelik ve durum filtreleri bulunur.
- Bir kayıt açıldığında tam açıklama ve AI gerekçesi görülebilir.
- Durum/öncelik güncellemesinde loading, başarı ve hata geri bildirimi gösterilir.
- Sayfa yenilendiğinde güncellenen değer API'den geri gelir.
- Masaüstü ve mobil görünüm kontrol edilir.

### S3-03 - AI öncelik iyileştirmesi

- Mevcut veri setinden bağımsız, sürümlenmiş bir validation CSV hazırlanır.
- Baseline kategori ve öncelik metrikleri yeniden üretilebilir bir komutla raporlanır.
- Öncelik uyumu validation setinde en az %75 olur.
- Yanlış pozitif/negatif örnekler kategori bazında raporlanır.
- Model/kuralların sınırlılıkları `ai/README.md` içinde açıklanır.

### S3-04 - Otomatik test ve CI

- Backend health/create/list/detail/update/404/422 testleri bulunur.
- AI kategori, routing ve priority testleri bulunur.
- Frontend production build CI içinde çalışır.
- GitHub Actions workflow'u push ve pull request üzerinde tetiklenir.
- Ana dalda kırmızı test bırakılmaz.

### S3-05 - Çalıştırılabilir paket

- Örnek ortam değişkenleri belgelenir; gizli bilgi repository'ye eklenmez.
- Backend ve frontend için Docker yapılandırması veya eşdeğer tek-komut kurulum bulunur.
- Temiz klasörde README adımları denenir.
- Kalıcı veri ve CORS davranışı dokümante edilir.
- Canlı link yetişmezse lokal demo paketi eksiksiz tutulur.

### S3-06 - UX son kontrol

- 320 px ve masaüstü genişliklerinde kritik içerik taşmaz.
- Form alanları label ve klavye odağıyla kullanılabilir.
- API hata mesajları kullanıcı dostudur.
- Boş, loading ve hata durumları bütün admin akışlarında görünürdür.

### S3-07 - Final teslim

- Public GitHub repository günceldir.
- Üç sprintin backlog, Daily Scrum, board, ürün durumu, Review ve Retrospective kanıtları erişilebilir.
- 3 dakikalık proje videosu YouTube'a yüklenir.
- Ürün Teslim Formu Scrum Master tarafından 2 Ağustos 23.59'dan önce tamamlanır.
- Demo konuşması ve yedek lokal demo prova edilir.

## Gün Gün Çalışma Planı

| Tarih | Takım hedefi | Umut Can | Eren | Semih |
| --- | --- | --- | --- | --- |
| 20 Tem | Planning ve sözleşme | Admin akış wireframe'i | PATCH sözleşmesi | Validation veri planı |
| 21 Tem | Backend update | UI state taslağı | Şema/servis/route | Priority hata analizi |
| 22 Tem | Backend test | API mock entegrasyonu | Update testleri | Validation CSV v1 |
| 23 Tem | Admin detay | Detay ve filtre UI | API review/fix | Baseline rapor scripti |
| 24 Tem | Admin update | Update UX | Entegrasyon desteği | Priority v2 |
| 25 Tem | AI iyileştirme | Mobil admin kontrolü | Test desteği | Ölçüm ve hata matrisi |
| 26 Tem | Entegrasyon günü | Uçtan uca UI | API bug fix | AI adapter entegrasyonu |
| 27 Tem | Otomasyon | Build kontrolü | GitHub Actions | AI/backend test paketi |
| 28 Tem | Paketleme | Env/README kontrolü | Docker omurgası | Test desteği |
| 29 Tem | UX ve erişilebilirlik | Mobil/a11y düzeltmeleri | Deployment desteği | AI dokümantasyonu |
| 30 Tem | Release adayı | Demo akışı | Temiz kurulum testi | Regresyon raporu |
| 31 Tem | Kod dondurma | Son UI bug fix | Son backend bug fix | Son AI bug fix |
| 1 Ağu | Teslim hazırlığı | Video/UI anlatımı | Teknik anlatım | AI anlatımı ve README review |
| 2 Ağu | Final kontrol | Form ve link kontrolü | Ürün Teslim Formu | Repo/test kanıt kontrolü |

## Daily Scrum Formatı

Her gün en fazla 15 dakikalık görüşmede şu dört bilgi kaydedilir:

- Dün tamamlanan iş ve kanıt linki.
- Bugünkü tek ana hedef.
- Blocker ve ihtiyaç duyulan kişi.
- Story'nin kalan tahmini.

## Riskler ve Yanıtlar

| Risk | Etki | Önlem |
| --- | --- | --- |
| Üç kişilik ekipte kapasite aşımı | P0 işlerin yetişmemesi | Stretch goal'ları backlog dışında tutmak |
| AI metriğinin hedefe ulaşmaması | Jüri AI puanı ve güven | Hata analizi, validation seti, açıklanabilir fallback |
| Deployment gecikmesi | Canlı demo linki olmaması | Docker ve yedek lokal demo paketi |
| Son gün entegrasyon hatası | Teslim riski | 31 Temmuz kod dondurma ve 2 günlük tampon |
| Eksik sprint kanıtı | Proje yönetimi puanı | README link kontrolü ve teslim checklist'i |
| Gizli bilgi sızıntısı | Güvenlik | `.env` ignore, örnek env, commit öncesi secret taraması |

## Definition of Done

- Kabul kriterleri otomatik veya belgeli manuel testten geçer.
- İlgili test/build komutu başarılıdır.
- README/API/AI dokümanı davranışla uyumludur.
- Ekran görüntüsü gerektiren UI değişikliğinin güncel kanıtı vardır.
- En az bir takım arkadaşı değişikliği gözden geçirir.
- Demo akışı kırılmaz.

## Stretch Goals

Yalnızca tüm P0 işler Done olduğunda:

1. Embedding tabanlı benzer talep önerisi için küçük PoC.
2. İlçe/mahalle bazlı basit yoğunluk haritası.
3. Canlı ortamda PostgreSQL geçişi.

Bu işler final teslim için zorunlu değildir ve ana akışı riske atarsa yapılmayacaktır.

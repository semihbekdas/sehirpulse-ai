# Sprint 2 Review

## Sprint Hedefi

Çalışan MVP'yi yeniden doğrulamak, teknik ve dokümantasyon borcunu görünür hâle getirmek, gerçek ekran kanıtlarını eklemek ve final sprintini ölçülebilir bir backlog ile hazırlamak.

## Tamamlanan İşler

- Talep formu ve admin panelinin gerçek ekran görüntüleri repository'ye eklendi.
- README; takım, ürün, gerçek özellikler, kurulum, API, Sprint 1, Sprint 2 ve Sprint 3 planını içerecek şekilde yenilendi.
- Boş Miro ve Daily Scrum bağlantıları repository içi doğrulanabilir kaynaklarla değiştirildi.
- Kodda bulunmayan durum/öncelik güncelleme özelliğinin tamamlandığı yönündeki yanlış ifade kaldırıldı.
- Vite ve React araç zinciri güncel, sabit sürümlere taşındı.
- Frontend production build, backend smoke ve AI kontrolleri tekrar çalıştırıldı.
- 150 satırlık veri setinde kategori ve öncelik regresyon ölçümleri çıkarıldı.
- Sprint 3 için 55 SP'lik P0/P1 planı oluşturuldu.

## Ürün Demosunda Gösterilebilen Akış

1. `/report` sayfasında geçerli talep oluşturulur.
2. `POST /tickets` talebi doğrular ve AI analizini üretir.
3. Kayıt SQLite veritabanına yazılır.
4. Kullanıcıya talep numarası, kategori ve yönlendirilen birim gösterilir.
5. `/admin/tickets` sayfasında kayıt; kategori, birim, konum, öncelik, durum ve AI gerekçesiyle listelenir.

## Doğrulama Sonuçları

- Kategori veri seti uyumu: 133/150 (%88,7).
- Öncelik veri seti uyumu: 74/150 (%49,3).
- Backend smoke senaryoları: başarılı.
- Frontend Vite 8 production build: başarılı.
- Frontend bağımlılık taraması: 0 bilinen açık.

## Tamamlanamayan veya Sprint 3'e Taşınan İşler

- Admin panelinden talep durumu ve öncelik güncelleme.
- Detay görünümü, filtreleme ve arama.
- Öncelik modelinin bağımsız doğrulama setinde iyileştirilmesi.
- Otomatik test/CI.
- Docker ve deployment.
- Harita ve benzer talep tespiti.

## Review Katılımcıları

- Umut Can Özgül
- Eren Altunay
- Semih Bekdaş

## Alınan Kararlar

- Final sprintinde önce ürün bütünlüğü ve çalışan yönetim akışı tamamlanacak.
- Öncelik modelinin mevcut %49,3 uyumu kabul edilebilir final seviyesi değildir; bu iş P0 olacaktır.
- Harita ve embedding çalışmaları, zorunlu işler bitmeden başlanmayacak.
- 31 Temmuz kod dondurma hedefidir; 1-2 Ağustos yalnızca test, video ve teslim için ayrılacaktır.

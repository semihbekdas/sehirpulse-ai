# Güncel Demo Notları

Sprint 1'de kurulan temel akış Sprint 2 sonunda yeniden doğrulanmıştır. Aşağıdaki konuşma planı mevcut ürünü gösterir; Sprint 3 sonunda admin update ve deployment adımları eklenmelidir.

## Süre Hedefi

2-3 dakika.

## Konuşma Akışı

| Bölüm | Anlatacak Kişi | Süre | İçerik |
| --- | --- | --- | --- |
| Problem ve ürün fikri | Kişi 1 | 30 sn | Vatandaş talepleri manuel sınıflandırıldığında zaman kaybı oluşur. ŞehirPulse AI bu süreci otomatikleştirir. |
| Talep formu | Kişi 1 | 30 sn | Vatandaş form üzerinden talep gönderir. |
| Backend ve veri akışı | Kişi 2 | 35 sn | Talep API'ye gelir, AI modülünden geçer ve veritabanına kaydedilir. |
| AI kategori ve routing | Kişi 3 | 45 sn | Metin analiz edilir, kategori ve ilgili birim belirlenir. |
| Admin liste | Kişi 1 + Kişi 2 | 30 sn | Talep admin panelinde görüntülenir. |
| Sprint 3 hedefleri | Ortak | 20 sn | Admin yönetim akışı, öncelik iyileştirmesi, otomatik test ve deployment tamamlanacak. |

## Demo İçin Güçlü Örnekler

| Metin | Beklenen Kategori | Beklenen Birim |
| --- | --- | --- |
| Mahallemizdeki sokak lambası 3 gündür yanmıyor. | Aydınlatma | Aydınlatma ve Enerji İşleri |
| Yolda büyük bir çukur oluştu, araçlar zarar görüyor. | Yol ve kaldırım | Fen İşleri Müdürlüğü |
| Çöp konteynerleri dolmuş, kötü koku yayılıyor. | Temizlik | Temizlik İşleri Müdürlüğü |
| Parktaki salıncak kırılmış, çocuklar için tehlikeli. | Park ve yeşil alan | Park ve Bahçeler Müdürlüğü |
| Otobüs durağında seferler çok aksıyor. | Ulaşım | Ulaşım Hizmetleri Müdürlüğü |
| Gece geç saatlerde çok yüksek müzik sesi geliyor. | Gürültü | Zabıta Müdürlüğü |

## Demo Kontrol Listesi

- [x] Backend smoke test geçti.
- [x] Frontend production build geçti.
- [x] `/health` yanıt veriyor.
- [x] `POST /tickets` talep oluşturuyor.
- [x] `GET /tickets` admin listesi verisini döndürüyor.
- [x] `GET /tickets/{id}` detay ve `404` senaryoları çalışıyor.
- [x] AI kategori ve birim çıktısı beklenen şekilde görünüyor.

## Sprint 3 Sonunda Eklenecek Demo Adımları

1. Admin bir talebin detayını açar.
2. Talep durumunu ve gerektiğinde önceliğini günceller.
3. Sayfa yenilendiğinde değişikliğin veritabanından kalıcı geldiği gösterilir.
4. Otomatik test/build kontrolü ve çalıştırma yöntemi kısaca gösterilir.
5. AI priority validation metriği ve sınırlılıkları açıklanır.

# Sprint 1 Retrospective

## İyi Gidenler

- Sprint hedefi net tutuldu ve uçtan uca akış önceliklendirildi.
- Backend, frontend ve AI katmanları ayrı ama uyumlu sözleşmelerle geliştirildi.
- AI tarafı açıklanabilir rule-based yaklaşımla hızlıca entegre edildi.
- Dokümantasyon proje teslimine uygun şekilde yapılandırıldı.

## Zorlanılan Noktalar

- Türkçe metin sınıflandırmada bazı kategoriler ortak kelime kullanıyor.
- Frontend ve backend aynı anda geliştirilirken API sözleşmesini sabit tutmak kritik.
- Gerçek belediye verisi olmadığı için veri seti sentetik örneklerle başlatıldı.

## Bir Sonraki Sprintte İyileştirilecekler

- Kategoriler için daha dengeli ve gerçekçi veri toplanmalı.
- Admin panelde filtreleme, detay ve durum güncelleme eklenmeli.
- Benzer talep tespiti için embedding yaklaşımı denenmeli.
- Harita görünümü ile konumsal analiz başlatılmalı.

## Teknik Borçlar

- Kimlik doğrulama yok.
- Test otomasyonu sınırlı.
- SQLite production için yeterli değil.
- AI modeli rule-based olduğu için bağlamı sınırlı anlıyor.

## Sprint 2 Aksiyonları

- PostgreSQL geçiş planı çıkar.
- Talep detay ekranı geliştir.
- Kategori ve öncelik için test seti oluştur.
- Harita prototipi ekle.
- Benzer kayıt gruplama PoC çalışması yap.

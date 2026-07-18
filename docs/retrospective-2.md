# Sprint 2 Retrospective

## İyi Gidenler

- Çalışan uçtan uca MVP korunurken ekran görüntüleri ve teslim kanıtları görünür hâle getirildi.
- Kod, README ve ekran görüntüleri birlikte incelenerek yanlış veya eksik ürün iddiaları ayıklandı.
- Frontend bağımlılıklarının yerel kurulumla kilit dosyası arasındaki sürüm farkı fark edilip giderildi.
- AI başarımı tahmin edilmek yerine veri seti üzerinde ölçüldü.
- Final sprinti için sorumlu, SP ve bitiş ölçütü olan uygulanabilir bir backlog çıkarıldı.

## Zorlanılan Noktalar

- Sprint 2 başında yeni özellik hedefi ve story point planı repository'de belgelenmemişti.
- Harici backlog/board bağlantısı paylaşılmamış, README'de boş linkler kalmıştı.
- Mevcut dokümanların çoğu Sprint 1 dilinde kaldığı için güncel ürün durumu dağınıktı.
- Öncelik kurallarının mevcut veri setindeki uyumu düşük kaldı.
- Otomatik test dosyaları ve CI olmadığı için doğrulamalar manuel komutlarla çalıştırıldı.

## İyileştirme Kararları

- Her Sprint 3 işi başlamadan önce kabul kriteri ve test senaryosu yazılacak.
- Günlük kısa durum notları tarih ve sorumluyla `docs/daily-notes.md` içinde tutulacak.
- Her PR'da frontend build ve backend/AI testleri otomatik çalışacak.
- README yalnızca merge edilmiş ve test edilmiş özellikleri tamamlanmış olarak gösterecek.
- 31 Temmuz sonrasında yeni özellik alınmayacak.

## Teknik Borç

- Ticket update endpointi yok.
- Frontend için otomatik component/akış testi yok.
- Backend smoke kontrolleri kalıcı test dosyalarına dönüştürülmemiş.
- SQLite migration yapısı yok.
- AI öncelik kuralları zayıf; bağımsız validation seti yok.
- Kimlik doğrulama ve yetkilendirme yok.
- Canlıya alma ve gözlemlenebilirlik yapılandırması yok.

## Sprint 3 Aksiyonları

- Eren: update API, test/CI ve Docker omurgası.
- Umut Can: admin iş akışı, filtre/detay ve UX kontrolleri.
- Semih: AI validation seti, öncelik iyileştirmesi ve entegrasyon testleri.
- Tüm takım: demo provası, 3 dakikalık video ve final teslimi.

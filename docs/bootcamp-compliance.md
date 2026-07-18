# Bootcamp 2026 Kılavuzu Uyum Kontrolü

Bu dosya, Bootcamp 2026 Bursiyer Kılavuzu'ndaki proje yönetimi ve teslim beklentilerinin ŞehirPulse AI repository'sindeki karşılığını gösterir.

## Takım Durumu

Kılavuzda takımların 5 kişi olması ve Product Owner, Scrum Master, 3 Developer yapısıyla ilerlemesi beklenmektedir. Bu projede ekipten ayrılan/aktif devam etmeyen üyeler olduğu için süreç 3 aktif kişiyle yürütülmektedir. Kılavuzda belirtildiği gibi takımda Bootcamp'e katılmayan kişiler varsa akademi ekibine bildirilebilir ve kalan kişilerle devam edilebilir.

## Güncel Rol Dağılımı

| Aktif Kişi | Scrum Rolü | Teknik Sorumluluk | Kılavuzla Uyum |
| --- | --- | --- | --- |
| Umut Can Özgül | Product Owner | Frontend, ürün kapsamı, backlog, demo akışı | PO aktif geliştirmeye dahil |
| Eren Altunay | Scrum Master | Backend, repo düzeni, API, sprint dokümanları | SM iletişim ve geliştirme sorumluluğu alıyor |
| Semih Bekdaş | Developer | AI/data, kategori tahmini, routing, test verisi | Developer sprint hedefini teknik çıktıya dönüştürüyor |

## Ürün Fikri ve Rollerini Belgeleme

| Kılavuz Beklentisi | Repository Karşılığı | Durum |
| --- | --- | --- |
| Takım ismi | ŞehirPulse AI takımı | Hazır |
| Takım rolleri | `README.md`, `docs/product-definition.md`, `docs/sprint-1.md` | Hazır |
| Ürün ismi | ŞehirPulse AI | Hazır |
| Ürün açıklaması | `README.md`, `docs/product-definition.md` | Hazır |
| Ürün özellikleri | `README.md`, `docs/product-backlog.md` | Hazır |
| Hedef kitle | `docs/product-definition.md` | Hazır |
| Product Backlog | `docs/product-backlog.md` | Hazır |

## Her Sprint Sonunda Beklenen Kanıtlar

| Kılavuz Beklentisi | Repository Karşılığı | Sprint 1 Durumu |
| --- | --- | --- |
| Backlog dağıtma mantığı | `docs/product-backlog.md` | Tamamlandı |
| Daily Scrum notları | `docs/daily-notes.md` | Tamamlandı |
| Sprint board updates | Issue listesi, backlog tablosu, PR template | Hazır |
| Ürün durumu | Çalışan frontend/backend/AI MVP | Tamamlandı |
| Sprint Review | `docs/sprint-review-1.md` | Tamamlandı |
| Sprint Retrospective | `docs/retrospective-1.md` | Tamamlandı |

### Sprint 2 Kanıtları

| Kılavuz Beklentisi | Repository Karşılığı | Durum |
| --- | --- | --- |
| Backlog dağıtma mantığı | `docs/sprint-2.md`, `docs/product-backlog.md` | Tamamlandı |
| Daily Scrum notları | `docs/daily-notes.md` - 18 Temmuz karar özeti | Tamamlandı |
| Sprint board updates | `docs/sprint-2.md` - board tablosu | Tamamlandı |
| Ürün durumu | README ekran görüntüleri ve `docs/test-report.md` | Tamamlandı |
| Sprint Review | `docs/sprint-review-2.md` | Tamamlandı |
| Sprint Retrospective | `docs/retrospective-2.md` | Tamamlandı |

## Değerlendirme Kriterlerine Hazırlık

| Kriter | Mevcut Karşılık | Sonraki İyileştirme |
| --- | --- | --- |
| Çalışan proje | Talep formu, API, AI routing, admin liste | Canlı deployment |
| Özgünlük | Belediyeler için AI destekli talep yönlendirme | Harita ve benzer talep gruplama |
| Ürün tamamlanma | Uçtan uca MVP | Detay ekranı, durum yönetimi |
| Pazar uygunluğu | Belediye, kampüs, site ve tesis yönetimi hedefleniyor | Pilot kurum/persona analizi |
| Yapay zeka öğeleri | Rule-based sınıflandırma, routing, öncelik | Embedding, LLM veya agent orkestrasyonu |
| Temiz kod/mimari | Frontend, backend, AI katmanları ayrı | Test otomasyonu, servis katmanı genişletme |
| Canlıya alınabilirlik | Lokal çalışır mimari ve README kurulum adımları | Docker ve cloud deployment |

## Final Teslim Notları

Bootcamp final tesliminde ayrıca şunlar gerekecektir:

- GitHub reposunun public olması.
- 3 dakikalık proje videosunun YouTube'a yüklenmesi.
- Ürün Teslim Formu'nun Scrum Master tarafından doldurulması.
- 3 sprint sonunda proje yönetimi dokümanlarının eksiksiz olması.
- Canlı demo linki varsa formda paylaşılması.

Final sprint 20 Temmuz-2 Ağustos 2026 tarihleri arasındadır. Kod dondurma hedefi 31 Temmuz, final form hedefi 2 Ağustos 23.59'dan öncedir.

## Sprint 3 İçin Kılavuza Göre Öncelikler

- Çalışan proje ve ürün bütünlüğü: admin update/detay/filtre akışını tamamlamak.
- Yapay zeka öğeleri: öncelik sonucunu ayrı validation setinde ölçmek ve iyileştirmek.
- Temiz kod/mimari: kalıcı testler ve GitHub Actions eklemek.
- Canlıya alınabilirlik: Docker ve temiz ortam kurulumunu doğrulamak.
- Kullanıcı değeri: mobil/erişilebilirlik ve anlaşılır hata durumlarını tamamlamak.
- Proje yönetimi: üç sprintin backlog, Daily, board, Review ve Retrospective linklerini README'den erişilebilir tutmak.
- Final teslim: public repo, 3 dakikalık YouTube videosu ve Ürün Teslim Formu.

Harita ve embedding tabanlı benzer talep tespiti, zorunlu P0 teslimleri riske atmayacaksa ek puan/stretch goal olarak değerlendirilecektir.

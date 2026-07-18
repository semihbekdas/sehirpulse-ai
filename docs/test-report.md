# Test Raporu

Bu rapor Sprint 1 MVP kontrollerini ve 18 Temmuz 2026 tarihinde tekrarlanan Sprint 2 doğrulamalarını listeler.

## Calistirilan Kontroller

| Kontrol | Komut | Beklenen Sonuc |
| --- | --- | --- |
| Python soz dizimi | `python3 -m compileall ai backend/app` | Hata vermeden tamamlanir. |
| AI smoke test | `python3 -c "from ai.classify import classify_ticket; ..."` | Demo metinleri beklenen kategorilere duser. |
| Veri seti satir sayisi | `python3 -c "import csv; ..."` | `150` satir dondurur. |
| Backend API smoke test | FastAPI `TestClient` ile `/health`, `POST /tickets`, `GET /tickets`, `GET /tickets/{id}` | `200`, `201`, `200`, `200/404` yanitlari alinir. |
| Frontend build | `npm run build` | Vite production build basariyla tamamlanir. |

## Test Edilen AI Ornekleri

| Metin | Beklenen Kategori | Beklenen Birim |
| --- | --- | --- |
| Mahallemizdeki sokak lambası 3 gündür yanmıyor. | Aydınlatma | Aydınlatma ve Enerji İşleri |
| Mahallemizdeki sokak lambasi 3 gundur yanmiyor. | Aydınlatma | Aydınlatma ve Enerji İşleri |
| Yolda büyük bir çukur oluştu, araçlar zarar görüyor. | Yol ve kaldırım | Fen İşleri Müdürlüğü |
| Yolda buyuk bir cukur olustu, araclar zarar goruyor. | Yol ve kaldırım | Fen İşleri Müdürlüğü |
| Çöp konteynerleri dolmuş, kötü koku yayılıyor. | Temizlik | Temizlik İşleri Müdürlüğü |
| Alt geçit güvensiz ve karanlık olduğu için risk var. | Güvenlik | Zabıta Müdürlüğü |

## Notlar

- `backend/sehirpulse.db`, `frontend/dist/`, `frontend/node_modules/` ve `__pycache__/` dosyalari lokal test sirasinda olusur ve `.gitignore` kapsamindadir.
- Güncel ekran görüntüleri `docs/screenshots/` klasöründedir.

## Sprint 2 Doğrulaması - 18 Temmuz 2026

| Kontrol | Sonuç |
| --- | --- |
| `python3 -m compileall -q ai backend/app` | Başarılı |
| 3 örnek AI kategori/routing smoke testi | 3/3 başarılı |
| FastAPI `TestClient` health/create/list/detail/404 akışı | 6/6 kontrol başarılı |
| Mevcut CSV kategori etiketi uyumu | 133/150 (%88,7) |
| Mevcut CSV öncelik etiketi uyumu | 74/150 (%49,3) |
| `npm ci` | Kilit dosyasıyla başarılı |
| `npm run build` | Vite production build başarılı |
| `npm audit` | 0 bilinen açık |

## Ölçüm Notu

Kategori ve öncelik oranları `ai/data/sample_tickets_tr.csv` içindeki mevcut sentetik veri ile mevcut kuralların uyumunu gösterir. Ayrı tutulmuş bir test seti kullanılmadığı için bu sonuçlar production model doğruluğu olarak sunulmamalıdır.

Öncelik uyumunun %49,3 kalması Sprint 3 için P0 teknik iyileştirme olarak backlog'a alınmıştır.

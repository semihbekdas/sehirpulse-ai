# Test Raporu

Bu rapor Sprint 1 MVP tesliminden once calistirilan lokal dogrulamalari listeler.

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
- Ekran goruntuleri demo calistirilan ortamda `screenshots/` klasorune eklenmelidir.

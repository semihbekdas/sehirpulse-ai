# Sprint 1 Review

## Sprint Hedefi

Vatandaş talebi oluşturulabilen, backend'e kaydedilebilen, AI ile kategori/birim tahmini yapılabilen ve admin panelinde listelenebilen temel ürün iskeletini geliştirmek.

## Tamamlanan İşler

- React + Vite frontend kurulumu yapıldı.
- `/report` vatandaş talep formu geliştirildi.
- Form validasyon, loading, hata ve başarı durumları eklendi.
- FastAPI backend kurulumu yapıldı.
- SQLite + SQLAlchemy Ticket modeli oluşturuldu.
- `POST /tickets`, `GET /tickets`, `GET /tickets/{id}` endpointleri geliştirildi.
- AI kategori tahmini, routing ve temel öncelik modülleri oluşturuldu.
- Backend create akışı AI adapter ile bağlandı.
- `/admin/tickets` admin liste ekranı geliştirildi.
- Sprint dokümanları ve backlog hazırlandı.

## Tamamlanamayan veya Sprint 2'ye Taşınan İşler

- Harita görünümü.
- Benzer talep tespiti.
- Gelişmiş aciliyet skoru.
- Kullanıcı hesabı ve rol bazlı yetki.
- Production deployment.

## Demo Akışı

1. Backend `uvicorn app.main:app --reload` ile başlatılır.
2. Frontend `npm run dev` ile başlatılır.
3. `/report` ekranı açılır.
4. `Mahallemizdeki sokak lambası 3 gündür yanmıyor.` metniyle talep gönderilir.
5. Başarı mesajında talep ID, kategori ve birim gösterilir.
6. `/admin/tickets` ekranı açılır.
7. Talep listede `Aydınlatma` ve `Aydınlatma ve Enerji İşleri` bilgileriyle gösterilir.

## Ekran Görüntüleri

- `docs/screenshots/report-form.png`
- `docs/screenshots/admin-ticket-list.png`

## Sprint 2 Önerileri

- Talep detay ekranı.
- Harita ve yoğunluk görünümü.
- Benzer talep gruplama.
- Gelişmiş öncelik skoru.
- Departman bazlı filtreleme.

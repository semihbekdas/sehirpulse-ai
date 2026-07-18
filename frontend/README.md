# ŞehirPulse AI Frontend

React 19 + Vite 8 tabanlı kullanıcı arayüzüdür. İki ana ekran vardır:

- `/report`: Vatandas talep formu.
- `/admin/tickets`: Admin talep listesi.

## Gereksinimler

- Node.js `20.19+` veya `22.12+`
- Kilitli bağımlılıklar için `npm ci`

## Kurulum

```bash
npm ci
npm run dev
```

Varsayilan frontend adresi: `http://localhost:5173`

Backend varsayilan adresi: `http://localhost:8000`

Farkli backend adresi icin `.env` dosyasina ekleyin:

```bash
VITE_API_URL=http://localhost:8000
```

## Doğrulama

```bash
npm run build
npm audit
```

Son Sprint 2 kontrolünde production build başarılı olmuş ve bağımlılık taraması 0 bilinen açık raporlamıştır.

## Mevcut Sınırlar

- Routing, `window.location.pathname` üzerinden hafif bir MVP yaklaşımıyla yapılır.
- Admin ekranı talepleri listeler; durum/öncelik güncelleme ve filtreleme Sprint 3 planındadır.
- Otomatik frontend testleri henüz eklenmemiştir.

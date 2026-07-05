# Ürün Tanımı

## Ürün Adı

ŞehirPulse AI

## Problem

Belediye ve benzeri kurumlarda vatandaşlardan gelen talep, şikayet ve ihbarlar çoğu zaman manuel okunur, sınıflandırılır ve ilgili birime yönlendirilir. Başvuru sayısı arttığında bu süreç yavaşlar, tekrar eden kayıtlar fark edilmeyebilir ve acil işler geç ele alınabilir.

## Çözüm

ŞehirPulse AI, vatandaş talebini kaydeden, açıklama metninden temel kategori tahmini yapan, ilgili belediye birimini öneren ve kayıtları admin panelinde gösteren yapay zeka destekli bir yönetim panelidir.

## Hedef Kullanıcılar

| Kullanıcı | İhtiyaç |
| --- | --- |
| Vatandaş | Talep, şikayet veya ihbarı hızlıca iletmek |
| Belediye yetkilisi | Gelen talepleri tek listede görmek |
| Birim sorumlusu | Kendisine yönlenen işleri önceliklendirmek |
| Proje takımı | Sprint bazlı çalışan MVP göstermek |

## Sprint 1 MVP Kapsamı

Sprint 1'de yapılacaklar:

- Vatandaş talep formu.
- `POST /tickets` ile talep kaydı.
- `GET /tickets` ile admin listeleme.
- Rule-based AI kategori tahmini.
- Kategoriye göre belediye birimi routing.
- Temel öncelik seviyesi.
- Sprint dokümantasyonu.

Sprint 1 dışında bırakılanlar:

- Gerçek kullanıcı hesabı ve yetkilendirme.
- Gelişmiş harita/yoğunluk analizi.
- Embedding ile benzer kayıt gruplama.
- LLM agent orkestrasyonu.
- Canlı production deployment.

## Başarı Ölçütü

Sprint sonunda demo sırasında şu akış kesintisiz gösterilebilmelidir:

```text
Talep formu → Backend kayıt → AI kategori/birim → Admin listesi
```

# Ürün Tanımı

## Ürün Adı

ŞehirPulse AI

## Takım ve Roller

Bootcamp sürecinde standart ekip yapısı 5 kişi olarak tanımlanmıştır. Takımda sonradan ayrılan/aktif devam etmeyen üyeler olduğu için bu proje 3 aktif kişiyle yürütülmektedir. Roller, kılavuzdaki eşit sorumluluk ve aktif geliştirme beklentisine göre birleştirilmiştir.

| Rol | Aktif Sorumluluk |
| --- | --- |
| Product Owner + Frontend | Ürün vizyonu, hedef kitle, backlog, talep formu ve admin liste ekranı |
| Scrum Master + Backend | İletişim sorumluluğu, repo düzeni, API, veritabanı ve entegrasyon |
| Developer + AI/Data | AI sınıflandırma, routing, örnek veri seti ve AI dokümantasyonu |

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
- Bootcamp kılavuzunda beklenen Sprint 1 kanıt dokümanları.

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

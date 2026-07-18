# ŞehirPulse AI Modülü

Bu klasör, backend'e kolay bağlanan ve karar gerekçesi üreten kural tabanlı kategori, routing ve öncelik katmanını içerir. Mevcut yaklaşım bir production makine öğrenmesi modeli değildir.

## Dosyalar

| Dosya | Gorev |
| --- | --- |
| `classify.py` | Talep metnini kategori ve alt kategoriye ayirir. |
| `routing.py` | Kategoriye gore belediye birimini dondurur. |
| `priority_basic.py` | Basit dusuk/orta/yuksek oncelik hesabi yapar. |
| `data/category_department_mapping.csv` | Kategori ve belediye birimi sozlesmesi. |
| `data/sample_tickets_tr.csv` | Demo ve manuel test icin Turkce ornek talepler. |

## Yaklasim

Kural tabanlı sınıflandırmada her kategori için anahtar kelimeler tanımlanır. Metinde geçen kelimeler puanlanır ve en yüksek puana sahip kategori seçilir.

Metin esleme katmani Turkce karakterli ve ASCII yazimlari birlikte destekler. Ornegin `çukur` ve `cukur`, `sokak lambası` ve `sokak lambasi` ayni kategoriye dusurulur.

Bu yontem:

- Hizli entegre edilir.
- Karar gerekcesi uretir.
- Daha sonra TF-IDF, embedding veya LLM tabanlı sınıflandırmaya geçiş için temel sözleşmeyi korur.

## Hızlı Test

```bash
python3 ai/classify.py
python3 ai/routing.py
```

Beklenen demo metni:

```text
Mahallemizdeki sokak lambası 3 gündür yanmıyor.
```

Beklenen sonuc:

```text
Kategori: Aydınlatma
Birim: Aydınlatma ve Enerji İşleri
```

## Sprint 2 Regresyon Ölçümü

`data/sample_tickets_tr.csv` içindeki 150 sentetik örnekte:

- Kategori etiketi uyumu: `133/150` (%88,7)
- Öncelik etiketi uyumu: `74/150` (%49,3)

Bu oranlar aynı veri seti ve mevcut kurallar üzerindeki regresyon kontrolüdür; bağımsız test başarımı değildir. Özellikle priority katmanı iyileştirmeye açıktır.

## Bilinen Sınırlılıklar

- Anahtar kelime çakışmaları çok kategorili metinlerde yanlış sonuca neden olabilir.
- Kelime bağlamı, olumsuzluk ve ironi anlaşılmaz.
- Güven skoru olasılık kalibrasyonu değildir; kural puanından türetilir.
- Öncelik katmanı süre, risk ve etkilenen kişi bilgisini sınırlı kurallarla değerlendirir.
- Production için ayrı eğitim/validation/test verisi yoktur.

Sprint 3 hedefi, ayrı bir validation seti oluşturmak ve öncelik uyumunu en az %75'e çıkarmaktır.

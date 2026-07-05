# SehirPulse AI Modulu

Sprint 1 icin hedef, kusursuz model degil; backend'e kolay baglanan, aciklanabilir ve demo sirasinda guvenilir calisan bir AI katmani uretmektir.

## Dosyalar

| Dosya | Gorev |
| --- | --- |
| `classify.py` | Talep metnini kategori ve alt kategoriye ayirir. |
| `routing.py` | Kategoriye gore belediye birimini dondurur. |
| `priority_basic.py` | Basit dusuk/orta/yuksek oncelik hesabi yapar. |
| `data/category_department_mapping.csv` | Kategori ve belediye birimi sozlesmesi. |
| `data/sample_tickets_tr.csv` | Demo ve manuel test icin Turkce ornek talepler. |

## Yaklasim

Ilk sprintte rule-based siniflandirma kullanilir. Her kategori icin anahtar kelimeler tanimlanir. Metinde gecen kelimeler puanlanir ve en yuksek puana sahip kategori secilir.

Metin esleme katmani Turkce karakterli ve ASCII yazimlari birlikte destekler. Ornegin `çukur` ve `cukur`, `sokak lambası` ve `sokak lambasi` ayni kategoriye dusurulur.

Bu yontem:

- Hizli entegre edilir.
- Karar gerekcesi uretir.
- Sprint 2'de TF-IDF, embedding veya LLM tabanli siniflandirmaya gecis icin temel sozlesmeyi korur.

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

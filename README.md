# NLP ile Metin Ön İşleme (Tokenization, Stemming, Lemmatization)

Bu proje, **Doğal Dil İşleme (Natural Language Processing - NLP)** alanında yaygın olarak kullanılan **Tokenization**, **Stopwords Removal**, **Stemming** ve **Lemmatization** işlemlerini hem **İngilizce** hem de **Türkçe** metinler üzerinde uygulamaktadır.

---

## Özellikler

- **Tokenization:** Metni anlamlı kelime parçalarına ayırma.
- **Stopwords Removal:** Anlam taşımayan kelimeleri (örn. "ve", "ile", "the", "is") temizleme.
- **Stemming:** Kelimeleri kök hâline indirme (ör. `running → run`).
- **Lemmatization:** Kelimeleri sözlükteki temel hâline dönüştürme (ör. `better → good`).
- **Türkçe & İngilizce desteği:** `nltk` ve `snowballstemmer` kullanılarak.

---

## 🛠 Kullanılan Kütüphaneler

- **nltk** → Tokenization, stopwords, stemming, lemmatization
- **snowballstemmer** → Türkçe kök çıkarma
- **string** → Noktalama işaretlerini temizleme

---

## Kurulum:
```bash
pip install nltk snowballstemmer

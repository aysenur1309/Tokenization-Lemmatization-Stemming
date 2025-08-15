# NLP ile Metin Ön İşleme (Tokenization, Stemming, Lemmatization)

Bu proje, **Doğal Dil İşleme (Natural Language Processing - NLP)** alanında yaygın olarak kullanılan **Tokenization**, **Stopwords Removal**, **Stemming** ve **Lemmatization** işlemlerini hem **İngilizce** hem de **Türkçe** metinler üzerinde uygulamaktadır.

---

## Özellikler

- **Tokenization:** Metni anlamlı kelime parçalarına ayırma.
- **Stopwords Removal:** Anlam taşımayan kelimeleri (örn. "ve", "ile", "the", "is") temizleme.
- **Stemming:** Kelimeleri kök hâline indirme (ör. `running → run`).
- **Lemmatization:** Kelimeleri sözlükteki temel hâline dönüştürme (ör. `better → good`).
- **Türkçe & İngilizce desteği:** `nltk` ve `snowballstemmer` kullanılarak.

 ### Stemming 
- *Veri Azaltma:* Farklı şekillerde yazılmış kelimelerin köklerine indirgenmesi, veri setinin boyutunu küçültür ve böylece analiz süreçleri hızlanır.
- *Anlamsal Benzerlik:* Aynı köke sahip kelimeler, anlamsal olarak birbirine yakın olduğu varsayılır. Bu da, daha doğru ve anlamlı sonuçlar elde edilmesini sağlar.
- *Sınıflandırma ve Kümeleme:* Metin sınıflandırma ve kümeleme gibi işlemlerde, stemming sayesinde benzer anlamlardaki kelimeler bir araya getirilerek daha iyi sonuçlar elde edilir.


---

## 🛠 Kullanılan Kütüphaneler

- **nltk** → Tokenization, stopwords, stemming, lemmatization
- **snowballstemmer** → Türkçe kök çıkarma
- **string** → Noktalama işaretlerini temizleme

---

## Kurulum:
```bash
pip install nltk snowballstemmer

import nltk
import string 

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords 
from nltk.stem import PorterStemmer, WordNetLemmatizer

stop_words = set(stopwords.words('english')) # İngilizce stopword'ler yüklendi

# Örnek cümle
sentence = "Cybersecurity risks are becoming increasingly prevalent and sophisticated in today's digital age."

# Tokenization, bir metni anlamlı parçalara (token) ayırma işlemi
words = word_tokenize(sentence) 

# Küçük harfe dönüştürme ve noktalama işaretlerini kaldırma işlemi
# Bu koşul, sadece harf ve sayılardan oluşan kelimeleri seçer
# isalnum() metodu, bir stringin alfanümerik olup olmadığını kontrol eder
# Yani sadece harf veya sayı içeriyorsa True, aksi halde False döner
words = [word.lower() for word in words if word.isalnum()]

word = "Merhaba123"
print(word.isalnum())

word = "Merhaba Dünya!"
print(word.isalnum())  # Çıktı: False çünkü boşluk ve ünlem işareti var

word = "@kodlama"
print(word.isalnum())  # Çıktı: False çünkü @ işareti var

# Stopwords'leri kaldırma 
# Kelime stopwords değilse kelimeyi alır kelimeler listesine atar
words = [word for word in words if word not in stop_words
         ]
# Stemming(Kök çıkarma)
porter_stemmer = PorterStemmer()
stemmed_words = [porter_stemmer.stem(word) for word in words]

# Lematizasyon, bir kelimeyi sözlükteki temel hâline (lemma) dönüştürme
wordnet_lemmatizer = WordNetLemmatizer()
lemmatized_words = [wordnet_lemmatizer.lemmatize(word) for word in words]

print(f"Orijinal Cümle: {sentence}")  # Sonuçları yazdırma 
print(f"Tokenlar: {words}")
print(f"Stemmed Kelimeler: {stemmed_words}")
print(f"Lemmatized Kelimeler: {lemmatized_words}")


from snowballstemmer import TurkishStemmer # Türkçe kök çıkarma

cumle = "Günümüz dijital çağında siber güvenlik riskleri giderek yaygılaşmakta ve karmaşılaşmaktadır."
kelimeler = word_tokenize(cumle)

# Küçük harfe dönüştürme ve noktalama işaretlerini kaldırma
kelimeler = [kelime.lower() for kelime in kelimeler if kelime.isalnum()]

kelime = "Merhabalar"
print(kelime.isalnum())

kelime = "Merhaba Dünya!!"
print(kelime.isalnum())

turkcekok = TurkishStemmer()

stemmed_kelimeler = [turkcekok.stemWord(kelime) for kelime in kelimeler]

print(f"Orijinal Cümle: {cumle}")  # Sonuçları yazdırma
print(f"Tokenlar: {kelimeler}")
print(f"Stemmed Kelimeler: {stemmed_kelimeler}")

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords 

def removeStopWords(documents):  # Stopwords'leri kaldırma fonksiyonu
    stop_words = set(stopwords.words('english'))
    result = []
    for document in documents:  # Tüm dökümanları alıp tokenize etme 
        words = word_tokenize(document)
    # Stopword'leri çıkarma. Eğer word değişkeni stopwords değilse filtered_words listesine at
        filtered_words = [word for word in words if word.lower() not in stop_words]
    # Temizlenmiş cümleyi result listesine ekleme .join(filtered_words)    
        result.append(" ".join(filtered_words)) 
    return result


# Örnek cümleler
documents = ["This is a simple example sentence.",
             "Cybersecurity risks are becoming increasingly prevalent and sophisticated in today's digital age."
]

yeni = removeStopWords(documents)  # Stopwords'leri kaldırma işlemi

print("Orijinal Cümle:")
for document in documents:
    print(f"- {document}")

print("\nProcessed Sentences (Stopwords Removed):")
for document in yeni:
    print(f"- {document}") 

def tokenizedDocument(documents):  # Tokenization fonksiyonu
    result = []
    for document in documents:
        words = word_tokenize(document)
        result.append(words)
    return result    

def removeLongWords(documents, max_length):  # Uzun kelimeleri kaldıran foksiyon
    result = []
    for document in documents:
        filtered_words = [word for word in document if len(word) <= max_length]
        result.append(filtered_words)
    return result 
  
def removeShortWords(documents, min_length):  # Kısa kelimeleri kaldıran fonksiyon
    result = []
    for document in documents:
        filtered_words = [word for word in document if len(word) >= min_length]
        result.append(filtered_words)
    return result

def removeWords(documents, words_to_remove):  # Belirli kelimeleri kaldıran fonksiyon
    result = []
    for document in documents:
        filtered_words = [word for word in document if word not in words_to_remove]
        result.append(filtered_words)
    return result

# Örnek cümleler
cumleler = [
    "an example of a short sentence",
    "Cybersecurity risks are becoming increasingly prevalent and sophisticated in today's digital age."
]

# Tokenization işlemi
dokuman = tokenizedDocument(cumleler) 

# Uzun kelimeleri kaldırma işlemi
uzun = removeLongWords(dokuman,6)

# Kısa kelimeleri kaldırma işlemi
kisa = removeShortWords(dokuman,4)

# Belirli kelimeleri kaldırma işlemi
kelimeler = ["short", "risks", "prevalent"]
istenilenkelimeatimi = removeWords(dokuman, kelimeler)

print("Orijinal Cümleler:")
for cumle in cumleler:
    print(f"-{cumle}")

print("\nUzun Kelimelerin Atılması:")
for filtered_cumle in uzun:
    print(f"- {' '.join(filtered_cumle)}")

print("\nKısa Kelimelerin Atılması:")
for filtered_cumle in kisa:
    print(f"- {' '.join(filtered_cumle)}")
    
print("\nBelirtilen Kelimelerin Atılması:")
for filtered_cumle in istenilenkelimeatimi:
    print(f"- {' '.join(filtered_cumle)}")
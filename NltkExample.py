import nltk
from nltk.tokenize import sent_tokenize
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer


def NLTKSteps(content):
    nltk.download("punkt")  # Cümle ayrıştırıcı için

    nltk.download("averaged_perceptron_tagger")  # Kelime etiketleme için

    text = content
    sentences = sent_tokenize(text)

    translator = str.maketrans("", "", string.punctuation)  # noktalama işareti çıkarma
    text_without_punctuation = text.translate(translator)

    my_input = []

    for cumleler in sentences:
        translator = str.maketrans("", "", string.punctuation)
        text_without_punctuation = cumleler.translate(translator)
        my_input.append(text_without_punctuation)

    stop_words = set(
        stopwords.words("english")
    )  # İngilizce stop word listesini kullanır

    my_input2 = []

    for cumleler in my_input:
        words = word_tokenize(cumleler)
        filtered_words = [word for word in words if word.lower() not in stop_words]
        my_input2.append(filtered_words)

    stemmer = PorterStemmer()

    for kapsül in my_input2:
        for cumleler in kapsül:
            kelimeData = cumleler.split(" ")
            for kelimeler in kelimeData:
                stemmed_word = stemmer.stem(kelimeler)

    return my_input2, sentences

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


import tkinter as tk


def summary_userinterface(summary_data, nltk_data):
    def copy_text():
        entered_text = summary_text.get("1.0", tk.END)
        if entered_text:
            summary_text.clipboard_clear()
            summary_text.clipboard_append(entered_text)

    def summary_function(text):
        # Cümlelere ayırma
        sentences = sent_tokenize(text)

        # Gereksiz kelimeleri kaldırma
        stop_words = set(stopwords.words("english"))
        clean_sentences = []
        for sentence in sentences:
            words = word_tokenize(sentence)
            clean_sentence = [
                word for word in words if word.casefold() not in stop_words
            ]
            clean_sentences.append(" ".join(clean_sentence))

        # Metni vektörlere dönüştürme
        vectorizer = TfidfVectorizer()
        sentence_vectors = vectorizer.fit_transform(clean_sentences)

        # Özet çıkarma
        similarity_matrix = cosine_similarity(sentence_vectors)
        summary_indices = similarity_matrix.sum(axis=1).argsort()[:-3:-1]
        summary_sentences = [sentences[i] for i in summary_indices]

        summary = " ".join(summary_sentences)
        return summary

    summary_text_data = summary_function(summary_data)

    pencere = tk.Tk()
    pencere.title("Grapy Summary User Interface")
    # Pencere boyutunu ayarla
    # # Ekran boyutlarını ayarlama
    window_width = 450
    window_height = 550
    screen_width = pencere.winfo_screenwidth()
    screen_height = pencere.winfo_screenheight()
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    pencere.geometry(f"{window_width}x{window_height}+{x}+{y}")
    # Başlık alanı oluştur
    baslik_alani = tk.Frame(pencere, bg="#6C4AB6", height=75)
    baslik_alani.pack(fill=tk.X)
    # Başlık metni oluştur
    baslik_metni = tk.Label(
        baslik_alani, text="Grapy", font=("Roboto", 32), fg="white", bg="#6C4AB6"
    )
    baslik_metni.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    # Metin giriş alanını oluştur
    summary_text = tk.Text(pencere, height=10, width=46)
    summary_text.insert(tk.END, summary_text_data)
    # Metni sona ekle
    summary_text.pack(pady=10)
    # Kopyala düğmesini oluştur
    buton_stil = {
        "width": 40,
        "height": 2,
        "background": "white",
        "foreground": "black",
        "highlightthickness": 2,
        "highlightbackground": "red",
        "highlightcolor": "red",
        "relief": "solid",
        "font": 24,
    }
    copy_button = tk.Button(pencere, text="Kopyala", command=copy_text, **buton_stil)
    copy_button.pack(pady=10)
    listbox = tk.Listbox(pencere)
    listbox.pack(ipadx=125, pady=10)
    for item in nltk_data:
        listbox.insert("end", item)
        # Pencereyi ekranda göster
    pencere.mainloop()

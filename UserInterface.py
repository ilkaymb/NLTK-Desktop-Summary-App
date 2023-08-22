import tkinter as tk
from neo4j import GraphDatabase
import NltkExample
from tkinter.filedialog import askopenfilename
import GraphInterface
import RogueInterface
import TFIDF
import Summary


def grafButtonClicked():
    if "fileSelected" in globals() and fileSelected:  # Dosya seçildiyse
        sonuc, sentenceData = NltkExample.NLTKSteps(content)
        similarity = TFIDF.TFIDF_Function(sentenceData)

        labelData = {}
        index = 0

        GraphInterface.create_networkx_graph(sentenceData, similarity)


def summaryButtonClicked():
    if "fileSelected" in globals() and fileSelected:  # Dosya seçildiyse
        sonuc, sentenceData = NltkExample.NLTKSteps(content)
        similarity = TFIDF.TFIDF_Function(sentenceData)

        labelData = {}
        index = 0

        Summary.summary_userinterface(content, sonuc)


def rogueScorePage():
    RogueInterface.RogueInterface()


def open_file():
    global fileSelected
    file_path = askopenfilename()
    if file_path:
        file = open(file_path, "r", encoding="utf-8")
        global content
        content = file.read()
        file.close()

        fileSelected = True
        # Değer girişi için giriş alanını oluştur

        # Değer al düğmesini oluştur
        change_text(content)
        graph_button_active()
        summary_button_active()


def get_value(value):
    return value
    # Burada yapmak istediğiniz işlemleri gerçekleştirin


def graph_button_active():
    graph_button.config(state=tk.NORMAL)


def summary_button_active():
    summary_buton.config(state=tk.NORMAL)


def change_text(new_text):
    file_text.config(text=new_text)


# Pencereyi oluştur
pencere = tk.Tk()
pencere.title("Grapy")


# Pencere boyutunu ayarla
# Ekran boyutlarını ayarlama
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


# Buton stilini ayarla
buton_stil = {
    "width": 40,
    "height": 2,
    "background": "white",
    "foreground": "black",
    "highlightthickness": 2,
    "highlightbackground": "red",  # Kenarlık (border) rengi
    "highlightcolor": "red",  # Kenarlık (border) rengi
    "relief": "solid",
    "font": 24,
}

# Buton oluştur
file_buton = tk.Button(pencere, text="Dosya Seç", **buton_stil, command=open_file)
file_buton.pack(pady=10)

summary_buton = tk.Button(
    pencere,
    text="Özet Çıkar",
    **buton_stil,
    command=summaryButtonClicked,
    state=tk.DISABLED,
)
summary_buton.pack(pady=10)


rogue_button = tk.Button(
    pencere, text="Rogue Skoru Hesapla", **buton_stil, command=rogueScorePage
)
rogue_button.pack(pady=10)


threshold_input = tk.Button(
    pencere,
    text="Cümle benzerliği için threshold değeri giriniz",
)

threshold_label = tk.Label(pencere, text="Threshold Değeri:", font=("Roboto", 12))
threshold_label.pack(pady=10)

# Threshold değerini alacak giriş kutusunu oluşturma
threshold_entry = tk.Entry(
    pencere,
)
threshold_entry.pack(ipadx=125, ipady=6)

graph_button = tk.Button(
    pencere,
    text="Graph Oluştur",
    **buton_stil,
    command=grafButtonClicked,
    state=tk.DISABLED,
)
graph_button.pack(pady=10)


file_text = tk.Label(pencere, text="", width=400, wraplength=400, font=("Roboto", 10))
file_text.pack()
# Pencereyi ekranda göster
pencere.mainloop()

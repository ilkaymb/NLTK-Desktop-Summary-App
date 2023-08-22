import tkinter as tk
import RogueCalculate


def RogueInterface():
    def rogue_calculate():
        entered_text1 = rogue_text1.get("1.0", tk.END)
        entered_text2 = rogue_text2.get("1.0", tk.END)

        rouge_1, rouge_2, rouge_l = RogueCalculate.RogueScore(
            entered_text1,
            entered_text2,
        )
        rouge_1Label.config(text=rouge_1)
        rouge_2Label.config(text=rouge_2)
        rouge_lLabel.config(text=rouge_l)

    # Ana pencereyi oluştur
    pencere = tk.Tk()
    pencere.title("Grapy Rogue Hesaplama")
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

    # Metin alanları
    label1 = tk.Label(pencere, text="Metin 1:")
    label1.pack()

    rogue_text1 = tk.Text(pencere, height=3, width=46)
    # Metni sona ekle
    rogue_text1.pack(pady=10)

    label2 = tk.Label(pencere, text="Metin 2:")
    label2.pack()
    rogue_text2 = tk.Text(pencere, height=3, width=46)
    # Metni sona ekle
    rogue_text2.pack(pady=10)

    # Buton
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
    button = tk.Button(
        pencere, text="Rogue Hesapla", command=rogue_calculate, **buton_stil
    )
    button.pack(pady=10)

    rouge_1Label = tk.Label(pencere, text="")
    rouge_1Label.pack()

    rouge_2Label = tk.Label(pencere, text="")
    rouge_2Label.pack()

    rouge_lLabel = tk.Label(pencere, text="")
    rouge_lLabel.pack()

    # Uygulamayı çalıştır
    pencere.mainloop()

import customtkinter as ctk
from tkinter import *

# Ana pencereyi oluştur
root = ctk.CTk()
root.title('Görev Listesi')
root.geometry('800x500+400+300')
root.grid_propagate(False)
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)  # Sağ panel için sütun yapılandırması

# Paneli oluştur
panel = ctk.CTkFrame(root, fg_color="#333333", corner_radius=10)
panel.place(x=15, y=15)

# Sağ paneli oluştur
sag_panel = ctk.CTkFrame(root, fg_color="#333333", corner_radius=10)
sag_panel.place(x=570, y=15)


def tamamla_gorev():
    print("basıldı")


def sil_gorev():
    print('sil görev')


# Butonlar için bir çerçeve oluştur
buton_cerceve = ctk.CTkFrame(panel, fg_color="#333333", corner_radius=10)
buton_cerceve.pack(pady=5)

# Tamamla butonunu oluştur ve çerçeveye yerleştir
tamamla_buton = ctk.CTkButton(buton_cerceve, text="Tamamla", fg_color="#0052cc", hover_color="#003380",
                              text_color="#ffffff",
                              corner_radius=10, width=50, command=tamamla_gorev)
tamamla_buton.pack(side=LEFT, padx=5)

# Sil butonunu oluştur ve çerçeveye yerleştir
sil_buton = ctk.CTkButton(buton_cerceve, text="Sil", fg_color="#cc000e", hover_color="#800008", text_color="#ffffff",
                          corner_radius=10, width=50, command=sil_gorev)
sil_buton.pack(side=LEFT, padx=5)

# Listbox'u oluştur ve stilini ayarla
listbox = Listbox(panel, bg="#222222", fg="#ffffff", highlightthickness=0, borderwidth=0, width=60, height=19)
listbox.pack(pady=(5, 10), fill='both', expand=True)

# Entry bileşenini oluştur ve stilini ayarla
gorev_entry = ctk.CTkEntry(panel, placeholder_text="Görev ekle", fg_color="#444444", text_color="#ffffff",
                           corner_radius=10)
gorev_entry.pack(pady=(10, 5), fill='x', padx=10)


# Görev ekleme fonksiyonu
def ekle_gorev():
    gorev = gorev_entry.get()
    if gorev != "":
        listbox.insert(END, gorev)
        gorev_entry.delete(0, END)


# 'Ekle' butonunu oluştur ve stilini ayarla
ekle_buton = ctk.CTkButton(panel, text="Ekle", command=ekle_gorev, fg_color="#0052cc", hover_color="#003380",
                           text_color="#ffffff", corner_radius=10)
ekle_buton.pack(pady=(5, 20))

# Yuvarlak buton için Canvas oluştur
canvas = Canvas(sag_panel, width=100, height=100, bg="#333333", highlightthickness=0)
canvas.pack(pady=(5, 20), padx=10)

# Yuvarlak butonu çiz
oval_id = canvas.create_oval(10, 10, 90, 90, fill="#2220E2", outline="#0052cc")

# Buton resmini yükle
buton_resmi = PhotoImage(file="person.png")
canvas.create_image(50, 50, image=buton_resmi)

# Kullanıcı isim alanı
metin_alani = ctk.CTkLabel(sag_panel, text="MUAZZEZ ABACI", text_color="#ffffff", corner_radius=10,
                           font=('Pt Mono', 22))
metin_alani.pack(pady=(0, 40), fill='x', padx=10)

# E-posta güncelleme metin giriş alanı
guncelle_eposta_entry = ctk.CTkEntry(sag_panel, placeholder_text="Yeni e-posta adresin", fg_color="#444444",
                                     text_color='#fff', corner_radius=10)
guncelle_eposta_entry.pack(pady=5, fill='x', padx=10)

# 'E-Postanı güncelle' butonunu oluştur
guncelle_eposta_buton = ctk.CTkButton(sag_panel, text="E-Postanı güncelle", fg_color="#0052cc", hover_color="#003380",
                                      text_color="#ffffff", corner_radius=10)
guncelle_eposta_buton.pack(pady=5, fill='x', padx=10)

# Şifre güncelleme metin giriş alanı
guncelle_sifre_entry = ctk.CTkEntry(sag_panel, placeholder_text="Yeni şifren", fg_color="#444444",
                                    text_color='#fff', corner_radius=10)
guncelle_sifre_entry.pack(pady=(40, 5), fill='x', padx=10)

# 'Şifreni güncelle' butonunu oluştur
guncelle_sifre_buton = ctk.CTkButton(sag_panel, text="Şifreni güncelle", fg_color="#0052cc", hover_color="#003380",
                                     text_color="#ffffff", corner_radius=10)
guncelle_sifre_buton.pack(pady=5, fill='x', padx=10)

# Çıkış yap butonu oluşturur
cikis_yap_buton = ctk.CTkButton(sag_panel, text="Çıkış Yap", fg_color="#cc000e", hover_color="#800008",
                                text_color="#ffffff", corner_radius=10)
cikis_yap_buton.pack(pady=(40, 20), fill='x', padx=10)

# Ana döngüyü başlat
root.mainloop()

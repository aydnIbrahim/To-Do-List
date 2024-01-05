import signup_page

import customtkinter as ctk
from tkinter import *
from tkinter import messagebox

from PIL import Image, ImageTk

fg_color = '#333333'
fg_color_cerceve = '#ae550c'

root = ctk.CTk()
root.title("Giriş Yap")
root.geometry('373x440+650+300')
root.grid_propagate(False)
root.resizable(False, False)
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# panel oluşturma
panel = ctk.CTkFrame(root, fg_color=fg_color, corner_radius=10)
panel.place(x=15, y=15)

# Hoşgeldin başlığı
hosgeldin_title = ctk.CTkLabel(panel, text="HOŞGELDİN", text_color='#fff', corner_radius=10, font=('Pt Mono', 40))
hosgeldin_title.pack(pady=(15, 50), fill='x', padx=15)

# Email giriş çerçevesi
email_cerceve = ctk.CTkFrame(panel, fg_color='#333', corner_radius=10)
email_cerceve.pack(pady=15, padx=20)

# Email label oluşturur
email_label = ctk.CTkLabel(email_cerceve, text="E-Posta ", text_color='#fff', corner_radius=10, font=('Pt Mono', 14))
email_label.pack(side=LEFT, padx=5)

# Email giriş alanı oluşturur
email_entry = ctk.CTkEntry(email_cerceve, placeholder_text='E-Posta adresin', fg_color=fg_color_cerceve,
                           text_color='#fff', corner_radius=10, border_width=0, width=200)
email_entry.pack(side=LEFT, padx=5)

# Şifre girişi çerçevesi
sifre_cerceve = ctk.CTkFrame(panel, fg_color='#333', corner_radius=10)
sifre_cerceve.pack(pady=15, padx=20)

# Şifre label oluşturur
sifre_label = ctk.CTkLabel(sifre_cerceve, text='Şifre ', text_color='#fff', corner_radius=10, font=('Pt Mono', 14))
sifre_label.pack(side=LEFT, padx=(5, 25))

# Sifre giris alanı olusturur
sifre_entry = ctk.CTkEntry(sifre_cerceve, placeholder_text='Şifren', fg_color=fg_color_cerceve, text_color='#fff',
                           corner_radius=10, border_width=0, width=165, show='*')
sifre_entry.pack(side=LEFT, padx=1)

# Göz ikonu eklenir ve bir Tkinter PhotoImage'a dönüştürülür
eye_icon = Image.open('eye.png')
eye_photo_image = ImageTk.PhotoImage(eye_icon)

# Göz çizgi ikonu eklenir ve bir Tkinter PhotoImage'a dönüştürülür
eye_slash_icon = Image.open('eye.slash.png')
eye_slash_photo_image = ImageTk.PhotoImage(eye_slash_icon)

# Canvas oluşturulur ve arka plan şeffaf yapılır
canvas_eye = Canvas(sifre_cerceve, bg='#333', width=35, height=35, highlightthickness=0)
canvas_eye.pack(side=LEFT, padx=1)

# Canvas üzerine göz ikonu eklenir
eye_button = canvas_eye.create_image(10, 10, anchor='nw', image=eye_photo_image)
canvas_eye.itemconfigure(eye_button, state='normal')

# Canvas üzerine göz çizgi ikonu eklenir
eye_slash_button = canvas_eye.create_image(10, 10, anchor='nw', image=eye_slash_photo_image)
canvas_eye.itemconfigure(eye_slash_button, state='hidden')


# Göz ikonuna tıklama olayı ekleyin
def on_eye_click(event):
    sifre_entry.configure(show='')
    canvas_eye.itemconfigure(eye_button, state='hidden')
    canvas_eye.itemconfigure(eye_slash_button, state='normal')


def on_eye_slash_click(event):
    sifre_entry.configure(show='*')
    canvas_eye.itemconfigure(eye_button, state='normal')
    canvas_eye.itemconfigure(eye_slash_button, state='hidden')


canvas_eye.tag_bind(eye_button, '<Button-1>', on_eye_click)
canvas_eye.tag_bind(eye_slash_button, '<Button-1>', on_eye_slash_click)


def giris_yap():
    print('giris yapildi')


# Giriş Yap butonu oluşturur
giris_yap_buton = ctk.CTkButton(panel, text='Giriş Yap', fg_color='#0052cc', hover_color='#003380', text_color='#fff',
                                corner_radius=10, width=170, command=giris_yap)
giris_yap_buton.pack(pady=30, padx=30)


def hesap_yoksa_kayit_ol():
    root.destroy()
    signup_page.mainloop()
    print('hesap yoksa kayit olundu')


# Hesap yoksa kayıt ol butonu oluşturur
hesap_yoksa_kayit_ol_buton = ctk.CTkButton(panel, text='Bir hesabın yok mu? Hemen kayıt ol!', fg_color='#333',
                                           hover_color='#333', command=hesap_yoksa_kayit_ol)
hesap_yoksa_kayit_ol_buton.pack(pady=30, padx=30)

root.mainloop()

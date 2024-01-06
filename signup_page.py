import os

import customtkinter as ctk
from tkinter import *
from tkinter import messagebox

from PIL import ImageTk, Image

import tdl_database

fg_color = '#333'
fg_color_cerceve = '#ae550c'

signup_page = ctk.CTk()
signup_page.title("Kayıt Ol")
signup_page.geometry('373x620+650+300')
signup_page.grid_propagate(False)
signup_page.resizable(False, False)
signup_page.grid_rowconfigure(0, weight=1)
signup_page.grid_columnconfigure(0, weight=1)

# panel oluşturma
panel = ctk.CTkFrame(signup_page, fg_color=fg_color, corner_radius=10)
panel.place(x=15, y=15)

# Hoşgeldin başlığı
hosgeldin_title = ctk.CTkLabel(panel, text="HOŞGELDİN", text_color='#fff', corner_radius=10, font=('Pt Mono', 40))
hosgeldin_title.pack(pady=(15, 50), fill='x', padx=15)

# İsim giriş çerçevesi oluşturur
isim_cerceve = ctk.CTkFrame(panel, fg_color='#333', corner_radius=10)
isim_cerceve.pack(pady=15, padx=20)

# İsim label oluşturur
isim_label = ctk.CTkLabel(isim_cerceve, text='İsim', text_color='#fff', corner_radius=10, font=('Pt Mono', 14))
isim_label.pack(side=LEFT, padx=(5, 33))

# İsim giriş alanı oluşturur
isim_entry = ctk.CTkEntry(isim_cerceve, placeholder_text='İsmin', fg_color=fg_color_cerceve, text_color='#fff',
                          corner_radius=10, border_width=0, width=200)
isim_entry.pack(side=LEFT, padx=5)

# Soy isim çerçevesi oluşturur
soy_isim_cerceve = ctk.CTkFrame(panel, fg_color='#333', corner_radius=10)
soy_isim_cerceve.pack(pady=15, padx=20)

# Soy isim label oluşturur
soy_isim_label = ctk.CTkLabel(soy_isim_cerceve, text='Soy isim', text_color='#fff', corner_radius=10, font=('Pt Mono', 14))
soy_isim_label.pack(side=LEFT, padx=5)

# Soy isim giriş alanı oluşturur
soy_isim_entry = ctk.CTkEntry(soy_isim_cerceve, placeholder_text='Soy ismin', fg_color=fg_color_cerceve, text_color='#fff',
                              corner_radius=10, border_width=0, width=200)
soy_isim_entry.pack(side=LEFT, padx=5)

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

# Şifre onayla girişi çerçevesi
sifre_onayla_cerceve = ctk.CTkFrame(panel, fg_color='#333', corner_radius=10)
sifre_onayla_cerceve.pack(pady=15, padx=20)

# Şifre onayla label oluşturur
sifre_onayla_label = ctk.CTkLabel(sifre_onayla_cerceve, text='Şifre ', text_color='#fff', corner_radius=10,
                           font=('Pt Mono', 14))
sifre_onayla_label.pack(side=LEFT, padx=(5, 25))

# Sifre onayla giris alanı olusturur
sifre_entry_onayla = ctk.CTkEntry(sifre_onayla_cerceve, placeholder_text='Şifreni onayla', fg_color=fg_color_cerceve,
                           text_color='#fff', corner_radius=10, border_width=0, width=165, show='*')
sifre_entry_onayla.pack(side=LEFT, padx=1)

# Göz ikonu eklenir ve bir Tkinter PhotoImage'a dönüştürülür
eye_icon = Image.open('eye.png')
eye_photo_image = ImageTk.PhotoImage(eye_icon)

# Göz çizgi ikonu eklenir ve bir Tkinter PhotoImage'a dönüştürülür
eye_slash_icon = Image.open('eye.slash.png')
eye_slash_photo_image = ImageTk.PhotoImage(eye_slash_icon)

# Canvas oluşturulur ve arka plan şeffaf yapılır
canvas_eye_onayla = Canvas(sifre_onayla_cerceve, bg='#333', width=35, height=35, highlightthickness=0)
canvas_eye_onayla.pack(side=LEFT, padx=1)

# Canvas oluşturulur ve arka plan şeffaf yapılır
canvas_eye = Canvas(sifre_cerceve, bg='#333', width=35, height=35, highlightthickness=0)
canvas_eye.pack(side=LEFT, padx=1)

# Canvas üzerine göz ikonu eklenir
eye_button_sifre = canvas_eye.create_image(10, 10, anchor='nw', image=eye_photo_image)
canvas_eye.itemconfigure(eye_button_sifre, state='normal')

# Canvas üzerine göz çizgi ikonu eklenir
eye_slash_button_sifre = canvas_eye.create_image(10, 10, anchor='nw', image=eye_slash_photo_image)
canvas_eye.itemconfigure(eye_slash_button_sifre, state='hidden')

# Canvas üzerine göz ikonu eklenir
eye_button_sifre_onayla = canvas_eye_onayla.create_image(10, 10, anchor='nw', image=eye_photo_image)
canvas_eye_onayla.itemconfigure(eye_button_sifre_onayla, state='normal')

# Canvas üzerine göz çizgi ikonu eklenir
eye_slash_button_sifre_onayla = canvas_eye_onayla.create_image(10, 10, anchor='nw', image=eye_slash_photo_image)
canvas_eye_onayla.itemconfigure(eye_slash_button_sifre_onayla, state='hidden')


# Göz ikonuna tıklama olayı ekleyin
def on_eye_click(event):
    sifre_entry.configure(show='')
    canvas_eye.itemconfigure(eye_button_sifre, state='hidden')
    canvas_eye.itemconfigure(eye_slash_button_sifre, state='normal')


def on_eye_slash_click(event):
    sifre_entry.configure(show='*')
    canvas_eye.itemconfigure(eye_button_sifre, state='normal')
    canvas_eye.itemconfigure(eye_slash_button_sifre, state='hidden')


# Göz ikonuna tıklama olayı ekleyin
def on_eye_click_onayla(event):
    sifre_entry_onayla.configure(show='')
    canvas_eye_onayla.itemconfigure(eye_button_sifre_onayla, state='hidden')
    canvas_eye_onayla.itemconfigure(eye_slash_button_sifre_onayla, state='normal')


def on_eye_slash_click_onayla(event):
    sifre_entry_onayla.configure(show='*')
    canvas_eye_onayla.itemconfigure(eye_button_sifre_onayla, state='normal')
    canvas_eye_onayla.itemconfigure(eye_slash_button_sifre_onayla, state='hidden')


canvas_eye.tag_bind(eye_button_sifre, '<Button-1>', on_eye_click)
canvas_eye.tag_bind(eye_slash_button_sifre, '<Button-1>', on_eye_slash_click)

canvas_eye_onayla.tag_bind(eye_button_sifre_onayla, '<Button-1>', on_eye_click_onayla)
canvas_eye_onayla.tag_bind(eye_slash_button_sifre_onayla, '<Button-1>', on_eye_slash_click_onayla)


def kayit_ol():
    if isim_entry.get() and soy_isim_entry.get() and email_entry.get() and sifre_entry.get() and sifre_entry_onayla.get():
        if sifre_entry.get() == sifre_entry_onayla.get():
            print(tdl_database.signup(isim_entry.get(), soy_isim_entry.get(), email_entry.get(), sifre_entry.get()))
        else:
            messagebox.showerror(title='', message='Şifreler eşleşmiyor')
    else:
        messagebox.showerror(title='', message='Bilgiler boş olmamalıdır.')
    print('kayit olundu')


kayit_ol_buton = ctk.CTkButton(panel, text='Kayıt Ol', fg_color='#0052cc', hover_color='#003380', text_color='#fff',
                               corner_radius=10, width=170, command=kayit_ol)
kayit_ol_buton.pack(pady=30, padx=30)


def hesap_varsa_giris_yap():
    signup_page.destroy()
    os.system('python LoginPage.py')


# hesap varsa giriş yap butonu oluşturur
hesap_varsa_giris_yap_buton = ctk.CTkButton(panel, text='Bir hesabın mı var? Giriş Yap!', fg_color='#333',
                                            hover_color='#333', command=hesap_varsa_giris_yap)
hesap_varsa_giris_yap_buton.pack(pady=30, padx=30)

signup_page.mainloop()


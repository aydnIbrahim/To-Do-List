import customtkinter as ctk
from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import askstring

from PIL import ImageTk, Image

import tdl_database

user_id = 1
user_name_surname = ''


class SignupPage:
    def __init__(self):

        self.fg_color = '#333'
        self.fg_color_cerceve = '#ae550c'

        self.signup_page = ctk.CTk()
        self.signup_page.title("Kayıt Ol")
        self.signup_page.geometry('373x620+650+300')
        self.signup_page.grid_propagate(False)
        self.signup_page.resizable(False, False)
        self.signup_page.grid_rowconfigure(0, weight=1)
        self.signup_page.grid_columnconfigure(0, weight=1)

        # panel oluşturma
        self.panel = ctk.CTkFrame(self.signup_page, fg_color=self.fg_color, corner_radius=10)
        self.panel.place(x=15, y=15)

        # Hoşgeldin başlığı
        self.hosgeldin_title = ctk.CTkLabel(self.panel, text="HOŞGELDİN", text_color='#fff', corner_radius=10,
                                            font=('Pt Mono', 40))
        self.hosgeldin_title.pack(pady=(15, 50), fill='x', padx=15)

        # İsim giriş çerçevesi oluşturur
        self.isim_cerceve = ctk.CTkFrame(self.panel, fg_color='#333', corner_radius=10)
        self.isim_cerceve.pack(pady=15, padx=20)

        # İsim label oluşturur
        self.isim_label = ctk.CTkLabel(self.isim_cerceve, text='İsim', text_color='#fff', corner_radius=10,
                                       font=('Pt Mono', 14))
        self.isim_label.pack(side=LEFT, padx=(5, 33))

        # İsim giriş alanı oluşturur
        self.isim_entry = ctk.CTkEntry(self.isim_cerceve, placeholder_text='İsmin', fg_color=self.fg_color_cerceve,
                                       text_color='#fff',
                                       corner_radius=10, border_width=0, width=200)
        self.isim_entry.pack(side=LEFT, padx=5)

        # Soy isim çerçevesi oluşturur
        self.soy_isim_cerceve = ctk.CTkFrame(self.panel, fg_color='#333', corner_radius=10)
        self.soy_isim_cerceve.pack(pady=15, padx=20)

        # Soy isim label oluşturur
        self.soy_isim_label = ctk.CTkLabel(self.soy_isim_cerceve, text='Soy isim', text_color='#fff', corner_radius=10,
                                           font=('Pt Mono', 14))
        self.soy_isim_label.pack(side=LEFT, padx=5)

        # Soy isim giriş alanı oluşturur
        self.soy_isim_entry = ctk.CTkEntry(self.soy_isim_cerceve, placeholder_text='Soy ismin',
                                           fg_color=self.fg_color_cerceve,
                                           text_color='#fff',
                                           corner_radius=10, border_width=0, width=200)
        self.soy_isim_entry.pack(side=LEFT, padx=5)

        # Email giriş çerçevesi
        self.email_cerceve = ctk.CTkFrame(self.panel, fg_color='#333', corner_radius=10)
        self.email_cerceve.pack(pady=15, padx=20)

        # Email label oluşturur
        self.email_label = ctk.CTkLabel(self.email_cerceve, text="E-Posta ", text_color='#fff', corner_radius=10,
                                        font=('Pt Mono', 14))
        self.email_label.pack(side=LEFT, padx=5)

        # Email giriş alanı oluşturur
        self.email_entry = ctk.CTkEntry(self.email_cerceve, placeholder_text='E-Posta adresin',
                                        fg_color=self.fg_color_cerceve,
                                        text_color='#fff', corner_radius=10, border_width=0, width=200)
        self.email_entry.pack(side=LEFT, padx=5)

        # Şifre girişi çerçevesi
        self.sifre_cerceve = ctk.CTkFrame(self.panel, fg_color='#333', corner_radius=10)
        self.sifre_cerceve.pack(pady=15, padx=20)

        # Şifre label oluşturur
        self.sifre_label = ctk.CTkLabel(self.sifre_cerceve, text='Şifre ', text_color='#fff', corner_radius=10,
                                        font=('Pt Mono', 14))
        self.sifre_label.pack(side=LEFT, padx=(5, 25))

        # Sifre giris alanı olusturur
        self.sifre_entry = ctk.CTkEntry(self.sifre_cerceve, placeholder_text='Şifren', fg_color=self.fg_color_cerceve,
                                        text_color='#fff', corner_radius=10, border_width=0, width=165, show='*')
        self.sifre_entry.pack(side=LEFT, padx=1)

        # Şifre onayla girişi çerçevesi
        self.sifre_onayla_cerceve = ctk.CTkFrame(self.panel, fg_color='#333', corner_radius=10)
        self.sifre_onayla_cerceve.pack(pady=15, padx=20)

        # Şifre onayla label oluşturur
        self.sifre_onayla_label = ctk.CTkLabel(self.sifre_onayla_cerceve, text='Şifre ', text_color='#fff',
                                               corner_radius=10, font=('Pt Mono', 14))
        self.sifre_onayla_label.pack(side=LEFT, padx=(5, 25))

        # Sifre onayla giris alanı olusturur
        self.sifre_entry_onayla = ctk.CTkEntry(self.sifre_onayla_cerceve, placeholder_text='Şifreni onayla',
                                               fg_color=self.fg_color_cerceve, text_color='#fff', corner_radius=10,
                                               border_width=0, width=165, show='*')
        self.sifre_entry_onayla.pack(side=LEFT, padx=1)

        # Göz ikonu eklenir ve bir Tkinter PhotoImage'a dönüştürülür
        self.eye_icon = Image.open('eye.png')
        self.eye_photo_image = ImageTk.PhotoImage(self.eye_icon)

        # Göz çizgi ikonu eklenir ve bir Tkinter PhotoImage'a dönüştürülür
        self.eye_slash_icon = Image.open('eye.slash.png')
        self.eye_slash_photo_image = ImageTk.PhotoImage(self.eye_slash_icon)

        # Canvas oluşturulur ve arka plan şeffaf yapılır
        self.canvas_eye_onayla = Canvas(self.sifre_onayla_cerceve, bg='#333', width=35, height=35, highlightthickness=0)
        self.canvas_eye_onayla.pack(side=LEFT, padx=1)

        # Canvas oluşturulur ve arka plan şeffaf yapılır
        self.canvas_eye = Canvas(self.sifre_cerceve, bg='#333', width=35, height=35, highlightthickness=0)
        self.canvas_eye.pack(side=LEFT, padx=1)

        # Canvas üzerine göz ikonu eklenir
        self.eye_button_sifre = self.canvas_eye.create_image(10, 10, anchor='nw', image=self.eye_photo_image)
        self.canvas_eye.itemconfigure(self.eye_button_sifre, state='normal')

        # Canvas üzerine göz çizgi ikonu eklenir
        self.eye_slash_button_sifre = self.canvas_eye.create_image(10, 10, anchor='nw',
                                                                   image=self.eye_slash_photo_image)
        self.canvas_eye.itemconfigure(self.eye_slash_button_sifre, state='hidden')

        # Canvas üzerine göz ikonu eklenir
        self.eye_button_sifre_onayla = self.canvas_eye_onayla.create_image(10, 10, anchor='nw',
                                                                           image=self.eye_photo_image)
        self.canvas_eye_onayla.itemconfigure(self.eye_button_sifre_onayla, state='normal')

        # Canvas üzerine göz çizgi ikonu eklenir
        self.eye_slash_button_sifre_onayla = self.canvas_eye_onayla.create_image(10, 10, anchor='nw',
                                                                                 image=self.eye_slash_photo_image)
        self.canvas_eye_onayla.itemconfigure(self.eye_slash_button_sifre_onayla, state='hidden')

        self.canvas_eye.tag_bind(self.eye_button_sifre, '<Button-1>', self.on_eye_click)
        self.canvas_eye.tag_bind(self.eye_slash_button_sifre, '<Button-1>', self.on_eye_slash_click)

        self.canvas_eye_onayla.tag_bind(self.eye_button_sifre_onayla, '<Button-1>', self.on_eye_click_onayla)
        self.canvas_eye_onayla.tag_bind(self.eye_slash_button_sifre_onayla, '<Button-1>',
                                        self.on_eye_slash_click_onayla)

        self.kayit_ol_buton = ctk.CTkButton(self.panel, text='Kayıt Ol', fg_color='#0052cc', hover_color='#003380',
                                            text_color='#fff', corner_radius=10, width=170, command=self.kayit_ol)
        self.kayit_ol_buton.pack(pady=30, padx=30)

        # hesap varsa giriş yap butonu oluşturur
        self.hesap_varsa_giris_yap_buton = ctk.CTkButton(self.panel, text='Bir hesabın mı var? Giriş Yap!',
                                                         fg_color='#333',
                                                         hover_color='#333', command=self.hesap_varsa_giris_yap)
        self.hesap_varsa_giris_yap_buton.pack(pady=30, padx=30)

        self.signup_page.mainloop()

    # Göz ikonuna tıklama olayı ekleyin
    def on_eye_click(self, event):
        self.sifre_entry.configure(show='')
        self.canvas_eye.itemconfigure(self.eye_button_sifre, state='hidden')
        self.canvas_eye.itemconfigure(self.eye_slash_button_sifre, state='normal')

    def on_eye_slash_click(self, event):
        self.sifre_entry.configure(show='*')
        self.canvas_eye.itemconfigure(self.eye_button_sifre, state='normal')
        self.canvas_eye.itemconfigure(self.eye_slash_button_sifre, state='hidden')

    # Göz ikonuna tıklama olayı ekleyin
    def on_eye_click_onayla(self, event):
        self.sifre_entry_onayla.configure(show='')
        self.canvas_eye_onayla.itemconfigure(self.eye_button_sifre_onayla, state='hidden')
        self.canvas_eye_onayla.itemconfigure(self.eye_slash_button_sifre_onayla, state='normal')

    def on_eye_slash_click_onayla(self, event):
        self.sifre_entry_onayla.configure(show='*')
        self.canvas_eye_onayla.itemconfigure(self.eye_button_sifre_onayla, state='normal')
        self.canvas_eye_onayla.itemconfigure(self.eye_slash_button_sifre_onayla, state='hidden')

    def kayit_ol(self):
        if (self.isim_entry.get() and self.soy_isim_entry.get() and self.email_entry.get() and self.sifre_entry.get()
                and self.sifre_entry_onayla.get()):
            if self.sifre_entry.get() == self.sifre_entry_onayla.get():
                result = tdl_database.signup(self.isim_entry.get(), self.soy_isim_entry.get(), self.email_entry.get(),
                                             self.sifre_entry.get())
                if result:
                    self.signup_page.destroy()
                    login_page_signup = LoginPage()
                    login_page_signup.mainloop()
                else:
                    messagebox.showerror(title='', message="Kayıt işlemi gerçekleştirilemedi.")
            else:
                messagebox.showerror(title='', message='Şifreler eşleşmiyor')
        else:
            messagebox.showerror(title='', message='Bilgiler boş olmamalıdır.')

    def hesap_varsa_giris_yap(self):
        self.signup_page.destroy()
        login_page = LoginPage()
        login_page.mainloop()

    def mainloop(self):
        self.signup_page.mainloop()


class LoginPage:
    def __init__(self):

        self.fg_color = '#333333'
        self.fg_color_cerceve = '#ae550c'

        self.login_page = ctk.CTk()
        self.login_page.title("Giriş Yap")
        self.login_page.geometry('373x440+650+300')
        self.login_page.grid_propagate(False)
        self.login_page.resizable(False, False)
        self.login_page.grid_rowconfigure(0, weight=1)
        self.login_page.grid_columnconfigure(0, weight=1)

        # panel oluşturma
        self.panel = ctk.CTkFrame(self.login_page, fg_color=self.fg_color, corner_radius=10)
        self.panel.place(x=15, y=15)

        # Hoşgeldin başlığı
        self.hosgeldin_title = ctk.CTkLabel(self.panel, text="HOŞGELDİN", text_color='#fff', corner_radius=10,
                                            font=('Pt Mono', 40))
        self.hosgeldin_title.pack(pady=(15, 50), fill='x', padx=15)

        # Email giriş çerçevesi
        self.email_cerceve = ctk.CTkFrame(self.panel, fg_color='#333', corner_radius=10)
        self.email_cerceve.pack(pady=15, padx=20)

        # Email label oluşturur
        self.email_label = ctk.CTkLabel(self.email_cerceve, text="E-Posta ", text_color='#fff', corner_radius=10,
                                        font=('Pt Mono', 14))
        self.email_label.pack(side=LEFT, padx=5)

        # Email giriş alanı oluşturur
        self.email_entry = ctk.CTkEntry(self.email_cerceve, placeholder_text='E-Posta adresin',
                                        fg_color=self.fg_color_cerceve,
                                        text_color='#fff', corner_radius=10, border_width=0, width=200)
        self.email_entry.pack(side=LEFT, padx=5)

        # Şifre girişi çerçevesi
        self.sifre_cerceve = ctk.CTkFrame(self.panel, fg_color='#333', corner_radius=10)
        self.sifre_cerceve.pack(pady=15, padx=20)

        # Şifre label oluşturur
        self.sifre_label = ctk.CTkLabel(self.sifre_cerceve, text='Şifre ', text_color='#fff', corner_radius=10,
                                        font=('Pt Mono', 14))
        self.sifre_label.pack(side=LEFT, padx=(5, 25))

        # Sifre giris alanı olusturur
        self.sifre_entry = ctk.CTkEntry(self.sifre_cerceve, placeholder_text='Şifren', fg_color=self.fg_color_cerceve,
                                        text_color='#fff',
                                        corner_radius=10, border_width=0, width=165, show='*')
        self.sifre_entry.pack(side=LEFT, padx=1)

        # Göz ikonu eklenir ve bir Tkinter PhotoImage'a dönüştürülür
        self.eye_icon = Image.open('eye.png')
        self.eye_photo_image = ImageTk.PhotoImage(self.eye_icon)

        # Göz çizgi ikonu eklenir ve bir Tkinter PhotoImage'a dönüştürülür
        self.eye_slash_icon = Image.open('eye.slash.png')
        self.eye_slash_photo_image = ImageTk.PhotoImage(self.eye_slash_icon)

        # Canvas oluşturulur ve arka plan şeffaf yapılır
        self.canvas_eye = Canvas(self.sifre_cerceve, bg='#333', width=35, height=35, highlightthickness=0)
        self.canvas_eye.pack(side=LEFT, padx=1)

        # Canvas üzerine göz ikonu eklenir
        self.eye_button = self.canvas_eye.create_image(10, 10, anchor='nw', image=self.eye_photo_image)
        self.canvas_eye.itemconfigure(self.eye_button, state='normal')

        # Canvas üzerine göz çizgi ikonu eklenir
        self.eye_slash_button = self.canvas_eye.create_image(10, 10, anchor='nw', image=self.eye_slash_photo_image)
        self.canvas_eye.itemconfigure(self.eye_slash_button, state='hidden')

        self.canvas_eye.tag_bind(self.eye_button, '<Button-1>', self.on_eye_click)
        self.canvas_eye.tag_bind(self.eye_slash_button, '<Button-1>', self.on_eye_slash_click)

        # Giriş Yap butonu oluşturur
        self.giris_yap_buton = ctk.CTkButton(self.panel, text='Giriş Yap', fg_color='#0052cc', hover_color='#003380',
                                             text_color='#fff', corner_radius=10, width=170, command=self.giris_yap)
        self.giris_yap_buton.pack(pady=30, padx=30)

        # Hesap yoksa kayıt ol butonu oluşturur
        self.hesap_yoksa_kayit_ol_buton = ctk.CTkButton(self.panel, text='Bir hesabın yok mu? Hemen kayıt ol!',
                                                        fg_color='#333',
                                                        hover_color='#333', command=self.hesap_yoksa_kayit_ol)
        self.hesap_yoksa_kayit_ol_buton.pack(pady=30, padx=30)

        self.login_page.mainloop()

    # Göz ikonuna tıklama olayı ekleyin
    def on_eye_click(self, event):
        self.sifre_entry.configure(show='')
        self.canvas_eye.itemconfigure(self.eye_button, state='hidden')
        self.canvas_eye.itemconfigure(self.eye_slash_button, state='normal')

    def on_eye_slash_click(self, event):
        self.sifre_entry.configure(show='*')
        self.canvas_eye.itemconfigure(self.eye_button, state='normal')
        self.canvas_eye.itemconfigure(self.eye_slash_button, state='hidden')

    def giris_yap(self):
        if self.email_entry.get() and self.sifre_entry.get():
            email = self.email_entry.get()
            r = tdl_database.signin(email, self.sifre_entry.get())
            if r:
                messagebox.showinfo(title='', message='Giriş başarılı.')
                global user_id
                user_id = int(tdl_database.get_id_no(self.email_entry.get())[0])
                global user_name_surname
                user_name_surname = tdl_database.get_name_surname(self.email_entry.get())
                self.login_page.destroy()
                main_page = MainPage()
                main_page.mainloop()
            else:
                messagebox.showerror(title='', message='Giriş bilgileri eşleşmiyor.')
        else:
            messagebox.showerror(title='', message='Giriş bilgileri boş olmamalıdır.')

    def hesap_yoksa_kayit_ol(self):
        self.login_page.destroy()
        signup_page = SignupPage()
        signup_page.mainloop()

    def mainloop(self):
        self.login_page.mainloop()


class MainPage:

    def __init__(self):
        # Ana pencereyi oluştur
        self.main_page = ctk.CTk()
        self.main_page.title('To Do')
        self.main_page.geometry('800x500+400+300')
        self.main_page.grid_propagate(False)
        self.main_page.grid_rowconfigure(0, weight=1)
        self.main_page.grid_columnconfigure(0, weight=1)
        self.main_page.grid_columnconfigure(1, weight=1)  # Sağ panel için sütun yapılandırması

        # Paneli oluştur
        self.panel = ctk.CTkFrame(self.main_page, fg_color="#333333", corner_radius=10)
        self.panel.place(x=15, y=15)

        # Sağ paneli oluştur
        self.sag_panel = ctk.CTkFrame(self.main_page, fg_color="#333333", corner_radius=10)
        self.sag_panel.place(x=570, y=15)

        # Butonlar için bir çerçeve oluştur
        self.buton_cerceve = ctk.CTkFrame(self.panel, fg_color="#333333", corner_radius=10)
        self.buton_cerceve.pack(pady=5)

        # Tamamla butonunu oluştur ve çerçeveye yerleştir
        self.tamamla_buton = ctk.CTkButton(self.buton_cerceve, text="Tamamla", fg_color="#0052cc",
                                           hover_color="#003380",
                                           text_color="#ffffff", corner_radius=10, width=50, command=self.tamamla_gorev)
        self.tamamla_buton.pack(side=LEFT, padx=5)

        # Sil butonunu oluştur ve çerçeveye yerleştir
        self.sil_buton = ctk.CTkButton(self.buton_cerceve, text="Sil", fg_color="#cc000e", hover_color="#800008",
                                       text_color="#ffffff", corner_radius=10, width=50, command=self.sil_gorev)
        self.sil_buton.pack(side=LEFT, padx=5)

        # Listbox'u oluştur ve stilini ayarla
        self.listbox_task = Listbox(self.panel, bg="#222222", fg="#ffffff", highlightthickness=0, borderwidth=0,
                                    width=60, height=13)
        self.listbox_task.pack(pady=(5, 0), fill='both', expand=True)

        # tamamlanmış görevleri tutan listbox
        self.listbox_completed = Listbox(self.panel, bg="#222222", fg="#ffffff", highlightthickness=0, borderwidth=0,
                                         width=60, height=6)
        self.listbox_completed.pack(pady=(0, 18), fill='both', expand=True)

        # Kullanıcının daha önce kaydedilmiş olan görevlerini döndürür
        global user_id
        result = tdl_database.view_tasks(user_id)
        items = result.split(", ")
        for i in items:
            self.listbox_task.insert(END, i)

        # Kullanıcının daha önce kaydedilen tamamlanmış görevlerini görüntüler
        result_c = tdl_database.view_completed_tasks(user_id)
        items_c = result_c.split(", ")
        for c in items_c:
            self.listbox_completed.insert(END, c)

        # Entry bileşenini oluştur ve stilini ayarla
        self.gorev_entry = ctk.CTkEntry(self.panel, placeholder_text="Görev ekle", fg_color="#444444",
                                        text_color="#ffffff",
                                        corner_radius=10)
        self.gorev_entry.pack(pady=(10, 5), fill='x', padx=10)

        # 'Ekle' butonunu oluştur ve stilini ayarla
        self.ekle_buton = ctk.CTkButton(self.panel, text="Ekle", command=self.ekle_gorev, fg_color="#0052cc",
                                        hover_color="#003380",
                                        text_color="#ffffff", corner_radius=10)
        self.ekle_buton.pack(pady=(5, 20))

        # Yuvarlak buton için Canvas oluştur
        self.canvas_eye = Canvas(self.sag_panel, width=100, height=100, bg="#333333", highlightthickness=0)
        self.canvas_eye.pack(pady=(5, 20), padx=10)

        # Yuvarlak butonu çiz
        self.oval_id = self.canvas_eye.create_oval(10, 10, 90, 90, fill="#2220E2", outline="#0052cc")

        # Buton resmini yükle
        self.buton_resmi = PhotoImage(file="person.png")
        self.canvas_eye.create_image(50, 50, image=self.buton_resmi)

        # Kullanıcı isim alanı
        self.isim_alani = ctk.CTkLabel(self.sag_panel, text=f"{user_name_surname}",
                                       text_color="#ffffff", corner_radius=10, font=('Pt Mono', 22))
        self.isim_alani.pack(pady=(0, 40), fill='x', padx=10)

        # E-posta güncelleme metin giriş alanı
        self.guncelle_eposta_entry = ctk.CTkEntry(self.sag_panel, placeholder_text="Yeni e-posta adresin",
                                                  fg_color="#444444",
                                                  text_color='#fff', corner_radius=10)
        self.guncelle_eposta_entry.pack(pady=5, fill='x', padx=10)

        # 'E-Postanı güncelle' butonunu oluştur
        self.guncelle_eposta_buton = ctk.CTkButton(self.sag_panel, text="E-Postanı güncelle", fg_color="#0052cc",
                                                   hover_color="#003380", text_color="#ffffff", corner_radius=10,
                                                   command=self.email_degis)
        self.guncelle_eposta_buton.pack(pady=5, fill='x', padx=10)

        self.password_cerceve = ctk.CTkFrame(self.sag_panel, fg_color="#333333", corner_radius=10)
        self.password_cerceve.pack(pady=(40, 5), fill='x', padx=1)

        # Şifre güncelleme metin giriş alanı
        self.guncelle_sifre_entry = ctk.CTkEntry(self.password_cerceve, placeholder_text="Yeni şifren",
                                                 fg_color="#444444",
                                                 text_color='#fff', corner_radius=10, width=150, show='*')
        self.guncelle_sifre_entry.pack(side=LEFT, padx=10)

        # Göz ikonunu yükleyin ve bir Tkinter PhotoImage'a dönüştürün
        self.eye_icon = Image.open("eye.png")
        self.eye_photo_image = ImageTk.PhotoImage(self.eye_icon)

        self.eye_slash_icon = Image.open("eye.slash.png")
        self.eye_slash_photo_image = ImageTk.PhotoImage(self.eye_slash_icon)

        # Canvas oluşturun ve arka planını şeffaf yapın
        self.canvas_eye = Canvas(self.password_cerceve, width=40, height=40, bg='#333333', highlightthickness=0)
        self.canvas_eye.pack(side=LEFT, padx=1)

        # Canvas üzerine göz ikonunu ekleyin
        self.eye_button = self.canvas_eye.create_image(10, 10, anchor='nw', image=self.eye_photo_image)
        self.canvas_eye.itemconfigure(self.eye_button, state='normal')

        # Canvas üzerine göz çizgi ikonunu ekleyin
        self.eye_slash_button = self.canvas_eye.create_image(10, 10, anchor='nw', image=self.eye_slash_photo_image)
        self.canvas_eye.itemconfigure(self.eye_slash_button, state='hidden')

        # 'Şifreni güncelle' butonunu oluştur
        self.guncelle_sifre_buton = ctk.CTkButton(self.sag_panel, text="Şifreni güncelle", fg_color="#0052cc",
                                                  hover_color="#003380", text_color="#ffffff", corner_radius=10,
                                                  command=self.sifre_degis)
        self.guncelle_sifre_buton.pack(pady=5, fill='x', padx=10)

        # Çıkış yap butonu oluşturur
        self.cikis_yap_buton = ctk.CTkButton(self.sag_panel, text="Çıkış Yap", fg_color="#cc000e",
                                             hover_color="#800008", text_color="#ffffff", corner_radius=10,
                                             command=self.cikis_yap)
        self.cikis_yap_buton.pack(pady=(40, 20), fill='x', padx=10)

        self.canvas_eye.tag_bind(self.eye_button, '<Button-1>', self.on_eye_click)
        self.canvas_eye.tag_bind(self.eye_slash_button, '<Button-1>', self.on_eye_slash_click)

        # Ana döngüyü başlat
        self.main_page.mainloop()

    def tamamla_gorev(self):
        selected_indicies = self.listbox_task.curselection()
        if selected_indicies:
            selected_item = self.listbox_task.get(selected_indicies[0])
            r = messagebox.askokcancel(title="", message="Bu görevi tamamlamak istediğine emin misin?")
            if r:
                tdl_database.complete_task(user_id, selected_item)
                self.listbox_completed.insert(END, '\u0336'.join(selected_item) + '\u0336')
                self.listbox_task.delete(selected_indicies)
        else:
            messagebox.showerror(title='', message="Önce bir görev seçin")

    def sil_gorev(self):
        selected_indicies_active = self.listbox_task.curselection()
        selected_indicies_completed = self.listbox_completed.curselection()
        if selected_indicies_active:
            selected_item_active = self.listbox_task.get(selected_indicies_active[0])
            r = messagebox.askokcancel(title="", message="Bu görevi silmek istediğine emin misin?")
            if r:
                s = tdl_database.remove_task(user_id, selected_item_active)
                if s:
                    self.listbox_task.delete(selected_indicies_active)
                    messagebox.showinfo(title='', message="Bu görev başarıyla silindi.")
                else:
                    messagebox.showerror(title='', message="Bu görev silirken bir hata oluştu.")
            else:
                messagebox.showinfo(title='', message="Bu görev silinmedi.")
        elif selected_indicies_completed:
            selected_item_completed = self.listbox_completed.get(selected_indicies_completed[0])
            rr = messagebox.askokcancel(title="", message="Bu görevi silmek istediğine emin misin?")
            if rr:
                ss = tdl_database.remove_task(user_id, selected_item_completed)
                if ss:
                    self.listbox_completed.delete(selected_indicies_completed)
                    messagebox.showinfo(title='', message="Bu görev başarıyla silindi.")
                else:
                    messagebox.showerror(title='', message="Bu görev silirken bir hata oluştu.")
            else:
                messagebox.showinfo(title='', message="Bu görev silinmedi.")
        else:
            messagebox.showerror(title='', message="Önce bir görev seçin")

    # Görev ekleme fonksiyonu
    def ekle_gorev(self):
        gorev = self.gorev_entry.get()
        if gorev != "":
            self.listbox_task.insert(END, gorev)
            tdl_database.add_task(user_id, gorev)
            self.gorev_entry.delete(0, END)

    def cikis_yap(self):
        self.main_page.destroy()
        login_page_main = LoginPage()
        login_page_main.mainloop()

    def email_degis(self):
        new_email = self.guncelle_eposta_entry.get()
        if new_email != "":
            old_email = askstring('', "Lütfen önceki email adresinizi giriniz.")
            result = tdl_database.change_email(user_id, old_email, new_email)
            if result:
                messagebox.showinfo(title='', message="E-posta hesabınız başarıyla değiştirilmiştir.")
            else:
                messagebox.showerror(title='', message="İşlem gerçekleştirilemedi.")

    def sifre_degis(self):
        new_sifre = self.guncelle_sifre_entry.get()
        if new_sifre != "":
            old_sifre = askstring('', "Lütfen mevcut şifrenizi giriniz.")
            result = tdl_database.change_password(user_id, old_sifre, new_sifre)
            if result:
                messagebox.showinfo(title='', message="Şifreniz başarıyla güncellenmiştir.")
            else:
                messagebox.showerror(title='', message="İşlem gerçekleştirilemedi.")

    # Göz ikonuna tıklama olayı ekleyin
    def on_eye_click(self, event):
        self.guncelle_sifre_entry.configure(show='')
        self.canvas_eye.itemconfigure(self.eye_button, state='hidden')
        self.canvas_eye.itemconfigure(self.eye_slash_button, state='normal')

    def on_eye_slash_click(self, event):
        self.guncelle_sifre_entry.configure(show='*')
        self.canvas_eye.itemconfigure(self.eye_button, state='normal')
        self.canvas_eye.itemconfigure(self.eye_slash_button, state='hidden')

    def mainloop(self):
        self.main_page.mainloop()


loginPage = LoginPage()
loginPage.mainloop()

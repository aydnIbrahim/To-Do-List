from tkinter import *
from tkinter import messagebox

login_page = Tk()
login_page.title("Giriş yap")
login_page.geometry("700x350+500+350")
login_page.config(bg="#20222E")
login_page.resizable(False, False)

title = Label(login_page, text="GİRİŞ YAP", font=("Pt Mono", 30))
title.config(background="#20222E")
title.place(x=300, y=40)

email_entry = Entry(login_page, font=("Helvetica", 12), width=20)
email_entry.place(x=200, y=150)

password_entry = Entry(login_page, font=("Helvetica", 12), width=20, show='*')
password_entry.place(x=300, y=180)


def login_func():
    username = email_entry.get()
    password = password_entry.get()
    if username == '' and password == '':
        print("Olmaz")
    else:
        print(username, password)


login_button = Button(login_page, text="GİRİŞ", highlightthickness=0, borderwidth=0, border=0, command=login_func)
login_button.config(background='#20222E')
login_button.place(x=300, y=220)

login_page.mainloop()


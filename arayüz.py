from tkinter import *
from tkinter import messagebox

main_page = Tk()
main_page.title("To Do List")
main_page.geometry("700x400+500+350")
main_page.config(bg="#323131")
main_page.resizable(False, False)

frame = Frame(main_page)
frame.place(x=15, y=50)

lb = Listbox(frame, width=95, height=16, font=("Helvetica", 12))
lb.config(background="#20222E")
lb.pack()

title = Label(main_page, text="GÖREVLER", font=("Pt Mono", 20))
title.place(x=300, y=12)

metin = StringVar(main_page, value="Merhaba")
text_field = Text(main_page, width=80, height=2)
text_field.place(x=12, y=300)


def complete_task():
    result = messagebox.askokcancel("?", "Bu görevi tamamlamak istediğine emin misin?", parent=main_page)
    if result:
        value = lb.get(lb.curselection()[0])
        print(value)
    else:
        messagebox.showinfo("", "Görev tamamlanmadı.", parent=main_page)


def delete_task():
    result = messagebox.askokcancel("", "Bu görevi silmek istediğine emin misin?", parent=main_page)
    if result:
        value = lb.get(lb.curselection()[0])
        print(value)
    else:
        messagebox.showinfo("", "Görev tamamlanmadı.", parent=main_page)


def add_task_button():
    if text_field.get("1.0", "end-1c") == "":
        messagebox.showerror("Ekleme Hatası", "Boş görev girilemez", parent=main_page)
    else:
        lb.insert(END, text_field.get("1.0", "end-1c"))
        text_field.delete("1.0", "end-1c")


add_button = Button(main_page, text="Ekle", command=add_task_button, highlightthickness=0, width=7)
add_button.place(x=585, y=302)

complete_button = Button(main_page, text="Tamamla", command=complete_task)
complete_button.place(x=15, y=15)

delete_button = Button(main_page, text="Sil", command=delete_task)
delete_button.place(x=110, y=15)

main_page.mainloop()

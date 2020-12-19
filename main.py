import sqlite3
from tkinter import *
from tkinter import messagebox

db = sqlite3.connect("D://Загрузки//sqlite3//tmp.db")
cursor = db.cursor()
sql_table = """CREATE TABLE IF NOT EXISTS Users (
 Login,
 Password
      )"""
cursor.execute(sql_table)
db.commit()
record = ["Misha", "12345"]
sql_insert = """INSERT INTO Users VALUES (?, ?)"""
cursor.execute(sql_insert, record)
db.commit()
cursor.close()

window = Tk()
window.title("Авторизация пользователя")

lbl_wellcome = Label(window, text="Авторизация")
lbl_wellcome.grid(column=0, row=0)
lbl_login = Label(window, text="Логин")
lbl_login.grid(column=0, row=1)
lbl_password = Label(window, text="Пароль")
lbl_password.grid(column=0, row=2)

login_text = Entry(window)
login_text.grid(column=1, row=1)
pass_text = Entry(window)
pass_text.grid(column=1, row=2)


def clicked():
    db = sqlite3.connect("D://Загрузки//sqlite3//tmp.db")
    cursor = db.cursor()
    sql = "SELECT * FROM Users"
    cursor.execute(sql)
    users = cursor.fetchall()
    flag = False
    for user in users:
        if user[0] == login_text.get() and user[1] == pass_text.get():
            messagebox.showinfo('Оповещение', 'Вход успешен')
            flag = True
    if not flag:
        messagebox.showerror('Ошибка', 'Неверный пароль или логин')


btn_valid = Button(window, text="Войти", command=clicked)
btn_valid.grid(column=0, row=3)

window.geometry("250x100")
window.mainloop()

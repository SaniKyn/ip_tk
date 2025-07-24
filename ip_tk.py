from tkinter import *
from tkinter import ttk
import webbrowser

from database.dbsql.sql_get_links import get_link

 
def click_button():
    link = webbrowser.open_new_tab(get_link(name='METANIT'))
    # изменяем текст на кнопке
    btn["text"] = f"Clicks {link}"   


root = Tk() # корневой объект окна
root.geometry("500x500")

btn = ttk.Button(text="Send", command=click_button) # Создал кнопку. Также добавили пакет ttk по факту меняет только внешний вид 
btn.pack()    # размещаем кнопку в окне
btn["text"] = "Send" # Можно вне настроить параметры, используя имя переменной виджета и синтаксис словарей


root.mainloop()
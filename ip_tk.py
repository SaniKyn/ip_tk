from tkinter import *
from tkinter import ttk
import webbrowser


 
def click_button():
    links = webbrowser.open_new_tab("https://metanit.com/")
    # изменяем текст на кнопке
    btn["text"] = f"Clicks {links}"   


root = Tk() # корневой объект окна
root.geometry("500x500")

btn = ttk.Button(text="Send", command=click_button) # Создал кнопку. Также добавили пакет ttk по факту меняет только внешний вид 
btn.pack()    # размещаем кнопку в окне
btn["text"] = "Send" # Можно вне настроить параметры, используя имя переменной виджета и синтаксис словарей


root.mainloop()
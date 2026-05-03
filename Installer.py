import tkinter as tk
from tkinter import messagebox
import webbrowser
import time

def start_installer():
    root = tk.Tk()
    root.withdraw() # Скрываем основное окно

    # Сценарий общения
    messagebox.showinfo("Установщик", "Добро пожаловать в установку CheatPanel v2.0!")
    time.sleep(1)
    
    if messagebox.askyesno("Вопрос", "Вы готовы активировать читы и доминировать в игре?"):
        messagebox.showwarning("Система", "Обнаружен конфликт. Нужно загрузить патч безопасности.")
        messagebox.showinfo("Загрузка", "Сейчас откроется страница загрузки панели. Установите её вручную.")
        
        # Ссылка на вторую программу (например, на твой GitHub)
        webbrowser.open("https://github.com")
        
        messagebox.showinfo("Статус", "Установщик завершит работу после скачивания.")
    else:
        messagebox.showerror("Ошибка", "Отказ в доступе. Установка прервана.")
    
    root.destroy()

if __name__ == "__main__":
    start_installer()

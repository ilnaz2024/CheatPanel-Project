import tkinter as tk
from tkinter import messagebox
import random
import webbrowser
import time

# Настройки хаоса
phrases = ["Привет!", "Лоооооох", "Это мой комп!", "Отдай комп!", "Хакер, верни комп!", "Иван победил!"]
links = ["https://google.com"]

def run_revenge():
    """Финальная стадия: спам окнами и браузером"""
    def spawn():
        top = tk.Toplevel()
        top.title("SYSTEM ERROR")
        top.attributes('-topmost', True)
        top.geometry(f"+{random.randint(0, 800)}+{random.randint(0, 500)}")
        
        tk.Label(top, text=random.choice(phrases), fg="red", font=("Arial", 12)).pack(padx=20, pady=20)
        
        # Наказание браузером (шанс 20%)
        if random.random() < 0.2:
            webbrowser.open(random.choice(links))
        
        top.after(400, spawn)
    spawn()

def start_cheat_panel():
    root = tk.Tk()
    root.withdraw()

    # 1. Предупреждение
    choice = messagebox.askquestion("Внимание", "Вы хотите активировать чит? Осторожно, говорят, панель взломана неизвестным... Продолжить?")
    
    if choice == 'yes':
        # 2. Сообщение от Ивана
        messagebox.showwarning("!!!", "На ваш комп зашел мальчик Иван 03.03.1998. Он поиграет и отдаст!")
        
        # 3. Имитация «нашего» взлома (пропустим для краткости или вставь код из прошлого ответа)
        print("Взлом Ивана запущен...")
        
        # 4. Хаос
        run_revenge()
    else:
        messagebox.showinfo("Удача", "Мудрое решение. Программа закрыта.")
        root.destroy()

    root.mainloop()

if __name__ == "__main__":
    start_cheat_panel()

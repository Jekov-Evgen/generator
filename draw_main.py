from tkinter import *
from tkinter import ttk
from random import randint

def error():
    info = Tk()
    
    Label(info, text="Вы ввели неверные значения", font="30").grid(row=0, column=0, padx=10, pady=10)
    Button(int, text="ОК", width=50).grid(row=1, column=0, padx=10, pady=10)

class MainWindow:
    def __init__(self) -> None:
        self.root = Tk()
        self.root.title("Генератор чисел")
        frm = ttk.Frame(self.root, padding=10)
        frm.grid()
        
        ttk.Label(text="Введите нижнию грпницу", font="30").grid(row=0, column=0, padx=10, pady=10)
        self.lower_limit = ttk.Entry(width=50)
        self.lower_limit.grid(row=1, column=0, padx=10, pady=10)
        
        ttk.Label(text="Введите верхнюю границу", font="30").grid(row=2, column=0, padx=10, pady=10)
        self.upper_limit = ttk.Entry(width=50)
        self.upper_limit.grid(row=3, column=0, padx=10, pady=10)
        
        ttk.Label(text="Введите количество генерируемых чисел", font="30").grid(row=4, column=0 ,padx=10, pady=10)
        self.quantity = ttk.Entry(width=50)
        self.quantity.grid(row=5, column=0, padx=10, pady=10)
        
        ttk.Button(text="Сгенерировать", width=50, command=self.generator).grid(row=6, column=0 ,padx=10, pady=10)
        
        
    def run(self):
        self.root.mainloop()
        
    def generator(self):
        try:
            bottom = int(self.lower_limit.get())
            up = int(self.upper_limit.get())
            quantity = int(self.quantity.get())
        except:
            error()
            
        res = Tk()
        count = 0
        
        for i in range(0, quantity):
            count += 1
            rand = randint(bottom, up)
            Label(res, text=f"{rand}", font="15").grid(row=i, column=0, padx=10, pady=10)
            
        Button(res, text="Выйти", width=50, command=res.destroy).grid(row=count + 1, column=0, padx=10, pady=10)
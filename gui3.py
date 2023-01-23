import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("tk")
        self.geometry('300x50')
        self.label = ttk.Label(self, text='UAS Bahasa Pemrograman')
        self.label.pack()

        self.button = ttk.Button(self, text='klik disini')
        self.button['command'] = self.button_click
        self.button.pack()

    def button_click(self):
        showinfo(title='info', message='20210801197 \n Ananda Dwi Rizkyta \n Teknik Informatika')

if __name__ == "__main__":
    app = App()
    app.mainloop()
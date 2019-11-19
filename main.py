import tkinter as tk
from app import App

if __name__ == '__main__':

    my_window = tk.Tk()
    my_window.title("Conversie tool")
    my_window.geometry("500x500")
    frame_a = App(my_window)
    frame_a.grid(row=0, column=0)
    my_window.mainloop()

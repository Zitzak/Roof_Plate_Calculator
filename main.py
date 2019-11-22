import tkinter as tk
from app import App

if __name__ == '__main__':

	my_window = tk.Tk()
	my_window.title("Conversie tool")

	frame_calculator = App(my_window)

	screen_width = my_window.winfo_screenwidth()
	screen_height =  my_window.winfo_screenheight()

	start_x_coordinates = (screen_width / 2) - (screen_width / 16)
	start_y_coordinates = (screen_height / 2) - (screen_height / 3)

	my_window.geometry("+%d+%d" % (start_x_coordinates, start_y_coordinates))
	my_window.resizable(0,0)
	frame_calculator.grid(row=0, column=0)

	my_window.mainloop()

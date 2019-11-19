import tkinter as tk
import re
from roof_plate_converter import RoofPlateConverter


class App(tk.Frame, RoofPlateConverter):

	def __init__(self, the_window):
		tk.Frame.__init__(self, the_window)
		self.converter = RoofPlateConverter()
		# test = [[110, 130], [130, 150], [150, 170], [170, 190], [190, 210]]
		# self.size_roof = dict.fromkeys((item[0] for item in test), False)
		self.format_string_example = "Input format verkeerd.\nGebruik alleen " \
									"getallen met één streep(-) ertussen.\nDe getallen mogen" \
									" alleen een verschil van 10 of 20\nhebben die bij alle maten gelijk moet zijn." \
									"\n\nVoorbeeld 1:\n170-190\n190-210\n210-230\n\nVoorbeeld 2:\n150-160\n160-170\n" \
									"170-180"

		self.ask_size_label = tk.Label(self, text="Vul hier de maten in")
		self.text_field = tk.Text(the_window, height=20, width=53)
		self.button = tk.Button(self, text="Converteren", command=self.validate_input)

		self.ask_size_label.grid(row=0, column=0)
		self.text_field.grid(row=1, columnspan=1, padx=10, pady=10)
		self.button.grid(row=2, column=0)

	def validate_input(self):

		user_input = self.text_field.get(1.0, "end")
		user_input = re.split("[-\n]", user_input)
		while True:
			try:
				user_input.remove('')
			except:
				break
		if all(x.isdigit() for x in user_input) is False or not user_input:
			self.display_output(self.format_string_example)
		else:
			user_input = [int(value) for value in user_input]
			diff = abs(user_input[0] - user_input[1])
			for i, j in zip(user_input[:], user_input[2:]):
				if abs(i - j) is not diff:
					self.display_output(self.format_string_example)
			self.run_converter(user_input, diff)

	def run_converter(self, user_input, diff):
		self.converter.make_dicts(user_input, diff)
		self.converter.run()
		self.converter.print_test_final()

		# else:
		#     # self.pl
		#     self.plates.make_vars(20, self.size_roof)
		#     self.plates.run()
		#     self.plates.print_test_final()

	def display_output(self, strig):
		self.text_field.delete(1.0, "end")
		self.text_field.insert(1.0, strig)

# 110-130
# 130-150
# 150-170
# 170-190
# 190-210

# def input_to_backend(win):

# print("test")
# win.display_output2("3 x 100\n1 x 150 - 170\n1 x 170 - 190\n1 x 110 - 130")
# def display_output(win):
# 	test = win.tekst.get(1.0, "end")
# 	test = re.split("[-\n\0]", test)
# 	test.pop()
# 	if all(x.isdigit() for x in test) is False:
# 		w
# test = [x for x in test if x.isdigit()]


# lambda win=self: display_output(win)

# test.pop()
# if test is False
# 	print("False")
# for x in test:
# 	try:
# 		int(x)
# 	except:
# 		test.remove(x)
# test = int(test)
# print(test)
# win.display_output2("3 x 100\n1 x 150 - 170\n1 x 170 - 190\n1 x 110 - 130")

# my_window = tk.Tk()
# my_window.title("Dak platen omrekenen")
# my_window.geometry("400x400")
# frame_a = AppInterface(my_window)
# frame_a.config(width=500)

# frame_a.grid(row=0, column=0)

# my_window.mainloop()

# 150-170
# 170-190
# 210-230

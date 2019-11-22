import tkinter as tk
import re
from roof_plate_calculator import RoofPlateCalculator


class App(tk.Frame, RoofPlateCalculator):

	def __init__(self, the_window):
		super().__init__()
		self.output_str = None
		self.calculator = None
		self.diff = None
		self.user_input = None
		self.format_string_example = "Input format verkeerd.\nGebruik alleen " \
									"getallen met één streep(-) ertussen.\nDe getallen mogen" \
									" alleen een verschil van 10 of 20\nhebben die bij alle maten gelijk moet zijn." \
									"\n\nVoorbeeld 1:\n170-190\n190-210\n210-230\n\nVoorbeeld 2:\n150-160\n160-170\n" \
									"170-180"

		self.ask_size_label = tk.Label(self, text="Vul hieronder de maten in")
		self.text_field = tk.Text(the_window, height=30, width=55)
		self.button = tk.Button(self, text="Converteren", command=self.run_calculator)

		self.ask_size_label.grid(row=0, column=0, columnspan=1)
		self.text_field.grid(row=2, column=0, columnspan=1, padx=10, pady=10)
		self.button.grid(row=1, column=0, columnspan=1)
		self.text_field.focus()

	def get_and_split_input(self):

		user_input = self.text_field.get(1.0, "end")
		user_input = re.split("[-\n]", user_input)
		while True:
			try:
				user_input.remove('')
			except:
				break
		return user_input

	def validate_input(self):

		if all(x.isdigit() for x in self.user_input) is False or not self.user_input:
			self.output_format_string_example()
		else:
			self.user_input = [int(value) for value in self.user_input]
			self.diff = abs(self.user_input[0] - self.user_input[1])
			for i, j in zip(self.user_input[:], self.user_input[2:]):
				if abs(i - j) is not self.diff:
					self.output_format_string_example()
					return False
			return True

	def format_output(self):

		self.output_str = "Na conversie\n---------------\n\nRechte platen:\n"
		for keys, value in self.calculator.final_flat_plate.items():
			if value is not 0:
				self.output_str = self.output_str + str(keys) + "\t-\tx " + str(value) + "\n"
		self.output_str = self.output_str + "\nSchuine platen:\n"
		for keys, value in self.calculator.final_sloping_plate.items():
			if value is not 0:
				self.output_str = self.output_str + str(keys) + "-" + str((int(keys) + self.diff)) + "\t-\tx " + str(value) + "\n"

	def run_calculator(self):
		self.user_input = self.get_and_split_input()
		if self.validate_input() is True:
			self.calculator = RoofPlateCalculator(self.user_input, self.diff)
			self.calculator.run()
			self.format_output()
			self.display_output_str()

	def display_output_str(self):

			self.text_field.insert(1.0, "Voor conversie\n---------------\n\n")
			self.text_field.insert("end", "\n\n\n" + self.output_str)

	def output_format_string_example(self):

		self.text_field.delete(1.0, "end")
		self.text_field.insert(1.0, self.format_string_example)



#Voorbeelden
# 110-130
# 130-150
# 150-170
# 170-190
# 190-210

# 130-150
# 150-170
# 170-190
# 190-210
# 210-230
# 230-250
import tkinter as tk
import re
from roof_plate_converter import RoofPlateConverter


class App(tk.Frame, RoofPlateConverter):

	def __init__(self, the_window):
		super().__init__()
		self.output_str = ""
		self.format_string_example = "Input format verkeerd.\nGebruik alleen " \
									"getallen met één streep(-) ertussen.\nDe getallen mogen" \
									" alleen een verschil van 10 of 20\nhebben die bij alle maten gelijk moet zijn." \
									"\n\nVoorbeeld 1:\n170-190\n190-210\n210-230\n\nVoorbeeld 2:\n150-160\n160-170\n" \
									"170-180"

		self.ask_size_label = tk.Label(self, text="Vul hieronder de maten in")
		self.text_field = tk.Text(the_window, height=30, width=55)
		self.text_field.config(relief='sunken')
		self.button = tk.Button(self, text="Converteren", command=self.validate_input)

		self.ask_size_label.grid(row=0, column=0, columnspan=1)
		self.text_field.grid(row=2, column=0, columnspan=1, padx=10, pady=10)
		self.button.grid(row=1, column=0, columnspan=1)
		self.text_field.focus()

	def validate_input(self):

		user_input = self.text_field.get(1.0, "end")
		user_input = re.split("[-\n]", user_input)
		while True:
			try:
				user_input.remove('')
			except:
				break
		if all(x.isdigit() for x in user_input) is False or not user_input:
			self.display_output(self.format_string_example, False)
		else:
			user_input = [int(value) for value in user_input]
			diff = abs(user_input[0] - user_input[1])
			for i, j in zip(user_input[:], user_input[2:]):
				if abs(i - j) is not diff:
					self.display_output(self.format_string_example, False)
					return
			self.run_converter(user_input, diff)

	def format_output(self, diff, flat_plates, sloping_plates):

		self.output_str = "Na conversie\n---------------\n\nRechte platen:\n"
		for keys, value in flat_plates.items():
			if value is not 0:
				self.output_str = self.output_str + str(keys) + "\tx " + str(value) + "\n"
		self.output_str = self.output_str + "\nSchuine platen:\n"
		for keys, value in sloping_plates.items():
			if value is not 0:
				self.output_str = self.output_str + str(keys) + "-" + str((int(keys) + diff)) + "\tx " + str(value) + "\n"
		self.display_output(self.output_str, True)

	def run_converter(self, user_input, diff):
		converter = RoofPlateConverter(user_input, diff)
		converter.run()
		self.format_output(diff, converter.final_flat_plate, converter.final_sloping_plate)

	def display_output(self, string, end):

		if end is False:
			self.text_field.delete(1.0, "end")
			self.text_field.insert(1.0, string)
		else:
			self.text_field.insert(1.0, "Voor conversie\n---------------\n\n")
			self.text_field.insert("end", "\n\n\n" + string)


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
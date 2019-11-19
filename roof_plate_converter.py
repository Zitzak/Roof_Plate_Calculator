class RoofPlateConverter:
	
	def __init__(self, user_input, diff):

		self.sloping_plate_options_10 = [[30, 40], [40, 50], [50, 60], [60, 70], [70, 80], [80, 90], [90, 100], [100, 110]]
		self.sloping_plate_options_20 = [[30, 50], [50, 70], [70, 90], [90, 110], [110, 130]]
		self.flat_plates_options = [30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 142]
		self.sloping_plate = self.make_sloping_plates_dict(diff)
		self.flat_plate = dict.fromkeys(self.flat_plates_options, 0)
		self.size_roof = user_input[::2]
		self.size_roof = dict.fromkeys(self.size_roof, False)
		self.final_flat_plate = []
		self.final_sloping_plate = []

	# def print_test(self):
	# 	print("size roof			", self.size_roof)
	# 	print("slopping roof plates 		", self.sloping_plate)
	# 	print("flat roof plates		", self.flat_plate)
	#
	# def print_test_final(self):
	# 	print("Final sloping plates 		", self.final_sloping_plate)
	# 	print("Final flat plates		", self.final_flat_plate)

	def make_sloping_plates_dict(self, diff):

		if diff == 10:
			sloping_plate = dict.fromkeys((item[0] for item in self.sloping_plate_options_10), 0)
		else:
			sloping_plate = dict.fromkeys((item[0] for item in self.sloping_plate_options_20), 0)
		return sloping_plate

	def check_option_only_one_plate(self):

		for sizes_needed in self.size_roof:
			for size_available in self.sloping_plate:
				if sizes_needed == size_available:
					self.size_roof[sizes_needed] = True
					self.sloping_plate[size_available] +=1

	def check_option_only_sloped_plate(self, size_needed, current_size_flat):

		for size_available in self.sloping_plate:
			if ((size_needed - current_size_flat) - size_available) == 0:
				self.sloping_plate[size_available] += 1
				self.size_roof[size_needed] = True
				return True
		return False

	def check_all_input(self, current_size_flat):

		temp = current_size_flat
		self.check_option_only_one_plate()
		while True:
			for sizes_needed in self.size_roof:
				if self.size_roof[sizes_needed] is not True:
					if self.check_option_only_sloped_plate(sizes_needed, temp) is True:
						self.flat_plate[current_size_flat] += (temp // current_size_flat)
					if all(x == False for x in self.size_roof) or all(x == True for x in self.size_roof):
						return
			temp = temp * 2
			if (temp // current_size_flat) > 10:
				return

	def clear_all(self):

		for keys in self.flat_plate:
			self.flat_plate[keys] = 0
		for keys in self.sloping_plate:
			self.sloping_plate[keys] = 0
		for keys in self.size_roof:
			self.size_roof[keys] = False

	def run(self):

		for current_size_flat in self.flat_plate:
			self.check_all_input(current_size_flat)
			if all(x==True for x in self.size_roof.values()):
				self.final_flat_plate = self.flat_plate.copy()
				self.final_sloping_plate = self.sloping_plate.copy()
			self.clear_all()

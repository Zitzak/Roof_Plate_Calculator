class RoofPlateCalculator:
	
	def __init__(self, user_input, diff):
		''' Initiates the sizes of roof plates avalible aswell as the sizes needed for calculation.'''
		self.sloping_plate_options_10 = [[30, 40], [40, 50], [50, 60], [60, 70], [70, 80], [80, 90], [90, 100], [100, 110]]
		self.sloping_plate_options_20 = [[30, 50], [50, 70], [70, 90], [90, 110], [110, 130]]
		self.flat_plates_options = [30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 142]
		self.sloping_plate = self.make_sloping_plates_dict(diff)
		self.flat_plates = dict.fromkeys(self.flat_plates_options, 0)
		self.size_roof = user_input[::2]
		self.size_roof = dict.fromkeys(self.size_roof, False)
		self.final_flat_plate = None
		self.final_sloping_plate = None

	# def print_test(self):
	# 	print("size roof			", self.size_roof)
	# 	print("slopping roof plates 		", self.sloping_plate)
	# 	print("flat roof plates		", self.flat_plates)
	#
	# def print_test_final(self):
	# 	print("Final sloping plates 		", self.final_sloping_plate)
	# 	print("Final flat plates		", self.final_flat_plate)

	def make_sloping_plates_dict(self, diff):
		'''Creates dict from sloping_plate_options for to be used in calculations.'''
		if diff == 10:
			sloping_plate = dict.fromkeys((item[0] for item in self.sloping_plate_options_10), 0)
		else:
			sloping_plate = dict.fromkeys((item[0] for item in self.sloping_plate_options_20), 0)
		return sloping_plate

	def get_matching_sloping_plate_without_flat_plate(self):
		'''Loops through all slooping plates to find match, without flat plate.'''
		for sizes_needed in self.size_roof:
			for size_available in self.sloping_plate:
				if sizes_needed == size_available:
					self.size_roof[sizes_needed] = True
					self.sloping_plate[size_available] +=1

	def get_matching_sloped_plate(self, size_needed, current_size_flat_plate):
		'''Loops through all sloping plates to find one that fits.'''
		for size_available in self.sloping_plate:
			if ((size_needed - current_size_flat_plate) - size_available) == 0:
				self.size_roof[size_needed] = True
				self.sloping_plate[size_available] += 1
				return True
		return False

	def get_matching_sizes(self, current_size_flat_plate):
		'''Try fitting 1 plate for size then loops through size_roof and sends to method that checks 
		for matching sloping_plate. Returns if all True, all False or temp is to high.'''
		temp_current_size_flat_plate = current_size_flat_plate
		self.get_matching_sloping_plate_without_flat_plate()
		while True:
			for sizes_needed in self.size_roof:
				if self.size_roof[sizes_needed] is False:
					if self.get_matching_sloped_plate(sizes_needed, temp_current_size_flat_plate) is True:
						self.flat_plates[current_size_flat_plate] += (temp_current_size_flat_plate // current_size_flat_plate)
					if all(x == False for x in self.size_roof) or all(x == True for x in self.size_roof):
						return
			temp_current_size_flat_plate = temp_current_size_flat_plate * 2
			if (temp_current_size_flat_plate // current_size_flat_plate) > 10:
				return

	def clear_all(self):
		'''Sets all dicts back to False or zero(0).'''
		for keys in self.flat_plates:
			self.flat_plates[keys] = 0
		for keys in self.sloping_plate:
			self.sloping_plate[keys] = 0
		for keys in self.size_roof:
			self.size_roof[keys] = False

	def run(self):
		''' Loops through flat plates avalible and sends each iter to get_maching_sizes, then checks if all sizes are found and if so, stores them.'''
		for current_size_flat_plate in self.flat_plates:
			self.get_matching_sizes(current_size_flat_plate)
			if all(x==True for x in self.size_roof.values()):
				self.final_flat_plate = self.flat_plates.copy()
				self.final_sloping_plate = self.sloping_plate.copy()
			self.clear_all()

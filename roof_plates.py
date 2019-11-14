class	RoofPlates():
	
	def __init__(self):

		self.print_sloping_plate_10 = [[30, 40], [40, 50], [50, 60], [60, 70], [70, 80], [80, 90], [90, 100], [100, 110]]
		self.print_sloping_plate_20 = [[30, 50], [50, 70], [70, 90], [90, 110], [110, 130]]
		self.print_flat_plate = [30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 142]

		self.final_flat_plate = []
		self.final_sloping_plate = []

	def print_test(self):
		print("size roof			", self.size_roof)
		print("slopping roof plates 		", self.sloping_plate)
		print("flat roof plates		", self.flat_plate)

	def print_test_final(self):
		print("Final sloping plates 		", self.final_sloping_plate)
		print("Final flat plates		", self.final_flat_plate)

	def make_vars(self, difference, size_roof):

		if difference == 10:
			self.sloping_plate = dict.fromkeys((item[0] for item in self.print_sloping_plate_10), 0)
		else:
			self.sloping_plate = dict.fromkeys((item[0] for item in self.print_sloping_plate_20), 0)
		self.flat_plate = dict.fromkeys(self.print_flat_plate, 0)
		self.sloping_plate[70] = 50
		self.size_roof = size_roof

	def	check_option_only_one_plate(self):

		for sizes_needed in self.size_roof:
			for size_avalible in self.sloping_plate:
				if sizes_needed == size_avalible:
					self.size_roof[sizes_needed] = True
					self.sloping_plate[size_avalible] +=1



	def	check_option_only_sloped_plate(self, size_needed, current_size_flat):

		for size_avalible in self.sloping_plate:
			if ((size_needed - current_size_flat) - size_avalible) == 0:
				self.sloping_plate[size_avalible] +=1
				self.size_roof[size_needed] = True
				# self.flat_plate[current_size_flat] +=1
				return True
		return False



	def	check_all_input(self, current_size_flat):

		temp = current_size_flat
		self.check_option_only_one_plate()
		boo = True
		while boo:

			# print("test", self.size_roof)
			for sizes_needed in self.size_roof:
				if self.size_roof[sizes_needed] != True:
					if self.check_option_only_sloped_plate(sizes_needed, temp) is True:
						self.flat_plate[current_size_flat] += (temp // current_size_flat)

					if all(x==False for x in self.size_roof.values()) or all(x==True for x in self.size_roof.values()):
						print("test2", current_size_flat)
						self.print_test()
						return
			temp = temp * 2
			if (temp // current_size_flat) > 10:
				print("test1", self.size_roof, current_size_flat)
				return
					# if all(x==True for x in self.size_roof.values()):
					# 	return
					
	def	clear_all(self):

		for keys in self.flat_plate:
			self.flat_plate[keys] = 0
		for keys in self.sloping_plate:
			self.sloping_plate[keys] = 0
		for keys in self.size_roof:
			self.size_roof[keys] = False


	def run(self):

		# boo = True

		for current_size_flat in self.flat_plate:
			print(current_size_flat)
			self.print_test()
			print("\n")
			self.check_all_input(current_size_flat)
			if all(x==True for x in self.size_roof.values()):
				print("update final", current_size_flat)
				self.final_flat_plate = self.flat_plate.copy()
				self.final_sloping_plate = self.sloping_plate.copy()
				# print("all True")
				# return
			self.clear_all()
			
			
		# while boo:
		# 	for elem in self.size_roof:
		# 		print(self.size_roof)
		# 		self.size_roof[elem] = True
		# 		if all(x==True for x in self.size_roof.values()):
		# 			boo = False
		# print("test")
		# for elem in self.size_roof:
		# 	self.size_roof[elem] = True
		# if all(x==True for x in self.size_roof.values()):
		# 	print(True)
		# else:
		# 	print(False)


		# self.test(self.size_roof)
						
		# print(self.size_roof)


	# def test(self):

	# 	for key in self.flat_plate:
	# 		for value in self.size_roof:
	# 			if (value - key) > 0:
	# 				for key1 in self.sloping_plate:
	# 					if (value - key - key1) == 0:
	# 						self.flat_plate[key] +=1
	# 						self.sloping_plate[key1] = +1
							
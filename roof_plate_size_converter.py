from roof_plates import RoofPlates


if __name__ == '__main__':
	test = [[110, 130], [130, 150], [150, 170], [170, 190], [190, 210]]  ## <---------
	# test = [[130, 150], [150, 170], [170, 190], [190, 210], [210, 230], [230, 250]]  ## <---------
	plates = RoofPlates()
	size_roof = dict.fromkeys((item[0] for item in test), False)
	difference = abs(test[0][0] - test[0][1])
	if difference == 10:
		plates.make_vars(difference, size_roof)
	elif difference == 20:
		plates.make_vars(difference, size_roof)
	else:
		pass ##<-------- Invalid difference


	# test2 = [n[0] for n in test]
	plates.run()
	# plates.make_dict_from_plates(abs(test[0][0] - test[0][1]))
	print("FINAL")
	plates.print_test_final()
	# print(size_roof)
	# print(plates.flat_plate)
	# print(plates.sloping_plate)
	
	
	
	#Clear all dic
	
	# plates.sloping_plate = dict.fromkeys(plates.sloping_plate, 0)
	# print(plates.sloping_plate)

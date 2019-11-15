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



	plates.run()

	print("FINAL")
	plates.print_test_final()



def print_test(flat, difference):

	for keys, value in flat.items():
		if value is not 0:
			print(keys, (int(keys) + difference), sep="-", end='\tx')
			print(value)

if __name__ == '__main__':

	test = [110, 130, 130, 150, 150, 170, 170, 190, 190, 210]

	test2 = test[::2]
	test2.append(test[-1])

	flat = {30: 0, 40: 0, 50: 0, 60: 0, 70: 0, 80: 6, 90: 0, 100: 0, 110: 0, 120: 0, 142: 0}
	sloping = {30: 2, 40: 0, 50: 1, 60: 0, 70: 1, 80: 0, 90: 1, 100: 0}
	print_test(sloping, 20)

	# print(test2, sloping, flat, sep='\n')
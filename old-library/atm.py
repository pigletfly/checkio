def checkio(balance,withdraw):
	left = balance
	for draw in withdraw:
		if draw < 0:
			break
		if draw + 1 > balance:
			continue
		if draw % 5 !=0:
			continue
		left = left - draw - 1
	return left


if __name__ == "__main__":
	print checkio(120, [10, 20, 30]) == 57
	print checkio(120, [200, 10]) == 109
	print checkio(120, [3, 10]) == 109
	print checkio(120, [200 , 119]) == 120
	print checkio(120, [120, 10, 122, 2, 10, 10, 30, 1]) == 56
	print checkio(120, [-10]) == 120
	print checkio(100,[100,-10]) == 100

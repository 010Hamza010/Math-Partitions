from math import floor, ceil

def P(Number, Start=2):
	Sum = 0

	for index in range(Start, Number+1):
		Sum += floor(Number/index)

		if ceil(Number/2) > index:
			Sum += P(Number - index, index) - floor((Number - index)/index) - 1

	Sum += 1

	return Sum


def main():
	n = int(input('>>> '))

	print(P(n))

if __name__ == '__main__':
	main()

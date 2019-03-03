# -*- coding: utf-8 -*-
class LockPicker(object):

	def __init__(self, sticky_number, first_guess, second_guess):
		self.sticky_number = sticky_number
		self.first_guess = first_guess
		self.second_guess = second_guess
		self.sticky_remainder = sticky_number%4

	def __generate_guess_list(self, initial_guess):
		guess_list = []
		for multiple in range(0,4):
			guess = initial_guess + 10*multiple
			if guess%4 == self.sticky_remainder:
				guess_list.append(guess)
		return guess_list


	def generate_combination(self):
		first_digit = self.sticky_number + 5
		third_guess_list = []

		third_guess_list.extend(self.__generate_guess_list(initial_guess=self.first_guess))
		third_guess_list.extend(self.__generate_guess_list(initial_guess=self.second_guess))

		second_digit_base_two = self.sticky_remainder + 2
		second_digit_base_six = self.sticky_remainder + 6
		second_guess_list = [second_digit_base_two, second_digit_base_six]

		for _ in range(0,4): 
			second_digit_base_two += 8
			second_digit_base_six += 8 
			second_guess_list.append(second_digit_base_two)
			second_guess_list.append(second_digit_base_six)

		return (first_digit, second_guess_list, third_guess_list)

def main(): 
	picker = LockPicker(sticky_number=6, first_guess=1, second_guess=8)
	possible_combination = picker.generate_combination()
	print("First Digit: {f}".format(f=possible_combination[0]))
	print("Second Digit: {s}".format(s = possible_combination[1]))
	print("Third Digit: {t}".format(t=possible_combination[2]))


if __name__ == '__main__':
	main()
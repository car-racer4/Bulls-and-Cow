def get_bull_count(correct_number, input_number):
    correct_list = list(str(correct_number))
    input_list = list(str(input_number))
    counter = 0
    for i in range(4):
        if correct_list[i] == input_list[i]:
            counter += 1

    return counter


def number2list(number, list_):
    number_string = str(number)
    for i in range(4):
        list_[int(number_string[i])] += 1


def get_cow_count(correct_number, input_number):
    correct_number_count = [0] * 10
    input_number_count = [0] * 10
    number2list(correct_number, correct_number_count)
    number2list(input_number, input_number_count)
    counter = 0
    for i in range(10):
        temp = min(correct_number_count[i], input_number_count[i])
        if temp != 0:
            counter += temp

    return counter - get_bull_count(correct_number, input_number)


def four_numbers_input():
	values = []
	for i in range(4):
		value = input(f"Enter number {i+1}: ")
		values.append(int(value))
	return values

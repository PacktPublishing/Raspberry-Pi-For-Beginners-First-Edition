def get_max_value_from_number_list(number_list):
    max_value = number_list[0]
    for number in number_list:
        if number > max_value:
            max_value = number
    return max_value

number_list = [1, 5, -6, 12, 7]
max_value = get_max_value_from_number_list(number_list)
print(max_value)
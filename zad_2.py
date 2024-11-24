def multiply_five_numbers_times_two(numbers: list[int]):
    if len(numbers) != 5:
        print("You need to pass 5 numbers")
        return []
    res = []
    for number in numbers:
        var = number * 2
        res.append(var)
    return res


def multiply_five_numbers_times_two_list_comp(numbers: list[int]):
    if len(numbers) != 5:
        print("You need to pass 5 numbers")
        return []
    return [number * 2 for number in numbers]


numbers = [1, 2, 3, 4, 5]
multiplied = multiply_five_numbers_times_two(numbers)
print(multiplied)

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
multiplied = multiply_five_numbers_times_two(numbers)
print(multiplied)

numbers = [1, 2, 3, 4, 5]
multiplied = multiply_five_numbers_times_two_list_comp(numbers)
print(multiplied)

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
multiplied = multiply_five_numbers_times_two_list_comp(numbers)
print(multiplied)

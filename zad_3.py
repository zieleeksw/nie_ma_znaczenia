def print_even(numbers: list[int]):
    if len(numbers) != 10:
        print("You need to pass exactly 10 numbers")
        return []
    for number in numbers:
        if number % 2 == 0:
            print(number)


numbers = list(range(1,11))
print_even(numbers)
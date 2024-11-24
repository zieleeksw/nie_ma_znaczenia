def print_every_second_element(numbers: list[int]):
    if len(numbers) != 10:
        print("You need to pass exactly 10 numbers")
        return []
    for i in range(0, len(numbers), 2):
        print(numbers[i])


numbers = list(range(1, 11))
print_every_second_element(numbers)

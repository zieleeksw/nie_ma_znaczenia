'''
4. Stworzyć funkcję, która przyjmie 3 argumenty typu int i sprawdzi czy suma
dwóch pierwszych liczb jest większa lub równa trzeciej, a następnie zwróci tę
informację jako typ logiczny bool
'''


def is_sum_of_first_and_second_higher_than_third(first: int, second: int, third: int) -> bool:
    return (first + second) > third

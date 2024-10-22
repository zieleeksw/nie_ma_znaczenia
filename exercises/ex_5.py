'''
5. Stworzyć funkcję, która przyjmie 2 argumenty. Pierwszy typu list , a drugi
typu int . Funkcja ma sprawdzić (zwracając typ logiczny bool ), czy lista z
parametru pierwszego zawiera taką wartość jaką przekazano w parametrze
drugim.
'''


def contains_value(my_list: list, value: int) -> bool:
    return value in my_list

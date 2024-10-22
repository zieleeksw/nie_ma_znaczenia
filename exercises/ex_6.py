'''
6. Stworzyć funkcję, która przyjmuje 2 argumenty typu list i zwraca wynik typu
list . Funkcja ma za zadanie złączyć przekazane listy w jedną, usunąć
duplikaty, każdy element podnieść do potęgi 3 stopnia, a następnie zwrócić
powstałą listę.
'''


def merge_and_cube_lists(list1: list, list2: list) -> list:
    merged_list = set(list1) | set(list2)
    cubed_list = [x ** 3 for x in merged_list]
    return cubed_list

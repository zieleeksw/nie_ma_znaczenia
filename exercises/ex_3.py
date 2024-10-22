'''
3. Stworzyć funkcję, która będzie sprawdzała czy przekazana liczba w
parametrze jest parzysta i zwróci tą informację jako typ logiczny bool
( True / False ). Należy uruchomić funkcję, wynik wykonania zapisać do
zmiennej, a następnie wykorzystując warunek logiczny wyświetlić prawidłowy
tekst "Liczba parzysta" / "Liczba nieparzysta"
'''


def is_even(num: int) -> bool:
    return num % 2 == 0


def print_even_or_odd(number: int):
    is_even_num = is_even(number)
    if is_even_num:
        print("Liczba parzysta")
    else:
        print("Liczba nieparzysta")


print_even_or_odd(2)
print_even_or_odd(3)

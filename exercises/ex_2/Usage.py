from datetime import date

from exercises.ex_1.Student import Student
from exercises.ex_2.Book import Book
from exercises.ex_2.Employee import Employee
from exercises.ex_2.Library import Library
from exercises.ex_2.Order import Order

library1 = Library("Warsaw", "Nowy Świat 123", "00-001", "9:00-17:00", "+48 22 123 45 67")
library2 = Library("Cracow", "Rynek 10", "31-101", "10:00-18:00", "+48 12 345 67 89")

employee1 = Employee("Jan", "Kowalski", date(2020, 1, 15), date(1990, 5, 20), "Warsaw", "Nowy Świat 123", "00-001",
                     "+48 22 123 45 67")
employee2 = Employee("Anna", "Nowak", date(2021, 3, 12), date(1992, 4, 12), "Warsaw", "Nowy Świat 124", "00-001",
                     "+48 22 124 45 67")

book1 = Book(library1, date(2020, 6, 21), "Adam", "Mickiewicz", 423)
book2 = Book(library1, date(2021, 5, 3), "Henryk", "Sienkiewicz", 312)
book3 = Book(library2, date(2022, 7, 11), "Bolesław", "Prus", 202)
book4 = Book(library1, date(2021, 3, 8), "Stefan", "Żeromski", 253)
book5 = Book(library1, date(2021, 5, 3), "Henryk", "Sienkiewicz", 312)

student1 = Student("Mateusz", [5, 4, 4, 5])
student2 = Student("Magdalena", [3, 4, 4, 4])
student3 = Student("Paweł", [5, 5, 5, 5])

order1 = Order(employee1, student1, [book1, book2], date(2022, 7, 11))
order2 = Order(employee2, student2, [book2, book3], date(2023, 1, 18))

print(order1)
print(order2)
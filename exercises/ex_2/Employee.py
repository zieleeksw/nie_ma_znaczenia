class Employee:
    def __init__(self,
                 first_name,
                 last_name,
                 hire_date,
                 birth_date,
                 city,
                 street,
                 zip_code,
                 phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return (f"Employee: {self.first_name} "
                f"{self.last_name}, "
                f"Hire Date: {self.hire_date}, "
                f"Birth Date: {self.birth_date}, "
                f"Address: {self.street}, "
                f"{self.city} "
                f"({self.zip_code}), "
                f"Phone: {self.phone}")

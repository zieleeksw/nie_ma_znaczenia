class Brewery:
    def __init__(self, id: str,
                 name: str,
                 brewery_type: str,
                 street: str,
                 city: str,
                 state: str,
                 postal_code: str,
                 country: str,
                 phone: str):
        self.id = id
        self.name = name
        self.brewery_type = brewery_type
        self.street = street
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.country = country
        self.phone = phone

    def __str__(self):
        return (f"Brewery ID: {self.id}\n"
                f"Name: {self.name}\n"
                f"Type: {self.brewery_type}\n"
                f"Street: {self.street}\n"
                f"City: {self.city}\n"
                f"State: {self.state}\n"
                f"Postal Code: {self.postal_code}\n"
                f"Country: {self.country}\n"
                f"Phone: {self.phone}\n")

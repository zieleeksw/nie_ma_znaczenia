class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return (f"Property [area={self.area}, "
                f"rooms={self.rooms}, "
                f"price={self.price}, "
                f"address={self.address}]")

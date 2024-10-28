from exercises.ex_3.Property import Property


class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f"Flat [area={self.area}, rooms={self.rooms}, price={self.price}, address={self.address}, floor={self.floor}]"

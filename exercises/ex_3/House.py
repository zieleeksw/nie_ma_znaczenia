from exercises.ex_3.Property import Property


class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return (f"House [area={self.area}, "
                f"rooms={self.rooms}, "
                f"price={self.price}, "
                f"address={self.address}, "
                f"plot={self.plot}]")

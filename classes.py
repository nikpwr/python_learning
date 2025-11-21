class Car:
    def __init__(self, brand, year, colour, max_speed):
        self.brand = brand
        self.year = year
        self.colour = colour
        self.max_speed = max_speed
        self.info = f"{brand}\nColor:{colour}\nMax Speed:{max_speed}\nYear: {year}"
    
    def print_info(self):
        print(self.info)

    def set_colour_to_green(self):
        self.colour = 'Green'

    def get_car_info(self):
        return self.info
    
    def get_colour(self):
        return self.colour

    def print_colour(self):
        print(self.colour)

audi = Car('Audi',2000,'Red',200)
audi.set_colour_to_green()

print(Car.get_car_info(audi))
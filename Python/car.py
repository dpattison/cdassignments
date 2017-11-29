class car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if price >= 10000:
            self.tax = .15
        else:
            self.tax = .12
        self.display_all()

    def display_all(self):
        print "Price: " + str(self.price)
        print "Speed: " + self.speed
        print "Fuel: " + self.fuel
        print "Mileage: " + self.mileage
        print "Tax: " + str(self.tax)
        print
        return self

car1 = car(1000, "60mph", "full", "15mph")
car2 = car(2000, "60mph", "full", "15mph")
car3 = car(30000, "60mph", "full", "15mph")
car4 = car(40000, "60mph", "full", "15mph")
car5 = car(50000, "60mph", "full", "15mph")
car6 = car(600, "60mph", "full", "15mph")

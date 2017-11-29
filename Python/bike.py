class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayinfo(self):
        print "The price is " + str(self.price)
        print "The max speed is " + self.max_speed
        print "Total miles equals " + str(self.miles)
        return self

    def ride(self):
        print "Riding..."
        self.miles += 10
        return self

    def reverse(self):
        if self.miles >= 5:
            print "Reversing..."
            self.miles -= 5
        elif 0 < self.miles < 5:
            print "Reversing to zero"
            self.miles = 0
        elif self.miles == 0:
            print "Can't reverse any more"
        return self


bike1 = Bike(200, "25mph")
bike2 = Bike(100, "10mph")
bike3 = Bike(10, "1mph")

bike1.displayinfo()
bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.displayinfo()

bike2.displayinfo()
bike2.ride().ride().reverse().reverse()
bike2.displayinfo()

bike3.displayinfo()
bike3.reverse().reverse().reverse()
bike3.displayinfo()

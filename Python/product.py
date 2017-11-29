class product(object):
    def __init__(self, price, item_name, weight, brand):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"


    def sell(self):
        self.status = "sold"
        return self

    def addtax(self, tax):
        return self.price * (1 + tax)

    def returnitem(self, reason):
        if reason == "defective":
            self.status = "defective"
            self.price = 0
        elif reason == "unopened":
            self.status = "for sale"
        elif reason == "opened":
            self.status = "used"
            self.price = self.price * .8
        return self

    def displayinfo(self):
        print "Price: " + str(self.price)
        print "Item Name: " + self.item_name
        print "Weigth: " + str(self.weight)
        print "Brand: " + self.brand
        print "Status: " + self.status
        print
        return self

product1 = product(12, "shirt", 80, "Nike")
product1.returnitem("opened").displayinfo()

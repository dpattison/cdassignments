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
product2 = product(1223, "pants", 12, "Adidas")
# product1.returnitem("opened").displayinfo()


class store(object):
    def __init__(self, location, owner):
        self.products = []
        self.location = location
        self.owner = owner
        

    def addproduct(self, product):
        self.products.append(product)
        return self
        

    def removeproduct(self, product):
        self.products.remove(product)
        return self
        

    def inventory(self):
        for product in self.products:
            product.displayinfo()
        return self
            

store1 = store("newport", "dave")

store1.addproduct(product1)
store1.addproduct(product2)
store1.removeproduct(product1).inventory()



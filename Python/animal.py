class animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def walk(self):
        self.health -= 1
        return self
    
    def run(self):
        self.health -= 5
        return self
     
    def display_health(self):
        print self.health
        return self

animal1 = animal("Tiger", 20)
animal1.display_health().walk().walk().walk().run().run().display_health()

class dog(animal):
    def __init__(self, name):
        super(dog, self).__init__(name, 150)
    
    def pet(self):
        self.health += 5
        return self

dog1 = dog("Fido")
dog1.display_health().walk().walk().walk().run().run().pet().display_health()


class dragon(animal):
    def __init__(self, name):
        super(dragon, self).__init__(name, 170)
        self.health = 170
    def fly(self):
        self.health -= 10
        return self
    def display_health(self):
        super(dragon, self).display_health()
        print "I am a Dragon"
        return self

dragon1 = dragon("Slick")
dragon1.fly().display_health()

animal2 = animal("willy", 50)
# animal2.fly()
# animal2.pet()
animal2.display_health()
# dog1.fly()
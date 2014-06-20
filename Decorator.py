class Beverage:
    # description of the beverage
    description = "Unknown Beverage"
    # interfaces
    def getDescription(self):
        return self.description
    def cost(self):
        return 1.0
    
# Concrete beverage classes    
class HouseBlend(Beverage):
    def __init__(self):
        self.description = "House Blend"
    def cost(self):
        return 0.2 + Beverage.cost(self)

class DarkRoast(Beverage):
    def __init__(self):
        self.description = "Dark Roast"
    def cost(self):
        return 0.3 + Beverage.cost(self)
    
class Espresso(Beverage):
    def __init__(self):
        self.description = "Espresso"
    def cost(self):
        return 0.1 + Beverage.cost(self)

class Decaf(Beverage):
    def __init__(self):
        self.description = "Decaf"
    def cost(self):
        return 0.4 + Beverage.cost(self) 

# Abstract Condiment Decorator
class CondimentDecorator(Beverage):
    def getDescription(self):
        return self.description

# Concrete Condiment Decorator classes
class Milk(CondimentDecorator):
    beverage = None
    def __init__(self, beverage):
        self.beverage = beverage
    def getDescription(self):
        return self.beverage.getDescription() + ", Milk"
    def cost(self):
        return self.beverage.cost() + 0.6
    
class Mocha(CondimentDecorator):
    beverage = None
    def __init__(self, beverage):
        self.beverage = beverage
    def getDescription(self):
        return self.beverage.getDescription() + ", Mocha"
    def cost(self):
        return self.beverage.cost() + 0.7

class Soy(CondimentDecorator):
    beverage = None
    def __init__(self, beverage):
        self.beverage = beverage
    def getDescription(self):
        return self.beverage.getDescription() + ", Soy"
    def cost(self):
        return self.beverage.cost() + 0.8
    
class Whip(CondimentDecorator):
    beverage = None
    def __init__(self, beverage):
        self.beverage = beverage
    def getDescription(self):
        return self.beverage.getDescription() + ", Whip"
    def cost(self):
        return self.beverage.cost() + 0.9
    
if __name__=="__main__":
    beverage1 = Espresso()
    print beverage1.getDescription() + " : $" + str(beverage1.cost())
    
    beverage2 = DarkRoast()
    beverage2 = Mocha(beverage2)
    beverage2 = Mocha(beverage2)
    beverage2 = Whip(beverage2)
    print beverage2.getDescription() + " : $" + str(beverage2.cost())
    
    beverage3 = HouseBlend()
    beverage3 = Soy(beverage3)
    beverage3 = Mocha(beverage3)
    beverage3 = Whip(beverage3)
    print beverage3.getDescription() + " : $" + str(beverage3.cost())
    
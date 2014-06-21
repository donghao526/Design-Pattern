class Duck:
    flyBehavior = None
    quackBehavior = None
    def display(self):
        print ""
    def performFly(self):
        self.flyBehavior.fly()
    def performQuack(self):
        self.quackBehavior.quack()
    def setFlyBehavior(self, flyBehavior):
        self.flyBehavior = flyBehavior
    def setQuackBehavior(self, quackBehavior):
        self.quackBehavior = quackBehavior
        
# Model Duck
class ModelDuck(Duck):
    def __init__(self):
        self.flyBehavior = FlyNoWay()
        self.quackBehavior = WaWaQuack()
    def display(self):
        print "I am a model duck"

# Abstract Fly and Qucak Behavior
class FlyBehavior:
    def fly(self):
        print ""      
class QuackBehavior:
    def quack(self):
        print ""
# Concrete Fly behavior        
class FlyWithSwing(FlyBehavior):
    def fly(self):
        print "I fly with swings"        
class FlyNoWay(FlyBehavior):
    def fly(self):
        print "I can't fly"
        
# Concrete quack behavior        
class ZhiZhiQuack(QuackBehavior):
    def quack(self):
        print "Zhi Zhi Quack"       
class WaWaQuack(QuackBehavior):
    def quack(self):
        print "Wa Wa Quack"
     
#Test code   
if __name__=="__main__":
    duck = ModelDuck()
    duck.performFly()
    duck.setFlyBehavior(FlyWithSwing())
    duck.performFly()
    
    duck.performQuack()
    duck.setQuackBehavior(ZhiZhiQuack())
    duck.performQuack()
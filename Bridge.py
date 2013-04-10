# The Abstraction Interface
class Abstraction:
    def __init__(self,imp):
        self.imp = imp
    def Operation(self):
        self.imp.OperationImp();

# The Implementor Interface
class Implementor:
    def OperationImp(self):
        print "The interface for the concrete implementors."

# The Concrete Implementation of A        
class ConcreteImplementorA(Implementor):
    def OperationImp(self):
        print "The concrete implementation of A"
        
# The Concrete Implementation of B  
class ConcreteImplementorB(Implementor):
    def OperationImp(self):
        print "The concrete implementation of B"
 
# Extending the interface of Abstraction        
class RefinedAbstraction(Abstraction):
    def __init__(self,imp):
        Abstraction.__init__(self,imp)
        
class Client:
    def show(self):      
        
        # Define two concrete implementor  
        implementorA = ConcreteImplementorA()
        implementorB = ConcreteImplementorB()
        
        # Use the Concrete implementation of A 
        ReAbstarction = RefinedAbstraction(implementorA)
        ReAbstarction.Operation()
        
        # Use the Concrete implementation of B 
        ReAbstarction = RefinedAbstraction(implementorB)
        ReAbstarction.Operation()
    
if __name__=="__main__":
        client = Client()
        client.show()   
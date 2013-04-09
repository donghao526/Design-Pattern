# Target is the interface client wanted 
class Target:
    def Request(self):
        print "This is a common request"

# Adaptee is the class to implements specific function
class Adaptee:
    def SpecificRequesst(self):
        print "This is a specific request"
        
# Adapter is the class client wanted and implements specific function
class Adapter(Target):
    def __init__(self):
        self.adaptee = Adaptee()
    def Request(self):
        self.adaptee.SpecificRequesst()

# client use the interface of target to requests
class Client:
    def show(self):
        adapter = Adapter()
        adapter.Request()

if __name__=="__main__":
    
    client = Client()
    client.show()
    
        
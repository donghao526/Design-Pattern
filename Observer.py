#interface of Subject
class Subject:
    def __init__(self):
        self._observer=[]
    #Add observers
    def Attach(self,observer):
        self._observer.append(observer)
    #remove observers
    def Detach(self,observer):
        self._observer.remove(observer)
    def Notify(self):
        for element in self._observer:
            element.Update(self)
                   
#Concrete Subject        
class ConcreteSubject(Subject):
    def GetState(self):
        return self.subjectState
    def SetSate(self,state): 
        self.subjectState=state
        self.Notify()
#interface of Observers
class Observer:
    def Update(self,subject):
        print "Update in Observer"
   
#Concrete Observers           
class ConcreteObserver1(Observer):
    def Update(self,subject):
        print "Update in Observer1:The state of the Subject has changed to: ",subject.GetState()
        
class ConcreteObserver2(Observer):
    def Update(self,subject):
        print "Update in Observer2:The state of the Subject has changed to: ",subject.GetState()

class ConcreteObserver3(Observer):
    def Update(self,subject):
        print "Update in Observer3:The state of the Subject has changed to: ",subject.GetState()

#Client change the state twice     
class Client:
    def show(self):
        conSubject = ConcreteSubject()
        observer1 = ConcreteObserver1()
        observer2 = ConcreteObserver2()
        observer3 = ConcreteObserver3()
        conSubject.Attach(observer1) 
        conSubject.Attach(observer2) 
        conSubject.Attach(observer3) 
        conSubject.SetSate("sunny")
        conSubject.SetSate("rainy")

if __name__=="__main__":
    client = Client()
    client.show()       
    
# Window class and Concrete Window Subclass       
class Window:
    def __init__(self):
        print "Window"      
class PMWindow(Window):
    def __init__(self):
        print "PMWindow"
class MotlfWindow(Window):
    def __init__(self):
        print "MotlfWindow"

# ScrollBar class and Concrete ScrollBar Subclass     
class ScrollBar:
    def __init__(self):
        print "ScrollBar"
class PMScrollBar(ScrollBar):
    def __init__(self):
        print "PMScrollBar"
class MotlfScrollBar(ScrollBar):
    def __init__(self):
        print "MotlfScrollBar"

# WidgetFactory class and Concrete WidgetFactory Subclass      
class WidgetFactory:
    def CreateWindow(self):
        return Window()
    def CreateScrollBar(self):
        return ScrollBar()
class PMWidgetFactory:
    def CreateWindow(self):
        return PMWindow()
    def CreateScrollBar(self):
        return PMScrollBar();
class MotlfWidgetFactory:
    def CreateWindow(self):
        return MotlfWindow()
    def CreateScrollBar(self):
        return MotlfScrollBar()
# Client
class Client:
    def show(self):
        fac1 =  PMWidgetFactory()
        fac2 =  MotlfWidgetFactory()
        fac1.CreateScrollBar()
        fac1.CreateWindow()
        fac2.CreateScrollBar()
        fac2.CreateWindow()
    
if __name__=="__main__":
        client = Client()
        client.show()  
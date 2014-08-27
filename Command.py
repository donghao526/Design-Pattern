#define the remote control class and which is the client
class RemoteControl:
    def __init__(self):
        self.onCommands = []
        self.offCommands = []
        c = Command();
        self.onCommands.append(c)
        self.onCommands.append(c)
        self.offCommands.append(c)
        self.offCommands.append(c)
        self.lastCommands = c
    def setCommands(self, slot, onCommand, offCommand):
        self.onCommands[slot]  = onCommand
        self.offCommands[slot] = offCommand
    def onButtonPressed(self, slot):
        self.onCommands[slot].execute()
        self.lastCommands = self.onCommands[slot]
    def offButtonPressed(self, slot):
        self.offCommands[slot].execute()
        self.lastCommands = self.offCommands[slot]
    def undo(self):
        self.lastCommands.undo()
        
# define the Command interface       
class Command:
    def execute(self):
        print "Nothint to do"
 
# define Light, Stereo and four concrete Commands       
class Light:
    def on(self):
        print "Light is On"
    def off(self):
        print "Light is Off"
        
class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light
    def execute(self):
        self.light.on();
    def undo(self):
        self.light.off();
        
class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light
    def execute(self):
        self.light.off();
    def undo(self):
        self.light.on();
        
class Stereo:
    def on(self):
        print "Stereo is On"
    def off(self):
        print "Stereo is Off"
        
class StereoOnCommand(Command):
    def __init__(self, stereo):
        self.stereo = stereo
    def execute(self):
        self.stereo.on();
    def undo(self):
        self.stereo.off();
        
class StereoOffCommand(Command):
    def __init__(self, stereo):
        self.stereo = stereo
    def execute(self):
        self.stereo.off();
    def undo(self):
        self.stereo.on();
        
#Test code   
if __name__=="__main__":
    rc = RemoteControl()
    light = Light()
    LightOn  = LightOnCommand(light)
    LightOff = LightOffCommand(light)
    rc.setCommands(0, LightOn, LightOff)
    rc.onButtonPressed(0)
    rc.offButtonPressed(0)
    rc.undo();
    
    stereo = Stereo()
    StereoOn  = StereoOnCommand(stereo)
    StereoOff = StereoOffCommand(stereo)
    rc.setCommands(1, StereoOn, StereoOff)
    rc.onButtonPressed(1)
    rc.offButtonPressed(1)
    rc.undo();
    
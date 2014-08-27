#define the components
class Screen:
    def on(self):
        print "Screen is on"
    def off(self):
        print "Screen is off"
    def up(self):
        print "Screen is up"
    def down(self):
        print "Screen is down"
        
class DvdPlayer:
    def on(self):
        print "DVD is on"
    def play(self):
        print "DVD is playing"
    def stop(self):
        print "DVD is stop"
    def off(self):
        print "DVD is off"    
                
class Amplifier:
    def on(self):
        print "Amplifier is on"
    def setDvd(self, dvd):
        print "Amplifier is setting dvd"
    def setVolume(self, value):
        print "Amplifier is setting the volume to %d" , value
    def off(self):
        print "Amplifier is off"
        
# define the Facade    
class Facade:
    def __init__(self, dvd, screen, amplifier):
        self.dvd = dvd
        self.screen = screen
        self.amplifier = amplifier
    def watchMovie(self):
        print "Get Ready, Watch Movie..."
        self.screen.on()
        self.screen.up()
        self.amplifier.on()
        self.amplifier.setDvd(self.dvd)
        self.amplifier.setVolume(5)
        self.dvd.on()
        self.dvd.play()
    def endMovie(self):
        print "Shutting movie theater down..."
        self.dvd.stop()
        self.dvd.off()
        self.amplifier.off()
        self.screen.down()
        self.screen.off()
        
# Test code   
if __name__=="__main__":
    
    screen = Screen()
    dvd = DvdPlayer()
    amplifier = Amplifier()
    
    facade = Facade(dvd, screen, amplifier)
    facade.watchMovie()
    facade.endMovie()
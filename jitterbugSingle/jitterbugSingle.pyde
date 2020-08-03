class State:
    def __init__(self):
        self.flag = False
        
    def clicked(self):
        self.flag = True
        
    def released(self):
        self.flag = False
        
class JitterBug:
    speed = 3
    def __init__(self, startX=0, startY=0, startDiameter=20):
        self.x = startX
        self.y = startY
        self.diameter = startDiameter
        
    def start(self, x, y):
        self.x = x
        self.y = y
        
    def move(self):
        self.x += random(-JitterBug.speed, JitterBug.speed)
        self.y += random(-JitterBug.speed, JitterBug.speed)
        
    def display(self):
        ellipse(self.x, self.y, self.diameter, self.diameter)
        
    def __repr__(self):
        return str("bug(" + str(self.x) + ", " + ")")
    
    @classmethod
    def speedUp(cls):
        JitterBug.speed += 1
        
    @classmethod
    def speedDown(cls):
        if JitterBug.speed > 0:
            JitterBug.speed -= 1
    
jits = []
mouseDown = State()
flag = False    

        
def setup():
    size(1400, 940)
    background(220)
    
def draw():
    if (keyPressed == True):
        if (key == 'a'):
            ##speed += 1
            JitterBug.speedUp()
        if (key == 's'):
            ##speed -= 1
            JitterBug.speedDown()
    
    if (mousePressed and not mouseDown.flag):
        jits.append(JitterBug(mouseX, mouseY, 50))
        mouseDown.clicked()

    if (not mousePressed and mouseDown.flag):
        mouseDown.released()

    for jit in jits:
        jit.move()
        jit.display()
    

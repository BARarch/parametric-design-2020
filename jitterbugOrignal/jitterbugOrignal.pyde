speed = 3

class JitterBug():
    def __init__(self, startX, startY, startDiameter):
        self.x = startX
        self.y = startY
        self.diameter = startDiameter
        
    def move(self):
        self.x += random(-speed, speed)
        self.y += random(-speed, speed)
    
    def display(self):
        ellipse(self.x, self.y, self.diameter, self.diameter)
        
jit = JitterBug(400, 200, 40)
jit2 = JitterBug(800, 400, 20)

def setup():
    size(1400, 940)
    background(220)
    
def draw():
    jit.move()
    jit.display()
    jit2.move()
    jit2.display()
    

def reTransform(x, y, phi):
    return x * cos(phi) + y * sin(phi), -x * sin(phi) + y * cos(phi)

i = 0
y = 400
x = 40
angle = 0
speed = 10
rotSpeed = 4

class State:
    def __init__(self):
        self.flag = False
        
    def clicked(self):
        self.flag = True
        
    def released(self):
        self.flag = False

class Row:
    def __init__(self, startX, startY):
        self.x = startX
        self.y = startY
        self.angle = .1
        self.speed = 20
        self.rotSpeed = .05
        self.frame = 0
        
    def move(self):
        self.x += self.speed
        self.angle +=self.rotSpeed
        
    def display(self):
        if self.x < 700:
            xp, yp = reTransform(self.x, self.y, self.angle)
            rotate(self.angle)
            rect(xp - 20, yp - 20, 40, 40)
            self.frame += 1
        
squares = Row(30, 400)
mouseDown = State()
rows = []  

def setup():
    size(800, 800)
    background(220)
    stroke(50)
    noFill()
    strokeWeight(3)
    
def draw():
    if (mousePressed and not mouseDown.flag):
        rows.append(Row(mouseX, mouseY))
        mouseDown.clicked()

    if (not mousePressed and mouseDown.flag):
        mouseDown.released()
    
    for row in rows:
        row.move()
        row.display()

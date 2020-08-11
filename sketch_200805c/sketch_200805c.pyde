add_library('pdf')
class ColorTriangle:
    def __init__(self, dia):
        self.centerX = 200
        self.centerY = 200
        self.d = dia
        self.i = 0
        self.col = "RED"
        self.colorLimit = 5
        
        self.theta0, self.theta1, self.theta2 = 0, 0, 0
        self.d0, self.d1, self.d2 = self.d, self.d, self.d
        
    def set_center(self, centerX, centerY):
        self.centerX = centerX
        self.centerY = centerY

    def set_diamter(self, d):
        self.d = d
        
    def display(self):
        def transform(r, theta):
            return self.centerX + r * cos(theta), self.centerY + r * sin(theta)
        
        x0, y0 = transform(self.d0, self.theta0)
        x1, y1 = transform(self.d1, self.theta1)
        x2, y2 = transform(self.d2, self.theta2)
        
        triangle(x0, y0, x1, y1, x2, y2)
        self.i += 1
        
    def moveP0(self, r, theta):
        self.theta0 = PI / 2 + theta
        self.d0 = self.d * r
        
    def moveP1(self, r, theta):
        self.theta1 = 7 * PI / 6 + theta
        self.d1 = self.d * r
        
    def moveP2(self, r, theta):
        self.theta2 = -PI / 6 + theta
        self.d2 = self.d * r

t1 = ColorTriangle(280)
        
def setup():
    size(980, 980)
    x = map(.5, 0, 1, 0, width)
    y = map(.5, 0, 1, 0, height)
    strokeWeight(8)
    strokeJoin(ROUND)
    t1.set_center(x, y)
    beginRecord(PDF, "triangle_output_demo.pdf")
    
def draw():
    grey = random(0, 255)
    col = random(grey, 255)

    print("grey: " + str(grey) +"\tcolor: " + str(col))
    background(220)
    if t1.col == "RED":
        fill(col, grey, grey)
        t1.moveP0(col / 255, ((grey - 128) / 128) * PI / 8)
        t1.display()
        if t1.i == t1.colorLimit:
            t1.col = "GREEN"
            t1.i = 0
    
    elif t1.col == "GREEN":
        fill(grey, col, grey)
        t1.moveP1(col / 255, ((grey - 128) / 128) * PI / 8)
        t1.display()
        if t1.i == t1.colorLimit:
            t1.col = "BLUE"
            t1.i = 0
        
    elif t1.col == "BLUE":
        fill(grey, grey, col)
        t1.moveP2(col / 255, ((grey - 128) / 128) * PI / 8)
        t1.display()
        if t1.i == t1.colorLimit:
            t1.col = 1
            t1.i = 0

    else:
        noLoop()
        endRecord()

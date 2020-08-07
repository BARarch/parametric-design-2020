add_library('pdf')
def reTransform(x, y, phi):
    return x * cos(phi) + y * sin(phi), -x * sin(phi) + y * cos(phi)

def positions(nX, nY):
    for i in range(nY):
        for j in range(nX):
            yield (j, i)        
                                    
def display(x, y):
    angle = .002 * (x - y)
    angle2 = .600 * (x - y)
    xp, yp = reTransform(x, y, angle)
    strokeWeight(abs(3 * cos(angle2)))
    rotate(angle)
    rect(500, 300, 600, 250)
    rect(0, 0, 0, 0)
    rect(300, 300, 300, 150)

    
nX = 15
nY = 100       

loc = positions(nX, nY)

def setup():
    size(1000, 1000)

    background(255, 40, 150)
    stroke(40)
    noFill()
    strokeWeight(3)
    beginRecord(PDF, "Friday_August_7.pdf")
    
def draw():
    try:
        i, j = next(loc)
        x = map(i, 0, nX, 0, width)
        y = map(j, 0, nY, 0, height)
        display(x, y)
        print("x=" + str(x) + " y=" + str(y))
    except Exception as e:
        print(e)
        endRecord()
        print("Done")
        noLoop()
        

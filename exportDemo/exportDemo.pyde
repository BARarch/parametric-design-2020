add_library('pdf')


def roTransform(x, y, phi):
    return x * cos(phi) + y * sin(phi), -x * sin(phi) + y * cos(phi)

def display(x, y, coef):
    angle = (coef + .005) * (x + y)
    angle2 = (coef + .008) * (x + y)
    xp, yp = roTransform(x, y, angle)
    strokeWeight(abs(3* cos(angle2)))
    rotate(angle)
    rect(xp - 30, yp - 30, 60, 60)
    
def positions(nX, nY):
    for i in range(nY):
        for j in range(nX):
            yield (j, i)

def setup():
    size(980, 980)
    background(220)
    noFill()
    strokeWeight(3)
    beginRecord(PDF, squareDemo.pdf)
    
nX = 40
nY = 40
loc = positions(nX, nY)
    
def draw():
    try:
        i, j = next(loc)
        x = map(i, 0, nX, 0, width)
        y = map(j, 0, nY, 0, height)
        display(x, y, .001)
    except Exception as e:
        endRecord()
        print(e)
        print("DONE")
        noLoop()
        
    
    

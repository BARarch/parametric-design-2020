def reTransform(x, y, phi):
    return x * cos(phi) + y * sin(phi), -x * sin(phi) + y * cos(phi)

def positions(nX, nY):
    for i in range(nY):
        for j in range(nX):
            yield (j, i)        
                                    
def display(x, y, coef):
    angle = (coef + .005) * (x + y)
    angle2 = (coef + .008) * (x + y)
    xp, yp = reTransform(x, y, angle)
    strokeWeight(abs(3 * cos(angle2)))
    rotate(angle)
    rect(xp - 30, yp - 30, 60, 60)

nX = 40
nY = 40        

loc = positions(nX, nY)
colorRun = 1
c = .001

def setup():
    size(1000, 1000)

    background(220)
    stroke(50)
    noFill()
    strokeWeight(3)
    
def draw():
    try:
        i, j = next(loc)
        x = map(i, 0, nX, 0, width)
        y = map(j, 0, nY, 0, height)
        display(x, y, c)
        print("x=" + str(x) + " y=" + str(y))
    except Exception as e:
        if colorRun:
            loc = positions(nX, nY)
            colorRun = 0
            c = .003
            stroke(255, 0, 0)
        else:
            print("Done")
            noLoop()

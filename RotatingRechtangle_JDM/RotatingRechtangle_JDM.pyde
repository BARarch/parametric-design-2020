def reTransform(x, y, phi):
    return x * cos(phi) + y * sin(phi), -x * sin(phi) + y * cos(phi)

def positions(nX, nY):
    for i in range(nY):
        for j in range(nX):
            yield (j, i)        
                                    
def display(x, y):
    angle = .002 * (x + y)
    angle2 = .005 * (x + y)
    xp, yp = reTransform(x, y, angle)
    strokeWeight(abs(3 * sin(angle2)))
    rotate(angle)
    rect(xp -  60, yp - 60, 110, 90)
    
nX = 5
nY = 35  

loc = positions(nX, nY)

def setup():
    size(1000, 1000)

    background(220)
    stroke(50)
    fill(151, 214, 185)
    strokeWeight(1)
    
def draw():
    try:
        i, j = next(loc)
        x = map(i, 0, nX, 0, width)
        y = map(j, 0, nY, 0, height)
        display(x, y)
        print("x=" + str(x) + " y=" + str(y))
    except Exception as e:
        print(e)
        print("Done")
        noLoop()
    

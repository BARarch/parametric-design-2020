add_library('pdf')
def reTransform(x, y, phi):
    return x * cos(phi) + y * sin(phi), -x * sin(phi) + y * cos(phi)

def positions(nX, nY):
    for i in range(nY):
        for j in range(nX):
            yield (j, i)        
                                    
def display(x, y):
    angle = .020 * (x - y)
    angle2 = .022 * (x + y)
    xp, yp = reTransform(x, y, angle)
    strokeWeight(abs(4 * sin(angle2)))
    rect(xp - 30, yp + 30, -60, 60)
    rect(xp - 40, yp + 40, -60, 60)
    rect(xp - 50, yp + 50, -60, 60)
    
nX = 5
nY = 50   

loc = positions(nX, nY)

def setup():
    size(1000, 1000)

    background(220)
    stroke(50)
    noFill()
    strokeWeight(3)
    beginRecord(PDF, "Square_4.pdf")
    
def draw():
    try:
        i, j = next(loc)
        x = map(i, 0, nX, 0, width)
        y = map(j, 0, nY, 0, height)
        display(x, y)
        print("y=" + str(x) + " y=" + str(y))
    except Exception as e:
        print(e)
        endRecord()
        print("Done")
        noLoop()
   

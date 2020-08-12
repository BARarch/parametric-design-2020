add_library('pdf')
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
    strokeWeight(abs(1 * sin(angle2)))
    rotate(angle)
    rect(xp - 30, yp - 30, 200, 60)

nX = 500
nY = 4       

loc = positions(nX, nY)

def setup():
    beginRecord(PDF, "IN ROTATION.PDF")
    size(3000, 1375)
    background(228, 210, 231)
    stroke(116, 1, 113)
    noFill()
    strokeWeight(.002)
    
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
    

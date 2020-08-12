add_library('pdf')
def reTransform(x, y, phi):
    return x * cos(phi) + y * sin(phi), -x * sin(phi) + y * cos(phi)

def positions(nX, nY):
    for i in range(nY):
        for j in range(nX):
            yield (j, i)        
                                    
def display(x, y):
    angle = .01 * (x + y)
    angle2 = .02 * (x + y)
    xp, yp = reTransform(x, y, angle)
    strokeWeight(abs(2 * sin(angle2)))
    rotate(angle)
    rect(400, 400, xp - 100, yp - 100)
    
    
   

nX = 300
nY = 1  

loc = positions(nX, nY)

def setup():
    size(1000, 1000)
    
    stroke(random(250), random(150), random(140))
    background(0, 0, 0)
    noFill()

    beginRecord(PDF, "screensaver.pdf")
    
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

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
    triangle(500, 300, 600, 250, 700, 250); 
    fill(255, 0, 0)
    triangle(500, 300, 600, 350, 700, 250); 
    fill(255, 0, 0)
    
    triangle(300, 300, 400, 275, 500, 300); 
    fill (0, 255, 0)
    triangle(300, 300, 400, 350, 500, 300); 
    fill (0, 255, 0)
    
    triangle(100, 250, 200, 250, 300, 300); 
    fill (171, 67, 234)
    triangle(100, 250, 200, 350, 300, 300); 
    
    
    triangle(700, 250, 800, 150, 900, 100);
    fill (0, 0, 255)
    triangle(700, 250, 800, 270, 900, 100);
  
    triangle(900, 100, 1000, 50, 1200, 5);
    fill (171, 67, 234)
    triangle(900, 100, 1000, 170, 1200, 5);
    
    triangle(1190, 185, 1280, 180, 1700, 250);
    fill (0, 255, 0)
    triangle(1190, 185, 1280, 310, 1700, 250);
  
  
nX = 22
nY = 22  

loc = positions(nX, nY)

def setup():
    size(1650, 1650)

    background(108, 87, 229)
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
    

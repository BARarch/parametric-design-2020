  
def reTransform(x, y, phi):
    return x * cos(phi) + y * sin(phi), -x * sin(phi) + y * cos(phi)

def setup():
    size(1400, 980)
    background(220)
    stroke(255)
    noFill()
    strokeWeight(8)
    
def draw():
    background(1)
    angle = PI * mouseX/ width
    rotate(angle)
    xp, yp = reTransform(700, 490, angle)
    
    rect(xp - 30, yp - 30, 60, 60)
    ellipse(xp - 0, yp - 0, 120, 120)
    
    rect(xp - 70, 0, 140, 140)
    rect(xp - 70, xp - 0, 140, 140)
    
    ellipse(xp - 100, yp - 0, yp - 120, 120)
    ellipse(xp - -100, yp - 0, yp - 120, 120)
    
    ellipse(400, yp - 0, 120, 120)
       
    

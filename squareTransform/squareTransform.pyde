def reTransform(x, y, phi):
    return x * cos(phi) + y * sin(phi), -x * sin(phi) + y * cos(phi)

def setup():
    size(1400, 980)
    background(220)
    noFill()
    strokeWeight(8)
    
def draw():
    background(220)
    angle = PI * mouseX/ width
    rotate(angle)
    xp, yp = reTransform(400, 400, angle)
    rect(xp - 30, yp - 30, 60, 60)

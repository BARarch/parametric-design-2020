margin = 50
rectSize = 100
rectCount = 5

def setup():
    size(800, 800)
    
    
def draw():
    background(20)
    cornerRadius = mouseX/10.0
    print(cornerRadius)
    for S in range(rectCount):
        for l in range(rectCount):
            noStroke()
            fill(150)
            rect(l + rectSize + (S + S) * margin, S * rectSize + (l + l) * margin, rectSize, rectSize, cornerRadius)
            

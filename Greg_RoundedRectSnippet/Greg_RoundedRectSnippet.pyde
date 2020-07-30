margin = 50
rectSize = 100
rectCount = 5

def setup():
    size(800, 800)
    
    
def draw():
    background(50)
    cornerRadius = mouseX/10.0
    print(cornerRadius)
    for i in range(rectCount):
        for n in range(rectCount):
            noStroke()
            fill(150)
            rect(n * rectSize + (n + 1) * margin, i * rectSize + (i + 1) * margin, rectSize, rectSize, cornerRadius)

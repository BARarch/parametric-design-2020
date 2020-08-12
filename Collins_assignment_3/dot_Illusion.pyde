margin = 7
rectSize = 49.5
rectCount = 14

def setup():
    size(800, 800)
   
    
def draw():
    background(50, 200, 250)
    cornerRadius = mouseX/10.0
    print(cornerRadius)
    for i in range(rectCount):
        for n in range(rectCount):
            noStroke()
            fill(40, 100, 200)
            rect(n * rectSize + (n + 1) * margin, i * rectSize + (i + 1) * margin, rectSize, rectSize, cornerRadius)

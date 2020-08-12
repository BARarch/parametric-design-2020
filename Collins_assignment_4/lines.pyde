def setup():
    size(800, 800)
    stroke(1)
    noFill()
    
def draw():
    A = [int(random(100)) for i in range(20)]
    # Count inversions
    inv = 0
    for i, num in enumerate(A):
        for otherNum in A[i + 1:]:
            line(0, i, 600, 600)
            line(600, 600, otherNum, 300)
            line(600, 600, i, -200)
            line(600, 600, otherNum, 800)
            line(otherNum, 900, 600, 600)
            line(600, 600, 900, 40)
            line(600, 600, i, -7000)
            line(600, 600, -7000, i)
            line(600, 600, 900, 900)
            line(600, 600, 900, 90)
            line(600, 600, 900, 300)
            line(600, 600, 900, 40)
            line(600, 600, 900, -100)
            line(i, otherNum, 600, 600)
            
            line(0, i, 200, 200)
            line(200, 200, otherNum, 300)
            line(200, 200, i, -200)
            line(200, 200, otherNum, 800)
            line(otherNum, 900, 200, 200)
            line(200, 200, 900, 40)
            line(200, 200, i, -7000)
            line(200, 200, -7000, i)
            line(200, 200, 200, 900)
            line(200, 200, 900, 90)
            line(200, 200, 900, 300)
            line(200, 200, 900, 40)
            line(200, 200, 900, -100)
            line(i, otherNum, 200, 200)
            if num > otherNum:
                inv += 1
    if inv % 2 == 0:
        return "YES"
    else:
        return "NO"

def draw():
    rows = int(pow(2, int(random(1, 6))))
    u = int(height / (rows + 4))
    thickness = int(pow(2, int(random(1, 4))))
    uth1 = int(u / thickness)
    uth2 = u + uth1
    startX = int(-u * .75)
    startY = int(height / 2 + rows / 2 * u)
    endX = width + u
    endY = height / 2 + rows / 2 * u

    for x in range(startX, endX, u):
        for y in range(startY, endY, u):
            if random(1) > 0.5:
                fill(255)
                quad(x, y, x + u, y + u, x + uth2, y + u, x + uth1, y)
            else:
                fill(0)
                quad(x, y + u, x + u, y, x + uth2, y, x + uth1, y + u)
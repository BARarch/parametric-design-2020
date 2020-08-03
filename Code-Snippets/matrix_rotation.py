def draw(matrix, r):

    matrix = [[int(random(50) for i in range(10)) for j in range(12)]]
    r = 12
    from collections import deque

    ## Generator for the parimeter bounds
    def bounds(matrix):
        x0, y0, x1, y1 = 0, 0, len(matrix[0]), len(matrix)

        while x0 < x1 and y0 < y1:
            yield x0, y0, x1, y1
            x0 += 1
            x1 -= 1
            y0 += 1
            y1 -= 1

    ## Generator for the parimeter index sequences
    def sequences(x0, y0, x1, y1):
        # Go Left
        x = x0
        y = y0
        for _ in range(x0, x1 - 1):
            yield x, y
            x += 1

        # Go Down
        for _ in range(y0, y1 - 1):
            yield x, y
            y += 1

        # Go Right
        for _ in range(x1 - 1, x0, -1):
            yield x, y
            x -= 1

        # Go Up Again
        for _ in range(y1 - 1, y0, -1):
            yield x, y
            y -= 1

    def print_res(matrix):
        for row in matrix:
            print(' '.join(map(str, row)))

    for bound in bounds(matrix):
        q = deque()
        #print(bound)
        for x, y in sequences(*bound):
            q.append(matrix[y][x])

        for _ in range(r % len(q)):
            q.append(q.popleft())

        for x, y in sequences(*bound):
            matrix[y][x] = q.popleft()

    print_res(matrix)
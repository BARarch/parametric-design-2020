def draw():
    A = [int(random(100)) for i in range(20)]
    # Count inversions
    inv = 0
    for i, num in enumerate(A):
        for otherNum in A[i + 1:]:
            if num > otherNum:
                inv += 1
    if inv % 2 == 0:
        return "YES"
    else:
        return "NO"
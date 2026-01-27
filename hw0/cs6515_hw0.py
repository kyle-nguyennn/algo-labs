def HW0(A: tuple[int, ...]) -> tuple[int, list[int]]:
    n = len(A)

    if n == 0:
        return 0, []

    t = []

    for i in range(n):
        t.append(1)

        for j in range(i):
            if (A[j] < A[i]) and (t[i] < 1 + t[j]):
                t[i] = 1 + t[j]

    length = end = max(t)

    positions = []

    for i in reversed(range(n)):
        if t[i] == end:
            positions.append(i)

            end -= 1

    positions.reverse()

    return length, positions

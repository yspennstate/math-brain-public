def fwht_int(a):
    a = list(a); h = 1; n = len(a)
    while h < n:
        for i in range(0, n, 2 * h):
            for j in range(i, i + h):
                x, y = a[j], a[j + h]; a[j], a[j + h] = x + y, x - y
        h *= 2
    return a

from itertools import combinations, permutations


def closure(n, edges):
    r = [[False] * n for _ in range(n)]
    for u, v in edges:
        r[u][v] = True
    for k in range(n):
        for i in range(n):
            if r[i][k]:
                for j in range(n):
                    if r[k][j]:
                        r[i][j] = True
    return r


def extensions(elements, r):
    elements = tuple(elements)
    out = []
    for p in permutations(elements):
        pos = {x: i for i, x in enumerate(p)}
        if all(not r[x][y] or pos[x] < pos[y]
               for x in elements for y in elements):
            out.append(p)
    return out


def rel(x, c, r):
    if r[x][c]:
        return "L"
    if r[c][x]:
        return "R"
    return "I"


def interval(tau, c, r):
    pos = {x: i + 1 for i, x in enumerate(tau)}
    n = len(tau)
    a = max([pos[x] for x in tau if r[x][c]] or [0])
    b = min([pos[x] - 1 for x in tau if r[c][x]] or [n])
    assert a <= b
    return a, b, b - a + 1


def predicted_delta(tau, i, c, r):
    a, b, _ = interval(tau, c, r)
    u, v = tau[i], tau[i + 1]
    rr = i + 1
    cu, cv = rel(u, c, r), rel(v, c, r)
    if cu == "L" and cv == "I" and a == rr:
        return -1
    if cu == "I" and cv == "L" and a == rr + 1:
        return +1
    if cu == "R" and cv == "I" and b == rr - 1:
        return +1
    if cu == "I" and cv == "R" and b == rr:
        return -1
    return 0


n = 5
c = 2
pairs = list(combinations(range(n), 2))
checked = 0
nonzero = 0

for mask in range(1 << len(pairs)):
    edges = [pairs[k] for k in range(len(pairs)) if (mask >> k) & 1]
    r = closure(n, edges)
    Q = [x for x in range(n) if x != c]
    for tau in extensions(Q, r):
        for i in range(len(tau) - 1):
            u, v = tau[i], tau[i + 1]
            if r[u][v] or r[v][u]:
                continue
            tau2 = list(tau)
            tau2[i], tau2[i + 1] = tau2[i + 1], tau2[i]
            tau2 = tuple(tau2)

            a, b, w = interval(tau, c, r)
            a2, b2, w2 = interval(tau2, c, r)
            d = w2 - w
            pd = predicted_delta(tau, i, c, r)
            checked += 1
            nonzero += (d != 0)

            assert abs(d) <= 1
            assert d == pd
            I = set(range(a, b + 1))
            I2 = set(range(a2, b2 + 1))
            assert I <= I2 or I2 <= I
            assert len(I ^ I2) <= 1

print(f"PASS checked={checked} nonzero={nonzero}")

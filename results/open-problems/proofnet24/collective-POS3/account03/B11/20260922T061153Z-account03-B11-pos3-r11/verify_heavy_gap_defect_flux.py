from itertools import combinations


def closure(n, mask):
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    r = [0] * n
    for k, (i, j) in enumerate(pairs):
        if (mask >> k) & 1:
            r[i] |= 1 << j
    for k in range(n - 1, -1, -1):
        for i in range(k):
            if (r[i] >> k) & 1:
                r[i] |= r[k]
    return tuple(r)


def lt(r, i, j):
    return bool((r[i] >> j) & 1)


def inc(r, i, j):
    return i != j and not lt(r, i, j) and not lt(r, j, i)


def width(r):
    n = len(r)
    w = 0
    for m in range(1 << n):
        v = [i for i in range(n) if (m >> i) & 1]
        if len(v) <= w:
            continue
        if all(inc(r, i, j) for i, j in combinations(v, 2)):
            w = len(v)
    return w


def cover(r, i, j):
    if not lt(r, i, j):
        return False
    return not any(
        k not in (i, j) and lt(r, i, k) and lt(r, k, j)
        for k in range(len(r))
    )


def extensions(r):
    n = len(r)
    pred = [0] * n
    for i in range(n):
        for j in range(n):
            if lt(r, i, j):
                pred[j] |= 1 << i
    out = []

    def rec(a, used):
        if len(a) == n:
            out.append(tuple(a))
            return
        for v in range(n):
            if not (used >> v) & 1 and pred[v] & ~used == 0:
                rec(a + [v], used | (1 << v))

    rec([], 0)
    return out


def valid(L, r):
    p = {v: i for i, v in enumerate(L)}
    return all(
        not lt(r, i, j) or p[i] < p[j]
        for i in range(len(r))
        for j in range(len(r))
    )


def swap(L, u, v):
    a = list(L)
    i = a.index(u)
    j = a.index(v)
    a[i], a[j] = a[j], a[i]
    return tuple(a)


def channels(r, x, y, a):
    n = len(r)
    c1 = [q for q in range(n) if q not in (x, y, a) and cover(r, x, q) and inc(r, q, a)]
    c2 = [q for q in range(n) if q not in (x, y, a) and cover(r, q, a) and inc(r, q, x)]
    c3 = [q for q in range(n) if q not in (x, y, a) and cover(r, a, q) and inc(r, q, y)]
    c4 = [q for q in range(n) if q not in (x, y, a) and cover(r, q, y) and inc(r, q, a)]
    return c1, c2, c3, c4


def has_canonical_witness(r, x, y, a, L, side):
    p = {v: i for i, v in enumerate(L)}
    c1, c2, c3, c4 = channels(r, x, y, a)
    if side == "L":
        return any(p[x] < p[q] < p[a] for q in c1 + c2)
    return any(p[a] < p[q] < p[y] for q in c3 + c4)


P = T = H = 0
maxch = 0
for n in range(3, 7):
    seen = set()
    for m in range(1 << (n * (n - 1) // 2)):
        r = closure(n, m)
        if r in seen:
            continue
        seen.add(r)
        if width(r) > 3:
            continue
        P += 1
        le = extensions(r)
        E = len(le)
        for x in range(n):
            for y in range(n):
                if not cover(r, x, y):
                    continue
                for a in range(n):
                    if a in (x, y) or not (inc(r, a, x) and inc(r, a, y)):
                        continue
                    T += 1
                    A, M, C = [], [], []
                    for L in le:
                        p = {v: i for i, v in enumerate(L)}
                        if p[a] < p[x]:
                            A.append(L)
                        elif p[a] < p[y]:
                            M.append(L)
                        else:
                            C.append(L)
                    oL = [L for L in M if not valid(swap(L, a, x), r)]
                    iL = [L for L in A if not valid(swap(L, a, x), r)]
                    oR = [L for L in M if not valid(swap(L, a, y), r)]
                    iR = [L for L in C if not valid(swap(L, a, y), r)]
                    assert len(oL) + len(oR) - len(iL) - len(iR) == 3 * len(M) - E
                    assert all(has_canonical_witness(r, x, y, a, L, "L") for L in oL)
                    assert all(has_canonical_witness(r, x, y, a, L, "R") for L in oR)
                    ch = channels(r, x, y, a)
                    assert len(ch[0]) <= 1 and len(ch[1]) <= 2 and len(ch[2]) <= 2 and len(ch[3]) <= 1
                    maxch = max(maxch, sum(map(len, ch)))
                    if 3 * len(M) > E:
                        H += 1

# Exact calibration: relations 0<2, 0<3, 1<2; x=0, y=3, a=4.
r = closure(5, (1 << 1) | (1 << 2) | (1 << 4))
le = extensions(r)
E = len(le)
x, y, a = 0, 3, 4
A = M = C = oL = iL = oR = iR = 0
for L in le:
    p = {v: i for i, v in enumerate(L)}
    if p[a] < p[x]:
        A += 1
        iL += not valid(swap(L, a, x), r)
    elif p[a] < p[y]:
        M += 1
        oL += not valid(swap(L, a, x), r)
        oR += not valid(swap(L, a, y), r)
    else:
        C += 1
        iR += not valid(swap(L, a, y), r)
p24 = sum(L.index(2) < L.index(4) for L in le)
assert (E, A, M, C, oL, iL, oR, iR, p24) == (25, 7, 9, 9, 2, 0, 0, 0, 7)
assert channels(r, x, y, a) == ([2], [], [], [])

print("width<=3 naturally-labelled posets n<=6:", P)
print("cover/incomparable triples checked:", T)
print("heavy triples 3H>E:", H)
print("maximum canonical off-bridge channel count observed:", maxch)
print("calibration E,A,H,C,outL,inL,outR,inR,N(2<4):", E, A, M, C, oL, iL, oR, iR, p24)
print("POS3_HEAVY_GAP_DEFECT_FLUX_CHECK_PASS")

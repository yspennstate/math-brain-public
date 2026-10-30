from fractions import Fraction
from functools import lru_cache
from itertools import combinations

N = 9
COVERS = [
    (0, 6), (0, 7), (1, 4), (2, 3), (2, 7),
    (3, 6), (4, 5), (5, 7), (6, 8),
]
D0, U0, X0, L0, Y0 = 3, 7, 5, 0, 6

lt = [[False] * N for _ in range(N)]
for a, b in COVERS:
    lt[a][b] = True
for k in range(N):
    for i in range(N):
        if lt[i][k]:
            for j in range(N):
                if lt[k][j]:
                    lt[i][j] = True

pred = [0] * N
for v in range(N):
    mask = 0
    for u in range(N):
        if lt[u][v]:
            mask |= 1 << u
    pred[v] = mask

@lru_cache(None)
def extend(mask):
    if mask == (1 << N) - 1:
        return ((),)
    ans = []
    for v in range(N):
        if mask & (1 << v):
            continue
        if pred[v] & ~mask:
            continue
        for tail in extend(mask | (1 << v)):
            ans.append((v,) + tail)
    return tuple(ans)

EXTS = extend(0)
E = len(EXTS)

def before(a, b):
    c = 0
    for L in EXTS:
        p = {v: i for i, v in enumerate(L)}
        c += p[a] < p[b]
    return Fraction(c, E)

def order3(a, b, c):
    q = 0
    for L in EXTS:
        p = {v: i for i, v in enumerate(L)}
        q += p[a] < p[b] < p[c]
    return Fraction(q, E)

def is_cover(a, b):
    if not lt[a][b]:
        return False
    return not any(v != a and v != b and lt[a][v] and lt[v][b] for v in range(N))

width = 0
width_witness = None
for r in range(1, N + 1):
    for S in combinations(range(N), r):
        if all(not lt[a][b] and not lt[b][a] for a, b in combinations(S, 2)):
            width = r
            width_witness = S

D = [v for v in range(N) if lt[v][U0] and not lt[v][D0]]
U = [v for v in range(N) if lt[D0][v] and not lt[U0][v]]
Dmax = [v for v in D if not any(v != w and lt[v][w] for w in D)]
Umin = [v for v in U if not any(v != w and lt[w][v] for w in U)]

p_du = before(D0, U0)
p_dx = before(D0, X0)
p_ld = before(L0, D0)
p_yu = before(Y0, U0)
p_x_y = before(X0, Y0)
p_ldu = order3(L0, D0, U0)

assert E == 353
assert width == 3
assert D == [0, 1, 4, 5]
assert Dmax == [0, 5]
assert U == [6, 8]
assert Umin == [6]
assert is_cover(L0, U0)
assert is_cover(X0, U0)
assert is_cover(D0, Y0)
assert p_du == Fraction(333, 353) and p_du > Fraction(5, 6)
assert p_dx == Fraction(261, 353) and p_dx > Fraction(2, 3)
assert p_ld == Fraction(242, 353) and p_ld > Fraction(2, 3)
assert p_yu == Fraction(273, 353) and p_yu > Fraction(2, 3)
assert p_ldu == Fraction(222, 353) and p_ldu > Fraction(1, 2)
assert p_ldu == p_ld + p_du - 1
assert Fraction(1, 3) <= p_x_y <= Fraction(2, 3)

print("extensions", E)
print("width", width, "witness", width_witness)
print("D", D, "Dmax", Dmax)
print("U", U, "Umin", Umin)
print("covers", (L0, U0), is_cover(L0, U0), (X0, U0), is_cover(X0, U0), (D0, Y0), is_cover(D0, Y0))
print("P(d<u)", p_du)
print("P(d<x)", p_dx)
print("P(l<d)", p_ld)
print("P(y<u)", p_yu)
print("P(l<d<u)", p_ldu)
print("identity_rhs", p_ld + p_du - 1)
print("balanced_escape_P(x<y)", p_x_y)
print("POS3_SECOND_BLOCKER_SUPERHEAVY_CHECK_PASS")

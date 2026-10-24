from fractions import Fraction

P = 257
C0 = Fraction(-123, 200)
C1 = Fraction(-3, 100)
C2 = Fraction(1, 100)
C3 = Fraction(-3, 400)
T = Fraction(53, 5)

def legendre_symbol(a, p):
    a %= p
    if a == 0:
        return 0
    v = pow(a, (p - 1) // 2, p)
    return 1 if v == 1 else -1

def build_graph(p):
    V = [x for x in range(p)
         if x not in (0, 1)
         and legendre_symbol(x, p) == 1
         and legendre_symbol(x - 1, p) == 1]
    n = len(V)
    A = [[0] * n for _ in range(n)]
    for i, x in enumerate(V):
        for j in range(i + 1, n):
            y = V[j]
            if legendre_symbol(x - y, p) == 1:
                A[i][j] = A[j][i] = 1
    return V, A

def ldl_positive_definite(M):
    n = len(M)
    L = [[Fraction(0) for _ in range(n)] for __ in range(n)]
    D = [Fraction(0) for _ in range(n)]
    for i in range(n):
        L[i][i] = Fraction(1)
        D[i] = M[i][i] - sum(L[i][k] * L[i][k] * D[k] for k in range(i))
        assert D[i] > 0, (i, D[i])
        for j in range(i + 1, n):
            numer = M[j][i] - sum(L[j][k] * L[i][k] * D[k] for k in range(i))
            L[j][i] = numer / D[i]
    for i in range(n):
        for j in range(n):
            s = sum(L[i][k] * D[k] * L[j][k] for k in range(min(i, j) + 1))
            assert s == M[i][j], (i, j)
    return D

V, A = build_graph(P)
n = len(V)
assert n == (P - 5) // 4 == 63
deg = [sum(row) for row in A]
assert sum(deg) == 2 * 945
assert sum(deg) == 30 * n
assert sorted(set(deg)) == [28, 30, 32, 34]

Svals = []
for x, dx in zip(V, deg):
    Sx = sum(legendre_symbol(t * (t - 1) * (t - x), P) for t in range(P))
    Svals.append(Sx)
    assert 8 * dx == P - 15 + Sx
assert sorted(set(Svals)) == [-18, -2, 14, 30]

Vset = set(V)
def r(x): return (1 - x) % P
def s(x): return pow(x, -1, P)
idx = {x:i for i,x in enumerate(V)}
for x in V:
    assert r(x) in Vset and s(x) in Vset
for i, x in enumerate(V):
    for j, y in enumerate(V):
        if i == j:
            continue
        axy = A[i][j]
        assert A[idx[r(x)]][idx[r(y)]] == axy
        assert A[idx[s(x)]][idx[s(y)]] == axy

seen = set()
orbit_sizes = []
for x in V:
    if x in seen:
        continue
    orb = set()
    frontier = [x]
    while frontier:
        y = frontier.pop()
        if y in orb:
            continue
        orb.add(y)
        frontier += [r(y), s(y)]
    seen |= orb
    orbit_sizes.append(len(orb))
assert sorted(orbit_sizes) == [3] + [6] * 10

eps2 = int(P % 8 == 1)
eps3 = int(P % 12 == 1)
regular = (n - 3 * eps2 - 2 * eps3) // 6
assert regular == 10 and eps2 == 1 and eps3 == 0
assert len(orbit_sizes) == regular + eps2 + eps3 == 11

delta = [d - 30 for d in deg]
B = [[Fraction(0) for _ in range(n)] for __ in range(n)]
for i in range(n):
    for j in range(n):
        if i == j or A[i][j] == 1:
            B[i][j] = Fraction(1)
        else:
            di, dj = delta[i], delta[j]
            B[i][j] = (C0 + C1 * (di + dj) + C2 * di * dj
                       + C3 * (di * di + dj * dj))

M = [[(T if i == j else Fraction(0)) - B[i][j] for j in range(n)] for i in range(n)]
D = ldl_positive_definite(M)
threshold_margin = Fraction(4 * P, 9) - T * T
assert threshold_margin == Fraction(419, 225) > 0

print("P04-I0101-P257-DEGREE-AWARE-DUAL=PASS")
print(f"p={P}")
print(f"|V2|={n}")
print(f"edges={sum(deg)//2}")
print(f"degree_set={sorted(set(deg))}")
print(f"legendre_trace_set={sorted(set(Svals))}")
print(f"s3_orbit_sizes={sorted(orbit_sizes)}")
print(f"dual_coeffs={C0},{C1},{C2},{C3}")
print(f"t={T}")
print(f"threshold_margin_4p_over_9_minus_t2={threshold_margin}")
print(f"ldl_pivots_positive={len(D)}")
print(f"min_pivot_exact={min(D)}")
print("EXACT_RECONSTRUCTION=PASS")

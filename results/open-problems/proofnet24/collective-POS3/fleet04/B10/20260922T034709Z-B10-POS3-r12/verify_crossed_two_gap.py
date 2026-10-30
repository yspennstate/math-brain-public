from itertools import combinations

N = 15
EDGES = [
    (0,1),(0,10),(1,2),(2,3),(2,12),(3,4),(3,9),(5,6),
    (6,2),(6,11),(7,3),(7,8),(7,13),(8,4),(8,9),(9,14),
    (10,6),(11,7),(11,12),(12,8),(12,13),(13,4),(13,14),
]
X,Y,D,U = 3,13,12,9

reach = [[False]*N for _ in range(N)]
for a,b in EDGES:
    reach[a][b] = True
for k in range(N):
    for i in range(N):
        if reach[i][k]:
            for j in range(N):
                if reach[k][j]:
                    reach[i][j] = True

predmask = [0]*N
for v in range(N):
    for w in range(N):
        if reach[w][v]:
            predmask[v] |= 1 << w

extensions = []
def rec(mask, order):
    if len(order) == N:
        extensions.append(tuple(order))
        return
    for v in range(N):
        if not (mask >> v) & 1 and not (predmask[v] & ~mask):
            rec(mask | (1 << v), order + (v,))
rec(0, ())

E = len(extensions)
Nxy = A = B = H = N8y = 0
for L in extensions:
    p = {v:i for i,v in enumerate(L)}
    Nxy += p[X] < p[Y]
    A += p[X] < p[D]
    B += p[U] < p[Y]
    H += (p[X] < p[D] and p[U] < p[Y])
    N8y += p[8] < p[Y]

R = A + B - H

pred = lambda v: {w for w in range(N) if reach[w][v]}
succ = lambda v: {w for w in range(N) if reach[v][w]}

assert E == 1810
assert Nxy == 1207
assert pred(Y) - pred(X) == {D}
assert pred(X) - pred(Y) == set()
assert succ(X) - succ(Y) == {U}
assert succ(Y) - succ(X) == set()
assert reach[D][U]
assert (A,B,H,R) == (336,352,84,604)
assert 2*Nxy - E == R
assert 3*Nxy - 2*E == 1
assert 3*R - E == 2
assert N8y == 1081

print("extensions", E)
print("crossed_pair", X, Y, "Nxy", Nxy, "fraction", f"{Nxy}/{E}")
print("lower_only_event_A", A, "fraction", f"{A}/{E}")
print("upper_only_event_B", B, "fraction", f"{B}/{E}")
print("intersection_H", H, "fraction", f"{H}/{E}")
print("union_R", R, "fraction", f"{R}/{E}")
print("identity_2Nxy_minus_E", 2*Nxy-E, "equals_R", R)
print("threshold_count_3Nxy_minus_2E", 3*Nxy-2*E)
print("union_threshold_3R_minus_E", 3*R-E)
print("balanced_escape_pair_8_13", N8y, "fraction", f"{N8y}/{E}")
print("POS3_CROSSED_TWO_GAP_REGRESSION_PASS")

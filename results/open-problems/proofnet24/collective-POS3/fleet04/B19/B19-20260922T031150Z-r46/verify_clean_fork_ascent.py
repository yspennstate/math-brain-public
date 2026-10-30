from functools import lru_cache
from fractions import Fraction

N = 8
GENERATORS = [
    (0,2),(0,5),(1,2),(1,3),(1,6),
    (2,4),(3,4),(3,5),(5,7),(6,7),
]

lt = [[False]*N for _ in range(N)]
for i,j in GENERATORS:
    lt[i][j] = True
for k in range(N):
    for i in range(N):
        if lt[i][k]:
            for j in range(N):
                if lt[k][j]:
                    lt[i][j] = True

predmask = []
for v in range(N):
    m = 0
    for u in range(N):
        if lt[u][v]:
            m |= 1 << u
    predmask.append(m)

@lru_cache(None)
def extensions(mask):
    if mask == (1 << N) - 1:
        return ((),)
    out = []
    for v in range(N):
        if (mask >> v) & 1:
            continue
        if predmask[v] & ~mask:
            continue
        for tail in extensions(mask | (1 << v)):
            out.append((v,) + tail)
    return tuple(out)

LE = extensions(0)
E = len(LE)

def count_before(a,b):
    return sum(1 for L in LE if L.index(a) < L.index(b))

def predset(v):
    return {u for u in range(N) if lt[u][v]}

def rel(u,v):
    if lt[u][v]:
        return -1
    if lt[v][u]:
        return 1
    return 0

def distinguishers(a,b):
    return [z for z in range(N) if z not in (a,b) and rel(z,a) != rel(z,b)]

def positive_blockers(a,b):
    S = [w for w in range(N)
         if w not in (a,b) and lt[a][w] and rel(w,b) == 0]
    return sorted(w for w in S if not any(v != w and v in S and lt[v][w] for v in S))

a,b = 3,6
z1,z2 = positive_blockers(a,b)
assert (z1,z2) == (4,5)
assert predset(a) == predset(b) == {1}
assert count_before(a,b) == 82

B1 = count_before(b,z1)
B2 = count_before(b,z2)
Q = sum(1 for L in LE if L.index(b) < L.index(z1) and L.index(b) < L.index(z2))
A1 = E - B1
A2 = E - B2
joint_reverse = sum(1 for L in LE
                    if L.index(z1) < L.index(b) and L.index(z2) < L.index(b))
U = E - Q
R = 2*(E-count_before(a,b)) - Q

assert B1 == 103 and B2 == 83
assert Q == 78
assert joint_reverse == 13
assert Q*E >= B1*B2
assert U*3 > E
assert U*9 < 5*E
assert R*9 < 2*E

# The fork children are 4 and 5. Their strong-majority orientation in this
# witness is 5 before 4. This next pair has unequal predecessor sets and
# exactly two distinguishers, one lower and one upper.
a1,b1 = 5,4
assert count_before(a1,b1) == 93
assert predset(a1) == {0,1,3}
assert predset(b1) == {0,1,2,3}
assert distinguishers(a1,b1) == [2,7]

print("extensions", E)
print("equal_pred_pair", a, b, "count", count_before(a,b),
      "prob", Fraction(count_before(a,b),E))
print("positive_blockers", [z1,z2])
print("b_before_blockers", B1, B2,
      "probs", Fraction(B1,E), Fraction(B2,E))
print("Q", Q, "Q_prob", Fraction(Q,E))
print("tp2_lower_tail_cross", Q*E, B1*B2, "slack", Q*E-B1*B2)
print("positive_union_U", U, "U_prob", Fraction(U,E))
print("reverse_remainder_R", R, "R_prob", Fraction(R,E))
print("child_extreme_pair", a1, b1, "count", count_before(a1,b1),
      "prob", Fraction(count_before(a1,b1),E))
print("child_pred_sets", sorted(predset(a1)), sorted(predset(b1)))
print("child_distinguishers", distinguishers(a1,b1))
print("POS3_CLEAN_FORK_ASCENT_REGRESSION_PASS")

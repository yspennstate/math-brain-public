from fractions import Fraction as F
from itertools import combinations

ASSERTIONS = 0

def ck(cond, msg):
    global ASSERTIONS
    ASSERTIONS += 1
    if not cond:
        raise AssertionError(msg)

def hitting_times(P):
    n = len(P)
    h = [F(0) for _ in range(n)]
    ck(P[0][0] == 1, "state 1 absorbing")
    for i in range(1, n):
        ck(sum(P[i]) == 1, ("row stochastic", i))
        for j in range(i, n):
            ck(P[i][j] == 0, ("strictly downward", i, j))
        h[i] = 1 + sum(P[i][j] * h[j] for j in range(i))
        ck(h[i] == 1 + sum(P[i][j] * h[j] for j in range(i)), ("harmonic", i))
    return h

def cut_outflow(P, A):
    n = len(P)
    A = set(A)
    return sum(P[i][j] for i in A for j in range(n) if j not in A)

def all_cuts(P):
    n = len(P)
    transient = list(range(1, n))
    rows = []
    for r in range(1, len(transient)+1):
        for A in combinations(transient, r):
            q = cut_outflow(P, A)
            ck(q > 0, ("positive downward cut flow", A))
            c = F(len(A) * (n-len(A)), n) / q
            rows.append((c, A, q))
    return rows

def kappa(P):
    rows = all_cuts(P)
    b = max(c for c, _, _ in rows)
    return b, [A for c, A, _ in rows if c == b]

def best_contiguous_kappa(P):
    n = len(P)
    rows = []
    for a in range(1, n):
        for b in range(a, n):
            A = tuple(range(a, b+1))
            q = cut_outflow(P, A)
            c = F(len(A) * (n-len(A)), n) / q
            rows.append((c, A))
    best = max(c for c, _ in rows)
    return best, [A for c, A in rows if c == best]

def oriented_energy(P, f):
    n = len(P)
    return sum(P[i][j] * max(f[i]-f[j], F(0))
               for i in range(1,n) for j in range(i))

def upward_energy(P, f):
    n = len(P)
    return sum(P[i][j] * max(f[j]-f[i], F(0))
               for i in range(1,n) for j in range(i))

def pair_positive(f):
    n=len(f)
    return sum(max(f[i]-f[j], F(0)) for i in range(n) for j in range(n))

def coarea_integrals(P, f):
    levels = sorted(set(f))
    left = F(0)
    q_int = F(0)
    card_int = F(0)
    for right in levels[1:]:
        mid = (left + right) / 2
        A = tuple(i for i, x in enumerate(f) if x > mid)
        width = right-left
        q_int += width * cut_outflow(P, A)
        card_int += width * F(len(A) * (len(f)-len(A)))
        left = right
    return q_int, card_int

def math_labels(A):
    return tuple(i+1 for i in A)

P1 = [[F(0) for _ in range(5)] for _ in range(5)]
P1[0][0] = 1
P1[1][0] = 1
P1[2][1] = 1
P1[3][0] = F(3,4)
P1[3][2] = F(1,4)
P1[4][3] = 1

h1 = hitting_times(P1)
ck(h1 == [F(0), F(1), F(2), F(3,2), F(5,2)], ("h1", h1))
ck(h1[3] < h1[2], "interior dip")
ck(max(h1) == h1[4], "top state still maximizer")
kap1, sets1 = kappa(P1)
ck(kap1 == F(6,5), ("kappa1", kap1, sets1))
J1 = oriented_energy(P1, h1)
U1 = upward_energy(P1, h1)
S1 = pair_positive(h1)
ck(J1 == F(33,8), ("J1", J1))
ck(U1 == F(1,8), ("U1", U1))
ck(J1-U1 == 4, ("Bellman signed balance", J1-U1))
ck(S1 == 12, ("pair positive", S1))
qint1, cardint1 = coarea_integrals(P1, h1)
ck(qint1 == J1, ("coarea edge", qint1, J1))
ck(cardint1 == S1, ("coarea pair", cardint1, S1))
ck(J1 >= S1/(5*kap1), ("coarea-kappa inequality", J1, S1/(5*kap1)))

P2 = [[F(0) for _ in range(5)] for _ in range(5)]
P2[0][0] = 1
P2[1][0] = 1
P2[2][0] = F(1,4)
P2[2][1] = F(3,4)
P2[3][1] = F(1,4)
P2[3][2] = F(3,4)
P2[4][2] = 1

h2 = hitting_times(P2)
ck(h2 == [F(0), F(1), F(7,4), F(41,16), F(11,4)], ("h2", h2))
kap2, sets2 = kappa(P2)
ck(kap2 == F(6,5), ("kappa2", kap2, sets2))
ck(sets2 == [(2,4)], ("unique worst cut", sets2))
cont2, csets2 = best_contiguous_kappa(P2)
ck(cont2 == F(24,25), ("contiguous kappa", cont2, csets2))
ck(kap2/cont2 == F(5,4), ("contiguous loss factor", kap2/cont2))

for tag, P, h, kap in [("P1",P1,h1,kap1),("P2",P2,h2,kap2)]:
    levels = sorted(set(h))
    for a,b in zip(levels, levels[1:]):
        mid=(a+b)/2
        A=tuple(i for i,x in enumerate(h) if x>mid)
        q=cut_outflow(P,A)
        lower=F(len(A)*(len(P)-len(A)), len(P)*kap)
        ck(q >= lower, (tag, "level cut", A, q, lower))
    qint, cardint = coarea_integrals(P,h)
    ck(qint == oriented_energy(P,h), (tag,"coarea_q"))
    ck(cardint == pair_positive(h), (tag,"coarea_card"))

print("P0250 exact self-check")
print("ASSERTIONS", ASSERTIONS)
print("monotonicity_witness_h", ",".join(str(x) for x in h1))
print("monotonicity_witness_kappa", kap1)
print("monotonicity_witness_J", J1)
print("monotonicity_witness_U", U1)
print("monotonicity_witness_pair_positive", S1)
print("monotonicity_coarea_lower_rhs", S1/(5*kap1))
print("noncontiguous_witness_h", ",".join(str(x) for x in h2))
print("noncontiguous_witness_kappa", kap2)
print("noncontiguous_worst_cut_math_labels", math_labels(sets2[0]))
print("best_contiguous_kappa", cont2)
print("noncontiguous_over_contiguous_ratio", kap2/cont2)
print("ALL_EXACT_P0250_COAREA_OBSTRUCTION_CHECKS_PASS")

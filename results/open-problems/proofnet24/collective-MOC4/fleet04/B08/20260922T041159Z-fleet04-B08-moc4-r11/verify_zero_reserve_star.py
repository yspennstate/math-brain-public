from fractions import Fraction
from itertools import permutations, combinations

S4 = list(permutations(range(4)))
TRANS = list(combinations(range(4), 2))
ID = (0, 1, 2, 3)
V4 = [ID, (1, 0, 3, 2), (2, 3, 0, 1), (3, 2, 1, 0)]


def compose(p, q):
    return tuple(p[q[i]] for i in range(4))


def swap_values(p, i, j):
    return tuple(j if x == i else i if x == j else x for x in p)


def swap_positions(p, i, j):
    q = list(p)
    q[i], q[j] = q[j], q[i]
    return tuple(q)


def gmul(z, w):
    a, b = z
    c, d = w
    return (a*c-b*d, a*d+b*c)


def support(a, b):
    H = {}
    for p in S4:
        z = (1, 0)
        for i in range(4):
            x = (a[i][0] + b[p[i]][0], a[i][1] + b[p[i]][1])
            z = gmul(z, x)
        H[p] = Fraction(z[0], 1)  # eta=1, real-part support
    return H


def v4_coset(p):
    return {compose(p, v) for v in V4}


def analyze(a, b):
    H = support(a, b)
    M = max(H.values())
    maximizers = [p for p in S4 if H[p] == M]
    assert len(maximizers) == 1
    star = maximizers[0]
    m = sum(H.values(), Fraction(0)) / 24

    cosets = []
    unseen = set(S4)
    while unseen:
        p = next(iter(unseen))
        c = v4_coset(p)
        cosets.append(c)
        unseen -= c
    Q = max(sum((H[p] for p in c), Fraction(0))/4 for c in cosets)
    B = sum((H[p] for p in v4_coset(star)), Fraction(0))/4
    d = M-m
    Delta = M-Q

    ans = {}
    for side, neigh in (("out", swap_values), ("in", swap_positions)):
        gaps = []
        excess = []
        neigh_values = []
        for i, j in TRANS:
            roof_sum = max(H[p] + H[neigh(p, i, j)] for p in S4)
            v = H[neigh(star, i, j)]
            gaps.append(2*M-roof_sum)
            excess.append(roof_sum-(M+v))
            neigh_values.append(v)
        G = sum(gaps, Fraction(0))
        E = sum(excess, Fraction(0))
        R = 3*d-Delta-G/2
        # Lead six-transposition identity at the maximizing permutation.
        assert sum(neigh_values, Fraction(0)) == 6*m + 2*(M-B)
        # New exact reserve decomposition.
        assert R == (Q-B) + E/2
        ans[side] = (gaps, excess, G, E, R)
    return H, M, m, Q, B, d, Delta, star, ans


def f(x):
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def show(name, x):
    _, M, m, Q, B, d, Delta, star, ans = x
    print(name, "maximizer", star)
    print("M", f(M), "m", f(m), "Q", f(Q), "Bstar", f(B), "d", f(d), "Delta", f(Delta))
    for side in ("out", "in"):
        gaps, excess, G, E, R = ans[side]
        print(side, "gaps", [f(v) for v in gaps], "G", f(G))
        print(side, "star_excess", [f(v) for v in excess], "E", f(E), "reserve", f(R))
    print("bilateral_reserve", f(min(ans["out"][-1], ans["in"][-1])))


lead = analyze(
    [(-1,0),(2,0),(1,0),(0,0)],
    [(-1,0),(1,0),(-2,0),(2,0)],
)
partner = analyze(
    [(-4,4),(0,-1),(-3,2),(-4,-4)],
    [(-4,-4),(2,-1),(2,-4),(4,-1)],
)
show("lead", lead)
show("partner", partner)

# Lead: one side is exactly zero reserve because the maximizing endpoint's
# V4 fiber is Q-maximal and all six incident in-side transposition edges attain
# their pair roofs. The other side misses one roof by 4, hence reserve 2.
assert lead[4] == lead[3] == 15
assert lead[8]["out"][3] == 4 and lead[8]["out"][4] == 2
assert lead[8]["in"][3] == 0 and lead[8]["in"][4] == 0

# Partner: the maximizing endpoint is also in a Q-maximal V4 fiber, but large
# star-edge roof excess remains on both sides, so the bilateral reserve is 529.
assert partner[4] == partner[3] == Fraction(245, 2)
assert partner[8]["out"][3] == 1058 and partner[8]["out"][4] == 529
assert partner[8]["in"][3] == 1174 and partner[8]["in"][4] == 587

print("PASS MOC4-ZERO-RESERVE-ENDPOINT-STAR-RIGIDITY-v1")

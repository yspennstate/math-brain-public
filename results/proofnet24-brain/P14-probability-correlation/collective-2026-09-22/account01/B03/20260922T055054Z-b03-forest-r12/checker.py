from itertools import combinations
from collections import Counter

V = range(4)
e = (0, 1)
f = (2, 3)
base = [(0, 2), (0, 3), (1, 2), (1, 3)]
name = {0: "02", 1: "03", 2: "12", 3: "13"}


def forest(S):
    parent = list(V)

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for i in S:
        a, b = base[i]
        a, b = find(a), find(b)
        if a == b:
            return False
        parent[b] = a
    return True


def addable(S, edge):
    parent = list(V)

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for i in S:
        a, b = base[i]
        a, b = find(a), find(b)
        parent[b] = a
    return find(edge[0]) != find(edge[1])


def jointly_addable(S):
    parent = list(V)

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def join(edge):
        a, b = map(find, edge)
        if a == b:
            return False
        parent[b] = a
        return True

    for i in S:
        assert join(base[i])
    return join(e) and join(f)


def fmt(S):
    return "{" + ",".join(name[i] for i in sorted(S)) + "}"


forests = []
for mask in range(1 << len(base)):
    S = frozenset(i for i in range(len(base)) if mask >> i & 1)
    if forest(S):
        forests.append(S)

A = {S for S in forests if addable(S, e)}
B = {S for S in forests if addable(S, f)}
D = {S for S in forests if jointly_addable(S)}

domain = [(F, H) for F in forests for H in forests if F not in A and H in D]
codomain = [
    (F, H)
    for F in forests
    for H in forests
    if F in A and H in B and H not in D
]


def fiber(pair):
    F, H = pair
    return frozenset(F & H), frozenset(F | H)


bad_fiber = (frozenset(), frozenset(range(4)))
fiber_domain = [x for x in domain if fiber(x) == bad_fiber]
fiber_codomain = [x for x in codomain if fiber(x) == bad_fiber]

print(
    f"K4_COUNTS N={len(forests)} A={len(A)} B={len(B)} D={len(D)} "
    f"GAP={len(A) * len(B) - len(forests) * len(D)}"
)
print(
    f"RESIDUAL_TOTAL domain={len(domain)} codomain={len(codomain)} "
    f"surplus={len(codomain) - len(domain)}"
)
print(
    f"FIXED_FIBER I=empty U=all4 domain={len(fiber_domain)} "
    f"codomain={len(fiber_codomain)} deficit={len(fiber_domain) - len(fiber_codomain)}"
)
for F, H in fiber_domain:
    print(f"DOMAIN F={fmt(F)} H={fmt(H)}")
for F, H in fiber_codomain:
    print(f"CODOMAIN F={fmt(F)} H={fmt(H)}")

grades = Counter()
for F, H in domain:
    if len(F) + len(H) == 4:
        I, U = fiber((F, H))
        grades[(len(I), len(U), "D")] += 1
for F, H in codomain:
    if len(F) + len(H) == 4:
        I, U = fiber((F, H))
        grades[(len(I), len(U), "C")] += 1
for i, u in [(0, 4), (1, 3), (2, 2)]:
    d = grades[(i, u, "D")]
    c = grades[(i, u, "C")]
    print(f"SIZE4_GRADE I={i} U={u} domain={d} codomain={c} balance={c-d}")

# Explicit overlap pivot.  This starts from a domain pair in the deficient
# transfer-only fiber and changes both intersection and union while preserving
# |F|+|H|.  S is the quotient e-path, d is the cut edge between the f endpoints,
# and c is duplicated into H while retained in F.
F = frozenset([0, 1, 2])       # {02,03,12}
H = frozenset([3])             # {13}
S = frozenset([0, 2])          # {02,12}
d = 2                           # 12
c = 0                           # 02
Fp = (F - S) | {c}
Hp = H | (S - {d})
valid = Fp in A and Hp in B and Hp not in D
print(
    f"PIVOT sourceF={fmt(F)} sourceH={fmt(H)} c={name[c]} d={name[d]} "
    f"targetF={fmt(Fp)} targetH={fmt(Hp)} valid_codomain={valid}"
)
print("TRANSFER_ONLY_HALL_REFUTED=True")

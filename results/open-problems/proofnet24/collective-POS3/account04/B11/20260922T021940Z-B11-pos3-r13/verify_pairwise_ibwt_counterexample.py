from itertools import permutations, combinations
from fractions import Fraction
from collections import Counter

# Five-element width-three poset P.
# Covers: c<b<r, a<r, c<s.  (c<r is transitive.)
# C={c}; Q=P\C has relations a<r and b<r.
NAMES = ("c", "a", "b", "r", "s")
COVERS = {("c", "b"), ("b", "r"), ("a", "r"), ("c", "s")}


def closure(rel):
    out = set(rel)
    changed = True
    while changed:
        changed = False
        for x, y in list(out):
            for u, v in list(out):
                if y == u and (x, v) not in out:
                    out.add((x, v))
                    changed = True
    return out


def extensions(elements, rel):
    ans = []
    for perm in permutations(elements):
        pos = {x: i for i, x in enumerate(perm)}
        if all(pos[x] < pos[y] for x, y in rel):
            ans.append(perm)
    return ans


def prob(exts, x, y):
    return Fraction(sum(e.index(x) < e.index(y) for e in exts), len(exts))


def incomparable(rel, x, y):
    return (x, y) not in rel and (y, x) not in rel


def width(elements, rel):
    best = 0
    for r in range(1, len(elements) + 1):
        for subset in combinations(elements, r):
            if all(incomparable(rel, x, y) for x, y in combinations(subset, 2)):
                best = max(best, r)
    return best


P_REL = closure(COVERS)
Q_NAMES = ("a", "b", "r", "s")
Q_REL = {(x, y) for x, y in P_REL if x in Q_NAMES and y in Q_NAMES}
EP = extensions(NAMES, P_REL)
EQ = extensions(Q_NAMES, Q_REL)

# Structural and exact-count checks.
assert len(EP) == 11
assert len(EQ) == 8
assert width(NAMES, P_REL) == 3
assert {q for q in Q_NAMES if incomparable(P_REL, "c", q)} == {"a"}
assert prob(EP, "c", "a") == Fraction(8, 11) > Fraction(2, 3)

# A uniform-Q balanced pair is pushed outside the balanced interval by the exact
# projected insertion law from P.
assert prob(EQ, "a", "s") == Fraction(5, 8)
assert Fraction(1, 3) <= prob(EQ, "a", "s") <= Fraction(2, 3)
assert prob(EP, "a", "s") == Fraction(8, 11) > Fraction(2, 3)

# The example refutes pairwise transfer only, not the existential IBWT target:
# another Q-balanced pair remains balanced after projection.
assert prob(EQ, "a", "b") == Fraction(1, 2)
assert prob(EP, "a", "b") == Fraction(7, 11)
assert Fraction(1, 3) <= prob(EP, "a", "b") <= Fraction(2, 3)

# Exact restriction weights W_C(tau); C is first in 8 of the 11 extensions.
weights = Counter(tuple(x for x in e if x != "c") for e in EP)
assert sorted(weights.values()) == [1, 1, 1, 1, 1, 2, 2, 2]
prefix = sum(1 for e in EP if e[0] == "c")
assert prefix == 8

print("POS3_PAIRWISE_IBWT_COUNTEREXAMPLE_PASS")
print(f"eQ={len(EQ)} eP={len(EP)} widthP={width(NAMES, P_REL)}")
print(f"Pr_Q(a<s)={prob(EQ, 'a', 's')} Pr_P(a<s)={prob(EP, 'a', 's')}")
print(f"Pr_P(c<a)={prob(EP, 'c', 'a')} prefix_mass={Fraction(prefix, len(EP))}")
print(f"Pr_Q(a<b)={prob(EQ, 'a', 'b')} Pr_P(a<b)={prob(EP, 'a', 'b')}")
print("restriction_weight_multiset=" + str(sorted(weights.values())))

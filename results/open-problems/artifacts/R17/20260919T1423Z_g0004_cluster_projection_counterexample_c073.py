from fractions import Fraction
from collections import defaultdict

# Exact self-check for the finite obstruction used in R17 C073.
# Graph: path b --e1-- x --e2-- y, iid Bernoulli(p), p=3/4.
# Increasing observable f = 1{e2 open}.  Projecting f to the vertex cluster C_b
# is not monotone under cluster inclusion.

p = Fraction(3, 4)
states = [(e1, e2) for e1 in (0, 1) for e2 in (0, 1)]

prob = {}
for e1, e2 in states:
    prob[(e1, e2)] = (p if e1 else 1 - p) * (p if e2 else 1 - p)


def cluster(e1, e2):
    if not e1:
        return ("b",)
    if not e2:
        return ("b", "x")
    return ("b", "x", "y")


def f(e1, e2):
    return Fraction(e2, 1)


mass = defaultdict(Fraction)
weighted = defaultdict(Fraction)
for state, weight in prob.items():
    K = cluster(*state)
    mass[K] += weight
    weighted[K] += weight * f(*state)

cond = {K: weighted[K] / mass[K] for K in mass}

assert sum(prob.values(), Fraction()) == 1
assert mass[("b",)] == Fraction(1, 4)
assert weighted[("b",)] == Fraction(3, 16)
assert cond[("b",)] == Fraction(3, 4)
assert mass[("b", "x")] == Fraction(3, 16)
assert weighted[("b", "x")] == 0
assert cond[("b", "x")] == 0
assert set(("b",)).issubset(set(("b", "x")))
assert cond[("b",)] > cond[("b", "x")]
assert cond[("b", "x", "y")] == 1

print("p =", p)
for K in [("b",), ("b", "x"), ("b", "x", "y")]:
    print(f"C={K}: mass={mass[K]}, f-weight={weighted[K]}, E[f|C]={cond[K]}")
print("monotonicity witness: {b} subset {b,x}, but 3/4 > 0")
print("EXACT_COUNTEREXAMPLE_PASS")

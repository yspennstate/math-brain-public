from fractions import Fraction
from itertools import combinations

# Exact finite self-check for the B11 stress test in I0122.
# P = C2 + C3 (disjoint union), with chains
# A: a0 < a1 and B: b0 < b1 < b2.
# Every linear extension is an interleaving of A and B, so there are C(5,2)=10.

A = ("a0", "a1")
B = ("b0", "b1", "b2")

extensions = []
for apos in combinations(range(5), 2):
    apos = set(apos)
    ia = ib = 0
    word = []
    for r in range(5):
        if r in apos:
            word.append(A[ia])
            ia += 1
        else:
            word.append(B[ib])
            ib += 1
    extensions.append(tuple(word))

assert len(extensions) == 10
assert len(set(extensions)) == 10

verts = A + B
means = {}
for v in verts:
    means[v] = sum(Fraction(e.index(v) + 1, 1) for e in extensions) / len(extensions)

assert means == {
    "a0": Fraction(2, 1),
    "a1": Fraction(4, 1),
    "b0": Fraction(3, 2),
    "b1": Fraction(3, 1),
    "b2": Fraction(9, 2),
}


def prob_before(x, y):
    return Fraction(sum(e.index(x) < e.index(y) for e in extensions), len(extensions))


# False-lemma witness: an incomparable pair whose expected-rank gap is exactly 1
# need not itself be 1/3-balanced.
p = prob_before("a0", "b1")
q = 1 - p
assert abs(means["a0"] - means["b1"]) == 1
assert p == Fraction(7, 10)
assert q == Fraction(3, 10)
assert min(p, q) == Fraction(3, 10) < Fraction(1, 3)

# This is NOT a counterexample to the 1/3-2/3 conjecture: compute delta(P) exactly.
incomparable = [(a, b) for a in A for b in B]
balances = {}
for x, y in incomparable:
    r = prob_before(x, y)
    balances[(x, y)] = min(r, 1 - r)

delta = max(balances.values())
assert delta == Fraction(2, 5) >= Fraction(1, 3)

print("poset=C2_disjoint_union_C3")
print("linear_extensions=", len(extensions))
print("means=", ",".join(f"{v}:{means[v]}" for v in verts))
print("witness_pair=a0,b1")
print("P(a0<b1)=", p)
print("P(b1<a0)=", q)
print("mean_rank_gap=", abs(means["a0"] - means["b1"]))
print("witness_balance=", min(p, q))
print("delta(P)=", delta)
print("pair_balances=", ",".join(f"{x},{y}:{balances[(x, y)]}" for x, y in incomparable))
print("ALL_EXACT_CHECKS_PASS")

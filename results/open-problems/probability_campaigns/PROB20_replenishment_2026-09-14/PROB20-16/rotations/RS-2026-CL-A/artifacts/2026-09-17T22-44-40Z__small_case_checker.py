from fractions import Fraction
from itertools import product, combinations

states = list(product([0, 1], repeat=3))


def compositions(n, k, prefix=()):
    if k == 1:
        yield prefix + (n,)
        return
    for x in range(n + 1):
        yield from compositions(n - x, k - 1, prefix + (x,))


def cylinder(probs, S):
    return sum(
        probs[i]
        for i, x in enumerate(states)
        if all(x[j] == 1 for j in S)
    )


# Exact denominator-4 enumeration of unbiased pairwise-independent laws on {0,1}^3.
laws = []
for counts in compositions(4, 8):
    probs = tuple(Fraction(c, 4) for c in counts)
    if any(cylinder(probs, (i,)) != Fraction(1, 2) for i in range(3)):
        continue
    if any(
        cylinder(probs, (i, j)) != Fraction(1, 4)
        for i, j in combinations(range(3), 2)
    ):
        continue
    laws.append((counts, cylinder(probs, (0, 1, 2))))

assert len(laws) == 2
assert sorted(t for _, t in laws) == [Fraction(0), Fraction(1, 4)]

# Lexicographic state order: 000,001,010,011,100,101,110,111.
odd_counts = (0, 1, 1, 0, 1, 0, 0, 1)
assert any(counts == odd_counts for counts, _ in laws)
odd = tuple(Fraction(c, 4) for c in odd_counts)

q = [cylinder(odd, (i,)) for i in range(3)]
a123 = cylinder(odd, (0, 1, 2))
gamma3 = a123 / (q[0] * q[1] * q[2])
assert gamma3 == 2

# Forced-support channel with product null Bernoulli(1/2)^3, so lambda=1.
b = {}
for j in range(1, 4):
    b[j] = sum(cylinder(odd, S) ** 2 for S in combinations(range(3), j))

assert b[1] == Fraction(3, 4)
assert b[2] == Fraction(3, 16)
assert b[3] == Fraction(1, 16)
chi2 = sum(b.values())
assert chi2 == 1

# Marginal-matched independent support has q_i=1/2, hence
# 1+chi^2 = product_i (1+q_i^2) for lambda=1.
matched_independent_chi2 = (Fraction(5, 4) ** 3) - 1
assert matched_independent_chi2 == Fraction(61, 64)
excess = chi2 - matched_independent_chi2
assert excess == Fraction(3, 64)

print("EXACT_SMALL_CASE_PASS")
print("denominator_4_unbiased_pairwise_independent_laws =", len(laws))
print("possible_triple_cylinders =", ",".join(str(x) for x in sorted(t for _, t in laws)))
print("odd_parity_gamma3 =", gamma3)
print("odd_parity_b1 =", b[1])
print("odd_parity_b2 =", b[2])
print("odd_parity_b3 =", b[3])
print("odd_parity_chi2 =", chi2)
print("matched_independent_chi2 =", matched_independent_chi2)
print("chi2_excess =", excess)

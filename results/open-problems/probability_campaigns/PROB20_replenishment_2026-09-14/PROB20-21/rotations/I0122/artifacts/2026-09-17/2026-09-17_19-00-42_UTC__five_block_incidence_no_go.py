from fractions import Fraction

# Exact abstract incidence model for the k=5 (m=4 boundary) obstruction.
# This does NOT claim realization by a poset. It proves that the boundary-cover
# identities plus the mandatory singleton/nonadjacent-double swap witnesses,
# by themselves, do not force any boundary reverse event to have mass >= 1/3.

m = 4
N = 3
patterns = [frozenset()]  # canonical extension L_*
for i in range(1, m + 1):
    patterns.extend([frozenset({i})] * N)
patterns.extend([
    frozenset({1, 3}),
    frozenset({1, 4}),
    frozenset({2, 4}),
])

e = len(patterns)
assert e == 16
assert sum(1 for S in patterns if S) == e - 1

# Mandatory witnesses supplied by adjacent swaps and commuting nonadjacent swaps.
for i in range(1, m + 1):
    assert frozenset({i}) in patterns
for S in (frozenset({1, 3}), frozenset({1, 4}), frozenset({2, 4})):
    assert S in patterns

marginals = []
for i in range(1, m + 1):
    count = sum(1 for S in patterns if i in S)
    marginals.append(count)
    assert Fraction(count, e) < Fraction(1, 3)

assert marginals == [5, 4, 4, 5]

print('I0122_FIVE_BLOCK_INCIDENCE_NO_GO_PASS')
print(f'e={e}')
print('marginal_counts=' + repr(marginals))
print('marginal_probabilities=' + repr([str(Fraction(c, e)) for c in marginals]))
print('required_singletons=present')
print('required_nonadjacent_double_swaps=present')
print('interpretation=abstract incidence constraints alone cannot force a 1/3 boundary')

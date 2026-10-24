"""Exact two-spin check of the weighted-current cumulant identity."""
from fractions import Fraction

t = Fraction(1, 3)
weights = {}
for s0 in (-1, 1):
    for s1 in (-1, 1):
        weights[(s0, s1)] = (1 + t * s0 * s1) / 4
assert sum(weights.values()) == 1
variance = sum(prob * (s0 + s1) ** 2 for (s0, s1), prob in weights.items())
fourth = sum(prob * (s0 + s1) ** 4 for (s0, s1), prob in weights.items())
deficit = (3 * variance**2 - fourth) / variance**2
diag_pair_weight = 1 / variance
event_probability = (
    2 * diag_pair_weight**2  # both diagonal pairs at one site
    + 2 * diag_pair_weight**2 * t**2  # diagonal pairs at opposite sites
    + 1 - (2 * diag_pair_weight) ** 2  # at least one off-diagonal pair
)
assert variance == Fraction(8, 3)
assert fourth == Fraction(32, 3)
assert deficit == 2 * event_probability == Fraction(3, 2)
print(f"V={variance}; E[S^4]={fourth}; deficit={deficit}; P(A)={event_probability}")

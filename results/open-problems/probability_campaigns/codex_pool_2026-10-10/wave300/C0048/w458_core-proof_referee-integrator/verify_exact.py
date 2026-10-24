"""Independent exact-arithmetic checks of the two C0048 peer packets."""
from fractions import Fraction as Q
from itertools import product

q = 3
weights = {}
for s, t in product(range(q), repeat=2):
    x = Q((s == 0) + (t == 0), 1) - Q(2, q)
    weights[x] = weights.get(x, Q(0)) + (2 if s == t else 1)
z = sum(weights.values())
moments = [sum(w * x**k for x, w in weights.items()) / z for k in range(1, 5)]
k2, k3, k4 = moments[1], moments[2], moments[3] - 3 * moments[1] ** 2

# One-edge FK graph at p=1/2, q=3: opening probability 1/4.
open_prob = Q(1, 4)
es2 = 2 * (1 - open_prob) + 4 * open_prob
es3 = 2 * (1 - open_prob) + 8 * open_prob
es4 = 2 * (1 - open_prob) + 16 * open_prob
var_s2 = (1 - open_prob) * (2 - es2) ** 2 + open_prob * (4 - es2) ** 2
a2, a3, a4 = Q(2, 9), Q(2, 27), Q(-2, 27)
rhs = (a2 * es2, a3 * es3, a4 * es4 + 3 * a2**2 * var_s2)
lhs = (k2, k3, k4)
assert lhs == rhs, (lhs, rhs)

# Four-cycle FK at p=1/2, q=3; total weight by edge count.
from math import comb
z4 = sum(comb(4, n) * 3 ** (4 - n) for n in range(4)) + 3
one_edge_numer = sum(comb(3, n - 1) * 3 ** (4 - n) for n in range(1, 4)) + 3
marginal = Q(one_edge_numer, z4)
all_open = Q(3, z4)
assert (z4, marginal, all_open) == (258, Q(11, 43), Q(1, 86))
assert all_open > marginal**4

print(f"two_vertex_cumulants={lhs}; FK_rhs={rhs}; matches={lhs == rhs}")
print(f"four_cycle_Z={z4}; one_edge={marginal}; all_four={all_open}; joint_over_product={float(all_open / marginal**4):.8f}")

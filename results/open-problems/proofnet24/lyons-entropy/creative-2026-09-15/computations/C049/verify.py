#!/usr/bin/env python3
"""Exact certificates for C049. No floating-point assertion is used."""

from pathlib import Path
import json

import sympy as s


HERE = Path(__file__).resolve().parent
t = s.symbols("t", real=True)
a, b = s.symbols("a b", positive=True)
K = s.Matrix([[a, t], [t, b]])


def atoms(matrix):
    n = matrix.rows
    eye = s.eye(n)
    out = []
    # Order: empty, first coordinate, second coordinate, both coordinates.
    for mask in range(1 << n):
        cols = [matrix[:, j] if (mask >> j) & 1 else eye[:, j] - matrix[:, j]
                for j in range(n)]
        out.append(s.factor(s.Matrix.hstack(*cols).det()))
    return out


p = atoms(K)
expected = [(1-a)*(1-b)-t*t, a*(1-b)+t*t,
            (1-a)*b+t*t, a*b-t*t]
assert all(s.expand(x-y) == 0 for x, y in zip(p, expected))
mu = [s.factor(x.subs(t, 0)) for x in p]
g = [s.diff(x, t).subs(t, 0) for x in p]
h = [s.diff(x, t, 2).subs(t, 0) for x in p]
assert sum(p).expand() == 1
assert g == [0, 0, 0, 0]
assert h == [-2, 2, 2, -2]
assert s.simplify(sum(1 / x for x in mu) - 1 / (a*(1-a)*b*(1-b))) == 0


def hessian_from_jets(probabilities, alpha):
    z = sum(x ** alpha for x in probabilities)
    # All first atom derivatives vanish at t=0 in these certificates.
    return s.simplify(alpha * sum(x ** (alpha-1) * y
                                 for x, y in zip(probabilities, h))
                      / ((1-alpha)*z))


plus_sub = {a: s.Rational(1, 4), b: s.Rational(1, 4)}
minus_sub = {a: s.Rational(1, 4), b: s.Rational(3, 4)}
plus_mu = [x.subs(plus_sub) for x in mu]
minus_mu = [x.subs(minus_sub) for x in mu]
assert plus_mu == [s.Rational(9, 16), s.Rational(3, 16),
                   s.Rational(3, 16), s.Rational(1, 16)]
assert minus_mu == [s.Rational(3, 16), s.Rational(1, 16),
                    s.Rational(9, 16), s.Rational(3, 16)]

h2 = hessian_from_jets(plus_mu, s.Integer(2))
h32 = hessian_from_jets(plus_mu, s.Rational(3, 2))
h12 = hessian_from_jets(minus_mu, s.Rational(1, 2))
assert h2 == s.Rational(64, 25)
assert s.simplify(h32 - s.Rational(96, 169)*(37-20*s.sqrt(3))) == 0
assert s.simplify(h12 - s.Rational(32, 3)*(7-4*s.sqrt(3))) == 0
# Radical signs are certified by positive rational power comparisons.
assert s.Rational(7, 4)**2 > 3
assert s.Rational(37, 20)**2 > 3
assert s.Rational(2, 1)**2 > 3

# A finite, exact order-2 midpoint failure at t=+/-1/8.
plus_end = [x.subs(plus_sub).subs(t, s.Rational(1, 8)) for x in p]
assert plus_end == [s.Rational(35, 64), s.Rational(13, 64),
                    s.Rational(13, 64), s.Rational(3, 64)]
collision_zero = sum(x*x for x in plus_mu)
collision_end = sum(x*x for x in plus_end)
assert collision_zero == s.Rational(25, 64)
assert collision_end == s.Rational(393, 1024)
assert collision_end < collision_zero

# Physicality of both displayed whole intervals follows exactly from
# positive principal minors of K and I-K at t=+/-1/8 and their minima.
for subs in [plus_sub, minus_sub]:
    matrix = K.subs(subs)
    for endpoint in [s.Rational(-1, 8), s.Rational(1, 8)]:
        for candidate in [matrix.subs(t, endpoint),
                          (s.eye(2)-matrix).subs(t, endpoint)]:
            assert candidate[0, 0] > 0
            assert candidate.det() > 0

# Shannon quartic term, obtained by differentiating the exact atom entropy.
entropy = -sum(x*s.log(x) for x in p)
shannon_fourth_plus = s.simplify(s.diff(entropy.subs(plus_sub), t, 4).subs(t, 0))
shannon_fourth_minus = s.simplify(s.diff(entropy.subs(minus_sub), t, 4).subs(t, 0))
assert shannon_fourth_plus == -s.Rational(1024, 3)
assert shannon_fourth_minus == -s.Rational(1024, 3)

# Exact near-one coefficient and the leading positive shrinking-midpoint gap.
eps = s.symbols("eps", real=True)
upper_order_curvature = (32*(1+eps)*(3**eps-1)**2
                         / (eps*(1+3**(1+eps))**2))
near_one_coefficient = s.limit(upper_order_curvature/eps, eps, 0)
assert near_one_coefficient == 2*s.log(3)**2
shrinking_step_square = s.Rational(9, 256)*s.log(3)**2
shrinking_gap_coefficient = s.simplify(
    shrinking_step_square*s.log(3)**2
    - s.Rational(128, 9)*shrinking_step_square**2)
assert shrinking_gap_coefficient == s.Rational(9, 512)*s.log(3)**4

# The frozen-product scaled power divergence at alpha=2 is exactly quartic.
power2 = s.factor(sum((x-y)**2/y for x, y in zip(p, mu))/2)
assert s.simplify(power2 - t**4/(2*a*(1-a)*b*(1-b))) == 0
assert s.simplify(power2.subs(plus_sub) - s.Rational(128, 9)*t**4) == 0

# Quantum and measured order-2 curvatures have opposite signs here.
x = s.symbols("x", real=True)
binary_h2 = -s.log(x*x+(1-x)**2)
quantum_h2_curvature = s.diff(binary_h2, x, 2).subs(x, s.Rational(1, 4))*2
assert quantum_h2_curvature == -s.Rational(192, 25)

# The elementary Hessian underlying the entire positive alpha in [1,2]
# family. Its determinant and leading diagonal are nonnegative for 0<=q<=1.
z = s.symbols("z", real=True)
w = s.symbols("w", positive=True)
q = s.symbols("q", real=True)
perspective = z*z*w**(-q)
perspective_hessian = s.hessian(perspective, (z, w))
perspective_det = s.factor(perspective_hessian.det())
assert s.simplify(perspective_hessian[0, 0] - 2*w**(-q)) == 0
assert s.simplify(perspective_det - 2*q*(1-q)*z*z*w**(-2*q-2)) == 0

# Exact numerical-data instance of the coordinate-replacement intertwining:
# endpoint [[1/4,1/8],[1/8,1/4]], D=(1/4)I, rational retention 3/5.
eta = s.Rational(3, 5)
endpoint_p = plus_end
reference = [s.Rational(3, 4), s.Rational(1, 4)]
channel_p = []
for y_mask in range(4):
    total = 0
    for x_mask in range(4):
        transition = 1
        for j in range(2):
            y_bit = (y_mask >> j) & 1
            x_bit = (x_mask >> j) & 1
            transition *= eta*int(y_bit == x_bit)+(1-eta)*reference[y_bit]
        total += endpoint_p[x_mask]*transition
    channel_p.append(total)
kernel_p = [x.subs(plus_sub).subs(t, eta/8) for x in p]
assert channel_p == kernel_p

# Direct sum with any independent Bernoulli factors preserves the measured
# obstruction by exact factorization of the power sum. This verifies one
# nontrivial rational three-site instance without relying on floating data.
d = s.Rational(2, 5)
three_K = s.diag(K.subs(plus_sub), d)
three_p = atoms(three_K)
assert s.simplify(sum(x*x for x in three_p)
                  - (d*d+(1-d)**2)*sum(x.subs(plus_sub)**2 for x in p)) == 0

results = {
    "status": "all exact assertions passed",
    "generic_atoms_empty_1_2_12": [str(x) for x in p],
    "generic_first_jets": list(map(str, g)),
    "generic_second_jets": list(map(str, h)),
    "upper_order_witness_atoms_at_zero": list(map(str, plus_mu)),
    "lower_order_witness_atoms_at_zero": list(map(str, minus_mu)),
    "ordinary_renyi_curvature": {
        "alpha_2_upper_witness": str(h2),
        "alpha_3_over_2_upper_witness": str(s.radsimp(h32)),
        "alpha_1_over_2_lower_witness": str(s.radsimp(h12)),
    },
    "alpha_2_midpoint_failure": {
        "endpoint_t": "1/8",
        "endpoint_atoms": list(map(str, plus_end)),
        "power_sum_at_midpoint": str(collision_zero),
        "power_sum_at_endpoints": str(collision_end),
        "positive_entropy_gain_at_both_endpoints": "log(400/393)",
    },
    "shannon_fourth_derivative_both_witnesses": str(shannon_fourth_plus),
    "near_one_upper_curvature": str(upper_order_curvature),
    "near_one_upper_curvature_divided_by_alpha_minus_one_limit": str(near_one_coefficient),
    "shrinking_midpoint_step_t": "(3*log(3)/16)*sqrt(abs(alpha-1))",
    "shrinking_midpoint_positive_gain_leading_coefficient": str(shrinking_gap_coefficient),
    "corrected_alpha_2_entropy_both_witnesses": "H(P_D) - (128/9)*t^4",
    "quantum_alpha_2_curvature_upper_witness": str(quantum_h2_curvature),
    "joint_convexity_hessian": str(perspective_hessian),
    "joint_convexity_hessian_determinant": str(perspective_det),
    "retention_3_over_5_atom_identity": list(map(str, channel_p)),
}
out = HERE / "results.json"
out.write_text(json.dumps(results, indent=2) + "\n")
print(json.dumps(results, indent=2))

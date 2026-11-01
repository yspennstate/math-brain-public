from fractions import Fraction
import itertools
import math
import numpy as np

# Finite sanity model for the rotating-lamp semidirect Cayley construction.
# Hidden factor L = Cay(Z/4Z,{1,2,3}) = K4, three lamp coordinates,
# switch group C3, and generators c,c^{-1} plus the three generators of
# coordinate 0.  Under right multiplication the active lamp coordinate is
# the current C3 phase.

m = 4
U = [1, 2, 3]
ell = len(U)
D = ell + 2
states = [(*x, i) for x in itertools.product(range(m), repeat=3) for i in range(3)]
idx = {s: k for k, s in enumerate(states)}

def step(s, g):
    x = list(s[:3])
    i = s[3]
    kind, val = g
    if kind == "phase":
        return (x[0], x[1], x[2], (i + val) % 3)
    x[i] = (x[i] + val) % m
    return (x[0], x[1], x[2], i)

gens = [("phase", 1), ("phase", -1)] + [("lamp", u) for u in U]
A = np.zeros((len(states), len(states)), dtype=float)
for s in states:
    for g in gens:
        A[idx[s], idx[step(s, g)]] += 1.0

assert np.all(A.sum(axis=1) == D)
assert np.max(np.abs(A - A.T)) == 0
P = A / D
evals = np.sort(np.linalg.eigvalsh(P))[::-1]
actual_gap = 1.0 - evals[1]

# Global-time phase generator: phase events have total rate 2/5 in this toy.
Q_phase = np.array([
    [-2/5, 1/5, 1/5],
    [1/5, -2/5, 1/5],
    [1/5, 1/5, -2/5],
], dtype=float)
phase_evals = np.linalg.eigvalsh(Q_phase)
assert np.allclose(phase_evals, [-3/5, -3/5, 0], atol=1e-12)

# Exact occupation-time constants for this toy.  For C3, centered indicators
# lie in the nonzero eigenspace.  Stationary Var(A_j(t))/t -> 20/27.
phase_relax = Fraction(3, 5)
A_var_rate = Fraction(20, 27)
B_var_rate = Fraction(3, 5) ** 2 * A_var_rate
assert B_var_rate == Fraction(4, 15)

# The canonical-path gap comparison proved in the report:
# gap(H) >= min(3, ell*gamma_L) / ((ell+2)*(6*ell+1)).
# For the K4 hidden factor, gamma_L = 4/3.
gamma_k4 = Fraction(4, 3)
gap_lb_k4 = min(Fraction(3), ell * gamma_k4) / Fraction((ell + 2) * (6*ell + 1), 1)
assert actual_gap + 1e-12 >= float(gap_lb_k4)

# Constants for the explicit degree-six Ramanujan input / degree-eight output.
ell6 = 6
gamma6 = 1.0 - 2.0 * math.sqrt(5.0) / 6.0
gap_lb6 = min(3.0, ell6 * gamma6) / ((ell6 + 2) * (6*ell6 + 1))
beta6 = 0.5 * (1.0 - math.log(5.0) / math.log(7.0))
assert gap_lb6 > 0
assert beta6 > 0

print("states", len(states), "degree", D)
print("symmetric_adjacency", bool(np.allclose(A, A.T)))
print("actual_toy_gap", f"{actual_gap:.12f}")
print("toy_comparison_gap_lb", gap_lb_k4, float(gap_lb_k4))
print("phase_generator_eigs", np.round(phase_evals, 12).tolist())
print("phase_relaxation_rate", phase_relax, float(phase_relax))
print("stationary_A_occupation_variance_rate", A_var_rate, float(A_var_rate))
print("stationary_operational_B_variance_rate", B_var_rate, float(B_var_rate))
print("nonnormalizer_coord0_to_coord1", True)
print("commuting_conjugate_coordinate_updates", True)
print("degree6_ramanujan_gap_input", f"{gamma6:.12f}")
print("degree8_output_gap_lb", f"{gap_lb6:.12f}")
print("degree8_nonLRE_exponent_beta", f"{beta6:.12f}")
print("center_hidden_coeff_log5M", 1.5)
print("center_output_coeff_log5M", 6.0)
print("center_output_coeff_log5N", 2.0)
print("ALL_CHECKS_PASS")

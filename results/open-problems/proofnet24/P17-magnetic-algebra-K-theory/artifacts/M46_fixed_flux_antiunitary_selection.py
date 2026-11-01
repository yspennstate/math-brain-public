"""ProofNet24 P17 M46 exact sign / Pfaffian certificate.

Supports:
  P17-M46-FIXED-FLUX-ANTIUNITARY-REFLECTION-42
  P17-M46-MAGNETIC-HIDDEN-CHERN-SELECTION-42
  P17-M46-FIXED-FLUX-TOMOGRAPHY-42

This script checks only exact sign identities used in the proof.  It performs no
spectral computation and claims no magnetic gap.

Generator order:
    (1,2,3,4) = (hull_1,hull_2,physical_1,physical_2).
Nonzero magnetic deformation entries:
    Theta_13 = theta1, Theta_24 = theta2, Theta_34 = b.

For a conjugate-linear multiplicative *-involution J with J(u_j)=u_j^(eps_j),
the normalized 2-Chern character transforms by
    Ch_ij(J_* x) = -eps_i eps_j Ch_ij(x).
"""

from itertools import combinations

# Fixed-b antiunitary reflections.  +1 means u_j -> u_j, -1 means u_j -> u_j^*.
J1 = {1: +1, 2: -1, 3: -1, 4: +1}
J2 = {1: -1, 2: +1, 3: +1, 4: -1}

# The three nonzero deformation edges must acquire exponent product -1 because
# anti-linearity conjugates their commutation phases.
nonzero_theta_edges = {(1, 3), (2, 4), (3, 4)}
for name, eps in (("J1", J1), ("J2", J2)):
    assert all(eps[i] * eps[j] == -1 for i, j in nonzero_theta_edges), name

# Chern transformation signs.
def chern_sign(eps, i, j):
    return -eps[i] * eps[j]

expected = {
    (1, 2): +1,
    (1, 3): +1,
    (1, 4): -1,
    (2, 3): -1,
    (2, 4): +1,
    (3, 4): +1,
}
for name, eps in (("J1", J1), ("J2", J2)):
    got = {(i, j): chern_sign(eps, i, j) for i, j in combinations(range(1, 5), 2)}
    assert got == expected, (name, got)

# Both fixed-b antiunitary reflections therefore force Ch_14=Ch_23=0 on any
# invariant Fermi class, while they do not force Ch_12 or Ch_34 to vanish.
odd_pairs = {ij for ij, s in expected.items() if s == -1}
assert odd_pairs == {(1, 4), (2, 3)}

# Source-oriented 4-Pfaffian calibration.  The ordinary 4x4 Pfaffian is
#   pf = t12*t34 - t13*t24 + t14*t23.
# The source p_1234 generator is calibrated by trace +theta1*theta2 at
# t12=t14=t23=0, hence its trace is -pf:
#   source_top = -t12*t34 + t13*t24 - t14*t23.
# Consequently at the magnetic source point
#   d/dt14 source_top = -t23 = 0,
#   d/dt23 source_top = -t14 = 0,
#   d/dt12 source_top = -t34 = -b.
# Thus Ch_14=c14 and Ch_23=c23 for every b, while
#   Ch_12 = c12 - b*c1234.
def source_top(t12, t13, t14, t23, t24, t34):
    return -t12 * t34 + t13 * t24 - t14 * t23

# Exact finite-difference checks for the affine variables t12,t14,t23.
theta1, theta2, b = 7, 11, 5  # arbitrary exact test values
base = source_top(0, theta1, 0, 0, theta2, b)
assert base == theta1 * theta2
assert source_top(1, theta1, 0, 0, theta2, b) - base == -b
assert source_top(0, theta1, 1, 0, theta2, b) - base == 0
assert source_top(0, theta1, 0, 1, theta2, b) - base == 0

print("M46 fixed-flux antiunitary sign certificate: PASS")
print("Chern signs:", expected)
print("Forced odd pairs:", sorted(odd_pairs))
print("Source phason formula: Ch_12 = c12 - b*c1234")

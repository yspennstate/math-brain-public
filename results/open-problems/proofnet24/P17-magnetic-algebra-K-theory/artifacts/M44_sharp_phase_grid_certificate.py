"""ProofNet24 P17 M44 exact/high-precision phase-grid certificate.

Supports:
  P17-M44-SHARP-HULL-PHASE-LIPSCHITZ-40
  P17-M44-ANISOTROPIC-REFLECTION-GRID-40

This script does NOT diagonalize Bloch matrices and does NOT claim a magnetic gap.
It evaluates the proved analytic phase-modulus constants for the historical
Example-4.3.3 rational magnetic target
    theta1=97/153, theta2=87/148, b=1/153, r=0.4,
and searches finite anisotropic phase grids by the exact reflection-orbit count.

For each phase circle we permit either the standard uniform grid (offset 0) or the
half-step uniform grid (offset pi/M). Both are invariant under phase inversion.  The
half-step choice removes inversion-fixed nodes when M is even and can reduce the
number of reflection-orbit representatives without changing the covering radius.
"""

from itertools import product
from math import gcd, prod
import mpmath as mp

mp.mp.dps = 80

r = mp.mpf("0.4")
Q1 = 153
Q2 = 148
P1 = 153
P2 = 148
theta1 = mp.mpf(97) / Q1
theta2 = mp.mpf(87) / Q2


def sharp_hull_data(theta, Q):
    """Return s,a,y*,m(a),A,c_h for the sharp residual-hull derivative bound.

    t(alpha)=exp[-1-a cos(x(alpha))], a=2 r sin(pi theta).
    The exact global maximum of |sin x| exp(-a cos x) occurs at
      y*=cos x=(1-sqrt(1+4a^2))/(2a).
    A self-adjoint weighted direction contributes the factor 2.
    """
    s = mp.sin(mp.pi * theta)
    a = 2 * r * s
    y = (1 - mp.sqrt(1 + 4 * a * a)) / (2 * a)
    m = mp.sqrt(1 - y * y) * mp.e ** (-a * y)
    A = mp.e ** (-1 + a)
    c_h = 2 * (a / Q) * mp.e ** (-1) * m
    return s, a, y, m, A, c_h


s1, a1, y1, m1, A1, c_alpha1 = sharp_hull_data(theta1, Q1)
s2, a2, y2, m2, A2, c_alpha2 = sharp_hull_data(theta2, Q2)

# Linearized Bloch coefficients from the doubled-cell distributed gauge.
c_tilde_beta1 = A1 / P1
c_beta2 = 2 * A2 / P2


def epsilon_exact(M):
    """Analytic covering budget for M=(M_a1,M_a2,M_tb1,M_b2).

    Hull terms use the sharp global Lipschitz constants. Bloch terms retain the
    exact sine modulus after uniformly distributing the Bloch phase over a cell.
    Standard and half-step uniform grids have the same covering radii pi/M_i.
    """
    M1, M2, M3, M4 = map(mp.mpf, M)
    return (
        mp.pi * c_alpha1 / M1
        + mp.pi * c_alpha2 / M2
        + 4 * A1 * mp.sin(mp.pi / (4 * P1 * M3))
        + 4 * A2 * mp.sin(mp.pi / (2 * P2 * M4))
    )


def inversion_fixed_count(M, half_shift=False):
    """Fixed nodes for x -> -x on an M-point inversion-invariant uniform grid.

    standard grid: x_k=2*pi*k/M, fixed count gcd(2,M);
    half-step grid: x_k=2*pi*(k+1/2)/M, fixed count 0 for even M, 1 for odd M.
    """
    if not half_shift:
        return gcd(2, M)
    return 0 if M % 2 == 0 else 1


def reflection_orbits(M, half_shifts=(False, False, False, False)):
    """Burnside orbit count for the retained doubled-family reflections.

    R1 flips (alpha1,beta2); R2 flips (alpha2,tilde_beta1).  half_shifts selects
    standard/half-step grids independently in the four coordinates.
    """
    M1, M2, M3, M4 = M
    f1, f2, f3, f4 = [
        inversion_fixed_count(M[i], half_shifts[i]) for i in range(4)
    ]
    total = (
        M1 * M2 * M3 * M4
        + f1 * f4 * M2 * M3
        + f2 * f3 * M1 * M4
        + f1 * f2 * f3 * f4
    )
    assert total % 4 == 0
    return total // 4


def best_grid(eps, max_M=16):
    """Exhaustively minimize orbit representatives for 1<=M_i<=max_M.

    Ties are broken by raw grid size and then by actual covering budget.  All 16
    standard/half-step offset choices are checked for every anisotropic size tuple.
    This is a bounded finite optimization certificate, not a global optimum over all
    possible grids or all M_i.
    """
    eps = mp.mpf(str(eps))
    best = None
    for M in product(range(1, max_M + 1), repeat=4):
        e = epsilon_exact(M)
        if e <= eps:
            for half_shifts in product((False, True), repeat=4):
                key = (
                    reflection_orbits(M, half_shifts),
                    prod(M),
                    e,
                    M,
                    half_shifts,
                )
                if best is None or key < best:
                    best = key
    return best


if __name__ == "__main__":
    print("theta1", mp.nstr(theta1, 50))
    print("theta2", mp.nstr(theta2, 50))
    print("s1", mp.nstr(s1, 50))
    print("s2", mp.nstr(s2, 50))
    print("a1", mp.nstr(a1, 50))
    print("a2", mp.nstr(a2, 50))
    print("y1", mp.nstr(y1, 50))
    print("y2", mp.nstr(y2, 50))
    print("m1", mp.nstr(m1, 50))
    print("m2", mp.nstr(m2, 50))
    print("A1", mp.nstr(A1, 50))
    print("A2", mp.nstr(A2, 50))
    print("c_alpha1", mp.nstr(c_alpha1, 50))
    print("c_alpha2", mp.nstr(c_alpha2, 50))
    print("c_tilde_beta1", mp.nstr(c_tilde_beta1, 50))
    print("c_beta2", mp.nstr(c_beta2, 50))
    equal_linear = mp.pi * (c_alpha1 + c_alpha2 + c_tilde_beta1 + c_beta2)
    print("equal_grid_linear_constant", mp.nstr(equal_linear, 50))

    examples = [(2, 3, 3, 5), (3, 3, 3, 7), (3, 3, 5, 11), (5, 5, 5, 12)]
    for M in examples:
        print("standard-grid", M, "raw", prod(M),
              "orbits", reflection_orbits(M),
              "epsilon", mp.nstr(epsilon_exact(M), 40))

    for eps in ("0.025", "0.022", "0.020", "0.018", "0.016", "0.014", "0.012", "0.010"):
        ans = best_grid(eps)
        print("target", eps, "best", ans[3], "half_shifts", ans[4],
              "orbits", ans[0], "raw", ans[1],
              "epsilon", mp.nstr(ans[2], 40))

"""Exact rational self-check for R09 / G0013 half-rotation shuffle.

This checker verifies only the scalar integrals used in the analytic proof that
for the half-rotation shuffle g(s)=s+1/2 mod 1,

    W_2^2(Law(S,g(S)), Unif([0,1]^2)) = 1/20.

The optimality argument itself is theorem-sized and belongs in the run report:
in (Z,D)=(X+Y,Y-X) coordinates, the target has independent marginals
Z'~Unif[1/2,3/2] and D' uniform on {-1/2,+1/2}; the displayed coupling
simultaneously realizes the one-dimensional monotone W_2 couplings.

No floating point arithmetic is used here.
"""
from fractions import Fraction as Q


def pmul(p, q):
    out = [Q(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] += a * b
    return out


def padd(p, q):
    n = max(len(p), len(q))
    return [
        (p[i] if i < len(p) else Q(0)) +
        (q[i] if i < len(q) else Q(0))
        for i in range(n)
    ]


def pint(p, a, b):
    return sum(
        c * (b ** (i + 1) - a ** (i + 1)) / Q(i + 1)
        for i, c in enumerate(p)
    )


# Rotated-coordinate cost is
#   (1/2) E[(Z-Z')^2] + (1/2) E[(D-D')^2].
# For D on [-1,1] with density 1-|d| and optimal D'=sgn(D)/2,
# symmetry cancels the factor 1/2:
#   C_D = int_0^1 (d-1/2)^2 (1-d) dd.
d_minus_half = [Q(-1, 2), Q(1)]
C_D = pint(pmul(pmul(d_minus_half, d_minus_half), [Q(1), Q(-1)]), Q(0), Q(1))

# Z=X+Y has triangular density z on [0,1], 2-z on [1,2].
# Its monotone transport to Unif[1/2,3/2] is Z'=1/2+F_Z(Z), with
# F_Z(z)=z^2/2 on [0,1] and -1+2z-z^2/2 on [1,2].
# Include the rotated-coordinate factor 1/2.
err_lo = [Q(-1, 2), Q(1), Q(-1, 2)]      # z - (1/2 + z^2/2)
err_hi = [Q(1, 2), Q(-1), Q(1, 2)]       # z - (1/2 + F_Z(z))
I_lo = pint(pmul(pmul(err_lo, err_lo), [Q(0), Q(1)]), Q(0), Q(1))
I_hi = pint(pmul(pmul(err_hi, err_hi), [Q(2), Q(-1)]), Q(1), Q(2))
C_Z = Q(1, 2) * (I_lo + I_hi)

TOTAL = C_D + C_Z

assert C_D == Q(1, 24), C_D
assert C_Z == Q(1, 120), C_Z
assert TOTAL == Q(1, 20), TOTAL

print(f"D_component={C_D}")
print(f"Z_component={C_Z}")
print(f"total_W2_squared={TOTAL}")
print("PASS")

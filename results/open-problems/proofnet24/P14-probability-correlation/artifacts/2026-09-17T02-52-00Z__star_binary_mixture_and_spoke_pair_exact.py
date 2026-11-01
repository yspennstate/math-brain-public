#!/usr/bin/env python3
"""Exact symbolic checks for the P14 degree-three-apex recovery.

No floating point and no third-party dependencies.

State variables for a forest of H=G-v relative to terminals x,y,z:
  D : x|y|z
  P : xy|z
  Q : xz|y
  S : yz|x
  T : xyz

Checks:
  (1) the unit three-spoke transfer is exactly F(0)+3 F(1/3), where
      F(s) is the transfer obtained by adjoining an equal-weight terminal triangle;
  (2) the Rayleigh numerator for any two apex spokes is a polynomial with
      nonnegative integer coefficients in D,P,Q,S,T.
"""

from fractions import Fraction

NAMES = ("D", "P", "Q", "S", "T")
ZERO = (0, 0, 0, 0, 0)


def add_vec(a, b):
    return tuple(x + y for x, y in zip(a, b))


def scale_vec(c, a):
    return tuple(c * x for x in a)


def F_vec(s):
    """Coefficient vector of F(s) in state order D,P,Q,S,T."""
    s = Fraction(s)
    return (
        1 + 3*s + 3*s*s,
        1 + 2*s,
        1 + 2*s,
        1 + 2*s,
        1,
    )


STAR = (8, 6, 6, 6, 4)
MIX = add_vec(F_vec(0), scale_vec(3, F_vec(Fraction(1, 3))))
assert MIX == tuple(Fraction(x) for x in STAR)


def linear_poly(coeffs):
    out = {}
    for i, c in enumerate(coeffs):
        if c:
            e = [0] * 5
            e[i] = 1
            out[tuple(e)] = Fraction(c)
    return out


def mul(a, b):
    out = {}
    for ea, ca in a.items():
        for eb, cb in b.items():
            e = tuple(x + y for x, y in zip(ea, eb))
            out[e] = out.get(e, Fraction(0)) + ca * cb
    return {e: c for e, c in out.items() if c}


def sub(a, b):
    out = dict(a)
    for e, c in b.items():
        out[e] = out.get(e, Fraction(0)) - c
        if not out[e]:
            del out[e]
    return out


def mon(i, j=None):
    e = [0] * 5
    e[i] += 1
    if j is not None:
        e[j] += 1
    return tuple(e)


# For spokes vx and vy.  In state P=xy|z, the pair vx,vy is forbidden;
# in Q=xz|y and S=yz|x, adding the third spoke is the only extra restriction.
Z   = linear_poly((8, 6, 6, 6, 4))
Zx  = linear_poly((4, 2, 2, 3, 1))
Zy  = linear_poly((4, 2, 3, 2, 1))
Zxy = linear_poly((2, 0, 1, 1, 0))
GAP_XY = sub(mul(Zx, Zy), mul(Z, Zxy))

TARGET_XY = {
    mon(0, 1): Fraction(4),  # 4 D P
    mon(1, 1): Fraction(4),  # 4 P^2
    mon(1, 2): Fraction(4),  # 4 P Q
    mon(1, 3): Fraction(4),  # 4 P S
    mon(1, 4): Fraction(4),  # 4 P T
    mon(2, 3): Fraction(1),  # Q S
    mon(2, 4): Fraction(1),  # Q T
    mon(3, 4): Fraction(1),  # S T
    mon(4, 4): Fraction(1),  # T^2
}
assert GAP_XY == TARGET_XY
assert all(c >= 0 for c in GAP_XY.values())

# Terminal relabellings send any unordered spoke pair to {vx,vy}; nevertheless,
# check the other two pairs directly by permuting the state labels.
# vx,vz is obtained by swapping y<->z, hence P<->Q and S fixed.
# vy,vz is obtained cyclically; direct state counts are written explicitly.
Zz  = linear_poly((4, 3, 2, 2, 1))
Zxz = linear_poly((2, 0, 1, 0, 0))  # D:2; P=xy: third y forbidden? see below
# Correct pair-containing counts by state, computed from the star cycle rule:
# vx,vz: D=2, P=1, Q=0, S=1, T=0
Zxz = linear_poly((2, 1, 0, 1, 0))
# vy,vz: D=2, P=1, Q=1, S=0, T=0
Zyz = linear_poly((2, 1, 1, 0, 0))
GAP_XZ = sub(mul(Zx, Zz), mul(Z, Zxz))
GAP_YZ = sub(mul(Zy, Zz), mul(Z, Zyz))
assert all(c >= 0 for c in GAP_XZ.values())
assert all(c >= 0 for c in GAP_YZ.values())


def fmt_poly(poly):
    terms = []
    for exp, c in sorted(poly.items()):
        factors = []
        for name, p in zip(NAMES, exp):
            if p == 1:
                factors.append(name)
            elif p > 1:
                factors.append(f"{name}^{p}")
        monomial = "*".join(factors) if factors else "1"
        terms.append(f"{c}*{monomial}")
    return " + ".join(terms)


print("STAR_TRANSFER", STAR)
print("F0_PLUS_3_F13", tuple(str(x) for x in MIX))
print("MIXTURE_IDENTITY_OK", MIX == tuple(Fraction(x) for x in STAR))
print("GAP_XY", fmt_poly(GAP_XY))
print("GAP_XZ", fmt_poly(GAP_XZ))
print("GAP_YZ", fmt_poly(GAP_YZ))
print("ALL_SPOKE_PAIR_COEFFICIENTS_NONNEGATIVE", all(
    c >= 0 for poly in (GAP_XY, GAP_XZ, GAP_YZ) for c in poly.values()
))
print("ALL_EXACT_CHECKS_PASSED")

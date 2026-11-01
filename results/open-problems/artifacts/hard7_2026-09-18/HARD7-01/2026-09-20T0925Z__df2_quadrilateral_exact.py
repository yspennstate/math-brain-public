#!/usr/bin/env python3
"""Exact symbolic checker for HARD7-01's planar DF2 quadrilateral theorem.

This is a self-check for the finite/symbolic algebra in the written proof.  It
is not an audit of the source Mahler conjecture and does not move d_sym.
"""

import sympy as sp

r, s, a, b = sp.symbols("r s a b", positive=True)

# Affine normal form B_{r,s}=conv{(1,0),(0,1),(-r,0),(0,-s)}.
# By endpoint swaps and axis interchange, it is enough to use s>=r>=1.
A = (1 + r) * (1 + s) / 2
E = (1 + r) * (1 + 3 * s)
Ep = (3 * r * s**2 + 6 * r * s + r - r**2 - 1) / (
    r * s * (r + 1) * (s + 1) ** 2
)

# Independent shoelace reconstruction of E=B-B in the chamber s>=r>=1.
verts = [
    (-(1 + r), 0),
    (-1, -s),
    (0, -(1 + s)),
    (r, -s),
    (1 + r, 0),
    (1, s),
    (0, 1 + s),
    (-r, s),
]


def signed_area(vs):
    return sp.factor(
        sp.Rational(1, 2)
        * sum(
            vs[i][0] * vs[(i + 1) % len(vs)][1]
            - vs[(i + 1) % len(vs)][0] * vs[i][1]
            for i in range(len(vs))
        )
    )


def polar_vertices(vs):
    out = []
    for i in range(len(vs)):
        x1, y1 = vs[i]
        x2, y2 = vs[(i + 1) % len(vs)]
        det = sp.expand(x1 * y2 - x2 * y1)
        # Intersection of <(X,Y),v_i>=1 and <(X,Y),v_{i+1}>=1.
        out.append(
            (
                sp.factor((y2 - y1) / det),
                sp.factor((x1 - x2) / det),
            )
        )
    return out


E_area_check = sp.factor(signed_area(verts))
pverts = polar_vertices(verts)
Ep_area_check = sp.factor(signed_area(pverts))

# DF2 quantity Q=(|B-B|+2|B|)|(B-B)^o|.
Q = sp.factor((E + 2 * A) * Ep)
Delta = sp.factor(Q - 12)
F = sp.factor(Delta * r * s * (s + 1) ** 2 / 2)

# Put r=1+a and s=r+b.  The chamber becomes a,b>=0.
Fab = sp.expand(F.subs({r: 1 + a, s: 1 + a + b}))

# Standard triangle sanity check for the pyramid dimension drop.
# B=conv{0,e1,e2}: |B|=1/2, |B-B|=3, |(B-B)^o|=3.
Atri = sp.Rational(1, 2)
Etri = sp.Rational(3, 1)
Eptri = sp.Rational(3, 1)
Ltri = Atri / 3
Dtri = Etri + sp.Rational(2, 3) * Atri
Dptri = sp.Rational(4, 3) * Eptri
DF6tri = sp.factor((Dtri + 4 * Ltri) * Dptri)

# For any pyramid, the derived formulas make DF6 exactly (4/3)*DF2.
pyramid_lhs = sp.factor(
    ((E + sp.Rational(2, 3) * A) + 4 * (A / 3))
    * (sp.Rational(4, 3) * Ep)
)
pyramid_scaling_residual = sp.factor(
    pyramid_lhs - sp.Rational(4, 3) * (E + 2 * A) * Ep
)

print("E_AREA_IDENTITY =", sp.simplify(E_area_check - E) == 0)
print("EP_AREA_IDENTITY =", sp.simplify(Ep_area_check - Ep) == 0)
print("QUAD_TARGET =", Q)
print("QUAD_DEFECT =", Delta)
print("DEFECT_NUMERATOR_F =", F)
print("F_SUBSTITUTED =", sp.factor(Fab))
print(
    "F_COEFFICIENTS_NONNEGATIVE =",
    all(c >= 0 for c in sp.Poly(Fab, a, b).coeffs()),
)
print(
    "F_ZERO_ONLY_A_B_ZERO =",
    sp.factor(Fab.subs(b, 0)),
    sp.factor(Fab.subs(a, 0)),
)
print("TRIANGLE_SANITY_D_VOLUME =", Dtri)
print("TRIANGLE_SANITY_DPOLAR_VOLUME =", Dptri)
print("TRIANGLE_SANITY_DF6 =", DF6tri)
print("PYRAMID_SCALING_IDENTITY =", sp.simplify(pyramid_scaling_residual) == 0)

all_pass = all(
    [
        sp.simplify(E_area_check - E) == 0,
        sp.simplify(Ep_area_check - Ep) == 0,
        sp.simplify(pyramid_scaling_residual) == 0,
        DF6tri == 16,
        all(c >= 0 for c in sp.Poly(Fab, a, b).coeffs()),
    ]
)
print("ALL_EXACT_CHECKS_PASS =", all_pass)

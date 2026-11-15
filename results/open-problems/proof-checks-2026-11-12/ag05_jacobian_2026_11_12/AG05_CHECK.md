# Row AG05 (the Jacobian conjecture): the three-dimensional counterexample recomputed

12 Nov 2026. Sources read: arXiv 2609.17795v1 (A. van den Essen, 15 Sep 2026, "An elementary way to find a
counterexample to the Jacobian Conjecture"), in full; the abstract and introduction of arXiv 2610.24889v1
(M. de Bondt, 17 Oct 2026). The counterexample is due to L. Alpöge (July 2026); van den Essen's map is Alpöge's
up to linear changes of coordinates on both sides (his Section 5).

## The map

With u = 1 - (2/3) x y,

    F1 = u^3 z + y^2 ( -(2/3) u^2 - (2/9) u )
    F2 = x u^2 z + y ( u^2 - (2/3) u - 2/9 )
    F3 = x + x^2 y + x^3 z

of degrees 7, 6, 4, with rational coefficients.

## What was checked (ag05_check.py, output ag05_check.out, exact rational arithmetic)

1. det JF = -1/9, a nonzero constant. Computed three ways: with sympy as a polynomial identity; with a separate
   polynomial arithmetic written for the purpose (dictionaries of fractions, no computer algebra system); and from
   the evaluated Jacobian matrix at 200 random rational points. The middle coefficient of q, printed unclearly in
   the text, was left as an unknown: -2/3 is the only value for which the determinant is constant, and three other
   values give 10 or 11 non-constant terms.
2. F is not injective. F(1, 0, -1) = F(0, -9, 71) = (-1, -1, 0). A grid of 3375 rational points with small entries
   has 16 such coincidences, for instance F(-1, -2, -1) = F(-1, -1/2, 1/2) = (1/27, -1/9, -2), away from the
   plane w = 0.
3. F3 = x (1 + x y + x^2 z) is reducible, which by itself rules out a polynomial inverse (a component of an
   invertible map is irreducible).

Why the map fails to be injective can be seen without a computer: the plane x = 0 is mapped bijectively onto the
plane w = 0 by (y, z) -> (z - (8/9) y^2, y/9), and the surface 1 + x y + x^2 z = 0 is mapped into the same plane.

So the Jacobian conjecture is false over Q, hence over C, in dimension three, and in every dimension n >= 3 by
adding identity coordinates. This is a finite exact computation and does not depend on any unread argument.

## What the other preprints say (not checked)

De Bondt derives from Alpöge's map counterexamples to the homogeneous and low-degree forms (HJC(15), JC(12, 3),
a cubic-linear one in dimension 90) and to Zhao's vanishing conjecture. None of this was recomputed here.

## What stays open

Dimension two: every polynomial map of C^2 with constant nonzero Jacobian determinant is invertible. The
construction above does not descend: the gradient of x + x^2 y is unimodular but, by Magnus's theorem (a Keller
pair with a component of prime degree is invertible), it cannot be completed to a planar counterexample. The
known planar results (Moh's degree bound, Magnus, the Abhyankar-Moh theory of two characteristic pairs) are
untouched. The real Jacobian conjecture in the plane was already false (Pinchuk 1994).

## Proposal for the row

Restate the row to dimension two: a polynomial map F of C^2 with det JF a nonzero constant is an automorphism.
Beside it: dimension three and above refuted (Alpöge, July 2026; recomputed here).

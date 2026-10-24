# R15 idea checkpoint — unequal-amplitude two-block Hessian-null curve

Date: 2026-09-19 UTC.  
Status: SELF_CHECK_ONLY / NOT CLAIMED.

This note records the analytic route **before** adding any new checker.

For the retained Talagrand `k=2` screen, continue the previous unequal-amplitude two-block parametrization

`h = a 1_J - b 1_K`, `a,b>0`,

`S(s)=A exp(as)+B exp(-bs)+C`,

with `m=(a+b)/2`, `delta=(a-b)/(a+b)`, and normalize at `s=0` by

`x=A/S(0)`, `y=B/S(0)`, `k=C/S(0)`.

The new route is to rewrite the derivatives of `ell=log S` as cumulants of the signed three-atom mass

`x delta_a + y delta_{-b} + k delta_0`,

whose total mass is one although `k` need not be positive. If `p=ell'(0)` and

`z = p/m-delta`,

then the necessary Hessian-null cubic condition `ell'''(0)=0` should solve explicitly for `k`, hence for `x,y`, and reduce the entire unequal-amplitude null problem to one scalar `z`.

The expected formulas are

`k = 2 z(1-z^2)/((1-delta^2)(delta+3z))`,

`x = (delta+z)(1+z)(1+delta+2z)/(2(1+delta)(delta+3z))`,

`y = (delta+z)(1-z)(1-delta-2z)/(2(1-delta)(delta+3z))`.

The key prospective rigidity is not merely cubic nullity. A local minimum with Hessian-null direction also needs `ell''''(0)>=0`. If equality held, the fifth derivative would also have to vanish. For a three-point support, the centered support polynomial should force, under cubic nullity,

`kappa_5 = (a-b-3p)(kappa_4+2 kappa_2^2)`.

For unequal amplitudes, the factor `a-b-3p` is exactly `-m(delta+3z)`. The exceptional denominator branch `delta+3z=0` should itself violate cubic nullity, while `kappa_2` should be nonzero at every cubic-null point. Therefore equality `kappa_4=0` ought to force `kappa_5 != 0`, impossible at a two-sided local minimum. If this works, every genuine unequal-amplitude Hessian-null direction must satisfy the **strict** fourth-order condition `ell''''(0)>0`.

A useful immediate test case is `C=0`. The cubic-null formula then gives `z in {0,+/-1}`; positivity of `A,B` excludes `+/-1`, while the predicted fourth cumulant at `z=0` is `-2m^4`, contradicting local minimality. This would completely exclude unequal-amplitude two-block Hessian-null bifurcations when the stationary remainder `C` vanishes.

Finally, the singular limit `delta -> 0`, `z=t delta`, should recover the exceptional positive-`C` branch of the earlier balanced calculation, while fixed nonzero `z` should recover its negative-`C` branch. This is a consistency test and a possible unification of the balanced and unequal calculations.

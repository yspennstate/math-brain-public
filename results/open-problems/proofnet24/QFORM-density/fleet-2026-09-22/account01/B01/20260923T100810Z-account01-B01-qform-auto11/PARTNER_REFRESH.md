# Partner refresh after main report

A fresh account02/B01 search after `REPORT.md` was committed found a newer completed designated-partner theorem than r39:

`yspennstate/math-open-problems@8a1e6a8429cc6895c7f06c885bd372a29bb341e0`, corrected on its strict-N3 parameter choice by `22510e9146745c10374a66be90e59c7c3207a9b8`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B01/20260923T100534Z-account02-B01-qform/REPORT.md`.

Its theorem `QFORM-RANK2-CROSS-COORD-SEPARABLE-KERNEL-L2-v1` states: in original independent coordinates, if a two-hub cross block `K` has rank two with singular product

`Delta=sigma_1(K)sigma_2(K)>0`,

and two source-disjoint original kernel coordinates have diagonal quadratic coefficients `a,c!=0` with no kernel-to-leaf cross terms, while all hub self-curvature, hub-kernel couplings, leaf curvature, affine leakage and conditioned outside couplings are retained, then the full quadratic form has a continuous `C_0` density satisfying

`||p_Q||_infinity <= (9/2) Delta^(-1/3)|ac|^(-1/6).`              (1)

The theorem uses product-preserving scalar `L^4(dt)` square-phase control and two-dimensional Plancherel; it does not assert scalar pointwise Fresnel decay.

## Equation-level application

Apply (1) to the partner's target-valid family with

`Delta=epsilon^(-1)`, `a=epsilon`, `c=-epsilon`, `0<epsilon<=1/4`.

Then

`Delta^(-1/3)|ac|^(-1/6)
 =epsilon^(1/3) * (epsilon^2)^(-1/6)
 =1`,

so, for every admissible cap-one product input law,

`boxed: ||p_Q||_infinity <= 9/2.`                                (2)

The density is continuous and vanishes at infinity in this scoped branch. The corrected strict-N3 parameter choice is: for a prescribed `tau in (0,1]`, choose `0<epsilon<min(1/4,tau)` and then take the Hadamard order `N>1/(epsilon tau)` (and larger if required by the displayed leaf bounds). This correction does not alter theorem (1) or bound (2).

This newer partner result complements the main report's weighted-log compiler: it gives a true `L^1` Fourier endpoint when the two-dimensional kernel is coordinate-separable, including the indefinite sign case `ac<0`, whereas Theorem 5.1 of `REPORT.md` permits completely arbitrary Schur curvature but pays the general residual only below the half endpoint.

Full QFORM remains OPEN. This refresh supersedes the sentence in Section 7 of `REPORT.md` that called r39 the latest completed account02/B01 result; r39 remains a valid equation-level application, and (2) is the newest designated-partner application for this run.

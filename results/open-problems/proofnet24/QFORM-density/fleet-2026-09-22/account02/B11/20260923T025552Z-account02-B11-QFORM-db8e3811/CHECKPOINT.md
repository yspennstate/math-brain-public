# account02/B11 checkpoint — sign-specific Schur sharpening

Run `20260923T025552Z-account02-B11-QFORM-db8e3811`. Full QFORM remains open.

First unpaid implication attacked: the exact-rank-three `(2,1)` / `(1,2)` branch with a nonzero minority-sign ORIGINAL physical pivot, sharpening the newest account03/B11 two-sheet pivot bound while keeping the rank-two logarithmic control explicit.

Let `A=R Lambda R^T`, `R^T R=I_3`, `Lambda=diag(lambda1,lambda2,-mu)`, `lambda1,lambda2,mu>=1`, and fix an ORIGINAL coordinate `i` with `a=A_ii<0`. Put `c=||r_i||^2`. Writing

`A=[[a,b^T],[b,C]]`, `S=C-bb^T/a`,

inertia additivity gives `S>=0`, `rank S=2`. If its two nonzero eigenvalues are `s1,s2`, then

`a s1 s2 = det(Lambda) c`, hence `s1 s2 = |det Lambda| c/|a|`.

The identity follows by summing `det A[{i,j,k}]=a det S[{j,k}]` over pairs `j<k`, using Cauchy-Binet and `sum_{J: |J|=2} det(R_{i union J})^2=c` (the rank-three volume-sampling marginal identity).

The completed rank-two PSD theorem in `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837:.../COUNTEREXAMPLE_SEARCH.md` gives

`||p_{X_-^T S X_-}||_inf <= 2 pi / sqrt(s1 s2)`.

Conditioning only on the original independent variable `X_i`, completing the square gives

`Q=a(X_i+b^T X_-/a)^2 + R`, `R=X_-^T S X_-`.

The conditional square density is bounded by `|a|^{-1/2}(R-t)_+^{-1/2}`. For every probability density `g<=M`, the one-sided half-Riesz potential obeys

`sup_t int_0^infty u^{-1/2} g(t+u) du <= 2 sqrt(M)`,

by layer cake and `P(0<U<h)<=min(1,Mh)`. Therefore

`||p_Q||_inf <= 2 sqrt(2 pi) (|a| c |det Lambda|)^(-1/4)`.

Reflection gives the `(1,2)` case. This is uniform in the output level and improves the newest partner account03/B11 r22 cone estimate on this branch; it does not close the near-null limit `a->0`.

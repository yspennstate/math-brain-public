# Addendum — the tempting two-heavy radial Laplace domination is false

This addendum is part of run `20260922T184845Z-account01-B17-QFORM-r12`. It does **not** retract `QFORM-TWO-ORTHOGONAL-SAMESIGN-HEAVY-NOESCAPE-v1`; it kills the proposed next extension in Section 7 of `REPORT.md` under arbitrary nonorthogonal two-heavy geometry.

## Candidate that fails

A natural attempt to extend the two-orthogonal-heavy theorem is the following radial comparison. Let `X=(X_1,X_2)` have independent one-dimensional probability densities bounded by one, let `V` be a real `2x2` matrix with `VV^T<=I_2`, and independently let

`G_C ~ N(0,C)`, `C=I_2-VV^T`.

The hoped-for inequality was

`E exp(-a ||sqrt(12)VX+G_C||^2) <= (1+2a)^(-1)`                         (R)

for every `a>=0`. If true, inserting it into the same positive half-Riesz integral used in the main report would eliminate the entire two-heavy same-sign mesoscopic regime. It is false.

## Exact cap-one counterexample

Take `X_1,X_2` iid `Unif[-1/2,1/2]` and

`V = [[1/sqrt(2),1/sqrt(2)],[0,0]]`.

Then `VV^T=diag(1,0)`, so `C=diag(0,1)`. Writing `G~N(0,1)`,

`sqrt(12)VX+G_C = (sqrt(6)(X_1+X_2), G)`.

Hence

`L(a):=E exp(-a ||sqrt(12)VX+G_C||^2)`
`=(1+2a)^(-1/2) E exp[-6a(X_1+X_2)^2]`.                              (1)

Let `S=X_1+X_2`. Its exact density is `1-|s|` on `[-1,1]`. Put `kappa=12a`. Then

`E exp[-(kappa/2)S^2]`
`=2 int_0^1 (1-s) exp(-kappa s^2/2) ds`
`=sqrt(2pi/kappa) erf(sqrt(kappa/2)) - (2/kappa)(1-exp(-kappa/2))`.       (2)

Thus (R) is equivalent here to

`sqrt(2pi/kappa) erf(sqrt(kappa/2)) - (2/kappa)(1-exp(-kappa/2))`
`<= (1+kappa/6)^(-1/2)`.                                                (3)

But the left side has asymptotic leading constant `sqrt(2pi/kappa)`, while the right side has leading constant `sqrt(6/kappa)`. Since `sqrt(2pi)>sqrt(6)` (`pi>3`), inequality (3) fails for all sufficiently large kappa.

For a completely explicit instance take `kappa=10000`, i.e. `a=2500/3`. The elementary bound `erf(x)>=1-exp(-x^2)` for `x>=0` gives

`LHS(3) >= sqrt(pi/5000)(1-exp(-5000))-1/5000`.

Using only `pi>3.1415` and `exp(-5000)<10^(-3)`,

`LHS(3) > 0.02506*0.999-0.0002 > 0.024834`,

whereas

`RHS(3)=sqrt(6/10006) < sqrt(6/10000) <0.0245`.

Therefore (R) is rigorously false for this exact product cap-one source.

Equivalently, the more abstract determinant comparison

`int f_1(x)f_2(y) exp[-(x,y)K(x,y)^T] dxdy <= det(I+K/6)^(-1/2)`

fails even for centered unit intervals and the rank-one matrix

`K=(kappa/2)[[1,1],[1,1]]`.

## Interpretation

This is a refutation of a **proof mechanism**, not a QFORM counterexample. The high-frequency Laplace transform can exceed the variance-matched Gaussian comparison because two independent physical coordinates may add along one heavy spectral line; the triangular density of their sum has enough mass near zero to beat the pointwise Gaussian transform for large `a`.

The central QFORM density averages these Laplace transforms against the positive `s^(-1/2)` half-Riesz weight. The present calculation does not show that this average exceeds `3sqrt(2)`; in fact the centered-interval collinear control remains below it. Thus the surviving next question is an **integrated** two-heavy comparison, not the false pointwise radial comparison.

Status: `REFUTED_INTERMEDIATE_MECHANISM`; full QFORM remains OPEN.

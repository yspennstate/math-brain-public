# Addendum — noncentral Gaussian limits cannot beat `3 sqrt(2)`

This closes the nearest remaining B17 witness mechanism identified in the preceding addendum. The original arbitrary bounded-density product-law conjecture remains OPEN.

## Theorem `QFORM-GAUSSIAN-FULL-NONCENTRAL-C3SQRT2-v1`

Let `G~N(m,Sigma)` in `R^n`, with arbitrary mean `m` and covariance

`Sigma >= sigma^2 I_n`, `sigma>0`.

Let `A` be any real symmetric `n x n` matrix with at least three eigenvalues of absolute value at least one. Then `Q=G^T A G` has a bounded continuous density and

`||p_Q||_infinity <= 1/(2 sqrt(2) sigma^2)`.

The constant is sharp: equality is attained in the centered three-dimensional mixed-sign case `m=0`, `Sigma=sigma^2 I_3`, `A=diag(1,1,-1)`.

Thus, with the covariance floor `sigma^2=1/12` inherited by covariance-convergent projection limits of independent density-one coordinates,

`||p_Q||_infinity <= 3 sqrt(2)`

for **every Gaussian limit, centered or noncentered**, in arbitrary dimension and with arbitrary extra spectral directions.

### Proof

Write

`G=m+Sigma^(1/2) Z`, `Z~N(0,I_n)`,

and put

`B=Sigma^(1/2) A Sigma^(1/2)`, `d=Sigma^(-1/2)m`.

Then exactly

`Q=(Z+d)^T B (Z+d)`.

Indeed, `Bd=Sigma^(1/2)Am` and `d^T B d=m^TAm`.

Diagonalize

`B=O^T diag(mu_1,...,mu_n) O`.

With `U=OZ~N(0,I_n)` and `delta=Od`,

`Q = sum_j mu_j (U_j+delta_j)^2`,

where the `U_j` are independent standard Gaussians.

The preceding full centered-Gaussian theorem shows, by Courant-Fischer, that among the coefficients `mu_j` one may select either:

1. a mixed-sign triple `a,b,-c` with `a,b,c>=sigma^2`, whenever the three large spectral directions of `A` include both signs; or
2. a same-sign triple with all three coefficient magnitudes at least `sigma^2`, when three large directions have the same sign.

The corresponding **centered** three-square core has density norm at most `1/(2 sqrt(2) sigma^2)` in case 1, and at most `1/(sigma^2 sqrt(2 pi e)) < 1/(2 sqrt(2) sigma^2)` in case 2.

It remains to show that the shifts `delta_j` cannot increase this core bound.

For a standard Gaussian `U` and real `delta`, the noncentral square `(U+delta)^2` has the Poisson-mixture representation

`(U+delta)^2 |_ {K=k}  =_d chi^2_{1+2k}`,

where

`K ~ Poisson(delta^2/2)`.

This follows from the Laplace transform:

`E exp(-s(U+delta)^2)
 = (1+2s)^(-1/2) exp(-delta^2 s/(1+2s))`

and

`E[(1+2s)^(-(1+2K)/2)]
 = (1+2s)^(-1/2)
   exp((delta^2/2)((1+2s)^(-1)-1))`.

The exponents agree because

`((1+2s)^(-1)-1)/2 = -s/(1+2s)`.

Conditional on `K=k`, use gamma additivity:

`chi^2_{1+2k} =_d chi^2_1 + chi^2_{2k}`

with the two summands independent. Do this independently for every selected coordinate. Therefore, conditional on the Poisson indices of the selected coordinates, the selected **noncentral** quadratic core has the form

`Y_noncentral =_d Y_centered + R_K`,

where `Y_centered` is exactly the corresponding centered three-square core with the same coefficients, and `R_K` is an independent (possibly signed) linear combination of even-degree central chi-square variables.

All unselected quadratic coordinates, including their shifts, may be absorbed into an additional independent residual variable. Hence, conditional on all selected Poisson indices,

`Q =_d Y_centered + R`

for some independent random variable `R`. Convolution with a probability measure cannot increase an `L^infinity` norm, so

`||p_{Q | K}||_infinity <= ||p_{Y_centered}||_infinity
 <= 1/(2 sqrt(2) sigma^2)`.

Finally, the unconditional density is a convex mixture of the conditional densities. A pointwise convex mixture preserves the same uniform bound, proving

`||p_Q||_infinity <= 1/(2 sqrt(2) sigma^2)`.

Continuity follows because the selected centered three-square core has a bounded continuous density, and convolution with any probability measure preserves boundedness and continuity; the Poisson mixture is dominated by the same uniform bound and converges pointwise by dominated summation. QED.

## Consequence for the B17 lower-bound search

Account02/B17 proves that `3 sqrt(2)` is a source-valid target lower bound via centered uniform block averages. The present theorem proves that **no Gaussian projection-limit witness whatsoever** — not even with arbitrary covariance, arbitrary mean/noncentrality, arbitrary dimension, arbitrary correlation in the eigenbasis, or arbitrary extra spectral directions — can raise that lower bound.

Therefore any valid target witness with density peak strictly larger than `3 sqrt(2)` must be genuinely non-Gaussian at the relevant scale (or finite-dimensional/mesoscopic in a way that does not collapse to a Gaussian projection limit). The next distinct B17 search should target such non-Gaussian mesoscopic or finite-dimensional constructions rather than shifted CLT families.

This theorem is a mechanism ceiling, not a universal upper bound for the original product-density problem.

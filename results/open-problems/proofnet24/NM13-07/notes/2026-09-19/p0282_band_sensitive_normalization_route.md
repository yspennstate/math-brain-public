# P0282 band-sensitive normalization route — idea before production checking

Date: 2026-09-19 UTC  
Track: `proofnet24/NM13-07`  
Canonical claim: `P0282`  
Entry frozen metric: `N_exact = 109`

The current `1521/2521` theorem loses most sharply at the finite seam `s=j-1=66`.  The exact multiband source lower bound uses

`nu_s(X>m) <= Pl_s(X>m) / rho_0^2`,

where `X=mu_1` and `rho_0=(K-s+1)/(K+1)` is the global minimum of `R_{s,n}(mu)`, attained by the one-row shape.  This is wasteful when conditioning on `X<=m`, because the one-row minimizer is then excluded.

## New route: first-row-sensitive lower normalization

For `mu |- s`,

`R_{s,n}(mu)=prod_{x in mu} (K-c(x))/(K-c(x)+1)`.

Fix a first-row cap `mu_1<=m`.  Since each factor decreases with content, the candidate minimizer under this cap is the row-packed partition

`lambda*(s,m)=(m,m,...,m,r)`, with `s=q m+r`, `0<=r<m`.

Its correction telescopes row by row:

`rho_m(s,K) = prod_{i=1}^q (K+i-m)/(K+i)`

and, if `r>0`, one additional factor

`(K+q+1-r)/(K+q+1)`.

The intended combinatorial lemma is

`mu_1<=m  ==>  R_{s,n}(mu) >= rho_m(s,K)`.

A direct way to prove it is row-major domination: after packing every row as far left and as high as the partition constraint allows, the ordered cell-content vector is coordinatewise maximal; because `(K-c)/(K-c+1)` is decreasing in `c`, the packed shape minimizes the product.

If this lemma is correct, then with `p_m=Pl_s(X>m)` one gets the stronger denominator bound

`A_s=E_Pl R^2 >= rho_m^2 (1-p_m) + rho_0^2 p_m`,

and hence

`nu_s(X>m) <= p_m / (rho_m^2(1-p_m)+rho_0^2 p_m)`.

This can be substituted independently at every band in the retained multiband summation.  It directly attacks the `s=66` bottleneck without changing the source metric or the large-s tail architecture.

## Tests to perform after this note

1. Prove the packed-shape minimizer lemma on the page and exact-check it exhaustively for small `s,m,K`.
2. Recompute the exact `s=66` multiband seam with the strengthened tilted-CDF bound and locate the smallest rational linear boundary that clears one.
3. Check whether the same boundary admits an eventual first-row tail proof.  If not, report the finite-seam gain honestly as a mechanism improvement rather than promoting a global theorem.
4. Only after a genuine mathematical gain, move the frozen row metric from 109 to 110 with the existing exact Gessel/Toeplitz machinery.

This note intentionally precedes new production checker code.
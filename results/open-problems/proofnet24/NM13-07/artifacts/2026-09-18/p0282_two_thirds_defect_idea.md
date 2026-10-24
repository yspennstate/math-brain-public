# P0282 idea before validation — conserved hook mass and a two-thirds defect window

Date: 2026-09-18 UTC
Track: NM13-07
Target: P0282, Chen fixed-size LIS log-concavity

This note is intentionally written before any new checker. It records the route to test; it is not itself a certificate.

The preceding run factored, for `E_j(n)=ell_{n,n-j}` and `n>=2j`,

`E_j(n)=((n)_j^2/j!) A_j(n)`,

where under Plancherel measure on partitions `mu|-j`,

`A_j(n)=E[R_mu(n,j)^2]`,

`R_mu(n,j)=prod_c (n-j-c+1)/(n-j-c+1+mu'_c)`.

The previous all-shape bound treated the entire first-order hook loss as error and therefore stopped at `j=O(sqrt(n))`. The new observation is that the first-order mass is actually conserved across every residual Young diagram:

`sum_c mu'_c = j`.

Put `N=n-j`, `h_c=mu'_c`, `d_c=N-c+1`, and `u_c=h_c/d_c`. Then

`log R_mu = -sum_c log(1+u_c)`.

Separate the deterministic first-order term `j/N`:

`log R_mu + j/N = -A(mu)+B(mu)`,

where

`A(mu)=sum_c h_c (c-1)/(N(N-c+1)) >= 0`,

`B(mu)=sum_c (u_c-log(1+u_c)) >= 0`.

Using `u-log(1+u)<=u^2/2`, `sum h_c=j`, `h_c<=j`, and `c<=j` gives the proposed uniform error

`|log R_mu + j/(n-j)| <= e_j(n)`,

`e_j(n):=max{ j(j-1)/((n-j)(n-2j+1)), j^2/(2(n-2j+1)^2) }`.

Method #5 is to introduce the tilt

`A_j(n;t)=E[R_mu(n,j)^(2t)]`, `Phi_j(t)=log A_j(n;t)`.

Then `Phi'_j(t)=2 E_t[log R_mu]`. The uniform interval above should integrate from `t=0` to `1` to give

`log A_j(n) = -2j/(n-j) + eta_j(n)`, `|eta_j(n)|<=2e_j(n)`.

The deterministic term `b_j=-2j/(n-j)` has favorable discrete curvature

`2b_j-b_{j-1}-b_{j+1}=4n/((n-j)((n-j)^2-1)) > 0`.

Combining this with the exact Chen ratio from the previous run should yield

`log Q_j(n) > 1/(j+1) - (4e_j+2e_{j-1}+2e_{j+1})`.

For a clean explicit corollary, if `3 n^2 >= 64 (j+1)^3`, then automatically `n>=4(j+1)`. For `r in {j-1,j,j+1}` one then has

`e_r <= 8 r^2/(3n^2)`,

so

`4e_j+2e_{j-1}+2e_{j+1} <= (64j^2+32)/(3n^2) < 1/(j+1)`.

Thus the proposed exact theorem is strict Chen log-concavity whenever

`3 n^2 >= 64 (j+1)^3`.

Equivalently this gives a boundary window of order `n^(2/3)`, with explicit constant `3^(1/3)/4` in the sufficient condition. A sharper asymptotic reading of the exact `e_j` bound should give every constant `c<1/2`: for fixed `c<1/2`, all sufficiently large `n` and `j<=c n^(2/3)` should satisfy the inequality because the total error is `(8+o(1))j^2/n^2`.

Method #12 is the conserved identity `sum mu'_c=j`; it is the mechanism that removes the false `O(j/n)` obstruction. Method #21 is to compare the tilted Plancherel observable with the Kerov/Plancherel concentration and cumulant literature. The immediate theorem above should not need an imported asymptotic theorem; such machinery is reserved for improving the residual second-order error beyond the all-shape bound.

Validation plan after this note: (i) algebraically recheck every inequality; (ii) exact-integer/Rational self-check at the minimal integer thresholds for representative `j`; (iii) independently reconstruct `E_{j-1},E_j,E_{j+1}` by residual partitions and hook lengths and verify positive Chen margins. The analytic proof, not the finite sample, must carry the all-`j` claim.

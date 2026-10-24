# HARD7-05 route note — subtract certified subleading spectral mass

New-method route written before the checker.

The preceding six-cycle Craig certificate bounds `tr(K^6)` and then uses only `||K||^6 <= tr(K^6)`. The loss is the unspent spectral mass `sum_{j>=2} lambda_j^6`. Rather than refine the Craig partition again, compress the killed AR(1) operator `K=1_{(0,infty)} P_r 1_{(0,infty)}` to the even-polynomial subspace

`E = span{1, x^2, x^4}`

in `L^2((0,infty),gamma)`. Its generalized Ritz values `nu_1 >= nu_2 >= nu_3` for `M v = nu G v` satisfy `lambda_j >= nu_j` by min-max. If exact inertia tests certify

`nu_2 > 7/25` and `nu_3 > 21/200`,

then

`lambda_1^6 <= tr(K^6) - (7/25)^6 - (21/200)^6`.

The matrix entries are truncated bivariate Gaussian even moments for correlation `r=287831/500000`, and reduce to the two scalar quantities

`P = 1/4 + asin(r)/(2*pi)`,  `h = r*sqrt(1-r^2)/(2*pi)`.

Planned exact checks:

1. `det(M-(7/25)G)<0` and its `(0,0)` entry is positive. For a symmetric 3x3 pencil this forces exactly one negative direction, hence two generalized eigenvalues above `7/25`.
2. Sylvester minors of `M-(21/200)G` are all positive, hence all three generalized eigenvalues exceed `21/200`.
3. Combine those lower bounds with the already certified `tr(K^6)<15014436/10^8` and test a purely rational power inequality for a stronger source-valid lower persistence endpoint.

This attacks the premise that the current trace loss is irreducible; it is not another finite-mesh persistence simulation and it does not change the source process.
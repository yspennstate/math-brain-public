# Addendum — variance sharpening of the fixed-order-three anchor bank

This addendum sharpens Theorem 4.1 in `REPORT.md`. The theorem there remains valid; this uses the exact ridge-size distribution to improve `5/6` to `7/8` at the current `23/24` leverage threshold.

## Exact ridge-size law

If the nonzero eigenvalues of `BB^T` are `x_s` and

`kappa_s = z x_s/(1+z x_s)`,

then the probability generating function of the ridge minor size `N` is

`E[s^N]
 = D_B(sz)/D_B(z)
 = prod_s (1-kappa_s+kappa_s s)`.

Hence `N` is exactly a sum of independent Bernoulli variables with parameters `kappa_s`. At the calibrated scale `E N=2`,

`Var(N)=sum_s kappa_s(1-kappa_s)<=2`.

Cantelli's one-sided variance inequality therefore gives

`tau:=P(N>=4)
     =P(N-E N>=2)
     <= Var(N)/(Var(N)+4)
     <=1/3`.

## Sharpened localization

Repeating the fixed-order monotonicity argument from the report,

`p_i <= (1-tau) ell_i^(3)+tau`.

Since `tau<=1/3` and the right-hand inversion decreases with `tau`,

`ell_i^(3) >= (p_i-1/3)/(2/3)=(3p_i-1)/2`.

Thus if both physical ridge anchors satisfy

`p_i>23/24`, `q_j>23/24`,

their fixed-order-three row and column inclusion probabilities are each `>15/16`. Under the same joint fixed-order-three minor law,

`P(i in I, j in J)
 >=15/16+15/16-1
 =7/8`.

Therefore

`boxed: M_3(i,j) > (7/8) E_3(B).`

On the current O0 resource `E_3(B)>=1/256`,

`boxed: M_3(i,j)>7/2048=0.00341796875.`

For `b=B_ij!=0`, the exact anchored Schur factorization gives the corresponding stronger residual statement

`boxed: b^2 E_2(C^sharp)>7/2048.`

This sharpening still uses no reciprocal selection of an individual minor.

## Optional leverage-sensitive tail refinement

A physical leverage `p_i>h` also forces at least one spectral Bernoulli parameter `alpha>h`, because `p_i` is a convex combination of the `kappa_s`. Writing the remaining Bernoulli sum as `M`, with mean `mu=2-alpha`, one has

`P(N>=4)
 <= alpha P(M>=3)+(1-alpha)P(M>=4)
 <= alpha mu^2/6 +(1-alpha)mu^3/24
 = (2-alpha)^2(alpha^2+alpha+2)/24`.

The last expression is decreasing on `alpha in[0,1]`, since its derivative is
`(alpha-2)(4alpha^2-alpha+2)/24<0`. At `h=23/24` this yields

`tau <= 1395625/7962624 =0.175271995764...`

and consequently the jointly anchored fixed-order-three fraction is actually

`>5903447/6566999 =0.898956585801...`.

The cleaner `7/8` lower bound above is sufficient for the current handoff; the sharper rational is recorded for later constant optimization.

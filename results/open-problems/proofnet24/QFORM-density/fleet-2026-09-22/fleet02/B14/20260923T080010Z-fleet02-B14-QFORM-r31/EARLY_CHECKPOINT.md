# B14 early checkpoint — diffuse diagonal-twisted Schur bank

Programme: QFORM-DENSITY-3EIG-20260922. Full conjecture remains OPEN.
Run: 20260923T080010Z-fleet02-B14-QFORM-r31.

First unpaid implication attacked: extend the completed fleet03/B14 indefinite-pair + exact-rank-one Schur-bank theorem to a bank carrying arbitrary ORIGINAL-coordinate diagonal quadratic curvature, without fragment/support/moment assumptions or post-rotation independence.

## Lemma: Fourier half-decay gives uniform square-root small ball

Let R be any real random variable satisfying

    |phi_R(t)| <= K |t|^{-1/2}  (t != 0).

Then for every s in R and rho>0,

    P(|R-s|<=rho) <= c_G K sqrt(rho),

where

    c_G = 2^(1/4) Gamma(1/4) sqrt(2 pi e)/(2 pi)
        = 2.8359324415... .

Proof: let G_rho be N(0,rho^2), independent, with density g_rho. On |R-s|<=rho,

    g_rho(s-R) >= exp(-1/2)/(sqrt(2 pi) rho),

hence P(|R-s|<=rho) <= sqrt(2 pi e) rho p_{R+G_rho}(s). Fourier inversion for the Gaussian-smoothed law gives

    p_{R+G_rho}(s)
      <= (2 pi)^(-1) int |phi_R(t)| exp(-rho^2 t^2/2) dt
      <= (2 pi)^(-1) K 2^(1/4) Gamma(1/4) rho^(-1/2).

Multiplication proves the claim. No density of R is assumed.

## Application of the required Claude result

The proved rank-one case of Claude's Fresnel–Brascamp–Lieb Theorem F (source pin e5f71d79eff325201dd0274053d20268ce65b837, FOURIER_ROUTE_REPORT.md) says: for independent cap-one V_i, a unit vector a with max_i a_i^2<=1/2, arbitrary diagonal D, arbitrary affine l,c, and lambda !=0,

    R(V)=V^T(D+lambda aa^T)V+l^T V+c

obeys

    |phi_R(t)| <= 2 sqrt(pi) |lambda|^(-1/2) |t|^(-1/2).

Therefore the preceding lemma yields, uniformly in l,c and in all fragmented/unbounded input laws,

    sup_s P(|R-s|<=rho)
      <= C0 |lambda|^(-1/2) sqrt(rho),

    C0 = 2^(3/4) sqrt(e) Gamma(1/4)
       = 10.0531187537... .

This is the exact small-ball input needed by the completed pair-log theorem. It keeps the whole bank intact; no active-fragment normalization occurs.

## Consequence to finish in the report

For an original-coordinate invertible indefinite pair B, kappa=sigma_min(B), and Schur complement S, if on a disjoint original-coordinate bank V

    S_VV = D + lambda aa^T,

with D diagonal, ||a||_2=1, max a_i^2<=1/2, |lambda|>=s, while all S_VZ, S_ZZ and affine terms are arbitrary, then fleet03/B14 r30's pair-completion scope plus the pair-log estimate gives

    ||p_Q||_infinity
      <= C_* [|det B| kappa s]^(-1/4),

    C_* = 4 sqrt(2 C0) = 17.9359917518... .

This extends partner r30 from an exact rank-one Schur bank to rank-one plus arbitrary diagonal bank curvature, at essentially the same constant. The next check is to write the conditioning/completion carefully and exhibit a target-valid diffuse family where every individual bank coefficient tends to zero but the new theorem stays uniform.

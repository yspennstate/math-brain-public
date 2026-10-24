# auto16 addendum — recursive two-hub compression and pair-pivot h<1 extension

This addendum strengthens the same run's `REPORT.md`. Full QFORM remains OPEN.

## A. Recursive scalar compression improves from 6k+2 to 4k+2

The immediately preceding account01/B13 run (`math-open-problems@829f5ef443f751724dc20e7ec45d04b37459df6`) proved recursive high-slab-ratio compression using the older three-hub E2 theorem. The new `QFORM-SCALAR-E2-LINF-OR-TWOHUB-v1` from the present report can be substituted at every recursive step.

Let an actual interval witness have slab ratio

`R=P{Q in J_0}/|J_0|`,

fix an original scalar pivot `d=A_kk!=0`, and let `M_0` be a scalar-Schur physical cross block with `E_0=E_2(M_0)>0`. Put

`C_2=17.0863179786`,

`T_2(R,d)=(C_2/(R sqrt(|d|)))^8`,

`tau_2(R,d)=T_2(R,d)^(1/4)=C_2^2/(R^2|d|)
              <291.943/(R^2|d|)`.                                (A.1)

Whenever the current residual block has `E_t>T_2`, the density alternative

`||p_Q||inf <= C_2 |d|^(-1/2) E_t^(-1/8)`

would be strictly below the observed slab ratio `R`. Therefore the two-hub branch is forced. Remove at most two row hubs and at most two column hubs. The surviving block has

`E_(t+1)<E_t/4`.                                                  (A.2)

After at most

`k_2=max(0,ceil(log_4(E_0/T_2)))`                                 (A.3)

steps, cumulative hub sets satisfy `|H|,|C|<=2k_2` and the residual block `N` satisfies

`E_2(N)<=T_2`, hence `s_2(N)<=tau_2`.                             (A.4)

A best rank-one approximation to `N`, together with all entries touching the cumulative row or column hubs, gives a Schur-block approximation of rank at most

`2k_2+2k_2+1=4k_2+1`.                                           (A.5)

Adding back the exact scalar-Schur rank-one correction gives the original cross block approximation

`boxed:
 dist_op(A[I,J], {rank<=4k_2+2})
 <=291.943/(R^2|d|).
}`                                                                      (A.6)

Thus the present run improves the preceding recursive theorem simultaneously in rank growth (`6k+2 -> 4k+2`) and operator scale (`895.352 -> 291.943`) for the scalar-pivot branch. This is structural only; the residual is not deleted from the quadratic random variable.

## B. Pair-pivot h<1 extension

The preceding account01/B13 report `math-open-problems@2b4a2e8c6490c5e2fb063a2aaa34303f6ba3d9ce` proves for an invertible indefinite original-coordinate physical pair, with least singular value `kappa`, the pointwise conditional envelope

`p_Q(t) <=4 kappa^(-1/2) E|t-R|^(-1/2)`.                          (B.1)

The present report gives, under an entropy-weighted E2 minor law with row-marginal cap `h<1`, an `L^p` Schur-remainder density for every Fourier exponent `r` satisfying `2h<r<2`, where `p=r/(r-1)>2`:

`||p_R||_p
 <=[2 sqrt(e/(2h)) r/(r-2h)]^(1/r) K_2(mu)^(-1/(4r)).            (B.2)

For completeness, if `g` is any probability density in `L^p`, `p>2`, and `r=p/(p-1)<2`, split the half-Riesz integral at `H`. With `beta=1-r/2`, Holder on `|u|<=H` and mass one outside give

`sup_t int |t-s|^(-1/2)g(s)ds`
` <= G (2/beta)^(1/r)H^(beta/r)+H^(-1/2)`,                       (B.3)

where `G=||g||_p`. Optimization yields

`sup_t E|t-R|^(-1/2)
 <= H_r G^(r/2)`,                                                 (B.4)

`H_r=sqrt(2) beta^(-3/2)(2beta/r)^(r/2)`.                         (B.5)

Combining (B.1)-(B.5) proves:

### `QFORM-PAIR-E2-ENTROPIC-LP-LINF-v1`

For every `1/2<=h<1` and `2h<r<2`,

`boxed:
 ||p_Q||inf
 <= C_pair(h,r) kappa^(-1/2) K_2(mu)^(-1/8),
}`                                                                      (B.6)

where

`C_pair(h,r)
 =4 H_r [2 sqrt(e/(2h)) r/(r-2h)]^(1/2)`.                        (B.7)

Again the E2 exponent is exactly `-1/8`, independent of the chosen interpolation exponent.

Take the same two-hub parameters

`h=67/100`, `r=87/50`, `L=log4`.                                 (B.8)

Then `H_r=5.7723005554...`, the pre-KL constant in (B.7) is

`81.2766836373...`,

and any entropy law with `D(mu||w_2)<=log4` gives

`boxed:
 ||p_Q||inf
 <=96.654810466 kappa^(-1/2) E_2(M)^(-1/8).
}`                                                                      (B.9)

If (B.9) fails in both orientations, the same entropy-projection duality gives at most two row hubs and two column hubs jointly carrying more than half of the E2 minor mass. In particular the exact null-diagonal pair

`[[0,b],[b,0]]`

is covered with `kappa=|b|`.

This trades a larger analytic constant than the earlier `75.41281` three-hub implementation for a strictly smaller finite obstruction: two hubs per side.

## C. Pair recursive rank compression

The same witness recursion as in Section A, now using (B.9), gives

`T_pair=(96.654810466/(R sqrt(kappa)))^8`,

`tau_pair=96.654810466^2/(R^2 kappa)
          <9342.16/(R^2 kappa)`.                                  (C.1)

After

`k_pair=max(0,ceil(log_4(E_0/T_pair)))`                           (C.2)

two-hub removals, the pair-Schur block is within `tau_pair` of rank at most `4k_pair+1`. Adding the exact rank-at-most-two pair-Schur correction gives

`boxed:
 dist_op(original cross block,{rank<=4k_pair+3})
 <9342.16/(R^2 kappa).
}`                                                                      (C.3)

For an exact zero-diagonal pair, replace `kappa` by `|b|`. This improves the previous recursive rank growth `6k_pair+3 -> 4k_pair+3`, at the cost of a weaker numerical residual scale. Both versions should be retained: the three-hub theorem is better when operator accuracy is decisive; the two-hub theorem is better when finite physical-core size is decisive.

## D. Remaining debt

The strongest current B13 obstruction after combining the main report and this addendum is a finite **two-by-two hub core**, or an exact transverse-star currency from the designated account02/B13 Schur identity, plus rank-one tails whose operator error is witness-dependent. The first unpaid implication remains

`QFORM-SCALAR-E2-TWOHUB-STAR-CLOSURE-v1`.

The live correction against raw slab continuity prevents simply dropping the small operator tail on arbitrarily translated, fragmented product supports.

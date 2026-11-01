SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B13, 2026-09-23T19:31:14Z.
attacking: the exact diagonal-plus-rank-two endpoint from fleet02/B13, using product purification plus the already-proved diffuse rank-two separable half-Riesz theorem after a genuine original-coordinate Schur pivot.

# fleet01/B13 — extremal product reduction and diffuse rank-two Schur-product rigidity

Programme: `QFORM-DENSITY-3EIG-20260922`.  
Run: `20260923T193114Z-fleet01-B13-qform-auto11`.  
Classification: `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_TARGET_LEVEL_IMPLICATION`.  
Full QFORM: **OPEN / NOT PROVED / NOT DISPROVED**. Continuity: separately OPEN.  
Execution memory status: `WITHOUT_VERIFIED_BRAIN`.

All random-coordinate conditioning below is on ORIGINAL physical coordinates. Deterministic orthogonalization is used only inside coefficient identities/Fourier integrals; no rotated random coordinates are declared independent.

## 1. Fresh premises actually used

1. Current owner/control keeps every worker exclusively on full QFORM and keeps the full theorem OPEN.
2. Live corrections retained: law-uniform pointwise quadratic oscillatory decay is false; rotated coordinates are not independent; arbitrary-joint coarea/projection-density shortcuts do not solve the indefinite pushforward; bounded-diameter or uniformly bounded-fragment extremality is false.
3. Designated partner fleet02/B13, canonical report
   `yspennstate/math-open-problems@eeabf558e96ea803514f8e438b49c18fe9ee789a`,
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B13/20260923T171027Z-fleet02-B13-rank2core/REPORT.md`.
   Its exact zero-disjoint-two-minor endpoint is
   `A=D+R`, `D` diagonal, `rank R<=2`.
4. Existing fleet01/B14 theorem, source
   `yspennstate/math-open-problems@0d6e70139fe0f7d8ee22cc5210efb3b8d00a0bda`,
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B14/20260922T181432Z-fleet01-B14-QFORM-r15/REPORT.md`.
   I do **not** rename this prior theorem as new. Its `QFORM-RANK2-DIFFUSE-SEPARABLE-HALF-RIESZ-v1` states: for `W^T W=I_2`, all row leverages at most `1/2`, invertible symmetric `M`, independent cap-one inputs, and arbitrary coordinatewise measurable phases/perturbations,

   `sup_s E |(W^T X)^T M(W^T X)+sum_j V_j(X_j)-s|^(-1/2)
       <=4 sqrt(2e) |det M|^(-1/4)`.

   Its grouped Schur theorem converts this to an ambient density bound after a genuine original-coordinate scalar square.

## 2. Exact extremal-product reduction

### Theorem 2.1 — `QFORM-EXTREMAL-PRODUCT-SUP-v1`

For every nonnegative measurable `K:R^n->[0,infinity]`,

`sup_{0<=f_i<=1, int f_i=1} int K(x) prod_i f_i(x_i) dx
 = sup_{|E_i|=1} int_{prod_i E_i} K(x) dx`.                 (2.1)

No optimizer is asserted.

### Proof

First assume `0<=K<=M`. Fix all marginals except `f_i` and write

`g_i(x_i)=int K(x) prod_{j!=i} f_j(x_j) dx_{-i}`.

The one-dimensional bathtub identity gives

`sup_{0<=f<=1, int f=1} int g_i f
 = sup_{|E|=1} int_E g_i`.                                  (2.2)

Indeed layer-cake/rearrangement of `g_i` fills unit Lebesgue mass at its largest values; if a level set must be split, non-atomic Lebesgue measure permits the required portion. Applying (2.2) successively to the finitely many coordinates, with an arbitrarily small total epsilon loss if a supremum is not attained, proves the `<=` direction in (2.1); the reverse direction is immediate by taking `f_i=1_{E_i}`.

For general nonnegative `K`, apply the bounded result to `K_m=min(K,m)`. Monotone convergence gives the result because

`sup_f int K f >= sup_E int_E K`

trivially, while for every `m`,

`sup_f int K_m f = sup_E int_E K_m <= sup_E int_E K`,

and `int K f=sup_m int K_m f`.

For the QFORM slab kernel `K=1_{x^T A x in J}`, any strict witness can moreover be approximated by bounded finite unions of intervals in every coordinate: Lebesgue regularity gives finite unions with arbitrarily small symmetric difference, their measures can be adjusted to exactly one by adding/trimming a tiny interval, and

`|prod_i 1_{E_i}-prod_i 1_{F_i}|_{L1} <= sum_i |E_i triangle F_i|`.

Thus strict slab ratios transfer with arbitrarily small loss to bounded finite-union unit-measure product sets. There is no single-interval, centered-uniform, bounded-diameter, or uniform fragment-count conclusion. QED.

## 3. New exact Schur transport identity for an exact diagonal-plus-rank-two endpoint

Assume now

`A=D+U Lambda U^T`,                                             (3.1)

where `D=diag(d_1,...,d_n)`, `U^T U=I_2`, and `Lambda` is invertible symmetric `2x2`. Put `u_i^T` for the rows of `U` and `c_i=||u_i||^2`.

Choose a genuine original coordinate `k`. Write

`d=d_k`, `u=u_k`, `c=||u||^2`, `a=A_kk=d+u^T Lambda u`.            (3.2)

Assume `a!=0` and `c<1`. The full Schur complement after pivoting `k` is

`S=A_{-k,-k}-a^(-1) A_{-k,k}A_{k,-k}
  =D_{-k}+U_{-k} N U_{-k}^T`,                                   (3.3)

with

`N=Lambda-Lambda u u^T Lambda/a`.                                (3.4)

Let

`G=U_{-k}^T U_{-k}=I_2-u u^T`,
`W=U_{-k} G^(-1/2)`,
`M=G^(1/2) N G^(1/2)`.                                           (3.5)

Then `W^T W=I_2` and

`S=D_{-k}+W M W^T`.                                               (3.6)

The two key identities are exact:

`tilde c_i:=||W_{i,:}||^2=u_i^T G^(-1)u_i <= c_i/(1-c)`,           (3.7)

and

`boxed: det M=(1-c) d det(Lambda)/a`.                              (3.8)

For (3.8), `det G=1-c` and the matrix determinant lemma gives

`det N=det Lambda [1-u^T Lambda u/a]=det Lambda*d/a`.

This is deterministic coefficient algebra; it does not rotate the product variables.

## 4. New target-level compiler — diffuse rank-two scalar-Schur product rigidity

### Theorem 4.1 — `QFORM-RANK2-DIFFUSE-SCALAR-SCHUR-PRODUCT-RIGIDITY-v1`

In (3.1), suppose

`max_i c_i <=1/3`.                                                (4.1)

For any original coordinate `k` with `d_k!=0` and `a=A_kk!=0`, the full ambient quadratic form, with arbitrary cap-one independent input laws, obeys

`boxed:
 ||p_{X^T A X}||_infinity
 <=4 sqrt(2e) [(1-c_k)|a d_k det Lambda|]^(-1/4).`                 (4.2)

Equivalently, for every interval `J`,

`P{X^TAX in J}
 <=4 sqrt(2e) [(1-c_k)|a d_k det Lambda|]^(-1/4) |J|`.             (4.3)

The same inequality is therefore the geometric sublevel-set inequality on every arbitrary measurable unit product set `prod_i E_i`.

### Proof

Condition only on original coordinates outside the bank after the scalar pivot (in the present whole-matrix endpoint there are none; the same argument permits arbitrary already-conditioned outside affine terms). Complete the square only in original coordinate `X_k`. The residual coefficient is the Schur complement (3.3).

Under (4.1), `c_k<=1/3`, so by (3.7), for every remaining original coordinate,

`tilde c_i <= (1/3)/(1-1/3)=1/2`.                                (4.4)

Thus the prior proved B14 grouped-Schur/half-Riesz theorem applies to (3.6), with the entire diagonal `D_{-k}` and all affine terms retained as coordinatewise perturbations. It gives

`||p_Q||_infinity <=4 sqrt(2e)|a|^(-1/2)|det M|^(-1/4)`.

Substitute (3.8):

`|a|^(-1/2)|det M|^(-1/4)
 =[(1-c)|a d det Lambda|]^(-1/4)`,

which is (4.2). No small coefficient is discarded and no transformed random coordinate is treated as independent. QED.

### Corollary 4.2 — actual inequality for a bad slab

If an interval `J` has slab ratio

`rho=P{X^TAX in J}/|J|`,

then every eligible pivot satisfies

`boxed:
 (1-c_k)|A_kk d_k det Lambda|
 <=1024 e^2 rho^(-4).`                                           (4.5)

The numerical constant is

`1024 e^2 = 7566.393445304985...`.

## 5. Application to the designated fleet02/B13 exact endpoint

The partner's exact zero-disjoint-two-minor endpoint gives

`A=D+R`, `rank R<=2`.                                             (5.1)

If `rank R=2`, write `R=U Lambda U^T` as above. Since the target assumption is `s_3(A)>=1` and `rank R<=2`, the singular-value rank inequality gives

`1<=s_3(A)<=||D||_op=max_i |d_i|`.                                (5.2)

Choose `k` with `|d_k|>=1`.

There is now a quantitative exhaustive split for this rank-two endpoint:

* **Diffuse carrier:** `max_i c_i<=1/3`. If the selected actual diagonal pivot `a=A_kk` is nonzero, (4.5) and `1-c_k>=2/3`, `|d_k|>=1` give

  `boxed: |A_kk det Lambda|
          <=1536 e^2 rho^(-4)
          =11349.590167957478... rho^(-4).`                        (5.3)

  Thus a diverging slab-ratio sequence in this diffuse exact endpoint forces the product of the genuine physical pivot and the latent rank-two determinant to vanish at least as `rho^-4`.

* **Heavy carrier:** `max_i c_i>1/3`. Since `sum_i c_i=2`, fewer than six physical coordinates can satisfy `c_i>1/3`; hence the obstruction is localized to at most five named original-coordinate carrier hubs.

* **Degenerate branches:** `rank R<=1`, or the selected `A_kk=0`, remain unpaid. Small `|det Lambda|` is not erased as a perturbation; it is retained in (5.3).

This applies a completed fleet02/B13 result to an actual target inequality rather than merely restating its normal form.

## 6. What this does and does not prove

The exact extremal-product step is complete and optimizer-free. The exact diagonal-plus-rank-two endpoint is now reduced further: in its rank-two diffuse subbranch a high slab ratio forces the explicit invariant product (5.3), while the nondiffuse subbranch has at most five physical leverage hubs.

This does **not** prove full QFORM. The first unpaid implication is

`QFORM-DELTA0-RANK2-HEAVYHUB-OR-DEGENERATE-GLUE-v1`:

close the at-most-five-heavy-carrier branch and the `A_kk=0`/rank-`<=1`/tiny-`det Lambda` degeneracies by a product-preserving receiver, and then return to the partner's nonzero-two-minor four-hub twist branch. In particular no Frobenius/max-norm-small twist may simply be deleted on arbitrarily translated or fragmented supports.

No counterexample to QFORM was found in this run.

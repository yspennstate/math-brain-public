SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B13, 2026-09-24T06:32:11.331510Z.
attacking: convert the corrected finite-mixture extremal-product reduction into a quantitative geometric tail obstruction for the partner's exact finite-direction endpoint, without deleting coefficient-small diagonal curvature for free.

# fleet01/B13 — extremal product laws and finite-direction diagonal-tail obstruction

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T063211Z-fleet01-B13-auto11`  
Control consumed: owner control revision `2026-09-22.15` on fresh main.  
Execution context: `WITHOUT_VERIFIED_BRAIN`.  
Status: **NEW QUANTITATIVE SUPPORTING LEMMA / PARTNER RESULT APPLIED / FULL UNRESTRICTED QFORM OPEN / CONTINUITY OPEN**.

The full target is not claimed here. No post-rotation independence, centered-uniform extremality, common support diameter, uniform fragment count, pointwise law-uniform quadratic oscillatory decay, or perturbative deletion of a coefficient-small quadratic tail is used.

## 1. Correct extremal-product reduction: finite mixtures, with arbitrarily small witness loss

The useful reduction is equality of suprema, not an assertion that a global optimizer exists.

### Proposition 1 — `QFORM-EXTREMAL-PRODUCT-FINITE-MIXTURE-v2`

Let `K:R^n->[0,1]` be measurable. Then

`sup int K(x) prod_i f_i(x_i) dx`

over all probability densities `0<=f_i<=1` equals

`sup int_(prod_i E_i) K(x) dx`

over bounded finite-union measurable sets `E_i subset R` with `|E_i|=1`.

More precisely, for every admissible product density `(f_i)` and every `eps>0` there are bounded finite-union unit-measure sets `E_i` such that

`int_(prod E_i) K >= int K prod_i f_i - eps`.                         (1.1)

#### Proof

It is enough to approximate each one-dimensional factor by a finite convex mixture of unit-set indicators.

Fix one cap-one density `f` and `delta>0`. Choose `R` so that

`tau=int_{|x|>R} f(x) dx <delta/8`.

Let `I` be any bounded interval of length `tau` outside `[-R,R]` and set

`g=f 1_{[-R,R]}+1_I`.

Then `0<=g<=1`, `int g=1`, `g` has bounded support, and

`||f-g||_1 <=2 tau<delta/4`.                                         (1.2)

Choose a grid mesh `h=1/K` with integer `K` sufficiently large, and let `g_h` be the conditional expectation of `g` on the grid cells of length `h`. Since `g` is bounded and compactly supported,

`0<=g_h<=1`, `int g_h=1`, `||g_h-g||_1 ->0`.                       (1.3)

Only finitely many cell values are nonzero. Write them as `p_1,...,p_N`. Since every cell has measure `1/K`,

`sum_j p_j=K`.                                                       (1.4)

Thus `p=(p_j)` belongs to the finite hypersimplex

`{q in [0,1]^N: sum q_j=K}`.

Its extreme points are precisely the `0/1` vectors with exactly `K` ones, so finite-dimensional convexity gives

`p=sum_r theta_r v^(r)`, `theta_r>=0`, `sum_r theta_r=1`,             (1.5)

where each `v^(r)` has exactly `K` ones. If `E_r` is the union of the corresponding `K` grid cells, then `|E_r|=K/K=1` and

`g_h=sum_r theta_r 1_{E_r}`.                                         (1.6)

Taking the mesh sufficiently fine gives a finite mixture with `L^1` distance `<delta` from `f`.

Do this for all `n` marginals, with total `L^1` error below `eps`. The tensor-product telescoping inequality gives

`||prod_i f_i-prod_i g_i||_1 <=sum_i ||f_i-g_i||_1<eps`.             (1.7)

Tensoring the finite mixtures writes `prod_i g_i` as a finite convex combination of product indicators `1_{prod_i E_i}`. Therefore the average of the corresponding `K`-integrals is at least the original product-density integral minus `eps`; one component satisfies (1.1). The reverse inequality between the two suprema is immediate because unit-set indicators are admissible cap-one densities. `QED`

For the slab kernel `K=1_{x^T A x in J}`, a strict ratio `rho` therefore transfers, for every `delta>0`, to bounded finite-union unit sets with slab ratio at least `rho-delta`. There is no assertion of an attained global bathtub optimizer.

## 2. Completed designated-partner theorem actually used

The completed fleet02/B13 r40 report is source-pinned at

`yspennstate/math-open-problems@2af615c6d649e207191127733fc6dd180db14944`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B13/20260924T025738Z-fleet02-B13-QFORM-auto11/REPORT.md`.

I use its Theorem 5.1, `QFORM-FINITE-DIRECTION-FINITE-DIAGONAL-GROUPING-v1`, at exactly its stated no-affine scope:

Let

`B=D_0+U Lambda U^T`, `U^T U=I`,                                   (2.1)

let `C` be a finite set of named original-coordinate centers, assume that outside

`T=C union supp(D_0)`

the nonzero physical rows of `U` occupy at most `m` one-dimensional latent directions, and put

`N=|T|+m`.

If `B` has at least three eigenvalues of modulus at least one, then for every independent cap-one input vector

`||p_(X^T B X)||_infty <=250 e N(8+log N)`.                          (2.2)

The proof groups each exact physical direction before applying curvature. In the exact two-line endpoint of the partner's current rank-two analysis, `|C|<=10`, `m<=2`, so finite extra diagonal support `r` gives `N<=r+12`.

The new argument below does **not** pretend that small diagonal coefficients may be removed uniformly. Instead it records exactly how much product-set mass is spent by the removed diagonal tail.

## 3. New geometric theorem: finite-direction forms with an infinite-cardinality diagonal tail

The dimension `n` is finite in the original target, but the point is to obtain an estimate depending only on the number of diagonal coordinates above a chosen threshold, rather than on `n`.

### Theorem 2 — `QFORM-FINITE-DIRECTION-DIAGONAL-TAIL-MOMENT-v1`

Let

`A=D+U Lambda U^T`, `D=diag(d_1,...,d_n)`, `U^T U=I`,               (3.1)

be real symmetric and satisfy

`s_3(A)>=1`.                                                         (3.2)

Let `C subset [n]` be finite and suppose that all nonzero rows of `U` outside `C` lie in at most `m` one-dimensional latent subspaces.

Fix `0<kappa<1` and define

`S_kappa={i notin C: |d_i|>kappa}`, `r=|S_kappa|`,
`N=|C|+r+m`,                                                        (3.3)

and

`A_kappa=D_kappa+U Lambda U^T`,                                     (3.4)

where `D_kappa` retains every `d_i` on `C union S_kappa` and is zero elsewhere.

For bounded measurable sets `E_i subset R` with `|E_i|=1`, put `E=prod_i E_i` and

`R_kappa(x)=x^T(A-A_kappa)x
            =sum_{i notin C, |d_i|<=kappa} d_i x_i^2`,              (3.5)

`L_kappa(E)=int_E |R_kappa(x)| dx`.                                 (3.6)

Define

`H_kappa= [250 e N(8+log N)]/(1-kappa)`.                            (3.7)

Then for every interval `J`,

`boxed:
 |{x in E: x^T A x in J}|
 <= H_kappa |J| +2 sqrt(2 H_kappa L_kappa(E)).}`                    (3.8)

Consequently, writing the product-set slab ratio as

`rho_E=|{x in E:x^T A x in J}|/|J|`,                               (3.9)

one has the quantitative obstruction

`boxed:
 L_kappa(E)
 >= |J|^2 (rho_E-H_kappa)_+^2 /(8 H_kappa).}`                       (3.10)

In particular the easier-to-compute weighted second-moment tail satisfies

`sum_{i notin C, |d_i|<=kappa}|d_i| int_{E_i}x^2 dx
 >= |J|^2 (rho_E-H_kappa)_+^2 /(8 H_kappa).`                        (3.11)

#### Proof

The matrix removed in (3.4) is diagonal and has operator norm at most `kappa`:

`||A-A_kappa||_op<=kappa`.                                          (3.12)

By the singular-value Weyl inequality,

`s_3(A_kappa)>=s_3(A)-kappa>=1-kappa`.                              (3.13)

Hence the scaled matrix

`B=A_kappa/(1-kappa)`                                               (3.14)

has at least three eigenvalues of modulus at least one. Its diagonal part is supported in `C union S_kappa`, and outside this finite set the rows of `U` still occupy at most the same `m` directions. Apply the completed partner theorem (2.2) to `B`. Since

`X^T B X=(1-kappa)^(-1) X^T A_kappa X`,                             (3.15)

scalar density scaling gives

`||p_(X^T A_kappa X)||_infty
 <= [250 e N(8+log N)]/(1-kappa)
 =H_kappa`.                                                         (3.16)

Now give `X` the product-indicator law `prod_i 1_{E_i}`. Each `E_i` has measure one, so `E` itself has volume one and this is a probability law. Set

`Q=X^T A X`, `Q_kappa=X^T A_kappa X`, `R=R_kappa(X)`.               (3.17)

For every `s>0`, on the event `{Q in J, |R|<=s}` one has

`Q_kappa=Q-R in J+[-s,s]`.                                         (3.18)

Therefore, by Markov and (3.16),

`P(Q in J)
 <=P(|R|>s)+P(Q_kappa in J+[-s,s])`
` <=L_kappa(E)/s + H_kappa(|J|+2s)`.                               (3.19)

If `L_kappa(E)=0`, let `s downarrow0`. Otherwise choose

`s=sqrt(L_kappa(E)/(2H_kappa))`.                                   (3.20)

This gives (3.8). Rearranging (3.8) gives (3.10). Finally

`L_kappa(E)
 <=sum_{i notin C, |d_i|<=kappa}|d_i| int_{E_i}x^2 dx`              (3.21)

by the triangle inequality, so (3.11) follows. `QED`

### Why the theorem is correction-safe

The diagonal tail is never declared negligible merely because `|d_i|<=kappa`. Its actual contribution under the chosen product-set witness is retained through `L_kappa(E)`. Remote or fragmented support can make this quantity arbitrarily large, and (3.8) records that escape explicitly. This is precisely why no common support-diameter localization is inserted.

The only use of `|d_i|<=kappa` is deterministic spectral stability (3.13), not random-variable perturbation theory.

## 4. Actual application to the partner's exact two-line endpoint

In the exact two-projective-line endpoint of fleet02/B13 r40, take `|C|<=10` and `m<=2`. Choose `kappa=1/2` and let

`r=#{i notin C: |d_i|>1/2}`.                                      (4.1)

Then `N<=r+12` and Theorem 2 gives, with

`H_r=500 e (r+12)(8+log(r+12))`,                                  (4.2)

`boxed:
 |{x in E:x^T A x in J}|
 <=H_r |J|+2 sqrt(2 H_r L_{1/2}(E)).}`                             (4.3)

Equivalently,

`boxed:
 L_{1/2}(E)>=|J|^2 (rho_E-H_r)_+^2/(8H_r).}`                       (4.4)

If `rho_E>=2H_r`, this simplifies to

`L_{1/2}(E)>=rho_E^2 |J|^2/(32H_r)`.                               (4.5)

For `r=0`,

`H_0=500 e*12*(8+log 12)=171005.587315...`.                         (4.6)

Thus the partner's statement that a hard exact-line survivor must use distributed diagonal curvature can be sharpened: if only `r` coordinates have diagonal coefficient above `1/2`, then every high-ratio bounded product-set witness must pay the explicit **actual diagonal-tail first moment** (4.4). The escape is not merely cardinality; it is a quantitative coupling of diagonal coefficients with the geometry/location of the extremal product sets.

## 5. Transfer back to arbitrary cap-one product laws

Suppose the same matrix `A` in the exact finite-direction scope has an arbitrary cap-one product-law slab witness of ratio `rho`. Proposition 1 applied to the slab indicator says that for every `delta>0` there is a bounded finite-union unit-product set `E` with

`rho_E>=rho-delta`.                                                  (5.1)

Therefore Theorem 2 yields

`boxed:
 L_kappa(E)
 >= |J|^2 (rho-delta-H_kappa)_+^2/(8H_kappa).}`                    (5.2)

No moment assumption has been imposed on the original laws: the moment in (5.2) belongs only to the bounded finite-union extremal witness produced by the reduction.

This supplies the requested bridge from arbitrary bounded densities to a concrete geometric sublevel-set inequality after applying the completed partner theorem.

## 6. What is and is not paid

Proved in this run:

- rigorous optimizer-free finite-mixture reduction to bounded finite-union unit-product indicators, with arbitrary prescribed witness loss;
- a new exact geometric inequality (3.8) for the finite-direction skeleton with arbitrary many coefficient-small diagonal coordinates;
- a quantitative contrapositive (3.10)/(4.4) forcing actual diagonal-tail currency in every high-ratio product-set witness;
- an explicit application of the completed fleet02/B13 r40 finite-direction theorem.

Not proved:

- the rough `O(rho^-1/6)` two-strip matrix can be replaced by its central lines;
- the diagonal-tail moment in (3.10) is uniformly small;
- the full exact-rank-two pivot-degenerate branch;
- the unrestricted full-matrix QFORM conjecture or continuity.

The first unpaid implication is now

`QFORM-DIAGONAL-TAIL-MOMENT-TO-PRODUCT-RECEIVER-v1`:

> In the exact finite-direction survivor, either consume the forced quantity `L_kappa(E)` by a second product-preserving curvature mechanism, or show that the large-tail-moment regime produces enough same-sign diagonal smoothing to close the slab bound. In the rough two-strip survivor, retain the strip matrix exactly; Theorem 2 cannot be invoked by simply projecting rows to the central lines.

Corrections honored: pointwise quadratic oscillatory decay is not used; no rotation of random coordinates is used; projection density alone is not used for an indefinite pushforward; diagonal `pi` is not promoted to a universal constant; no uniform bounded-diameter or finite-fragment assertion is made; and coefficient-small quadratic tails are charged through their actual product-set contribution rather than silently discarded.

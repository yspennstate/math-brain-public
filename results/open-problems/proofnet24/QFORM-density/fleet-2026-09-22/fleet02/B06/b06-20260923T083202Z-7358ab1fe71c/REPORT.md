SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B06, 2026-09-23T08:32:02Z.
attacking: near-collinear shared-coefficient zero-anchor branch: use the residual transverse coefficient together with the third large direction before hyperbolic reciprocal payment.

# fleet02/B06 — weighted max-reciprocal receiver and diffuse third-direction payment

**Run:** `b06-20260923T083202Z-7358ab1fe71c`  
**Status:** `NEW SUPPORTING THEOREMS + PARTNER SPLICE + SOURCE-VALID ROUTE COUNTEREXAMPLE`; full QFORM remains `OPEN / NOT PROVED / NOT DISPROVED`.  
**Continuity:** proved only for the new max-reciprocal receiver and the explicit mixed-Fresnel family below; universal continuity remains open.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Sources and correction boundary


Completed inputs actually used:

1. fleet02/B06 weighted affine-fiber product-projection theorem, `yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5`: for two affine forms of an independent cap-one product source with coefficient-row area `Delta`, the joint density is at most `e/Delta`.
2. designated partner fleet03/B06 r29, canonical mathematics `yspennstate/math-open-problems@83e20dbeb976ade9553a5dbee5344faceb723441`, plus its r28 anchored currency source `yspennstate/math-open-problems@36cc5730f42c76c15fdc330dc4b47beec060b8fd`. In the zero-anchor two-hub chamber the full coefficient rows satisfy `A0 B0 > sqrt(127/800) G^2`; the r29 transverse receiver pays `sin(theta)>=1/4` by `<20.233/G` and leaves the near-collinear tube.
3. newest-Claude source `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `FOURIER_ROUTE_REPORT.md`, Theorem MF (mixed Fresnel): one genuine heavy original coordinate coupled to a spread leaf direction plus one spread quadratic direction yields `|t|^{-3/2}` with arbitrary linear tilts and diagonal leaf curvature retained.

## 2. New theorem: max-reciprocal weighted fiber receiver

### Theorem 2.1 — `QFORM-SHARED-COEFFICIENT-MAX-RECIPROCAL-v1`

Let `X,Y` be independent real random variables with densities at most one. Let `Omega` be independent of `(X,Y)`, and let

`U=U(Omega), V=V(Omega), R=R(Omega)`

be arbitrary measurable functions. Assume `(U,V)` has a joint density `g` satisfying

`||g||_infinity <= K < infinity`.

Then

`T = 2 X U + 2 Y V + R`

has a continuous density and

`boxed: ||p_T||_infinity <= 2 sqrt(K).`                              (2.1)

#### Proof

For almost every background point, `u!=0` and `v!=0`: a two-dimensional absolutely continuous law gives zero mass to either coordinate axis. Conditional on `Omega`, the variables `2uX` and `2vY` are independent with density caps `1/(2|u|)` and `1/(2|v|)`. Young's inequality in the `L^infinity*L^1` form, used in the better direction, gives

`||p_(2uX+2vY | Omega)||_infinity
 <= min{1/(2|u|),1/(2|v|)}
 = 1/[2 max(|u|,|v|)].`                                             (2.2)

The shift `R(Omega)` is harmless. Therefore

`||p_T||_infinity <= (1/2) E [max(|U|,|V|)^(-1)].`                   (2.3)

Use layer cake. For `s>0`,

`P(max(|U|,|V|)^(-1)>s)
 = P(|U|<1/s, |V|<1/s)
 <= min(1,4K/s^2).`                                                  (2.4)

Splitting at `s=2 sqrt(K)`,

`E max(|U|,|V|)^(-1)
 <= int_0^infinity min(1,4K/s^2) ds
 = 4 sqrt(K).`                                                       (2.5)

This proves (2.1). For continuity: for a.e. `(u,v)` the conditional density is the convolution of two `L^1` densities, hence continuous; (2.2)-(2.5) give an integrable dominating envelope, so dominated convergence passes continuity through the background average. QED.

### Corollary 2.2 — shared affine coefficient rows

Let `Z` have independent cap-one coordinates and

`U=a.Z+u0, V=b.Z+v0`,
`A=||a||, B=||b||`,
`Delta=sqrt(A^2 B^2-(a.b)^2)>0`.

The completed weighted affine-fiber Brascamp--Lieb theorem gives

`||p_(U,V)||_infinity <= e/Delta`.

Therefore, for genuine independent cap-one anchors `X,Y` and arbitrary `R(Z)`,

`boxed: ||p_(2XU+2YV+R(Z))||_infinity <= 2 sqrt(e/Delta).`           (2.6)

This is a second weighted replacement for the invalid fiber supremum. It consumes the entire two-dimensional coefficient density before paying the reciprocal singularity. It is complementary to the preceding logarithmic rectangle receiver: (2.6) is better at moderate angle, while the logarithmic receiver is better extremely near collinearity.

## 3. Designated-partner splice: improved quantitative transverse gate

In fleet03/B06 r28-r29's zero-anchor two-hub chamber, let the complete coefficient rows have norms `A0,B0`, angle `theta`, and area `Delta0=A0 B0 sin(theta)`. The partner currency gives

`A0 B0 > sqrt(127/800) G^2`.                                        (3.1)

On the partner's existing transverse gate `sin(theta)>=1/4`,

`Delta0 > (1/4) sqrt(127/800) G^2`.                                  (3.2)

Applying (2.6) gives the actual inequality

`||p_Q||_infinity
 < 4 sqrt(e) (127/800)^(-1/4) G^(-1)
 = 10.4478949866... / G.`                                            (3.3)

This improves the partner r29 `<20.233/G` constant on the same gate and also slightly improves the preceding B06 logarithmic receiver at `sin(theta)=1/4` (`11.1776/G`). No disjoint support between the two coefficient rows is assumed.

The first unpaid state is still the quantitative near-collinear tube: (2.6) diverges like `Delta0^(-1/2)` and the earlier receiver like `log(A0B0/Delta0)`. A third large direction must be spent before that divergence.

## 4. New deterministic near-collinear spectral budget

### Lemma 4.1 — `QFORM-NEAR-COLLINEAR-THIRD-CURVATURE-BUDGET-v1`

Consider the double-null physical-anchor form

`A = [[0,0,a^T], [0,0,b^T], [a,b,C]]`,                              (4.1)

and decompose

`b = lambda a + epsilon`, `epsilon perp a`.                          (4.2)

If `A` has at least three eigenvalues of modulus at least one, then

`boxed: ||epsilon|| + ||C||op >= 1.`                                (4.3)

#### Proof

Let

`H = [[0,0,a^T], [0,0,lambda a^T], [a,lambda a,0]]`.                 (4.4)

Its anchor-to-background cross block has row rank one, so the symmetric bipartite matrix `H` has rank at most two. Because `A` is symmetric and has three eigenvalues of modulus at least one, its third singular value obeys `s_3(A)>=1`. Eckart--Young therefore gives

`1 <= s_3(A) <= ||A-H||op`.                                         (4.5)

But

`A-H = [[0,0,0], [0,0,epsilon^T], [0,epsilon,C]]`,                  (4.6)

and the residual star `[[0,epsilon^T],[epsilon,0]]` has operator norm exactly `||epsilon||`. Hence

`||A-H||op <= ||epsilon||+||C||op`,                                  (4.7)

proving (4.3). QED.

Thus if `||epsilon||<=1/2`, the background block itself has an eigenvalue of modulus at least `1/2`; if `||epsilon||>=1/2`, the residual transverse star carries operator norm at least `1/2`. This is a deterministic third-direction currency with no claim of a large physical coefficient.

The remaining difficulty is important: an arbitrary `C` with large operator norm need not be diagonal plus one spread rank-one term in the original coordinates, and a small `||epsilon||` is not a small random perturbation under arbitrary unbounded product laws. So (4.3) is not yet a full receiver.

## 5. Newest-Claude Theorem MF pays a genuine diffuse near-collinear target family

Theorem MF from the pinned newest-Claude package is applied here at a real target-level inequality, not merely cited.

Let `N,M>=2`, take flat unit vectors

`u=(N^(-1/2),...,N^(-1/2)) in R^N`,
`r=(M^(-1/2),...,M^(-1/2)) in R^M`,

on disjoint ORIGINAL-coordinate banks. Let

`U=u.Z`, `W=r.T`,

where all coordinates of `X,Y,Z,T` are independent and have densities at most one. For arbitrary real `lambda,delta`, consider

`Q_(lambda,delta) = 2 X U + 2 Y (lambda U + delta W) + W^2.`          (5.1)

### 5.1 It is an exact QFORM target for every `lambda,delta`

On the invariant four-dimensional span `(X,Y,U,W)`, the matrix is

`[[0,0,1,0],
  [0,0,lambda,delta],
  [1,lambda,0,0],
  [0,delta,0,1]].`                                                    (5.2)

The compression to `(X,U,W)` is

`[[0,1,0],[1,0,0],[0,0,1]]`,                                        (5.3)

with eigenvalues `{1,1,-1}`. Cauchy interlacing for (5.2) therefore forces at least two eigenvalues `>=1` and one eigenvalue `<=-1`. The orthogonal complements of the two diffuse banks are kernel directions. Hence the full original-coordinate matrix has at least three eigenvalues of modulus at least one for every `lambda,delta`.

### 5.2 Uniform density bound independent of the near-collinear angle

Condition on the ORIGINAL anchor `Y=y`. The remaining form is

`2 X U + W^2 + 2y(lambda U+delta W)`.                                (5.4)

Apply newest-Claude Theorem MF with heavy coordinate `H={X}`, leaf block the two original diffuse banks, cross column `u`, rank-one quadratic direction `r`, and diagonal leaf part zero. Its Gram matrix is exactly `Gamma=I_2`, and each normalized leaf leverage is `1/N` or `1/M`, hence at most `1/2`. The `y`-dependent term in (5.4) is only an arbitrary linear tilt, which Theorem MF explicitly retains.

Therefore, uniformly in `y,lambda,delta,N,M` and in all cap-one input laws,

`|phi_(Q|Y=y)(t)| <= (4 pi)^(3/2) / [2 |t|^(3/2)].`                 (5.5)

Averaging over `Y` preserves this bound. Integrating `min(1,B|t|^(-3/2))`, `B=(4pi)^(3/2)/2`, gives

`boxed: ||p_Q||_infinity
 <= 12 * 2^(-2/3)
 = 7.5595262994... .`                                                (5.6)

The same integrable characteristic-function envelope gives a continuous density in this family.

This is exactly the mechanism needed in the near-collinear debt: the third direction is consumed jointly with the dominant star **before** reciprocal hyperbolic curvature is paid. Note that the bound is independent of `delta`; it remains finite as the two anchor coefficient rows become exactly collinear.

## 6. Source-valid route counterexample: no large physical third-direction coefficient

Take, for example, `lambda=1` and any fixed `|delta|<=1` in (5.1), then send `N,M->infinity`. Every physical star coefficient is `O(N^(-1/2))` or `O(M^(-1/2))`, and every entry of the diffuse rank-one square block `r r^T` (including its physical diagonals) is `1/M`. Thus

`max_{i,j} |A_ij| -> 0`                                              (6.1)

while the matrix still has three eigenvalues of modulus at least one by Section 5.1.

So the structural statement

> a near-collinear shared-coefficient survivor plus the third large eigenvalue must expose one dimension-free physical coefficient/diagonal/edge

is false, even inside the exact target. This is **not** a counterexample to QFORM: Theorem MF gives the uniform bound (5.6). The repair is to aggregate the diffuse star and diffuse third square at the product-law level.

This strengthens the lesson of the earlier single-edge counterexamples: even the *third* spectral direction can be completely diffuse in physical coordinates, so the unresolved proof must aggregate before inverting.

## 7. First unpaid implication after this run

`QFORM-NEAR-COLLINEAR-ARBITRARY-BACKGROUND-RECEIVER-v1`:

Starting from (4.1)-(4.3) in the partner r29 near-collinear tube, retain arbitrary same-bank curvature `C`, arbitrary second-anchor coupling, and every complementary spectral component. Prove one of the following without selecting a good physical coefficient:

1. if `||epsilon||` carries the third-direction budget, a product-preserving two-bank/hub receiver consumes it jointly with the dominant star; or
2. if `||C||op` carries the budget, replace the special `diagonal + spread rank-one` leaf structure used by Theorem MF with an aggregate receiver valid for arbitrary `C`; or
3. route quantitatively into an already-paid physical-pair, fractional-volume, ridge, or grouped-bank exit.

The family (5.1) proves that a uniformly large physical third coefficient cannot be the bridge. Theorem MF proves that a diffuse third direction is nevertheless payable when its leaf curvature has the compatible rank-one-plus-diagonal structure. The missing step is the arbitrary-background extension, not the near-collinear geometry itself.

**Independent review:** not yet performed. Full QFORM and universal continuity remain open.

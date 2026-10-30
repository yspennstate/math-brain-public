SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B13, 2026-09-23T22:04:29Z.
attacking: convert the completed arbitrary-self two-hub Fourier receiver into a purely physical five-coordinate slab inequality, then specialize it exactly to diagonal-plus-rank-two carriers and use the fleet04/B13 diffuse slab dichotomy on the resulting geometry.

# fleet03/B13 r35 — physical two-hub / three-leaf transverse certificate

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T220429Z-fleet03-B13-qform-r35`  
Execution: `WITHOUT_VERIFIED_BRAIN`.  
Status: **new supporting theorem proved; full QFORM OPEN / NOT PROVED / NOT DISPROVED; global continuity separately OPEN.**

## 1. Source-pinned inputs actually used

1. **Two hubs with arbitrary self-interaction and one transverse square**, complete proof:
   `yspennstate/math-open-problems@237654c8819536e335afb91380290f5d833e2716`,
   `proofnet24/QFORM-density/interactive/20260923T190527Z-two-hubs-arbitrary-self/REPORT.md`.
   If `H in R^2` is independent of `Z=(Y1,Y2,V)`, the joint hub density is at most one, the joint light density is at most `M`, and
   `Q=R(H)+2 H.Y + lambda V^2 + 2 V G(Y)+F(Y)`, then Q has a continuous C0 density and
   `||p_Q||_infty < 16 M^(2/5) |lambda|^(-1/5)`.
   No independence among `(Y1,Y2,V)` is required.

2. **fleet04/B13 optimizer-free slab transfer and diffuse exact-rank-two dichotomy**, complete proof:
   `yspennstate/math-open-problems@d1764f29884bf14ce505d36668105edfcaf8315e`,
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B13/20260923T201653Z-fleet04-B13-extremal-slab-dichotomy-r1/REPORT.md`.
   In the exact endpoint
   `A=D+U Lambda U^T`, `U^TU=I_2`, `max_i ||u_i||^2 <=1/3`, `s_3(A)>=1`, choose k with `|d_k|>=1`. For slab ratio rho,
   `|A_kk det Lambda| <= 1536 e^2 rho^(-4)`,
   hence with `H0=sqrt(1536 e^2)=106.53445530886934`, either
   `|A_kk| <= H0 rho^(-2)`
   or the rank-two carrier is within `10.321552950446426 rho^(-1)` in operator norm of symmetric rank at most one.
   The same report proves the optimizer-free product-set supremum identity; no interval optimizer is assumed.

3. **Exact witnesswise bathtub purification**, fleet01/B13 handoff source:
   `yspennstate/math-open-problems@faabe6543fe023941b6965c2d9808c5d9186d8e5`,
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B13/20260923T213043Z-fleet01-B13-qform-auto11/REPORT.md`.
   For a bounded nonnegative kernel, successive one-coordinate bathtub replacement produces unit-measure indicators without decreasing the objective. I use this only as a product-law interpretation; the main receiver below already works directly for arbitrary cap-one product densities.

## 2. Main theorem: a physical five-coordinate receiver

### Theorem `QFORM-PHYSICAL-2HUB-3LEAF-TRANSVERSE-v1`

Let A be any real symmetric n x n matrix, with no rank or sign assumption. Let X have independent real coordinates with densities `0<=f_i<=1`. Select two distinct **physical** hub indices
`H={h1,h2}` and three distinct physical leaf indices `L={r,s,t}`, disjoint from H. Put

`W=A[H,L]`  (a 2 x 3 physical cross block),
`B=A[L,L]`.

Assume `rank W=2`. Let `nu in R^3` be either unit vector spanning `ker W`, and define

`Gamma(H,L) = det(W W^T) * |nu^T B nu|`.

If `Gamma(H,L)>0`, then the full ambient quadratic form
`Q=X^T A X` has a continuous density, vanishing at infinity, and

`boxed: ||p_Q||_infty < 16 Gamma(H,L)^(-1/5).`

Consequently every interval J satisfies

`boxed: P{Q in J}/|J| < 16 Gamma(H,L)^(-1/5).`

Equivalently, if a slab has ratio rho, then every such physical five-coordinate certificate obeys

`boxed: Gamma(H,L) < (16/rho)^5 = 1048576 rho^(-5).`

The statement remains valid with arbitrary affine terms added to Q.

### Proof

Condition on every original coordinate outside the five selected coordinates. This preserves independence and the cap-one densities of the five untouched physical coordinates. All interactions with conditioned coordinates become affine terms, so it is enough to prove a bound uniform in those affine coefficients.

Write the two hub variables as `h in R^2` and the three leaf variables as `x in R^3`. The conditional polynomial is

`q(h,x)=h^T C h + 2 h^T W x + x^T B x + ell_H.h + ell_L.x + c`,

with completely arbitrary symmetric `C`, arbitrary affine vectors, and the same W,B as above.

Because `rank W=2`, let `nu` be the unit kernel vector and define the linear change of light variables

`(y1,y2,v)=T x`,  `T = [ row_1(W); row_2(W); nu^T ]`.

The two rows of W are perpendicular to nu. Hence

`|det T|^2 = det(T T^T)=det(W W^T)`, so
`|det T|=sqrt(det(W W^T))`.

The original three leaf coordinates have a joint density at most one. After this invertible linear change, the joint density of `(Y1,Y2,V)` is therefore at most

`M = 1/sqrt(det(W W^T))`.

No independence of Y1,Y2,V is asserted or needed.

At fixed y, varying v changes x exactly in the direction nu, because `T nu=(0,0,1)`. Therefore the coefficient of `v^2` in `x^T Bx` is

`lambda = nu^T B nu`.

Every quadratic/affine function of `(y,v)` can be written uniquely in the form

`lambda v^2 + 2 v G(y)+F(y)`

with G affine and F quadratic (and arbitrary affine/constant pieces absorbed). Likewise all hub self-quadratic and hub-affine terms are an arbitrary function R(h). The hub-to-leaf term is exactly `2h.y` by the definition y=Wx. Thus the conditional polynomial is precisely in the scope of the source-pinned two-hub theorem:

`q=R(h)+2h.y+lambda v^2+2vG(y)+F(y)`.

The two original hub coordinates are independent of the three original leaf coordinates and have joint density at most one. The theorem therefore gives, uniformly in every conditioned outside configuration,

`||p_{q|outside}||_infty < 16 M^(2/5)|lambda|^(-1/5)`
`=16 [det(W W^T)|nu^T Bnu|]^(-1/5)`.

A mixture of these conditional densities gives a density of the full Q with the same cap. Each conditional density is continuous and vanishes at infinity, and the uniform cap provides dominated convergence, so the mixed density is also continuous and vanishes at infinity. This proves the theorem.

**Scope checks.** No rotation of the independent variables is used to claim independence: T is used only to compute the joint-density Jacobian of three already independent physical leaves, while the analytic receiver explicitly accepts dependent transformed light coordinates. No moment, support, log-concavity, Gaussianity, connectedness, or bounded-fragment hypothesis appears. Arbitrary same-side curvature, outside curvature, and affine terms are retained.

## 3. Exact diagonal-plus-rank-two specialization

Now assume

`A=D+U Lambda U^T`, `U^T U=I_2`,

with Lambda nonsingular symmetric 2 x 2. Write `u_i^T` for the rows of U and

`q_ab = det(u_a,u_b)^2 >=0`.

Take a physical hub pair `H={i,j}` and a disjoint leaf triple `L={r,s,t}`. Put

`S_L = q_rs+q_rt+q_st`.

Assume `q_ij>0` and `S_L>0`. Then `U_H` is invertible and `U_L` has rank two, so

`W=A[H,L]=U_H Lambda U_L^T`

has rank two. Cauchy--Binet gives

`det(W W^T)=q_ij (det Lambda)^2 S_L`.          (3.1)

A cofactor kernel vector of `U_L^T` is

`c_L=(det(u_s,u_t), -det(u_r,u_t), det(u_r,u_s))`,

whose squared norm is S_L. Since multiplication by the invertible matrix `U_H Lambda` does not change the kernel,
`nu=c_L/sqrt(S_L)` spans `ker W`. Moreover `U_L^T nu=0`, hence the rank-two carrier disappears exactly in the transverse leaf direction:

`nu^T B nu = nu^T D_L nu`
`=(d_r q_st+d_s q_rt+d_t q_rs)/S_L`.          (3.2)

Multiplying (3.1) and (3.2) cancels S_L. The five-coordinate theorem yields the explicit physical inequality

`boxed:
 ||p_Q||_infty
 < 16 [ q_ij (det Lambda)^2
        |d_r q_st+d_s q_rt+d_t q_rs| ]^(-1/5).`

Therefore every slab ratio rho forces, for all pair/triple choices with the stated nondegeneracy,

`boxed:
 q_ij (det Lambda)^2
 |d_r q_st+d_s q_rt+d_t q_rs|
 < 1048576 rho^(-5).`                         (3.3)

This is denominator-free: there is no inversion of a selected small minor. It exposes exactly the remaining cancellation currency in the diffuse rank-two endpoint.

## 4. Applying the completed fleet04/B13 result to an actual inequality

Assume the fleet04/B13 diffuse exact-rank-two chamber:

`max_i c_i<=1/3`, `c_i=||u_i||^2`, `s_3(A)>=1`.

Choose k as in fleet04/B13, with `|d_k|>=1`, and put `a_k=A_kk`, `R=U Lambda U^T`.

### 4.1 Near-null partner branch forces a large physical star

The partner theorem gives the actual slab alternative

`|a_k| <= H0 rho^(-2)`,  `H0=sqrt(1536 e^2)=106.53445530886934`,

unless the carrier is already `10.321552950446426 rho^(-1)`-close to rank one.

In the near-null branch, write `r_kk=u_k^T Lambda u_k=a_k-d_k`. Since `U^TU=I`,

`sum_j R_kj^2 = (R^2)_kk = u_k^T Lambda^2 u_k`.

Cauchy--Schwarz in coefficient space gives

`r_kk^2 <= c_k u_k^T Lambda^2 u_k`.

Therefore the **off-diagonal physical star** obeys

`sum_{j!=k} A_kj^2
 = u_k^T Lambda^2u_k-r_kk^2
 >= ((1-c_k)/c_k) r_kk^2`.

Since `|r_kk|>=|d_k|-|a_k|`,

`boxed:
 ||A[k,k^c]||_2
 >= sqrt((1-c_k)/c_k)
     (|d_k|-H0 rho^(-2))_+.`                 (4.1)

Using `c_k<=1/3` and `|d_k|>=1`,

`boxed:
 ||A[k,k^c]||_2
 >= sqrt(2) (1-H0 rho^(-2))_+.`              (4.2)

Thus the partner's near-null cancellation is not a weakly coupled pivot: at large rho it necessarily carries an order-one original-coordinate star. This is a product-coordinate invariant statement, not a rotated-coordinate surrogate.

### 4.2 A noncancelling five-coordinate subbranch is paid at rho^(-5/4) carrier scale

Take any hub pair `{i,j}` disjoint from a leaf triple `{k,r,s}` and suppose

`q_ij >= eta >0`, `q_rs>=zeta>0`,

and the signed transverse diagonal currency does not cancel by more than a factor theta:

`|d_k q_rs+d_r q_ks+d_s q_kr|
 >= theta |d_k| q_rs`, `theta>0`.

Equation (3.3), with `|d_k|>=1`, gives

`|det Lambda|
 < 1024 (eta theta zeta)^(-1/2) rho^(-5/2).`  (4.3)

If lambda_1,lambda_2 are the two eigenvalues of Lambda, then

`boxed:
 min(|lambda_1|,|lambda_2|)
 < 32 (eta theta zeta)^(-1/4) rho^(-5/4).`    (4.4)

So in every quantitatively noncancelling physical five-coordinate chamber, the fleet04 diffuse rank-two survivor is forced toward symmetric rank one at the stronger `rho^(-5/4)` rate. The only way this local receiver can fail to improve the partner's general `O(rho^-1)` rank-one alternative is through genuinely diffuse individual pair volumes and/or systematic signed cancellation of the transverse diagonal currency. That is precisely a grouped-bank rather than a single-minor obstruction.

No claim is made that diffuse leverage alone gives dimension-free eta or zeta; doing so would revive the forbidden small-minor selection step.

## 5. Product-indicator interpretation

For the slab kernel `K=1_{x^TAx in J}`, the exact/optimizer-free bathtub results imply that the supremum over all cap-one mass-one product densities equals the supremum over product indicators `prod_i 1_{E_i}`, `|E_i|=1`; strict witnesses can moreover be approximated by bounded finite unions without any uniform diameter or fragment-count conclusion.

Hence the theorem in Section 2 is equivalently the geometric sublevel-set inequality

`| {x in prod_i E_i : x^T A x in J} |
 < 16 Gamma(H,L)^(-1/5) |J|`

for every measurable unit product set. This is the requested product-extreme geometric form; no interval or centered-uniform extremizer is assumed.

## 6. Deterministic checks

A local numerical algebra check sampled 5000 random Parseval frames U, nonsingular signed diagonal Lambda, random diagonal D, and random disjoint 2-hub/3-leaf selections. It verified

`det(WW^T)|nu^T Bnu|
 =q_ij(det Lambda)^2 |d_r q_st+d_s q_rt+d_t q_rs|`

to maximum normalized floating error `2.57e-13`.

Exact constants used:

`16^5 = 1048576`,
`16^(5/2)=1024`,
`H0=sqrt(1536 e^2)=106.53445530886934`.

These computations are sanity checks only; the proof above is algebraic.

## 7. What this does and does not solve

This result creates a new **physical**, translation-stable, support-free certificate: every high-ratio witness must make every 2-hub/3-leaf transverse invariant tiny. In the exact diffuse rank-two endpoint the invariant collapses to the weighted pair-volume expression (3.3), exposing a concrete signed-cancellation/grouped-volume frontier rather than an unspecified small quadratic remainder.

The full QFORM conjecture remains **OPEN**. No valid counterexample is produced. The new first missing implication for B13 is:

`QFORM-GROUPED-WEIGHTED-TRANSVERSE-CANCELLATION-v1`:
aggregate the weighted currencies
`q_ij |d_r q_st+d_s q_rt+d_t q_rs|`
over diffuse rank-two pair laws without paying the number of physical pairs, and route the systematic-cancellation case to the existing finite-hub / grouped-crossing receivers. Individual q_ij or q_rs may be arbitrarily small in high dimension, so a max-minor argument is not acceptable.

The theorem in Section 2 **does** prove continuity and C0 decay in its sufficient five-coordinate branch. Global continuity under only the original spectral hypothesis remains **OPEN**.

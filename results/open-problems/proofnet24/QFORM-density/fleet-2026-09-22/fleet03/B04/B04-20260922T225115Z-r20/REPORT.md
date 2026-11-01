SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B04, 2026-09-22T22:51:15Z.
attacking: a rank-two-or-higher one-clean-side bilinear-bank L-infinity estimate by multidimensional projection-density rearrangement, then the critical two-cross-direction square-assisted branch.

# fleet03/B04 r20 — multidimensional bilinear-bank rearrangement and critical two-direction square splice

Programme `QFORM-DENSITY-3EIG-20260922`; assignment `Product Fourier rearrangement`; run `B04-20260922T225115Z-r20`. Execution `WITHOUT_VERIFIED_BRAIN`. Outcome `ESSENTIAL_STEP_APPLIED / SUPPORTING THEOREMS PROVED / FULL QFORM OPEN`.

## 1. Scope and source-pinned inputs

All variables below are built from original independent real coordinates with densities <=1. No moments, Gaussianity, log-concavity, compact/connected support, post-rotation independence, arbitrary-joint coarea, positive conditional-density moment, or law-uniform pointwise Fresnel decay is used.

This changes mechanism from r19. Instead of reducing to one singular direction and paying a one-dimensional inverse moment, it keeps r>=2 singular directions jointly, bounds the r-dimensional projection density of the original product law, and applies a radial decreasing rearrangement before any reciprocal local coefficient appears.

Completed peer inputs actually used:

1. fleet02/B06 `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1`, source `yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B06/b06-20260922T155426Z-9fd56fa68a65/REPORT.md`: if R has r orthonormal columns and X is an original-coordinate cap-one product vector, R^T X has r-dimensional density <=exp(r/2).

2. fleet02/B04 scalar bank projection bound, source `yspennstate/math-open-problems@07305f53ba9b8a1d3e6e79f8c851f415f007d4a7`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B04/B04-20260922T181702Z-dac07509/REPORT.md`:

`||p_(c^T Y)||_infinity <= sqrt(2)/||c||_2`.                  (1.1)

The designated fleet04/B04 handoff directory was absent on fresh lookup, so no designated-partner result is fabricated. The completed compatible peer results above are applied at equation level.

The fresh fleet02/B04 result `QFORM-HYPERBOLIC-TWOSIDED-HALFRIESZ-UNIFORM-FALSE-v1` is also respected: arbitrary two-sided contamination may collapse a hyperbolic packet to a square and make a standalone half-Riesz expectation diverge. Accordingly, the theorem below retains an explicit one-quadratically-clean-side hypothesis.

## 2. Radial bathtub lemma

Let `v_r=pi^(r/2)/Gamma(r/2+1)` be the volume of the Euclidean unit ball in R^r.

**Lemma 2.1.** If r>=2 and an R^r-valued random vector T has density rho<=K, then

`sup_z E ||T-z||_2^(-1) <= [r/(r-1)] v_r^(1/r) K^(1/r)`.      (2.1)

**Proof.** For fixed z, `||x-z||^-1` is radially decreasing. The bathtub/rearrangement principle maximizes its integral among probability densities <=K by `K 1_{B(z,R)}` with `K v_r R^r=1`. Hence

`E||T-z||^-1 <= K r v_r integral_0^R s^(r-2) ds`
` = K r v_r R^(r-1)/(r-1)`
` = [r/(r-1)]v_r^(1/r)K^(1/r)`. QED.                     (2.2)

The r>=2 threshold is essential for this proof: in one dimension the inverse-distance integral is logarithmically divergent.

## 3. Rank-r one-clean-side bilinear bank

Let I,J be disjoint original-coordinate banks, with product vectors X and Y, and let W be any further independent original-coordinate variables. Let B be a real |I| x |J| matrix. Fix

`2 <= r <= rank(B)`                                           (3.1)

and let `sigma_1>=...>=sigma_r>0` be the selected top r singular values. Let F(X,W) be arbitrary measurable and b(W) an arbitrary measurable J-vector. Define

`H = F(X,W) + (2 B^T X + b(W))^T Y`.                           (3.2)

The X side may contain arbitrary quadratic/nonlinear contamination. The Y side is quadratically clean after conditioning on (X,W).

Set

`Gamma_r = sqrt(e/2) [r/(r-1)] v_r^(1/r)`.                    (3.3)

### Theorem 3.1 — QFORM-RANKR-BILINEAR-BANK-LINF-v1

H is absolutely continuous and

`||p_H||_infinity <= Gamma_r (prod_{j=1}^r sigma_j)^(-1/r)`.  (3.4)

For r=2,

`Gamma_2=sqrt(2 pi e)=4.132731354122493...`,                  (3.5)

so

`||p_H||_infinity <= sqrt(2 pi e)(sigma_1 sigma_2)^(-1/2)`.   (3.6)

**Proof.** Condition on `(X,W)=(x,w)` and set `c(x,w)=2B^T x+b(w)`. Whenever c is nonzero, (1.1) gives

`||p_(H|x,w)||_infinity <= sqrt(2)/||c(x,w)||`.                (3.7)

Take an SVD. Let U_r,V_r correspond to sigma_1,...,sigma_r. Then

`||c(x,w)|| >= ||V_r^T c(x,w)||`
` = ||2 diag(sigma_1,...,sigma_r) U_r^T x + V_r^T b(w)||`.     (3.8)

By the completed fleet02/B06 theorem, `Z=U_r^T X` has r-dimensional density <=exp(r/2). Therefore

`L_w=2 diag(sigma_1,...,sigma_r)Z+V_r^T b(w)`                 (3.9)

has density cap

`K_r = exp(r/2)/(2^r prod sigma_j)`.                           (3.10)

Thus `P(L_w=0)=0`, so the exceptional coefficient-zero set is null. Lemma 2.1 gives

`E_X ||c(X,w)||^-1 <= E||L_w||^-1`
` <= [r/(r-1)]v_r^(1/r) [sqrt(e)/2](prod sigma_j)^(-1/r)`.    (3.11)

Average (3.7) in X and then W. The factor sqrt(2) converts sqrt(e)/2 into sqrt(e/2), giving (3.4). A mixture of the a.e. absolutely continuous conditional laws is absolutely continuous. QED.

This strengthens the completed one-clean-side finite-Lp theorem whenever two or more singular directions are retained: it reaches L-infinity and pays the geometric mean of the retained singular values, not a reciprocal individual matrix entry.

## 4. Exact half-Riesz consequence and overlap-safe scalar square

**Lemma 4.1.** If a real random variable T has density <=M, then

`sup_t E|T-t|^(-1/2) <= 2 sqrt(2M)`.                            (4.1)

**Proof.** Rearrangement fills the centered interval of length 1/M at height M:

`2M integral_0^(1/(2M)) s^(-1/2) ds = 2sqrt(2M)`. QED.       (4.2)

Let Z_0 be one additional original independent coordinate with density <=1, let a!=0, and let `m=m(X,Y,W)` be arbitrary measurable. Put

`Q = a[Z_0+m(X,Y,W)]^2 + H`.                                  (4.3)

The square shift may reuse both active banks.

### Theorem 4.2 — QFORM-SQUARE-RANKR-CLEANBANK-LINF-v1

`||p_Q||_infinity <= 2 sqrt(2 Gamma_r)|a|^(-1/2)
                     (prod sigma_j)^(-1/(2r)).`                (4.4)

For r=2,

`||p_Q||_infinity <= 2sqrt(2)(2 pi e)^(1/4)|a|^(-1/2)
                     (sigma_1 sigma_2)^(-1/4)`,                (4.5)

with coefficient

`2sqrt(2)(2 pi e)^(1/4)=5.749943550416816...`.                 (4.6)

If `sigma_1,sigma_2>=sigma`, then

`||p_Q||_infinity <= 5.749943550416816/sqrt(|a| sigma)`.       (4.7)

**Proof.** Conditional on (X,Y,W), the translated scalar square has density envelope

`p_(a[Z_0+m]^2)(u) <= |a|^(-1/2)|u|^(-1/2)`                   (4.8)

on its allowed half-line. Removing the indicator only enlarges the bound, hence

`p_Q(t) <= |a|^(-1/2) E|t-H|^(-1/2)`.                         (4.9)

Apply Lemma 4.1 and Theorem 3.1. QED.

This pays a previously critical endpoint. The completed fleet02/B04 unconditional weighted-determinant square theorem at q=2 needs strictly more than two quantitatively large residual cross singular directions; at two directions its absolute weighted Fourier envelope is logarithmically critical. Theorem 4.2 closes those two directions whenever one residual side is quadratically clean, without assuming the completed-square shift is independent of the residual variables.

## 5. Explicit genuinely rotated indefinite target

Let

`u=(1,1)/sqrt(2)`,
`H2=(1/sqrt(2))[[1,1],[1,-1]]`,
`B=3H2`,
`C=(1/2)[[1,1],[1,-1]]`.                                      (5.1)

For independent original coordinates `(z,x_1,x_2,y_1,y_2)`, define

`Q_* = 2[z+(1/4)u^T x]^2 + x^T Cx + 2x^TBy`.                  (5.2)

Its physical matrix is

`A_*=[[2,1/(2sqrt2),1/(2sqrt2),0,0],`
`     [1/(2sqrt2),9/16,9/16,3/sqrt2,3/sqrt2],`
`     [1/(2sqrt2),9/16,-7/16,3/sqrt2,-3/sqrt2],`
`     [0,3/sqrt2,3/sqrt2,0,0],`
`     [0,3/sqrt2,-3/sqrt2,0,0]].`                              (5.3)

Both singular values of B equal 3. The x side carries nonzero quadratic leakage; the y side is clean; the square overlaps x.

For a rigorous target certificate, let

`S0=[[0,B],[B^T,0]]`.                                          (5.4)

All singular values of S0 equal 3. Let `S=S0+diag(C,0_2)`. Since `||C||=1/sqrt(2)`,

`s_min(S)>=3-1/sqrt(2)>2`.                                     (5.5)

Put `A0=diag(2,S)`, so `s_min(A0)>=2`. The difference `E=A_*-A0` acts on span(z,u) as

`[[0,1/2],[1/2,1/8]]`,                                        (5.6)

so

`||E||=(1+sqrt(65))/16`.                                      (5.7)

Hence

`s_min(A_*) >= 2-(1+sqrt(65))/16`
`            =(31-sqrt(65))/16`
`            =1.4336088907313407...>1`.                       (5.8)

Thus all five eigenvalues of the symmetric matrix have modulus >1. It is indefinite; numerically (check only) they are

`(-3.36819688,-2.64036817,1.92353572,2.69142732,3.51860200)`. (5.9)

Applying Theorem 4.2 with `a=2`, `sigma_1=sigma_2=3` gives, for every admissible product input law,

`||p_(Q_*)||_infinity <= 2.3474046247213805...`.               (5.10)

The same active matrix can be lifted through orthonormal flat vectors on disjoint larger coordinate banks; the nonzero spectrum and aggregate singular values stay fixed while individual bank-to-bank entries shrink. The estimate is therefore genuinely aggregate-before-inversion.

## 6. Remaining implication and status

Paid: a one-clean-side cross bank with rank >=2 has a dimension-free output-density cap, and a scalar-square completion closes the critical two-cross-direction branch with explicit constant 5.74994355 at unit aggregate scale.

Not paid: `s_3(A)>=1` does not by itself expose a quadratically clean residual side. Arbitrary quadratic leakage on both active banks remains outside Theorem 3.1, and the fresh two-sided half-Riesz counterexample forbids a naive standalone extension.

Next exact debt: `QFORM-RANK2-TWOSIDED-CLEANING-OR-JOINT-REARRANGEMENT-v1`: from an unresolved residual carrying two aggregate cross singular directions, either route one side's quadratic leakage into an already-paid square/ridge/rank-two/4D-Schur packet so Theorem 4.2 applies, or prove a genuinely joint two-sided product-space estimate; do not pay a vanishing physical entry or demand a standalone two-sided hyperbolic half-Riesz bound.

Full QFORM: OPEN. Absolute continuity and essential boundedness are proved in the stated branches. A continuous representative for arbitrary merely measurable input densities is not proved by this branch. No target counterexample was found.

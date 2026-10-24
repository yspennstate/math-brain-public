# account01/B06 r51 — gradient-volume curved-fiber receiver and all-layer Pluecker compiler

**Run:** `20260924T083427Z-account01-B06-QFORM-r51`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`; programme revision `2026-09-22.5`; OWNER CONTROL `2026-09-22.15`  
**Assignment:** Curved fiber integration  
**Status:** NEW SUPPORTING ANALYTIC THEOREM + EXACT ALL-LAYER PLUECKER IDENTITY + CONDITION-NUMBER-FREE P1 TRANSITION; full unrestricted QFORM remains OPEN; global continuity remains OPEN  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 0. Scope and dependencies

The target is unchanged: independent real coordinates with probability densities bounded by one, arbitrary real symmetric `A` with at least three eigenvalues of absolute value at least one, and a universal essential density bound for `Q=X^T A X`. No moments, compact support, connected support, log-concavity, identical laws, Gaussianity, or independence after spectral rotation is assumed.

Fresh controls and the live correction inbox were read before publication. This report does not use law-uniform pointwise van der Corput decay, arbitrary-joint rank-three coarea, a conditional projection-density moment, a largest-minor inference, or an unrestricted fiber supremum.

Immediate predecessor: account01/B06 r50, `yspennstate/math-open-problems@5b36d64e5c6f1f6d38ac240ea80fa966f942ba0b`, path `proofnet24/QFORM-density/fleet-2026-09-22/account01/B06/20260924T073602Z-account01-B06-QFORM-r50/REPORT.md`. It proved the scalar-pivot/P2 receiver and the exact P1/P2 Pluecker bridge, leaving a near-rank-one hub with low P2 and nearly collinear P1 rows.

The designated partner theorem actually applied here is account02/B06 `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1`, canonical mathematics `yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5`, path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B06/b06-20260922T155426Z-9fd56fa68a65/REPORT.md`. If `R` has orthonormal columns and `Y=R^T X` is a `k`-dimensional projection of independent cap-one coordinates, then

`||p_Y||_infinity <= product_i (1-ell_i)^(-(1-ell_i)/2) <= exp(k/2)`.

For `k=2`, after deterministic normalization this implies the exact inequality used below:

`||p_(L W)||_infinity <= e / sqrt(det(L L^T))`                 (0.1)

for every full-row-rank `2 x n` matrix `L` and every original-coordinate cap-one product vector `W`.

The newest account02/B06 r15 result, `yspennstate/math-open-problems@85005bde4c308c565d29f1f8de42fdb08c062776`, is also used to locate the live branch: for a literal three-hub block `K`,

`sigma_2(K)>=1/64  =>  ||p_Q||_infinity<3149`.                 (0.2)

Hence the new receiver is aimed at the complementary near-rank-one hub transition.

## 1. A two-physical-coordinate gradient-volume small-ball theorem

Let `Y=(Y_1,Y_2)` be two literal original independent coordinates and let `Z` be a disjoint bank of literal original independent coordinates. Assume every one-dimensional input density is bounded by one. Consider

`S(Y,Z)=Y^T B Y + 2 Y^T N Z + 2 b^T Y + G(Z)`,                (1.1)

where `B=B^T` is `2 x 2`, `N` is `2 x m`, and `G` is arbitrary measurable (in the QFORM application it contains every same-bank quadratic and affine term). Put

`L=[B  N]`,
`Delta=sqrt(det(L L^T))=sqrt(det(B^2+N N^T))`.                 (1.2)

### Theorem 1.1 — `QFORM-2HUB-GRADIENT-VOLUME-SMALLBALL-v1`

If `Delta>0`, then for every `epsilon>0`,

`sup_t P(|S-t|<epsilon) <= min(1, 6 (pi e)^(1/3) Delta^(-1/3) epsilon^(2/3)).`   (1.3)

Consequently

`H_(1/2)(S):=sup_t E |S-t|^(-1/2)`
` <= 4*6^(3/4)*(pi e)^(1/4) Delta^(-1/4)`                     (1.4)

and the numerical front constant in (1.4) is

`C_grad = 26.21407380053348...`.

### Proof

Set `W=(Y,Z)`. By (0.1), applied to the **actual matrix `L`** after normalizing it by `(L L^T)^(-1/2)`,

`||p_(L W)||_infinity <= e/Delta`.                              (1.5)

The physical gradient in the two literal coordinates is

`g:=grad_Y S = 2(BY+NZ+b)=2(LW+b)`.                            (1.6)

Thus the two-dimensional density of `g` satisfies

`||p_g||_infinity <= e/(4 Delta)`.                              (1.7)

Fix a radius `r>0`. On the near-gradient region,

`P(|S-t|<epsilon, ||g||<=r)`
` <= P(||g||<=r)`
` <= (pi e/(4 Delta)) r^2`.                                    (1.8)

On the complementary region `||g||>r`, at least one literal derivative satisfies `|partial_(Y_i)S|>r/sqrt(2)`. Fix `i` and condition on every original coordinate except `Y_i`. Then `S` is a scalar quadratic polynomial of `Y_i`. On the set where its derivative has absolute value larger than `d:=r/sqrt(2)`, the quadratic has at most two monotone branches. The inverse image of an output interval of length `2 epsilon` therefore has total length at most `4 epsilon/d`. Since the conditional density of the original coordinate `Y_i` is at most one,

`P(|S-t|<epsilon, |partial_(Y_i)S|>r/sqrt(2) | other coordinates)`
` <= 4 sqrt(2) epsilon/r`.                                      (1.9)

Average and sum over `i=1,2`:

`P(|S-t|<epsilon, ||g||>r) <= 8 sqrt(2) epsilon/r`.             (1.10)

Combining (1.8) and (1.10),

`P(|S-t|<epsilon) <= 8 sqrt(2) epsilon/r + (pi e/(4 Delta)) r^2`. (1.11)

The exact minimum of `x/r+y r^2` is `3*2^(-2/3) x^(2/3)y^(1/3)`. With `x=8sqrt(2)epsilon` and `y=pi e/(4Delta)`, this is exactly the right side of (1.3).

For (1.4), write `H=6(pi e)^(1/3)Delta^(-1/3)`. The layer-cake identity gives

`E|S-t|^(-1/2) = (1/2) integral_0^infinity rho^(-3/2) P(|S-t|<rho) d rho`.

Split at `rho_0=H^(-3/2)`, where `H rho_0^(2/3)=1`. The small-rho part equals at most `3 H^(3/4)` and the tail at most `H^(3/4)`, yielding (1.4). QED.

This is a weighted curved-fiber estimate. The dangerous square-root kernel is paid only after the complete product-derived **gradient volume** has been aggregated. No fiber maximum occurs.

## 2. Scalar square plus gradient-volume half-Riesz

Return to the literal three-hub setup `H={i,j,k}` and a disjoint tail bank `T`. Write

`K=A[H,H]=[[a,c^T],[c,K_0]]`,
`M=A[H,T]=[[m^T],[M_0]]`,                                      (2.1)

where `a=K_ii !=0` and the lower block corresponds to `J=H\{i}`. Define the exact scalar-pivot Schur blocks

`B=K_0-c c^T/a`,
`N=M_0-c m^T/a`.                                                (2.2)

Completing the square only in the literal original coordinate `X_i` gives

`Q=a(X_i+shift)^2+S(X_J,X_T)`,                                  (2.3)

where `S` has the form (1.1) with its two literal `Y` coordinates equal to `X_J`, cross block `N`, quadratic block `B`, and every tail self-interaction retained in `G`.

Put

`Delta_i=sqrt(det(B^2+N N^T))`.                                 (2.4)

### Theorem 2.1 — `QFORM-SCALARPIVOT-GRADIENTVOLUME-WEIGHTED-v1`

If `a!=0` and `Delta_i>0`, then the full ambient quadratic form has an essentially bounded density and

`boxed: ||p_Q||_infinity <= C_grad |a|^(-1/2) Delta_i^(-1/4),`   (2.5)

where `C_grad=4*6^(3/4)*(pi e)^(1/4)<26.215`.

### Proof

Conditional on every original coordinate except `X_i`, the translated variable `X_i+shift` still has density cap one. The pushforward under `u -> a u^2` is bounded by `|a|^(-1/2)|y|^(-1/2)` on its half-line. Hence

`p_Q(q) <= |a|^(-1/2) E |q-S|^(-1/2)`.                          (2.6)

Apply Theorem 1.1 to `S`. QED.

No continuity conclusion is asserted by this proof.

## 3. Exact all-layer Pluecker identity

Let

`C=[B  N]`,                                                       (3.1)

whose columns are indexed by the two residual hub coordinates `J` followed by the tail coordinates `T`. For every unordered pair `r<s` in `J union T`, define the oriented mixed minor

`T_i(r,s)=det A[H,{i,r,s}]`.                                    (3.2)

### Lemma 3.1 — `QFORM-ALLLAYER-PLUCKER-IDENTITY-v1`

For every pair `r<s`,

`T_i(r,s)=+/- a det C[:,{r,s}]`.                                (3.3)

Therefore the complete fixed-pivot all-layer energy

`E_i:=sum_(r<s) T_i(r,s)^2`                                     (3.4)

obeys

`boxed: E_i=a^2 det(C C^T)=a^2 Delta_i^2.`                      (3.5)

If `R=adj(K)M` is the complete P1 mixed-minor matrix and `Sigma_i` is r50's P2 two-tail energy, then the same identity decomposes exactly as

`boxed: E_i=det(K)^2 + ||R_j||_2^2 + ||R_k||_2^2 + Sigma_i.`    (3.6)

### Proof

In the `3 x 3` determinant defining (3.2), subtract `(c/a)` times the pivot row from the two lower rows. For a residual hub column this produces the corresponding column of `B`; for a tail column it produces the corresponding column of `N`. Expansion down the pivot column proves (3.3). Cauchy-Binet gives (3.5).

The pair of residual hub columns contributes `det(K)^2`. A residual-hub/tail pair is exactly one component of one of the two P1 rows whose missing hub is the other residual coordinate. A tail/tail pair is exactly r50's P2 minor. Summing the three disjoint classes proves (3.6). QED.

Combining (2.5) and (3.5) gives the homogeneous certificate

### Corollary 3.2 — `QFORM-SCALARPIVOT-ALLLAYER-WEIGHTED-v1`

`boxed: ||p_Q||_infinity <= C_grad |a|^(-1/4) E_i^(-1/8)
      = C_grad (a^2 E_i)^(-1/8).`                               (3.7)

This strictly improves the structural reach of the r50 P2-only receiver: **P1 row collinearity is irrelevant here.** Their individual squared norms enter the all-layer currency before any reciprocal payment.

## 4. Condition-number-free near-singular P1 transition

Fix a P1 row `R_h` and let `P_h=K[H\{h},H\{h}]` be the complementary literal physical pair. Let its eigenvalues satisfy

`theta:=|lambda_1|>=|lambda_2|`,
`rho_h:=||R_h||_2`.                                              (4.1)

Assume `theta>0`.

### Corollary 4.1 — `QFORM-P1-NEARSINGULAR-ALLLAYER-EXIT-v1`

If `|lambda_2|<=theta/4`, then

`boxed: ||p_Q||_infinity <= C_ns (theta rho_h)^(-1/4),`          (4.2)

where

`C_ns=C_grad (8/3)^(1/4)=33.49860337810748...`.

### Proof

Since `|lambda_1+lambda_2|>=theta-|lambda_2|>=3theta/4`, one of the two literal diagonal entries of `P_h` has magnitude at least `3theta/8`; call that coordinate `j`. Pivot on this literal `j`. Because `h!=j`, formula (3.6) for `E_j` contains the full row norm `rho_h^2`, hence `E_j>=rho_h^2`. Insert these two lower bounds into (3.7). QED.

This remains valid at the exactly rank-one endpoint `lambda_2=0`; no inverse of `P_h` occurs.

On the complementary indefinite branch `|lambda_2|>theta/4`, account02/B06 r13's completed pair/P1 theorem gives

`||p_Q||_infinity <=15.0823111681 [|lambda_2| rho_h]^(-1/4)`
` <=21.329... (theta rho_h)^(-1/4)`.                              (4.3)

Thus the combination gives a **condition-number-free P1 receiver across the indefinite pair singularity**, with the near-singular side controlled by (4.2), not by perturbatively deleting the small pair eigenvalue.

If the well-conditioned pair is definite, the direct physical ellipse bound `pi/sqrt(|det P_h|)` remains the cleaner receiver. The still-unpaid corner is not the condition number: it is simultaneous small surviving pair scale `theta` and concentration of mixed-layer mass in a geometry not paid by another strong scalar pivot.

## 5. Effect on the r50 residual branch

The newest account02/B06 r15 compiler already removes `sigma_2(K)>=1/64`. Hence assume `sigma_2(K)<1/64`.

In the anisotropic case where a literal scalar pivot `a` is strong, r50 previously left the possibility that P1 rows were individually large but nearly collinear, because only their two-row Pluecker area was visible. Identity (3.6) removes that possibility: if the new all-layer currency `E_i` is small, then simultaneously

`|det K|` is small,
`||R_j||_2` is small,
`||R_k||_2` is small,
`Sigma_i` is small.                                             (5.1)

Thus only the P1 row **excluded by the pivot**, `R_i`, can still carry a large fraction of the complete P1 aggregate. If account02/B06 r13's `Lambda_1=sum_h||R_h||^2` lower bound is active, the residual is therefore a genuine single-row concentration, not a row-collinearity problem.

Apply Corollary 4.1 to `R_i` and its complementary physical pair. Unless that pair's surviving scale `theta_i` is also small, the branch is paid uniformly even if the second pair eigenvalue is zero or arbitrarily small. The first remaining finite-hub debt can therefore be stated more sharply as:

`QFORM-SINGLEROW-SMALLPAIR-SCALE-ROUTING-v1`:

> In the near-rank-one physical hub branch, after every strong-pivot all-layer currency is small, any large P1 aggregate must concentrate in the excluded row. Show that simultaneous largeness of that row and small surviving scale of its complementary physical pair forces a quantitative tail/grouped-coordinate receiver from the global three-large-eigenvalue hypothesis, retaining all tail self-curvature.

This is narrower than r50's `LOW-P2-ROWCOLLINEAR` debt.

## 6. Exact sanity checks

Random deterministic matrix checks (not proof) verified (3.5)-(3.6) for symmetric random `K`, random tail block `M`, and tail sizes `m=0,1,2,5,10`. Across 100 trials per size, the largest normalized discrepancy in `E_i=a^2 det([B N][B N]^T)` was below `8.4e-14`, and the largest normalized discrepancy in the categorized identity (3.6) was below `4.3e-16`. The proof is the exact row-elimination/Cauchy-Binet argument above.

## 7. Status

The full arbitrary-dimensional QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. Global continuity remains **OPEN**. The new theorems establish essential boundedness only under their explicit positive gradient-volume/all-layer currencies. No counterexample to the target was found.

The key new mechanism is product-weighted rather than fiberwise: the full two-dimensional physical gradient is treated as a product projection with density cap supplied by account02/B06, while the high-gradient region is paid by literal-coordinate monotonicity. This integrates the curved ellipse/hyperbola geometry jointly with product structure and avoids the known dimension loss from taking unrestricted spectral-fiber maxima.

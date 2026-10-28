SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B06, 2026-09-22T23:35:55Z.
attacking: weighted curved-fiber aggregation before local pair supremum; isolate an exact dimension-free product-weighted kernel inequality or a source-valid falsifier.

# account01/B06 — curvature-weighted physical-fiber covers

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260922T233555Z-qform-r19-b06`  
**Classification:** `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREM_PROVED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN` (repository retrieval/write occurred; no verified native learned-memory ingestion/receiver use occurred).

## 0. Exact target, source pins, and scope

The target remains: for every `n`, independent real coordinates `X_i` with probability densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove that `Q=X^T A X` has an essentially bounded density with one universal bound, or give a valid counterexample. Continuity is a separate requested conclusion and is **not** proved here.


1. `COUNTEREXAMPLE_SEARCH.md`, item 1: the physical-coordinate fibre identity

   `p_Q(s)=sum_i E_{X_-i} sum_{x_i:Q=s} f_i(x_i) |partial_i Q|/|grad Q|^2`

   for a.e. `s`, obtained by the partition of unity `(partial_i Q)^2/|grad Q|^2` and one-dimensional coarea.

2. `COUNTEREXAMPLE_SEARCH.md`, Theorem C: for an exact rank-three signature `(+,+,-)` form, the one-sheet side `s>=0` is bounded by `pi sqrt(2)` by ruled hyperboloid integration. I use this only in its stated exact-rank-three/no-extra-spectrum scope.

The designated partner result actually applied is account02/B06 `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1`, canonical proof

`yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5`

at

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B06/b06-20260922T155426Z-9fd56fa68a65/REPORT.md`.

For any `n x k` matrix `U` with orthonormal columns and `Y=U^T X`, if the row leverages are `ell_j`, the partner proves

`||p_Y||_infinity <= M(U):=prod_{ell_j<1}(1-ell_j)^(-(1-ell_j)/2) <= exp(k/2)`.

This is a weighted physical fibre integral, not an unrestricted fibre supremum.

All statements below respect the live corrections: no law-uniform pointwise quadratic-phase decay, no independence after spectral rotation, no arbitrary-joint rank-three coarea bound, no positive moment of a worst conditional projection cap, and no fixed uniformly good physical minor.

## 1. Setup for exact rank three

First isolate the exact-rank-three geometry, where a new weighted identity is clean and rigorous. Let

`A=R Lambda R^T`,   `R^T R=I_3`,   `Lambda=diag(lambda_1,lambda_2,lambda_3)`,   `|lambda_k|>=1`.

Write `r_i in R^3` for row `i` of `R`, `q_i=||r_i||`, and

`Y=R^T X`,   `z=Lambda Y`.

Then

`Q=Y^T Lambda Y`,
`grad Q=2 R z`,
`|grad Q|=2|z|`,
`partial_i Q=2 r_i dot z`.

For each `i` with `q_i>0`, let `u_i=r_i/q_i`, let `V_i` be any `3 x 2` matrix whose columns are an orthonormal basis of `u_i^perp`, and put

`W_i=V_i^T Y=(R V_i)^T X`.

The `i`-th row of `R V_i` is zero, so `W_i` depends only on `X_-i`. The columns of `R V_i` are orthonormal. Define its physical row leverages

`eta_ij=||V_i^T r_j||^2`

and the exact partner cap

`M_i=prod_{j:eta_ij<1}(1-eta_ij)^(-(1-eta_ij)/2) <= e`.

By the partner theorem,

`||p_{W_i}||_infinity <= M_i`.                                      (1.1)

The key improvement over the unweighted physical-fibre estimate is to retain the anisotropic curvature of `Lambda` on the two-dimensional fibre transverse to `r_i`.

## 2. Exact transverse-curvature matrix

For fixed `w=V_i^T y`, minimize the gradient size `|Lambda y|` over the missing scalar coordinate along `u_i`. Define

`K_i = V_i^T Lambda^2 V_i
       - (V_i^T Lambda^2 u_i)(V_i^T Lambda^2 u_i)^T/(u_i^T Lambda^2 u_i)`.        (2.1)

This is the Schur complement of the `u_i` entry of `Lambda^2` in the orthonormal basis `[u_i,V_i]`; hence `K_i` is positive definite and

`|Lambda y|^2 >= w^T K_i w`.                                         (2.2)

The determinant is exact:

`det K_i = det(Lambda^2)/(u_i^T Lambda^2 u_i)
         = |det Lambda|^2/(u_i^T Lambda^2 u_i)`.                       (2.3)

This identity is important: the two-dimensional fibre pays the **product of the two transverse curvatures**, rather than the worst scalar curvature or a physical minor.

Apply the linear map `K_i^(1/2)` to `W_i`. From (1.1), its density is bounded by

`M_i/(det K_i)^(1/2)`.

For any probability density `h` on `R^2` with `h<=M`, the bathtub/rearrangement bound is

`int h(w)/|w| dw <= 2 sqrt(pi M)`.                                    (2.4)

Indeed, the maximizing cap-`M` probability law is `M` times the indicator of the centered disk of area `1/M`. Consequently

`E (W_i^T K_i W_i)^(-1/2)
 <= 2 sqrt(pi M_i) (det K_i)^(-1/4)`.                                 (2.5)

This is the product-weighted curved-fibre replacement used below.

## 3. Main theorem: curvature-weighted physical-fibre cover

### Theorem — `QFORM-CURVATURE-WEIGHTED-PHYSICAL-FIBER-COVER-v1`

Let `A=R Lambda R^T` be as above. For nonnegative weights `a_i`, define

`G(a)=sum_i a_i r_i r_i^T`.                                           (3.1)

If

`G(a) >= I_3`                                                         (3.2)

in Loewner order, then `Q=X^T A X` has an essentially bounded density and

`||p_Q||_infinity
 <= 2 sqrt(pi) sum_{i:q_i>0} a_i q_i sqrt(M_i) (det K_i)^(-1/4)`       (3.3)

or, using (2.3), equivalently

`||p_Q||_infinity
 <= (2 sqrt(pi)/sqrt(|det Lambda|))
    sum_i a_i sqrt(q_i |Lambda r_i|) sqrt(M_i)`.                       (3.4)

In particular, since `M_i<=e` and `|lambda_k|>=1`, the coarser but simpler bound

`||p_Q||_infinity <= 2 sqrt(pi e) inf_{a>=0:G(a)>=I_3} sum_i a_i q_i`  (3.5)

holds.

### Proof

On every regular point, (3.2) gives the weighted gradient partition

`1 <= z^T G(a) z/|z|^2
   = sum_i a_i (r_i dot z)^2/|z|^2
   = sum_i a_i (partial_i Q)^2/|grad Q|^2`.                            (3.6)

Insert (3.6) into the newest-source physical-fibre/coarea identity before any fibrewise supremum is taken. Thus for a.e. `s`,

`p_Q(s) <= sum_i a_i T_i(s)`,                                         (3.7)

where

`T_i(s)=E_{X_-i} sum_{x_i:Q=s} f_i(x_i)|partial_i Q|/|grad Q|^2`.      (3.8)

At a root contributing to (3.8),

`|partial_i Q|/|grad Q|^2
 = |r_i dot z|/(2|z|^2)
 <= q_i/(2|z|)
 <= q_i/[2 (W_i^T K_i W_i)^(1/2)]`,                                  (3.9)

where the last step is (2.2). For fixed `X_-i`, the polynomial in `X_i` has at most two noncritical roots. The critical/identically-flat cases carry zero weight in (3.8) and are covered by the a.e. coarea identity. Since `f_i<=1`, the two roots cancel the factor `1/2` in (3.9), giving

`T_i(s) <= q_i E (W_i^T K_i W_i)^(-1/2)`.                             (3.10)

Now apply (2.5):

`T_i(s) <= 2 sqrt(pi) q_i sqrt(M_i) (det K_i)^(-1/4)`.                 (3.11)

Summing with weights `a_i` proves (3.3). Formula (3.4) follows from (2.3) and `u_i=r_i/q_i`:

`q_i(det K_i)^(-1/4)
 = sqrt(q_i |Lambda r_i|)/sqrt(|det Lambda|)`.                         (3.12)

Finally `M_i<=e`, while `det K_i>=1` because all singular values of `Lambda` are at least one; this gives (3.5). `QED`

### What is genuinely new here

The newest-source Theorem B bounded each physical-fibre contribution separately and then summed all physical rows, producing a dimension-dependent `sum_i ||P e_i||`. Formula (3.3) instead inserts an **arbitrary aggregate frame cover before coarea decomposition**, and it keeps the full transverse curvature determinant `det K_i` plus the partner's exact product-fibre factor `M_i`. No reciprocal physical determinant is selected and no spectral-fibre maximum appears.

The theorem is still a supporting result: the bare three-large-eigenvalue hypothesis does not by itself give a dimension-free value of the cover objective in (3.3).

## 4. SDP form and a bounded-support corollary

Define the uncurved cover number

`Gamma_0(R)=inf { sum_i a_i q_i : a_i>=0, sum_i a_i r_i r_i^T >= I_3 }`. (4.1)

The primal is strictly feasible (`a_i=2`), so elementary semidefinite duality gives

`Gamma_0(R)=sup { tr H : H>=0, r_i^T H r_i <= q_i for every i }`.       (4.2)

Thus (3.5) is a finite-dimensional weighted covering problem, not a hidden conditional-density supremum.

If a physical set `S` of cardinality `m` has aggregate spectral Gram matrix

`G_S=sum_{i in S} r_i r_i^T >= theta I_3`,                             (4.3)

choose `a_i=theta^(-1)` on `S` and zero elsewhere. Since `sum_{i in S}q_i^2=tr G_S<=3`, Cauchy-Schwarz yields

`sum_{i in S} q_i <= sqrt(3m)`.

Therefore

`||p_Q||_infinity <= 2 sqrt(3 pi e m)/theta`.                          (4.4)

This is dimension-free for every fixed `(m,theta)`, all signatures, arbitrary fragmented/unbounded cap-one input laws, and it uses **aggregate physical curvature** rather than one selected principal minor.

Stress tests:

* Coordinate frame `R=I_3`: take `S={1,2,3}`, `theta=1`; the result is finite (coarse compared with the sharp diagonal `pi`).
* Equal-norm diffuse Parseval frames: `q_i=sqrt(3/n)` and `Gamma_0(R)=sqrt(3n)` in the isotropic equal-weight case (trace of the constraint already forces this). Hence this physical-fibre cover alone correctly loses `sqrt(n)` there; the newest-source Fresnel/Brascamp-Lieb Theorem F is the complementary dimension-free mechanism. This explicitly prevents us from falsely promoting (3.5) to the full conjecture.

## 5. Two-sheet refinement: cover only the curved side that still needs payment

Now take exact rank three with signature `(+,+,-)`:

`Lambda=diag(lambda_1,lambda_2,-mu)`, `lambda_1,lambda_2,mu>=1`.

The newest-source Theorem C already proves

`p_Q(s) <= pi sqrt(2)` for `s>=0`.                                    (5.1)

For `s<0`, the spectral gradient variable `z=Lambda y` lies in the two-sheet cone

`K_-={z !=0 : z^T Lambda^(-1) z <0}`,                                 (5.2)

because `Q=y^T Lambda y=z^T Lambda^(-1)z`.

The proof of Theorem 3 never needed (3.2) away from the actual level set. Hence for the two-sheet side it is enough that

`z^T G(a) z >= |z|^2` for every `z in K_-`.                           (5.3)

Define the curvature-weighted cone cost

`Gamma_-(R,Lambda)
 = inf sum_i a_i q_i sqrt(M_i)(det K_i)^(-1/4)`,                       (5.4)

where the infimum is over `a_i>=0` satisfying (5.3). Then

`ess sup_{s<0} p_Q(s) <= 2 sqrt(pi) Gamma_-(R,Lambda)`.                (5.5)

The cone constraint has an exact `3 x 3` LMI representation. Since the quadratic form `z^T Lambda^(-1)z` has a strict negative point, the homogeneous S-lemma gives that (5.3) is equivalent to the existence of `tau>=0` such that

`G(a)-I_3 + tau Lambda^(-1) >=0`.                                     (5.6)

Thus the previously geometric two-sheet payment becomes a finite semidefinite weighted-cover problem retaining the original product-law fibre caps and all transverse curvature factors. Combining (5.1) and (5.5),

`||p_Q||_infinity
 <= max { pi sqrt(2), 2 sqrt(pi) Gamma_-(R,Lambda) }`                  (5.7)

for this exact-rank-three signature. Reflection gives the analogous statement for `(-,-,+)`.

This is a structural reduction, **not** a proof that `Gamma_-` is universally bounded. For a completely diffuse isotropic frame the unweighted cover can still grow like `sqrt(n)`; that regime is instead paid by the newest-source Theorem F. The live hybrid problem is to combine these two mechanisms (and the existing scalar/Schur peels) without losing a dimension-dependent factor.

## 6. Consequences for the full proof graph

The run changes the unpaid interface in a concrete way.

1. The curved physical-fibre route no longer has to select one physical pair or one physical triple and invert its determinant. It can pay any **weighted aggregate coordinate cover** through (3.3).
2. The cost at coordinate `i` is not merely a leverage. It is the exact product

   `q_i sqrt(M_i)(det K_i)^(-1/4)
    = sqrt(M_i) sqrt(q_i |Lambda r_i|)/sqrt(|det Lambda|)`,

   which records both product-measure fibre geometry and the two transverse spectral curvatures.
3. On the indefinite exact-rank-three case, the ruled one-sheet theorem means the weighted cover is needed only on the two-sheet cone; the S-lemma converts that requirement into (5.6).
4. A bounded-size aggregate spectral cover immediately gives the explicit dimension-free bound (4.4), even if every tempting same-sign Pluecker pair has zero full physical determinant (the known Hadamard support-disjoint obstruction).

The first unpaid implication is therefore

`QFORM-HYBRID-CONE-COVER-OR-FRESNEL-v1`:

for an exact-rank-three frame outside the diffuse Fresnel/Brascamp-Lieb branch, either show the cone SDP (5.6) has a dimension-free curvature-weighted objective, or use the failure certificate from its dual to force one of the already-paid scalar-Schur / grouped cross / mixed-hub branches. The equal-norm diffuse frame is a mandatory stress test and must be sent to Theorem F rather than to (3.5).

For the **full arbitrary-rank target**, additional eigenvalues remain a separate debt: (3.3)-(5.7) use the exact rank-three identity `|grad Q|=2|Lambda R^T X|`. They must not be applied after simply discarding additional spectral components. A full proof still has to route arbitrary extra components through a source-valid conditioning, cross-block, Fresnel, or Schur mechanism.

## 7. Status

* Full universal QFORM theorem: **OPEN**.
* Valid counterexample to the original conjecture: **none supplied**.
* Exact new result: `QFORM-CURVATURE-WEIGHTED-PHYSICAL-FIBER-COVER-v1`, including cone-restricted two-sheet form and LMI reduction.
* Latest Claude-attributed source actually applied: physical-fibre identity and one-sheet ruled theorem at `e5f71d79eff325201dd0274053d20268ce65b837`.
* Named partner actually applied: account02/B06 weighted affine-fibre Brascamp-Lieb theorem at `8dd33c1abd4fd64140f59032feda2b13d4351da5`.
* Essential boundedness: proved only in the quantified branches above.
* Continuous density: **not proved** by this argument.
* Next useful recipient: account03/B08 (hybrid/diffuse geometry), with account03/B17 as a useful witness/optimization recipient for the cone-SDP stress tests.

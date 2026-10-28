SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B11, 2026-09-22T20:10:09Z.
attacking: the partner's parabolic null-graph trace obstruction via a product-preserving three-ray bank compression, then the first overlap compiler beyond separated banks.

# account03/B11 QFORM r15 — aligned three-bank compiler for curved indefinite blocks

Programme: `QFORM-DENSITY-3EIG-20260922`  
Worker: `account03/B11` — Indefinite signatures  
Run: `20260922T201009Z-account03-B11-QFORM-r15`  
Control refresh before publication: revision `2026-09-22.15` remained active; no B11 stop.  
Outcome: **ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_THEOREM / FULL_TARGET_OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**

The full universal conjecture remains open. This run pays a genuinely high-dimensional curved three-bank branch which was not covered by the preceding zero-diagonal triangle theorem. All independence used below comes from disjoint sets of original coordinates. No spectral rotation is treated as preserving independence.

## 1. Valid inputs and live corrections

### 1.1 Previous B11 localized theorem

From

`yspennstate/math-open-problems@a9f23a3a387c9be219fcaf08ef66079f8c124e0c`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B11/20260922T192514Z-account03-B11-QFORM-r14/REPORT.md`,

we use `QFORM-LOCALIZED-3BLOCK-REPAIR-v1`: if three independent cap-one variables carry a symmetric `3 x 3` quadratic matrix `C` with

`σ_min(C) >= s > 0`,

then, uniformly over every affine perturbation,

`||p||_infinity <= 128 * 2^(1/4) / s < 153/s`.                 (1.1)

Its proof stays in the independent coordinates and uses a scalar-pivot / physical-indefinite-pair dichotomy. It does **not** use the refuted arbitrary-joint coarea claim.

### 1.2 Product one-dimensional marginal bound

For a nonzero coefficient vector `u` supported on one original-coordinate bank of independent cap-one variables,

`||p_<u,X>||_infinity <= sqrt(2)/||u||_2`.                     (1.2)

This is the standard one-dimensional product-marginal bound and is also the quantitative projection input used in the completed account03/B09 three-bank theorem. We use it only to compress one independent bank to one scalar; it is not used as a claim about an indefinite quadratic pushforward.

### 1.3 Assigned partner result actually applied

The completed designated partner result is account04/B11 r2:

`yspennstate/math-open-problems@797dcde430e982a020d7642b54cadc281cbc9bc1`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B11/20260922T191727Z-account04-B11-nullgraph-obstruction-r2/REPORT.md`.

For the canonical indefinite form

`T = 2 Z W + V^2`,

with joint density `h(z,v,w)`, it proves the exact identity

`p_T(t) = (1/2) ∫_{w != 0} h((t-v^2)/(2w),v,w) dv dw / |w|`.  (1.3)

Equivalently, with

`N(h)=sup_t ∫_{w != 0} h((t-v^2)/(2w),v,w) dv dw / |w|`,

`N(h)=2 ||p_T||_infinity` for the corresponding density representative. The partner also gives an explicit nonlinear dependent construction with bounded `(V,W)` density and uniformly bounded conditional `Z|(V,W)` densities for which `N(h)=infinity`. Thus marginal/conditional caps alone do not pay the trace. Genuine product-linear provenance is the missing ingredient.

### 1.4 Corrections enforced

This proof does not use: law-uniform pointwise quadratic-phase decay; independence after diagonalizing a quadratic matrix; the false arbitrary-joint three-dimensional coarea estimate; positive conditional projection-density moments; a naive fiber supremum; a fixed good physical triple; or the refuted near-zero half-Riesz interface. The rank-two opposite-sign logarithm remains a mandatory control.

## 2. Main theorem — curved rank-one geometry on three independent banks

### Theorem 2.1 — `QFORM-ALIGNED-THREE-BANK-COMPILER-v1`

Let `I,J,K,R` be pairwise disjoint sets of original coordinate indices. All original coordinates are independent and have probability densities at most one. Choose nonzero vectors

`u in R^I`, `v in R^J`, `w in R^K`,

and let `B=(b_ab)_{a,b=1}^3` be a real symmetric `3 x 3` matrix. Assume the active blocks of the full symmetric matrix `A` have the aligned rank-one form

`A[I,I] = b_11 u u^T`,
`A[J,J] = b_22 v v^T`,
`A[K,K] = b_33 w w^T`,
`A[I,J] = b_12 u v^T`,
`A[I,K] = b_13 u w^T`,
`A[J,K] = b_23 v w^T`,                                          (2.1)

with the transposed blocks imposed by symmetry. Arbitrary quadratic curvature on `R` is allowed. Couplings to `R` are allowed provided

`range A[I,R] subset span{u}`,
`range A[J,R] subset span{v}`,
`range A[K,R] subset span{w}`.                                  (2.2)

Put

`D = diag(||u||_2, ||v||_2, ||w||_2)`,
`C = D B D`,                                                     (2.3)

and suppose

`σ_min(C) >= s > 0`.                                            (2.4)

Then the full ambient quadratic form `Q=X^T A X` has an essentially bounded density and

`boxed: ||p_Q||_infinity <= 256 * 2^(1/4) / s < 304.438/s.`     (2.5)

The theorem is signature-free. In particular it includes genuinely coupled compressed signatures `(+,+,-)` and `(+,-,-)` with arbitrary diagonal/self-bank curvature `b_11,b_22,b_33`.

### Proof

Condition on every outside original coordinate `X_R`. Because the original law is a product, the three banks `X_I,X_J,X_K` remain independent and retain their original marginal laws. Assumption (2.2) implies that all outside cross terms become affine functions of exactly the three scalar bank projections

`U=<u,X_I>`, `V=<v,X_J>`, `W=<w,X_K>`;                          (2.6)

while the outside quadratic part becomes an additive conditioned constant. By (2.1), the conditional quadratic part is

`(U,V,W) B (U,V,W)^T`.                                         (2.7)

Normalize the bank projections:

`Z_1=U/||u||_2`, `Z_2=V/||v||_2`, `Z_3=W/||w||_2`.             (2.8)

The variables `Z_1,Z_2,Z_3` are genuinely independent because their original-coordinate banks are disjoint. By (1.2), each has density bounded by `sqrt(2)`. In vector notation the conditioned form becomes

`Z^T C Z + ell^T Z + gamma`.                                   (2.9)

Now set `Y=sqrt(2) Z`. Each `Y_i` has density bounded by one and the three remain independent. Equation (2.9) becomes

`Y^T (C/2) Y + (ell/sqrt(2))^T Y + gamma`.                     (2.10)

By (2.4),

`σ_min(C/2) >= s/2`.                                           (2.11)

Apply the previous localized theorem (1.1) to the three **independent scalar bank variables** `Y_i`. Uniformly in every outside conditioning value,

`||p_(Q | X_R)||_infinity`
` <= 128 * 2^(1/4)/(s/2)`
` = 256 * 2^(1/4)/s`.                                          (2.12)

Averaging the corresponding conditional interval inequality over `X_R` gives the same bound for the unconditional law. This avoids measurable-density-selection issues and proves (2.5). `QED`

### Why this is new relative to the zero-diagonal triangle theorem

The completed three-bank triangle theorem pays a cycle of three rank-one cross blocks when all three active self blocks vanish. Theorem 2.1 permits **arbitrary self-bank quadratic coefficients** `b_11,b_22,b_33`, so long as all active blocks share the same one-dimensional bank directions and the compressed `3 x 3` matrix is uniformly nonsingular. This pays a concrete curved-bank part of the current aggregate-before-inversion residual without selecting a small physical coordinate minor.

## 3. Exact-rank-three three-ray corollary

### Corollary 3.1 — `QFORM-THREE-RAY-EXACT-RANK3-v1`

Let

`A = R M R^T`, `R^T R=I_3`, `σ_min(M)>=s`,                      (3.1)

so `A` has exact rank three. Suppose the original coordinates can be partitioned into three disjoint banks `I_1,I_2,I_3` such that every row `r_i` of `R` in bank `I_k` lies on one fixed ray:

`r_i = a_i v_k`.                                                (3.2)

No bound is imposed on the number of coordinates in a bank or on the individual coefficients `a_i`. Then

`boxed: ||p_(X^T A X)||_infinity < 304.438/s`.                  (3.3)

In particular, if the three nonzero eigenvalues of `A` have modulus at least one, the bound is `<304.438` for either indefinite signature.

### Proof

Let

`σ_k^2 = sum_{i in I_k} a_i^2`, `s_k=σ_k v_k`.                 (3.4)

Since `R^T R=I_3`,

`sum_{k=1}^3 s_k s_k^T = I_3`.                                (3.5)

There are exactly three vectors in three dimensions, so the square matrix

`S=[s_1 s_2 s_3]`

satisfies `S S^T=I_3` and is therefore orthogonal. Define independent normalized bank projections

`Z_k = σ_k^(-1) sum_{i in I_k} a_i X_i`.                       (3.6)

Then each `Z_k` has density cap at most `sqrt(2)` by (1.2), and

`R^T X = S Z`.                                                  (3.7)

Consequently

`X^T A X = Z^T (S^T M S) Z`,                                  (3.8)

and orthogonal conjugacy gives

`σ_min(S^T M S)=σ_min(M)>=s`.                                  (3.9)

Apply Theorem 2.1 with the three banks and no outside variables. `QED`

This is a genuinely high-dimensional rotated theorem: each ray may contain arbitrarily many fragmented cap-one input coordinates. It is not a diagonal-basis independence argument; the only independent variables are the three compressed **disjoint original-coordinate banks**.

## 4. Actual use of account04/B11: a bounded overlapping null-graph trace

The partner obstruction asks for product-specific structure capable of controlling the parabolic null-graph trace (1.3), even though marginal and conditional caps alone fail. Theorem 2.1 supplies such a structure for an explicit genuinely overlapping family.

Let

`H0 = [[0,0,1],[0,1,0],[1,0,0]]`,                              (4.1)

so `y^T H0 y = 2 y_1 y_3 + y_2^2` and `spec(H0)={1,1,-1}`. Let `Z=(Z_1,Z_2,Z_3)` be the independent normalized bank projections of Theorem 2.1, each with density cap at most `sqrt(2)`. Let `O` be any orthogonal `3 x 3` matrix and define

`Y = O Z`.                                                       (4.2)

The coordinates of `Y` are generally dependent and each may involve **all three original banks**. Nevertheless

`T = Y^T H0 Y = Z^T C Z`, `C=O^T H0 O`,                       (4.3)

and

`σ_min(C)=1`.                                                   (4.4)

Theorem 2.1 therefore gives

`||p_T||_infinity <= 256 * 2^(1/4) < 304.438`.                 (4.5)

Now apply the partner's exact identity (1.3) to the actual joint density `h_Y` of the dependent triple `Y`. We obtain the quantitative overlapping trace bound

`boxed: N(h_Y) = 2 ||p_T||_infinity`
`       <= 512 * 2^(1/4) < 608.875.`                           (4.6)

This is an actual inequality obtained by combining the completed account04/B11 result with the new compiler. It directly excludes the partner's multiscale null-graph divergence for this three-bank product-linear provenance. The partner's counterexample is not contradicted: its nonlinear relation `Z=-V^2/(2W)+U` is not a linear orthogonal image of three independent product-bank projections.

### Fully coupled exact example

Take

`O=(1/7)[[6,-2,-3],[-2,3,-6],[-3,-6,-2]]`.                    (4.7)

Every entry is nonzero and `O^T O=I`. Exact multiplication gives

`C=O^T H0 O`
` =(1/49)[[-32,-36,9],[-36,33,4],[9,4,48]]`.                  (4.8)

Thus the compressed form has all three off-diagonal couplings nonzero, `C^2=I`, `det C=-1`, and signature `(+,+,-)`. It is therefore a strict genuinely rotated indefinite example, not a separable or block-diagonal control. Equation (4.6) applies uniformly to arbitrary fragmented cap-one laws inside the three source banks.

Negating the matrix gives the corresponding `(+,-,-)` statement with the same constant.

## 5. How the third direction removes the rank-two logarithm

The opposite-sign rank-two control remains:

for independent `X,Y ~ Uniform[-1/2,1/2]`,

`p_(2XY)(t)=log(1/(2|t|))`, `0<|t|<1/2`,                       (5.1)

so the density is logarithmically unbounded at zero.

There are two equivalent product-preserving views of the repair in the branch proved here.

First, Theorem 2.1 keeps a third independent bank and produces a full nonsingular `3 x 3` compressed matrix. The preceding localized theorem then forces either a quantitatively useful scalar pivot, whose square-root smoothing integrates the rank-two half-Riesz singularity, or a quantitatively useful physical indefinite pair whose logarithmic envelope is paid by the third singular direction. The three-bank compression happens **before** any reciprocal local determinant is paid.

Second, for the canonical `H0`, the three linearly independent null vectors

`l_1=(1,0,0)`, `l_2=(0,0,1)`, `l_3=(1,sqrt(2),-1)`             (5.2)

have Gram matrix

`[l_i^T H0 l_j] = [[0,1,-1],[1,0,1],[-1,1,0]]`.               (5.3)

Hence in independent null-ray coordinates the quadratic form is

`2(U_1 U_2 - U_1 U_3 + U_2 U_3)`.                             (5.4)

The third independent scalar closes a bilinear triangle rather than leaving one product singularity exposed. The completed triangle log-smoothing theorem bounds exactly this geometry. This makes the dimensional threshold concrete: two opposite-sign directions retain the harmonic logarithm; the third independent product direction supplies an integrable averaging channel.

## 6. What remains unpaid

The full target is **OPEN / NOT PROVED**. Theorem 2.1 requires an exact aligned rank-one three-bank structure and a uniformly nonsingular compressed matrix. The bare condition that `A` has three eigenvalues of magnitude at least one does not by itself provide such a partition; known diffuse and singleton-plus-two-bank examples rule out a naive single-good-minor reduction.

The first remaining B11 implication is therefore:

`QFORM-APPROXIMATE-THREE-BANK-OR-RIDGE-v1`: from the three-large-eigenvalue hypothesis, produce either

1. an exact/grouped aligned three-bank compressed block entering Theorem 2.1 at universal scale;
2. an already-paid wedge/triangle/ridge/diffuse certificate at universal scale; or
3. a product-preserving residual estimate that handles the genuinely unaligned curvature directly.

One must **not** treat approximate alignment as a small additive perturbation by coefficient norm alone: the input laws have no moment or support bound, so a small matrix coefficient can multiply arbitrarily large coordinates. Any approximation must be absorbed at the probability/characteristic-function level or by conditioning with a translation-uniform theorem.

This report proves existence of an **essentially bounded density** only in the stated branches. It does **not** prove a continuous representative.

## 7. Exact computation

`VERIFY.py` in this run directory checks with exact rational arithmetic that the matrix (4.7) is orthogonal, that (4.8) is exact, `C^2=I`, `det C=-1`, and `tr C=1`, hence `spec(C)={1,1,-1}`. It also checks the null-ray Gram matrix (5.3) and the constants

`256*2^(1/4)=304.4370214406966...`,
`512*2^(1/4)=608.8740428813932...`.

The checker terminates `QFORM_ALIGNED_THREE_BANK_COMPILER_CHECK_PASS`. No Monte Carlo or histogram is used as proof evidence.

## 8. Integrity

The source owner message was reread under the live revision `2026-09-22.15`; the newer correction inbox was also reread before publication. Where the preserved owner-message prose asserts an arbitrary-joint coarea lemma, the later source correction controls and that assertion is not used. Repository transport is not native receiver ingestion, so this run remains `WITHOUT_VERIFIED_BRAIN`.

No scheduler/task, notification, email, Drive, public-release, remote-workflow, paid-model/API, Codex, credential, permission, or cross-account-native action was performed.

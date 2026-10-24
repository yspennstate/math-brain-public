SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B09, 2026-09-24T07:46:14Z.
attacking: convert the promoted-frame determinant failure into a macroscopic literal Pluecker star, then expose that star as an actual source-coordinate bilinear coefficient without selecting a tiny minor.

# account01/B09 r33 — determinant-or-star promotion compiler

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: B09 bilinear block mechanism  
Status: **NEW SUPPORTING THEOREM / ESSENTIAL STEP APPLIED / FULL QFORM OPEN / FULL-TARGET CONTINUITY OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**.

The unrestricted conjecture is not claimed solved. The purpose of this run is to close the precise structural debt left by account01/B09 r32: a high-leverage source coordinate may make the retained-hub Brascamp--Lieb gate fail after promotion, and one must not pay by the reciprocal of a tiny scalar pivot. The result below shows that this failure is itself a quantitative physical object: a literal basis-star carrying a fixed fraction of the residual determinant currency. In the rank-one fixed-hub packet, it becomes a macroscopic source-coordinate Pluecker star and an independent bounded-density linear observable.

All random variables remain literal original independent source coordinates with one-dimensional densities bounded by one. A two-coordinate determinant-one change is used only to expose an algebraic bilinear coefficient; after that change the two transformed variables are explicitly treated as a joint density bounded by one, not as independent variables.

## 1. Sources actually used

The immediate source is account01/B09 r32, `QFORM-PROMOTED-LEAF-RETAINED-HUB-BL-v1`, at

`yspennstate/math-open-problems@dd2f429f6135ce79e5801d58eca341a82d736527`,

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B09/20260924T065224Z-account01-B09-QFORM-auto11-r32/REPORT.md`.

For one literal hub `h`, leaf block

`A_LL=D+V Lambda V^T`,

physical hub column `c=A[L,h]`, promoted literal set `S`, residual set `R=L\S`, mixed rows

`x_j=(V_j,c_j) in R^(r+1)`,

and `G_R=sum_(j in R)x_jx_j^T`, r32 proves: if `G_R>0` and every residual leverage is at most `1/2`, then the full ambient form has a continuous density and

`||p_Q||_infinity <= C_r [det(G_R) prod_q |lambda_q|]^(-1/(r+2))`,

with the identical coefficient times interval length, where

`C_r=4(r+2)/r * 2^(-2/(r+2))`.

The number of promoted literal coordinates costs no Fourier power or numerical factor.

The rank-one fixed-hub source from r31/r32 also gives, for `x_j=(v_j,c_j) in R^2`,

`Omega_(1,h)^dis = lambda^2 T^2 rho`,

where

`T=det(sum_j x_jx_j^T)=sum_(i<j)(c_i v_j-c_jv_i)^2`

and `0<=rho<=1` is the two-basis disjointness probability. In particular

`|lambda| T >= sqrt(Omega_(1,h)^dis)`.

The designated partner source actually applied below is account02/B09 r19,

`QFORM-TWOHUB-DOUBLE-RETENTION-v1`,

at `yspennstate/math-open-problems@6e6427a931f0c121990176664cc3870715edbead`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B09/20260924T064452Z-account02-B09-QFORM-r19/REPORT.md`.

## 2. Exact basis-star identity

### Theorem 2.1 — `QFORM-MIXED-GRAM-BASISSTAR-IDENTITY-v1`

Let `R` be a finite literal-coordinate set and let rows `x_i in R^d` have positive Gram

`G_R=sum_(i in R)x_ix_i^T>0`.

Put

`D(R)=det G_R`,

and for `i in R`

`ell_i(R)=x_i^T G_R^(-1)x_i`.

For each `d`-element subset `B subset R`, let `X_B` be the square matrix with rows `x_j^T`, `j in B`, and define the literal basis-star volume at `i`

`S_i(R)=sum_(B subset R, |B|=d, i in B) det(X_B)^2`.

Then exactly

`boxed: S_i(R)=D(R) ell_i(R)=D(R)-D(R\{i}).`                    (2.1)

### Proof

Cauchy--Binet gives

`D(R)=sum_(B subset R, |B|=d) det(X_B)^2`.                     (2.2)

Removing row `i` deletes exactly the terms with `i in B`, hence

`S_i(R)=D(R)-D(R\{i}).`                                       (2.3)

On the other hand

`G_(R\{i})=G_R-x_ix_i^T`,

and the matrix determinant lemma gives

`D(R\{i})=D(R)(1-ell_i(R)).`                                  (2.4)

Since the left side is nonnegative, `0<=ell_i<=1`; (2.1) follows, including the exact-coloop endpoint `ell_i=1`. QED.

The important point is that a leverage failure is already **aggregate physical determinant currency**. It does not require selecting a single basis/minor from a large sum.

## 3. Thresholded promotion stopping theorem

### Theorem 3.1 — `QFORM-PROMOTION-DETERMINANT-OR-STAR-v1`

Start from `R_0` with `D_0=D(R_0)>0` and fix `eta in (0,1]`. Run the following finite source-coordinate procedure.

At a current set `R`, if every leverage is at most `1/2`, stop in the **diffuse residual** branch. Otherwise choose any literal row `i in R` with `ell_i(R)>1/2`. If

`D(R\{i}) >= eta D_0`,                                        (3.1)

promote `i` and continue with `R\{i}`. If (3.1) fails, stop in the **basis-star** branch.

Then exactly one of the following holds.

**A. Diffuse residual.** There is a residual literal set `R_*` with

`D(R_*)>=eta D_0`                                              (3.2)

and every residual leverage at most `1/2`.

**B. Macroscopic literal star.** At the stopping stage there is a literal row `i` such that

`boxed: S_i(R) > (eta/2) D_0.`                                 (3.3)

### Proof

Every executed deletion preserves (3.2), so if the process reaches the leverage gate, A holds. Otherwise at the first rejected deletion the current determinant obeys `D(R)>=eta D_0`, while `ell_i(R)>1/2`. By Theorem 2.1,

`S_i(R)=D(R)ell_i(R)>(eta/2)D_0`.                              (3.4)

No estimate accumulates with the number of promotions. QED.

This resolves the determinant part of the r32 debt: repeated promotion can never merely "lose determinant invisibly." Either enough determinant survives until the analytic theorem applies, or the first unacceptable loss is itself a macroscopic literal basis-star.

## 4. Rank-one fixed-hub compiler

Return to the rank-one fixed-hub packet

`A_LL=D+lambda vv^T`,                                          (4.1)

with one literal hub `h` and physical hub column `c=A[L,h]`. Put

`x_j=(v_j,c_j)`,
`W_ij=c_i v_j-c_j v_i`,                                       (4.2)

and

`T(R)=sum_(i<j, i,j in R) W_ij^2
    =det(sum_(j in R)x_jx_j^T).`                              (4.3)

Let the initial fixed-hub disjoint one-overlap currency be

`omega=Omega_(1,h)^dis>0`.                                    (4.4)

The r31/r32 identity gives

`|lambda| T(R_0) >= sqrt(omega).`                              (4.5)

Apply Theorem 3.1.

### Corollary 4.1 — quantitative paid-or-star dichotomy

For every `eta in (0,1]`, one of the following holds.

**Paid residual branch.** The full ambient quadratic form has a continuous `C_0` density and

`boxed:
 ||p_Q||_infinity
 <= 3*2^(4/3) eta^(-1/3) omega^(-1/6),`                       (4.6)

with the identical coefficient in

`P{Q in I} <= C |I|`.                                         (4.7)

**Macroscopic physical-star branch.** For a literal original leaf coordinate `i` and a residual literal bank `R`,

`boxed:
 |lambda| sum_(j in R\{i}) (c_i v_j-c_jv_i)^2
 > (eta/2) sqrt(omega).`                                      (4.8)

### Proof

In branch A of Theorem 3.1, r32 applies to the promoted set with

`|lambda|T(R_*) >= eta |lambda|T(R_0) >= eta sqrt(omega)`,      (4.9)

which gives (4.6). In branch B, use the two-dimensional identity

`S_i(R)=sum_(j in R\{i}) W_ij^2`                              (4.10)

and multiply (3.3) by `|lambda|`, then use (4.5). QED.

There is no selected-minor loss here. The entire one-row star is kept as an `l_2` object.

### Immediate eta=1 version

Taking `eta=1` gives an especially sharp one-step compiler. Either the initial mixed frame already satisfies every leverage gate and

`||p_Q||_infinity <= 3*2^(4/3) omega^(-1/6)`,                 (4.11)

or one literal coordinate obeys

`|lambda| sum_(j!=i) W_ij^2 > (1/2)sqrt(omega).`               (4.12)

Thus "high leverage" is no longer an unscaled localization statement.

## 5. The star carries a bounded-density independent linear observable

Let the star branch (4.8) occur and define the residual linear observable

`Z_i=sqrt(|lambda|) sum_(j in R\{i}) W_ij X_j`.                (5.1)

It uses only residual original coordinates, hence it is independent of the two literal coordinates `(X_h,X_i)`.

The standard product-projection bound for independent one-dimensional densities at most one gives

`||p_(a dot X)||_infinity <= sqrt(2)/||a||_2`.                 (5.2)

Therefore (4.8) implies

`boxed:
 ||p_(Z_i)||_infinity
 < 2 eta^(-1/2) omega^(-1/4).`                                (5.3)

This is exactly a linear anti-concentration resource on the whole star; no one physical edge is selected.

For `v_i!=0`, this observable is also an actual pair-to-bank bilinear coefficient after a determinant-one change in only the two pair variables. Indeed the physical cross rows from `(X_h,X_i)` to the residual bank are

`c_R` and `lambda v_i v_R`.                                   (5.4)

The row combination

`(-v_i)c_R + [c_i/(lambda v_i)](lambda v_i v_R)
 = c_i v_R-v_i c_R
 = W_i.`                                                       (5.5)

Choose any `M in SL_2(R)` whose first column is

`(-v_i, c_i/(lambda v_i))^T`.                                 (5.6)

After writing the original physical pair as `M(Z,T)^T`, the transformed pair has joint density at most one because `|det M|=1`, and the first transformed coordinate couples to the residual bank through exactly

`2 Z (W_i dot X_R)`.                                          (5.7)

No independence between `Z` and `T` is asserted. The residual source bank remains independent of the pair. This is a literal source-valid bilinear-block normal form.

When `v_i=0`, (4.8) instead reads

`|lambda| c_i^2 ||v_R||_2^2 > (eta/2)sqrt(omega)`.             (5.8)

That is an edge-times-square-mode endpoint; it is recorded separately rather than divided by `v_i`.

The remaining mathematical gap is now precise: combine the independent rough observable (5.1), or the degenerate endpoint (5.8), with the remaining pair/core curvature without assuming a conditional density bound after rotation and without deleting arbitrary same-bank quadratic terms. The bilinear term alone has a product/log singularity, so (5.3) is not by itself a full density proof.

## 6. Concrete constants for the live r31 packet

The preceding B09 reduction produced a fixed-hub packet at scale

`omega >= 13/48`.                                              (6.1)

With `eta=1`, Corollary 4.1 says either

`boxed: ||p_Q||_infinity < 9.399`,                             (6.2)

with a continuous density and `P{Q in I}<9.399|I|`, or a literal source coordinate satisfies

`boxed:
 |lambda| sum_(j!=i)W_ij^2 > 0.2602082499...`                  (6.3)

and the independent scaled star observable (5.1) has

`boxed: ||p_(Z_i)||_infinity < 2.773.`                         (6.4)

For a softer threshold `eta=1/2`, repeated promotions are allowed until half the initial determinant remains. Then the paid branch is `<11.841`, while a failed next promotion yields weighted star currency `>0.130104...`.

These constants are not claimed sharp.

## 7. Required designated-partner application to an actual target inequality

Apply account02/B09 r19 `QFORM-TWOHUB-DOUBLE-RETENTION-v1` with `lambda=8`.

Take independent cap-one variables `U,V,Y_0,Y_1,Y_2,...,Y_9`, let `q in R^8` be any flat unit vector, and set

`Q_8 = 2(U+V)^2 + 2 U Y_0 + 2 V Y_1 + 8 <q,(Y_2,...,Y_9)>^2.` (7.1)

The literal mixed Gram in coordinates `(q,U,V)` is `I_3`. Retaining both physical hub densities gives augmented Gram `diag(1,2,2)`. The private rows `Y_0,Y_1` have augmented leverage exactly `1/2`, while the eight flat square-mode rows have leverage `1/8`.

The partner theorem therefore yields a continuous density and

`boxed: ||p_(Q_8)||_infinity <= 6*8^(-1/3)=3`,                (7.2)

`boxed: P{Q_8 in I} <= 3 |I|.`                                (7.3)

For deterministic spectral bookkeeping only, the active coefficient matrix has spectrum

`{-1, 2-sqrt(5), 1, 2+sqrt(5), 8}`.                            (7.4)

Hence it has four eigenvalues of absolute value at least one and is an actual instance of the owner's target. No transformed-coordinate independence is used in applying the theorem.

## 8. What was and was not resolved

Resolved in this run:

- exact determinant loss under source-coordinate promotion is exactly a Cauchy--Binet basis-star volume;
- a greedy promoted-frame failure can no longer be recorded merely as "small residual determinant";
- in the rank-one fixed-hub packet, macroscopic disjoint one-overlap currency forces either the r32 continuous-density estimate or a universal-scale literal Pluecker star;
- that star yields an independent linear observable with an explicit density cap and, for `v_i!=0`, appears exactly as a bilinear cross coefficient after an `SL_2` change of the physical pair.

Not resolved:

- a macroscopic star norm alone is not yet converted into a full density bound with arbitrary pair core and arbitrary same-bank curvature;
- the unrestricted QFORM conjecture remains OPEN;
- continuity remains open for the unrestricted target.

The next B09 implication is

`QFORM-MACRO-PLUECKER-STAR-RECEIVER-v1`:

> Given the source-valid star currency
> `|lambda| ||c_i v_R-v_i c_R||_2^2 >= kappa`,
> prove a universal `O(|I|)` bound by combining the entire star with the physical pair/core curvature, or force an already-paid disjoint/grouped-crossing or finite-core exit. The proof must retain arbitrary same-bank curvature and must not select a reciprocal tiny edge.

The natural first split is the exact bilinear normal form (5.5)--(5.7) for `v_i!=0` versus the edge-times-square endpoint (5.8) for `v_i=0`.

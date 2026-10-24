SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B09, 2026-09-22T19:45:35Z.
attacking: three-bank rank-one bilinear triangle aggregation as a product-preserving payment for the one-strong-cross residual, with a direct O(interval length) bound.

# account03/B09 QFORM r16 — aggregate three-bank triangle smoothing

Programme: `QFORM-DENSITY-3EIG-20260922`  
Worker: `account03/B09` — Bilinear block mechanism  
Run: `20260922T194535Z-account03-B09-QFORM-r16`  
Control at start: `yspennstate/math-research-brain@f6f1d682ca00dd33feb4778e59908c68b6ad9dd6`, OWNER CONTROL revision `2026-09-22.15`  
Control refresh before publication: `yspennstate/math-research-brain@a5d4a7d937615b03a98ffcde037b6232cb51746d`, OWNER CONTROL revision `2026-09-22.15`  
Outcome: **SUPPORTING_THEOREM_PROVED / ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**

The exact full target remains open. The theorem below proves a dimension-free, aggregate-before-inversion payment for a genuine diffuse three-bank geometry that sits inside the current `one-strong-cross` residual. It gives a direct linear interval bound and uses only original disjoint coordinate banks; no post-rotation independence, fiber supremum, arbitrary-joint coarea bound, or law-uniform pointwise Fresnel decay is used.

## 1. Source-pinned inputs and corrections

### 1.1 Completed same-role other-account theorem actually applied

The scalar logarithmic triangle theorem is account02/B09

`QFORM-ZERODIAG-TRIANGLE-LOGSMOOTH-v1`,

source

`yspennstate/math-open-problems@4b179ce358c4a728673ad9a7e3ddc2481fa287d1:proofnet24/QFORM-density/fleet-2026-09-22/account02/B09/20260922T171216Z-account02-B09-QFORM-r5/REPORT.md`.

For independent scalar `U,V,W` with density caps one, arbitrary affine terms, and nonzero `a,b,c`, it proves

`||p_(2aUV+2bUW+2cVW+affine)||_infinity <= (3+log 8)|abc|^(-1/3).`   (1.1)

The proof pays the logarithmic density singularity of one product by the third independent coordinate and does not use a square-root small-ball decoupling.

I also apply account02/B09

`QFORM-ZEROINTERNAL-BANK-WEDGE-v1`,

source

`yspennstate/math-open-problems@4b179ce358c4a728673ad9a7e3ddc2481fa287d1:proofnet24/QFORM-density/fleet-2026-09-22/account02/B09/20260922T181745Z-account02-B09-QFORM-r6/REPORT.md`.

If an original-coordinate bank has zero self block and its cross block has two singular values `s1>=s2>0`, that theorem gives

`||p_Q||_infinity <= 2 sqrt(pi)/sqrt(s1 s2)`                         (1.2)

with arbitrary curvature on the opposite bank and arbitrary conditioned outside terms. Equation (1.2) is used in the combined routing corollary below.

The designated partner `account04/B09` was checked in both the canonical current-QFORM handoff location and its run directory. No completed current-QFORM artifact was present: the available B09 records were historical installation/benchmark/MOC4 runs. I therefore do not invent or misattribute a partner theorem and continue asynchronously, using the completed account02/B09 same-role result above.

### 1.2 Projection input

I use the one-dimensional product-marginal consequence recorded in the completed account02/B09 r6 proof from the Livshyts--Paouris--Pivovarov marginal-density theorem: for independent coordinates with one-dimensional density caps one, every normalized one-dimensional orthogonal projection has density cap at most `sqrt(2)`. Thus for a nonzero vector `u` supported on an original-coordinate bank,

`||p_(<u,X>)||_infinity <= sqrt(2)/||u||_2`.                         (1.3)

This is only a marginal-density input. It is not used as a substitute for controlling an indefinite quadratic pushforward.

### 1.3 Corrections enforced

This run does not use any of the following refuted interfaces: uniform pointwise quadratic-phase decay; post-rotation independence; arbitrary-joint rank-three coarea `2/3`; positive conditional projection-density moments; a universal fixed good minor; one-heavy-row plus the same square; or the false near-zero half-Riesz continuity step. In particular, all three aggregate scalar variables below come from **disjoint original-coordinate banks**, hence are genuinely independent before any nonlinear operation.

## 2. Main theorem — a diffuse rank-one cycle across three independent banks

### Theorem 2.1 — `QFORM-THREE-BANK-RANKONE-TRIANGLE-v1`

Let `I,J,K,R` be pairwise disjoint original-coordinate sets. Let the input coordinates be independent and have probability densities bounded by one. Choose nonzero coefficient vectors

`u in R^I`, `v in R^J`, `w in R^K`,

and define the genuinely independent scalar projections

`U=<u,X_I>`, `V=<v,X_J>`, `W=<w,X_K>`.

Let `Z` be any random variable measurable with respect to the disjoint outside coordinates `X_R`; in particular `Z` is independent of `(U,V,W)`. For nonzero real `a,b,c` and arbitrary real `alpha,beta,gamma,delta`, put

`F = Z + 2a U V + 2b U W + 2c V W
       + alpha U + beta V + gamma W + delta.`                        (2.1)

Define the three aggregate cross singular strengths

`s_IJ = |a| ||u||_2 ||v||_2`,
`s_IK = |b| ||u||_2 ||w||_2`,
`s_JK = |c| ||v||_2 ||w||_2`.                                      (2.2)

Then `F` has an essentially bounded density and

`boxed: ||p_F||_infinity
 <= 2(3+log 8) (s_IJ s_IK s_JK)^(-1/3).`                            (2.3)

Hence for every interval `L`,

`boxed: P{F in L}
 <= 2(3+log 8) (s_IJ s_IK s_JK)^(-1/3) |L|.`                       (2.4)

Numerically `2(3+log 8)=10.1588830833...<10.159`.

### Proof

By (1.3), the three independent scalar variables have density caps

`M_U <= sqrt(2)/||u||_2`,
`M_V <= sqrt(2)/||v||_2`,
`M_W <= sqrt(2)/||w||_2`.                                          (2.5)

Fix the outside variable `Z=z`; it only changes the additive constant. Scale

`U_bar=M_U U`, `V_bar=M_V V`, `W_bar=M_W W`.

These remain independent and each has density cap at most one. Rewriting the conditional form in the barred variables gives the scalar triangle (1.1) with coefficients

`a_bar=a/(M_U M_V)`,
`b_bar=b/(M_U M_W)`,
`c_bar=c/(M_V M_W)`.                                                (2.6)

Therefore, uniformly in the outside value `z`,

`||p_(F|Z=z)||_infinity
 <= (3+log 8)|a_bar b_bar c_bar|^(-1/3)`
` = (3+log 8)(M_U M_V M_W)^(2/3)|abc|^(-1/3).`                     (2.7)

Using (2.5),

`(M_U M_V M_W)^(2/3)
 <= 2 (||u||_2 ||v||_2 ||w||_2)^(-2/3).`                           (2.8)

But

`s_IJ s_IK s_JK
 = |abc| ||u||_2^2 ||v||_2^2 ||w||_2^2`.                           (2.9)

Substitution of (2.8)-(2.9) into (2.7) proves (2.3). Since the bound is uniform in `z`, averaging the conditional densities over `Z` preserves it. Equation (2.4) follows by integrating the density over an interval. `QED`

### Matrix form and allowed outside couplings

The theorem applies directly to a quadratic form whose three active original-coordinate banks satisfy

`A[I,I]=A[J,J]=A[K,K]=0`,
`A[I,J]=a u v^T`,
`A[I,K]=b u w^T`,
`A[J,K]=c v w^T`.                                                     (2.10)

Arbitrary outside quadratic curvature `A[R,R]` is allowed. Moreover, couplings to the outside may be retained whenever

`range A[I,R] subset span{u}`,
`range A[J,R] subset span{v}`,
`range A[K,R] subset span{w}`.                                       (2.11)

Indeed, conditioning on `X_R` then produces exactly the arbitrary aligned affine coefficients `alpha,beta,gamma` in (2.1), while the outside quadratic part becomes the shift `Z`. Thus (2.3) is an ambient conditional theorem, not merely an isolated three-scalar identity.

## 3. Actual application to the current one-strong-cross residual

Suppose the current B09 Schur residual contains a disjoint physical cut with one strong aggregate cross direction

`a u v^T`, `s_IJ=|a|||u||||v|| >= sigma`,                             (3.1)

but lacks the second cross singular direction required by `QFORM-HALFRIESZ-TWO-CROSS-v1`. If a third disjoint original-coordinate bank supplies two coherent rank-one couplings

`b u w^T` and `c v w^T`                                              (3.2)

with

`s_IK >= tau`, `s_JK >= tau`,                                        (3.3)

and the three active self blocks/couplings satisfy (2.10)-(2.11), then Theorem 2.1 pays the formerly logarithmic one-strong-cross geometry by

`||p_Q||_infinity
 <= 2(3+log 8) (sigma tau^2)^(-1/3).`                               (3.4)

This is the precise new branch: the independent third smoother need not be a physical square or a second singular direction across the same cut; it can be a **bilinear triangle completion** through a third disjoint product bank. No selected physical coordinate coefficient is inverted.

For example, if all three aggregate strengths are at least a universal `tau>0`, then

`||p_Q||_infinity <= 10.159/tau`.                                    (3.5)

Thus the remaining `QFORM-ONE-STRONG-CROSS-HALFRIESZ-v1` debt can now exclude the coherent third-bank triangle-completion subcase. What remains is the genuinely curved/self-bank or incoherent completion geometry.

## 4. Combined aggregate routing with the completed account02/B09 wedge theorem

The new triangle certificate and the completed flat-bank two-wedge theorem give the following actual quantitative routing rule.

### Corollary 4.1 — `QFORM-BANK-CYCLE-OR-WEDGE-v1`

After conditioning only disjoint outside original coordinates, suppose either:

1. a zero-internal bank has a cross block with `s1 s2 >= tau^2`; or
2. three disjoint rank-one banks satisfy Theorem 2.1 with `s_IJ s_IK s_JK >= tau^3`.

Then respectively

`||p_Q||_infinity <= 2 sqrt(pi)/tau`                                 (4.1)

by account02/B09 r6, or

`||p_Q||_infinity <= 2(3+log 8)/tau <10.159/tau`                     (4.2)

by Theorem 2.1. Hence under either aggregate certificate

`boxed: ||p_Q||_infinity < 10.159/tau`,                              (4.3)

and the same constant multiplies every interval length. This explicitly applies the completed other-account result to an end-to-end inequality rather than citing it only descriptively.

The two branches are genuinely complementary. The wedge theorem needs two singular directions across one cut and a flat coefficient-side bank. The triangle theorem allows every individual two-bank cross block to have rank one, provided the three rank-one links close a cycle through three independent banks.

## 5. Diffuse target-valid stress family: all local entries vanish, aggregate cycle stays paid

For each `m>=2`, take three disjoint banks `I,J,K`, each of size `m`, and normalized constant vectors

`u=v=w=m^(-1/2)(1,...,1)`.

Let

`a=1`, `b=1`, `c=-1`,                                                  (5.1)

with no self blocks. The full matrix acts nontrivially only on `span{u,v,w}` and its compressed matrix is

`M=[[0,1,1],[1,0,-1],[1,-1,0]].`                                     (5.2)

Direct exact algebra gives

`chi_M(lambda)=(lambda-1)^2(lambda+2)`,                               (5.3)

so the full spectrum is

`{1,1,-2,0,...,0}`.                                                    (5.4)

This family satisfies the **exact target hypothesis** for every `m`.

All three aggregate cross strengths equal one, so Theorem 2.1 gives for every admissible product input law

`boxed: ||p_Q||_infinity <= 2(3+log 8)<10.159`,                       (5.5)

uniformly in `m`.

By contrast, every individual nonzero physical cross entry has magnitude `1/m`, and a physical triple containing one coordinate from each bank has determinant magnitude

`2/m^3`.                                                              (5.6)

The physical-coordinate triangle theorem would therefore pay a factor of order `m`. Equation (5.5) removes that loss by aggregating the bank projections **before** reciprocal local-minor inversion. This is exactly the diffuse behavior the B09 assignment is intended to handle.

The exact checker `verify.py` in this run folder verifies the three displayed eigenvectors/eigenvalues, the `2/m^3` determinant identity for representative `m`, and the numerical constant. The same identities were independently recomputed in-run; no Monte Carlo or histogram is used as proof evidence.

## 6. What this does and does not solve

Proved this run:

- `QFORM-THREE-BANK-RANKONE-TRIANGLE-v1`, equation (2.3);
- its direct `O(|L|)` consequence (2.4);
- the coherent third-bank payment (3.4) for a real subcase of the current one-strong-cross residual;
- the combined bank-cycle-or-wedge certificate (4.3), explicitly using account02/B09 r6;
- a target-valid diffuse family with entries/minors tending to zero but a uniform bank-level density bound.

Not proved:

- the general one-strong-cross branch with arbitrary same-bank quadratic curvature;
- a structural theorem forcing a triangle or wedge certificate from `s_3(A)>=1`;
- the zero/near-zero outer physical-pivot branch in full generality;
- the unrestricted QFORM conjecture;
- continuity of the density in the new branch. Only absolute continuity plus an essential `L^infinity` bound is asserted here.

The next exact B09 implication is therefore:

`QFORM-ONE-STRONG-CROSS-CURVED-BANK-v1` — starting from `s_2(S)>=1`, low physical diagonals and one strong cross singular direction, retain arbitrary self-bank curvature and prove that either a coherent third-bank triangle/wedge/ridge certificate appears at universal scale, or the remaining curved-bank operator itself supplies a translation-uniform half-Riesz payment. The `(U+V)^2` correction and the near-zero rank-one-square correction remain mandatory controls.

## 7. Integrity and operational status

The designated account04/B09 partner had no completed current-QFORM artifact at the source checks, so no such result is claimed. The complete result above is mathematical support, not a full solution and not an independent review. Repository transport occurred; no genuine native brain ingestion/receiver use was verified, hence status remains `WITHOUT_VERIFIED_BRAIN`. No schedule, task, notification, email, Drive, public workflow, paid model/API/Codex, credential, permission, or cross-account-native action was taken.

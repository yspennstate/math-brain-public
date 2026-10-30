SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B03, 2026-09-22T18:39:16Z.
attacking: convert the newly completed physical n=3 theorem into a translation-uniform analytic clamp that survives conditioning on arbitrary outside coordinates, then splice the designated partner's three-cross fractional-collision branch.

# fleet02/B03 — affine physical-triple clamp and ambient conditioning bridge

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260922T183916Z-fleet02-B03-QFORM-r13`  
Assignment: Decoupled time integral  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **ESSENTIAL_STEP_APPLIED / PROVED SUPPORTING THEOREM / FULL QFORM OPEN**.

## 1. Exact target and current corrections

The owner target remains the unrestricted statement for every dimension, every independent real input vector with one-dimensional probability densities bounded by one, and every real symmetric matrix having at least three eigenvalues of modulus at least one. The goal is one universal essential-density bound for `Q=X^TAX`, or a source-valid target counterexample. Continuity is separate.

This report does not use post-rotation independence, law-uniform pointwise Fresnel decay, arbitrary-joint rank-three coarea, normalized scalar worst-fiber bounds, conditional sum/difference density caps, or the false fixed-minor/cross-rank dichotomies already in the correction ledger. The new step is deliberately in ORIGINAL product coordinates.

## 2. Source-valid dependencies actually consumed

### 2.1 Physical n=3 theorem (fresh fleet03/B05)

Canonical source:

`yspennstate/math-open-problems@e7ffb0d5d75841126cdfaaebf2a15bb4e0f896f3`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B05/20260922T184033Z-fleet03-B05-QFORM-r15/REPORT.md`.

It proves the homogeneous `n=3` theorem from two complete ingredients: a nonzero scalar-pivot/rank-two half-Riesz branch and a quantitatively forced indefinite physical-pair branch when all scalar diagonals are small. Its explicit homogeneous constant is below 105. The report itself does not state the arbitrary-affine version needed to condition an ambient matrix on outside coordinates.

### 2.2 Translation-uniform rank-two half-Riesz theorem

Canonical source:

`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`

`proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`.

For `U^T U=I_2`, invertible symmetric `2x2` `Lambda`, independent cap-one original coordinates, and an ARBITRARY original-coordinate affine term `b`,

`sup_t E |(U^T X)^T Lambda(U^T X)+b^T X-t|^(-1/2)
 <=128 |det Lambda|^(-1/4)`.                                           (2.1)

This arbitrary-affine scope is the exact missing ingredient in the scalar-pivot branch below.

### 2.3 Full-matrix indefinite physical-pair theorem

Canonical source:

`yspennstate/math-open-problems@742ac943440e41925fe09db9a8c02a96cbd83dbc`

`proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/FULL_MATRIX_PAIR_EXTENSION.md`.

If `s_3(A)>=s>0` and an ORIGINAL-coordinate principal pair `B` is invertible indefinite, with `D=|det B|` and `kappa=sigma_min(B)`, then for arbitrary affine terms and all other coefficients arbitrary,

`||p_Q||_infinity <=3*400^(1/3)(D^2 kappa s)^(-1/6)`.                 (2.2)

### 2.4 Designated partner fleet03/B03

Fresh completed partner source:

`yspennstate/math-open-problems@20e34081fe77e8ef03c707ab0ec6d618abd61672`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B03/20260922T182338Z-fleet03-B03-QFORM-r17/REPORT.md`.

Its theorem `QFORM-PIVOT-THREECROSS-FRACTIONAL-COLLISION-v1` states that an ORIGINAL physical pivot

`Q=a(Z+h(W))^2+R(W)`

whose residual admits an ORIGINAL-coordinate cross cut with at least three singular values at least `sigma` satisfies

`||p_Q||_infinity <= C_cross |a|^(-1/2) sigma^(-1/2)`,                (2.3)

where

`C_cross=2 sqrt(3 e sqrt(pi) Gamma(1/8)/Gamma(5/8))<17.426`.

This is derived from the exact independent-copy quantity `|eta_R(t)|^2`, retaining within-pair sum/difference dependence, and a bank-level regularized determinant before fractional time integration.

## 3. New theorem: translation-uniform physical three-coordinate clamp

### Theorem 3.1 — `QFORM-AFFINE-PHYSICAL-N3-CLAMP-v1`

Let `X=(X_1,X_2,X_3)` have independent real probability densities bounded by one. Let `A` be any real symmetric `3x3` matrix with

`sigma_min(A)>=s>0`,

let `b in R^3` and `c in R` be arbitrary, and put

`Q=X^T A X+b^T X+c`.

Then `Q` has an essentially bounded density and

`boxed( ||p_Q||_infinity <= 128*2^(1/4) / s ).`                      (3.1)

No sign, support, moment, centering, continuity, or diagonal-basis assumption is imposed.

### Proof

By scaling `A=s A_0`, `b=s b_0`, `c=s c_0`, it is enough to prove the case `s=1`; density then scales by `1/s`. Thus assume

`sigma_min(A)>=1`, hence `|det A|>=1`.                                 (3.2)

Write the diagonal entries as `A_ii`.

#### Branch I: a scalar physical pivot has modulus at least `1/2`

Suppose, after relabeling,

`|a|=|A_11|>=1/2`.                                                     (3.3)

Write

`A=[[a,v^T],[v,B]]`, `b=(beta,b_Y)`, `Y=(X_2,X_3)`.

The exact square completion INCLUDING the affine term is

`Q=a [X_1+a^(-1)(v^T Y+beta/2)]^2
   +Y^T S Y+ell^T Y+c'`,                                               (3.4)

where

`S=B-vv^T/a`,
`ell=b_Y-(beta/a)v`,
`det S=det A/a`.                                                        (3.5)

Conditional on `Y`, the shifted variable in the square is a translate of the original independent `X_1`, so its conditional density is still at most one. The square pushforward therefore gives, for almost every `t`,

`p_Q(t) <= |a|^(-1/2)
            E |Y^T S Y+ell^T Y+c'-t|^(-1/2)`.                          (3.6)

Apply the arbitrary-affine rank-two theorem (2.1) with `U=I_2` and `Lambda=S`:

`||p_Q||_infinity
 <=128 |a|^(-1/2)|det S|^(-1/4)
 =128 (|a||det A|)^(-1/4)
 <=128*2^(1/4)`.                                                        (3.7)

The last step uses (3.2)-(3.3).

#### Branch II: every diagonal pivot has modulus below `1/2`

Assume

`|A_11|,|A_22|,|A_33|<1/2`.                                           (3.8)

For every standard basis vector `e_i`, (3.2) implies `||Ae_i||_2>=1`. Hence for each row

`sum_{j!=i} A_ij^2=||Ae_i||_2^2-A_ii^2>3/4`.                          (3.9)

Since there are only two off-diagonal terms in that row, some pair `i!=j` obeys

`|d|:=|A_ij|>sqrt(3/8)`.                                               (3.10)

Its principal pair

`B_2=[[alpha,d],[d,beta]]`

has `|alpha|,|beta|<1/2`, so

`det B_2=alpha beta-d^2<1/4-3/8=-1/8`.                                (3.11)

Thus it is invertible indefinite with

`D=|det B_2|>1/8`.                                                     (3.12)

Comparing with `[[0,d],[d,0]]`, whose singular values are both `|d|`, and using the singular-value Lipschitz inequality under the diagonal perturbation `diag(alpha,beta)` gives

`kappa=sigma_min(B_2)>sqrt(3/8)-1/2=(sqrt(6)-2)/4`.                    (3.13)

Apply the full-matrix pair theorem (2.2), which already allows the arbitrary affine term `b^T X+c`, with `s_3(A)>=1`. This yields exactly the B05 branch-II constant

`C_pair
 =3*400^(1/3)[128(sqrt(6)+2)]^(1/6)`.                                 (3.14)

For a purely exact comparison, `400^(1/3)<8` and

`128(sqrt(6)+2)<640<3^6=729`,

so

`C_pair<3*8*3=72<128<128*2^(1/4)`.                                    (3.15)

Thus (3.1) holds in Branch II as well. The branches are exhaustive. QED.

## 4. New ambient corollary: a good physical principal triple survives every outside coupling

### Corollary 4.1 — `QFORM-PRINCIPAL-TRIPLE-CONDITIONAL-CLAMP-v1`

Let `X=(X_1,...,X_n)` have independent cap-one densities and let `A` be an arbitrary real symmetric `n x n` matrix. Suppose there is an ORIGINAL-coordinate triple `I` such that

`sigma_min(A[I,I])>=s>0`.                                              (4.1)

Then the FULL ambient form, with every coefficient outside `I` and every cross coupling arbitrary, satisfies

`boxed( ||p_(X^T A X)||_infinity <=128*2^(1/4)/s ).`                  (4.2)

The same conclusion holds after adding an arbitrary deterministic affine term.

### Proof

Condition on the outside original coordinates `X_(I^c)=w`. Independence is preserved inside the active triple. The conditional form is

`X_I^T A[I,I] X_I + b(w)^T X_I + c(w)`,                               (4.3)

for some completely arbitrary `b(w),c(w)`. Theorem 3.1 is UNIFORM in those affine parameters, hence for every interval `J`,

`P(Q in J | X_(I^c)=w)
 <= [128*2^(1/4)/s] |J|`                                               (4.4)

for almost every `w`. Averaging (4.4) gives the same interval inequality unconditionally. Therefore the law is absolutely continuous with essential density bounded by (4.2). QED.

This is the part not supplied by the fresh homogeneous n=3 theorem: the arbitrary-affine uniformity is what makes outside conditioning source-valid.

## 5. Partner theorem applied to an actual complementary full-matrix inequality

The new principal-triple branch is complementary to the designated partner's bank-level fractional-collision theorem. In the partner notation, if a physical pivot satisfies

`|a| sigma >=1/4`                                                       (5.1)

and its Schur residual has an ORIGINAL-coordinate cross cut with at least three singular values at least `sigma`, then (2.3) gives the concrete target-level inequality

`||p_Q||_infinity
 <=2 C_cross
 <34.852`.                                                             (5.2)

No principal `3x3` block is required in this branch, and arbitrary additional spectrum/couplings remain present in the residual. Conversely Corollary 4.1 pays a good physical triple even when no residual cut has three large cross singular directions.

Thus a putative full-target counterexample surviving the currently proved local gates must simultaneously avoid:

1. every original-coordinate principal triple with a universal lower singular-value scale, and
2. every useful physical pivot whose residual has three aggregated cross singular directions at a universal scale.

The known singleton-plus-two-bank family can indeed avoid both local gates, so this is not an exhaustive proof of the full conjecture; that family is controlled only after aggregate-before-inversion. The remaining debt is therefore genuinely structural/grouped, not a defect of the three-coordinate analytic clamp or the partner's three-cross time integral.

## 6. Relation to the independent-copy assignment

The designated partner theorem used in (5.2) is explicitly an independent-copy result: it starts from

`psi(t)=|eta_R(t)|^2=E exp(it(R-R'))`,

keeps each `(U_j,V_j)=(W_j+W'_j,W_j-W'_j)` pair dependent, aggregates the full original-coordinate cross bank through the regularized determinant, and only then takes the fractional time norm. This is precisely the dependence-safe ordering required by the B03 assignment and by the prior fleet02/B03 fragmentation counterexample.

The new affine triple theorem supplies the complementary low-dimensional endpoint where bank cross-rank is too small for that determinant splice. Together they give two source-valid analytic gates with no post-rotation independence and no unsupported conditional-cap step.

## 7. Status and first unpaid implication

**New proved statement:** `QFORM-AFFINE-PHYSICAL-N3-CLAMP-v1` with exact constant `128*2^(1/4)`, and its ambient conditioning corollary (4.2).

**Partner result actually applied:** fleet03/B03 `QFORM-PIVOT-THREECROSS-FRACTIONAL-COLLISION-v1`, yielding (5.2).

**Full QFORM:** OPEN / NOT PROVED / NOT DISPROVED.  
**Continuity:** NOT PROVED by this report.

The first unpaid implication is now a product-preserving structural aggregation statement: under only `s_3(A)>=1`, and after excluding the proved principal-triple and pivot-threecross gates, force one of the completed grouped-bank/ridge/pair mechanisms without paying a reciprocal fixed-minor cost. The previously constructed singleton-plus-two-bank family remains the mandatory stress test.

No numerical or Monte Carlo computation is used in this report. A narrow pre-publication review of the changed mathematical file found no credentials, scheduler identifiers, machine paths, signed URLs, unrelated private material, benchmark content, or public-release action.

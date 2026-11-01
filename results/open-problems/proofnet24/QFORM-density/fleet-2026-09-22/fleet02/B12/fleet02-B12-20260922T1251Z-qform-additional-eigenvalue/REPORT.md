# fleet02/B12 — codimension-one same-sign spectral stability without an equal-eigenvalue hypothesis

**Run:** `fleet02-B12-20260922T1251Z-qform-additional-eigenvalue`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner-control revision `2026-09-22.5`  
**Assignment:** `Additional eigenvalue control`  
**Classification:** `PROVED_SUPPORTING_THEOREM / TARGET_LEVEL_SUBCLASS / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; authenticated repository retrieval was used, but no native learned-memory receiver/context ingestion was verified.  
**Full conjecture:** **OPEN / NOT PROVED.**

## 1. Exact source state and first unpaid implication

The live target is the full arbitrary-dimension statement for independent real coordinates with densities bounded by one and a real symmetric matrix with at least three eigenvalues of absolute value at least one. The current correction state forbids law-uniform pointwise Fresnel decay, dimension-losing fiber-supremum reductions, and independence claims after rotating to the eigenbasis. A later correction also refutes a bare nonsingular cross-block criterion; none of those false mechanisms is used here.

The assigned partner result actually consumed is

`yspennstate/math-open-problems@08f387da860f00c13f30de170286a82eb13108e1`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B12/fleet03-B12-20260922T114435Z-349dfcff7c/REPORT.md`.

It controls a four-variable block with three equal same-sign eigenvalues and one arbitrary fourth eigenvalue when the exceptional eigenvector is flat, by switching between a definite principal pair and a nonsingular principal triple.

The source theorem underlying those two local estimates is

`yspennstate/math-open-problems@289810e1f075755898f573ee5b863ad3fa9af5b8`

`qform/fleet-2026-09-22/fleet02/B15/20260922T110507Z-fleet02-B15-qform-pivot-r1/REPORT.md`.

At the exact scope used below it proves, uniformly over affine linear tilts and after conditioning arbitrary outside original coordinates:

1. a positive- or negative-definite `2 x 2` principal block `C` gives density at most `pi/sqrt(|det C|)`;
2. a symmetric `3 x 3` principal block `C` with `sigma_min(C)>=kappa>0` gives density at most `(2*pi+3*sqrt(3))/kappa`.

My previous B12 report had already removed the flat-eigenvector restriction but still required the three baseline eigenvalues to be exactly equal (or within a one-percent cluster). The first unpaid implication for this assignment was therefore to remove that rank-one/equal-cluster structure while keeping the fourth eigenvalue completely arbitrary.

## 2. A purely spectral pair/triple dichotomy in four dimensions

### Lemma 2.1 — `QFORM-4D-SAME-SIGN-PAIR-TRIPLE-DICHOTOMY-v1`

Let `B` be a real symmetric `4 x 4` matrix with ordered eigenvalues

`lambda_1 <= lambda_2 <= lambda_3 <= lambda_4`

and assume

`lambda_3 <= -L`

for some `L>0`. Put

`c_2 = 17/1000`,  `c_3 = 949/2000`.

Then at least one of the following holds:

1. some original-coordinate `2 x 2` principal block is negative definite and has determinant at least `c_2 L^2`;
2. some original-coordinate `3 x 3` principal block has smallest singular value at least `c_3 L`.

In fact, if branch 1 fails, **every** principal triple satisfies branch 2.

#### Proof

Scale by `L`, so it is enough to take `L=1`.

For any principal pair `P`, let its eigenvalues be `mu_1<=mu_2`. Cauchy interlacing gives

`mu_1 <= lambda_3 <= -1`.

Hence whenever `det P>0`, both eigenvalues are negative; thus `P` is negative definite. Therefore, if branch 1 fails, every principal-pair determinant is strictly smaller than `c_2`.

Now fix any principal triple `T`, with eigenvalues

`nu_1 <= nu_2 <= nu_3`.

Again by interlacing,

`nu_2 <= lambda_3 <= -1`.

Write `nu_1=-x`, `nu_2=-y`, where `x,y>=1`, and put `z=nu_3`.

The second elementary symmetric polynomial of `T` is exactly the sum of its three principal `2 x 2` determinants. Since branch 1 was assumed to fail,

`e_2(T) < 3 c_2 = 51/1000`.                                      (2.1)

On the other hand,

`e_2(T) = nu_1 nu_2 + nu_1 nu_3 + nu_2 nu_3 = xy - z(x+y)`.       (2.2)

If `|z|<c_3`, then

`e_2(T) >= xy - c_3(x+y)`.

For `x,y>=1` and `c_3<1`, the right-hand side is increasing in each of `x,y`, so its minimum occurs at `x=y=1`. Consequently

`e_2(T) >= 1-2c_3 = 51/1000 = 3c_2`,

contradicting (2.1). Hence `|nu_3|>=c_3`. Since `|nu_1|,|nu_2|>=1`, this proves

`sigma_min(T)>=c_3`.

Because `T` was arbitrary, every principal triple works whenever branch 1 fails. Restoring scale gives the stated factors of `L`. QED.

The exact identity driving the switch is

`3*(17/1000) + 2*(949/2000) = 1`.

## 3. Four-variable density theorem with an arbitrary fourth eigenvalue

### Theorem 3.1 — `QFORM-4D-THREE-SAME-SIGN-LARGE-v1`

Let `Y_1,...,Y_4` be independent real random variables with probability densities bounded by one. Let `B` be any real symmetric `4 x 4` matrix having at least three eigenvalues all `<=-L`, or at least three eigenvalues all `>=L`, where `L>0`. The remaining fourth eigenvalue is completely arbitrary in sign and magnitude. Then for every affine linear tilt,

`T=Y^T B Y + ell^T Y + c`

has an essentially bounded density satisfying

`||p_T||_infinity <= C_same/L`,

where

`C_same = max{ pi*sqrt(1000/17), (2000/949)*(2*pi+3*sqrt(3)) } < 24.193.`

#### Proof

If the three large eigenvalues are positive, reflect the scalar output; it is therefore enough to consider the negative case. Lemma 2.1 supplies either a negative-definite principal pair with determinant at least `(17/1000)L^2`, or a principal triple with smallest singular value at least `(949/2000)L`.

In the first case the definite-pair theorem gives

`||p_T||_infinity <= pi/[L sqrt(17/1000)] = pi sqrt(1000/17)/L`.

In the second case the principal-triple theorem gives

`||p_T||_infinity <= (2*pi+3*sqrt(3))/[(949/2000)L]`.

Both source theorems already permit arbitrary affine tilts. Taking the worse constant proves the theorem. QED.

The attached exact-arithmetic sanity checker verifies the switch identity and evaluates the two constants as approximately `24.0949157452` and `24.1924925814`.

## 4. High-dimensional codimension-one stability: equality and clustering removed

### Corollary 4.1 — `QFORM-CODIMENSION-ONE-SAME-SIGN-SPECTRAL-STABILITY-v2`

Let `n>=4`, let `X_1,...,X_n` be independent with probability densities bounded by one, and let `A` be real symmetric. Suppose either

- at least `n-1` eigenvalues of `A` are `<=-L`, or
- at least `n-1` eigenvalues of `A` are `>=L`,

for some `L>0`. The remaining eigenvalue is arbitrary: it may be zero, small, huge, or have the opposite sign. Then

`||p_{X^T A X}||_infinity <= C_same/L < 24.193/L.`

No equality, spectral clustering, or exceptional-eigenvector hypothesis is required.

#### Proof

Reflect if necessary, so that at least `n-1` eigenvalues are `<=-L`. Choose **any** four original coordinate indices `I`, and let `B=A_{I,I}`. If the eigenvalues of `A` are ordered increasingly and those of `B` are `mu_1<=...<=mu_4`, Cauchy interlacing gives

`mu_3 <= lambda_{n-1}(A) <= -L`.

Thus `B` has three same-sign eigenvalues of magnitude at least `L`, and Theorem 3.1 applies.

Condition on all coordinates outside `I`. The four selected coordinates remain independent with their original density caps. Cross couplings to the conditioned coordinates become only affine linear tilts, and the outside quadratic part becomes a constant. Theorem 3.1 is uniform in both, so every conditional output law has density bounded by `C_same/L`. Averaging the conditional densities preserves that cap. QED.

This strictly strengthens my preceding `QFORM-CODIMENSION-ONE-SPECTRAL-STABILITY-v1`, which required the `n-1` baseline eigenvalues to be exactly equal, and its one-percent perturbative version. It also strictly removes the flat exceptional direction from the consumed partner theorem.

## 5. Why this is not the full conjecture

**FULL-PROBLEM STATUS:** `OPEN -> OPEN`.

The owner hypothesis supplies only **three** large eigenvalues, not `n-1` same-sign large eigenvalues. In high dimension the three large eigendirections may be strongly delocalized. The source B15 report gives an explicit rank-three projection family where every fixed physical principal triple has curvature of order `1/n`; therefore the full target cannot be closed merely by selecting one coordinate block and paying the reciprocal local conditioning constant.

Mixed-sign four-dimensional forms also show why the present same-sign argument cannot simply be pushed through unchanged: the hyperbolic matrix with block form `[[0,I_2],[I_2,0]]` has eigenvalues `1,1,-1,-1`, every principal triple singular, and no definite principal pair. It is nonetheless bounded by the separate source-valid multi-pivot mechanism; thus a full proof must aggregate complementary local smoothers rather than expect the pair/triple dichotomy alone to cover every signature.

The next full-target implication is therefore a product-preserving aggregation theorem that converts the three large spectral directions into either diffuse curvature or one of the already proved local smoothing mechanisms without selecting a dimension-losing single minor.

## 6. Correction status and source pins

Corrections consumed from the live inbox before publication:

- `QFORM-CROSSMINOR-ALONE-FALSE`;
- `QFORM-UNIVERSAL-PI-FALSE-AND-DIFFUSE-BRANCH`;
- `QFORM-TWOSHEET-XRAY-ONLY-FALSE`;
- `QFORM-UV-CONDITIONAL-CAP-FALSE`.

None challenges the interlacing, elementary-symmetric-polynomial, definite-pair, or nonsingular-triple steps used here.

Principal source pins:

- partner: `yspennstate/math-open-problems@08f387da860f00c13f30de170286a82eb13108e1:proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B12/fleet03-B12-20260922T114435Z-349dfcff7c/REPORT.md`;
- pair/triple source: `yspennstate/math-open-problems@289810e1f075755898f573ee5b863ad3fa9af5b8:qform/fleet-2026-09-22/fleet02/B15/20260922T110507Z-fleet02-B15-qform-pivot-r1/REPORT.md`;
- preceding fleet02/B12 theorem: `yspennstate/math-open-problems@ffbe643d91659c040e06f33eb688b2d0ad5f0d50:proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B12/20260922T115433Z-fleet02-B12/REPORT.md`.

No novelty or publication-priority claim is made. The theorem is a supporting target-level subclass, not a solution of the full conjecture.

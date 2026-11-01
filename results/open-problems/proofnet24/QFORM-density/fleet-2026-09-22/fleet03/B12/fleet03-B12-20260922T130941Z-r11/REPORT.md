# fleet03/B12 — optimal pair/triple switch and arbitrary-completion stability

**Run:** `fleet03-B12-20260922T130941Z-r11`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner-control revision `2026-09-22.5`  
**Assignment:** `Additional eigenvalue control`  
**Classification:** `PROVED_SUPPORTING_THEOREM / TARGET_LEVEL_LOCAL_CRITERION / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; authenticated repository reads were used, but no native learned-memory receiver/context ingestion was verified.  
**Full conjecture:** **OPEN / NOT PROVED.**

## 1. Exact target and correction ledger

The full target is: for every dimension `n`, independent real `X_i` with probability densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of absolute value at least one, prove one dimension- and law-independent finite bound on the density of `X^T A X`, or give a valid counterexample.

This run preserves the current corrections. In particular it does **not** use a law-uniform pointwise Fresnel estimate, a dimension-free fiber supremum, independence after spectral rotation, a bare rank-two cross minor, or a conditional-density-cap substitute for genuine original-coordinate independence. Relevant live correction IDs consumed before publication include:

- `QFORM-CROSSMINOR-ALONE-FALSE`;
- `QFORM-UNIVERSAL-PI-FALSE-AND-DIFFUSE-BRANCH`;
- `QFORM-TWOSHEET-XRAY-ONLY-FALSE`;
- `QFORM-UV-CONDITIONAL-CAP-FALSE`;
- `QFORM-SINGLE-SCHUR-RANK2-EXTRACTION-FALSE`;
- `QFORM-ABSOLUTE-AMBIGUITY-HOLDER-LOG-LOSS`;
- `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1`;
- `QFORM-BOUNDED-DIAMETER-LOCALIZATION-FALSE`.

The assigned fleet04/B12 partner had no current QFORM result visible in the authorized archive at the prewrite read, so no stale FEI artifact was reused. Instead I consumed the newest compatible completed B12 result:

`yspennstate/math-open-problems@8f66972059845cb23d014fa20efee714b6655b99`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B12/fleet02-B12-20260922T1251Z-qform-additional-eigenvalue/REPORT.md`.

That report proves a purely spectral four-dimensional dichotomy and the resulting bound `<24.193/L` whenever a `4 x 4` matrix has three same-sign eigenvalues of magnitude at least `L`, with the fourth eigenvalue arbitrary. I also use the underlying source estimates from

`yspennstate/math-open-problems@289810e1f075755898f573ee5b863ad3fa9af5b8`

`qform/fleet-2026-09-22/fleet02/B15/20260922T110507Z-fleet02-B15-qform-pivot-r1/REPORT.md`:

1. a definite original-coordinate `2 x 2` principal block `P` gives affine-quadratic density at most `pi/sqrt(|det P|)`;
2. a symmetric original-coordinate `3 x 3` principal block `T` with `sigma_min(T)>=kappa` gives affine-quadratic density at most `(2*pi+3*sqrt(3))/kappa`;
3. conditioning arbitrary outside original coordinates preserves the input independence and turns all cross couplings into linear tilts.

The peer chose rational thresholds `17/1000` and `949/2000`. The new step below optimizes the switch **exactly** and then states the resulting arbitrary-completion theorem in the form needed by B12.

## 2. Exact optimal switch inside the pair/triple mechanism

Put

`C3 = 2*pi + 3*sqrt(3)`

and define

`C_* = C3 + sqrt(C3^2 + 3*pi^2)`,

`a_* = (pi/C_*)^2`,

`b_* = C3/C_*`.

Then

`3 a_* + 2 b_* = 1`,

and numerically

`C_* = 24.1830382899615...`,

`a_* = 0.0168763303644014...`,

`b_* = 0.474685504453398...`.

### Lemma 2.1 — `QFORM-4D-SAME-SIGN-OPTIMAL-PAIR-TRIPLE-v1`

Let `B` be a real symmetric `4 x 4` matrix with ordered eigenvalues

`lambda_1 <= lambda_2 <= lambda_3 <= lambda_4`

and assume `lambda_3 <= -L`, where `L>0`. Then at least one of the following holds:

1. some original-coordinate principal pair is negative definite with determinant at least `a_* L^2`;
2. every original-coordinate principal triple has smallest singular value at least `b_* L`.

Positive same-sign curvature follows by replacing `B` by `-B`.

#### Proof

Scale by `L`, so take `L=1`. Consider any principal pair `P` with eigenvalues `mu_1<=mu_2`. Cauchy interlacing gives `mu_1<=lambda_3<=-1`. Therefore if `det P>0`, then `mu_2<0`, hence `P` is negative definite.

Assume branch 1 fails. Then **every** principal-pair determinant is strictly smaller than `a_*`: positive determinants above the threshold would give branch 1, while nonpositive determinants are automatically below the positive threshold.

Now fix an arbitrary principal triple `T`, with eigenvalues `nu_1<=nu_2<=nu_3`. Interlacing gives `nu_2<=lambda_3<=-1`. Write

`nu_1=-x`, `nu_2=-y`, `nu_3=z`,

with `x,y>=1`. The second elementary symmetric polynomial of `T` is the sum of its three coordinate principal-pair determinants. Hence

`e_2(T) < 3 a_*`.                                             (2.1)

On the other hand

`e_2(T)=xy-z(x+y)`.                                            (2.2)

Suppose for contradiction that `|z|<b_*`. Then

`e_2(T) >= xy-|z|(x+y) > xy-b_*(x+y)`.

Since `b_*<1`, the last expression is increasing separately in both `x` and `y` on `[1,infinity)^2`, so

`e_2(T) > 1-2b_* = 3a_*`,

contradicting (2.1). Thus `|nu_3|>=b_*`. Since `|nu_1|,|nu_2|>=1>=b_*`, we have `sigma_min(T)>=b_*`. Because `T` was arbitrary, every principal triple satisfies branch 2. Restoring scale proves the lemma. QED.

### Why the constants are optimal for this exact two-branch proof

If one uses a pair determinant threshold `a` and a triple singular-value threshold `b`, the above elementary-symmetric argument requires

`3a+2b<=1`.

The source density estimates then cost

`max{pi/sqrt(a), C3/b}`.

Increasing either `a` or `b` only improves the corresponding density bound, so an optimum lies on `3a+2b=1`. At the minimax point the two costs are equal:

`pi/sqrt(a) = C3/b = C`.

Substituting `a=(pi/C)^2` and `b=C3/C` into the frontier gives

`C^2 - 2 C3 C - 3 pi^2 = 0`,

whose positive root is precisely

`C=C_* = C3 + sqrt(C3^2+3*pi^2)`.

Thus no other choice of thresholds can improve the constant within this exact pair/triple + source-estimate mechanism.

## 3. Improved four-variable theorem

### Theorem 3.1 — `QFORM-4D-THREE-SAME-SIGN-LARGE-OPT-v1`

Let `Y_1,...,Y_4` be independent real variables with probability densities bounded by one. Let `B` be any real symmetric `4 x 4` matrix having at least three eigenvalues all `<=-L`, or at least three eigenvalues all `>=L`, where `L>0`. The fourth eigenvalue is arbitrary in sign and magnitude. Then for every affine linear tilt,

`T=Y^T B Y + ell^T Y + c`

has an essentially bounded density satisfying

`||p_T||_infinity <= C_*/L`,

with

`C_* = 24.1830382899615...`.

#### Proof

Reflect the scalar output in the positive case. Apply Lemma 2.1 in the negative case. In branch 1, the definite-pair theorem gives

`||p_T||_infinity <= pi/(L sqrt(a_*)) = C_*/L`.

In branch 2, the principal-triple theorem gives

`||p_T||_infinity <= C3/(b_* L) = C_*/L`.

The affine tilt is already permitted in both source theorems. QED.

The previous compatible peer constant was approximately `24.1924925814`; this lowers it by about `0.0094542914`, or `0.0391%`. The improvement is small numerically but exact and closes the optimization of this local mechanism.

## 4. Arbitrary added eigenvalues and cross-couplings once a physical block is certified

### Theorem 4.1 — `QFORM-LOCAL-4BLOCK-ARBITRARY-COMPLETION-v1`

Let `A` be any real symmetric `n x n` matrix, `n>=4`. Suppose there is a set `J` of four **original coordinate indices** for which the physical principal block `B=A[J,J]` has three eigenvalues all `<=-L` or all `>=L`. Make **no assumption at all** on the rest of `A`: the other eigenvalues may be smaller or larger, of either sign, and the cross couplings `A[J,J^c]` may be arbitrary.

For independent input coordinates with densities bounded by one,

`||p_{X^T A X}||_infinity <= C_*/L`.

#### Proof

Condition on `X_{J^c}=w` in the original independent coordinate system. The selected four variables retain their original independence and density caps. The conditional polynomial is

`X_J^T B X_J + 2 X_J^T A[J,J^c] w + w^T A[J^c,J^c]w`.

The second term is only a linear tilt in the four selected variables and the third is a scalar constant. Theorem 3.1 therefore bounds every conditional output density by `C_*/L`, uniformly in `w`. Averaging the conditional densities preserves the same essential-supremum bound. QED.

This is the precise B12 stability statement: **additional eigenvalues do not automatically help, but they also cannot hurt once a suitable physical principal block has been certified**, because outside matrix completion is handled by conditioning rather than by a false independent-convolution claim.

### Corollary 4.2 — improved codimension-one same-sign stability

If at least `n-1` eigenvalues of `A` are `<=-L`, or at least `n-1` are `>=L`, then

`||p_{X^T A X}||_infinity <= C_*/L`.

Indeed choose any four original coordinates. Cauchy interlacing gives three same-sign eigenvalues of the selected `4 x 4` principal block at scale `L`; apply Theorem 4.1.

This sharpens the compatible fleet02/B12 constant while preserving its complete freedom in the remaining eigenvalue.

## 5. Stress test and exact limitation

The local same-sign mechanism cannot be promoted unchanged to all four-dimensional signatures. The standard hyperbolic block

`H = [[0,I_2],[I_2,0]]`

has eigenvalues `1,1,-1,-1`, every coordinate principal triple is singular, and no coordinate principal pair is definite. Thus the pair/triple lemma genuinely uses three same-sign large directions. This does **not** make `H` a counterexample to QFORM; other source-valid multipivot/cross-block mechanisms control such forms.

Likewise, in high dimension the full owner hypothesis gives only three large eigenvalues, not `n-1` same-sign ones. Delocalized rank-three spectral subspaces can make every fixed small coordinate minor weak. The full target therefore remains OPEN.

## 6. First unpaid implication after this run

The exact remaining bridge is now more sharply separated:

> Given only three large spectral directions in arbitrary dimension, prove a product-preserving aggregation/dichotomy that yields either (i) a local four-coordinate same-sign block covered by Theorem 4.1, (ii) a diffuse rank-three/separable-phase block covered by the completed diffuse theorem, or (iii) a mixed-sign multipivot/cross-block smoother with a dimension-free quantitative certificate.

The next B12 attack should therefore move away from further optimization of the same local pair/triple constants and toward an aggregate criterion that is stable under arbitrary spectral remainder. In particular, proving a codimension-two scalar-baseline-plus-rank-two exceptional theorem would be a meaningful next step; a single-minor extraction theorem is known to be insufficient in the fully delocalized branch.

## 7. Provenance and status

Fresh prewrite control remained revision `2026-09-22.5`; no later fleet03/B12 pause or stop was observed. This report is source-bound mathematical work, not a claim of native brain ingestion. No scheduler mutation, email, Drive action, public release, paid call, remote workflow, credential use, or cross-account scheduler action was performed.

**Full QFORM:** `OPEN / NOT PROVED`.  
**New local theorem:** `PROVED` conditional on the cited source pair/triple density estimates.  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`.

SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B18, 2026-09-22T23:02:22Z.
attacking: the rank-two physical cross-cut gap left by the partner rank>=3 Fresnel theorem, retaining original-coordinate product provenance and arbitrary curvature on the opposite bank.

# account02/B18 — zero-self-block cross smoothing from product marginals

**Programme:** QFORM-DENSITY-3EIG-20260922  
**Assignment:** Literature-to-proof transfer  
**Status:** `PROVED_SUPPORTING_TARGET_LEVEL_BRANCH / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Live target and first unpaid implication

The full target remains OPEN: for independent real coordinates with probability densities bounded by one and arbitrary real symmetric A with at least three eigenvalues of modulus at least one, prove one universal dimension-independent bound on the density of X^T A X, or give a valid counterexample. No moment, support, centering, log-concavity, identical-law, smoothness, or independence-after-rotation assumption is used below.

The newest completed designated partner account03/B18 r19 proves `QFORM-CROSSBLOCK-RANKGE3-FRESNEL-v1`: under a physical bipartition, arbitrary measurable self-curvature on both banks is harmless when the cross block has rank r>=3, with density bound `[2r/(r-2)] (prod sigma_l)^(-1/r)`. Its method stops sharply at cross rank two because the absolute Fourier majorant becomes |t|^-1.

This run attacks the complementary rank-two threshold without inventing pointwise Fourier decay. The structural restriction is explicit: one physical bank must have zero quadratic self-block (affine terms are allowed). Under that restriction the physical variables on that bank enter linearly, so a one-dimensional projection-density theorem can be averaged against the actual product-projection law of the cross coefficient.

## 2. Primary source transferred exactly

Livshyts--Paouris--Pivovarov, *On sharp bounds for marginal densities of product measures*, Israel J. Math. 216 (2016), arXiv:1507.07949, Theorem 1.1: if a probability density on R^n is a product of one-dimensional probability densities bounded by one, then every k-dimensional orthogonal marginal has L-infinity norm at most `2^(k/2)` (indeed their theorem gives the sharper minimum with `(n/(n-k))^((n-k)/2)` when k<n). No moment, support, symmetry, identical-law, log-concavity, or smoothness assumption is present.

Two exact consequences used here are:

1. every unit one-dimensional linear aggregate of a physical product bank has density cap `sqrt(2)`;
2. every r-dimensional orthogonal marginal has density cap `2^(r/2)`.

When the projection dimension equals the whole bank dimension, no marginal theorem is needed: the orthogonal image has the same joint density cap at most one, so the weaker cap `2^(r/2)` still holds.

The newest Claude source `COUNTEREXAMPLE_SEARCH.md`, Theorem B, independently uses the same product-valid two-dimensional marginal cap in a physical-coordinate fiber calculation. The result below changes the payment: instead of summing coordinate leverage and losing dimension, it integrates a reciprocal linear coefficient over an actual rank-r cross image.

## 3. Main theorem — `QFORM-ZEROBLOCK-CROSSRANK2PLUS-v1`

Let I,J be disjoint sets of original independent coordinates, with `|I|=m`, and let

`Q = G(X_J) + ell^T X_I + 2 X_I^T B X_J`,

where G is an arbitrary real measurable function, `ell in R^m`, and B is an `m x |J|` real matrix of rank `r>=2`. Let the nonzero singular values of B be

`sigma_1 >= ... >= sigma_r > 0`,

put `D=prod_{k=1}^r sigma_k`, and let `v_r=pi^(r/2)/Gamma(r/2+1)` be the Euclidean unit-ball volume in R^r. Then Q has an essentially bounded density satisfying

`||p_Q||_infinity <= [r/(r-1)] v_r^(1/r) D^(-1/r)`.      (3.1)

In particular, for cross rank two,

`||p_Q||_infinity <= 2 sqrt(pi) (sigma_1 sigma_2)^(-1/2)`.      (3.2)

The theorem allows completely arbitrary quadratic curvature on the J-bank, by taking `G(X_J)=X_J^T A_JJ X_J + linear + constant`. Thus for a symmetric quadratic form it applies whenever a physical block I satisfies `A_II=0` and the physical cross block `A_IJ` has rank at least two.

### Proof

Take a thin SVD

`B=P Sigma R^T`,

where P and R have orthonormal columns and `Sigma=diag(sigma_1,...,sigma_r)`. Define

`W=R^T X_J`, `Y=B X_J=P Sigma W`.

Because X_J is still an original-coordinate product source, LPP gives

`||p_W||_infinity <= 2^(r/2)`

for a proper marginal. In the full-dimensional case the direct cap is at most one. Hence in every case Y has an r-dimensional density on `E=Ran B` satisfying

`||p_Y||_infinity <= K := 2^(r/2)/D`.      (3.3)

Now condition on `X_J=z`. Write `y=Bz`. The conditional random part on the I-bank is the genuine original-product linear form

`<ell+2y, X_I>`.

Since `r>=2`, necessarily `m>=2`. If `a=ell+2y` is nonzero, the k=1 LPP theorem applied in the direction `a/||a||` gives the conditional density cap

`||p_{<a,X_I>}||_infinity <= sqrt(2)/||a||`.      (3.4)

Let `ell_E` be the orthogonal projection of ell onto E and set `y_0=-ell_E/2`. Then

`||ell+2Y|| >= 2 ||Y-y_0||`.

The affine r-plane carrying Y has an absolutely continuous r-dimensional law, so the exceptional event `ell+2Y=0` has probability zero. Therefore the mixture density obeys

`||p_Q||_infinity <= (1/sqrt(2)) E[ ||Y-y_0||^(-1) ]`.      (3.5)

For `R_0=||Y-y_0||`, the density cap (3.3) gives, for every u>0,

`P(R_0 <= u) <= min(1, K v_r u^r)`.      (3.6)

Using the layer-cake identity for `R_0^(-1)` and splitting at `s_0=(K v_r)^(1/r)`,

`E R_0^(-1)
 <= s_0 + K v_r integral_{s_0}^infinity s^(-r) ds
 = [r/(r-1)] (K v_r)^(1/r)`.      (3.7)

Substitute `K=2^(r/2)/D` into (3.5)-(3.7). The factor `2^(1/2)` from `K^(1/r)` cancels the `1/sqrt(2)` in (3.5), yielding exactly (3.1).

No coordinate of Y was assumed independent of another. The only independence used is the original physical-bank independence: X_I is independent of X_J, hence independent of the entire random coefficient Y=B X_J.

### Continuity note

The target asks for an L-infinity density, which is already proved. In fact continuity also follows. For almost every y, the vector `ell+2y` has at least two nonzero physical coordinates: the exceptional set where an r-dimensional affine plane with r>=2 lies in the finite union of coordinate axes has r-dimensional measure zero. For such y, the conditional density is a convolution of at least two L1 densities and is continuous. The integrable dominator in (3.5)-(3.7) then permits dominated convergence after the arbitrary shift G(z).

## 4. Sharper two-pivot special case

If `|I|=2` and `rank B=2`, conditioning on Y=(Y_1,Y_2) gives a convolution of the two scaled physical densities. After absorbing ell/2 into the coefficient center,

`||p_{Q|X_J}||_infinity <= 1/[2 max(|Y_1-y_{0,1}|,|Y_2-y_{0,2}|)]`.

The joint density of Y is at most `K<=2/D`. If `R_infinity=max(|Y_1-y_{0,1}|,|Y_2-y_{0,2}|)`, then

`P(R_infinity<=u)<=min(1,4K u^2)`

and layer cake gives `E[1/(2R_infinity)]<=2 sqrt(K)`. Therefore

`boxed: ||p_Q||_infinity <= 2 sqrt(2) (sigma_1 sigma_2)^(-1/2)`      (4.1)

for this exact two-physical-pivot zero-self-block branch. This improves the generic r=2 constant `2sqrt(pi)`.

## 5. Direct application of the completed partner result

The completed account03/B18 r19 theorem at `math-open-problems@9415d0f2696d2e6ca05243c8e8f34b665bf5d42f` proves, for a physical cross block of rank `r>=3`,

`||p_Q||_infinity <= [2r/(r-2)] D^(-1/r)`

with arbitrary measurable self-curvature on both banks.

Combining it with (3.1) gives the following source-pinned two-tier cross-cut rule:

- if a physical cut has cross rank `r>=3`, arbitrary self-curvature is paid by the partner Fresnel theorem;
- if a physical cut has cross rank `r>=2` and one bank has zero quadratic self-block, the present reciprocal-coefficient theorem pays it, including the formerly logarithmic rank-two threshold.

For r>=3 and a zero self-block, (3.1) is also quantitatively stronger: its constants are `c_3=(3/2)(4pi/3)^(1/3)=2.4179879...`, `c_4=1.9872667...`, etc., versus the partner's constants `6,4,...`; but the partner is much more general because it retains arbitrary curvature on both sides.

This is a genuine application, not a claim that the bare spectral hypothesis forces such a cut. The live correction family `[1] direct_sum J_m/m direct_sum (-J_m/m)` has every physical cut of cross rank at most two and does not contain a useful zero self-block. It is therefore not closed by (3.1).

## 6. Source-valid status and next unpaid implication

**FULL TARGET CHANGE:** `OPEN -> OPEN`.

The new theorem closes a previously unhandled, target-valid structural class: rank-two cross smoothing can be dimension-free when product provenance is retained and one physical bank is affine rather than quadratically curved. It does not use the refuted arbitrary-joint coarea lemma, a conditional-density supremum, post-rotation independence, a fixed well-conditioned principal minor, or uniform pointwise quadratic-phase decay.

The first unpaid interface is now sharper:

`QFORM-RANK2-CROSSCUT-SELF-CURVATURE-v1` — when the best surviving physical cross cut has rank exactly two, retain nonzero quadratic self-curvature on the low-rank side and prove a universal payment from the global three-large-eigenvalue hypothesis, or route that matrix by a source-valid structural theorem into an existing square-pivot, grouped-bank, ridge-window, mixed-hub, or diagonal branch.

This is precisely where the present proof fails: once `A_II` is nonzero, conditioning on the opposite bank leaves a quadratic, not linear, form in X_I; the reciprocal-coefficient estimate (3.4) no longer applies, while the partner's rank>=3 L2/Fresnel time integral is logarithmically nonintegrable at rank two.

## 7. Source pins and correction status

- Fresh brain control snapshot used at entry: `e2f66606906db9d48887fb4b4b04195de4b1b9b8`, OWNER CONTROL revision `2026-09-22.15`.
- LPP primary source: arXiv:1507.07949, Theorem 1.1; exact marginal cap used above.
- Newest owner-required Claude source: `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, especially `COUNTEREXAMPLE_SEARCH.md` Theorem B and `FOURIER_ROUTE_REPORT.md`.
- Completed designated partner account03/B18 r19: handoff commit `86e7fb46b1a8535041e77e9864e44caf0175b551`; canonical theorem `math-open-problems@9415d0f2696d2e6ca05243c8e8f34b665bf5d42f`, `ADDENDUM_CROSSBLOCK.md`.
- Corrections respected: no independence after rotation; arbitrary-joint coarea false; conditional projection positive moments false; fiberwise trace/supremum mechanisms false; no universal rank-three cross-cut extraction; no uniform pointwise quadratic-phase decay.

Manual changed-file review: mathematical text, public source identifiers, logical fleet labels, and repository-relative source paths only; no credentials, scheduler identifiers, machine paths, unrelated private data, benchmark material, or public-release action.

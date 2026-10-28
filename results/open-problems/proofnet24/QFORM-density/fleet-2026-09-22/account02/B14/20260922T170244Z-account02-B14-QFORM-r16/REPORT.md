# account02/B14 — mass-linear localization interface and exact no-normalization barriers

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Owner control observed for publication:** revision `2026-09-22.8`  
**Run:** `20260922T170244Z-account02-B14-QFORM-r16`  
**Assignment:** Translations and localization  
**Status:** `SUPPORTING_LOCALIZATION_THEOREM + SOURCE-VALID_MECHANISM_COUNTEREXAMPLES / FULL_CONJECTURE_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and first unpaid implication

The target remains the full uniform-cube-free quadratic-form statement: for every finite `n`, every independent real `X_i` with probability densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of absolute value at least one, prove

\[
\Pr\{X^TAX\in I\}\le C|I|
\]

for one finite universal `C`, every bounded interval `I`, all dimensions, rotations, signatures, and additional eigenvalues, or produce a genuine counterexample.

The first unpaid B14 implication is no longer compactification itself. The completed assigned partner account03/B14 theorem gives exact law-level reduction to compact finite-fragment extreme-product inputs with the same best small-ball constant. The missing localization interface is:

> **When a proof further decomposes an extreme product law into small fragments or thin conditional slices, what quantitative form of the local estimate can be summed back without reintroducing support, fragment-count, or density-cap losses?**

This report proves an exact mass-linear compiler and then gives three target-valid obstruction families showing that normalized-fragment cap loss, support-location loss, or moment loss cannot be tolerated. This is a mechanism change from the preceding B14 inverse-gap graph estimates: the argument is now purely measure-decomposition/homogeneity, with no pair-gap or finite-graph singularity estimate.

## 2. Completed partner result actually consumed

I use the complete account03/B14 report

`yspennstate/math-open-problems@871a2d4c9f1ea58d89748ab1abab05021b4408de`

at

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B14/20260922T153828Z-account03-B14-QFORM-r13/REPORT.md`.

Its theorem is: every admissible one-dimensional density is an `L1` limit of finite convex combinations of compact finite-union indicator densities `1_E`, `|E|=1`; tensor products give a total-variation approximation of the whole product law by finite convex mixtures of compact extreme-product laws. Consequently, for each fixed symmetric `A`, the optimal small-ball constant over all admissible product laws equals exactly the optimal constant over compact finite-fragment extreme-product laws. No moment, support-diameter, translation, separation, or fixed-fragment-count bound is imposed.

I also retain the later correction `QFORM-CONDITIONAL-3D-PROJECTION-CAP-FALSE-v1` from account02/B17: normalizing a thin spectral slice can make the conditional 3D density cap arbitrarily large even for a target-class Hadamard product source. The replacement is to retain unnormalized slice mass through the curved trace; no universal raw integrated-fiber-sup theorem is asserted.

## 3. Main positive theorem: mass-linear localization compiler

Let `Q:R^n->R` be any measurable map; in the application `Q(x)=x^TAx`.

### Theorem 3.1 — `QFORM-MASS-LINEAR-LOCALIZATION-COMPILER-v1`

Let `nu` be a probability measure on `R^n` and suppose

\[
\nu=\sum_{\alpha\in\mathcal A}\nu_\alpha
\]

is a finite positive decomposition into subprobability measures. Write

\[
w_\alpha:=\nu_\alpha(\mathbb R^n),\qquad \sum_\alpha w_\alpha=1.
\]

Assume that for each `alpha` there is a nonnegative certificate constant `C_alpha` such that for every bounded interval `I`,

\[
\nu_\alpha\{Q\in I\}\le w_\alpha C_\alpha |I|. \tag{3.1}
\]

Then

\[
\nu\{Q\in I\}\le \left(\sum_\alpha w_\alpha C_\alpha\right)|I|. \tag{3.2}
\]

In particular, if `C_alpha<=C` for all `alpha`, then `nu` has the same small-ball constant `C`; no localization tax occurs.

### Proof

Positivity gives

\[
\nu\{Q\in I\}=\sum_\alpha \nu_\alpha\{Q\in I\}.
\]

Insert (3.1) and sum. No normalization of the pieces is used. `QED`

The point is not the algebraic summation itself; it is the exact admissible interface. A fragment or slice may be arbitrarily small, but its local estimate must be **linear in the unnormalized mass actually carried by that piece**, or its weighted average must be controlled by some separate argument. Any proof that first normalizes every tiny piece and then pays an unbounded cap/support penalty is outside this compiler.

### Corollary 3.2 — full-target transfer through the partner localization

Let `C` be a constant such that every compact finite-fragment extreme-product law in the partner class admits some finite positive decomposition satisfying (3.1) with

\[
\sum_\alpha w_\alpha C_\alpha\le C. \tag{3.3}
\]

The decomposition and even the local certificate mechanism may depend on the extreme product law. Then **every** admissible independent cap-one product law satisfies

\[
\Pr\{X^TAX\in I\}\le C|I|.
\]

### Proof

For every extreme-product law, Theorem 3.1 gives the bound with constant `C`. The account03/B14 law-level convex-mixture theorem says every admissible product law is a total-variation limit of finite convex mixtures of such extreme-product laws, independently of the test interval. Convex mixtures preserve the same interval bound, and total-variation convergence passes it to the limit. `QED`

Thus a law-dependent active block or local mechanism is permitted at the extreme-law level, provided the resulting certificate is mass-linear after all local pieces are summed. What is forbidden is hidden renormalization loss.

## 4. Exact zero-tax case: select before localizing

Let `S` be a fixed set of original coordinates and write `z=x_{S^c}`. Suppose a deterministic-outside theorem proves

\[
\Pr\{Q(X_S,z)\in I\}\le K|I| \tag{4.1}
\]

for every deterministic `z` and every admissible product law on the active coordinates `S`, with the same `K`.

Partition or otherwise decompose only the outside law into positive submeasures `rho_alpha` of masses `w_alpha`. On piece `alpha`, integrate (4.1) against `rho_alpha`; the contribution is at most

\[
w_\alpha K|I|.
\]

Hence Theorem 3.1 sums the pieces to exactly `K|I|`.

This recovers, in the precise mass-linear language, account03/B14's completed **select-before-localize** principle: tails, distant fragments, fragment counts, and arbitrary outside translations cost exactly zero when the active original-coordinate block is kept unfragmented and its estimate is uniform in the deterministic outside parameters. It also explains why the current orientation-free rank-two affine half-Riesz theorem is a compatible ingredient only when its active product-linear provenance is retained rather than rebuilt from normalized thin fragments.

## 5. First obstruction: normalized-fragment cap loss is unsummable

### Theorem 5.1 — `QFORM-NORMALIZE-THEN-CAP-BARRIER-v1`

For each integer `N>=1`, define the compact measure-one set

\[
E_N=\bigcup_{k=1}^N
\left[\frac{2(k-1)}N,\frac{2k-1}N\right]. \tag{5.1}
\]

The density `1_{E_N}` is admissible, supported in `[0,2]`, and has exactly `N` connected fragments, each of mass `1/N`.

Conditioning on a fragment and renormalizing it produces the probability density

\[
N\,1_{I_k},
\]

whose `L^infinity` cap is exactly `N`.

Therefore any fragmentwise proof architecture whose only local theorem supplies a normalized conditional constant of the form

\[
C F(M)
\]

when the normalized density cap is `M`, mechanically yields after mixture summation the bound

\[
\frac1N\sum_{k=1}^N C F(N)=C F(N). \tag{5.2}
\]

If `F(M)` is unbounded, this architecture cannot produce a universal constant from arbitrary fragmentation, even though the support stays in the fixed compact interval `[0,2]`.

More generally, if `m` independently fragmented coordinates each have `N_i` equal pieces and a local theorem pays

\[
\prod_{i=1}^m M_i^{\theta_i},\qquad \theta_i\ge0,
\]

then the normalized-box summation pays exactly

\[
\prod_{i=1}^m N_i^{\theta_i}. \tag{5.3}
\]

Thus **any positive homogeneity in a normalized fragment cap is fatal unless another pre-normalization packing/cancellation estimate removes it.**

This is a counterexample to the normalize-then-pay proof mechanism, not to QFORM. It is consistent with the account02/B17 correction: thin-slice normalization can create arbitrarily large conditional density caps, so the correct object is unnormalized slice mass until after the curved/product aggregation.

## 6. Second obstruction: three fragments already destroy every unbounded location penalty

### Theorem 6.1 — `QFORM-THREE-FRAGMENT-DISTANT-SHIFT-BARRIER-v1`

For `R>1`, let

\[
E_R=[-R-1/4,-R]\cup[-1/4,1/4]\cup[R,R+1/4]. \tag{6.1}
\]

Then `|E_R|=1`, `1_{E_R}` is an admissible probability density, the support has exactly three interval components, and the law is symmetric with median zero.

Let `Psi:[0,infinity)->[0,infinity)` be nondecreasing. If a fragmentwise certificate pays the mass-weighted location cost

\[
\sum_{J\in\pi_0(E_R)} |J|\,\Psi(\operatorname{dist}(0,J)),
\]

then the two outer fragments give

\[
\sum_J |J|\Psi(\operatorname{dist}(0,J))
\ge \frac12\Psi(R). \tag{6.2}
\]

Hence every unbounded location/separation penalty can be made arbitrarily large with **only three fragments and in median-zero gauge**.

This is not target difficulty. Take three independent copies of this law and `A=I_3`. The proved diagonal theorem applies for every `R` and gives

\[
\|p_{X_1^2+X_2^2+X_3^2}\|_\infty\le\pi. \tag{6.3}
\]

Thus a localization argument that grows with absolute fragment location, support diameter, or separation is paying an artifact that is absent even in a uniformly solved target family.

## 7. Third obstruction: every positive moment may be infinite inside the target

### Theorem 7.1 — `QFORM-NO-MOMENT-LOCALIZATION-WITNESS-v1`

For `k>=1`, let

\[
a_k=2^{-k-1},\qquad R_k=2^{k^2},
\]

and define the symmetric measurable set

\[
E=\bigcup_{k\ge1}
\Big([R_k,R_k+a_k]\cup[-R_k-a_k,-R_k]\Big). \tag{7.1}
\]

Its measure is

\[
|E|=\sum_{k\ge1}2a_k=\sum_{k\ge1}2^{-k}=1,
\]

so `f=1_E` is an admissible probability density. It is symmetric, hence median zero. For every `p>0`,

\[
\int |x|^p f(x)\,dx
\ge\sum_{k\ge1} 2a_k R_k^p
=\sum_{k\ge1}2^{-k}2^{p k^2}
=\infty. \tag{7.2}
\]

Thus **all positive moments are infinite**.

Nevertheless, for three independent copies and `A=I_3`, the same diagonal theorem gives the uniform output-density bound `<=pi`. Hence no finite moment is a hidden target hypothesis, and no localization proof may leave a final constant depending on moments.

The obstruction already appears in compact finite-fragment approximants. Truncate (7.1) at `k<=N`, whose total mass is `1-2^{-N}`, and add a symmetric central interval of length `2^{-N}`. The resulting compact symmetric finite-union set has total measure one, while its `p`th moment tends to infinity with `N` for every fixed `p>0`. The output density for `A=I_3` remains bounded by `pi` for every `N`.

More generally, for any prescribed nondecreasing unbounded tail penalty `Phi`, choosing `R_k` so that `Phi(R_k)>=2^{2k}` makes

\[
\int Phi(|x|)1_E(x)\,dx
\ge\sum_k 2^{-k}2^{2k}=\infty. \tag{7.3}
\]

So no unbounded radial localization penalty can be averaged uniformly under the original hypotheses.

## 8. Consequence for the current proof-first synthesis

The completed partner localization theorem is exact, but this report sharpens the admissible downstream interface:

1. **Safe:** leave the active original-coordinate mechanism unfragmented; localize only variables that enter it as deterministic parameters. Uniformity in those parameters gives a mass-linear certificate and zero localization tax.
2. **Safe:** decompose into positive submeasures only when the local estimate is already proportional to the unnormalized component mass, or when the weighted average in (3.3) is proved directly before normalization.
3. **Unsafe without extra structure:** normalize tiny fragments or thin slices and then invoke a theorem with any unbounded dependence on the resulting density cap.
4. **Unsafe:** pay any unbounded support-location, separation, diameter, or moment factor and hope the arbitrary-law hypotheses will average it away.

This interfaces directly with the proof-first owner continuation and the current rank-two affine half-Riesz theorem. That theorem is valuable because it is translation-uniform in the original product law; the remaining synthesis should preserve that provenance. A future curved-kernel or determinant/Pluecker aggregation must therefore be written at the **unnormalized mass level** (or select its active block before outside localization), not as a normalized fragment estimate with a later average.

## 9. First unpaid implication after this run

For B14 the next exact implication is:

> **QFORM-UNNORMALIZED-CURVED-CERTIFICATE-v1.** In one of the surviving heavy/localized branches, derive a deterministic-outside or weighted curved/half-Riesz estimate on positive submeasures whose contribution is linear in the submeasure mass before any tiny fragment/slice normalization; equivalently, prove a weighted-average certificate of the form (3.3). The active original-coordinate product structure and arbitrary affine translations must remain visible.

If a proposed bridge necessarily pays a positive power of a normalized fragment cap, an unbounded center/separation factor, or a moment factor, Theorems 5.1--7.1 show that this localization route cannot be universal and should be abandoned rather than hidden in a compactification step.

This is a supporting theorem/correction to proof architecture, not a full solution. The universal QFORM conjecture remains OPEN.

## 10. Source pins and integrity

- Control repository snapshot used immediately before publication: `yspennstate/math-research-brain@5409f30d9883f7d4dc3cc11348a3f817251a214e`, owner control revision `2026-09-22.8`.
- Assigned partner complete report: `yspennstate/math-open-problems@871a2d4c9f1ea58d89748ab1abab05021b4408de`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B14/20260922T153828Z-account03-B14-QFORM-r13/REPORT.md`, blob `af0567bbeccf3e204d94b89c7d1083b9a2f8a33f`.
- Later source-backed correction consumed: `QFORM-CONDITIONAL-3D-PROJECTION-CAP-FALSE-v1`, account02/B17, canonical report commit `f117a4870969d37706b8d7e62cbcae671cc2d3b0`.
- Diagonal `pi` theorem source/status: current programme state `CURRENT_RESEARCH.md`; it is used only in its proved diagonal scope.

Changed-file privacy review was manual and limited to this mathematical report: no credentials, account secrets, scheduler identifiers, machine paths, private personal data, benchmark gold, or public-release material are included. No paid call, remote workflow, email, notification, permission change, or cross-account authentication was used.

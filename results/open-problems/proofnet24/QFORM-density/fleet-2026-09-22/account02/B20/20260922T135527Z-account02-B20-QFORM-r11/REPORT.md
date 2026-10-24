# account02/B20 — near-null bank extraction and cap-refunded square cascade

Programme: `QFORM-DENSITY-3EIG-20260922`  
Owner revision: `2026-09-22.5`  
Run: `20260922T135527Z-account02-B20-QFORM-r11`  
Assignment: Proof closure and keeper / SYNTHESIS  
Status: `ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and correction-aware scope

For every dimension, independent real coordinates with one-dimensional probability densities at most one, and every real symmetric matrix with at least three eigenvalues of absolute value at least one, the target asks for one universal finite essential-supremum bound on the density of `Q=X^TAX`, or a genuine counterexample.

This report keeps original-coordinate independence. It does not use law-uniform pointwise quadratic-phase decay, unrestricted spectral-fiber suprema, independence after an orthogonal diagonalization, a single uniformly good coordinate minor, or conditional-cap-as-independence. Continuity is not inferred from an `L^infinity` density bound.

## 2. Current conditional proof assembly

The present source-valid assembly pays several large branches.

- Full-range diffuse geometry is covered by the regularized-determinant theorem recorded in the live control state.
- In exact rank three, the diffuse spectral-frame branch is covered by the Fourier--Brascamp--Lieb theorem (`max row leverage <=1/2`).
- account02/B11 closes the heavy minority-Rayleigh branch when the spectral Rayleigh quotient stays a fixed distance from the null cone.
- account03/B19 closes a localized pivot with diffuse rank-two Schur residual by an `L^3` bridge plus dependent square smoothing.
- The newest assigned-partner result account03/B20 closes the two-level localized branch away from small scalar pivots through an exact three-square cascade.
- account02/B19, account04/B20 and account01/B01 close several aggregate/cross-packet branches before reciprocal coordinate-minor losses are paid.

Thus an exact-rank-three hard core is the heavy near-null / mixed-leverage branch in which a physical heavy direction approaches the indefinite null cone and the residual square direction is entangled with the same original coordinates as the exported bilinear slope. Arbitrary additional spectral directions remain a separate interaction debt outside the already paid diffuse/separable basins.

## 3. Assigned partner consumed exactly: cap-parametric two-level cascade

The newest completed `account03/B20` result proves that in the genuine rank-exactly-three two-level Schur branch one has an exact representation

`Q = a V1^2 + b V2^2 + d Y3^2`,

with the source identity

`|a b d| = c c2 |det Lambda|`,

and, under unit density caps at the three successive smoothing stages,

`||p_Q||_infinity <= C_* |a|^(-1/2)|b|^(-3/10)|d|^(-1/5)`.

Here is the useful quantitative strengthening needed for synthesis.

### Theorem 3.1 — `QFORM-CAP-REFUNDED-SQUARE-CASCADE-v1`

Assume the same three-square representation, but suppose only:

1. `Y3` has a density bounded by `M3`;
2. conditionally on `d Y3^2`, the variable `V2` has a density bounded by `M2` almost surely;
3. after forming `R2=dY3^2+bV2^2`, the conditional density of `V1 | R2` is bounded by `M1` almost surely.

Then

`||p_Q||_infinity <= C_* M1 M2^(3/5) M3^(2/5) |a|^(-1/2)|b|^(-3/10)|d|^(-1/5)`.

Using the partner's exact pseudodeterminant identity,

`||p_Q||_infinity <= C_* M1 M2^(3/5) M3^(2/5)
 |a|^(-3/10)|b|^(-1/10)(c c2 |det Lambda|)^(-1/5)`.

#### Proof

Scale

`V1'=M1 V1`, `V2'=M2 V2`, `Y3'=M3 Y3`.

Every displayed conditional density cap becomes at most one; the conditioning sigma-fields and the random variables `dY3^2` and `R2` themselves are unchanged, while the three square coefficients become `a/M1^2`, `b/M2^2`, `d/M3^2`. Applying the exact account03/B20 theorem gives

`C_* (|a|/M1^2)^(-1/2)(|b|/M2^2)^(-3/10)(|d|/M3^2)^(-1/5)`,

which is the first formula. Substituting `|d|=c c2 |det Lambda|/(|ab|)` gives the second. QED.

### Corollary 3.2 — exact cap-refund thresholds

If `c,c2>=1/2`, `|det Lambda|>=1`, and the third cap is universally bounded, then a small first pivot is fully paid whenever

`M1 <= K1 |a|^(3/10)`,

and a small second pivot is fully paid whenever

`M2 <= K2 |b|^(1/6)`.

This is materially weaker than demanding a square-root refund. It identifies the precise amount of product-structure anti-concentration that a near-isotropic pivot still owes after the partner's determinant growth has already refunded part of the reciprocal pivot loss.

### Lemma 3.3 — source-valid fresh-bank conditional cap

Let `I` be a block of untouched original coordinates and

`U=sum_{i in I} e_i X_i`.

If the sigma-field `G` used at a smoothing stage depends only on original coordinates outside `I`, and `H` is `G`-measurable, then `V=U+H` satisfies

`||p_{V|G}||_infinity <= sqrt(2)/||e||_2`

almost surely (with the sharper singleton bound `1/|e_i|`).

Indeed, conditional on `G`, `H` is a translation and `U` keeps its unconditional product-law projection density. This is not a post-rotation independence assertion and does not use the refuted generic conditional-cap shortcut.

Combining Lemma 3.3 with Theorem 3.1 gives a concrete closure criterion: if the first two cascade variables contain genuinely untouched disjoint original-coordinate banks of coefficient norms `L1,L2`, and the last square has a fresh bank of norm `L3`, then

`||p_Q||_infinity <= 2 C_* L1^(-1)L2^(-3/5)L3^(-2/5)
 |a|^(-3/10)|b|^(-1/10)(c c2 |det Lambda|)^(-1/5)`.

Hence `L1` of order `|a|^(-3/10)` and `L2` of order `|b|^(-1/6)` already neutralize the two near-isotropic losses.

## 4. New universal structure in the heavy near-null branch

A fresh account02/B11 result proves the following exact source fact. In rank exactly three with inertia `(2,1)` or `(1,2)`, let a physical row have leverage `c>=1/2`. Rotate only the three-dimensional spectral coordinate system so this row is `sqrt(c)e1`, and let `a` be its spectral Rayleigh quotient. In the minority-sign near-null branch `|a|<1/4`, the physical cross row obeys

`E := sum_{j != 0} A_0j^2 >= 31/64`.

The next lemma converts this macroscopic export into source-realizable independent banks without selecting a vanishing minor.

### Theorem 4.1 — `QFORM-NEAR-NULL-CROSS-BANK-DICHOTOMY-v1`

Under the preceding hypotheses, one of the following holds.

**Singleton branch.** There is a physical coordinate `j` with

`|A_0j| >= sqrt(E)/2 >= sqrt(31)/16`.

**Two-bank branch.** There are disjoint nonempty sets `J,K` partitioning the remaining physical coordinates such that

`E/4 <= sum_{j in J} A_0j^2 < E/2`,

`sum_{k in K} A_0k^2 > E/2`.

Consequently the two source-realizable aggregates

`Y_J=sum_{j in J} A_0j X_j`, `Y_K=sum_{k in K} A_0k X_k`

are independent, independent of `X_0`, and satisfy the dimension-free density caps

`||p_YJ||_infinity <= 2 sqrt(2)/sqrt(E) <= 16 sqrt(2)/sqrt(31)`,

`||p_YK||_infinity < 2/sqrt(E) <= 16/sqrt(31)`.

#### Proof

Put `s_j=A_0j^2`, so `sum s_j=E`. If some `s_j>=E/4`, the singleton branch holds. Otherwise every atom is strictly smaller than `E/4`. Add atoms greedily until their sum first reaches `E/4`. The resulting set `J` has total weight below `E/2`; its complement `K` therefore has weight above `E/2`. Independence follows because `J,K,{0}` are disjoint blocks of the original product law. The sharp one-dimensional product-marginal bound gives `sqrt(2)` divided by the coefficient `l2` norm, producing the displayed constants. QED.

This is target-level mechanism movement: the near-null problem is no longer allowed to hide behind a cross row whose mass is spread over arbitrarily many individually tiny physical coefficients. Either one fixed cross edge is already macroscopic, or two disjoint original-coordinate slope banks carry universal norm and universal projection-density caps.

## 5. Exact application to the canonical null-cone model

The B11 null-cone family is

`Q=2( sqrt(c) X0 + sqrt(1-c) X1 ) X3 + X2^2`, `1/2<c<1`.

Set

`U=sqrt(c)X0+sqrt(1-c)X1`, `V=X3`, `Z=X2`.

These are functions of three disjoint original-coordinate blocks. The coefficient vector of `U` has Euclidean norm one, so the sharp projection theorem gives `M_U<=sqrt(2)`, while `M_V,M_Z<=1`. Applying the exact account04/B20 aggregate hyperbolic-square theorem with `a=b=1` gives

`||p_Q||_infinity <= 4 sqrt(M_U M_V) M_Z <= 4*2^(1/4)`.

Thus the canonical exact null-cone construction is uniformly paid. It is not a counterexample to QFORM. The hard branch is precisely the failure, in a general frame, to keep the strong exported slope and the residual square channel on suitably fresh/disjoint original-coordinate banks.

## 6. First unpaid universal implication after this run

### `QFORM-NEAR-NULL-FRESH-BANK-OR-ENTANGLEMENT-v1` — OPEN

For every exact-rank-three indefinite target form with a physical row of leverage at least `1/2` and minority spectral Rayleigh quotient `|a|<1/4`, use the guaranteed cross-row energy `E>=31/64` and Theorem 4.1 to prove one of:

1. a genuine fresh-bank square cascade satisfying the conditional-cap hypotheses of Theorem 3.1, with first-stage bank norm at least a constant multiple of `|a|^(-3/10)` when that refund is needed;
2. a disjoint aggregate hyperbolic-square normal form paid by account04/B20;
3. a rectangular multi-channel packet paid by account02/B19 or a rank-three cross packet paid by account01/B01; or
4. a direct product-preserving smoothing estimate for the entangled remainder.

The remaining issue is therefore **freshness/entanglement**, not existence of macroscopic cross mass. Marginal bank caps alone cannot simply be promoted to the conditional caps in Theorem 3.1; that would violate the live conditional-cap correction. Any closure must exhibit an actually untouched original-coordinate bank at the relevant smoothing stage, or replace conditional smoothing by a dependence-safe operator argument.

After exact rank three is closed, arbitrary additional spectral directions remain a separate source-valid interaction debt outside the already paid full-range diffuse and separable basins.

## 7. Honest status

- Full QFORM conjecture: `OPEN`.
- `QFORM-CAP-REFUNDED-SQUARE-CASCADE-v1`: `PROVED` under explicit conditional-cap hypotheses.
- `QFORM-NEAR-NULL-CROSS-BANK-DICHOTOMY-v1`: `PROVED` from the B11 cross-row lower bound.
- Canonical null-cone banked family: `PROVED` with density bound `4*2^(1/4)`.
- New full-target movement: none; mechanism-level movement is a quantitative reduction of the near-null debt to fresh-bank/entanglement closure.
- No continuity claim is made for the new cascade theorem beyond what its inputs separately provide.

## 8. Source pins

- `yspennstate/math-research-brain` fresh initial control commit `a16f38dc7169693c680b23f1c1a8791baab80242`, owner revision `2026-09-22.5`.
- Assigned partner account03/B20: `yspennstate/math-open-problems@e06f8c89c1f99a6a021fc9687af0168b8ad50399`, `proofnet24/QFORM-density/fleet-2026-09-22/account03/B20/20260922T131539Z-account03-B20-qform-r11/REPORT.md`.
- account02/B11 heavy minority/near-null theorem: `proofnet24/QFORM-density/fleet-2026-09-22/account02/B11/20260922T135203Z-b11-qform-6080e0b3/REPORT.md` on current master snapshot.
- account04/B20 aggregate hyperbolic-square theorem: `proofnet24/QFORM-density/fleet-2026-09-22/account04/B20/20260922T132134Z-account04-B20-QFORM-r1/REPORT.md`.
- account02/B19 synthesis handoff: `scheduled_tasks/work/shared/qform-density-2026-09-22/handoffs/account02/B19/20260922T123814Z-account02-B19-qform-r11.md`.
- account01/B01 random-slope cross-packet handoff: `scheduled_tasks/work/shared/qform-density-2026-09-22/handoffs/account01/B01/20260922T124907Z-b01-qform-auto11.md`.

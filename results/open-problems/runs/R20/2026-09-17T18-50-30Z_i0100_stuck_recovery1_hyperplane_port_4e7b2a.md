Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum was requested in prompt text, but the exposed runtime provides no authenticated applied-model or reasoning-effort receipt, so I do not claim otherwise. **NO MOVEMENT in the frozen exact-prime metric: `1213 -> 1213`; retained exact set `{5,13,17,29,41,181,241,317,421,541,601,661,1009,1021,1033,1049,1061,1093,1201,1213}`; unchanged count `3 -> 4`; status PARTIAL / SOURCE OPEN; mandatory STUCK RECOVERY 1. Section-B moves used for this thinking-only run: second-pass #1 CHANGE THE CATEGORY, #17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE, #25 COUNT THE SAME THING TWICE.**

# R20 / I0100 — mandatory stuck recovery 1: what is actually missing, and a single recovery route

Repository / branch: `yspennstate/math-open-problems` / `master`.
Canonical claim: `operations/claims/I0100.md`.
Outside source: Afonso S. Bandeira et al., *Randomstrasse101: Open Problems of 2025*, Conjecture 26; stable compilation arXiv:2603.29571.
Frozen metric: largest admissible prime with matching exact primal/dual certificates for the source-normalized theta quantity, preserving the complete covered-prime set.

This is the Section-I thinking-only run forced by three consecutive unchanged fixed-metric runs. It deliberately contains **no new theorem claim, no new finite prime, and no new checker**. Its purpose is to identify the exact block, inventory the routes already attempted and why each stopped, identify the nearest genuinely solved analogue, and choose exactly one recovery action.

## 1. Continuity, source status, ownership, and repository recovery

I continued from the newest immutable R20 report

`runs/R20/2026-09-17T17-48-29Z_i0100_grassmann_line_oriented_sweep_6c2f91.md`

rather than restarting.

Before this stuck analysis I reread/recovered the required campaign/control surfaces: `probability_campaign_2026_09/INDEX.md`, `probability_campaign_2026_09/RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/claims/I0100.md`, the current new-methods deployment/limitations record, the newest own R20 report, the exact I0100 intake hits, and neighboring Paley ownership/history. The intake and root ledgers are connector-bounded when rendered wholesale, so I used exact target searches for I0100 and neighboring claims rather than pretending that every unrelated byte of all ~780 JSONL rows rendered in one response.

Ownership remains non-overlapping:

- R20 owns I0100 / Conjecture 26 / one-localization theta;
- P04 owns I0101 / Conjecture 27 / two-localization and its newest located report is itself in stuck-recovery after finite frontier `p=4049`;
- R12 handed off/rotated from I0102 / Conjecture 28 and did not transfer that scope to R20;
- the former C28 Paley-ETF/I0103 work is a distinct Conjecture-29 scope and is not imported here.

Fresh public-source check on 2026-09-17: `https://randomstrasse101.math.ethz.ch/posts/PaleyGraph/` still states Conjecture 26 as

\[
\vartheta(\overline{G_{p,1}})\sim\sqrt{p/2}\qquad(p\equiv1\pmod4\text{ prime}),
\]

with `G_{p,1}` the induced graph on the neighbors of zero, and still states Conjectures 27–29 separately. A fresh bounded web/arXiv search for `Randomstrasse101 Conjecture 26 Paley one-localization theta`, `one-localization Paley Lovasz theta`, `Paley localization theta 2026`, and later/citing Paley theta work found the live open source, Magsino–Mixon–Parshall's 2019 local-Paley LP paper, the 2025 random-circulant theta paper and later Paley SDP/subgraph-hierarchy work, but no source-matching proof or refutation. This is only dated bounded-search evidence, not a novelty certificate.

A repository update since the previous R20 report is worth preserving but does not alter the source status: P26 independently reconstructed the exact `p=41` Fourier primal/dual theorem and recorded

`P26-AUDIT-R20-I0100-P41-FOURIER-DUAL-ENDTOEND-24 = PASS_FULL_FINITE_PROOF`

and, together with the distinct R19 audit,

`P26-RECONCILE-R20-I0100-P41-2OF2-24 = PASS`.

That closes only the historical finite `p=41` package. It is not an audit of the asymptotic Conjecture 26.

## 2. Frozen metric and why this run is mandatory

The exact-certified frontier entering and leaving this run is

\[
\boxed{p_{\max}=1213}
\]

with complete retained exact-certified set

\[
\boxed{\{5,13,17,29,41,181,241,317,421,541,601,661,1009,1021,1033,1049,1061,1093,1201,1213\}}.
\]

There is no new exact prime this run. The consecutive unchanged count therefore advances

\[
\boxed{3\longrightarrow4}.
\]

Under the owner protocol this is **STUCK RECOVERY 1**, not permission to manufacture another finite certificate or another equivalent reformulation.

## 3. The exact statement that blocks

The newest route puts the full theta deformation on a one-dimensional projective Grassmann line. In the notation of the preceding report, choose a full-row-rank matrix `B` for the relevant Paley half-Fourier subspace and

\[
A_q=I+(q-1)\frac{\mathbf1\mathbf1^\top}{m},\qquad m=n-1.
\]

The theta threshold `q_p` is the unique boundary between existence and nonexistence of a nonzero nonnegative kernel vector for `BA_q`, and

\[
T_p/\sqrt n\to1\quad\Longleftrightarrow\quad q_p\to1.
\]

Every maximal Plücker coordinate is affine in `q`, so at the actual sign-compatible wall there is an index set `I_p` with

\[
q_p
=1-
\frac{\Delta_{I_p}(1)}
     {\Delta_{I_p}(1)-\Delta_{I_p}(0)}.
\]

The exact unresolved obligation is therefore

\[
\boxed{
\text{find/control a positive-circuit / nonnegative-cocircuit compatible wall }I_p
\text{ for which }
\frac{\Delta_{I_p}(1)}{\Delta_{I_p}(1)-\Delta_{I_p}(0)}=o(1).
}
\tag{BLOCK}
\]

An arbitrary small determinant, an arbitrary Plücker root near one, or a one-point character-sum estimate is not enough. The missing information is the **orientation/sign compatibility** that identifies the wall actually seen by the positive orthant.

The equivalent fixed-margin formulation from the immediately preceding route says the same thing in separator language: for each fixed `epsilon>0`, construct the appropriate Paley half-Fourier separator with normalized mean one and coordinate floor better than `-(e^epsilon-1)`; do this for the two complementary halves. No existing route supplies that deterministic global sign control.

## 4. Every route tried, grouped by mechanism, and the precise failure

This inventory is intentionally about failure modes, not about restating all intermediate lemmas.

### Route A — exact Fourier LP / primal-dual certificates / stabilizer reduction

What worked: the circulant symmetry reduces theta to an exact Fourier LP, and exact primal/dual certificates moved the finite frontier repeatedly through `p=1213`.

Why it stopped: finite basic supports and exact objective identities do not themselves produce a formula uniform in `p`. Support changes are genuine and finite overshoots above and below the limiting scale occur. Extending the prime table is evidence, not an asymptotic mechanism.

### Route B — direct dual completion / common-neighbor spectral completion

What worked: the upper-half theta question can be phrased as completing an edge-prescribed common-neighbor deviation matrix with small top eigenvalue; the arithmetic entries are controlled by Legendre/Frobenius traces.

Why it stopped: pointwise Weil-size entry control gives only the old `sqrt(p)` scale. The needed completion must exploit off-edge freedom globally enough to make the top eigenvalue `o(p)`, and no deterministic completion with that spectral property was found.

### Route C — projected simplex / convex hull / Haar-factor / fractional-tiling formulations

What worked: theta became an opposite-vertex radial depth, a complementary pair of fractional Haar factorizations, and later a one-sided Chebyshev constant. These are exact equivalences and expose the self-dual target.

Why it stopped: the reformulations identify the correct extremal object but do not force its radial depth. They replace the theorem by an equally hard deterministic convex-geometric statement unless one adds orientation information about the Paley Fourier subspace.

### Route D — raw projection / Jacobi sums / Weil sharpening

What worked: the raw one-sided Chebyshev certificate is exactly expressible through Jacobi sums. Ping Xi's Jacobi-sum equidistribution makes its empirical limit an arcsine law.

Why it stopped: this route did more than fail — it identified a real obstruction. The raw certificate asymptotically reaches the `sqrt(2)` endpoint, and a positive fraction of coordinates violate the desired `1/sqrt(n)` floor. Therefore merely sharpening the same Weil estimate, or repairing only `o(n)` exceptional coordinates, cannot reach the conjectured constant.

### Route E — sparse, affine, and common-profile corrections

What worked: transverse balancing can be imposed exactly while preserving the radial objective; complementary halves admit exact dual radial identities.

Why it stopped: affine profiles in the one-point Jacobi coordinate remain stuck at the same `1/sqrt(2)` normalized barrier. Moreover a profile automatically balanced for both complementary halves is forced into this low-dimensional affine intersection. The two halves require genuinely different nonlinear information.

### Route F — entropy/Gibbs continuation and Fisher curvature

What worked: the radial optimum is the zero-temperature endpoint of a canonical maximum-entropy path; its derivative is the radial objective and its second derivative is a Schur-complement covariance/Fisher quantity. The first transverse derivative vanishes by symmetry.

Why it stopped: the second-order transverse term is nonzero and is governed by additive pair-count variance / Legendre elliptic traces. A scalar curvature bound does not control the vector Lagrange multiplier when the covariance becomes anisotropic. No uniform vector covariance bound along the path was obtained.

### Route G — quadratic and bounded-degree balanced polynomial profiles

What worked: the nonlinear balancing corrections have exact Fourier descriptions in terms of centered additive representation counts; the quadratic term is a restricted Mellin transform of the Legendre family, and the construction extends to an all-degree hierarchy.

Why it stopped: discovery computations showed that low fixed degree remains far below the full radial optimum at large certified primes. The hierarchy therefore does not close at degree two or any small fixed degree visible in the tests; a successful polynomial route would need growing degree plus new uniform control of high-order character correlations.

### Route H — random/Haar projected simplex, Wendel, conic intrinsic volumes, statistical dimension

What worked: the random analogue has an exact self-dual threshold at constant one. Wendel/hyperplane-arrangement formulas and conic intrinsic volumes solve the Haar model; the rank-one stretched orthant has an explicit statistical-dimension limit, and every fixed nonzero stretch lies macroscopically on one side of the random transition.

Why it stopped: at the exact critical point the favorable Haar event has probability tending to one half, so vague `Paley is pseudorandom/typical` reasoning cannot determine the deterministic side. More importantly, the random proof uses rotational/exchangeable symmetry and chamber counting; one-point Jacobi equidistribution is far too weak to transfer the orientation of all sign-compatible circuits/minors.

### Route I — fixed-margin Gordan separator

What worked: the full asymptotic does not require reproducing the microscopic random critical window. It is enough to rule out every fixed nonzero stretch, equivalently to construct a fixed-floor separator for each fixed `epsilon>0` in both complementary Paley halves.

Why it stopped: no explicit deterministic separator improving the all-prime `sqrt(2)` constant to an arbitrary fixed `1+epsilon` was found. Existing character-sum bounds control individual Fourier/Jacobi statistics, not the simultaneous coordinate floor after optimizing the free half-spectrum.

### Route J — Grassmann projective line / affine Plücker / oriented-matroid sweep

What worked: the entire theta deformation lies on one projective line; every maximal minor is affine in `q`; the actual threshold is an exact positive-circuit / nonnegative-cocircuit wall and therefore one of those affine roots.

Why it stopped: the affine-root list is enormous and most roots are irrelevant. Without a theorem identifying a sign-compatible root, or showing all sign-compatible roots concentrate near `q=1`, determinant estimates alone do not control the actual theta threshold. This is exactly (BLOCK).

### Route K — finite pivot, basis-homotopy, zonotope/Kashin, cocircuit-typical and related finite-dimensional algorithms

What worked: these routes clarified basis changes, dual geometry, and finite support certificates and supplied useful self-checks at small primes.

Why they stopped: they either remained finite algorithms with no uniform arithmetic law, or invoked generic Banach/discrepancy estimates that lose the Paley-specific constant. Typical cocircuit information again did not give the orientation-compatible extremal cocircuit required by the orthant crossing.

The common lesson is now stable: **all routes that only control marginals, norms, arbitrary minors, or fixed-degree corrections miss the same object — the global orientation of the Paley half-Fourier subspace relative to the positive orthant.**

## 5. What a successful proof must contain that no route so far contains

A successful argument must add one genuinely new ingredient:

> a deterministic, high-dimensional **orientation theorem** for the Paley half-Fourier subspace, strong enough to control the orthant wall rather than merely the sizes of Fourier coefficients.

Any one of the following would be enough, but none is currently available:

1. a sign-compatible circuit/cocircuit construction whose affine Plücker root satisfies `q=1+o(1)`;
2. a deterministic chamber-count/orientation analogue showing that the Paley projective line crosses the orthant ill-posed set at `q=1+o(1)`;
3. for every fixed `epsilon>0`, an explicit fixed-margin Gordan separator for both complementary halves.

What is specifically **not** enough anymore: another exact prime, another one-point Weil/Jacobi estimate, another arbitrary small minor, another low-degree polynomial profile, or another random-model phase-transition calculation without a deterministic transfer theorem.

## 6. Simplest special case still unproved

The simplest asymptotic special case that is both source-relevant and genuinely weaker than Conjecture 26 is a **single strict constant improvement over the old square-root barrier**. A concrete target is

\[
\boxed{
T_p\le \frac43\sqrt n
\quad\text{for all sufficiently large primes }p\equiv1\pmod4,
\qquad n=(p-1)/2.
}
\tag{WEAK-4/3}
\]

This is much weaker than `T_p~sqrt(n)` but strictly better than the generic `T_p <= sqrt(p) ~ sqrt(2n)` scale. In the rank-one-stretch language it asks only for one fixed nontrivial margin (`q<sqrt(2)`, asymptotically `q=4/3`), not for `q_p->1`.

The fresh bounded literature search did not locate an all-prime deterministic theorem of this form for the source-normalized one-localization theta. Magsino–Mixon–Parshall derive the local Fourier LP and dual and report strong computations; the 2025 random-circulant work gives square-root scale up to a `log log` factor in the random model; neither supplies (WEAK-4/3) for deterministic Paley localizations in the source normalization. This is again bounded negative evidence, not a publication-priority claim.

## 7. Nearest solved problem in the literature, and what its proof has that R20 lacks

The nearest **solved** analogue is the orthant-crossing problem for a random/Haar subspace, equivalently the probability that the origin lies in the convex hull of a symmetric random point cloud.

- Wendel (1962) gives the exact convex-hull/halfspace probability for iid centrally symmetric points.
- Kabluchko–Vysotsky–Zaporozhets (2017) and related conic/hyperplane-arrangement work compute analogous absorption probabilities/intrinsic volumes by chamber counting.
- Peña–Roshchina (2016) identify the Grassmann distance to ill-posedness for conic feasibility with alternative-margin quantities.

Those proofs possess precisely what the Paley problem lacks: **symmetry that makes global sign patterns/chambers countable or distribution-free**. Rotational or exchangeable randomness lets one average over all orientations and reduce the answer to hyperplane-arrangement combinatorics. The deterministic Paley half-Fourier subspace has strong arithmetic pseudorandomness at the level of one-point Jacobi sums, but no theorem saying its high-dimensional oriented matroid has the requisite chamber statistics.

That difference is sharper than saying merely “the Paley graph is not random”: the missing object is a deterministic replacement for the chamber-count/orientation step.

## 8. The three Section-B moves used in this thinking run

### #1 CHANGE THE CATEGORY

I moved the block from theta/LP language to **oriented hyperplane arrangements / conic feasibility**. This did not prove a new theorem, but it identified the exact missing category-level input: deterministic chamber/orientation control for the Paley Fourier subspace.

### #17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE

The constant-one self-dual threshold reappears exactly in Wendel-type convex-hull probabilities and random conic intrinsic-volume theory. This confirms that the target constant belongs naturally to orthant geometry, but the literature's proofs rely on rotational/exchangeable symmetry unavailable in the deterministic Paley instance.

### #25 COUNT THE SAME THING TWICE

The useful double-counting target is now clear: count sign-compatible orthant chambers (or positive circuits) once through the Paley projective-line wall structure and once through an arithmetic description of Paley Fourier orientations. No such second arithmetic count is presently known. This is a route specification, not a new claim.

## 9. Exactly one recovery action chosen

Section I requires choosing exactly one action. I choose:

\[
\boxed{\textbf{PORT THE TECHNIQUE FROM THE NEAREST SOLVED PROBLEM.}}
\]

Concretely, the next mathematical run will **not** extend the prime table and will **not** invent another equivalent formulation. It will attempt to port the Wendel / hyperplane-arrangement chamber-count mechanism to the deterministic Paley half-Fourier subspace, first only at the weak fixed stretch corresponding to (WEAK-4/3).

The success criterion for that next attack is intentionally weaker than the full conjecture: produce a deterministic orientation/chamber estimate strong enough to certify the fixed-margin separator at one explicit constant below `sqrt(2)`. If the port cannot even deliver that weaker statement, the report must say exactly which chamber statistic cannot be controlled and why.

The three Section-B moves reserved for the next run are:

- **#2 ATTACK THE NEGATION FIRST** — search for an explicit infinite family of sign-compatible walls with `q>=4/3`; if such a family exists, the proposed weak target is false and reveals the obstruction;
- **#4 PROVE SOMETHING WEAKER, COMPLETELY** — target (WEAK-4/3), not the full `q_p->1`;
- **#30 ONE PRIME, ONE SCALE, ONE DIRECTION AT A TIME** — freeze the single stretch `q=4/3` and the one-sided upper-half separator before attempting all `epsilon` or both halves.

No other recovery action is selected in this report.

## 10. Audit/closure state

- source Conjecture 26: **OPEN / PARTIAL**;
- fixed metric: `1213 -> 1213`;
- unchanged count: `3 -> 4`;
- stuck state: **RECOVERY 1**;
- no new theorem claim in this run;
- no new finite certificate in this run;
- `p=41` finite theorem now has two distinct outside passes (P26 and R19), but that is claim-scoped finite evidence only;
- existing stronger finite frontier `p=1213` remains SELF_CHECK_ONLY unless/until a distinct outside audit targets that exact package;
- no source-level two-audit closure exists;
- **NO CLOSURE CLAIM**.

Because R20 is CLOSABLE OUTSIDE, the operational addendum requires rotation after six unchanged fixed-metric runs. This run is unchanged count four, so it does not yet rotate.

## 11. Model/scheduler limitation

The latest deployment record still says the available scheduler control surface exposes prompt/title, schedule/timing, enabled state and timing mode, but no native model-family selector, no reasoning-effort selector, no guaranteed hour-long execution field and no authenticated applied-model telemetry. GPT-6/maximum therefore remains prompt-only. The historical P26 `You cannot modify this task` failure was context-specific; another authorized context later successfully updated P26. The valid fix for unavailable model routing is an authorized product/workspace scheduler or platform API/support surface exposing those controls, not a duplicate task or permission bypass.

No scheduler modification, email, Drive write, public posting, purchase, permission change, shared-root edit, or peer-track edit was performed by R20 in this run.

## 12. Structured ledger_delta

```yaml
ledger_delta:
  worker: R20
  lane: CLOSABLE_OUTSIDE
  source: "Afonso S. Bandeira et al., Randomstrasse101 (2025), Conjecture 26 / intake I0100"
  metric: "largest admissible prime with matching exact primal/dual certificates"
  metric_before: 1213
  metric_after: 1213
  covered_primes:
    - 5
    - 13
    - 17
    - 29
    - 41
    - 181
    - 241
    - 317
    - 421
    - 541
    - 601
    - 661
    - 1009
    - 1021
    - 1033
    - 1049
    - 1061
    - 1093
    - 1201
    - 1213
  status: PARTIAL
  source_status: OPEN
  unchanged_count_before: 3
  unchanged_count_after: 4
  stuck_recovery: 1
  tried_moves: [1, 17, 25]
  selected_recovery_action: "port the technique from the nearest solved problem"
  simplest_unproved_special_case: "T_p <= (4/3) sqrt(n) for all sufficiently large admissible primes"
  exact_block: "identify/control the sign-compatible positive-circuit/nonnegative-cocircuit Plucker wall and force q_p -> 1"
  next_moves: [2, 4, 30]
  remaining_obligation: "port Wendel/hyperplane-arrangement chamber counting to deterministic Paley half-Fourier orientation, first at fixed stretch q=4/3; if this fails, isolate the missing arithmetic chamber statistic"
  evidence:
    - "runs/R20/2026-09-17T17-48-29Z_i0100_grassmann_line_oriented_sweep_6c2f91.md"
    - "runs/R20/2026-09-17T16-48-05Z_i0100_rankone_statdim_fixedmargin_f3a71c.md"
    - "runs/R20/2026-09-17T16-04-11Z_i0100_selfdual_random_hierarchy_b7e2c4.md"
    - "runs/R20/2026-09-17T15-10-00Z_i0100_p1213_quadratic_mellin_5e8c31.md"
    - "runs/R20/2026-09-17T14-10-10Z_i0100_gibbs_paircount_curvature_3e7a91.md"
    - "runs/R20/2026-09-17T12-06-06Z_i0100_p1201_jacobi_arcsine_c9e41a.md"
    - "proofnet24/P26-proof-audit-recovery/runs/2026-09-17/2026-09-17_17-58-40__run-report.md"
  audit_ids:
    - "P26-AUDIT-R20-I0100-P41-FOURIER-DUAL-ENDTOEND-24 = PASS_FULL_FINITE_PROOF"
    - "R19-AUDIT-R20-I0100-P41-01 = PASS"
    - "P26-RECONCILE-R20-I0100-P41-2OF2-24 = PASS"
```

**NO CLOSURE CLAIM.**

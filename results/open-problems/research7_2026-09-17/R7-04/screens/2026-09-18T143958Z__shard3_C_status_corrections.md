Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding selector is exposed.

# R7-04 shard-3 C-series source-status corrections — 2026-09-18

## Snapshot and continuity

- Repository: `yspennstate/math-open-problems`, branch `master`.
- Captured fresh master immediately before this screen: `c3dcdf5927321bfe20d87a303eb7095db5adda4a`.
- Slot: `R7-04 Constructive Model Research`.
- Native ID: `6aabe7ea6e1881919a65503f8445a813`.
- Own root: `research7_2026-09-17/R7-04/`.
- Previous immutable report: `research7_2026-09-17/R7-04/runs/2026-09-18/2026-09-18T133645Z__report.md`, creation commit `cffe452f3fae0c1aa659739e36c5148a5a11c9f7`.
- Entering state: `PENDING_ADMISSION`, successor metric `UNKNOWN/UNMEASURED`.

The exact worker partition remains case-sensitive `sum(ord(c) for c in ID) % 7 == 3`. Existing claims, holds, source resolutions, posted/known work, and retired routes remain exclusions. This screen advances the successor cursor through C-series candidates that had not yet received a sufficiently source-exact current-status reconciliation. It does not revive retired E0010/F0106 or inherit their metrics.

## 1. C0089 is now positively source-resolved: KNOWN / RESOLVED_IN_LITERATURE_2025

Canonical row: `C0089`, Heydenreich--van der Hofstad Open Problem 16.7.

Primary source: Markus Heydenreich and Remco van der Hofstad, *Progress in High-Dimensional Percolation and Random Graphs* (2017 author version), Open Problem 16.7. Source PDF:

`https://www.mathematik.uni-muenchen.de/~heyden/survey-high-d-percolation.pdf`

The source asks for a quenched invariance principle for simple random walk on (i) the random interlacement set and (ii) an infinite component of the vacant set of random interlacements.

The repository's September-12 campaign record had the right suspicion but left the source status `unverified`: Procaccia--Rosenthal--Sapozhnikov (PRS) proved the interlacement-set QIP at every level and the vacant-set QIP in the then-known local-uniqueness regime; the campaign suggested that later sharpness/local-uniqueness results ought to extend the latter to the full supercritical phase, but did not verify the hypothesis match.

That gap is no longer merely inferential. The following later paper states the missing conclusion explicitly:

- A. Goswami, P.-F. Rodriguez, V. Shulzhenko, *Strong local uniqueness for the vacant set of random interlacements*, arXiv:2503.14497 (2025): `https://arxiv.org/abs/2503.14497`.

Its Corollary 1.2 says, for every `u in (0,u_*)`, for almost every vacant-set environment, the diffusively rescaled simple random walk on the infinite vacant cluster converges to Brownian motion with positive scalar covariance. The text immediately says this follows from PRS Theorem 1.1 plus the paper's new strong-local-uniqueness theorem, and explicitly checks that the previously outstanding PRS hypothesis is supplied by the new theorem.

The earlier components are:

- E. B. Procaccia, R. Rosenthal, A. Sapozhnikov, *Quenched invariance principle for simple random walk on clusters in correlated percolation models*, PTRF 166 (2016), 619--657, arXiv:1310.4764: `https://arxiv.org/abs/1310.4764`. It includes the random-interlacement-set QIP for every level and the vacant-set QIP under its structural hypotheses.
- H. Duminil-Copin, S. Goswami, P.-F. Rodriguez, F. Severo, A. Teixeira, *Phase transition for the vacant set of random walk and random interlacements*, arXiv:2308.07919: `https://arxiv.org/abs/2308.07919`, identifies the principal vacant-set critical/local-uniqueness thresholds.

Therefore this is a **positive source-matching literature resolution**, not a conclusion from search failure. `C0089` is excluded from R7-04 admission as **KNOWN / RESOLVED_IN_LITERATURE_2025**.

## 2. C0082 intake scope is narrower than the literal source; full source is not a clean CLOSABLE target

Canonical row: `C0082`, currently titled “First coefficient where the 1/d expansions of p_c on Z^d and on the hypercube differ.”

The authoritative source is again Heydenreich--van der Hofstad 2017, printed page 220. The literal source contains two consecutive problems:

- Open Problem 15.8 asks for an argument proving existence of the asymptotic expansion of `p_c(Z^d)` **without the lace expansion**, and asks that method to compute `a_4,a_5,...`.
- Open Problem 15.9 says: **extend Open Problem 15.8 to the hypercube and find the first i for which the coefficients on Z^d and the hypercube are distinct.**

Thus the full source mandate is not merely “identify the first differing coefficient.” It also imports the method/existence/computation demand of Open Problem 15.8 into the hypercube setting. The current C0082 intake statement suppresses this first clause and therefore makes the source look substantially more finite than it is.

Relevant known literature already gives all-order asymptotic expansions using the lace expansion:

- R. van der Hofstad and G. Slade, *Asymptotic expansions in n^{-1} for percolation critical values on the n-cube and Z^n*, arXiv:math/0401073: `https://arxiv.org/abs/math/0401073`.

The historical C0082 attempt predicts that the first difference may be `a_4`, based on short-cycle structure, but explicitly does not prove the needed fourth-order lace-diagram identity. Even a proof of that prediction by itself would not close the full literal Open Problem 15.9 because of the inherited lace-expansion-free extension clause.

Admission classification for R7-04: **SOURCE-EXACT BROAD/HARD METHOD+COEFFICIENT PROBLEM / NOT CLEAN CLOSABLE**. No claim is created.

## 3. C0091 has unusually strong 2026 evidence of current openness, but it is HARD rather than CLOSABLE

Canonical row: `C0091`, Heydenreich--van der Hofstad Open Problem 16.9, printed page 240.

The source explicitly asks to prove **any form of negative association for the FK random-cluster model for `q<1`**. The preceding source text names the weakest concrete target: pairwise negative edge correlation

`P(omega(a)=omega(b)=1) <= P(omega(a)=1) P(omega(b)=1)`

for arbitrary edges `a,b`.

A current source-status check has positive evidence that even this weakest form remains unresolved in general:

- Pengfei Tang and Zibo Zhang, *Negative correlation for the random-cluster model below one on high-degree regular graphs*, arXiv:2609.11578, submitted 2026-09-10: `https://arxiv.org/abs/2609.11578`.

Their abstract states that pairwise negative correlation on arbitrary finite graphs remains open; they prove it for broad high-degree regular graph sequences under isoperimetric hypotheses and establish an equivalence/reduction involving increasing degree. The repository's H0015 intake independently records this exact 2026 conjecture as a duplicate of `C0091`.

So this is a credible current-open HARD problem, not a stale source row. But it is a universal arbitrary-finite-graph correlation theorem, and the campaign ranking places it in the genuinely hard tier. R7-04's owner policy requires a genuinely CLOSABLE source rather than relabeling a famous hard theorem as closable. Classification: **HARD OUTSIDE / CURRENT-OPEN SUPPORTED / NOT R7-04 CLOSABLE**. No claim is created.

## 4. C0127 is source-open-looking but programmatic rather than a fixed short theorem

Canonical row: `C0127`, Sourav Chatterjee, *Chaos, concentration, and multiple valleys* (2008), Section 12 problem (6), p. 59, arXiv:0810.4221: `https://arxiv.org/abs/0810.4221`.

The source asks to **find a multiple-peaks condition on a Gaussian field equivalent to chaos and superconcentration, or show that no such condition exists**. The repository's prior attempt already gives a clean counterexample to one naive two-peak formulation: two stable low-overlap peaks can coexist without chaos or superconcentration. It leaves a growing-number-of-peaks formulation open.

Subsequent work, e.g. J. Ding, R. Eldan, A. Zhai, *On multiple peaks and moderate deviations for the supremum of a Gaussian field*, arXiv:1311.5592 (`https://arxiv.org/abs/1311.5592`), strengthens directions from superconcentration toward many peaks, but does not freeze the source's open-ended “find a condition” request into one source-specified necessary-and-sufficient predicate.

For R7-04 this therefore fails the exact closure-criterion gate: selecting our own favourite “multiple-peaks condition” and proving or refuting it would create a new conjecture rather than necessarily close the literal source. Classification: **BROAD META-PROBLEM / NOT CLEAN CLOSABLE**. No claim is created.

## 5. The only obvious finite Tier-2 shard-3 C target is already owned

`C0021`, the iterated 3-majority revealment exponent, is an excellent finite sharp-parameter CLOSABLE problem, but current canonical claim `operations/claims/C0021.md` is owned by P13 Outside Counterexample Research. A live claim is not released by schedule status or stale queue text. It is excluded.

Combining this with the preceding D/E/F/G/H/I R7-04 screens, no newly checked shard-3 C candidate simultaneously passes source exactness, current-open status, ownership, and R7-04's CLOSABLE criterion.

## Admission decision

R7-04 remains **PENDING_ADMISSION**.

- successor metric before: `UNKNOWN/UNMEASURED`
- successor metric after: `UNKNOWN/UNMEASURED`
- target-specific stagnation: not started
- canonical claim created: none
- Section-B research methods charged: none, because admission precedes research

The substantive mathematical/source progress of this screen is the positive current-literature closure of C0089 and the literal-source scope correction for C0082. Neither justifies inventing a replacement target.

## Next lawful cursor

Do not repeat the static C0089/C0082/C0091/C0127 screen absent a status change. On the next invocation, first reconcile repository deltas since this report and inspect only newly added, explicitly released, or previously unsourced shard-3 candidates. Prefer a literal finite construction, explicit counterexample request, fixed coupling, or short theorem. Keep `PENDING_ADMISSION` if no source crosses every gate.
# ADH Question 36 — literal no-tail-control refutation package

## Scope

Outside source: Antonio Auffinger, Michael Damron, Jack Hanson, *50 years of first-passage percolation*, arXiv:1511.03262, Section 7.1, Question 36.

The source asks whether the maximal-flow limit in equation (7.2) exists without the exponential-moment assumption. This package addresses the **literal deletion reading**: remove the positive exponential-moment hypothesis and do not silently impose a replacement finite-mean, second-moment, or other tail condition.

Under the corrected intended Kesten straight-cylinder height regime, that literal statement is false. The package gives an iid nonnegative capacity law, finite almost surely and satisfying `F(0)=0`, with no positive exponential moment, together with a legal slowly growing height function for which the normalized maximal flow has an almost-sure subsequence diverging to `+infinity`. Thus the finite law-of-large-numbers conclusion in (7.2) does not survive complete deletion of tail control.

This does **not** refute positive weakening results under finite mean, second moment, finite column-minimum moment, or other replacement hypotheses. In particular, P11's separate repaired claim `P11-I0062-FINITE-COLUMN-MIN-SHARP-07R` is outside this package.

## Source-height correction

The ADH survey prints Kesten's height condition with an `infinity` limit. P11 previously gave an exact Bernoulli zero-plane contradiction to that printed direction. Geoffrey Grimmett's 2021 retrospective, Theorem 7.12, states the Kesten condition in the zero direction

`k^{-1+delta} log n -> 0`.

Later exact quotations by Marie Théret and Barbara Dembin agree. The witness in this package satisfies the corrected zero-direction condition, so it does not exploit the survey transcription defect.

Kesten's 1987 article is:

Harry Kesten, *Surfaces with minimal random weights and maximal flows: a higher dimensional version of first-passage percolation*, Illinois J. Math. 31 (1987), 99–166, DOI `10.1215/ijm/1255989405`.

The bibliographic record was recovered, but direct article-body access through the available Project Euclid route remained blocked by its security challenge on 2026-09-17. This package therefore does not claim a fresh page-by-page verification of the 1987 text. The corrected geometry is supported by Grimmett's exact later theorem statement and later maximal-flow quotations.

## Main theorem in this package

Define

`P(T=1)=1/2`,

`P(T=2^(s^3))=2^(-s-1)` for integers `s>=1`.

Let

`m(k,l)=max(1, floor(sqrt(log_2(min(k,l)))))`

for sufficiently large integer side lengths. Along

`N_r=2^(r^2)`,

we have `m(N_r,N_r)=r`. If `Phi_r` is the bottom-to-top maximal flow in `[0,N_r]^2 x [0,r]`, then

`Phi_r/N_r^2 >= 2^(r^3-r^2-1)`

eventually almost surely. In particular

`limsup Phi/(kl)=+infinity` almost surely along a corrected-Kesten-admissible sequence.

The proof appears in `main.tex`. It has two deterministic realizations of the decisive lower bound: an explicit admissible parallel-column flow and an independent max-flow/min-cut argument.

## Exact finite core

`check.py` is the exact-arithmetic finite self-check copied into this self-contained package from P11's canonical artifact. `check.out` is its archived PASS output. The script checks distribution normalization/tail identities and the finite algebra of the high-column probability, expected count, Chebyshev bound, and normalized-flow benchmark. The asymptotic steps (no exponential moment, corrected height, summability, Borel–Cantelli, and flow/cut geometry) are proved in `main.tex`; they are not inferred from finite testing.

Canonical original checker paths:

- `proofnet24/P11-fpp-maxflow-q36/artifacts/2026-09-17/2026-09-17T01-24-14Z__heavy_tail_vertical_columns_exact_check.py`
- `proofnet24/P11-fpp-maxflow-q36/artifacts/2026-09-17/2026-09-17T01-24-14Z__heavy_tail_vertical_columns_exact_check.out`

P26 independently reexecuted the exact logic and archived a second PASS transcript at

`proofnet24/P26-proof-audit-recovery/artifacts/2026-09-17/2026-09-17_14-56-56__p11_i0062_heavytail_checker_reexecution.out`,

creation commit `bca4de73691ce24a5d74d07c89dcf8a0ac622290`, blob `57ea3526206b3b392a4f2c19418a496825dca8da`.

## Independent audits — 2/2 complete for this exact claim scope

### P04

Audit ID:

`P04-AUDIT-P11-I0062-Q36-SOURCE-REFUTATION-02P-10 = PASS (CLAIM-SCOPED)`.

Report:

`proofnet24/P04-closure-local-paley/runs/2026-09-17/2026-09-17T09-42-30Z__run-report.md`

Creation commit `2898565e9814059a45cf36ca60c187b457663915`, blob `05792586dc3e473449c4f8476b5fe484c7e945f3`.

P04 independently reconstructed the law, exact tail, corrected height, binomial/Borel–Cantelli estimate, primal high-column flow and max-flow/min-cut lower bound.

### P26

Audit ID:

`P26-AUDIT-P11-I0062-Q36-SOURCE-REFUTATION-02P-21 = PASS_FULL_MATHEMATICAL_PROOF / SOURCE_LITERAL_QUESTION_PASS / CORRECTED_HEIGHT_PROVEN / ORIGINAL_1987_HEIGHT_PROVENANCE_UNVERIFIED / PRIOR_ART_UNVERIFIED / CLAIM_SCOPED`.

Reconciliation ID:

`P26-RECONCILE-P11-I0062-Q36-02P-2OF2-21 = PASS`.

Report:

`proofnet24/P26-proof-audit-recovery/runs/2026-09-17/2026-09-17_14-56-56__run-report.md`

Creation commit `f00d576231bfcc2ac0a91746b0646a1a5eb6a5d7`, blob `e0cfd0da6b9bc8dc9334a0d20aff9d30bcedcd90`.

P26 independently reconstructed the full proof and reexecuted the exact arithmetic. P04 and P26 are distinct OTHER tracks; P11's self-proof is not counted as an outside audit.

## Prior-art/status check — 2026-09-17

The current source/literature check covered:

1. ADH Question 36 itself: the live survey text still asks whether (7.2) exists without the exponential-moment assumption.
2. Grimmett (2021), *Harry Kesten's work in probability theory*, Theorem 7.12: exact corrected zero-direction height statement and exponential-moment theorem.
3. Rossignol–Théret, *Existence and continuity of the flow constant in first passage percolation*, Electronic Journal of Probability 23 (2018), no. 99, DOI `10.1214/18-EJP214`, arXiv:1707.08766: existence/continuity of the flow constant without moment assumptions and convergence for natural flows, but not a theorem that invalidates this arbitrary-slow straight-cylinder witness.
4. Dembin–Garban, *Superconcentration for minimal surfaces in first passage percolation and disordered Ising ferromagnets* (2023/2024): bounded two-valued capacities and different fluctuation questions, not this heavy-tail source scope.
5. Current bounded searches for exact Question-36 wording, heavy-tail straight-cylinder counterexamples, and later citing work.

No searched source explicitly supplied this exact slow-height counterexample or declared the literal complete-deletion version of Question 36 negatively resolved. That is **bounded dated negative evidence, not a publication novelty certificate**. Publication novelty/priority remains unverified.

## Status

For the exact package claim `P11-I0062-Q36-SOURCE-REFUTATION-02P`:

- mathematical theorem: **PROVED**;
- literal complete-deletion reading of ADH Question 36 on the corrected intended geometry: **REFUTED / negative answer**;
- exact finite core: **PASS**;
- independent OTHER-track audits: **2/2 complete (P04 + P26)**;
- source/prior-art check: **current as of 2026-09-17, with direct Kesten-1987 article-body provenance explicitly unverified**;
- publication novelty/priority: **UNVERIFIED**;
- stronger weakest-replacement-hypothesis problem: **separate / not closed by this package**.

This README intentionally distinguishes the source-exact literal refutation from P11's stronger finite-`r_*` replacement theorem.

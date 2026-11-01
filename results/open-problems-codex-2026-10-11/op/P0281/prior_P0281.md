# Exclusive successor claim — P0281

Deployment: NEW-METHODS-2026-09-16
Owner/native slot: `6aa7b253b37c8191b693d8dc79298d37` (P13 outside-successor slot)
Category: **CLOSABLE OUTSIDE**
Status: **CLAIMED / source-screened / first research run in progress**
Claim date: 2026-09-18 UTC

## Source and exact target

Canonical problem ID: `P0281`.
Canonical dedup key: `log_concavity_of_finite_particle_tasep_transition_probabilities`.

Primary source: Leonid Petrov, Axel Saenz Rodriguez, Evan Sorensen, Hieu Trung Vu, **“AIM Workshop: All roads to KPZ Universality Open Problems”**, March 19, 2025, Section 3 “Log-concavity”, PDF p.2. The source defines log-concavity by

`f(a) f(b) <= f((a+b)/2)^2`

and then asks whether the fixed-time transition-probability function `f(a)` for continuous-time TASEP with step initial condition is log-concave.

The campaign’s canonical P0281 statement fixes the finite-particle interpretation: for continuous-time TASEP with `n` particles started from the step configuration, determine whether the fixed-time transition mass on ordered particle configurations is log-concave. In displacement coordinates

`a=(a_1,...,a_n),  a_1>=...>=a_n>=0`,

where particle `i` starts at `-i`, this means proving for every `n>=1`, every `t>0`, and every two source-valid configurations `a,b` whose componentwise midpoint `m=(a+b)/2` is integral/source-valid,

`p_{n,t}(a) p_{n,t}(b) <= p_{n,t}(m)^2`.

A single exact finite `(n,t,a,b)` counterexample refutes the universal source question. A bounded computation finding no counterexample does not prove it.

## Current-status and ownership screen

Checked 2026-09-18 UTC. The live workshop PDF still states the question in Section 3. A bounded fresh search using the exact TASEP/log-concavity wording recovered the 2025 workshop problem and adjacent transition-probability/integrable-TASEP literature, including later half-space transition formulas, but no paper in the checked results claiming this exact log-concavity theorem or an explicit counterexample. This is bounded negative evidence only, not a guarantee of worldwide openness or novelty.

The AIM workshop landing page was accessible; its separate `aimpl.org` open-problem link returned HTTP 502 in this run. The primary PDF hosted by Leonid Petrov was readable and visually checked on the Section 3 page.

Repository continuity/ownership: immediately before this create-only claim, direct fetch of `operations/claims/P0281.md` at current `master` returned 404. Exact-ID and exact-dedup-key searches recovered the canonical catalogue/brain-bundle rows and one NM13-08 admission screen, but no P0281 attempt (`P0281-A...`), no current/historical P0281 owner, and no P0281 mathematical report. NM13-08 explicitly identified P0281 as thematically suitable but excluded it solely by that track’s residue-shard rule and did not claim or research it. Thus prior substantive history is **HISTORY_GAP / none recovered in bounded repository scope**, not a zero-valued mathematical baseline.

I0051 remains retired, P0082 remains handed off, and D0093 remains handed off after its six-run CLOSABLE gate; none is reopened by this claim. I0054 remains owned by R11 and was not taken.

## Frozen source-faithful metric

Freeze

`N_LC` = the largest integer `N>=1` for which P13 has a rigorous proof that the exact source midpoint inequality above holds **simultaneously for every particle number `1<=n<=N`, every `t>0`, and every source-valid midpoint triple of ordered configurations**.

Larger is stronger. A theorem only for one ray/slice, one fixed event count under uniformization, bounded configurations, bounded times, or one special pair does **not** move `N_LC`. A finite exact counterexample at any `n` resolves the source negatively even if `N_LC` has not increased to `n-1`. Full positive source closure requires a proof for all finite `n`, not a finite value of this metric.

Admission baseline: **UNMEASURED / HISTORY_GAP** until the first P0281 research report proves and records the first source-domain value. Do not reset missing history to zero.

## First-run methods

The first research run uses three distinct Section-B methods and attacks the negation first:

- **B2 — attack the negation:** derive exact smallest-particle transition probabilities and search the first midpoint inequalities for an exact obstruction before attempting a general proof.
- **B6 — deform a known discrete model:** uniformize TASEP into iid clock-choice words and compare the independent/product Poisson limit with the reflected/blocking boundary mechanism that creates the actual TASEP law.
- **B25 — count the same finite restriction two ways:** count uniformized clock words ending in a configuration, derive an exact Poissonized generating series, and seek coefficientwise midpoint injections/inequalities.

Any finite enumeration is a self-check only unless its exact finite statement is separately proved/archived. Closure still requires source-matching proof/counterexample, current prior-art review, and the owner-required P26 plus distinct OTHER-track end-to-end audits.

Research root: `proofnet24/P13-outside-successor/`.

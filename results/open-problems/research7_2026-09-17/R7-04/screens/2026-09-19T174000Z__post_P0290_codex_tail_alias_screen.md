Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding selector is exposed.

# R7-04 post-P0290 shard-3 Codex-tail / alias screen

Date checked: 2026-09-19 UTC.  
Repository: private `yspennstate/math-open-problems`, branch `master`.  
Native worker: R7-04 / `6aabe7ea6e1881919a65503f8445a813`.  
Selection rule: exact case-sensitive candidate ID `sum(ord(c) for c in ID) % 7 == 3`.  
Worker class: **CLOSABLE OUTSIDE**.  
This is admission-stage work only. It creates no ownership claim and starts no successor stagnation counter.

## 1. Continuity and race state

Run-start captured master was `7fb58b15148d1bfb2d4fb6a1110a44dd08fe726a`.

Immediately preceding R7-04 report:

`research7_2026-09-17/R7-04/runs/2026-09-19/2026-09-19T164500Z__report.md`

creation commit `5368c4504eb9396039d0303bd7d33ed58648c655`.

That report retires P0290 from this worker after the sixth unchanged ordinary run, leaves its canonical ownership unreleased, and puts R7-04 in `PENDING_ADMISSION` with successor metric `UNKNOWN/UNMEASURED` and no successor stagnation count.

Fresh pre-screen master after concurrent work was `85224eddfe6cf89c9332e11b9cc2d428bce8d3ab`.

The exact comparison `5368c450..85224edd` is complete (`too_large = null`): 109 commits ahead, zero behind. It contains no change to root `QUEUE.md`, `RESULTS.md`, `POSTED.md`, `probability_campaign_2026_09/INDEX.md`, `probability_campaign_2026_09/RANKING.md`, or screened intake `problems.jsonl`. Admission-relevant canonical claim changes in that delta are `AK-KATZIN-C41-EQUALITY`, `MAXIMAL-INTERSECTION-ELLIPSOID-UNIQUENESS`, and `BHS-MST-CM-UNIV`, plus a release of `VDH-8.3-DUALITY`; none of those claim IDs belongs to this worker's mod-7 shard, and the VDH source is in any event HARD-shaped. A fresh neighboring CLOSABLE gate independently reaches the same lifecycle conclusion for those new claim events; its shard function differs and is not reused as R7-04 ownership logic.

## 2. Why this screen is new rather than repetition

The older R7-04 screens already exhausted the static D-series shard frontier, corrected the C-series source statuses, reconciled I0047, and after P0029 checked the early Codex shard beginning with P0013/P0031. They also impose a delta-only cursor against reopening unchanged sentinels merely to manufacture activity.

P0290's retirement leaves a materially different unexplored ranked region: the **post-P0290 populated Codex tail through P0488**. This pass therefore screens that tail, prioritizing source rows that are finite/certificate-shaped or intake-ranked as unusually tractable before touching broad asymptotic rows.

## 3. Section-B methods used at the admission stage

### B16 — solve/check small or low-complexity candidates first

The post-P0290 shard-3 IDs include many tier-3/4/5 asymptotic problems. I first isolated the rows whose archived disposition makes them plausibly closer to CLOSABLE: P0353, P0407, P0459, and P0461. This avoids spending a run pretending that LQG exact dimensions, Riesz-gas phase uniqueness, ARW infinite-volume limits, or RWRE zero-one laws are finite/certificate endpoints.

Two low-complexity rows are already excluded in the canonical catalog:

- `P0353`, **Fixed-clade count CLTs for critical beta-splitting trees** — the campaign list marks it `EXCLUDED: resolution_claimed_in_literature`.
- `P0407`, **FCFS characterization for minimum mean slowdown** — likewise excluded by a recorded literature-resolution claim.

Neither can be resurrected as an outside-open target without a source-status correction.

### B21 — find who else is already working on the same shape

`P0461`, **Entropy concavity for determinantal kernels**, is exact shard 3. The intake source is Russell Lyons, *Determinantal Probability: Basic Properties and Conjectures*, ICM 2014 / arXiv:1406.2707, Conjecture 2.6 (with a related stationary-symbol conjecture grouped in the intake). The source asks for concavity of Shannon entropy of the full finite determinantal subset law as a function of an arbitrary Hermitian positive-contraction kernel.

A direct canonical claim fetch `operations/claims/P0461.md` returned 404 at fresh master. That is **not** permission to claim it. Repository alias/history search recovered an existing active project at

`proofnet24/lyons-entropy/`

whose entry README says explicitly that the full Lyons Conjecture 2.6 remains OPEN and points to an ongoing 100-worker cross-field campaign, a 915-file recovery manifest, creative campaign, claim ledger and continuation work. Its target file states the same all-finite-`n`, all-positive-contraction concavity inequality. This is an existing active target under the owner's no-clone/no-replacement rule even though no `operations/claims/P0461.md` file exists.

Therefore P0461 is **ACTIVE DUPLICATE / NOT SELECTABLE BY R7-04**. I do not manufacture a second owner simply because the newer canonical claim namespace is absent.

A bounded 2026-09-19 public search recovered Lyons's original 2014 source but did not surface a source-matching later solution. Search misses are not proof of current openness or novelty and are not needed for the decisive active-target exclusion.

### B22 — read prior failures/partials before deciding whether a source is actually closable

`P0459`, **Simultaneous concentration of bilateral preference degrees**, is also exact shard 3 and is genuinely CLOSABLE-shaped. But fresh master contains

`operations/claims/P0459.md`

with exclusive active owner native slot `6aa7b517489c8191a5250c9384e9b33c`, status `CLAIMED / READY / CLOSABLE OUTSIDE / OPEN`, source Dabirian--Subramanian, *Connectivity of a family of bilateral preference random graphs*, J. Appl. Prob. 63(2) (2026), §1.1 open problems, and an explicit frozen metric. The same compare shows a new substantive P0459 run at 17:33 UTC. Thus P0459 is **OWNED ACTIVE / NOT SELECTABLE**.

The remaining newly exposed shard-3 tail candidates are not comparable finite endpoints:

- `P0468`: Biskup Conjecture 16.3, recover the critical-chaos logarithmic Laplace tail from the full Gibbs--Markov axiom family;
- `P0470`: Biskup Conjecture 16.5, an iterated finite-volume/depth limit for deep DGFF extremal level-set counts with critical-chaos random mass;
- `P0477`: Biskup Problem 16.12, a quenched high-probability displacement bound in a DGFF landscape;
- `P0486`: directional zero-one law beyond the plane for iid uniformly elliptic RWRE, independently screened in current repository history as HARD-shaped.

The earlier post-P0290 shard rows (`P0297`, `P0301`, `P0308`, `P0310`, `P0317`, `P0326`, `P0335`, `P0344`, `P0362`, `P0369`, `P0371`, `P0378`, `P0380`, `P0387`, `P0396`, `P0400`, `P0416`, `P0425`, `P0434`, `P0443`, `P0452`) are all archived as tier-3/4/5 theorem-scale asymptotic, infinite-volume, phase, universality, allocation, or scheduling problems rather than the finite construction/coupling/certificate profile requested for this slot. This pass does **not** pretend that a title/tier label proves impossibility of future admission; it records only that none outranks the blocked P0459/P0461 pair as a genuinely CLOSABLE candidate under the present source-level gate.

## 4. Admission decision

No candidate in this bounded ranked tail pass simultaneously satisfies:

1. exact mod-7 shard 3;
2. original outside source with a precise source-level closure endpoint;
3. genuinely CLOSABLE rather than a finite slice of a HARD theorem;
4. no active claim/reservation/alias ownership;
5. not solved, known, posted, retired, or literature-excluded.

The two strongest CLOSABLE-shaped rows fail ownership/active-target checks (`P0459`, `P0461`); the two deceptively low-complexity rows are literature-excluded (`P0353`, `P0407`); the remaining visible tail is HARD-shaped at source level.

Therefore the lawful state remains **`PENDING_ADMISSION`**. No `operations/claims/<ID>.md` is created. No source metric is frozen and no stagnation counter advances.

## 5. Frozen successor state and next admission action

- target: `PENDING_ADMISSION`;
- successor metric before: `UNKNOWN/UNMEASURED`;
- successor metric after: `UNKNOWN/UNMEASURED`;
- movement: **NO TARGET METRIC EXISTS YET**;
- successor ordinary unchanged count: **not started**;
- successor stuck recoveries: **not started**.

Next run should remain delta-first. It should not reopen P0290, P0459, P0461, P0353, or P0407 without a material ownership/source-status change. The next bounded work is to inspect a not-yet-source-reviewed tier-3 shard row only if no newly admitted exact CLOSABLE row or explicit release appears in the fresh repository delta; any such row must pass full original-source and current-literature admission before a claim is created.

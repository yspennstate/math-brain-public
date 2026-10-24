Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — **NO MATHEMATICAL MOVEMENT; ADMISSION_PENDING; methods B2/B15/B29 were NOT attempted because no source passed admission.** GPT-6/maximum was requested in prompt text, but this runtime exposes no authenticated binding model/reasoning selector, so I do not claim otherwise.

# NM13-07 — first admission screen for geometric/extremal CLOSABLE OUTSIDE work

UTC report time: 2026-09-17T21:47:00Z  
Repository: `yspennstate/math-open-problems`, branch `master`  
Own namespace: `proofnet24/NM13-07/`  
Captured master before write: `4d1beb3e5b51ccb494117307c1f8b2eaf2859d9e`  
Category: **CLOSABLE OUTSIDE**  
Admission state after this run: **ADMISSION_PENDING / NO CLAIM CREATED**

## 1. Continuity and governing policy recovered

This is the first NM13-07 mathematical invocation; repository search found the deployment record but no prior `proofnet24/NM13-07/runs/` report. I therefore used the current fleet controls rather than inventing predecessor state.

Read/reconciled this run:
- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- current task-health coordinator state `operations/task_health/runs/2026-09-17T185900Z/status.md`;
- relevant D- and E-intake source rows, their historical attempt material, and current `operations/claims/` ownership evidence;
- repository searches for neighboring `NM13-06` and `NM13-08` runs (none were visible at the captured master).

The coordinator's latest visible gate explicitly reports that no new READY + CLOSABLE + UNASSIGNED successor had been honestly established at that snapshot. That is not by itself a prohibition on a new admission, so I independently advanced the shard-6 screen below.

## 2. Exact shard computation

The prompt requires

`int(SHA256(UTF-8 canonical_dedup_key).hexdigest(),16) mod 13 = 6`.

I recovered canonical keys from the intake ledgers before evaluating the shard. The following exact keys all land in residue 6:

| Candidate | Canonical dedup key | SHA256 | disposition |
|---|---|---|---|
| D0005 | `complete_mixability_open_2014::open_problem_5` | `b9aa519cb282a305a387a8ffc235a13d49530ef2070ccfe63b93c0c9f15834be` | ideal geometric/convex candidate, but already exclusively CLAIMED |
| D0042 | `virag_operator_limits_2014::question_4_(formulas)` | `dce7c106e36aaf59b052ebacb1a3e7f2a5c951bb277b5ba2df419d7496a49a57` | broad limiting-operator/correlation-formula question; HARD-shaped, not CLOSABLE |
| D0044 | `virag_operator_limits_2014::question_6_(decimation)` | `95f289b2fa22b60905865aa7f0c3038f4845e8a697750a197e10ed55456ec0ea` | another worker reached six-run CLOSABLE retirement boundary; do not reopen |
| D0051 | `ddg_lqg_metric_intro_2021::problem_5.3` | `858189ccb926154afada955836f7d6b923a2dd47d4b28c2bd9fff2e45bcb67de` | LQG-geodesic thick-point dimensions; HARD asymptotic geometry |
| D0084 | `ghs_mating_trees_survey_2019::problem_6.5` | `b083d8c1e0fba40c2e0f4dcc21729b94141d959706467fd1bb07807fca37b88b` | embedded random-planar-map convergence; HARD asymptotic geometry |
| E0047 | `bandeira::op_1_3_rank_constrained_sdp` | `0823a951119a95b08cbfeca693be29c4eaca9a2fcd8623b1c726935146fef8fa` | finite-r vector-spin-glass transition; HARD asymptotic variational problem |
| E0057 | `bandeira::op_10_4_mra` | `671a85d2f794c56b5db867782b05ddd5effaa912de586e28f814f1d9297453bc` | potentially short-theorem-shaped, but exact source/current-status reconciliation remains incomplete |

All residues above were computed from the literal UTF-8 key, not from the intake ID or title.

## 3. Ownership and exclusion screening

### D0005 — rejected because it is owned

D0005 is the best subject match in this shard: Wang's Open Problem 5 asks whether the uniform distribution on every convex body in `R^d` is `(d+1)`-completely mixable. But `operations/claims/D0005.md` is an existing create-only exclusive claim for another native slot. Its claim explicitly says not to duplicate the schedule or ownership. I therefore did not touch it.

### D0044 — rejected because the active route is retired/rotated

The current task-health state records that D0044 reached its six-supported-no-movement CLOSABLE retirement boundary and is now a successor-admission gate. Reopening it here would violate the retirement discipline even though the source question itself is not globally closed.

### I0075 / I0089 / RS-2026-DC34 / RS-2026-DC35 / I0123 / I0125 — excluded before shard dispatch

These are the most obvious geometric/network/convexity/packing candidates surfaced by `QUEUE.md` and repository search, but current claims, handoffs, or terminal recovery history already reserve or exhaust them. A disabled, rotated, or historically renamed schedule does not release source ownership. No alias was used to bypass those exclusions.

## 4. CLOSABLE-vs-HARD classification of the unowned residue-6 leads

I did not relabel a hard asymptotic problem merely to fill the slot.

- D0042 asks for a general connection between asymptotic correlation formulas and limiting random operators. It has no frozen finite decision target in the source statement.
- D0051 asks for Hausdorff dimensions of intersections between LQG geodesics and thick-point sets across a continuum of `alpha`; this is a hard continuum/asymptotic program.
- D0084 asks for embedded convergence of further random planar-map models to LQG; it is an asymptotic scaling-limit theorem, not a finite geometric certificate.
- E0047 asks for finite-r spiked-Wigner rank-constrained SDP transition thresholds. The recovered attempt reduces it to the zero-temperature vector-SK variational problem, whose finite-r evaluation is itself open. It is not an honest closable assignment in the present state.

These remain possible HARD inventory for appropriately authorized hard workers, not NM13-07 admissions.

## 5. E0057 current-status screen — promising but not admitted

E0057 is the only newly surfaced residue-6 item in this pass that could plausibly be a short theorem: the 2015 Bandeira source asks about consistency of a (quasi-)maximum-likelihood estimator for multireference alignment after the source's normalization/power-spectrum fixing. The intake already records that the separate sample-complexity half was subsequently answered, while retaining the estimator-consistency half.

Fresh public-literature queries on 2026-09-17 included:
- `multireference alignment maximum likelihood estimator consistency`;
- `multi-reference alignment consistency maximum likelihood`;
- recent 2025-2026 MRA/MLE work.

The screen recovered, among other things:
- Perry–Weed–Bandeira–Rigollet–Singer on MRA sample complexity;
- later finite-group/dihedral and high-dimensional MRA estimation results;
- Kreymer–Balanov–Bendory, arXiv:2601.04831, *An Ultra-Fast MLE for Low SNR Multi-Reference Alignment* (2026).

I did **not** recover from the bounded search a paper whose theorem statement cleanly matches the source's exact quasi-MLE consistency clause. But I also did not recover the original source text deeply enough in this invocation to certify that the intake paraphrase preserves every estimator, normalization, identifiability and quotient convention needed for a create-only claim. General MLE consistency folklore is not enough to declare the source KNOWN or to dispatch a possibly different quasi-MLE problem.

Therefore E0057 remains `PENDING_SOURCE_CURRENT / UNASSIGNED_NOT_CERTIFIED`, not READY. This is exactly the admission boundary the owner protocol requires.

## 6. Mathematical status and methods

No source passed admission, so there is no lawful source metric to freeze.

- Metric before: **UNMEASURED**.
- Metric after: **UNMEASURED**.
- Mathematical movement: **none**.
- B2 ATTACK THE NEGATION: **NOT ATTEMPTED** on any source problem.
- B15 BREAK THE SYMMETRY: **NOT ATTEMPTED** on any source problem.
- B29 ADD THE POINTS AT INFINITY: **NOT ATTEMPTED** on any source problem.

Those methods are retained as the initial triple for the first genuinely admitted NM13-07 target. Screening/ownership work is not counted as mathematical progress.

## 7. Durable admission cursor for the next invocation

Do not repeat the candidates above absent a status/ownership change. Continue the residue-6 scan in this order:

1. remaining E-intake batches outside the Bandeira batch, prioritizing finite convex/geometric/network questions;
2. F/G/H/I intake rows whose canonical dedup keys have not yet been shard-tested by NM13-07;
3. Codex/campaign raw catalogue candidates marked admitted with no substantive attempt, again hashing the canonical source key before any source work;
4. only after those, revisit E0057 if the original source's exact estimator definition can be recovered and matched against current literature.

For any next candidate, stop at the first failed gate in the order: canonical identity -> shard -> source-exact statement -> posted/index exclusions -> ownership/history -> current primary/later/citing literature -> CLOSABLE classification -> create-only claim. After a successful claim, immediately spend the substantive run on B2/B15/B29 rather than another screening report.

## 8. `ledger_delta` for P26

```yaml
ledger_delta:
  track: NM13-07
  category: CLOSABLE_OUTSIDE
  target: ADMISSION_PENDING
  claim_id: null
  metric_name: null
  metric_before: UNMEASURED
  metric_after: UNMEASURED
  mathematical_status: ADMISSION_PENDING
  movement: none
  methods_attempted: []
  assigned_initial_methods_retained: [2, 15, 29]
  unchanged_run_count: 0
  closure_audits: 0/2
  secondary_auditor_if_needed: NM13-08
  source_screen_summary: >-
    D0005 is shard-6 and geometric but already claimed; D0044 is retired after its
    six-run boundary; D0042/D0051/D0084/E0047 are HARD-shaped; E0057 is a possible
    short-theorem lead but remains pending exact source/current-literature reconciliation.
  next_state: CONTINUE_ADMISSION_CURSOR
```

**End of complete run report.**

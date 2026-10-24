Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. ADMISSION_PENDING / no mathematical movement. Section-B methods #2, #11, #30 were NOT TRIED because no lawful CLOSABLE OUTSIDE source was admitted; screening is not counted as mathematical progress.**

# NM13-10 — first admission screen

Date: 2026-09-17 UTC  
Repository / branch: `yspennstate/math-open-problems` / `master`  
Own namespace: `proofnet24/NM13-10/`  
Captured master before delivery: `e2af38150badfae8de572a732ab4583c0f6c8d31`

## 1. Runtime/model control

The actual runtime is GPT-5.6 Sol. The reasoning-effort level is not authenticated by an exposed selector or telemetry and is therefore **UNVERIFIED**. The task prompt requests GPT-6 / maximum reasoning, but the currently exposed scheduler controls do not bind a model or reasoning-effort value. I do not claim that request was installed as an enforced runtime configuration.

## 2. Controlling continuity recovered

I read/recovered the current controlling surfaces before screening:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- current intake ledgers under `probability_1000_intake_*`;
- canonical ownership claims and current/historical reports for candidates that survived the shard screen;
- the newest directly relevant neighboring successor-admission report, `runs/R15/20260917_2008Z_successor_admission_d0039_j39.md`;
- the D0027 canonical claim and its six-run handoff.

No previous `proofnet24/NM13-10/` report exists in the visible repository, so this is the first own-state report. Missing own history is not interpreted as permission to reuse another lane's work.

The root queue itself warns that listed/PENDING rows are not automatically dispatchable, that current claims supersede stale queue labels, and that an attractive route is not a READY certification. I followed that stricter gate.

## 3. Shard rule and bounded screening method

This worker may select only candidates whose **canonical dedup key** satisfies

```text
int(SHA256(UTF-8 canonical_dedup_key).hexdigest(), 16) mod 13 = 9.
```

For intake records with an explicit `dedup_key`, I used that exact string. I did not hash display titles or local aliases. Rows without a canonical dedup key were not promoted merely by inventing one during this run.

I screened the accessible C/E/F/G intake material and the D intake through `D0102`, while checking exact ownership/history for the most plausible residue-9 rows. The useful residue-9 candidates encountered in the D ledger include:

| ID | canonical dedup key | current disposition from this run |
|---|---|---|
| D0027 | `kcm_facilitated_open_2025::conjecture_2` | **EXCLUDED / owned+retired-handoff**: canonical `operations/claims/D0027.md` belongs to R7-04; no explicit canonical release was found, and the six-run handoff says not to continue seventh-run churn in that lane. |
| D0034 | `bradley_mixing_open_2005::question_6` | **OPEN-LOOKING but HARD, not CLOSABLE**: source asks for a process provably not representable as an instantaneous function of *any* stationary Harris recurrent Markov chain. The newest R15 screen reached the same conclusion after a fresh current-status check. |
| D0055 | `maxtype_recursive_open_2017::conjecture_of_derrida_and_retaux` | **KNOWN/RESOLVED** in the admitted source scope under the later Chen-Dagard-Derrida-Hu-Lifshits-Shi theorem with the source's allowed integrability qualification. |
| D0057 | `maxtype_recursive_open_2017::conjecture_2` | **HARD asymptotic**: conditional geometric limit in the critical Derrida-Retaux recursion; no finite/short closure mechanism recovered. |
| D0061 | `lyons_nonamenable_2000::conjecture_3.8_(benjamini-schramm_1996)` | **HARD famous problem**: `p_c < p_u` on every transitive nonamenable graph; not relabeled CLOSABLE. |
| D0085 | `ghs_mating_trees_survey_2019::problem_6.6` | **HARD asymptotic**: no-macroscopic-faces transfer for random planar-map embeddings; current source statement needs a scaling-limit theorem, not a finite certificate. |
| D0094 | `rolla_arw_survey_2020::third_open_problem_after_theorem_6.1` | **OPEN-LOOKING but not CLOSABLE**: tightness of the single-site odometer on cycles in the fast phase. The prior attempt identifies the quotient/cycle obstruction: box-domain monotonicity does not transfer to the conservative cycle. |
| D0096 | `rolla_arw_survey_2020::second_open_problem_after_theorem_7.2` | **KNOWN/RESOLVED** by later activated-random-walk work showing the critical density is below one. |

Other residue-9 rows encountered in the C/E/F/G screens were either already claimed/posted/resolved or plainly theorem-scale hard. In particular:

- E0017 is already canonically claimed by another track; current master itself is actively receiving E0017 work, so it is not reserve inventory.
- F0090 / Kalai Conjecture 8 is in `POSTED.md`/campaign INDEX as settled and publicly posted; it is excluded.
- C-series residue-9 leads such as DGFF extremal/scaling questions, percolation-torus criticality, rotor-router recurrence, and random-matrix convergence-rate questions are asymptotic HARD targets rather than finite/sharp-constant CLOSABLE targets.
- F0088 (double-dimer scaling) and F0091 (threshold-circuit question) are likewise HARD.
- G0014 is a front/Bramson-type asymptotic conjecture, not a finite closure target.

This is a bounded screen, not a claim that the whole repository contains no eligible candidate.

## 4. Fresh source/current-literature checks on the nearest residue-9 leads

### D0027 — FA-1f exponential relaxation

The canonical claim is current and exclusive to R7-04. It names Martinelli-Shapira-Toninelli, arXiv:2510.20461, Section 1.1 Conjecture 2, and preserves the exact all-`q`, all-source-admissible-initial-laws, all-local-observables quantifiers. The current handoff dated 2026-09-17 retires it from that research lane after six unchanged ordinary runs but leaves the canonical claim and complete handoff in place. This worker therefore does **not** reopen it.

A fresh web query on 2026-09-17 for the exact FA-1f Conjecture 2 still surfaced the 2025 open-problems statement and summaries saying available results cover sufficiently large `q`, not a complete all-`q` proof. That is bounded negative evidence only. Ownership/retirement already suffices to exclude D0027 here.

### D0034 — Bradley Question 6

Bradley's source asks whether there exists a strictly stationary `psi`-mixing, perhaps even 1-dependent, sequence that is **not** an instantaneous function of any strictly stationary Harris recurrent Markov chain. The source text itself emphasizes the universal representation obstruction. A fresh 2026-09-17 search did not recover a source-matching later solution; the nearest contemporary Bradley work found concerns other mixing/CLT questions, not this representation problem.

The newest R15 successor-admission report independently screened D0034 on 2026-09-17 and reached the same operational conclusion: open-looking, no visible canonical owner, but the `for every Harris recurrent Markov chain` non-representability obligation has no finite witness or short invariant currently in hand. I therefore do not convert it into a CLOSABLE target merely because the desired answer is existential.

### D0094 — fast-phase ARW odometer tightness on cycles

Rolla's survey states the finite-cycle problem directly after Theorem 6.1: show that the family of one-site odometers is tight in the fast phase. A fresh 2026-09-17 search recovered the source statement and did not recover a later source-matching tightness theorem. This again is bounded negative evidence only.

The prior exact campaign attempt is already informative: finite-box odometers on `Z^d` can be monotone in the domain and converge to the infinite-volume odometer, but `Z_n` is a quotient/conservative system rather than an increasing subgraph, so that comparison fails. The existing high-probability `T <= kappa n log^2 n` bound also does not by itself give a uniform single-site tail. No short source-closing route was recovered in this run, so D0094 remains HARD-shaped rather than a valid CLOSABLE admission.

## 5. Why no Section-B method is reported as tried

The task-specific instruction says the initial research methods are B2, B11, B30 **after admission**, and explicitly says not to misreport them as tried before they are genuinely attempted. No source passed the exact source/current-status/history/ownership/CLOSABLE gate. Therefore:

- B2 ATTACK THE NEGATION FIRST: **not tried on an admitted target**;
- B11 DUALIZE: **not tried on an admitted target**;
- B30 LOCALIZE ONE SCALE/DIRECTION: **not tried on an admitted target**.

Admission screening is bookkeeping/source control, not mathematical movement, so I do not turn the three methods into nominal checkboxes.

## 6. Admission state and screening cursor

No canonical claim is created in this run.

There is therefore **no active source mathematical metric yet**. The mathematical metric remains `UNMEASURED / NO ACTIVE SOURCE`; I do not invent a zero baseline.

Operational admission state:

```text
READY + CLOSABLE + UNASSIGNED source found in this bounded residue-9 screen: 0
claim_created: false
active_source: NONE
mathematical_metric: UNMEASURED
mathematical_movement: none
```

This zero is an operational screening count only; it is **not** the task's mathematical metric and is not reported as mathematical progress.

**Next screening cursor:** continue past the already-screened accessible C/E/F/G and D-through-D0102 residue-9 material into other canonical intake/catalog rows that have not yet been source/status/ownership reconciled. Do not recycle D0027, D0034, D0055, D0057, D0061, D0085, D0094, or D0096 absent a material ownership/status/source change. Prefer a row whose *full source quantifiers* can plausibly be decided by one exact counterexample, one sharp number, a finite certificate, or a short analytic theorem.

## 7. Delivery and integrity

No checker or substantive artifact was warranted because there is no admitted mathematical target. No shared root ledger, peer file, claim, workflow, schedule, email, Drive file, permission, or public posting was changed by this run.

This report is the single immutable run report for the invocation. It contains a `ledger_delta` for P26; P26 alone may reconcile shared root state.

## 8. Structured `ledger_delta`

```yaml
ledger_delta:
  worker: NM13-10
  allocation: CLOSABLE_OUTSIDE
  source_status: ADMISSION_PENDING
  active_source: NONE
  claim_created: false
  mathematical_metric: UNMEASURED
  mathematical_movement: none
  admission_screen_count:
    before: 0
    after: 0
    note: operational_only_not_math_progress
  section_B_methods:
    assigned_initial: [2, 11, 30]
    actually_tried: []
    reason_not_tried: no_lawful_target_admitted
  shard:
    rule: "int(SHA256(UTF-8 canonical_dedup_key).hexdigest(),16) mod 13 = 9"
    screened_visible_families: [C, E, F, G, D]
    D_cursor_through: D0102
  screened_key_rows:
    D0027:
      residue: 9
      disposition: CLAIMED_AND_RETIRED_HANDOFF_DO_NOT_REOPEN
      owner: R7-04
    D0034:
      residue: 9
      disposition: OPEN_LOOKING_BUT_HARD_NOT_CLOSABLE
    D0055:
      residue: 9
      disposition: KNOWN_RESOLVED
    D0057:
      residue: 9
      disposition: HARD_ASYMPTOTIC
    D0061:
      residue: 9
      disposition: HARD_FAMOUS
    D0085:
      residue: 9
      disposition: HARD_ASYMPTOTIC
    D0094:
      residue: 9
      disposition: OPEN_LOOKING_BUT_HARD_NOT_CLOSABLE
    D0096:
      residue: 9
      disposition: KNOWN_RESOLVED
  fresh_literature_checks:
    date: 2026-09-17
    scope: bounded_web_search
    candidates: [D0027, D0034, D0094]
    limitation: bounded_negative_search_is_not_worldwide_openness_or_novelty
  prior_history_recovered:
    - operations/claims/D0027.md
    - research7_2026-09-17/R7-04/handoffs/2026-09-17T194200Z__D0027_sixrun_handoff.md
    - runs/R15/20260917_2008Z_successor_admission_d0039_j39.md
    - probability_1000_intake_D_20260908/attempts.jsonl
  checker: none
  artifacts: []
  audits: []
  shared_roots_edited: false
  peer_files_edited: false
  next_action: continue_residue9_admission_screen_beyond_current_cursor
```

**End of complete run report.**
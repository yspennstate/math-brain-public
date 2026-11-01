Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO METRIC MOVEMENT: `d_bad=+infinity -> +infinity`; Section-B methods #1 CHANGE THE CATEGORY, #16 COMPUTE EVERY SMALL CASE, and #25 COUNT THE SAME THING TWICE were genuinely attempted.**

# NM13-05 — P0411 post-stuck recovery: audit normal form and exact small-even cross-checks

Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker / namespace: `NM13-05` / `proofnet24/NM13-05/`  
Canonical source / claim ID: `P0411`  
Canonical dedup key: `boundary-hole_monotonicity_and_coefficient_positivity_for_ideal_cells`  
SHA-256: `55ed478fc4a65273f15d74d172f46ee938595061ac9a7d82ad3a03afcfd6c1cc`  
Shard: `4 mod 13`  
Category: **CLOSABLE OUTSIDE**  
Run date: 2026-09-19 UTC

## 1. Runtime truth and controlling continuity

The prompt requests GPT-6 with maximum reasoning. This invocation actually identifies as **GPT-5.6 Sol**. Authenticated reasoning-effort telemetry is not exposed in this task surface, so the reasoning level is **UNVERIFIED**. I do not claim GPT-6, maximum reasoning, an hour-long execution, or a support escalation.

At the start of this invocation I reread or exact-target-recovered current `master` state for:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized amendment `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- canonical claim `operations/claims/P0411.md`;
- prior attempt `P0411-A001` and proof packet `probability_campaign_2026_09/codex_20h_20260906/proofs/IPVT_boundary_hole_partial.md`;
- newest own report `2026-09-19T10-28-30Z__p0411-stuck-recovery1-literal-u-source-audit-blocker.md`;
- newest neighboring NM13-06 report and current P26 audit report;
- the exact predecessor-to-prewrite Git delta;
- current public source/follow-up literature described in section 7.

The append-only intake corpora are too large to claim that every unchanged byte was freshly rendered model-visible. I preserve the completed canonical admission history and use the complete Git delta to detect changes to intake/attempt ledgers, root ledgers, policy, and claims. Missing display is never treated as a release or permission to reset continuity.

The canonical claim remains **CLAIMED / MANUALLY ADMITTED / CLOSABLE OUTSIDE**, exclusively owned by `proofnet24/NM13-05`. No P0411 release, reassignment, retirement, alias conflict, or source-level closure appeared.

## 2. Frozen metric and stuck/recovery state

The frozen marginal family remains

`R_d := d_H(o, ∂C_d)`, `d>=2`,

with survival `H_d(u)=P(R_d>=u)` from Proposition 5.1. The frozen obstruction threshold remains

`d_bad := min { d>=2 : g_d(u)=-H_d'(u) is not nonincreasing on u>=0 }`,

with `d_bad=+infinity` when there is no bad dimension.

Certified state this run:

- metric before: **`d_bad=+infinity`**;
- metric after: **`d_bad=+infinity`**;
- movement: **NO MOVEMENT**;
- unchanged-run counter: **`4 -> 5`**;
- stuck-recovery count: **`1 -> 1`**.

This is the research run following the first mandatory Section-I diagnosis. The previous run selected exactly one recovery action, **REFUTE INSTEAD OF PROVE**, and recorded #1/#16/#25 as the next methods. I do not invent a second recovery episode here.

Because P0411 is CLOSABLE, the six-unchanged-run rotation rule is now one run away. If closure is still unavailable at the next invocation and the frozen metric again remains unchanged, that invocation must record the sixth unchanged run and preserve a terminal handoff/rotation rather than pad P0411 with additional lemmas.

## 3. Frozen repository delta before this report

Predecessor report creation commit:

`1c34dd2db8c54525ffb92bd1cfd83611a09e6972`.

After writing the substantive idea/checker artifacts but before this immutable report, frozen `master` was:

`7263fd4a1ee2e0388378d1bec24970d8726e4fa7`.

Exact comparison reports:

- status: `ahead`;
- **109 commits ahead**;
- **0 behind**;
- total commits: `109`;
- `too_large = null`, so the changed-file list is complete.

The complete delta contains no modification of `operations/claims/P0411.md`, no P0411 audit PASS, no P0411 ownership release, and no change to root `QUEUE.md`, `POSTED.md`, `RESULTS.md`, campaign `INDEX.md`/`RANKING.md`, probability intake `problems.jsonl`, or probability attempt ledgers. A separate `H0008` lifecycle edit and other workers' reports/artifacts do not affect P0411 ownership or closure.

This invocation itself added, before freezing the report head, only these substantive own-namespace artifacts:

1. `proofnet24/NM13-05/artifacts/2026-09-19/2026-09-19T11-30-00Z__p0411_audit_normal_form_idea.md`, commit `610382f6f4be918cbad77ccd5a2b350ecb0c8eaf`;
2. `proofnet24/NM13-05/artifacts/2026-09-19/p0411_small_even_audit.py`, commit `e6ff645c40f369067c34b378d6106a1983c53eeb`;
3. `proofnet24/NM13-05/artifacts/2026-09-19/p0411_small_even_audit.out`, commit `7263fd4a1ee2e0388378d1bec24970d8726e4fa7`.

The checker was executed locally with exit code 0 before archival. Its output ends `ALL_EXACT_CHECKS_PASS`. It is explicitly a **self-check / finite audit aid**, not an independent audit.

## 4. Method #1 — CHANGE THE CATEGORY: build the minimal audit object

The previous stuck report identified that P0411's practical blocker is no longer an owner-track search for a missing density lemma. The useful category change is therefore from a mixed geometric-probability conjecture to a minimal **analytic-function audit object** whose clauses cannot contaminate one another.

Start only from the source identity, with `n=d-1`:

`J_d(u)=1/H_d(u)=c_d^{-1} integral_{R^n} (sqrt(cosh(u)^2+|x|^2)-sinh(u))^(-2n) dx`,

`c_d=pi^(n/2) Gamma(n/2)/Gamma(n)`.

The source package then separates into five logically distinct obligations:

1. **scaled-hole monotonicity** — prior campaign PROVED candidate; not NM13-05 discovery;
2. **odd-dimensional positive rational polynomial** — prior campaign PROVED candidate; not NM13-05 discovery;
3. **even-dimensional positive power series in the source-displayed variable `u`** — literal clause already contradicted by the archived exact `d=2` sixth coefficient;
4. **decreasing density for every `d>=2`** — NM13-05 PROVED candidate; this is the clause measured by frozen `d_bad=+infinity`;
5. **median below mean** — consequence of the decreasing-density theorem.

This category change has a concrete audit consequence: the classical Pringsheim argument from later NM13-05 runs is a strengthening of item 3, but it is **not needed** to refute the literal source conjunction. A source-level auditor can decide the literal even-dimensional clause from the source formula and a single independently reconstructed `d=2` coefficient. That sharply reduces the closure surface.

Outcome of #1: **useful reduction / no metric movement / no new theorem claim**. It packages what an auditor must actually verify and prevents stronger analytic extras from being mistaken for required source scope.

## 5. Method #16 — COMPUTE EVERY SMALL CASE: exact even-dimensional sign reconnaissance

This method was used as adversarial audit work, not as a replacement metric and not as an asymptotic claim.

For even `d`, let `n=d-1` (odd), `alpha=(n-2)/2`, and

`F_d(u):=e^{-nu}/H_d(u)=G_n(q)`, `q=e^{2u}`.

The exact source-faithful radial reduction from the preceding work is

`G_n(q)=K_n integral_1^infinity (z-1)^alpha z^(-2n) (q+z)^alpha (q+2z-1) dz`,

where

`K_n=Gamma(n)/Gamma(n/2)^2`.

For `k>=1`, direct differentiation gives

`partial_q^k[(q+z)^alpha(q+2z-1)]`

`=(alpha)_(k-1)(q+z)^(alpha-k)[(alpha-k+1)(q+2z-1)+k(q+z)]`.

At `q=1` the square bracket simplifies to `(n-k)z+k`. With

`z=(1+t)/(1-t)`, `t=s^2`,

the derivative integral becomes

`G_n^(k)(1) = K_n (alpha)_(k-1) 2^(n-k-1) I_(n,k)`,

where

`I_(n,k)= integral_0^1 2 s^(n-1)(1-s^2)^(n+k-1)[n+(n-2k)s^2]/(1+s^2)^(2n) ds`.

Because `n` is odd, this is an integral of a rational function in `s`; exact reduction gives a rational-linear combination of `1` and `pi`. Composition with `q=e^{2u}` uses the exact identity

`[u^j]F_d(u) = (2^j/j!) sum_(k=0)^j S(j,k) G_n^(k)(1)`,

with `S(j,k)` the Stirling number of the second kind.

The checker uses only integer/rational arithmetic plus a rigorous rational enclosure of `pi` obtained from Machin's identity

`pi = 16 atan(1/5) - 4 atan(1/239)`

and alternating-series remainder bounds. There is no floating-point sign decision.

Exact scan result:

| even dimension | certified coefficient signs from zero | first certified negative degree |
|---:|---|---:|
| `d=2` | degrees `0,...,5` positive | `6` |
| `d=4` | degrees `0,...,16` positive | `17` |
| `d=6` | degrees `0,...,27` positive | `28` |
| `d=8` | degrees `0,...,39` positive | `40` |

For `d=2`, the checker returns exactly

`c_6 = 61/240 - 4/(5*pi) = (61*pi-192)/(240*pi) < 0`.

For `d=4`, the first negative coefficient is exactly

`c_17 = -163135746061/30707712000 + (23226058112/1391630625)/pi < 0`.

The much larger exact `d=6` and `d=8` rational pairs, together with certification that every earlier coefficient in the displayed ranges is positive, are archived in `p0411_small_even_audit.out` rather than duplicated here.

Outcome of #16: **finite exact audit information**. It confirms that the `d=2` failure is not numerically isolated in the first few even dimensions, while making no claim that the degree sequence `6,17,28,40` has a closed form or proves the all-even theorem. The earlier analytic Pringsheim result already supplies the all-even existence statement; this table is an independently useful finite check, not a re-counted theorem.

## 6. Method #25 — COUNT THE SAME THING TWICE: independent `d=2` reconstruction

The archived campaign proof packet derives the `d=2` obstruction from the source's closed arctangent formula. This run reconstructs the same coefficient from the Proposition 5.1 radial integral lane used above.

For `d=2`, `n=1`. The exact radial recurrence gives

`G_1'(1)   = -1/2 + 2/pi`,

`G_1''(1)  =  5/4 - 4/pi`,

`G_1'''(1) = -33/8 + 13/pi`,

`G_1^(4)(1)= 285/16 - 56/pi`,

`G_1^(5)(1)= -3045/32 + 299/pi`,

`G_1^(6)(1)= 38745/64 - 1902/pi`.

Using

`[u^6]G_1(e^{2u}) = (2^6/6!) sum_(k=0)^6 S(6,k) G_1^(k)(1)`

gives exactly

`[u^6]F_2(u) = 61/240 - 4/(5*pi) = (61*pi-192)/(240*pi)`.

This is **identical** to the archived arctangent-formula coefficient. The checker asserts exact equality of the two rational-plus-`1/pi` representations and then certifies negativity from its rational `pi` enclosure.

Outcome of #25: **succeeded as an adversarial self-check**. Two source-faithful derivations land on the same exact finite obstruction. This does not constitute an outside audit and does not re-label the older coefficient discovery as new NM13-05 progress.

## 7. Current source and literature check — 2026-09-19

Fresh bounded queries included:

- `"Ideal Poisson-Voronoi tessellations on hyperbolic spaces" Conjecture 7.5 positive coefficients 2026`;
- `"Ideal Poisson-Voronoi tessellations on hyperbolic spaces" erratum correction Conjecture 7.5`;
- `"Ideal Poisson-Voronoi" D'Achille Khezeli 2026 convergence`;
- `"Face volume densities" D'Achille Thale 2026 hyperbolic Voronoi`.

The original D'Achille--Curien--Enriquez--Lyons--Unel paper is published in *The Annals of Probability* 54(2), DOI `10.1214/25-AOP1781`, with publication date 2026-03-06 in the current bibliographic record. The maintained source still contains the P0411 source family recovered in the repository.

Two later 2026 papers were rechecked:

- D'Achille--Thale, arXiv:2606.26049, submitted 2026-06-24, studies face-volume densities / typical face volumes;
- D'Achille--Khezeli, arXiv:2606.30517, submitted 2026-06-29, studies convergence to IPVTs and graph variants.

Mellick's 2026 *Proceedings of the AMS* paper resolves a different indistinguishability question from the original IPVT paper. A May 2026 D'Achille seminar listing and a current author/publication listing were also visible. None of these bounded results supplied an erratum, corrected transformed variable, or a source-matching resolution of the Conjecture 7.5 even-dimensional coefficient clause.

This is **bounded negative evidence only**. It is not proof of worldwide novelty, priority, or absence of private/source-author clarification. Classical ingredients such as Machin's identity, alternating arctangent bounds, Stirling composition, and Pringsheim's theorem are prior art and are not claimed as new.

## 8. Honest mathematical status and audit gate

Current source-scope disposition remains split:

- scaled-hole monotonicity: prior campaign PROVED candidate;
- odd-dimensional positive rational polynomial: prior campaign PROVED candidate;
- even-dimensional positive `u`-Maclaurin clause: **REFUTED candidate under the literal displayed-variable reading**, already by the archived exact `d=2` coefficient; this run adds an independent source-integral reconstruction and exact small-even audit table;
- decreasing boundary-distance density for all `d>=2`: NM13-05 PROVED candidate, with frozen metric `d_bad=+infinity`;
- strict IFR / sharp-tail / all-even analytic strengthenings: NM13-05 candidate extras, not necessary for the minimal source refutation;
- median `<` mean: PROVED candidate consequence.

**Fleet closure remains false.** Current independent audit count is still **0/2**:

- P26: newest report audits `R06 ROMERO-MAX4-N9`, not P0411;
- NM13-06: newest report is successor-admission work and explicitly recognizes P0411 as still owned by NM13-05; it does not contain a P0411 PASS.

A repository search for `P0411-AUDIT` returned no current result. Self-checks and owner-track double derivations do not count as either required OTHER-track audit.

No paper folder is created because the two-audit closure gate is not satisfied.

## 9. Next step and six-run rotation guard

The mathematically useful owner-track package is now audit-normalized: the literal source refutation can be checked at `d=2` without depending on the stronger Pringsheim theorem, while the density theorem remains separately frozen at `d_bad=+infinity`.

Next invocation must first recover any new P26 or NM13-06 P0411 audit and any source correction. If the closure gate is still incomplete and `d_bad` remains `+infinity`, then that is the **sixth consecutive unchanged metric run**. The CLOSABLE rotation rule must then take precedence: write the full P0411 terminal handoff, preserve `d_bad=+infinity`, all source/interpretation qualifications, artifact pointers, audit state, and recovery counters, then resume shard-4 successor admission without treating the handoff as a release to steal another owner's source.

If, before that rotation point, an independent audit lands with a concrete source-matching repair obligation, the reserved next methods are #4 PROVE SOMETHING WEAKER COMPLETELY, #12 FIND WHAT IS CONSERVED, and #20 FIND WHY THE ALGORITHM FAILS. These are **not tried in this run** and must not be spent merely to avoid required rotation.

## 10. Model / scheduler-control truth

The exposed task-control schema still provides title/prompt, schedule or relative-start configuration, timing mode, enabled state, list, and update operations. It exposes **no bindable model-family selector, no bindable reasoning-effort selector, and no authenticated applied-runtime attestation**. GPT-6/maximum therefore remains prompt-only in this surface.

Making the request binding would require an owner-authorized product/workspace/admin/API scheduling surface that persists model/reasoning routing fields and returns authenticated applied-runtime metadata.

The historical P26 `You cannot modify this task` event is an authorization-context boundary, not evidence that P26 is globally immutable. Current `RESULTS.md` records a later authorized context in which the P26 prompt update succeeded. If a denial recurs, the compliant workaround is the same task's owning/otherwise-authorized workspace/account/API/admin context or an approved platform ownership/permission repair path — never duplication or access-control bypass.

No scheduler, permission, workflow, public surface, email/Drive resource, paid-compute resource, shared root, peer namespace, D-series file, or canonical claim was modified by this invocation.

## 11. Structured ledger_delta for P26

```yaml
ledger_delta:
  track: NM13-05
  source_id: P0411
  claim_id: P0411
  canonical_dedup_key: boundary-hole_monotonicity_and_coefficient_positivity_for_ideal_cells
  shard_mod13: 4
  category: CLOSABLE_OUTSIDE
  run_kind: POST_STUCK_RECOVERY_RESEARCH
  source_status: REFUTED_CANDIDATE_LITERAL_EVEN_COEFFICIENT_CLAUSE_WITH_PROVED_CANDIDATE_DENSITY_CLAUSE
  fleet_closed: false
  metric_name: d_bad
  metric_before: +infinity
  metric_after: +infinity
  metric_movement: none
  unchanged_runs_before: 4
  unchanged_runs_after: 5
  recovery_count_before: 1
  recovery_count_after: 1
  methods:
    - number: 1
      name: CHANGE_THE_CATEGORY
      outcome: reduced_package_to_minimal_analytic_audit_object_separating_literal_refutation_from_density_and_extras
    - number: 16
      name: COMPUTE_EVERY_SMALL_CASE_AND_STARE_AT_THE_SEQUENCE
      outcome: exact_small_even_scan_first_negative_degrees_d2_6_d4_17_d6_28_d8_40_with_rational_pi_sign_certification
    - number: 25
      name: COUNT_THE_SAME_THING_TWICE
      outcome: proposition_5_1_radial_lane_exactly_matches_archived_d2_arctangent_sixth_coefficient
  new_claims:
    - finite_audit_observation: exact_first_negative_degrees_for_d_2_4_6_8
      scope: audit_aid_not_source_theorem_not_metric_movement
  finite_core:
    checker: proofnet24/NM13-05/artifacts/2026-09-19/p0411_small_even_audit.py
    output: proofnet24/NM13-05/artifacts/2026-09-19/p0411_small_even_audit.out
    result: ALL_EXACT_CHECKS_PASS
    label: self_check_not_independent_audit
  audit_p26: not_recovered
  audit_nm13_06: not_recovered
  audits_complete: 0_of_2
  predecessor_report_commit: 1c34dd2db8c54525ffb92bd1cfd83611a09e6972
  prewrite_head: 7263fd4a1ee2e0388378d1bec24970d8726e4fa7
  predecessor_to_prewrite_ahead: 109
  predecessor_to_prewrite_behind: 0
  next_methods_if_audit_repair_preempts_rotation: [4, 12, 20]
  next_step: check_audits_and_source_correction_then_if_still_unclosed_record_sixth_unchanged_and_terminal_handoff_rotation
  rotation_guard: next_unchanged_run_is_sixth_and_mandatory_for_closable_target
```

## 12. Mutation boundary

This invocation creates exactly this one immutable report under `proofnet24/NM13-05/runs/` plus the three warranted substantive own-namespace audit artifacts listed above. It does not edit the canonical P0411 claim, shared root ledgers, campaign roots, source/attempt ledgers, peer namespaces, D-series files, workflows, permissions, public surfaces, email/Drive resources, paid-compute resources, or any schedule. The report is to be read back at its returned creation commit; no receipt-only follow-up commit is authorized.

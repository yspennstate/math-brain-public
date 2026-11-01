Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.**

# NM13-13 — successor admission screen: static residue-12 Codex-P corpus exhausted

Status: **ADMISSION_PENDING**. Successor metric: **UNMEASURED -> UNMEASURED**. Mathematical progress: **none**; this invocation is admission screening only. No Section-B method is reported as tried. The reserved first-successor methods **B2 / B14 / B16** remain unspent.

## 1. Authoritative continuity recovered

This invocation continued from the newest verified NM13-13 report,

`proofnet24/NM13-13/runs/2026-09-19/2026-09-19T19-04-00Z__p0083-triangle-leaf-all-p-terminal-handoff-successor-screen.md`

(created at `1187130d733ed4327e06fbf08f613786d1827cc8`). That report is controlling: P0083 is terminally handed off after consuming both permitted HARD recovery episodes, and **must not be reopened by NM13-13 without a fresh explicit owner reassignment**. Its successor cursor was **after P0126 in the legacy Codex-P residue-12 corpus**.

At run start I read the required governance/state files: `FLEET_RULES.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, `operations/NEW_METHODS_2026-09-16.md`, the later owner-authorized NM13 deployment amendment `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`, `QUEUE.md`, `POSTED.md`, `RESULTS.md`, `probability_campaign_2026_09/INDEX.md`, `probability_campaign_2026_09/RANKING.md`, the newest own report, neighboring NM13 reports, the Codex intake ledger, claim inventory, and targeted attempt/handoff history.

The pre-write `master` snapshot was `c2b2b2f4af804173b8c9e66c600e3e857e05c3a4`. Exact comparison from the controlling own report commit to that snapshot is `ahead_by=132`, `behind_by=0`. In that full interval the only `operations/claims/*.md` addition is `operations/claims/SHPECTOROV-ZHAO-2026-SRG69.md`, already owned by another native slot. There is **no mutation of the screened Codex `problems.jsonl`, no release of another claimed target, and no admission-relevant root queue/posted/campaign mutation**. SRG69 is therefore unavailable to this worker and was not touched.

The newest NM13-01 report remains an admission screen, not a P0083 audit. No P26/NM13-01 audit of P0083 is inferred from unrelated audit activity.

## 2. Canonical identity and shard rule

For every candidate below I used the canonical `dedup_key` from the Codex source ledger before hashing; I did not hash display titles or aliases. Targeted checks against the mirrored Claude/F intake dedup indexes and repository search found no alternate canonical identity that would justify duplicate ownership under a different ID. The shard test is exactly

`int(SHA256(UTF-8 canonical_dedup_key).hexdigest(), 16) mod 13 = 12`.

Continuing strictly after P0126, the static Codex-P scan found the following residue-12 identities through the terminal populated P0488 frontier. Hash prefixes are audit aids; the full canonical strings make the residues reproducible.

| ID | canonical dedup_key | SHA256 prefix | disposition |
|---|---|---:|---|
| P0132 | `measurable_loop_erasure_of_planar_brownian_motion` | `1917a1ad0b11` | reject: continuum measurability/scaling-limit problem, no finite certificate metric |
| P0158 | `ordered-phase_susceptibility_exponent_on_random_trees_and_graphs` | `9b976a89a2d8` | reject: broad critical-exponent asymptotic |
| P0159 | `quenched_non-gaussian_critical_spin_limits_on_heterogeneous_random_graphs` | `3d59a93a0619` | reject: broad quenched distributional limit |
| P0162 | `fourier_entropy_versus_total_influence` | `06ad9d9aa4f0` | **exclude**: famous current FEI conjecture and already active/retired P03 route |
| P0179 | `uniform_permutation_representations_of_the_gieseking_group` | `30a64b21be84` | reject: strong-convergence/operator-norm asymptotic, no finite milestone |
| P0199 | `cutoff_for_cyclic-to-random_transpositions` | `0f9cca2fe25a` | reject: asymptotic cutoff program |
| P0217 | `percolation_of_merging_planar_empires` | `53f9b9290ca0` | reject: infinite-space percolation classification |
| P0218 | `growth_exponents_in_the_spatial_city-formation_model` | `08b706f8f932` | reject: broad growth-exponent program |
| P0248 | `diameter-squared_optimized_relaxation_on_cayley_graphs` | `5ef4e9169b31` | **exclude**: repository records literature resolution; never reopen |
| P0278 | `cutoff_for_unit-rate_zero_range_on_higher_dimensional_lattices` | `9f5103bb7411` | reject: asymptotic cutoff program |
| P0293 | `order_one_over_n_accuracy_for_least_workload_mean_field_queues` | `8f6fe868746a` | closest quantitative lead; fails realistic-movement / finite-certificate admission gate |
| P0330 | `higher-order_free-energy_expansion_of_the_two-dimensional_coulomb_gas` | `97424898ba32` | reject: open-ended thermodynamic expansion |
| P0332 | `regularity_threshold_for_bounded_coulomb-gas_linear-statistic_fluctuations` | `453fc7ab1abf` | reject: broad analytic regularity threshold |
| P0369 | `nonendogeny_from_instability_of_the_diagonal_coupling` | `304118e48247` | reject: methodological/topological criterion rather than fixed finite target |
| P0375 | `arw_375` | `426e5fc45f23` | reject: infinite-volume microscopic-law universality |
| P0380 | `arw_380` | `d96bdf184393` | reject: infinite-volume/finite-volume density identity |
| P0440 | `waiting-time_tails_with_deterministic_multiserver_setup` | `36b70d3adfa6` | quantitative but source target is an open family of moment/tail bounds, not a frozen certifiable number |
| P0466 | `joint_intermediate_level-set_limits_from_one_continuum_field` | `bc4a364d54de` | reject: joint continuum scaling limit |
| P0469 | `explicit_law_of_the_position_and_height_of_the_dgff_maximum` | `6332ad1be403` | reject: continuum limiting density/PDE problem |
| P0479 | `scaling_law_of_effective_resistance_in_dgff_conductances` | `185120d3f94f` | reject: distributional scaling law |

Every listed hash has residue 12. P0488 itself is source-ledger **resolved_in_literature** and marks the populated Codex frontier; resolved rows are excluded before any ownership selection. There is no populated P0489+ Codex-P source row in the checked static ledger.

## 3. Closest lead: P0293 did not pass admission

P0293 is the only residue-12 row in this continuation that plausibly fits the instruction's fallback allowance for a real quantitative milestone. The direct source is Tim Hellemans and Benny Van Houdt, *Open problems in refined mean field approximations*, Queueing Systems 100 (2022), DOI `10.1007/s11134-022-09756-9`. The source defines the finite-N mean workload `W_N^{LL(d)}(lambda)` and mean-field workload `W^{LL(d)}(lambda)`, reports experiments for LL(2) in which `N*(W_N-W)` appears stable, and explicitly asks whether continuous-variable mean-field models can be proved **1/N-accurate**.

Canonical identity/ownership checks for P0293 were clean: exact-ID, exact-key, title, `operations/claims/P0293.md`, proofnet ownership, handoff, and attempt searches recovered no active or historical exclusive owner and no source-matching canonical claim. The full claim-file delta after the predecessor report also contains no P0293 claim.

Nevertheless I did **not** admit it. The reason is substantive, not merely subject preference. The source clause is a stationary continuous-state stochastic-process error theorem, not a finite construction or finite obstruction. I recovered no already-certified nontrivial rate exponent for the exact LL(d) target that could serve as the required measured baseline, and no finite certificate can decide the source-wide `O(1/N)` assertion. Freezing an arbitrary single `lambda`, service law, or finite `N` would silently weaken the source question, while declaring a baseline of zero would violate the UNMEASURED rule. Given the owner's instruction to admit a HARD target only when its tracked quantity can realistically move or a finite certificate can decide a source-relevant clause, P0293 remains a **screened lead, not READY**.

P0440 was the next quantitative-looking row, but it is even less suitable for a frozen metric: the source asks for a family of higher-moment or tail bounds under deterministic multiserver setup. No canonical single bound/cutoff is supplied by the row, so choosing one would invent the target.

## 4. Bounded current-literature checks

Dated 2026-09-19, public-web and repository checks were deliberately bounded and are **not** evidence of worldwide openness.

- **P0293.** Direct source PDF checked at `https://win.uantwerpen.be/~vanhoudt/papers/2022/Questa_100.pdf`; Crossref confirms DOI `10.1007/s11134-022-09756-9` and the 2022 version of record. Exact-title, `least-loaded-of-d`, workload, stationary mean-field, and `O(1/N)` queries did not recover a later theorem settling the exact LL(d) stationary error question. Discrete-state/refined-mean-field `1/N` results and results for other queueing models were not treated as source-matching resolutions.
- **P0132.** 2026 searches around Brownian loop-erasure/SLE2 recovered Berestycki--Sauzedde's *Brownian paths as loop-decorated SLEs* (`arXiv:2602.04673`) and related 2026 work. These reinforce that the row is a continuum coupling/measurability question; they do not create a finite source milestone suitable for this lane.
- **P0162.** González--MacManus--Pereyra, *Further evidence towards the Fourier Entropy-Influence conjecture* (`arXiv:2606.00246`, May 2026), still explicitly treats FEI as a conjecture. Han's 2025 Combinatorica bound is progress, not a resolution. This row is excluded independently by the owner's famous-problem and existing-P03 rules.
- **P0248.** Repository history already records the Cayley relaxation target as resolved in the literature, so no reopening was considered.

Access limits: public web plus the private repository; no claim of exhaustive MathSciNet/zbMATH/citation-graph coverage. Negative searches are only bounded evidence.

## 5. Ownership/race result

The exact predecessor-to-prewrite comparison contains 132 commits and exactly one canonical claim-file addition: `SHPECTOROV-ZHAO-2026-SRG69.md`, owned elsewhere. No screened intake ledger changed. A second exact delta over the latest 24 commits contained no claim-file or intake mutation. Therefore there was no lawful newly released residue-12 target to substitute for the static screen above.

No canonical claim was created because **no candidate passed admission**. No owner was overwritten and no disabled/inaccessible scheduler was treated as releasing ownership.

## 6. Cursor and next action

The durable screening cursor is now:

`AFTER_P0488 / LEGACY_CODEX_P_STATIC_RESIDUE12_CORPUS_EXHAUSTED`.

Future NM13-13 admission runs should be **delta-only**: inspect newly appended/modified source ledgers, QUEUE changes, canonical claim releases, or genuinely new outside-source leads whose canonical identity hashes to residue 12. They should not rescan the unchanged P0001-P0488 static Codex corpus. If a new candidate passes all gates, then and only then create its canonical claim create-only, read it back, freeze one measured metric, and actually attempt B2/B14/B16 in the substantive continuation.

P0083 remains terminally handed off and is not lawful fallback inventory.

## 7. Model/scheduler control status

The exposed scheduler control schema still offers task prompt/title, schedule/timing, enabled state and related timing controls; it exposes **no model-family selector and no reasoning-effort selector**. Thus `GPT-6 / maximum` remains prompt text only in this environment. Changing that would require the scheduling product/API to expose binding model and reasoning fields (or an owning administrative context that actually provides them); this run cannot manufacture those controls.

The historical P26 `You cannot modify this task` denial is treated as an authorization-context failure, not as a released task. The lawful workaround is to use the owning/authorized product, workspace, API/admin context, or authorized platform support. No duplication, permission bypass, scheduler mutation, or support escalation was attempted here.

## 8. Structured ledger_delta

```yaml
ledger_delta:
  worker: NM13-13
  category: HARD_OUTSIDE
  state_before: ADMISSION_PENDING
  state_after: ADMISSION_PENDING
  source_or_claim_id: null
  canonical_claim_created: false
  successor_metric:
    before: UNMEASURED
    after: UNMEASURED
  mathematical_progress: false
  screening_progress_only: true
  methods_actual: []
  methods_reserved_for_first_admitted_run: [2, 14, 16]
  p0083_terminal_handoff:
    remains_binding: true
    hard_recoveries_consumed: "2/2"
  screening_cursor:
    before: "after P0126 in legacy Codex-P residue-12 corpus"
    after: "AFTER_P0488 / LEGACY_CODEX_P_STATIC_RESIDUE12_CORPUS_EXHAUSTED"
  closest_screened_lead:
    id: P0293
    dedup_key: order_one_over_n_accuracy_for_least_workload_mean_field_queues
    sha256: 8f6fe868746ad9b117e896f2e48dff871f3cf1fcc25b0e03c0651a99cadf26ef
    residue_mod_13: 12
    disposition: "SCREENED_NOT_READY: quantitative source clause, but no recovered measured baseline and no realistic finite certificate / source-wide movable metric"
  next_step: "delta-only admission scan for new/released residue-12 inventory; do not rescan static P0001-P0488 and do not reopen P0083"
  audits:
    P26: NOT_APPLICABLE_NO_COMPLETED_SUCCESSOR_CLAIM
    NM13-01: NOT_APPLICABLE_NO_COMPLETED_SUCCESSOR_CLAIM
  bounded_literature_check_date: 2026-09-19
```

No artifacts were created because screenings are not mathematical progress and no finite claim warranted a checker. No shared root, peer namespace, canonical claim, schedule, workflow, permission, public surface, email/Drive resource, or paid compute was modified.
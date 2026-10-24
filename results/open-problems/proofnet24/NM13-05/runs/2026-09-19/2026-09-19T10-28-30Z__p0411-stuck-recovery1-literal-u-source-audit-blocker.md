Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not verified GPT-6 at maximum, and I do not claim otherwise. NO METRIC MOVEMENT: `d_bad = +infinity -> +infinity`; THINKING/STUCK RUN with no new theorem claim; NEW-METHODS genuinely attempted: #22 READ THE FAILURES, NOT THE SUCCESSES, #26 HUNT THE SPORADIC CASE, #27 SWAP THE QUANTIFIERS.**

# NM13-05 — P0411 Section-I stuck report: literal-u source diagnosis and recovery choice

Run date: 2026-09-19.  
Repository / branch: `yspennstate/math-open-problems` / `master`.  
Worker / namespace: `NM13-05` / `proofnet24/NM13-05/`.  
Category: **CLOSABLE OUTSIDE**.  
Canonical source / claim ID: `P0411`.  
Canonical dedup key: `boundary-hole_monotonicity_and_coefficient_positivity_for_ideal_cells`.  
SHA-256: `55ed478fc4a65273f15d74d172f46ee938595061ac9a7d82ad3a03afcfd6c1cc`.  
Shard: `4 mod 13`.

## 1. Why this invocation is a thinking/stuck run

The newest immutable NM13-05 predecessor is

`proofnet24/NM13-05/runs/2026-09-19/2026-09-19T09-29-00Z__p0411-exact-radius-infinite-sign-changes-stuck-trigger.md`

at creation commit

`81ea9f7a3803e615404405dfe4ba3d13b1564dd4`.

That report preserved the frozen metric

\[
d_{\rm bad}:=\min\{d\ge2:g_d=-H_d'\text{ is not nonincreasing on }[0,\infty)\},
\]

with `d_bad=+infinity` if no such dimension exists, and recorded the third consecutive unchanged run. Section I therefore requires this invocation to be a **thinking/stuck run with no new theorem claim before the full blocker diagnosis and one recovery choice**. I obey that requirement here.

Certified metric before this run: `d_bad=+infinity`.  
Certified metric after this run: `d_bad=+infinity`.  
Metric movement: **none**.  
Supported unchanged-run counter: `3 -> 4`.  
Recovery counter: `0 -> 1`.

The six-unchanged-run CLOSABLE rotation threshold has **not** fired yet.

## 2. Authoritative continuity and mandatory reads

Before diagnosing the blocker I reread or exact-target-recovered current `master` state for:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- the newest NM13-05 report quoted above;
- canonical claim `operations/claims/P0411.md`;
- archived attempt `P0411-A001` and proof packet `probability_campaign_2026_09/codex_20h_20260906/proofs/IPVT_boundary_hole_partial.md`;
- current P0411 search hits in the intake/campaign inventory and attempt-integrity records;
- newest neighboring NM13-06 report and newest P26 audit report.

The canonical claim remains `CLAIMED / MANUALLY ADMITTED / CLOSABLE OUTSIDE`, owner `proofnet24/NM13-05`; there is no release, reassignment, retirement, or conflicting alias claim. The newest NM13-06 report explicitly sees P0411 as still owned/stuck-triggered rather than released. The newest P26 run is a stuck report about the unrelated Romero split-reliability obstruction, not a P0411 audit. Repository search still recovers **no P0411 PASS from P26 and no P0411 PASS from NM13-06**. Audit count remains `0/2`.

The large append-only intake JSONL corpora are not honestly renderable in full model-visible form every hour through this connector. I therefore do not claim to have visually reread every unchanged byte. I recovered the exact P0411 canonical identity/attempt material and inspected the complete Git delta from the predecessor report to the frozen pre-write snapshot for any mutation of intake/source ledgers, claims, ownership/handoff state, or shared exclusion roots. Missing display is not treated as permission to reset, reopen, or invent history.

Frozen pre-write snapshot observed before this report write:

`779db2335bc615c199d6cfdbde62c88cfad51cfc`.

Exact comparison from predecessor creation commit `81ea9f7a3803e615404405dfe4ba3d13b1564dd4` to that snapshot reports:

- status `ahead`;
- `103` commits ahead;
- `0` behind;
- `too_large = null`.

The complete changed-file list contains no edit to `operations/claims/P0411.md`, no P0411 audit, and no mutation of root `QUEUE.md`, `POSTED.md`, `RESULTS.md`, campaign `INDEX.md` / `RANKING.md`, or the screened P0411 source/attempt records that would release, close, or redefine this target. New unrelated fleet claims/work do not change P0411 ownership.

## 3. Current source text and bounded literature refresh — 2026-09-19

Primary source checked again:

- Matteo D'Achille, Nicolas Curien, Nathanaël Enriquez, Russell Lyons, Meltem Ünel, *Ideal Poisson--Voronoi tessellations on hyperbolic spaces*, Annals of Probability 54(2), 846--891 (2026), DOI `10.1214/25-AOP1781`; current bibliographic records give publication date 2026-03-06. The current arXiv/author version is dated 2025-03-19.

The source's future-directions paragraph is unambiguous about the variable in the even-dimensional coefficient clause: for even `d` it writes the hole probability as

\[
H_d(u)=\frac{e^{-(d-1)u}}{f(u)}
\]

and describes `f` as an infinite power series with positive coefficients (with the stated rational-linear-combination arithmetic restriction). It does **not** state a transformed variable `phi(u)` there. The same source gives the exact `d=2` formula in Remark 5.2 and the exact `d=3` formula

\[
H_3(u)=\frac{3e^{-2u}}{2+e^{2u}}.
\]

Fresh dated search strings included:

- `"Ideal Poisson-Voronoi tessellations on hyperbolic spaces" "Conjecture 7.5" positive coefficients`;
- `"Ideal Poisson-Voronoi tessellations on hyperbolic spaces" erratum correction 2026`;
- `"Ideal Poisson-Voronoi" "Conjecture 7.5" 2026`;
- `"Ideal Poisson-Voronoi" D'Achille Khezeli 2026 convergence`.

Later author / source-adjacent material recovered in the bounded search:

- D'Achille--Thäle, *Face volume densities of positive-intensity and ideal Poisson--Voronoi tessellations in hyperbolic spaces*, arXiv:2606.26049, submitted 2026-06-24, concerns face-volume densities and typical face volumes, not this boundary-distance coefficient statement;
- D'Achille--Khezeli, *Convergence towards Ideal Poisson--Voronoi tessellations with a focus on Diestel--Leader graphs*, arXiv:2606.30517, submitted 2026-06-29, gives general convergence/uniqueness results and answers another IPVT open problem, not this coefficient statement;
- Mellick, *Indistinguishability of cells for the ideal Poisson Voronoi tessellation*, Proc. AMS (2026), resolves a different question from the IPVT paper.

The bounded search recovered no erratum, author correction, later paper, or source note replacing the displayed variable `u` by a transformed variable in this clause. This is **bounded negative evidence only**; it is not a claim of worldwide openness, novelty, priority, or author intent beyond the text actually found.

## 4. Section-I blocker diagnosis

### (a) Exact statement that blocks

The literal source clause is the following coefficient-positivity question for every even dimension `d=2m`:

\[
\boxed{
F_{2m}(u):=\frac{e^{-(2m-1)u}}{H_{2m}(u)}
=\sum_{k\ge0} a_{m,k}u^k
\quad\text{with all }a_{m,k}>0\ ?
}
\tag{B}
\]

For the **literal displayed variable `u`**, the archived campaign already gives the exact `d=2` obstruction

\[
[u^6]F_2(u)=\frac{61\pi-192}{240\pi}<0,
\]

and the two preceding NM13-05 reports contain stronger all-even analytic refutation candidates. Thus the mathematical blocker is no longer “find a counterexample to (B).” The remaining obstacle is whether the source should somehow be reinterpreted as an **unstated different problem** such as

\[
\exists\,\phi\ne\mathrm{id}:\quad
F_{2m}(u)=\sum_{k\ge0} b_{m,k}\,\phi(u)^k,
\qquad b_{m,k}>0.
\tag{B'}
\]

No recovered source text defines such a `phi`. A worker cannot silently replace (B) by (B') and still call the result source-matching.

### (b) Every route tried and the precise reason it no longer resolves the blocker

The routes below are the actual P0411 chain, not a retroactive relabeling.

1. **#2 ATTACK THE NEGATION FIRST.** Searched for a density upturn / finite counterexample. It found none and exposed the score structure that eventually yielded a proof. It does not adjudicate an unstated change of variable.
2. **#8 DISCRETIZE.** Finite dimension/`u` reconnaissance found no density violation. It was correctly not used as a certificate and says nothing about source semantics.
3. **#11 DUALIZE.** The score/variance representation proved decreasing density in all dimensions, saturating the frozen metric at `+infinity`. Once saturated, repeating this route cannot move `d_bad`.
4. **#3 PROVE SOMETHING STRONGER.** Strict IFR / log-concavity and sharp hazard bounds strengthened the density theorem but did not change the frozen metric or the wording of the coefficient clause.
5. **#18 SAY IT IN ANOTHER LANGUAGE.** Hazard/log-normalizer language clarified the density mechanism, not the source's intended series variable.
6. **#29 ADD THE POINTS AT INFINITY.** Exact tail asymptotics and hazard endpoint were obtained, again without changing `d_bad` or the semantic issue.
7. **#23 DO WHAT THE PROPOSER DID NOT EXPECT.** Treated the `d=2` sign failure as potentially universal and led to the all-even obstruction. It attacks the literal statement, not an unstated transformed variant.
8. **#7 TAKE THE LIMIT.** The `q -> -1` branch endpoint supplied a complex singularity obstruction. It refutes positivity in `u`; it cannot tell us what the authors might have meant but did not write.
9. **#21 ASK WHO ELSE HAS THIS SHAPE.** Pringsheim's theorem converted the branch singularity into a positivity contradiction. Same limitation: it is a theorem about the actual `u`-series.
10. **#14 FIND THE GROUP ACTING.** Exponential covering geometry identified `u=+/- i*pi/2` as the nearest branch preimages. This fixed the exact radius, not source semantics.
11. **#17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE.** The exact `pi/2` radius plus Pringsheim on tails gave infinitely many signs. This strengthens the literal refutation but does not license changing the variable.
12. **#30 DO ONE PRIME, ONE SCALE, ONE DIRECTION AT A TIME.** Separating imaginary singular directions from the regular positive-real direction completed the tail argument. Again, no semantic bridge.
13. **This run #22 READ THE FAILURES, NOT THE SUCCESSES.** I reread the archived `P0411-A001` interpretation warning, the current source wording, author pages, and later IPVT papers. Outcome: no documented correction or transformed variable was recovered. The old warning remains a prudent publication caveat, but it is not evidence for an alternate source statement.
14. **This run #26 HUNT THE SPORADIC CASE.** I treated `d=2` as the most dangerous exceptional case rather than doing more general algebra. Outcome: the exception cuts the other way—the source itself gives the exact `d=2` formula, and the archived exact sixth coefficient is already negative. There is no surviving literal `d=2` positivity special case to prove.
15. **This run #27 SWAP THE QUANTIFIERS.** I separated “the source specifies this `f(u)`” from “there exists some reparametrization under which a positive series exists.” Outcome: the latter is a materially different existential problem, not an equivalent restatement supplied by the source. It cannot be used to rescue (B) without an author/source correction.

### (c) What a proof would have to contain that no route so far contains

For the literal source text, no additional hidden mathematical ingredient is presently identified: the density clause has a full candidate proof and the positive-coefficient clause has an exact literal counterexample plus stronger analytic obstruction candidates.

What the current package lacks is **external validation, not another owner-track lemma**:

1. an independent source-reading decision that the displayed `f(u)` means a Maclaurin series in `u` exactly as written, or an actual author/erratum correction if it does not;
2. a P26 end-to-end audit of the source-matching density/refutation package;
3. a genuinely distinct NM13-06 end-to-end audit;
4. a prior-art review deep enough to distinguish classical ingredients (in particular Pringsheim) from any genuinely new synthesis.

None of these can be manufactured by repeating NM13-05's own argument.

### (d) Simplest special case still unproved

Under the **literal source statement**, I identify no remaining mathematical special case that is both source-matching and genuinely unproved inside the candidate package. The simplest still-unverified unit is instead the **independent reproduction of the `d=2` literal contradiction** from the published formula, followed by independent checking of the all-dimensional density argument. That is an audit obligation, not permission for NM13-05 to count another self-check as progress.

If one insists on studying (B'), then even `d=2` becomes a new reparametrization problem—but (B') is not the source problem and is therefore not adopted as this worker's target.

### (e) Nearest solved problem in the literature and what it uses that this blocker lacks

The nearest exact source-adjacent solved case is the paper's own Remark 5.2. It evaluates the hole law explicitly in `d=2` and gives in `d=3`

\[
H_3(u)=\frac{3e^{-2u}}{2+e^{2u}}.
\]

That solved low-dimensional case uses direct exact evaluation of the source integral/rational reduction. The current blocker does **not** lack an analogous analytic technique: exact source formulas and analytic reductions are already available. It lacks a documented alternate source definition (if one exists) and the two required independent audits. No amount of further owner-track symbolic manipulation can supply an unstated author correction or count as an independent audit.

## 5. Exactly one recovery choice

Section I requires exactly one choice. I choose:

**REFUTE INSTEAD OF PROVE.**

The object attacked in this thinking run is the surviving *interpretation loophole*, not a new theorem: could the source-valid target secretly be a transformed-variable positivity statement rather than the displayed `u`-series?

Outcome of the recovery attempt: **no source-supported transformed-variable reading was recovered.** The current arXiv/source text explicitly writes `f(u)` in the distance variable; the author/publication pages and bounded 2026 follow-up search supplied no erratum or correction changing it. Therefore NM13-05 will continue to treat the literal displayed-variable clause as the source statement while preserving the publication caveat that an author could later clarify otherwise.

This is a source/interpretation diagnosis, **not a new mathematical theorem claim** and not fleet closure.

Recovery count therefore moves `0 -> 1`.

## 6. Next three Section-B moves if another P0411 research run is permitted before rotation

The next triple is deliberately different from this run and from the preceding run:

- **#1 CHANGE THE CATEGORY:** rewrite the source package as a minimal analytic-function/generating-function audit object, separating source statement, classical ingredients, and genuinely new deductions;
- **#16 COMPUTE EVERY SMALL CASE AND STARE AT THE SEQUENCE:** if used, independently reconstruct the first coefficients from the source integral in the smallest even dimensions solely as an adversarial audit aid, not as movement of `d_bad`;
- **#25 COUNT THE SAME THING TWICE:** derive the `d=2` obstruction independently from the closed arctangent formula and directly from Proposition 5.1's integral, so an eventual external auditor can compare two source-faithful derivations.

These are proposed next methods, **not tried in this run**. If the frozen metric reaches six consecutive unchanged runs before closure, the CLOSABLE rotation rule takes precedence and this target must be handed off/rotated rather than padded with more lemmas.

## 7. Honest status and closure gate

Source-wide candidate status remains split but source-faithful:

- scaled-hole monotonicity: prior campaign PROVED candidate;
- decreasing boundary-distance density for every `d>=2`: NM13-05 PROVED candidate, frozen metric `d_bad=+infinity`;
- strict IFR / sharp tail statements: NM13-05 PROVED candidate extras, not required to declare the source clause answered;
- odd-dimensional positive rational polynomial: prior campaign PROVED candidate;
- even-dimensional positive `u`-power-series clause: **REFUTED candidate** under the literal displayed-variable reading, already at `d=2`, later strengthened by NM13-05 analytic work;
- median `<` mean: PROVED candidate from decreasing density.

**Fleet closure remains false.** Required audits are still `0/2`: P26 has not supplied a P0411 PASS, and NM13-06 has not supplied a P0411 PASS. No paper folder is created in this run because closure protocol is not complete.

No new checker or artifact is created. That is deliberate: Section I requires diagnosis rather than another lemma/certificate, and a duplicate self-check would not move the metric or satisfy an independent audit.

## 8. Model / scheduler-control truth

The prompt requests GPT-6 with maximum reasoning, but this invocation actually identifies as **GPT-5.6 Sol**. Authenticated reasoning-effort telemetry is not exposed, so the reasoning level is **UNVERIFIED**. I do not claim GPT-6, maximum reasoning, an hour-long execution, or a support escalation.

The exposed task-control schema still provides scheduling/timing, prompt/title, enablement/list/update controls but **no bindable model-family selector, no bindable reasoning-effort selector, and no authenticated applied-runtime receipt**. GPT-6/maximum therefore remains prompt text only in this surface. Making it enforceable would require an owner-authorized product/workspace/API/admin surface that persists those inference-routing fields and reports the applied runtime.

The historical P26 `You cannot modify this task` event is context-specific authorization evidence, not a release. Current repository `RESULTS.md` records that a later authorized context successfully updated P26's prompt; that does not imply every context can edit it. If a denial recurs, the compliant workaround is the owning/otherwise-authorized account/workspace/API/admin context or supported platform ownership/repair path—not cloning the protected task or bypassing access controls. No scheduler modification or support request was made here.

## 9. Structured ledger_delta for P26

```yaml
ledger_delta:
  track: NM13-05
  source_id: P0411
  claim_id: P0411
  canonical_dedup_key: boundary-hole_monotonicity_and_coefficient_positivity_for_ideal_cells
  shard_mod13: 4
  category: CLOSABLE_OUTSIDE
  run_kind: SECTION_I_STUCK_THINKING
  source_status: REFUTED_CANDIDATE_LITERAL_EVEN_COEFFICIENT_CLAUSE_WITH_PROVED_CANDIDATE_DENSITY_CLAUSE
  fleet_closed: false
  metric_name: d_bad
  metric_before: +infinity
  metric_after: +infinity
  metric_movement: none
  unchanged_runs_before: 3
  unchanged_runs_after: 4
  recovery_count_before: 0
  recovery_count_after: 1
  stuck_triggered: true
  recovery_choice: REFUTE_INSTEAD_OF_PROVE
  methods:
    - number: 22
      name: READ_THE_FAILURES_NOT_THE_SUCCESSES
      outcome: no_source_erratum_or_transformed_variable_recovered
    - number: 26
      name: HUNT_THE_SPORADIC_CASE
      outcome: d2_is_already_exact_literal_counterexample_not_a_surviving_positive_case
    - number: 27
      name: SWAP_THE_QUANTIFIERS
      outcome: transformed_variable_existence_is_a_different_problem_not_source_equivalent
  new_claims: []
  finite_core: none_new
  new_artifacts: none
  audit_p26: not_recovered
  audit_nm13_06: not_recovered
  audits_complete: 0_of_2
  next_methods: [1, 16, 25]
  next_step: independent_source_faithful_audit_readiness_or_rotation_at_six_unchanged; do_not_reset_metric
  predecessor_report_commit: 81ea9f7a3803e615404405dfe4ba3d13b1564dd4
  prewrite_head: 779db2335bc615c199d6cfdbde62c88cfad51cfc
  predecessor_to_prewrite_ahead: 103
  predecessor_to_prewrite_behind: 0
```

## 10. Mutation boundary

This invocation creates exactly this one immutable report under `proofnet24/NM13-05/runs/` and then reads it back at the returned creation commit. It does not edit the canonical claim, shared root ledgers, campaign roots, attempt/source ledgers, peer namespaces, D-series files, workflows, permissions, public surfaces, email/Drive resources, paid-compute resources, or any schedule.
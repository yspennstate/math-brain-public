Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. NO MATHEMATICAL MOVEMENT: P13 remains `ADMISSION_PENDING`; successor metric `UNMEASURED -> UNMEASURED`. Methods actually tried: B17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE, B18 SAY IT IN ANOTHER LANGUAGE, B22 READ THE FAILURES, NOT THE SUCCESSES.**

# P13 outside successor — I0054 ownership screen and P0205 source-convention diagnostic

Date: 2026-09-19 UTC  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Native slot: `6aa7b253b37c8191b693d8dc79298d37`  
Own root: `proofnet24/P13-outside-successor`  
Status: **ADMISSION_PENDING**

## 1. Continuity and immutable exclusions

The newest preceding P13 report is

`proofnet24/P13-outside-successor/runs/2026-09-19/2026-09-19T22-08-53Z__successor-delta-g0004-released-hard-i0054-owned-c077.md`

at creation commit `abf8ac4b35bf81caffafb747f7064adcc37d8ac0`, blob `96878bb0cca09f6e6fa826360a40acb7b24abec2`.

Its state is preserved without reset:

- I0051 / Aldous--Janson Open Problem 9 is **RETIRED** and was not reopened;
- C0021 remains handed off;
- P0342 remains at its frozen source metric `2/2`, terminally handed off after the six-unchanged CLOSABLE rule, with closure audits still external/pending; ordinary P0342 attacking research was not restarted;
- P13 has no admitted successor, no successor denominator, and no successor unchanged/recovery counter yet.

I reread the owner directive at anchor `749da260517828ed311f6f1b1af74915c054bdf3`, current `operations/NEW_METHODS_2026-09-16.md`, campaign `INDEX.md` / `RANKING.md`, root `POSTED.md` / `RESULTS.md` / `QUEUE.md`, the newest own report above, current claim surfaces, the newest R11 I0054 report, the newest coordinator health/admission screens, and the relevant P0205 intake/attempt history. The append-only intake corpora are too large to claim that every historical byte was freshly rendered model-visible in one connector response; however, the exact complete Git delta below contains no `probability_1000_intake_*/problems.jsonl` mutation, so unchanged prior reconciliation is reused rather than falsely represented as a fresh whole-corpus read.

A fresh pre-write master snapshot was `664979ca169443dad543a50691850f62183ca258`. Exact comparison from the preceding P13 report commit to current master returned `ahead_by=135`, `behind_by=0`, `total_commits=135`, `too_large=null`. The complete changed-file set contains no root `QUEUE.md`, `RESULTS.md`, campaign `INDEX.md` / `RANKING.md`, or screened intake-`problems.jsonl` mutation. The material claim mutations are the already-screened HARD releases/reassignments, one resolved literal-source release, and newly owned HARD claims; none creates a free READY CLOSABLE target. Root `POSTED.md` changed only for posting metadata/exclusions, which does not create open inventory.

The latest coordinator health report at `operations/task_health/runs/2026-09-19T225200Z/status.md` independently records zero newly lawful free READY CLOSABLE successors among the material claim delta. The newer PROB20-05 admission-delta report at `2026-09-19T231200Z` reaches the same conclusion after checking all eight claim mutations. I use these as cross-checks, not as substitutes for the mandatory I0054/P13-specific work below.

## 2. Mandatory first successor screen: I0054 remains occupied

Source: David J. Aldous and Svante Janson, *The Critical Beta-splitting Random Tree II: Overview and Open Problems*, arXiv:2303.02529v3, revised 2025-04-18, Open Problem 18 in section 6.3.

The source asks for **superficially/genuinely different discrete models** whose scaling limit is the same `CTCS(infinity)` object; reproducing only an infinite object, relabeling the original finite construction, or applying a trivial rescaling is not source-matching.

Canonical ownership remains

`operations/claims/I0054.md`

with owner R11, native task `6aa7b68c70c481919b1a131eb67b6b24`. P13 therefore did not create, edit, shadow, or override an I0054 claim.

The newest R11 report recovered this invocation is

`runs/R11/2026-09-19T22-40-00Z_i0054-shuffled-sticky-u057-u058-c078-9d4c.md`.

It moves R11's internal distinct-construction count `77 -> 78`, using methods B6/B12/B29, while explicitly retaining source-level **PARTIAL / not CLOSED** status. That is peer progress, not P13 progress and not an ownership release.

Fresh bounded literature queries dated 2026-09-19 checked the exact arXiv identifier/title together with `Open Problem 18`, `CTCS(infinity)`, `discrete model`, later Aldous/Janson papers, and recent critical-beta-splitting papers. The search recovered Aldous--Janson Part III, Brandenberger--Chin--Mossel's 2025 harmonic-descent work, Chorbadzhiyska--Minchev--Savov arXiv:2608.18320 (2026-08-18), and Heng Ma arXiv:2609.14329 (2026-09-13). The 2026 papers announce resolutions of other height/fragmentation questions (for example Ma explicitly answers Aldous--Janson Open Problem 4), not exact Open Problem 18. This is bounded negative evidence only; it is not a worldwide-openness or novelty certificate.

Disposition: **I0054 = OWNED BY R11 / PARTIAL / SKIP**.

## 3. Highest useful free CLOSABLE-shaped residue: P0205 source ambiguity revisited mathematically

The live David Aldous page *Metropolis on Cayley graphs* currently says:

- define `mu(p)`, `0<p<1`, as the law of `X(T_p-1)`, where `T_p` has `Geometric(p)` distribution;
- take `mu(0)` to be uniform;
- let `tau(p)` be the relaxation time of the Metropolis chain based on the Cayley random walk with stationary law `mu(p)`;
- ask whether `tau(p)` is monotone decreasing in `p`;
- then ask whether `tau(p) <= C tau(infinity)` for a universal `C`, and for decreasing bounds in terms of `tau(infinity)`, `p`, number of states, and familiar graph parameters.

Direct fetch of `operations/claims/P0205.md` remains 404. The canonical P0205 history records an exact two-state refutation of the monotonicity clause, but no owner for the remaining clauses. Thus ownership is clear enough to screen P0205, but source precision/readiness is the issue.

This run does not simply repeat the word `ambiguous`; it isolates exactly what the likely intended `infinity` means and why that still does not authorize P13 to silently repair the source.

### 3.1 B18 — say it in another language: the geometric resolvent

Adopt the standard success-probability convention

`P(T_p=k)=p(1-p)^(k-1)`, `k>=1`.

If `P` is the transition matrix of the Cayley random walk and the walk starts at the identity `e`, then

`mu_p = p * sum_{k>=0} (1-p)^k delta_e P^k`.

This is the Abel/resolvent average of the random walk. On every finite irreducible Cayley graph, `P` is doubly stochastic and has uniform stationary distribution `pi`. The standard finite-state Abelian limit gives

`mu_p -> pi` as `p downarrow 0`,

even when the discrete walk is periodic. Thus the source's separate declaration `mu(0)=uniform` is mathematically coherent with this convention.

Now reparameterize by the expected number of performed walk steps

`s = E(T_p-1) = (1-p)/p`, so `p = 1/(s+1)`.

Then `p downarrow 0` is exactly `s -> infinity`. Therefore the only natural way found in this run to make the source's `tau(infinity)` coexist with its displayed `p in (0,1)` is to read `infinity` as **infinite geometric mean time**, i.e. the `p=0` Abel-limit chain.

This translation is mathematically clean, but it is not literally defined on the source page: the page writes `tau(p)` and never introduces `s` or a notation `tau(s)`. Hence it is evidence for an intended repair, not authority to rewrite the printed source.

### 3.2 B17 — look for your numbers somewhere else: the exact two-state ratio forces `C>=2` under that repair

Use the previously recovered two-element Cayley group with deterministic flip proposal. Under the same geometric convention,

`mu_p = (1/(2-p), (1-p)/(2-p))`.

The Metropolis transition matrix is

`M_p = [[p, 1-p], [1, 0]]`,

whose eigenvalues are `1` and `p-1`. Under the ordinary reversible spectral-gap convention `tau=1/(1-lambda_2)`, this gives

`tau(p)=1/(2-p)`.

It is strictly increasing, so it exactly refutes the source's monotone-decreasing question, as already recorded by the canonical attempt history.

The new admission diagnostic is the comparison-ratio consequence. If the intended `tau(infinity)` is the infinite-mean (`p=0`) Abel limit above, then

`tau(infinity)=tau(0)=1/2`,

and therefore

`tau(p)/tau(infinity) = 2/(2-p) -> 2` as `p up-arrow 1`.

Consequently any source-valid universal constant in the remaining comparison question must satisfy

`C >= 2`

under this most natural repaired convention. This is an exact lower-bound diagnostic, not a solution of the universal comparison problem and not a P13 source metric because P0205 has not crossed admission.

### 3.3 B22 — read the failures, not the successes: why the repair is still not source-safe

The failure modes are informative. The source simultaneously uses the probability-like parameter range `0<p<1`, separately defines `mu(0)`, and then invokes `tau(infinity)` without defining a second time parameter. The resolvent calculation above makes one intended interpretation highly plausible, but it does not eliminate all convention risk. In particular:

1. `Geometric(p)` conventions differ in the literature; the source page does not state its mass/tail convention.
2. `tau(infinity)` is not defined as `tau(0)` or as a limit after the `s=(1-p)/p` reparameterization.
3. For a periodic base Cayley walk, “relaxation time” can also depend on whether one uses the ordinary second eigenvalue, an absolute spectral gap, or a lazified/continuous-time convention. The exact two-state example makes that convention difference non-cosmetic at the endpoint.
4. The remaining final clause is open-ended (“some decreasing bound ...”), so even after repairing the comparator there is no single source-fixed denominator without choosing a sharper subquestion not literally printed by the author.

Therefore the source/readiness defect is now narrower but real: **P0205 is unclaimed, the monotonicity clause is already refuted, and the remaining clauses have a plausible mathematical interpretation, but the printed comparator/convention is not precise enough for P13 to freeze a source-faithful metric without silently editing the source.**

Disposition: **P0205 = UNCLAIMED / NOT READY / SOURCE-CONVENTION AMBIGUITY AFTER PARTIAL REFUTATION**. No canonical claim was created.

## 4. Why no alternative successor is admitted this invocation

The current queue and current canonical claims were reconciled against the fresh complete delta rather than trusting old queue labels. Higher-ranked CLOSABLE-shaped entries remain occupied or invalid in current state: I0004 is claimed/READY by P21; I0035 is reserved by C31; I0054 is R11; I0082 remains under R08 claim/history; I0095 is reserved to R02; I0105 remains a broad `PENDING_SCOPE` program rather than one frozen endpoint; I0121 and I0122 have ownership/retirement histories; I0124 has an R15 claim/handoff history. The coordinator's latest exact material-delta screen likewise finds no free READY CLOSABLE successor.

Several claims released since the preceding P13 report are genuinely unassigned, but their preserved source obligations are HARD OUTSIDE (weak even log-Brunn--Minkowski, heavy-tailed configuration-model MST universality, maximal-intersection ellipsoid uniqueness, and the relevant VDH release). The compact AK-Katzin equality clause is released because it is already exactly refuted as printed. Reclassifying any of those as CLOSABLE would violate the owner directive.

Accordingly there is no lawful create-only successor claim to acquire in this run. P13 remains `ADMISSION_PENDING`; successor metric and denominator remain `UNMEASURED`, not zero; successor unchanged/recovery counters remain `NOT_STARTED_PRE_ADMISSION`.

## 5. Method accounting

This run actually used three Section-B approaches, and the triple differs from P13's preceding B2/B23/B30 triple.

- **B17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE:** transported the exact two-state P0205 witness from the already-refuted monotonicity clause into the repaired comparison question, yielding the exact necessary lower bound `C>=2` under the natural infinite-mean interpretation.
- **B18 SAY IT IN ANOTHER LANGUAGE:** rewrote the geometric-time law as the Abel resolvent `p sum (1-p)^k P^k` and reparameterized by mean walk time `s=(1-p)/p`, showing precisely why an `infinity` comparator is mathematically natural even though it is not source-defined.
- **B22 READ THE FAILURES, NOT THE SUCCESSES:** used the notation/convention failure itself to identify why a seemingly obvious repair is still not sufficient for source-faithful admission and why the open-ended final clause cannot supply a frozen denominator.

The exact two-state arithmetic is elementary and fully displayed above; no finite computational claim requiring a checker was introduced. No checker/file churn is counted as movement.

## 6. Structured ledger delta for P26

```yaml
ledger_delta:
  task_id: P13
  native_slot: 6aa7b253b37c8191b693d8dc79298d37
  category: CLOSABLE_OUTSIDE
  status: ADMISSION_PENDING
  retired_predecessor: I0051
  terminal_handoff_preserved: P0342
  p0342_metric: 2/2
  successor_source_id: NONE
  successor_claim_id: NONE
  successor_metric_before: UNMEASURED
  successor_metric_after: UNMEASURED
  successor_denominator: UNFROZEN_PRE_ADMISSION
  mathematical_movement: false
  screening_movement:
    - I0054 current owner R11 confirmed; newest internal class count 77->78; source PARTIAL
    - P0205 comparator ambiguity narrowed by exact Abel-resolvent / mean-time reparameterization
    - under the natural repaired P0205 comparator, exact Z2 witness forces universal C >= 2
  methods_tried: [17, 18, 22]
  previous_p13_method_triple: [2, 23, 30]
  successor_unchanged_runs: NOT_STARTED_PRE_ADMISSION
  successor_recovery_count: NOT_STARTED_PRE_ADMISSION
  i0054:
    disposition: OWNED_R11_SKIP
    canonical_claim: operations/claims/I0054.md
    newest_peer_metric: 78
    source_status: PARTIAL_NOT_CLOSED
  p0205:
    ownership: UNCLAIMED_VISIBLE_SCOPE
    monotonicity_clause: PRIOR_EXACT_REFUTATION_PRESERVED
    remaining_readiness: NOT_READY_SOURCE_CONVENTION_AMBIGUITY
    exact_diagnostic: C_GE_2_UNDER_NATURAL_INFINITE_MEAN_REPAIR
    claim_created: false
  fresh_prewrite_master: 664979ca169443dad543a50691850f62183ca258
  predecessor_report_commit: abf8ac4b35bf81caffafb747f7064adcc37d8ac0
  commits_ahead_at_prewrite: 135
  commits_behind_at_prewrite: 0
  compare_too_large: null
  audit_partner_primary: P26
  audit_partner_secondary: P14
  closure_claimed: false
```

## 7. Delivery / safety accounting

This invocation writes only this new immutable P13 report under the existing own root. It does not modify a canonical claim, shared root ledger, peer report, historical report, schedule, workflow, permission, email/Gmail resource, Drive resource, paid-compute resource, public posting, credential, or external contact. No force push is used. The scheduler/model request remains prompt-only: the exposed controls provide no binding GPT-6 selector, no binding maximum-reasoning selector, and no authenticated run-level effort receipt, so the report states the actual visible model and marks reasoning telemetry UNVERIFIED.

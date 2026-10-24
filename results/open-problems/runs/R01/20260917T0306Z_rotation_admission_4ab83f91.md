Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum was requested, but the exposed runtime/task surface still provides no authenticated model selector or reasoning-effort selector, so I do not claim otherwise. **Retired I0024 metric remains C=1 and INTERNAL-CLOSED; retired I0113 metric remains M3=3/3 with unchanged count frozen at 6. No successor metric is started because no screened candidate is simultaneously READY + unassigned + CLOSABLE OUTSIDE. Section-B methods used: #21 ASK WHO ELSE HAS THIS SHAPE, #23 DO WHAT THE PROPOSER DID NOT EXPECT, #30 ONE SCALE / ONE DIRECTION AT A TIME.**

# R01 post-closure successor admission — I0045 scope changed by later PA local-limit work; DC35/BIS32 are source-clean but HARD, so no unlawful claim

Repository / branch: `yspennstate/math-open-problems` / `master`.
Dated source/status checks: 2026-09-17 UTC.

## 1. Continuity: I0024 stays closed and I0113 stays rotated

I continued from `runs/R01/20260917T0202Z_7c91e4b2.md`; I did not reopen either retired research target.

Preserved I0024 state:

- source: David Aldous and James Fill, *Reversible Markov Chains and Random Walks on Graphs*, Open Problem 3.44;
- source question still live on the current Aldous--Fill page: does relaxation time admit a characterization exactly as an infimum over flows?;
- proved candidate:
  \[
  \tau_2=\inf_{R:\,BR=I_{\mathcal H_0}}\sup_{0\ne b\in\mathcal H_0}
  \frac{(Rb)^T C^{-1}(Rb)}{b^T\Pi^{-1}b},
  \qquad R_*=CB^TL^+;
  \]
- fixed metric: `C=1`, the theoretical optimum;
- exact finite checks and the scalar-candidate counterexamples are preserved in `paper_af344_exact_flow_characterization/`;
- distinct other-track audits: `R20-AUDIT-R01-I0024-03 = PASS` and `P26-AUDIT-R01-I0024-AF344-SINGULAR-RIGHT-INVERSE-10 = PASS`;
- mathematical/source-question status: `PROVED / INTERNAL-CLOSED`; broad publication novelty of the Moore--Penrose/right-inverse mechanism remains deliberately unclaimed.

Fresh source check on 2026-09-17 found that Aldous--Fill Chapter 3 still prints Open Problem 3.44 and Chapter 4 still contrasts it with the non-exact distinguished-path upper bound. A bounded current search for `exact inf over flows`, `relaxation time right inverse`, and neighboring flow/spectral-gap language did not locate a later primary paper explicitly superseding the source-level classification. This negative search is not a novelty certificate.

Preserved I0113 state:

- source: Justin Salez, Problem 2.7, cutoff under weak dependencies;
- frozen source metric `M3=3/3` was unchanged for six consecutive active runs;
- the all-three perturbative cutoff theorem, anisotropic `log n sum_i delta_i^2 -> 0` condition, bounded-block extension, Gibbs gradient estimate, exact Gamma_2/Schur reduction and finite exact counterexamples/evidence remain preserved;
- status: `PARTIAL / PROVED-CANDIDATE / ROTATED`.

No seventh I0113 research run is produced.

## 2. Required repository recovery

Before successor screening I recovered/read the current campaign and operational surfaces including:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`;
- current create-only ownership under `operations/claims/`;
- newest R01 report and current R02 evidence surfaced by repository search;
- targeted intake hits for the candidates touched below.

The intake JSONL corpus is too large to render row-for-row through the connector in one invocation. I used exact-ID/source/ownership searches for the candidates actually screened and do not falsely claim a byte-for-byte visible reread of all approximately 780 intake rows.

The current follow-up implementation manifest still says PENDING candidates may not be promoted to READY automatically and records the lack of model/reasoning task selectors. Those constraints remain binding.

## 3. Method #21 — ASK WHO ELSE HAS THIS SHAPE: I0045 is no longer a clean untouched self-loop local-limit target

Candidate: `I0045`, the van der Hofstad preferential-attachment local-weak-limit/self-loop row. `operations/claims/I0045.md` was absent immediately before this screen, so ownership itself would not block admission.

The source-side mathematical gap can be recovered from van der Hofstad's preferential-attachment chapter: Theorem 5.7 proves local weak convergence to the Polya-point tree for the fixed-edge/no-self-loop variant and then explicitly says that theorem does **not** include the case where self-loops are allowed, while expressing the belief that a similar result should hold for `PA(m,delta)`.

Later primary work materially changes that status. Tiffany Y. Y. Lo, *Local weak limit of preferential attachment random trees with additive fitness*, Advances in Applied Probability 56 (2024), proves a local weak limit for PA trees with i.i.d. positive bounded additive fitness. More importantly for this queue row, the published discussion states that with straightforward modifications the same Polya-point-tree description also applies to PA trees **with self-loops** when the fitness is bounded, and explains the `m>=2` outgoing-edge variation; it cites earlier work for the non-random unit-fitness case.

This does not justify calling the full historical van-der-Hofstad source clause globally KNOWN without checking exact model equivalence across every `m>=1` and `delta>-m`, especially the negative-attractiveness range and the precise collapsing/self-loop convention. It does show that the stale queue shorthand `self-loops/local weak limits; exact recurrence route` is no longer a clean untouched CLOSABLE target.

**Admission verdict:** `I0045 = HOLD_CURRENT_STATUS_SCOPE / SUBSTANTIALLY_PARTIALLY_RESOLVED`. A future claim would have to freeze the exact residual `(m,delta)` regime not covered by the later local-limit literature and show that this residual is still author/source-open. I do not create a claim.

## 4. Method #23 — DO WHAT THE PROPOSER DID NOT EXPECT: RS-2026-DC35 is source-clean but cannot honestly be turned into a one-subcase CLOSABLE theorem

Candidate: `RS-2026-DC35`, Chiara Meroni, Randomstrasse 101, Open Problem 35, posted 23 February 2026 and updated 5 June 2026. `operations/claims/RS-2026-DC35.md` was absent immediately before this screen.

The live source asks:

> Determine under which conditions on a cone D subset R^d the D-convex hull of finitely many points is semialgebraic.

The same source records positive special cases and explicitly separates this characterization problem from Conjecture 34, the existence of a non-semialgebraic finite-set D-convex hull. The natural contrary move would be to freeze one low-dimensional cone class and prove either semialgebraicity or failure.

That would be mathematically useful, but it would only be a **PARTIAL** result for Open Problem 35; a non-semialgebraic example would principally advance the separately owned Conjecture 34. There is no source-stable scalar metric for one low-dimensional subcase that turns the broad characterization into a CLOSABLE source answer without changing its quantifiers.

Fresh current search found no later primary paper claiming a general characterization after the February/June 2026 source post. Meroni--Raita (2025) remains one of the positive special-case inputs cited by the source, not a resolution.

**Admission verdict:** `RS-2026-DC35 = OPEN_BROAD / HARD_NOT_CLOSABLE_FOR_R01`. No claim is created.

## 5. Method #30 — ONE DIRECTION AT A TIME: RS-2026-BIS32 is genuinely open-looking but belongs in HARD, not this CLOSABLE slot

Candidate: `RS-2026-BIS32`, Afonso Bandeira's Randomstrasse 101 Conjecture 32 (16 February 2026), the Zdeborova--Boettcher min/max-bisection identity. `operations/claims/RS-2026-BIS32.md` was absent immediately before this screen.

The exact live source asks, for each fixed `d>=3` and even `n`,
\[
\frac1n\mathbb E\,\mathrm{MinBis}(G_d)
+
\frac1n\mathbb E\,\mathrm{MaxBis}(G_d)
=\frac d2+o(1).
\]

The source itself records only the large-degree asymptotic result of Dembo--Montanari--Sen. Current literature checks show substantial but nonclosing progress: large-degree/local-algorithm work remains asymptotic in `d`, and the 2025 Gheissari--Perkins--Yap fixed-magnetization Ising paper proves a **positive-temperature** Zdeborova--Boettcher relation up to the reconstruction threshold, not the zero-temperature fixed-`d` extremal-bisection conjecture above. I found no 2025--2026 primary source resolving Conjecture 32 for every fixed `d>=3`.

This makes it a legitimate open-looking outside target, but not a plausible CLOSABLE successor: the frozen source metric would have to control a fixed-degree `n -> infinity` spin-glass/extremal-graph asymptotic, and finite exact computation cannot close that obligation. Treating `d=3` or another single degree as the full source target would change the quantifier and at best produce a PARTIAL theorem.

**Admission verdict:** `RS-2026-BIS32 = OPEN / HARD_OUTSIDE / NOT_R01_CLOSABLE`. No claim is created.

## 6. Successor gate after this run

The current bounded screen adds three useful exclusions/classifications without stealing work:

- `I0045`: unclaimed but no longer a clean untouched source target; later PA local-limit literature covers important self-loop regimes, exact residual source scope must be frozen first;
- `RS-2026-DC35`: unclaimed and source-current, but broad characterization/HARD; a one-cone theorem is only PARTIAL and DC34 is separate;
- `RS-2026-BIS32`: unclaimed and open-looking, but a fixed-degree zero-temperature asymptotic/HARD target, not CLOSABLE.

Together with the already-recovered current screens/ownership constraints (`I0006` HOLD_SOURCE, `I0011` owned, `I0028` owned/HARD, `I0035` owned, `I0054` owned, `I0055` literature-resolved, `I0074` source-scope hold, `I0105/I0106` not CLOSABLE-ready, and current Randomstrasse ownership), I still do not have a candidate satisfying all mandatory dispatch gates:

1. exact outside source;
2. current primary-literature status checked;
3. no existing owner;
4. genuinely CLOSABLE with a stable source metric.

Therefore **R01 remains `ROTATION_WAIT / SUCCESSOR_ADMISSION_REQUIRED`**. This is not permission to reopen I0024 or I0113, promote a PENDING row, steal a HARD assignment, or manufacture a partial subcase as a full source claim.

## 7. Directed R01 -> R02 audit duty

The newest complete R02 package surfaced by the repository search is still the earlier I0095 `17 x 17` discrepancy witness era. R01 already independently checked that finite certificate under `R01-AUDIT-R02-I0095-A17-04 = PASS_FINITE_METRIC_CLAIM`. I did not find a newer complete theorem/closure package that would justify burning the audit budget again. No duplicate audit or invented verdict is created.

## 8. Model/reasoning selector and protected-task status

The implementation limit is unchanged and is supported by `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`:

- exposed task controls do not provide a model selector or reasoning-effort selector;
- GPT-6 / maximum is therefore a prompt request, not an authenticated setting;
- no guaranteed hour-long execution control is exposed;
- the historical P26 update attempt returned `You cannot modify this task`, while other authorized contexts later succeeded on their own task sets.

Actually forcing and verifying GPT-6/maximum would require a product/owner scheduler surface exposing explicit model and reasoning fields plus completed-run telemetry, or platform support/ownership migration. The legitimate workaround for an unmodifiable task is the owning authorized context, explicit permission transfer/change, or platform support — not duplication or bypass. No scheduler modification is attempted here.

## 9. Structured ledger_delta

```yaml
ledger_delta:
  track: R01
  run_id: 20260917T0306Z_rotation_admission_4ab83f91
  I0024:
    source: "Aldous-Fill Open Problem 3.44"
    metric: "uniform multiplicative distortion C"
    before: 1
    after: 1
    unchanged_count: "retired/closed"
    status: PROVED_INTERNAL_CLOSED
    audits:
      - R20-AUDIT-R01-I0024-03
      - P26-AUDIT-R01-I0024-AF344-SINGULAR-RIGHT-INVERSE-10
  I0113:
    source: "Salez Problem 2.7"
    metric: "M3 all-three source implementations covered"
    before: "3/3"
    after: "3/3"
    unchanged_count: 6
    status: PARTIAL_PROVED_CANDIDATE_ROTATED
  methods_this_run: [21, 23, 30]
  successor_screen:
    I0045:
      ownership: UNCLAIMED_AT_SCREEN
      status: HOLD_CURRENT_STATUS_SCOPE_SUBSTANTIALLY_PARTIALLY_RESOLVED
      claim_created: false
      reason: "later local-weak-limit literature explicitly covers bounded-fitness self-loop PA regimes; exact residual source model/range must be frozen"
    RS-2026-DC35:
      ownership: UNCLAIMED_AT_SCREEN
      status: OPEN_BROAD_HARD_NOT_CLOSABLE
      claim_created: false
      reason: "full cone characterization is broad; one low-dimensional cone is only PARTIAL and non-semialgebraic example overlaps distinct DC34"
    RS-2026-BIS32:
      ownership: UNCLAIMED_AT_SCREEN
      status: OPEN_HARD_OUTSIDE_NOT_R01_CLOSABLE
      claim_created: false
      reason: "fixed-d zero-temperature n->infinity extremal-bisection conjecture remains hard; current positive-temperature/large-d results do not close source"
  successor_metric: UNMEASURED
  overall: ROTATION_WAIT_SUCCESSOR_ADMISSION_REQUIRED
  R02_audit:
    trigger: NOT_TRIGGERED
    reason: "no newer complete R02 theorem/closure package recovered; earlier I0095 finite metric already audited"
    new_audit_ids: []
```

No new finite mathematical claim is made, so no decorative checker or artifact is created. No Gmail/email, Drive, public posting, purchase, permission change, shared-root edit, peer-track edit, workflow execution, force-push, or scheduler change was performed.
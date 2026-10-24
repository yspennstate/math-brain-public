Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO MOVEMENT: frozen metric `S_exact = UNBOUNDED -> UNBOUNDED`. Section-B methods actually tried, transparently reused as audit lenses because the prior immutable P0457 history has already exhausted all thirty methods: #20 FIND WHY THE ALGORITHM FAILS, #22 READ THE FAILURES NOT THE SUCCESSES, #27 SWAP THE QUANTIFIERS.**

# NM13-04 / P0457 — closure-critical source-theorem audit, no new certificate

Run date: 2026-09-18 UTC  
Repository / branch: `yspennstate/math-open-problems` / `master`  
Track / namespace: `proofnet24/NM13-04/`  
Category: `CLOSABLE OUTSIDE`  
Canonical source/claim: `P0457`, `operations/claims/P0457.md`  
Status after this invocation: **PROVED-CANDIDATE / AUDIT-PENDING**, not repository-closed  
Frozen metric: **`S_exact = UNBOUNDED`**  
Unchanged-run counter: **1 -> 2** since the last metric movement  
Stuck recoveries used: **1 -> 1**  
Required independent audits: **P26 = NOT PASSED; NM13-05 = NOT PASSED**

## 1. Runtime and control-plane disclosure

The prompt requests GPT-6 with maximum reasoning. This invocation actually identifies as **GPT-5.6 Sol**. Authenticated reasoning-effort telemetry is not exposed, so the reasoning level is **UNVERIFIED**. I do not claim GPT-6, a binding maximum-reasoning setting, an hour-long execution, or a support escalation.

The task-control surface exposed here offers title/prompt, schedule or relative-start fields, timing mode, enabled state, and task identifiers, but no bindable model-family selector and no bindable reasoning-effort selector. Thus `GPT-6 / maximum` remains prompt text only. Making it enforceable would require an owner-authorized product/workspace/API/admin surface that exposes persistent model/reasoning controls and authenticated per-run runtime attestation.

The historical P26 response `You cannot modify this task` remains an authorization-context boundary. A legitimate workaround is to use the task-owning or otherwise authorized account/workspace/product/admin/API surface, or platform support. It is not permission to clone the task or bypass access controls. No task or schedule was modified in this invocation.

## 2. Authoritative continuity and required repository read

I continued the already admitted P0457 target. Intake was not reopened and no second claim was created.

Canonical identity remains:

- source: Hossein Dabirian and Vijay Subramanian, *Connectivity of a family of bilateral preference random graphs*, Journal of Applied Probability 63(2) (2026), 552–579, DOI `10.1017/jpr.2025.10051`;
- canonical dedup key: `diameter_near_the_newly_established_bilateral_connectivity_threshold`;
- SHA-256: `839d9617dd11661f03c25aa6c4d2e47c012b337f35570dde06ca7695f66ff561`;
- shard residue: `3 mod 13`, matching NM13-04;
- exclusive owner: NM13-04;
- frozen source model: exact bilateral-preference `LK(n,k)`, not an independent-edge surrogate.

Before deciding what to do, I reread or targeted-recovered current `master` state for:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- canonical claim `operations/claims/P0457.md`;
- current P0457 search/history and the relevant source/attempt surfaces;
- newest own report `proofnet24/NM13-04/runs/2026-09-18/2026-09-18T07-25-00Z__p0457-disconnected-shell-correction.md`;
- newest visible neighboring NM13-03 and NM13-05 run state;
- current P26 audit-run state and exact repository searches for a P0457 audit pass.

The newest own report is controlling continuity. It corrected the auxiliary all-`s` deterministic shell theorem by exhibiting the exact disconnected witness `n=4,s=2,k=1` and replacing the overbroad finite-distance clause with a componentwise statement. That correction did **not** invalidate the independent near-logarithmic source theorem. It also explicitly directed the next invocation to check for a real P26/NM13-05 audit or source/literature correction first, rather than manufacture another co-degree certificate.

Current exact searches recover **no P0457 audit PASS from P26** and **no P0457 audit PASS from NM13-05**. NM13-05's newest visible work is successor-admission screening after handing off D0004, not an audit of P0457. P26's newest visible audit activity concerns another source. No owner-authorized P0457 release, competing owner, handoff, POSTED settlement, or source-specific correction was recovered.

The latest P0457-related commit visible before this write remains NM13-04's own disconnected-shell correction commit `14683c2fbeaf4e28162a4a88b6e34af7b1204eb0`; no later P0457 commit from another track appears in current commit search.

Large aggregate ledgers and directory listings can be connector-truncated. Exact paths, exact IDs, canonical claims, immutable reports, and targeted searches are the continuity anchors. I do not interpret truncation or inaccessible history as absence.

## 3. Fresh source and bounded literature status — 2026-09-18

The current Cambridge primary source still states in Section 1.1 that, after its improved connectivity theorem, **another open problem is characterizing the diameter for the additional range of `k(n)` from Theorem 6 where connectivity holds**. The same source states Theorem 6 with connected side

`k >= log n + t' sqrt(log n) log log n`, for fixed `t' > 1/2`.

I checked the rendered primary PDF, including the Open Problems page, rather than relying on an abstract alone.

The nearest older same-model result remains Richard J. La and Maya Kabkab, *A New Random Graph Model with Self-Optimizing Nodes: Connectivity and Diameter*, Internet Mathematics 11 (2015), DOI `10.1080/15427951.2015.1022626`. Its published abstract records the stronger embedded-connected-ER condition `k > beta_* log n`, `beta_* ~= 2.4626`, under which the old diameter mechanism applies.

Fresh bounded queries on 2026-09-18 used the exact 2026 title plus `diameter`, the author names plus `bilateral preference diameter`, `LK(n,k) diameter`, the DOI, and the 2015 predecessor title. They recovered the primary 2026 paper, the 2015 predecessor, and adjacent random-graph material, but no later source-matching resolution. This is **bounded negative evidence only**, not a proof of worldwide openness and not a publication-novelty certificate.

## 4. Frozen metric and why it does not move

The canonical metric is

`S_exact = largest co-degree s >= 0 for which NM13-04 has a complete deterministic diameter classification for LK(n,n-1-s), uniformly over the stated feasible n.`

The all-`s` componentwise classification already saturated this metric at `UNBOUNDED`. The previous run corrected wording without changing the saturation. This invocation does not redefine the metric to make audit work look like numerical progress.

- before: `S_exact = UNBOUNDED`;
- after: `S_exact = UNBOUNDED`;
- movement: **none**;
- consecutive unchanged invocations since saturation: **1 -> 2**;
- stuck-recovery episodes: **1 -> 1**;
- six-unchanged CLOSABLE rotation gate: not yet reached.

No finite certificate was created merely to decorate an already saturated metric.

## 5. Source theorem under audit

The source-level candidate proved earlier on this track is:

> Fix constants `t0 > 1/2` and `T > 1`. For any integer sequence `k=k(n)` satisfying, for all sufficiently large `n`,
>
> `log n + t0 sqrt(log n) log log n <= k <= T log n`,
>
> one has
>
> `D(LK(n,k)) / (log n / log log n) -> 1`
>
> in probability.

For the genuinely new source interval, one may take fixed `T` beyond the La–Kabkab threshold constant `beta_* ~= 2.4626`; the old same-model theorem handles the regime above that threshold. The earlier P0457 proof uses two independent proof layers for the hard upper-bound step: the original leave-one-out core-attachment derivation and a later two-round capacity/sprinkling derivation.

This invocation did not try to produce a third proof. It stress-tested the closure-critical logical joints.

## 6. Method #20 — FIND WHY THE ALGORITHM FAILS

I treated the two-round capacity proof as an algorithm whose failure modes must be explicit.

The key construction is: delete the two endpoint blocks, expose an internal threshold core `C_ij`, define capacity-good targets by an internal `q`-exceedance budget, then expose boundary edges. A target `w` is safe for endpoint `v` when `V_vw>q` and the remaining boundary exceedance count stays within its reserved capacity. The proof then defines

`Z_v = number of q-high incident edges of v that are not safe targets`.

The deterministic forcing implication is

`A_v != empty and Z_v < k  =>  v proposes a safe edge`,

where `A_v` is the safe-target set. If `v` has at most `k` q-high edges, it proposes all of them; if it has more than `k`, failure to propose any safe edge would force all of its top `k` edges to be unsafe and hence `Z_v >= k`.

I rechecked the two places where hidden dependence could break this mechanism:

1. **target-side proposal:** after internal `W_ij` edges are exposed, the variables `Y_w^(-v)` for distinct `w` use disjoint boundary-edge bundles, and `V_vw` is independent of those bundles; the safe-target Bernoulli lower bound is therefore conditional on the correct sigma-field;
2. **endpoint-side proposal:** the argument does not assume endpoint `v` itself has fewer than `k` q-high edges; `Z_v<k` is exactly what handles the overfull case.

I also rechecked the apparent core-diameter uniformity issue. The upper bound does **not** require a fresh diameter theorem simultaneously for all `C_ij`: each `C_ij` is connected by definite `G_+` edges, so the two attachment targets lie in the same component of the single global threshold graph `G_+`; their distance is bounded by the global maximum finite-component diameter already controlled by the classical sparse-ER diameter theorem. Thus no unjustified polylogarithmic union of bare `o_P(1)` diameter statements is needed at this step.

**Outcome #20:** no mathematical failure found in the closure-critical attachment/path mechanism. This is a self-audit, not an independent audit PASS.

## 7. Method #27 — SWAP THE QUANTIFIERS

I audited whether the earlier proof silently proves only “for each fixed `k`” while the stated theorem quantifies over arbitrary sequences `k(n)` in the near-logarithmic band.

The relevant estimates are uniform once `t0>1/2` and `T>1` are fixed:

- the global kth-order-statistic sandwich uses only `k >= log n` and `k <= T log n`;
- `delta = (t0/8) sqrt(log n) log log n / k` obeys the required smallness and gives `delta k = (t0/8) sqrt(log n) log log n` exactly at the scale needed for the boundary margin;
- `delta^2 k >= c_{t0,T}(log log n)^2`, uniformly over the band;
- the final attachment exponent retains a positive source-scale reserve proportional to `t0 sqrt(log n) log log n`;
- all constants in the block and Chernoff bounds may be chosen from fixed `t0,T`, not from a particular subsequence.

Therefore the proof supports the sequence-wise quantifier written in the theorem rather than only pointwise-in-parameter convergence. For the source's **additional** diameter range, taking a fixed `T > beta_*` covers the previously unresolved logarithmic band; no claim is needed that the new proof controls arbitrary super-logarithmic `k` outside the old source gap.

**Outcome #27:** the quantifier audit survives. No scope expansion is claimed beyond the source-relevant band.

## 8. Method #22 — READ THE FAILURES, NOT THE SUCCESSES

The source itself explains why its connectivity proof becomes delicate near threshold: the simpler ER-style sufficient conditions no longer characterize the dependent LK graph sharply enough. The 2015 predecessor's diameter route similarly relies on a **connected** embedded ER subgraph and therefore stops at the stronger constant `beta_* ~= 2.4626`.

The P0457 route was designed around that exact failure: the definite lower threshold graph is allowed to be disconnected and to have many isolated vertices. Only its giant/core component is used for long travel, and every source vertex is attached to the appropriate core through bilateral-preference edges by a separate leave-one-out or two-round capacity argument. The lower bound comes from the opposite threshold inclusion.

The fresh literature check found no later paper that already supplies this missing near-threshold transfer. Again, this does not certify novelty worldwide.

**Outcome #22:** the failure mechanism in the predecessor is still the right obstruction, and the P0457 construction addresses that obstruction rather than assuming it away.

## 9. Method-accounting exception is explicit

The owner directive normally asks for three Section-B methods not previously tried on the problem. The immutable P0457 history already records that **all thirty methods have been used**. It is therefore impossible to satisfy the “previously untried” clause literally without inventing history.

I did not do that. I reused #20/#22/#27 as **audit lenses**, a different triple from the immediately preceding report (#2/#19/#29), and stated the reuse in the first line. The outcomes above are genuine work performed this invocation, but they are not represented as first-time methods.

## 10. Closure state and next step

P0457 remains **PROVED-CANDIDATE / AUDIT-PENDING**, not `PROVED` or repository-closed.

Closure prerequisites currently stand as follows:

- full source-target argument on page: **candidate present**;
- finite-core exact certificate: **not applicable to the analytic near-logarithmic theorem itself**; exact certificates exist for the auxiliary finite deterministic claims and the latest disconnected-shell correction;
- prior-art/source search: **recorded but bounded; novelty unverified**;
- independent audit by P26: **NOT PASSED**;
- independent audit by NM13-05: **NOT PASSED**.

Accordingly, the next invocation should again check for a real P26 or NM13-05 audit or a source/literature correction **before** doing new mathematics. If an external audit identifies a concrete gap, repair exactly that obligation. If both independent audits pass, proceed to the owner closure/paper-package protocol. If neither exists, do not generate another finite certificate or co-degree lemma merely to fill the run; the metric is already saturated and the source theorem has already been independently derived within the same track by two internal routes.

No audit is presumed to pass because it was designated in advance.

## 11. Structured `ledger_delta` for P26

```yaml
ledger_delta:
  track: NM13-04
  category: CLOSABLE_OUTSIDE
  status: PROVED_CANDIDATE_AUDIT_PENDING
  source_id: P0457
  claim_id: operations/claims/P0457.md
  dedup_key: diameter_near_the_newly_established_bilateral_connectivity_threshold
  selection_residue: 3
  metric:
    name: S_exact
    before: UNBOUNDED
    after: UNBOUNDED
    normalization_changed: false
  mathematical_movement: false
  section_B_methods:
    attempted_this_run: [20, 22, 27]
    all_previously_used_on_P0457: true
    reuse_disclosed: true
    immediately_previous_triple: [2, 19, 29]
    outcomes:
      20: "closure-critical two-round attachment/path mechanism re-audited; no failure found"
      22: "predecessor/source failure mechanism rechecked against current literature; no source-matching resolution recovered"
      27: "uniform sequence-k quantifiers in the fixed logarithmic band re-audited; no scope defect found"
  counters:
    unchanged_runs_before: 1
    unchanged_runs_after: 2
    stuck_recoveries_before: 1
    stuck_recoveries_after: 1
    closable_rotation_threshold: 6
  audits:
    P26: NOT_PASSED
    NM13-05: NOT_PASSED
  literature_check:
    date: 2026-09-18
    source_primary: "Dabirian-Subramanian, J. Appl. Probab. 63(2), DOI 10.1017/jpr.2025.10051"
    source_open_problem_still_present: true
    predecessor: "La-Kabkab, Internet Mathematics 11 (2015), DOI 10.1080/15427951.2015.1022626"
    later_source_matching_resolution_found: false
    scope_note: "bounded web/primary-source search; not proof of worldwide openness or novelty"
  artifacts_created: []
  claim_created_or_modified: false
  shared_root_edits: NONE
  peer_edits: NONE
  next_step: "Check P26/NM13-05 audit and source/literature correction first; repair only a concrete external-audit defect; if both audits pass, enter closure/paper-package protocol; otherwise do not manufacture filler certificates."
```

No email/Gmail, Drive, public posting, paid compute, permission change, workflow execution, external unreviewed script, peer-track edit, shared-root edit, or scheduler creation/modification was performed.

**End of immutable run report.**
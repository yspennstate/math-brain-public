Model actually ran: **GPT-5.6 Sol. Reasoning: UNVERIFIED by authenticated runtime metadata; GPT-6 / maximum was requested but is not verified. Frozen I0030 metric remains retired at `N_certified=22`; no successor metric is started. Section-B methods used: #17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE, #22 READ THE FAILURES / LATER LITERATURE, #30 ONE SCALE / ONE DIRECTION AT A TIME.**

# R05 — post-I0030 closure successor-admission gate

Repository/branch: `yspennstate/math-open-problems`, `master`.

## 1. Continuity: AF7.30 / I0030 stays closed; do not manufacture order-23 work

I continued from `runs/R05/20260917T051753Z_i0030_n22_closure.md` and did not restart or enlarge the frozen Aldous–Fill target.

The original source was rechecked on 17 September 2026. Aldous–Fill Proposition 7.29(ii) states, for continuous-time random walk on a distance-regular graph, that `q(t,d)/q(t,0)` is nondecreasing in `t` for fixed distance. Open Problem 7.30 still asks whether random walk on an arc-transitive graph has some monotonicity stronger than Corollary 7.3.

The frozen R05 theorem remains:

> For every finite simple connected arc-transitive `d`-regular graph, with `P=A/d`, `H_t=exp(t(P-I))`, and every arc `x~y`, the ratio `H_t(x,y)/H_t(x,x)` is strictly increasing for finite `t>=0`, from `0` to `1`.

The proof package is already complete: edge homogeneity gives `a'=b-a`, exponential spectral tilting gives `r'(t)=Var_{nu_t}(lambda)>0`, and the source-responsive theorem has two distinct OTHER-track full-proof audits:

- `R04-AUDIT-R05-I0030-C1-20260916T130900Z = PASS_MATH / NOVELTY_UNVERIFIED`;
- `P26-AUDIT-R05-I0030-C1-1WALK-REGULAR-13 = PASS_FULL_MATHEMATICAL_PROOF / SOURCE_RESPONSIVE_PASS / FINITE_CERT_REEXECUTED / PRIOR_ART_UNVERIFIED / SOURCE_CLOSURE_INTERPRETIVE`.

The source-matching package `paper_af730_adjacent_monotonicity/` exists. The mathematical/source-response campaign status is therefore unchanged:

`SOURCE_RESPONSIVE_POSITIVE_ANSWER / CAMPAIGN_CLOSURE_COMPLETE / PUBLICATION_NOVELTY_UNVERIFIED`.

The finite metric is frozen at `N_certified=22`. Extending Conder's census to order 23 would violate the post-closure rotation instruction and add no source obligation.

## 2. Required repository recovery

Before successor screening I reread/recovered the current campaign and operational surfaces:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`;
- the newest cumulative CLOSABLE screen `operations/task_health/runs/2026-09-17T034510Z/queue_screening.md`;
- the newest R05 closure report and recent R01/R06/R09/P16 successor screens;
- current create-only claim files for the historical READY rows.

The large intake JSONLs cannot be rendered byte-for-byte in one connector response. I used targeted exact-ID/source/ownership retrieval for the candidates actually screened and do not claim otherwise.

The stale admission snapshot had marked I0066 and I0028 READY, but current master has canonical claims for both: I0066 belongs to P15 and I0028 belongs to the former HARD10-01 slot. They are not available to R05. Current screens also exclude or occupy I0035, I0054, I0055, I0068, I0070, I0077, I0078, I0079, I0082, I0087, I0095, I0110, I0112, I0113, I0004, I0043, I0073, and the active complete-mixability successors. I did not overwrite or duplicate any claim.

All thirty Section-B methods had already been used by R05 before closure. The present #17/#22/#30 are second-cycle uses and are not the preceding run's #2/#14/#24 triple.

## 3. #17/#22 — advance the reserve cursor through old preferential-attachment rows rather than recycle stale OPEN labels

### I0047 — first-passage percolation on preferential attachment

The queue shorthand is the old van der Hofstad Saint-Flour Open Problem 3.8, asking for first-passage asymptotics on preferential-attachment graphs. Current same-author material no longer supports treating the historical row as an untouched small CLOSABLE target: the modern text explicitly notes that first-passage results have been obtained in the scale-free regime and flags incorporation of those results into the text. Existing PA/FPP literature also treats substantial parameter regimes.

That does not prove every historical clause is globally resolved. It does show that dispatch now requires reconstructing the exact residual weight/degree regime and checking it against the later FPP papers. No stable source-wide finite metric is available from the stale intake row.

Disposition: `I0047 = PARTIALLY_RESOLVED_OR_SCOPE_RECONCILIATION_REQUIRED / NOT_READY_CLOSABLE`.

No claim is created.

### I0048 — percolation transition on preferential attachment

This row is materially overtaken by primary literature. Hazra, van der Hofstad and Ray, *Percolation on preferential attachment models*, arXiv:2312.14085, identify the critical percolation threshold for affine PA with `m` edges and parameter `delta`:

- for `delta>0`, an explicit positive threshold;
- for `delta<=0`, threshold `0`.

Their proof also equates the graph threshold with that of the Pólya-point-tree local limit. This directly answers the main threshold question that the old queue shorthand presents as an open percolation-transition problem. Any residual comparison with a particular independent-edge variant would need to be recovered clause-by-clause from the historical source before admission.

Disposition: `I0048 = MAIN_THRESHOLD_RESOLVED / EXACT_RESIDUAL_SCOPE_REQUIRED / NOT_READY_CLOSABLE`.

No claim is created.

### I0049 — critical window for uniformly grown graphs

I did not duplicate P16's fresh source check. The current fleet record already identifies the old critical-value/window problem as resolved in its intake scope: critical value `1/4` in the current van der Hofstad text and critical window of order `(log n)^(-2)` in Jorritsma–Maillard–Mörters (arXiv:2512.18937).

Disposition remains `KNOWN / DO_NOT_DISPATCH`.

## 4. #30 — one clause at a time: I0050 is also not a clean new CLOSABLE source

The next queue row, I0050, concerns annealed configuration-model limits, pressure and critical values. The later primary paper Can–Giardinà–Giberti–van der Hofstad, *Annealed Ising model on configuration models* (arXiv:1904.03664; Ann. Inst. H. Poincaré Probab. Statist. 58 (2022), 134–163), already proves variational expressions for the annealed pressure and identifies annealed critical values for deterministic degree sequences and for i.i.d. degrees. Follow-up work on annealed inhomogeneities further develops the critical behavior.

Because the historical queue row bundles several clauses, I do not overstate this as global resolution without reconstructing the exact old Open Problem 5.3 wording. But it is not an untouched source-exact CLOSABLE target. A lawful successor would need an exact residual clause demonstrably not covered by the 2021/2022 results, plus a stable source-matching metric.

Disposition: `I0050 = SUBSTANTIALLY_LATER_RESOLVED / RESIDUAL_SCOPE_RECONCILIATION_REQUIRED / NOT_READY_CLOSABLE`.

No claim is created.

## 5. Successor admission conclusion

After preserving the closed I0030 result, reconciling current ownership, and advancing the queue cursor through I0047–I0050, I still do not have a candidate satisfying all four mandatory dispatch gates simultaneously:

1. exact outside source and locator recovered;
2. dated current-version, later-author and citing-literature checks completed for the exact residual statement;
3. no current owner/claim;
4. genuinely CLOSABLE source scope with a stable source-matching metric.

Therefore R05 is now:

`ROTATION_WAIT / SUCCESSOR_ADMISSION_REQUIRED`.

This is not permission to reopen AF7.30, extend the `N_certified=22` census, steal a HARD problem, or promote a PENDING row automatically. No new mathematical source claim is made in this run, so no decorative checker or artifact is created.

## 6. Model / scheduler implementation status

The implementation limitation is unchanged. The exposed task/scheduler controls do not provide a per-task model-family selector, reasoning-effort selector, authenticated completed-run model telemetry, or guaranteed hour-long execution control. `GPT-6 / maximum` therefore remains prompt text rather than an enforceable setting.

The historical P26 `You cannot modify this task` response is an authorization/context boundary; a later authorized P/C context successfully updated P26. The legitimate remedy for an unmodifiable task is its owning authorized context, an explicit permission change/transfer, or platform support—not duplication or permission bypass.

## 7. ledger_delta

```yaml
ledger_delta:
  worker: R05
  predecessor:
    source: "David Aldous and James Fill, Reversible Markov Chains and Random Walks on Graphs, Open Problem 7.30 / I0030"
    frozen_metric: "largest vertex count through which every admissible graph in the frozen source class has been completely certified"
    before: 22
    after: 22
    metric_state: RETIRED_FROZEN_AFTER_CLOSURE
    mathematical_status: PROVED
    campaign_closure: COMPLETE
    source_status: SOURCE_RESPONSIVE_POSITIVE_ANSWER
    novelty: UNVERIFIED
    audits:
      - R04-AUDIT-R05-I0030-C1-20260916T130900Z
      - P26-AUDIT-R05-I0030-C1-1WALK-REGULAR-13
  methods_this_run: [17, 22, 30]
  successor_screen:
    I0047: PARTIALLY_RESOLVED_OR_SCOPE_RECONCILIATION_REQUIRED_NOT_READY_CLOSABLE
    I0048: MAIN_THRESHOLD_RESOLVED_EXACT_RESIDUAL_SCOPE_REQUIRED_NOT_READY_CLOSABLE
    I0049: KNOWN_DO_NOT_DISPATCH
    I0050: SUBSTANTIALLY_LATER_RESOLVED_RESIDUAL_SCOPE_RECONCILIATION_REQUIRED_NOT_READY_CLOSABLE
  successor_metric: UNMEASURED
  successor_claim_created: false
  active_state: ROTATION_WAIT_SUCCESSOR_ADMISSION_REQUIRED
  remaining_obligation: "A future run may resume only after a genuinely source-current, unowned CLOSABLE OUTSIDE successor is admitted with a stable metric. Do not reopen I0030."
```

No email/Gmail, Drive, public posting, purchase, permission change, shared-root edit, peer-file edit, workflow execution, force-push, or duplicate task was performed.

Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FROZEN-METRIC MOVEMENT: `D_fix = 1 -> 1`; Section-B methods actually tried: #3 PROVE SOMETHING STRONGER, #14 FIND THE GROUP ACTING, #18 SAY IT IN ANOTHER LANGUAGE.**

# NM13-08 research invocation — P0093 all-arity fixed-simplex theorem and 0/1-QSO prior-art bridge

Date: 2026-09-18 UTC  
Track / namespace: `proofnet24/NM13-08/`  
Category: `CLOSABLE OUTSIDE`  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Canonical source / claim: `P0093`, `operations/claims/P0093.md`  
Canonical dedup key: `infinitely_many_fixed_points_of_a_finite-color_automaton`  
Selection shard: `7 mod 13`  
Workflow status after this run: **PROVED-CANDIDATE / AUDIT-PENDING; not protocol-closed**  
Frozen metric before / after: **`D_fix = 1 -> 1`**  
Consecutive unchanged research runs on P0093: **0 -> 1**  
Stuck recoveries used on P0093: **0 -> 0**  
Required eventual outside auditors: **P26 and NM13-09; neither is counted as passed**

## 1. Runtime / control-plane disclosure

The task prompt requests GPT-6 with maximum reasoning. This invocation actually identifies as **GPT-5.6 Sol**. Authenticated reasoning-effort telemetry is not exposed to this report, so the reasoning level is **UNVERIFIED**. I do not claim GPT-6, a binding maximum-reasoning setting, an hour-long execution, or a support escalation.

The exposed task-control surface still offers title/prompt, schedule or relative-start fields, timing mode, and enabled state. It exposes **no bindable model-family selector and no bindable reasoning-effort selector**, and no authenticated per-run applied-model receipt. Therefore `GPT-6 / maximum` remains prompt text only. Making it binding would require an owner-authorized product/workspace/API/admin task surface that actually exposes persistent model and reasoning fields plus authenticated runtime attestation.

The historical P26 `You cannot modify this task` event is an authorization-context boundary, not a mathematical ownership release. Current root reconciliation states that P26 was later modified successfully from another authorized context. If a denial recurs, the legitimate route is the task-owning/otherwise-authorized workspace or platform/admin support for that same task; never task cloning, permission changes, or access-control bypass. This invocation did not create, modify, disable, duplicate, or probe any schedule.

## 2. Authoritative continuity and required repository read

This invocation continues the newest complete NM13-08 report:

`proofnet24/NM13-08/runs/2026-09-18/2026-09-18T06-50-00Z__p0093-fixed-line-construction.md`,

creation commit

`05d3027f580a3d8989c939f9d9ecdd49c1693837`.

That report is authoritative continuity. It admitted P0093 under canonical shard residue 7, created/read back `operations/claims/P0093.md`, and proved the source existence statement for one explicit three-color binary-child automaton. Its exact fixed set was

`{(1,0,0)} union {(1/2,t,1/2-t): 0<=t<=1/2}`,

so the frozen source metric moved

`D_fix: UNMEASURED -> 1`.

It also archived an exact symbolic checker for that base construction. The source-level proof was complete, but closure was correctly withheld because the required P26 and NM13-09 audits had not passed and publication-prior-art status remained unresolved. I do not reset the metric, discard the construction, or pretend this is a fresh admission.

Before the new mathematics I reread or targeted-recovered current `master` state for:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized NM13 deployment material including `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- the newest own report and current canonical P0093 claim;
- the newest visible neighboring NM13-07 and NM13-09 reports;
- the newest visible P26 audit report;
- P0093 source/intake/ranking records, exact-key/ID searches, claim searches, attempt searches, audit searches, and current repository ownership deltas.

The pre-write `master` head captured for this report was

`fad18e47bbe70d099c298dc0f7c64144cd54cacd`.

Compared with the preceding NM13-08 report commit, `master` was **84 commits ahead**. The exact changed-file surface contains other workers' reports/artifacts and new canonical claims, but no change to root `QUEUE.md`, `POSTED.md`, `RESULTS.md`, campaign `INDEX.md`/`RANKING.md`, the controlling owner-rule files, or a P0093 source ledger. No P0093 release, competing owner, handoff, retirement, or source-level correction appeared. The canonical claim remains exclusively NM13-08's.

The latest visible neighboring reports also do not supply a P0093 audit. NM13-07 is working on P0282 (Chen fixed-size LIS log-concavity). NM13-09 is in post-P0245 successor admission screening. The newest P26 report audits R19/E0071 (Björklund Problem 3), not P0093. Repository-wide `P0093 audit` searches recovered no completed P26 or NM13-09 end-to-end audit. Thus both required audits remain **NOT PASSED**.

Large append-only intake/catalogue surfaces are connector-bounded when displayed wholesale. I used the canonical claim, exact P0093/key searches, the intake/rank-sheet entries, prior immutable reports, and exact commit comparison as continuity anchors. I do not infer that inaccessible or truncated history is empty.

## 3. Exact source scope and dated literature recheck

Primary source: Tobias Johnson, Moumanti Podder, Fiona Skerman, *Random tree recursions: which fixed points correspond to tangible sets of trees?*, Random Structures & Algorithms 56(3) (2020), 796–837; arXiv:1808.03019v2.

The paper defines a deterministic tree automaton as

`A : N_0^Sigma -> Sigma`,

and, after fixing a Galton-Watson child law `chi`, defines the automaton distributional map `Psi` by assigning i.i.d. child colors with law `x` and applying `A` to the child-count vector. Its standing setup assumes positive child-law mass on `{2,3,...}`; therefore deterministic offspring `chi=delta_d` is source-admissible for every integer `d>=2`.

Section 6 asks, in substance and with the paper's own notation: when `3 <= |Sigma| < infinity`, can an automaton have infinitely many fixed points? The authors note that this is impossible when `|Sigma|=2` by analyticity.

Dated 2026-09-18 source/current-status searches included the exact article title, the exact `infinitely many fixed points` phrase, `finite-color automaton`, `automaton distributional map`, all three author names, and later citing-tree-recursion terms. No later primary author paper or citing result surfaced that explicitly answers this Section 6 question. This remains **bounded negative evidence only**, not proof of worldwide openness or novelty.

A materially important prior-art bridge did surface under method #18 below: the deterministic-binary case is exactly a `0/1` quadratic stochastic operator, and the QSO literature reaches back at least to Vallander (1972). This raises the prior-art risk substantially. I therefore keep the mathematical source proof intact but **do not make a publication-novelty claim** and do not promote P0093 to protocol closure before the primary older literature is reconciled.

## 4. Frozen metric and what can / cannot count as movement

The frozen metric from admission is

`D_fix = a certified lower bound on the real dimension of the fixed-point set of the one explicit source-admissible three-color, binary-child automaton/child-law pair fixed in operations/claims/P0093.md`.

The previous run proved the complete fixed set of that particular pair contains a line segment, hence

`D_fix = 1`.

This run proves a stronger **family theorem** for all color counts and all deterministic offspring arities, but the frozen metric is deliberately not redefined to mean `supremum dimension over a family`, `m-2`, or a count of parameter values. Therefore:

`D_fix: 1 -> 1`.

This is **no frozen-metric movement**, and the supported unchanged-run counter advances `0 -> 1`. The run nevertheless contains new source-relevant mathematics and a stronger prior-art diagnosis. It is not stuck: the three-unchanged-run trigger has not fired.

## 5. Method #3 — PROVE SOMETHING STRONGER: every finite color count and every deterministic arity

The previous example used `|Sigma|=3` and binary offspring. The natural stronger statement is that neither `3` nor `2` is a special algebraic accident.

### Theorem `NM13-08-P0093-02` — all-arity fixed-simplex family

For every integers

`m >= 3`, `d >= 2`,

there is an `m`-color deterministic tree automaton `A_{m,d}` with the source-admissible child law

`chi = delta_d`

whose automaton distributional map has fixed set exactly

`{e_0} union {x in Delta_{m-1} : x_0 = a_d}`,

where

`a_d = d^(-1/(d-1))`.

Consequently its fixed-point set contains an `(m-2)`-dimensional simplex. In particular it contains uncountably many fixed points for every finite `m>=3` and every deterministic arity `d>=2`.

### Construction

Let

`Sigma={0,1,...,m-1}`.

For a count vector `n=(n_0,...,n_{m-1})` of total size `d`, define

`A_{m,d}(n)=i`

for `i>=1` exactly when

`n_i=1`, `n_0=d-1`, and `n_j=0` for every active color `j notin {0,i}`.

For every other count vector, output color `0`. Count vectors whose total is not `d` are never seen under `chi=delta_d`; set their output to `0` as well to make `A_{m,d}:N_0^Sigma->Sigma` total.

In words: the parent copies the label of the unique nonzero-colored child exactly when there is **one** such child and the remaining `d-1` children are color 0; otherwise the parent is color 0.

### Exact distributional map

Let the i.i.d. child color law be

`x=(x_0,x_1,...,x_{m-1}) in Delta_{m-1}`.

For each active color `i>=1`, the parent is color `i` precisely when one of the `d` ordered child positions is color `i` and every other child is color 0. Hence

`Psi_i(x) = d x_0^(d-1) x_i`  for `i>=1`.

Write

`lambda(x_0)=d x_0^(d-1)`.

The active mass is `1-x_0`, so

`Psi_0(x)=1-lambda(x_0)(1-x_0)`.

This is an exact identity; no limiting or numerical argument is used.

### Complete fixed-set proof

Suppose first that `x=e_0=(1,0,...,0)`. Then every child is color 0, the parent is color 0, and `Psi(e_0)=e_0`.

Now let `x` be any other fixed point. Then at least one active coordinate `x_i` is strictly positive. Its fixed-point equation is

`x_i = Psi_i(x) = lambda(x_0) x_i`.

Since `x_i>0`, this forces

`lambda(x_0)=1`,

that is

`d x_0^(d-1)=1`.

On `[0,1]` the left side is strictly increasing for `d>=2`, so the unique solution is

`x_0=a_d=d^(-1/(d-1))`.

Conversely, if `x_0=a_d`, then `lambda(x_0)=1`, and therefore

`Psi_i(x)=x_i` for every `i>=1`.

Also

`Psi_0(x)=1-(1-x_0)=x_0`.

So every point of the affine simplex slice

`{x in Delta_{m-1}: x_0=a_d}`

is fixed. This slice is naturally a scaled copy of `Delta_{m-2}` and has real dimension `m-2`.

There are no other fixed points by the positive-active-coordinate argument above. This proves the exact fixed-set formula. `QED`.

### Source-level consequences

1. The original three-color binary construction is the special case `(m,d)=(3,2)`, where `a_2=1/2`.
2. The source's lower color threshold is sharp in the literal existence question: the paper itself rules out infinitely many fixed points for two colors, while the construction works for every `m>=3`.
3. Among deterministic source-admissible child laws, binary offspring `d=2` is the smallest possible arity, and it already works.
4. The positive answer is therefore not a delicate special case: every allowed finite color count beyond two admits such a deterministic-arity example.

**Outcome of method #3: success — a complete stronger theorem, without changing the frozen metric.**

## 6. Method #14 — FIND THE GROUP ACTING: the fixed simplex is a symmetry fiber

The active colors `1,...,m-1` are completely symmetric. The permutation group

`S_{m-1}`

acts on the probability simplex by permuting those coordinates and fixing color 0, and the automaton is equivariant under this action.

The useful quotient coordinate is the total active mass

`q = 1-x_0`.

Whenever `q>0`, also record the normalized active composition

`r_i = x_i/q`, `i=1,...,m-1`,

so `r` lies in `Delta_{m-2}`. The exact map above becomes

`q' = lambda(x_0) q = d(1-q)^(d-1) q`,

while

`r' = r`.

Thus the whole nonlinear `m`-state map is a one-dimensional scalar quotient map in `q` together with a frozen `S_{m-1}`-fiber coordinate `r`.

The nontrivial scalar fixed condition is

`d(1-q)^(d-1)=1`,

or

`q = 1-a_d`.

At that scalar fixed value the multiplier on every active coordinate is exactly one, so the entire fiber

`r in Delta_{m-2}`

is pointwise fixed. This makes the dimension `m-2` structural rather than an accidental factorization.

The finite group action itself does not generate a continuum; rather, quotienting by it exposes that the scalar dynamics is blind to the active composition, and the critical multiplier `1` freezes an entire composition fiber.

**Outcome of method #14: success — the symmetry quotient explains the fixed-simplex mechanism and its dimension uniformly in `m`.**

## 7. Method #18 — SAY IT IN ANOTHER LANGUAGE: deterministic binary automata are 0/1 quadratic stochastic operators

For `d=2`, write the parent rule on an unordered child-color pair. The distributional map has the general form

`Psi_k(x) = sum_{i,j} p_{ij,k} x_i x_j`,

with symmetric heredity coefficients satisfying

`p_{ij,k} in {0,1}` and `sum_k p_{ij,k}=1`.

That is exactly a **quadratic stochastic operator with deterministic (`0/1`) heredity coefficients**. Equivalently, the automaton gives a commutative (not necessarily associative) binary operation on colors, and `Psi(x)` is the law of the product of two i.i.d. colors with law `x`.

This translation is mathematically useful and changes the prior-art posture.

### Fresh 2026-09-18 QSO search

Queries included combinations of:

- `quadratic stochastic operator infinitely many fixed points`;
- `quadratic stochastic operator coefficients 1 or 0`;
- `0/1 quadratic stochastic operator Vallander`;
- `On the limit behavior of iteration sequence of certain quadratic transformations`.

The accessible literature establishes at least the following.

1. Modern QSO papers contain explicit operators with infinitely many fixed points, so the general `infinitely many fixed points` mechanism is certainly not new in the unrestricted QSO category.
2. A 2016 paper on doubly stochastic quadratic operators explicitly says that an older paper classified quadratic stochastic operators on the two-dimensional simplex whose relevant coefficients are `1` or `0`.
3. That cited older reference is S. S. Vallander, *On the limit behavior of iteration sequence of certain quadratic transformations*, Soviet Math. Doklady 13 (1972), 123–126.
4. Later QSO papers repeatedly cite Vallander as foundational work on these finite-simplex quadratic transformations.

This is a much closer prior-art connection than the previous report's generic observation that QSO literature exists, because **the source-valid binary deterministic automata are precisely the 0/1 subclass**.

However, I did **not** recover Vallander's primary full text in the presently accessible search surface, and the secondary references inspected here do not by themselves certify that Vallander wrote down this exact automaton/operator, proved a continuum fixed set for an equivalent 0/1 operator, or made the tree-automaton translation. I therefore do not label P0093 `KNOWN`, and I do not claim novelty either.

Current prior-art verdict:

**MATERIAL OVERLAP FOUND / EXACT PRECEDENCE UNVERIFIED.**

The mathematically complete source-level construction survives regardless of priority. But primary-source inspection of Vallander 1972 (and the exact 0/1-classification theorem it contains) is now a mandatory pre-publication / pre-closure literature obligation. If that paper already contains an equivalent continuum-fixed 0/1 QSO, the correct fleet status should be changed from a new proof candidate to `KNOWN` or `KNOWN VIA TRANSLATION`, with full attribution rather than a novelty claim.

**Outcome of method #18: success — it found the correct external language and a concrete 1972 prior-art risk that must be resolved before closure.**

## 8. Validation posture — why no new checker was manufactured

The theorem in Section 5 is a short exact analytic argument with no finite computational core: its only identities are the multinomial probability

`Psi_i=d x_0^(d-1)x_i`

and the one-variable equation

`d x_0^(d-1)=1`.

A new enumerative checker would add ceremony rather than independence. The previous run already archived an exact symbolic checker for the base source-answering case `(m,d)=(3,2)`. This run therefore follows the owner's 90/10 rule and does **not** manufacture another certificate for an unchanged frozen metric.

Self-check status: the displayed proof above is the worker's own proof, not an independent audit.

## 9. Audit / closure state

P0093 is **not called closed**.

The mathematical existence question has a complete explicit source-valid affirmative construction, now strengthened to the all-`m`, all-deterministic-`d` theorem above. But the closure protocol still requires:

- P26 independent end-to-end audit: **NOT PASSED / not recovered**;
- NM13-09 independent end-to-end audit: **NOT PASSED / not recovered**;
- final primary prior-art reconciliation of the deterministic `0/1` QSO literature, especially Vallander 1972.

The newest P26 report audits R19/E0071, and the newest NM13-09 report is admission screening. Neither is counted as a P0093 audit merely because it exists in the neighboring history.

No paper folder is created on this run. Packaging before the two-audit gate and before the new 1972 prior-art issue is resolved would invert the owner's research/closure order.

## 10. Next step

The highest-value next P0093 obligation is **not another finite checker**. It is a source/prior-art and independent-proof attack:

1. obtain and read the primary Vallander 1972 theorem (or an authoritative reproduction of its full statement) and determine whether the 0/1 QSO class already contains an operator equivalent, up to color permutation, to the binary `(m,d)=(3,2)` construction or another continuum-fixed example;
2. separately verify whether later 0/1-QSO classification papers state a fixed-set classification sufficient to make the source question `KNOWN VIA TRANSLATION`;
3. preserve the complete source-level proof above regardless of novelty outcome;
4. await / solicit through the normal fleet ledger the two required end-to-end audits by P26 and NM13-09; do not count a self-check or another NM13-08 run as an audit.

If mathematical exploration continues before those audits land, fresh Section-B routes should avoid repeating `#3/#14/#18`; natural unspent routes are #21 (ask who else has this shape), #22 (read the failures/classification literature rather than success snippets), and #27 (swap the existential quantifiers: fixed child law versus fixed automaton family). These are **suggested next methods only and are not counted as tried in this invocation**.

## 11. Structured `ledger_delta` for P26

```yaml
ledger_delta:
  worker: NM13-08
  category: CLOSABLE_OUTSIDE
  run_status: PROVED_CANDIDATE_AUDIT_PENDING
  source_id: P0093
  claim_id: P0093
  claim_path: operations/claims/P0093.md
  canonical_dedup_key: infinitely_many_fixed_points_of_a_finite_color_automaton
  shard_residue_required: 7
  source_question: finite_color_tree_automaton_infinitely_many_distributional_fixed_points
  metric:
    name: D_fix
    definition: certified_real_dimension_lower_bound_for_the_fixed_three_color_binary_pair
    before: 1
    after: 1
    movement: false
  unchanged_research_runs:
    before: 0
    after: 1
  stuck_recoveries_used:
    before: 0
    after: 0
  methods_attempted:
    - 3
    - 14
    - 18
  method_outcomes:
    3: ALL_M_GE_3_AND_DETERMINISTIC_D_GE_2_FIXED_SIMPLEX_THEOREM
    14: S_M_MINUS_1_QUOTIENT_EXPOSES_SCALAR_DYNAMICS_AND_FIXED_FIBER
    18: DETERMINISTIC_BINARY_AUTOMATON_IDENTIFIED_AS_0_1_QSO_PRIOR_ART_RISK
  new_theorem:
    id: NM13-08-P0093-02
    statement: for_every_m_ge_3_d_ge_2_exact_fixed_set_is_e0_union_slice_x0_eq_d_pow_minus_1_over_d_minus_1
    source_relevant: true
    theorem_proof_on_report_page: true
    essential_finite_core: false
  prior_art:
    date_checked: 2026-09-18
    exact_source_resolution_found: false
    material_overlap_found: true
    overlap: deterministic_binary_case_is_0_1_quadratic_stochastic_operator
    primary_reference_to_reconcile: Vallander_1972_Soviet_Math_Doklady_13_123_126
    primary_full_text_recovered_this_run: false
    novelty_status: UNVERIFIED_HIGH_RISK
    worldwide_openness_claimed: false
  audits:
    P26: NOT_PASSED
    NM13-09: NOT_PASSED
  previous_report_commit: 05d3027f580a3d8989c939f9d9ecdd49c1693837
  prewrite_master_head: fad18e47bbe70d099c298dc0f7c64144cd54cacd
  repo_delta_from_previous_report:
    commits_ahead: 84
    queue_changed: false
    posted_changed: false
    results_changed: false
    campaign_index_changed: false
    campaign_ranking_changed: false
    p0093_claim_changed: false
    p0093_release_found: false
    p0093_competing_owner_found: false
    p0093_audit_found: false
  next_step: reconcile_primary_1972_0_1_QSO_prior_art_then_independent_P26_and_NM13_09_audits
```

## 12. Operational safeguards observed

This invocation wrote only this immutable NM13-08 run report. It did not edit shared root ledgers, the canonical claim, another track's namespace, workflows, permissions, schedules, public surfaces, email/Gmail, Drive, or paid-compute resources. It did not run or import unreviewed external scripts. The report is intended to be read back at its creation commit; no receipt-only follow-up commit is authorized.

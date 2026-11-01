Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO ADMISSION MOVEMENT: `E_ready: 0 -> 0`; I0076 remains `OPEN / PARTIAL / RETIRED-HANDOFF` at `2/4`, and I0124 remains `PARTIAL / RETIRED-HANDOFF` with historical `H_288=112`. Methods #1 CHANGE THE CATEGORY, #11 DUALIZE, #23 DO WHAT THE PROPOSER DID NOT EXPECT.**

# R15 successor admission — F0111 exact hazard/dual reduction

Date checked: 2026-09-18 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Worker: R15, CLOSABLE OUTSIDE.

## 1. Continuity and exclusions

I did **not** reopen Burdzy--Scheutzow Problem 7.2 (`I0076`). Its controlling six-run handoff remains `OPEN / PARTIAL / RETIRED-HANDOFF` with the source-matching counterexample metric frozen at `2/4`. The exact source hypothesis remains: `X` is both FBM and BBM, and at one arbitrary a.s.-finite random real time `T` the two **complete centered half-paths**

`(X_{T+t}-X_T)_{t>=0}` and `(X_{T-t}-X_T)_{t>=0}`

are independent as processes. There is no deterministic-time substitute, no stopping-time assumption, and no assumption that either seam half is itself Brownian. Problem 7.5 remains excluded. The two concrete R15 counterexample candidates are eliminated; the continuous marked-cell copied-block construction in the handoff is only an architecture, not a frozen candidate.

A fresh bounded 2026-09-18 search of the original title/problem language, later author material, and citing Brownian/splitting-time literature again found no accessible source explicitly resolving exact Problem 7.2. This is bounded negative evidence only.

I0124 likewise remains retired after its six-unchanged-run handoff; no cap-set work was reopened.

The current admission metric is

`E_ready = number of newly verified source-clean, current-open, ownership-clear, genuinely CLOSABLE OUTSIDE successors found in this bounded run`.

Before: `0`. After: `0`.

At run start I reread/recovered the campaign INDEX/RANKING, root POSTED/RESULTS/QUEUE, NEW-METHODS implementation material, the newest own R15 report, current neighboring admission/coordinator work, and current ownership state. The newest coordinator pass has meanwhile admitted Fatehizadeh--Luca to another lane and still reports no second fresh free `READY + CLOSABLE OUTSIDE + UNASSIGNED` successor. I therefore continued the intake screen rather than duplicating an admitted source.

## 2. Fresh candidate: F0111, Talagrand Problem 10.9

Source: Michel Talagrand, *Are Many Small Sets Explicitly Small?*, STOC 2010, Problem 10.9, Section 10.

Exact source question:

> Does there exist a universal `gamma>0` such that, for every finite set `S` and every `k`, the threshold up-class
>
> `A_{S,k}={X subset S : |X|>=k}`
>
> belongs to `C_gamma`?

For an up-class `A`, Talagrand defines

`F_A(t)=-log(1-zeta_t(A))`,

where `zeta_t` is the product law with coordinate-`i` inclusion probability `1-exp(-t_i)`. Membership `A in C_gamma` means that for **every** `q in R_+^S` one can choose a multilinear polynomial

`P(t)=sum_{empty != I subset S} beta_I t_I`,  `beta_I>=0`,

such that

`F_A(t)<=P(t)` for all `t>=0`,

and

`P(gamma q)<=gamma F_A(q)`.

The source proves the endpoint classes `k=1` and `k=|S|` (the latter through Theorem 10.6 / 10.7) and gives the disjoint-block stability Proposition 10.5. Problem 10.9 asks for **one gamma uniform in S,k and every heterogeneous q**.

Repository-wide exact search found no canonical `operations/claims/F0111` file. That is only an ownership fact, not an admission decision.

A bounded current-literature search found substantial later work around Talagrand's p-small / weakly-p-small and threshold conjectures, including DeMarco--Kahn and Frankston--Kahn--Park, and the Park--Pham proof of the Kahn--Kalai conjecture. Those results must not be silently substituted for Problem 10.9: the source's `C_gamma` condition is a stronger, pointwise polynomial-majorant statement quantified over every heterogeneous vector `q`. I found no accessible later theorem explicitly claiming Problem 10.9. This is bounded negative evidence, not an exhaustive openness certificate.

## 3. Method #1 — CHANGE THE CATEGORY: exact Poisson-binomial hazard formula

The threshold class has a clean reliability / lower-tail formulation that does not seem to be recorded in the intake attempt.

Let `n=|S|`, write

`y_i=e^{t_i}-1`, `T=sum_i t_i`,

and let `e_j(y)` be the `j`-th elementary symmetric polynomial. Under `zeta_t`, the complement of `A_{S,k}` is the event that at most `k-1` coordinates are selected. Hence, exactly,

`1-zeta_t(A_{S,k}) = e^{-T} sum_{j=0}^{k-1} e_j(y)`.

Therefore

`F_{n,k}(t)=T-log(sum_{j=0}^{k-1} e_j(e^{t_1}-1,...,e^{t_n}-1)).`       (R15.1)

This moves F0111 from a Boolean-class formulation into a **Poisson-binomial lower-tail hazard majorization** problem. The endpoint `k=1` gives `F=T` exactly. For `k=n`, (R15.1) is the all-success hazard treated by the source.

The exact obstruction to a naive use of Proposition 10.5 is now visible. A cardinality threshold can be recursively written using several threshold predicates on the same block, but Proposition 10.5 composes classes only across a genuine partition into disjoint blocks. The obvious sorting-network / dynamic-programming decomposition reuses a block in several predicates, so it is not a legal `C_gamma` composition argument.

## 4. Method #11 — DUALIZE: an exact dual-witness lemma

For fixed `A,q,gamma`, consider the finite-dimensional coefficient problem

`OPT_A(q,gamma) = inf sum_I beta_I (gamma q)_I`

over `beta_I>=0`, subject to

`sum_I beta_I t_I >= F_A(t)` for every `t>=0`.

Then `A in C_gamma` at this particular `q` is exactly `OPT_A(q,gamma)<=gamma F_A(q)`.

The full semi-infinite LP has technical strong-duality questions, but **weak duality alone gives a rigorous counterexample certificate**:

### R15-F0111-D1 — positive-measure dual witness lemma

Let `mu` be any finite positive measure on `R_+^S` such that, for every nonempty `I subset S`,

`int t_I dmu(t) <= (gamma q)_I`.                                      (R15.2)

Then every admissible majorant polynomial satisfies

`P(gamma q) >= int F_A(t) dmu(t)`.                                  (R15.3)

Consequently, if one can find `q` and `mu` obeying (R15.2) but

`int F_A(t) dmu(t) > gamma F_A(q)`,                                 (R15.4)

then `A notin C_gamma`.

**Proof.** If `P(t)=sum_I beta_I t_I` with `beta_I>=0` majorizes `F_A`, then

`int F_A dmu <= int P dmu = sum_I beta_I int t_I dmu <= sum_I beta_I (gamma q)_I=P(gamma q)`.

This proves (R15.3), and (R15.4) contradicts the defining budget inequality. QED.

This is useful because it converts the negative direction of Problem 10.9 into a moment problem. No unproved strong-duality claim is needed.

## 5. Method #23 — REVERSE THE EXPECTED ANSWER: try to break every gamma

The first natural dual attack is to exploit the permutation symmetry of the threshold class while allowing the source's `q` to be homogeneous. It fails in a revealing way rather than producing a counterexample.

Take `q_i=r` for all `i`, fix `m>=k`, choose a uniformly random `m`-subset `J` of `[n]`, and put

`t=a 1_J`,  with  `a=gamma n r/m`.

Let `mu` be the law of this random vector. For an `s`-set `I`,

`int t_I dmu = a^s (m)_s/(n)_s`

(with the value zero when `s>m`). Since

`(n/m)^s (m)_s/(n)_s = product_{j=0}^{s-1} [(1-j/m)/(1-j/n)] <= 1`,  (R15.5)

we have the exact moment constraints

`int t_I dmu <= (gamma r)^s=(gamma q)_I`.

Thus this is a valid dual test measure for every `r>=0` and every `m`.

Now send `r->0` with `n,m,k` fixed. From (R15.1),

`F_{n,k}(r 1_n)=C(n,k) r^k+O(r^{k+1})`,

while

`int F_{n,k}(t)dmu = F_{m,k}(a 1_m)=C(m,k) a^k+O(a^{k+1})`.

Therefore

`[int F dmu]/[gamma F(q)]
 -> gamma^{k-1} * [C(m,k)/C(n,k)]*(n/m)^k
 = gamma^{k-1} product_{j=0}^{k-1} [(1-j/m)/(1-j/n)]
 <= gamma^{k-1}.`                                                    (R15.6)

For the only relevant regime `gamma<=1` (smaller gamma makes `C_gamma` easier), this family cannot violate the dual inequality in the sparse limit. For `m<n` the product is strictly less than one when `k>=2`.

So the most obvious symmetric rare-event counterexample is **structurally on the wrong side** of the inequality. A negative solution, if it exists, must exploit either heterogeneous `q`, a genuinely multi-scale dual measure, or a non-sparse regime. This is the main new mathematical information from this screen.

## 6. Why F0111 is not admitted by R15

F0111 is attractive because the source predicate is exact and the negative direction now has an explicit dual certificate. But it is not honestly `CLOSABLE READY` yet:

1. the source quantifies uniformly over every `n,k` and every heterogeneous `q`;
2. the intake's existing attempt already records that no general source-valid polynomial construction is known beyond the disjoint-block recursion;
3. the exact dual route above identifies a finite-dimensional coefficient cone but still leaves a continuum moment problem over all `t` and all scales;
4. the first large symmetric counterexample family fails rather than exposing a finite witness;
5. the current-literature search is bounded and does not yet certify global openness.

Disposition:

`F0111 = OPEN-LOOKING / OWNERSHIP-CLEAR-IN-BOUNDED-SEARCH / HARD-LEANING / NOT CLOSABLE-READY / NOT CLAIMED`.

I did not create `operations/claims/F0111.md` and did not promote it to READY.

## 7. Source / prior-art checks actually performed

Checked 2026-09-18:

- Talagrand, *Are Many Small Sets Explicitly Small?*, original STOC paper / author-hosted PDF, especially Definition 10.1, Proposition 10.5, Theorem 10.6 and the actual Problem 10.9 page;
- DeMarco--Kahn, *Note on a problem of M. Talagrand* (2015), which answers a different p-small covering problem in a clique-count class;
- Frankston--Kahn--Park, *On a problem of M. Talagrand* (2022), which proves the pair-supported special case of the weakly-p-small to p-small conjecture;
- Park--Pham, *A proof of the Kahn--Kalai conjecture* (JAMS 2024), as nearby later threshold work;
- repository F0111 intake / attempt material and exact ownership search.

Search terms included exact `Problem 10.9`, `C_gamma`, `card X >= k`, the paper title, and later Talagrand threshold/p-small literature.

Limit: search/indexing is bounded; absence of a hit is not a worldwide prior-art certificate.

## 8. Why no checker was created

No finite computational claim is load-bearing here. (R15.1), D1, (R15.5), and the leading-order calculation (R15.6) are symbolic identities/inequalities proved on the page. Writing a checker merely to restate them would invert the 90/10 rule.

## 9. Model / control boundary

The actually running model is GPT-5.6 Sol. Authenticated reasoning-effort telemetry is not exposed, so the reasoning level is UNVERIFIED. The exposed task-management surface still has no binding model-family selector, no reasoning-effort selector, no authenticated applied-model receipt, and no guaranteed hour-long runtime control. Therefore GPT-6 / maximum remains a prompt request, not something this worker can certify or enforce.

The historical P26 `You cannot modify this task` event remains an authorization-context boundary; repository history records a later authorized context succeeding. The lawful remedy is an owner/admin-authorized product or backend surface exposing persistent model/reasoning controls and runtime telemetry, or platform support — not task duplication or a permission bypass. No scheduler or permission change was made.

## 10. Structured ledger_delta

```yaml
ledger_delta:
  worker: R15
  allocation: CLOSABLE_OUTSIDE
  repository: yspennstate/math-open-problems
  branch: master
  continuity:
    I0076:
      source: Burdzy_Scheutzow_Forward_Brownian_Motion_Problem_7_2
      status: OPEN_PARTIAL_RETIRED_HANDOFF_DO_NOT_REOPEN
      metric_name: source_matching_obligations_for_frozen_counterexample
      metric_before: 2
      metric_after: 2
      target: 4
      active_research_this_run: false
    I0124:
      status: PARTIAL_RETIRED_HANDOFF_DO_NOT_REOPEN
      historical_metric_name: H_288
      historical_metric_value: 112
      active_research_this_run: false
  successor:
    status: SUCCESSOR_ADMISSION_REQUIRED
    active_source: NONE
    claim_created: false
    metric_name: E_ready
    metric_before: 0
    metric_after: 0
    movement: none
    unchanged_count: UNKNOWN
  methods_actually_tried: [1, 11, 23]
  substantive_screen:
    problem_id: F0111
    source: Talagrand_STOC_2010_Problem_10_9
    disposition: OPEN_LOOKING_HARD_NOT_CLOSABLE_READY
    owner_found: false
    claim_created: false
    new_exact_reductions:
      - poisson_binomial_lower_tail_hazard_formula_R15_1
      - positive_measure_weak_dual_witness_lemma_D1
      - symmetric_sparse_dual_family_cannot_refute_for_gamma_le_1_R15_6
    exact_blocker: >-
      Uniformly control or refute the positive-coefficient multilinear majorant budget
      for every n, k, heterogeneous q and all t>=0. The disjoint-block closure does not
      implement exact cardinality thresholds without reusing blocks, and the first natural
      symmetric dual counterexample family lies on the non-refuting side.
  evidence:
    original_source_checked: true
    original_problem_page_checked: true
    current_literature_checked: true
    repository_ownership_checked: true
    finite_checker_needed: false
  audit_ids: []
  remaining_obligation: >-
    Continue successor admission beyond F0111. Admit only a source-clean current-open
    ownership-clear CLOSABLE target; do not relabel the exact dual formulation itself as closure.
  next_methods: [3, 15, 27]
  closure_claim: false
```

## 11. Next cursor

Use **#3 PROVE SOMETHING STRONGER, #15 BREAK THE SYMMETRY ON PURPOSE, #27 SWAP THE QUANTIFIERS** on fresh ownership-clear rows. Prefer literal finite/existence/counterexample endpoints where the full source statement can be discharged by one exact construction or a short analytic proof.

**NO I0076 OR I0124 REOPENING. NO F0111 CLAIM. R15 remains `SUCCESSOR_ADMISSION_REQUIRED`.**
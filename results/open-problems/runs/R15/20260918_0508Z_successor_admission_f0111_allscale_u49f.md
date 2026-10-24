Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO ADMISSION MOVEMENT: `E_ready: 0 -> 0`; I0076 remains `OPEN / PARTIAL / RETIRED-HANDOFF` at `2/4`, and I0124 remains `PARTIAL / RETIRED-HANDOFF` with historical `H_288=112`. Methods #3 PROVE SOMETHING STRONGER, #15 BREAK THE SYMMETRY ON PURPOSE, #27 SWAP THE QUANTIFIERS.**

# R15 successor admission — F0111 all-scale orbit obstruction and homogeneous primal reduction

Date checked: 2026-09-18 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Worker: R15, CLOSABLE OUTSIDE.

## 1. Continuity, source fidelity, and exclusions

I did **not** reopen Burdzy--Scheutzow Problem 7.2 (`I0076`). The controlling six-run handoff remains `OPEN / PARTIAL / RETIRED-HANDOFF`, with its original counterexample metric frozen at `2/4`.

The source hypothesis is preserved exactly: `X` is both forward Brownian and backward Brownian, and there exists an arbitrary a.s.-finite random real time `T` for which the two **complete centered half-paths**

`(X_{T+t}-X_T)_{t>=0}` and `(X_{T-t}-X_T)_{t>=0}`

are independent as processes. I do not replace this by deterministic-time independence, do not assume `T` is a stopping/splitting time, and do not separately assume the two seam halves are Brownian. Problem 7.5 remains excluded. The two concrete R15 counterexample candidates were eliminated before retirement; the marked-Brownian-cell copied-block idea in the handoff is only an architecture, not a surviving frozen candidate.

I0124 also remains retired after its six-unchanged-run handoff. No cap-set work was reopened.

The current admission metric remains

`E_ready = number of newly verified source-clean, current-open, ownership-clear, genuinely CLOSABLE OUTSIDE successors found in this bounded run`.

Before: `0`. After: `0`.

Before new mathematics I reread/recovered the current campaign `INDEX.md` / `RANKING.md`, root `POSTED.md` / `RESULTS.md` / `QUEUE.md`, the current new-methods implementation material, the newest own R15 report, recent neighboring admission/coordinator reports, and current exact-ID/source ownership records for the queue front examined below. Large intake JSONL rendering is connector-bounded, so I used exact-ID/source-targeted retrieval and do not claim a fictitious byte-for-byte rescan of every historical intake row.

The newest current fleet screens still expose no second free target simultaneously satisfying `READY + CLOSABLE OUTSIDE + UNASSIGNED`: the recent Fatehizadeh--Luca candidate has already acquired a canonical claim in another lane, and Jeandel's Baker candidate was downgraded to HARD-shaped. I therefore did not create a successor claim merely to keep R15 occupied.

## 2. Fresh source/current-literature check for F0111

I continued the exact source `F0111`, Michel Talagrand, *Are Many Small Sets Explicitly Small?*, STOC 2010, Problem 10.9, only as **successor screening mathematics**, not as an admitted R15 target.

The source asks whether there exists a universal `gamma>0` such that every cardinality threshold up-class

`A_{n,k}={X subset [n]: |X|>=k}`

belongs to Talagrand's `C_gamma`. For an up-class `A`,

`F_A(t)=-log(1-zeta_t(A))`,

where coordinate `i` is present under `zeta_t` with probability `1-exp(-t_i)`. Membership in `C_gamma` means that for **every** `q in R_+^n` there is a multilinear polynomial

`P(t)=sum_{empty != I subset [n]} beta_I t_I`, `beta_I>=0`,

such that `F_A(t)<=P(t)` for every `t>=0` and

`P(gamma q)<=gamma F_A(q)`.

Fresh 2026-09-18 source/current searches again recovered the original STOC source (ACM publication record dated 5 June 2010, plus an accessible copy containing Definition 10.1 and the Section 10 problem), and nearby later work including DeMarco--Kahn and the modern p-small/threshold literature. I found no accessible later theorem explicitly claiming Talagrand's exact Problem 10.9 with its heterogeneous-`q`, pointwise positive-polynomial majorant quantifiers. This is bounded negative evidence only, not a worldwide openness certificate.

The preceding R15 report already established the exact threshold hazard formula

`F_{n,k}(t)=T-log(sum_{j=0}^{k-1} e_j(e^{t_1}-1,...,e^{t_n}-1))`, `T=sum_i t_i`,

and the weak-dual witness lemma: any positive measure `mu` satisfying

`int t_I dmu <= (gamma q)_I` for every nonempty `I`

forces every admissible majorant to satisfy

`P(gamma q) >= int F_{n,k}(t)dmu(t)`.

Thus a strict inequality `int F dmu > gamma F(q)` is a rigorous negative certificate. The previous run tested a natural exchangeable one-orbit family only in the sparse limit. This run strengthens that analysis to **all scales**.

## 3. Method #3 — PROVE SOMETHING STRONGER: the entire symmetric one-orbit dual family cannot refute

### R15-F0111-D2 — exact all-scale non-refutation theorem

Fix integers `n>=m>=k>=1`, `r>=0`, and `0<gamma<=1`. Let

`q=r 1_n`.

Choose a uniformly random `m`-subset `J` of `[n]` and set

`t=a 1_J`, where `a=gamma n r/m`.

Let `mu` be the law of `t`. Then:

1. `mu` satisfies **all** dual moment constraints
   `int t_I dmu <= (gamma q)_I` for every nonempty `I subset [n]`;
2. nevertheless

`int F_{n,k}(t)dmu(t) <= gamma F_{n,k}(q)`.

Consequently **no member of this entire exchangeable one-orbit family can be a dual counterexample to `C_gamma`, at any scale `r`**. This replaces the previous sparse-limit obstruction by an exact all-scale theorem.

### Proof of (1): exact moment constraints

Let `s=|I|`. If `s>m`, the left side is zero. Otherwise

`E_mu[t_I]=a^s (m)_s/(n)_s`.

Since `a=gamma n r/m`,

`E_mu[t_I]/(gamma r)^s
 = (n/m)^s (m)_s/(n)_s
 = product_{j=0}^{s-1} [(1-j/m)/(1-j/n)] <= 1`,

because `m<=n`. Hence every dual moment constraint holds.

### Proof of (2): exponential order statistics plus log-concavity

Let `E_1,...,E_n` be i.i.d. rate-one exponentials and let `T_{n,k}` be their `k`-th order statistic. Since a coordinate is present under `zeta_{r1_n}` exactly when `E_i<=r`,

`F_{n,k}(r1_n) = -log P(T_{n,k}>r)`.                         (D2.1)

The exponential-spacing representation gives

`T_{n,k} =_d sum_{j=0}^{k-1} Z_j/(n-j)`,                      (D2.2)

with independent rate-one exponentials `Z_0,...,Z_{k-1}`.

Use the same `Z_j` to couple `T_{m,k}` and `T_{n,k}`. Then, term by term,

`(m/n) T_{m,k}
 = sum_{j=0}^{k-1} [m/(n(m-j))] Z_j
 >= sum_{j=0}^{k-1} [1/(n-j)] Z_j
 = T_{n,k}`,                                                   (D2.3)

because

`m/[n(m-j)] >= 1/(n-j)` iff `j(n-m)>=0`.

Since `a=gamma n r/m`, (D2.3) implies

`P(T_{m,k}>a)
 = P((m/n)T_{m,k}>gamma r)
 >= P(T_{n,k}>gamma r)`.

Therefore

`F_{m,k}(a1_m) <= F_{n,k}(gamma r 1_n)`.                      (D2.4)

It remains to compare scale `gamma r` with `r`. Define

`H(r)=F_{n,k}(r1_n)=-log P(T_{n,k}>r)`.

Each summand in (D2.2) has a log-concave density on `R_+`; convolution preserves log-concavity, so `T_{n,k}` has a log-concave density. Integrating a log-concave density over the ray `[r,infinity)` preserves log-concavity of the survival function. Thus `H=-log(survival)` is convex. Also `H(0)=0`. Hence for `0<=gamma<=1`,

`H(gamma r) <= gamma H(r)`.                                  (D2.5)

Finally, because the `n-m` inactive coordinates of `t=a1_J` have selection probability zero and `m>=k`, permutation symmetry gives

`int F_{n,k}(t)dmu(t)=F_{m,k}(a1_m)`.

Combining this with (D2.4)--(D2.5) proves

`int F dmu <= gamma F_{n,k}(r1_n)=gamma F(q)`.

QED.

For completeness, restricting to `gamma<=1` loses nothing in a positive solution search: if a particular positive-coefficient majorant works at `gamma`, then for `0<gamma'<=gamma`, positivity and absence of a constant term give

`P(gamma' q) <= (gamma'/gamma) P(gamma q) <= gamma' F(q)`.

Thus existence at any larger parameter implies existence at every smaller one.

### What D2 changes

The previous report only knew that this symmetric witness fails as `r->0`. D2 eliminates **the full scale parameter**. A negative solution cannot be obtained by taking one uniformly random `m`-subset, putting a common height on it, and using homogeneous `q`, no matter how the scale is tuned.

That is genuine route elimination, not a source solution.

## 4. Method #15 — BREAK THE SYMMETRY ON PURPOSE: exact heterogeneous one-atom reduction

D2 says the next negative attack must use asymmetry somewhere. The cleanest exact place to expose it is a single-atom dual measure.

Fix strictly positive `q,t` and consider

`mu = w delta_t`.

The dual constraints are

`w t_I <= (gamma q)_I` for every nonempty `I`.

Put

`rho_i = gamma q_i/t_i`.

Then the **largest feasible atom weight is explicit**:

`w_max(t;q,gamma) = min_{empty != I subset [n]} product_{i in I} rho_i`

and therefore

`w_max = product_{i: rho_i<1} rho_i` if at least one `rho_i<1`,

while

`w_max = min_i rho_i` if all `rho_i>=1`.                      (D2.6)

The proof is immediate: among products of positive `rho_i`, every factor below one should be included in a minimizing subset, every factor above one should be omitted, and if no factor is below one the best nonempty subset is the smallest singleton.

So every heterogeneous one-atom counterexample is equivalent to the finite-dimensional analytic inequality

`w_max(t;q,gamma) F_{n,k}(t) > gamma F_{n,k}(q)`.             (D2.7)

This is a substantially sharper search problem than the original semi-infinite dual, although it is still continuous and does not by itself make F0111 CLOSABLE.

The probabilistic reason asymmetry matters is also precise. For homogeneous `q`, the `k`-th-arrival time has deterministic spacing rates `n,n-1,...`. For heterogeneous rates `q_i`, after each arrival the next total rate depends on **which coordinate arrived**, so the deterministic spacing representation (D2.2) disappears. The pathwise comparison behind D2 is therefore genuinely an exchangeability theorem, not an argument that silently covers heterogeneous `q`.

## 5. Method #27 — SWAP THE QUANTIFIERS: homogeneous primal symmetrization

A complementary positive attack becomes much smaller after swapping the order in which one handles `q` and the all-`t` majorization.

Fix homogeneous `q=r1_n`. Suppose `P` is any feasible positive-coefficient majorant for this `q`. Average it over the permutation group:

`P_bar(t)=1/n! sum_{sigma in S_n} P(sigma t)`.

Because `F_{n,k}` is permutation invariant,

`P_bar(t)>=F_{n,k}(t)` for every `t>=0`.

All coefficients remain nonnegative, and since `q` is fixed by every permutation,

`P_bar(gamma q)=P(gamma q)`.

Therefore at homogeneous `q` one may assume without loss that

`P_bar(t)=sum_{s=1}^n beta_s e_s(t)`, `beta_s>=0`.            (D2.8)

This reduces the primal coefficient dimension from `2^n-1` to exactly `n`.

Evaluating (D2.8) on the orbit representatives `t=a1_m` yields the necessary one-dimensional family of constraints

`sum_{s=1}^m binom(m,s) beta_s a^s >= F_{m,k}(a1_m)`          (D2.9)

for every `m=1,...,n` and every `a>=0` (with the right side zero when `m<k`).

The missing theorem is now sharply stated: **are these orbit constraints sufficient for the global majorization over arbitrary `t` after symmetrization, perhaps via a Schur-convexity/majorization principle?** I did not prove that. Without it, (D2.8)--(D2.9) is a rigorous reduction, not a positive solution.

## 6. Admission consequence

F0111 remains

`OPEN-LOOKING / OWNERSHIP-CLEAR-IN-BOUNDED-SEARCH / HARD / NOT CLOSABLE-READY / NOT CLAIMED`.

This run improved the mathematical understanding of that screen but did **not** turn the source into an eligible CLOSABLE successor. The exact remaining negative routes must use at least one of:

- heterogeneous `q`;
- multiple dual atoms/orbits or genuinely multiscale mass;
- a nonexchangeable construction not dominated by D2.

The positive route can, at homogeneous `q`, be reduced to the `n` coefficients in (D2.8), but the global all-`t` majorization is still unresolved. The full source additionally quantifies over every heterogeneous `q`, every `n`, and every `k`.

Current ownership/current-status checks of the queue front still leave `E_ready=0`. I did not create `operations/claims/F0111.md` or any other successor claim.

## 7. Why no checker was created

No finite computation is load-bearing in D2, (D2.6), or the symmetrization reduction. These are exact analytic statements with complete proofs on the page. A checker would only recertify elementary algebra and would violate the run's 90/10 research-first rule.

## 8. Model/control boundary

The actually running model is GPT-5.6 Sol. Authenticated reasoning-effort telemetry is not exposed, so the reasoning level is UNVERIFIED. The exposed task-management surface still has prompt/title, schedule/relative-start, timing-mode and enabled-state controls, but no binding model-family selector, no reasoning-effort selector, no authenticated applied-model receipt, and no guaranteed hour-long execution field. Therefore GPT-6 / maximum is a prompt request, not something this worker can truthfully certify or enforce.

The historical P26 `You cannot modify this task` response remains an authorization-context boundary; repository history records later success from an authorized context. The lawful remedy is the task-owning/otherwise authorized product or backend surface, supported ownership/admin reassignment, or platform support. I did not duplicate a task, bypass permissions, or modify any schedule.

## 9. Structured ledger_delta

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
  methods_actually_tried: [3, 15, 27]
  substantive_screen:
    problem_id: F0111
    source: Talagrand_STOC_2010_Problem_10_9
    disposition: OPEN_LOOKING_HARD_NOT_CLOSABLE_READY
    owner_found: false
    claim_created: false
    new_exact_results:
      - R15_F0111_D2_all_scale_non_refutation_for_uniform_m_subset_orbit_duals_at_homogeneous_q
      - exact_maximum_weight_formula_for_heterogeneous_single_atom_dual_witnesses
      - homogeneous_q_primal_symmetrization_from_2_power_n_minus_1_coefficients_to_n_coefficients
    remaining_obstruction: >-
      Either find a heterogeneous or genuinely multiscale dual witness violating the budget,
      or prove a global positive majorization theorem. D2 rules out the entire one-scale
      exchangeable uniform-m-subset orbit family at homogeneous q for every scale.
  evidence:
    original_source_checked: true
    current_literature_checked: true
    later_related_work_checked: true
    repository_ownership_checked: true
    finite_checker_needed: false
  audit_ids: []
  remaining_obligation: >-
    Continue successor admission beyond F0111. Admit only a source-clean current-open
    ownership-clear genuinely CLOSABLE outside target. Do not promote F0111 from this
    reduction alone.
  next_methods: [4, 18, 21]
  closure_claim: false
```

## 10. Next cursor

Use fresh methods **#4 PROVE SOMETHING WEAKER, COMPLETELY; #18 SAY IT IN ANOTHER LANGUAGE; #21 ASK WHO ELSE HAS THIS SHAPE** on the next ownership-clear source rows. Prefer a literal finite witness/existence/counterexample endpoint whose **full source statement**, not an invented restricted milestone, can be discharged.

**NO I0076 OR I0124 REOPENING. NO F0111 CLAIM. R15 remains `SUCCESSOR_ADMISSION_REQUIRED`.**

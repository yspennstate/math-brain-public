Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO ADMISSION MOVEMENT: `E_ready: 0 -> 0`; retired I0100 remains frozen at `p_max=1213`, retirement count `6`; methods #7 TAKE THE LIMIT, #19 MAKE IT AN ALGORITHM, #25 COUNT THE SAME THING TWICE.**

# R20 successor admission — F0111 degree-drop no-go and exact gap-insertion reduction

Date checked: 2026-09-18 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Worker: R20, CLOSABLE OUTSIDE.

## 1. Continuity, ownership, and source status

I did **not** reopen Randomstrasse101 Conjecture 26 / intake I0100. Its mandatory six-unchanged-run handoff remains controlling. The original metric is frozen at

`p_max = 1213`,

with retained exact primal/dual certificate set

`{5,13,17,29,41,181,241,317,421,541,601,661,1009,1021,1033,1049,1061,1093,1201,1213}`.

A fresh 2026-09-18 current-source search recovered the current Jig root for Randomstrasse101 Conjecture 26 still labeled **Open**, asking whether the Lovasz theta of the complement of the Paley 1-localization is asymptotic to `sqrt(p/2)`. The kernel-checked sufficient reductions displayed there do not claim the root asymptotic. Therefore I0100 remains `OPEN / PARTIAL / RETIRED-HANDOFF`; the retirement count remains 6 and was not incremented.

Before new mathematics I recovered the newest R20 report

`runs/R20/2026-09-18T05-12-10Z_successor_admission_f0111_tangent_family_5c2a81.md`,

and checked current fleet/admission state and neighboring F0111 work. In particular, R15 has independently screened F0111 and proved an all-scale no-go for one symmetric one-orbit dual family plus a homogeneous-primal symmetrization. I do not rederive or relabel those results here.

A direct current fetch of `operations/claims/F0111.md` returned 404 immediately before this report. This is bounded visible-repository evidence of no canonical F0111 claim, not permission to call F0111 admitted. The newest coordinator-type admission screen still reports no newly free source-clean/current-open/ownership-clear CLOSABLE target in its lane; fresh fleet commits added claims rather than a relevant release.

The current admission metric therefore stays

`E_ready = number of newly verified source-clean, current-open, ownership-clear, genuinely CLOSABLE OUTSIDE successors found in this bounded run`.

Before: `0`. After: `0`.

## 2. F0111 source fidelity and current-status check

I continued Michel Talagrand, *Are Many Small Sets Explicitly Small?*, STOC 2010, Problem 10.9 (`F0111`) only as **successor-screening mathematics**, not as an admitted R20 target.

The source asks whether there exists a universal `gamma>0` such that every cardinality-threshold up-class

`A_{n,k} = {X subset [n] : |X| >= k}`

belongs to Talagrand's `C_gamma`. For an up-class `A`, write

`F_A(t) = -log(1-zeta_t(A))`,

where coordinate `i` is selected independently with probability `1-exp(-t_i)`. Membership in `C_gamma` means that for every base point `q>=0` there exists a multilinear polynomial with nonnegative coefficients and no constant term,

`P(t)=sum_{empty != I subset [n]} beta_I t_I`, `beta_I>=0`,

such that

`F_A(t) <= P(t)` for all `t>=0`,

and

`P(gamma q) <= gamma F_A(q)`.

Fresh dated searches on 2026-09-18 used the source title plus `Problem 10.9`, `threshold classes`, and `polynomial majorant`, and separately searched nearby later Talagrand-threshold/p-small literature. I recovered the ACM STOC publication and the exact Problem 10.9 source. I did not recover an accessible later theorem explicitly claiming the full heterogeneous-`q`, pointwise positive-polynomial source statement. This is only bounded negative evidence, not a worldwide or novelty certificate.

The source's Theorem 10.7 is particularly relevant below. It supplies a universal constant for the two-variable kernel

`G(u,v) = -log(exp(-u)+exp(-v)-exp(-u-v))`

by constructing, at every base point `(u0,v0)`, a polynomial

`R(u,v)=a u+b v+c u v`, `a,b,c>=0`,

that majorizes `G` globally and obeys the source `C_gamma` budget at the base point.

## 3. Exact threshold hazard identities carried forward

Let

`N_t = sum_i Bernoulli(1-exp(-t_i))`

and

`F_{n,k}(t) = -log P(N_t < k)`.

Put `y_i=exp(t_i)-1` and

`Z_j(y)=sum_{ell=0}^j e_ell(y)`.

Then exactly

`F_{n,k}(t)=sum_i t_i - log Z_{k-1}(y)`.                     (3.1)

The preceding R20 run proved

`partial_i F_{n,k}(t)=e_{k-1}(y_{-i})/Z_{k-1}(y)`,             (3.2)

and hence the global positive multilinear bound

`F_{n,k}(t) <= e_k(t)`.                                        (3.3)

For self-containment, (3.3) follows because each `(k-1)`-fold term satisfies

`y_J/Z_{k-1}(y) <= y_J/prod_{j in J}(1+y_j)
                 = prod_{j in J}(1-exp(-t_j))
                 <= prod_{j in J} t_j`,

so

`partial_i F <= e_{k-1}(t_{-i})`.

Integrating along `s t`, `0<=s<=1`, and using

`sum_i t_i e_{k-1}(t_{-i}) = k e_k(t)`

gives (3.3).

## 4. Method #25 — COUNT THE SAME THING TWICE: an exact degree-drop envelope

The first new observation is that (3.3) can be applied after *forcing the proof to ignore selected coordinates*.

### R20-F0111-E1 — degree-drop envelope

Fix `1<=d<=k` and a subset `B subset [n]` with

`|B|=k-d`.

Then, for every `t>=0`,

`F_{n,k}(t) <= F_{B^c,d}(t_{B^c}) <= e_d(t_{B^c}).`           (E1)

### Proof

Let `N_{B^c}` be the number of selected coordinates outside `B`. The event

`{N_{B^c}<d}`

forces

`N_t <= |B|+(d-1)=k-1`.

Thus

`{N_{B^c}<d} subset {N_t<k}`,

so

`P(N_t<k) >= P(N_{B^c}<d)`.

Applying `-log` gives the first inequality. The second is (3.3) for the smaller threshold problem `(B^c,d)`. QED.

This gives a finite algorithmic family of exact source-valid positive multilinear majorants:

`P_{B,d}(t)=e_d(t_{B^c})`.                                    (E2)

At a base point `q`,

`P_{B,d}(gamma q)=gamma^d e_d(q_{B^c})`,

so this certificate closes the source budget whenever

`gamma^{d-1} e_d(q_{B^c}) <= F_{n,k}(q)`.                     (E3)

A natural algorithm is therefore: sort or otherwise score coordinates, choose a proposed effective degree `d`, remove `k-d` coordinates into `B`, and test (E3). This exactly realizes the degree-drop intuition from the previous R20 saturation analysis.

The important question is whether this pure family can cover all base points. Method #7 answers **no**.

## 5. Method #7 — TAKE THE LIMIT: pure degree-drop certificates fail in the saturated boundary layer

Take `k-1` heavy coordinates, each equal to `M`, and let the remaining `m=n-k+1` light coordinates be a fixed nonzero vector

`q=(q_1,...,q_m)`, `T=sum_i q_i>0`.

Write `epsilon=exp(-M)` and `y_i=exp(q_i)-1` for the light coordinates.

Let `R` be the number of heavy coordinates that fail to be selected and let `L` be the number of selected light coordinates. The total count is less than `k` exactly when

`L<=R`.

Counting the cases `R=0` and `R=1` gives

`P(N<k)
 = (1-epsilon)^{k-1} P(L=0)
   +(k-1)epsilon(1-epsilon)^{k-2}P(L<=1)
   +O(epsilon^2)`.

Now

`P(L=0)=exp(-T)`

and

`P(L<=1)=exp(-T)(1+e_1(y))`.

Therefore

`P(N<k)
 = exp(-T)[1+(k-1)e^{-M} e_1(exp(q)-1)+O(e^{-2M})]`,

and hence

`F_{n,k}(M 1_{k-1},q)
 = T-(k-1)e^{-M}e_1(exp(q)-1)+O(e^{-2M}).`                    (L1)

In particular, for every sufficiently large finite `M`,

`F_{n,k}(M 1_{k-1},q) < T`,                                  (L2)

while the hazard approaches `T` from below.

### R20-F0111-NOGO2 — the whole pure degree-drop envelope family cannot solve Problem 10.9

Fix any `gamma>0`. For the saturated base points above and all sufficiently large `M`, **no** polynomial of the form (E2) can satisfy the source budget.

Proof. If `d=1`, then `|B|=k-1`. The best possible choice removes all heavy coordinates and leaves the light tail, giving

`P_{B,1}(gamma q_full)=gamma T`.

The source budget would require `T<=F(q_full)`, contradicting (L2).

If `d>=2`, the set `B` has only `k-d` slots, so at least `d-1` of the `k-1` heavy coordinates remain in `B^c`. Therefore

`e_d((q_full)_{B^c}) >= M^{d-1} T`,

and the normalized budget cost obeys

`P_{B,d}(gamma q_full)/gamma
 = gamma^{d-1}e_d((q_full)_{B^c})
 >= gamma^{d-1}M^{d-1}T -> infinity`,

whereas `F(q_full)->T`. QED.

This is a rigorous route no-go, **not** a refutation of F0111. It says a successful multiscale certificate must do something strictly subtler than selecting one effective degree. In the top-heavy boundary layer its light-tail linear coefficient must be **strictly below one at every finite heavy scale**, with the missing mass supplied by cross terms involving heavy coordinates. This is the precise defect that the pure degree-drop envelope cannot repair.

## 6. Methods #19 and #25 — MAKE IT AN ALGORITHM / COUNT TWICE: exact insertion through hazard gaps

The preceding no-go suggests not approximating the whole threshold hazard at once. Instead expose the *increment between adjacent thresholds*.

For `1<=j<=m`, define

`D_{m,j}(t)
 := F_{m,j}(t)-F_{m,j+1}(t)
 = log(Z_j(y)/Z_{j-1}(y))
 >=0`,                                                       (G1)

with `F_{m,m+1}=0`.

Telescoping gives the exact second count

`F_{m,k}(t)=sum_{j=k}^m D_{m,j}(t)`.                          (G2)

Now insert one new coordinate of intensity `x`. Conditioning on whether that coordinate is selected gives

`P(N_{m+1}<k)
 = e^{-x}P(N_m<k)+(1-e^{-x})P(N_m<k-1)`.                     (G3)

Set

`U=F_{m,k}(t)`,

`W=F_{m,k-1}(t)-F_{m,k}(t)=D_{m,k-1}(t)`.

Then (G3) becomes

`P(N_{m+1}<k)
 = e^{-U}[e^{-x}+e^{-W}-e^{-x-W}]`.

Therefore the exact insertion law is

`F_{m+1,k}(x,t)
 = F_{m,k}(t)+G(x,D_{m,k-1}(t)),`                             (G4)

where

`G(u,v)=-log(e^{-u}+e^{-v}-e^{-u-v})`.

This is exactly the two-variable kernel already handled by Talagrand's Theorem 10.7.

The gap sequence itself obeys the exact update

`D'_{k}
 = D_k + G(x,D_{k-1})-G(x,D_k)`.                             (G5)

Equation (G5) also exposes the obstruction to a naive positivity induction: the gap update contains a **subtraction** of a positive kernel term. The whole hazard insertion (G4) is positivity-friendly; the gap dynamics are not automatically so.

## 7. Conditional reduction: Problem 10.9 follows from uniform positive certificates for the gaps

The insertion identity turns the full source problem into a sharper subproblem.

### R20-F0111-RED1 — gap-certificate reduction

Let `gamma_G>0` be a universal constant supplied by Talagrand's Theorem 10.7 for the kernel `G` above. Suppose there exists a universal `gamma_D>0` with the following property:

for every `m>=1`, every `1<=j<=m`, and every base point `q>=0`, there is a multilinear polynomial `Q_{m,j,q}` with nonnegative coefficients and no constant term such that

`D_{m,j}(t) <= Q_{m,j,q}(t)` for all `t>=0`,                 (R1)

and

`Q_{m,j,q}(gamma_D q) <= gamma_D D_{m,j}(q)`.                (R2)

Then every cardinality-threshold class `A_{n,k}` belongs to `C_gamma` for

`gamma=min(gamma_G,gamma_D)`.

### Proof

The case `k=1` is already source-known; for `k>=2`, induct on the number of inserted coordinates beginning from `m=k-1`, where `F_{k-1,k}=0` has the zero certificate.

Assume `P(t)` is a source-valid positive multilinear certificate for `F_{m,k}` at base point `q`. Let `Q(t)` be a gap certificate for `D_{m,k-1}` at the same base point.

At the two-variable base point

`(x_0,D_{m,k-1}(q))`,

Talagrand's Theorem 10.7 gives a positive polynomial

`R(u,v)=a u+b v+c u v`, `a,b,c>=0`,

with

`G(u,v)<=R(u,v)` globally

and source budget at `gamma_G`.

Define

`P_new(x,t)=P(t)+R(x,Q(t))`.                                  (R3)

Because all coefficients are nonnegative and `x` is a new variable, (R3) is again multilinear with nonnegative coefficients. By (G4), (R1), and monotonicity of `R` in its second argument,

`F_{m+1,k}(x,t)
 <=P(t)+R(x,Q(t))
 =P_new(x,t)`.

It remains to check the budget at `gamma=min(gamma_G,gamma_D)`. Positive polynomials without constant terms satisfy, for `0<lambda<=lambda_0`,

`H(lambda z) <= (lambda/lambda_0) H(lambda_0 z)`.             (R4)

Applying (R4) to `Q` and (R2) gives

`Q(gamma q)<=gamma D_{m,k-1}(q)`.

Applying (R4) to the two-variable positive polynomial `R`, together with its `gamma_G` budget, gives

`R(gamma x_0, gamma D(q)) <= gamma G(x_0,D(q))`.

Hence

`P_new(gamma x_0,gamma q)
 <= gamma F_{m,k}(q)+gamma G(x_0,D(q))
 = gamma F_{m+1,k}(x_0,q)`

by (G4). This closes the induction. QED.

### Consequence

F0111 is therefore reduced to a much more structured source-faithful question:

> Do the adjacent-threshold gaps
> `D_{m,j}(t)=log(Z_j(e^t-1)/Z_{j-1}(e^t-1))`
> admit a universal Talagrand-positive-polynomial certificate?

The outer nonlinear composition is **already solved in the original source** through Theorem 10.7. The remaining difficulty is entirely in the gap object.

I label `R20-F0111-E1`, `R20-F0111-NOGO2`, and `R20-F0111-RED1` **SELF_CHECK_ONLY**. They are proved on the page but have no independent fleet audit and do not close F0111.

## 8. Admission consequence

The run materially sharpens the F0111 mechanism but does not make it honestly CLOSABLE. The source still quantifies uniformly over every `n,k,q`; the new gap-certificate problem remains theorem-sized, and no universal `gamma_D` is proved.

Current disposition:

`F0111 = OPEN-LOOKING / NO CANONICAL CLAIM VISIBLE IN BOUNDED CHECK / HARD-LEANING / NOT CLOSABLE-READY / NOT CLAIMED BY R20`.

No ownership claim was created. No finite checker was created because no finite arithmetic claim is load-bearing in E1, NOGO2, G4/G5, or RED1; these are exact analytic identities/arguments written out above. Manufacturing a checker would add bookkeeping without validating the missing universal gap theorem.

The new exact remaining obligation is

`GAP_CERTIFICATE:` find a universal `gamma_D>0` and positive multilinear base-point-dependent majorants for every

`D_{m,j}(t)=log(Z_j/Z_{j-1})`,

or produce a rigorous dual obstruction showing that such a uniform gap certificate cannot exist.

This is substantially narrower than the original semi-infinite F0111 statement and interfaces directly with total-positivity / reliability-polynomial / hazard-rate structure of the elementary-symmetric ratios.

Next Section-B moves for any continued F0111 screening are **#1 CHANGE THE CATEGORY, #12 FIND WHAT IS CONSERVED, #20 FIND WHY THE ALGORITHM FAILS**, focusing specifically on the gap map rather than another whole-hazard majorant.

## 9. Model/control boundary

The exposed scheduler/task-management interface still provides prompt/title, schedule/relative-start, enabled state, and timing mode, but no binding model-family selector, no reasoning-effort selector, no authenticated applied-model/reasoning receipt, and no guaranteed hour-long execution field. Therefore `GPT-6 / maximum` remains a prompt request rather than something this worker can certify or enforce.

The historical P26 `You cannot modify this task` response remains an authorization-context boundary. The lawful workaround is the owning or otherwise admin-authorized product/workspace/backend surface, supported ownership transfer, or platform support; duplicating the task or bypassing permissions is not valid. No scheduler change was attempted.

## 10. Structured ledger_delta

```yaml
ledger_delta:
  worker: R20
  allocation: CLOSABLE_OUTSIDE
  repository: yspennstate/math-open-problems
  branch: master
  retired_source:
    id: I0100
    target: Randomstrasse101_Conjecture_26_Paley_1_localization_theta_asymptotic
    status: OPEN_PARTIAL_RETIRED_HANDOFF_DO_NOT_REOPEN
    metric_name: largest_admissible_prime_with_matching_exact_primal_dual_certificates
    before: 1213
    after: 1213
    covered_primes: [5,13,17,29,41,181,241,317,421,541,601,661,1009,1021,1033,1049,1061,1093,1201,1213]
    unchanged_retirement_count: 6
  successor_screen:
    metric_name: E_ready
    before: 0
    after: 0
    status: SUCCESSOR_ADMISSION_REQUIRED
    source_screened: F0111
    source_target: Talagrand_Problem_10_9_threshold_classes_C_gamma
    ownership: NO_CANONICAL_F0111_CLAIM_VISIBLE_IN_DIRECT_CURRENT_FETCH
    admission: NOT_CLAIMED_HARD_LEANING
  section_B_methods:
    attempted: [7,19,25]
    results:
      7: top_heavy_limit_exact_expansion_and_pure_degree_drop_family_no_go
      19: exact_coordinate_insertion_algorithm_through_adjacent_threshold_gap_and_source_kernel_G
      25: degree_drop_event_envelope_and_gap_telescoping_double_count
    next: [1,12,20]
  new_self_checked_claims:
    - R20-F0111-E1_degree_drop_envelope
    - R20-F0111-NOGO2_pure_degree_drop_family_fails_uniform_budget
    - R20-F0111-G4_exact_gap_insertion_identity
    - R20-F0111-G5_gap_update_identity
    - R20-F0111-RED1_uniform_gap_certificate_implies_full_problem_10_9
  audits:
    independent: NONE
    closure: NONE
  remaining_obligation: universal_positive_multilinear_certificate_or_dual_obstruction_for_D_mj_log_Zj_over_Zjminus1
  evidence:
    current_I0100_source_checked: 2026-09-18
    Talagrand_original_source_checked: 2026-09-18
    F0111_current_literature_bounded_search: 2026-09-18
    F0111_direct_claim_fetch: 404_at_pre_report_check
    neighboring_F0111_R15_work_read: true
  shared_root_edits: NONE
  peer_track_edits: NONE
  checker_created: false
  closure_claim: false
```

No email/Gmail, Drive, public posting, purchase, paid compute, permission change, scheduler change, shared-root edit, or peer-track edit was performed.

**End of complete run report.**
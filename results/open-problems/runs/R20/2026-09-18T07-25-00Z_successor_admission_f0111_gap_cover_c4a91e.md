Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO ADMISSION MOVEMENT: `E_ready: 0 -> 0`; retired I0100 remains frozen at `p_max=1213`, retirement count `6`; methods #1 CHANGE THE CATEGORY, #12 FIND WHAT IS CONSERVED, #20 FIND WHY THE ALGORITHM FAILS.**

# R20 successor admission — F0111 gap conservation, fractional-cover envelopes, and failure of standalone gap certificates

Date checked: 2026-09-18 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Worker: R20, CLOSABLE OUTSIDE.

## 1. Continuity, source status, ownership and exclusions

I did **not** reopen Randomstrasse101 Conjecture 26 / intake I0100. Its mandatory six-unchanged-run handoff remains controlling, and the retirement count remains frozen at `6` rather than being incremented by successor-screening work.

The original fixed metric remains

`p_max = 1213`,

with the complete retained exact primal/dual certified prime set

`{5,13,17,29,41,181,241,317,421,541,601,661,1009,1021,1033,1049,1061,1093,1201,1213}`.

No numerical SDP value is promoted to an exact certificate. No new finite Paley claim is made in this report.

The source graph/normalization is preserved exactly. For prime `p = 1 mod 4`, let `Q` be the nonzero squares in `F_p`; `G_{p,1}` is the Paley graph induced on `Q`, equivalently after choosing a primitive root `g`, putting `alpha=g^2` and identifying `Q` with `Z_n`, `n=(p-1)/2`,

`G_{p,1}=Cay(Z_n,S_p)`,

`S_p={d != 0 : alpha^d-1 is a nonzero square mod p}`.

The target is the same clique-bounding normalization

`T_p = theta(complement G_{p,1}) ~ sqrt(p/2)`,

not theta of the graph itself, not Schrijver theta-prime, not degree-two localization, and not the ETF/degree-four SOS problems owned by other tracks.

Fresh public check dated 2026-09-18: the current Jig root `https://jig.so/p/7` still labels the exact Conjecture 26 root **Open** and explicitly says the finite counterexample to the pointwise bound does not bear on the surviving asymptotic. The later kernel-checked sufficient reductions shown there do not prove the root asymptotic. Thus I0100 remains `OPEN / PARTIAL / RETIRED-HANDOFF`.

I recovered before new work:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, `QUEUE.md`;
- `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`;
- newest own report `runs/R20/2026-09-18T06-08-00Z_successor_admission_f0111_gap_insertion_4d7a2c.md`;
- current neighboring F0111 work in R15;
- coordinator status `operations/task_health/runs/2026-09-18T055500Z/status.md`;
- current NM13-12 admission screen `proofnet24/NM13-12/runs/2026-09-18/2026-09-18T06-06-00Z__successor-admission-screen-1.md`.

A direct current probe of `operations/claims/F0111.md` again returned 404. That does **not** make F0111 READY: the current NM13-12 screen explicitly classifies F0111 as an active pending lead / NOT READY because R15 and R20 are already probing it as successor mathematics, and the coordinator still reports no newly promoted free READY target in its bounded pass. I therefore create no ownership claim.

The admission metric remains

`E_ready = number of newly verified source-clean, current-open, ownership-clear, genuinely CLOSABLE OUTSIDE successors found in this bounded run`.

Before: `0`. After: `0`.

## 2. F0111 source fidelity and dated literature check

I continued Michel Talagrand, *Are Many Small Sets Explicitly Small?*, STOC 2010, Problem 10.9 (`F0111`) only as **successor-screening mathematics**, not as an admitted R20 target.

The source asks whether there is a universal `gamma>0` such that every threshold up-class

`A_{n,k}={X subset [n] : |X|>=k}`

belongs to `C_gamma`. Writing

`F_{n,k}(t)=-log P_t(N<k)`,  `P(X_i=1)=1-exp(-t_i)`,

membership means that for every base point `q>=0` there is a multilinear polynomial

`P(t)=sum_{empty != I subset [n]} beta_I t_I`,  `beta_I>=0`,

with

`F_{n,k}(t)<=P(t)` for all `t>=0`

and

`P(gamma q)<=gamma F_{n,k}(q)`.

The primary PDF `https://michel.talagrand.net/preprints/small.pdf` was rechecked today. Its lines around Problem 10.9 state exactly the threshold-class question. The same source's Theorem 10.7 gives a universal positive multilinear majorant for the two-variable kernel

`G(u,v)=-log(exp(-u)+exp(-v)-exp(-u-v))`

of the form `a u+b v+cuv`, with a source-budget inequality at the base point. The source also proves stability of `C_gamma` under the disjoint-block composition of Proposition 10.5.

Dated searches on 2026-09-18 included the exact Talagrand title/Problem 10.9, `C_gamma`, threshold classes, p-small/weakly-p-small, and later threshold/down-set work. They recovered the ACM 2010 source, DeMarco--Kahn's 2015 related note and later p-small/down-set-threshold literature, but I did not recover a later paper explicitly claiming the exact heterogeneous-`q`, positive-polynomial-majorant Problem 10.9. This is bounded negative evidence only, not a worldwide openness or novelty certificate.

## 3. Starting point carried forward: exact threshold gaps

Put

`y_i=exp(t_i)-1`,

`e_r=e_r(y_1,...,y_n)`,

`Z_j=sum_{r=0}^j e_r`,  with `Z_0=1`.

The exact threshold hazard is

`F_{n,k}(t)=sum_i t_i-log Z_{k-1}`.                            (3.1)

For `1<=j<=n`, define the adjacent-threshold gap

`D_{n,j}(t):=F_{n,j}(t)-F_{n,j+1}(t)=log(Z_j/Z_{j-1})`.       (3.2)

The preceding R20 run proved the exact insertion identity, for `k>=2`,

`F_{m+1,k}(x,t)=F_{m,k}(t)+G(x,D_{m,k-1}(t))`,              (3.3)

and proposed a conditional route: if all the gaps had standalone uniform `C_gamma`-style positive certificates, then Theorem 10.7 could be composed with them.

The purpose of this run is to understand the gaps themselves rather than make another whole-`F` majorant.

---

# 4. Method #12 — FIND WHAT IS CONSERVED: the gap profile is decreasing and its total mass is exactly `sum t_i`

### R20-F0111-GAP1 — log-concavity and conservation theorem

For every `t>=0`,

`D_{n,1}(t)>=D_{n,2}(t)>=...>=D_{n,n}(t)>=0`,                (4.1)

and

`sum_{j=1}^n D_{n,j}(t)=sum_{i=1}^n t_i`.                    (4.2)

Consequently, for every `1<=j<=n`,

`D_{n,j}(t) <= (1/j) sum_i t_i`.                              (4.3)

### Proof

The elementary-symmetric sequence `(e_r)` is log-concave by Newton's inequalities. I spell out the only consequence needed for the partial sums `Z_j`.

We have

`Z_j^2-Z_{j-1}Z_{j+1}=e_j Z_j-e_{j+1}Z_{j-1}`.              (4.4)

If `e_j=0`, then also `e_{j+1}=0`, so the right side is zero. Otherwise put

`c=e_{j+1}/e_j`.

Log-concavity of `(e_r)` says the ratios `e_r/e_{r-1}` are nonincreasing, hence for each `1<=r<=j`,

`e_r >= c e_{r-1}`.

Summing gives `Z_j>=c Z_{j-1}` (in fact with the extra positive `e_0` slack), so

`e_j Z_j >= e_{j+1}Z_{j-1}`.

Thus `(Z_j)` is log-concave. Therefore the ratios `Z_j/Z_{j-1}` are nonincreasing, which is exactly (4.1) after taking logs.

The conservation law telescopes:

`sum_j D_{n,j}=log Z_n-log Z_0=log Z_n`.

But

`Z_n=sum_{r=0}^n e_r(y)=prod_i(1+y_i)=prod_i exp(t_i)=exp(sum_i t_i)`,

which proves (4.2). Since the first `j` gaps are each at least `D_{n,j}`,

`j D_{n,j} <= sum_{ell=1}^j D_{n,ell} <= sum_i t_i`,

proving (4.3). QED.

This is an exact structural invariant, not a numerical observation. I make no novelty claim for the Newton/log-concavity mechanism; the useful point here is that it identifies the precise conserved quantity in the threshold-gap dynamics.

---

# 5. Method #1 — CHANGE THE CATEGORY: all nonnegative linear gap majorants form a fractional hypergraph-cover polyhedron

The conserved profile suggests treating a gap majorant as a covering problem rather than as a probability inequality.

First record the exact saturation monotonicity.

Suppose a new coordinate with `y=exp(x)-1` is added to a configuration. Write

`R_j=Z_j/Z_{j-1}=exp(D_j)`.

For `j>=2`, the new ratio is

`R'_j=(R_j+y)/(1+y/R_{j-1})
     =R_{j-1}(R_j+y)/(R_{j-1}+y)`.                           (5.1)

By (4.1), `R_{j-1}>=R_j`, so the right side is nondecreasing in `y`, from `R_j` at `y=0` to `R_{j-1}` as `y->infinity`. For `j=1`, monotonicity is immediate from `Z_1'=Z_1+y`.

Therefore every gap is nondecreasing in each coordinate, and if `B` has `r<j` coordinates, sending those coordinates to infinity yields

`D_{n,j}(t) <= D_{n-r,j-r}(t_{B^c})
             <= (1/(j-r)) sum_{i notin B} t_i`.              (5.2)

The last inequality is (4.3) on the reduced configuration.

### R20-F0111-LIN1 — exact linear-envelope cone

Let

`L_a(t)=sum_i a_i t_i`,  `a_i>=0`.

Then

`D_{n,j}(t)<=L_a(t)` for every `t>=0`                         (5.3)

if and only if

`sum_{i in I} a_i >= 1` for every `I subset[n]` with `|I|=j`. (5.4)

Thus the cone of global nonnegative linear majorants of `D_{n,j}` is exactly the fractional vertex-cover polyhedron of the complete `j`-uniform hypergraph `K_n^(j)`.

### Necessity

Fix a `j`-set `I` and put `t=M 1_I`. Zero coordinates are irrelevant, and

`D_{n,j}(M1_I)=D_{j,j}(M1_j)
              =-log(1-(1-exp(-M))^j)
              =M-log j+o(1)`.                                (5.5)

If (5.3) holds, then

`M sum_{i in I}a_i >= M-log j+o(1)`.

Divide by `M` and let `M->infinity` to get (5.4).

### Sufficiency

Permute coordinates so

`a_1<=a_2<=...<=a_n`.

Condition (5.4) is then equivalent to

`a_1+...+a_j>=1`.                                             (5.6)

Put `s=sum_{i=1}^j a_i` and define

`c_i=a_i/s` for `i<=j`,

`c_i=a_j/s` for `i>j`.

Then `0<=c_i<=a_i`, `c_1<=...<=c_j`, the tail is constant, and

`sum_{i=1}^j c_i=1`.                                         (5.7)

Set `c_0=0` and for `k=1,...,j` define

`lambda_{k-1}=(j-k+1)(c_k-c_{k-1})`.                         (5.8)

These numbers are nonnegative and telescope to

`sum_{r=0}^{j-1}lambda_r=sum_{k=1}^j c_k=1`.                 (5.9)

For `0<=r<j`, let the step vector `v^(r)` have its first `r` coordinates zero and every remaining coordinate equal to `1/(j-r)`. Equation (5.2), with `B={1,...,r}`, says

`D_{n,j}(t)<=v^(r) dot t`                                     (5.10)

for every `t>=0`.

The coefficients in (5.8) were chosen so that

`c=sum_{r=0}^{j-1}lambda_r v^(r)`;                            (5.11)

indeed the increment of coordinate `k` is exactly `lambda_{k-1}/(j-k+1)=c_k-c_{k-1}`. Hence (5.10), convexity and `a>=c` coordinatewise give

`D_{n,j}(t)<=c dot t<=a dot t`.

This proves sufficiency. QED.

### Exact optimal linear cost at a base point

Sort the base coordinates in decreasing order,

`q_(1)>=q_(2)>=...>=q_(n)>=0`.

By the rearrangement inequality we may pair the smallest feasible cover weights with the largest `q_i`; the preceding convex decomposition then shows that the minimum possible linear-envelope cost is

`tau_j(q)
 = min_{0<=r<j} [1/(j-r)] sum_{i=r+1}^n q_(i).`              (5.12)

Every candidate in (5.12) is attained by the saturation step majorant (5.2), so this is equality, not merely a bound.

This turns the best **linear** gap certificate into a closed-form fractional-cover optimization. The category change is useful even though it does not solve the source problem: there is no longer any reason to search numerically over linear coefficients.

### Small-scale no-go for linear-only gap certificates

For `j>=2` and `q=epsilon 1_n`,

`tau_j(q)=(n/j)epsilon`,                                      (5.13)

whereas from (3.2)

`D_{n,j}(epsilon 1_n)=binom(n,j)epsilon^j+O(epsilon^(j+1))`.  (5.14)

Thus for every fixed `gamma>0`, an all-linear gap certificate necessarily costs order `gamma epsilon` at `gamma q`, while the target budget is order `gamma epsilon^j`. It fails for sufficiently small `epsilon`.

So a successful gap mechanism, if one exists for `j>=2`, must genuinely interpolate between degree `j` near the origin and the fractional-cover linear envelope after saturation. This is the same degree-drop phenomenon seen for the whole threshold hazard, now in an exact LP language.

---

# 6. Method #20 — FIND WHY THE ALGORITHM FAILS: the previous standalone-gap reduction is impossible already at `D_1`

The most important diagnostic is sharper than the linear no-go above. The first gap cannot satisfy a standalone `C_gamma` condition **even with arbitrary positive multilinear degree**.

From (3.2),

`D_{n,1}(t)=log Z_1
            =log(1+sum_i(exp(t_i)-1))`.                      (6.1)

### R20-F0111-NOGO3 — `D_1` is not in any positive `C_gamma`-type class at an interior base point

Fix any `gamma>0` and any base point `q` having at least two positive coordinates. There is no multilinear polynomial

`P(t)=sum_{empty != I} beta_I t_I`,  `beta_I>=0`,

such that both

`D_{n,1}(t)<=P(t)` for all `t>=0`                              (6.2)

and

`P(gamma q)<=gamma D_{n,1}(q)`.                               (6.3)

### Proof

On the `i`-th coordinate axis, `t=s e_i`, equation (6.1) gives exactly

`D_{n,1}(s e_i)=s`.                                           (6.4)

All multilinear monomials of degree at least two vanish on that axis, so (6.2) forces the singleton coefficient

`beta_{ {i} }>=1`                                             (6.5)

for every coordinate `i`.

Therefore

`P(gamma q)>=gamma sum_i q_i`.                                (6.6)

If at least two coordinates of `q` are positive, putting `y_i=exp(q_i)-1` gives the strict product inequality

`1+sum_i y_i < prod_i(1+y_i)=exp(sum_i q_i)`,                 (6.7)

because at least one positive cross term is missing on the left. Taking logs,

`D_{n,1}(q)<sum_i q_i`.                                       (6.8)

Equations (6.6)--(6.8) contradict (6.3). QED.

In fact the exact infimum of `P(gamma q)` over all global positive multilinear majorants of `D_1` is `gamma sum_i q_i`, achieved by the simple global majorant `P(t)=sum_i t_i` from (4.3). Thus the obstruction is exact, not an artefact of a poor linear search.

### Consequence for the previous R20 reduction

The preceding report's conditional statement `R20-F0111-RED1` was logically correct: **if** every gap `D_{m,j}` possessed a standalone uniform source-budget certificate, then the threshold problem would follow by composing with Talagrand's two-variable kernel theorem. This run proves that the stated hypothesis is false already for `j=1`.

Therefore that all-gap route cannot prove Problem 10.9 as written.

This does **not** refute F0111. It identifies the missing architecture:

- the `k=2` threshold insertion uses `D_{m,1}` and therefore cannot pay for the gap as an independent `C_gamma` object;
- any successful `k=2` induction must exploit the **outer kernel's slack** in `G(x,D_1)` so that the unavoidable standalone overpayment `sum q_i-D_1(q)` is absorbed by the outer coefficients rather than charged directly;
- for fixed `k>=3`, the insertion formula only needs `D_{m,k-1}` with index at least two, so a refined standalone-gap theorem for `j>=2` could still be useful, but it would have to be multiscale by (5.13)--(5.14).

The precise next analytic object is therefore no longer “prove `D_j in C_gamma` for every `j`.” It is:

`Find a q-adaptive positive polynomial Q>=D_{m,1} (or a direct majorant of G(x,D_{m,1})) whose excess cost is weighted by the b/c coefficients in Talagrand's outer certificate strongly enough to fit the whole F_{m+1,2} budget.`

Equivalently, for the difficult `k=2` case one should optimize the **composition**

`F_{m,2}(t)+R(x,Q(t))`,

not optimize `Q` in isolation. This is the first route in the current F0111 chain that explicitly uses the fact that the obstruction and the rescue live at different levels of the exact insertion formula.

---

# 7. What moved and what did not

The source-admission metric did not move:

`E_ready: 0 -> 0`.

I0100 did not move and was not attacked:

`p_max: 1213 -> 1213`, retirement count still `6`.

F0111 remains

`OPEN-LOOKING / ACTIVE PENDING LEAD / HARD-LEANING / NOT CLOSABLE-READY / NOT CLAIMED`.

The mathematical screening did move in three exact ways:

1. the gap profile is now known to be decreasing with the exact conserved total `sum_i t_i`;
2. **all** global nonnegative linear majorants of every gap are classified exactly by the complete-uniform-hypergraph fractional-cover polyhedron, with closed-form optimal base cost (5.12);
3. the previous all-gap `C_gamma` reduction is now rigorously eliminated at `D_1`, showing that the `k=2` case requires outer-kernel-weighted composition rather than standalone gap certification.

These are labeled **SELF_CHECK_ONLY**. No independent fleet audit is claimed, and none of them closes or refutes Talagrand Problem 10.9.

No finite exhaustive claim was made, so I did not manufacture an exact-arithmetic checker merely to certify algebraic identities. The validation portion of this run was source/readback checking rather than another unchanged finite certificate.

## 8. Prior-art / folklore qualification

The use of Newton inequalities and log-concavity of elementary symmetric polynomials is classical. The identification of inequalities (5.4) with the fractional vertex-cover polyhedron of `K_n^(j)` is also standard covering language once the exact gap saturation bound is known. I therefore make **no novelty claim** for those component mechanisms.

The potentially useful contribution of this run is the way these standard mechanisms fit the exact Talagrand threshold-gap object and the explicit `D_1` route obstruction. A publication-level novelty statement would require a dedicated citation-graph search well beyond today's bounded source/current-status check.

## 9. Model / scheduler-control boundary

The actual model self-identifies as GPT-5.6 Sol. No authenticated reasoning-effort telemetry is exposed, so the reasoning level is UNVERIFIED; I do not claim GPT-6 maximum.

The current implementation record and current coordinator report agree that the exposed task-management surface provides title/prompt, schedule/timing mode and enabled state, but **no binding model-family selector, no reasoning-effort selector, no authenticated completed-run model receipt, and no guaranteed one-hour duration field**. Therefore the requested GPT-6/maximum setting remains prompt-only in this surface.

The historical P26 `You cannot modify this task` response was an authorization-context boundary. Repository history records a later successful P26 update from another authorized context. The lawful workaround is the owning/admin-authorized scheduler surface, supported ownership transfer, or platform support; duplicating a task or bypassing permissions is not a valid workaround. I made no scheduler or permission changes.

## 10. Next methods

If F0111 remains the active admission probe next run, use a different triple:

- **#2 ATTACK THE NEGATION FIRST** — optimize a dual measure against the exact `k=2` insertion/composition rather than against `D_1` alone;
- **#14 FIND THE GROUP ACTING** — exploit permutation symmetry only after freezing the heterogeneous base-point order type, so the quotient retains the saturation pattern;
- **#29 ADD THE POINTS AT INFINITY** — compactify each coordinate by `p_i=1-exp(-t_i)` and treat saturated faces and the small-activity face in one boundary-recursion theorem.

Do not re-run the standalone all-gap `C_gamma` route; NOGO3 has killed it at `j=1`.

## 11. Structured ledger_delta

```yaml
ledger_delta:
  worker: R20
  allocation: CLOSABLE_OUTSIDE
  repository: yspennstate/math-open-problems
  branch: master
  model_actual: GPT-5.6_Sol
  reasoning_actual: UNVERIFIED
  predecessor:
    source_id: I0100
    source: Randomstrasse101_Conjecture_26_Paley_one_localization
    status: OPEN_PARTIAL_RETIRED_HANDOFF_DO_NOT_REOPEN
    metric_name: largest_prime_matching_exact_primal_dual
    metric_before: 1213
    metric_after: 1213
    retirement_unchanged_count: 6
    retained_prime_set: [5,13,17,29,41,181,241,317,421,541,601,661,1009,1021,1033,1049,1061,1093,1201,1213]
  successor_gate:
    metric_name: E_ready
    before: 0
    after: 0
    status: SUCCESSOR_ADMISSION_REQUIRED
    candidate_probe: F0111
    candidate_source: Talagrand_STOC_2010_Problem_10_9
    candidate_disposition: ACTIVE_PENDING_LEAD_HARD_LEANING_NOT_CLOSABLE_READY_NOT_CLAIMED
    claim_created: false
  tried_moves: [1,12,20]
  mathematical_screening_progress:
    - GAP1_decreasing_gap_profile_and_exact_total_mass
    - LIN1_exact_fractional_complete_hypergraph_cover_cone_for_linear_gap_majorants
    - exact_weighted_linear_cost_tau_j_formula
    - NOGO3_D1_has_no_standalone_positive_Cgamma_certificate_at_interior_base_points
  status: OPEN_PARTIAL_SCREENING_ONLY
  remaining_obligation: >-
    Admit a lawful source-clean current-open ownership-clear genuinely CLOSABLE
    outside successor. If F0111 continues as a screening lead, attack the k=2
    insertion at the composed outer-kernel level; do not require D1 itself to
    satisfy a standalone C_gamma budget. For j>=2, any gap certificate must be
    multiscale, interpolating degree j near zero with the fractional-cover
    linear envelope on saturated faces.
  evidence:
    - runs/R20/2026-09-18T06-08-00Z_successor_admission_f0111_gap_insertion_4d7a2c.md
    - runs/R15/20260918_0612Z_successor_admission_f0111_fkg_sendov_g51a.md
    - proofnet24/NM13-12/runs/2026-09-18/2026-09-18T06-06-00Z__successor-admission-screen-1.md
    - operations/task_health/runs/2026-09-18T055500Z/status.md
    - https://jig.so/p/7
    - https://michel.talagrand.net/preprints/small.pdf
  audits:
    current_run: SELF_CHECK_ONLY
    P26: NOT_REQUESTED_NO_CLOSURE_CLAIM
    second_other_track: NOT_REQUESTED_NO_CLOSURE_CLAIM
  next_moves: [2,14,29]
  shared_roots_edited: false
  peer_files_edited: false
  schedules_modified: false
  email_or_drive_used: false
```

**NO I0100 CLOSURE CLAIM. NO F0111 CLAIM. R20 remains `SUCCESSOR_ADMISSION_REQUIRED`.**
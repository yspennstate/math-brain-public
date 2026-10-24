Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO ADMISSION MOVEMENT: `E_ready: 0 -> 0`; retired I0100 remains frozen at `p_max=1213`, retirement count `6`; methods #1 CHANGE THE CATEGORY, #12 FIND WHAT IS CONSERVED, #20 FIND WHY THE ALGORITHM FAILS.**

# R20 successor admission — F0111 reverse-hazard conservation and gap-certificate no-go

Date checked: 2026-09-18 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Worker: R20, CLOSABLE OUTSIDE.

## 1. Continuity, ownership, exclusions, and current source

I did **not** reopen Randomstrasse101 Conjecture 26 / intake I0100. The mandatory six-unchanged-run handoff remains controlling. Its frozen metric is

`p_max = 1213`,

with the full retained exact primal/dual certificate set

`{5,13,17,29,41,181,241,317,421,541,601,661,1009,1021,1033,1049,1061,1093,1201,1213}`.

The canonical claim `operations/claims/I0100.md` still identifies R20 as the historical owner and fixes the source normalization, while the newer immutable R20 handoff reports retire active attack after six unchanged runs. I preserve both facts; I do not interpret the older claim file as permission to restart the source.

Fresh current-source search on 2026-09-18 recovered the current Jig root `https://jig.so/p/7`, still titled **Open** and asking exactly whether the Lovasz theta of the complement of the Paley 1-localization is asymptotic to `sqrt(p/2)`. The page contains kernel-checked sufficient reductions but does not claim the asymptotic. Thus I0100 remains `OPEN / PARTIAL / RETIRED-HANDOFF`; its retirement count stays `6` and is not incremented.

Before new work I reread/recovered:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/new_methods_2026-09-16/DEPLOYMENT.md`;
- newest own report `runs/R20/2026-09-18T06-08-00Z_successor_admission_f0111_gap_insertion_4d7a2c.md`;
- neighboring R15 F0111 reports through `runs/R15/20260918_0612Z_successor_admission_f0111_fkg_sendov_g51a.md`;
- newest coordinator reconciliation `operations/task_health/runs/2026-09-18T065500Z/status.md` at commit `f6a8a366a534ab3dbea1764c81946ac5837d9503`.

That coordinator pass still found no race-safe target crossing every source/current-open/ownership/CLOSABLE gate. Several attractive sources acquired owners in the same time window, so free inventory shrank rather than grew. A direct pre-report fetch of `operations/claims/F0111.md` still returned 404. This is bounded repository evidence only; it is not automatic admission.

The admission metric remains

`E_ready = number of newly verified source-clean, current-open, ownership-clear, genuinely CLOSABLE OUTSIDE successors found in this bounded run`.

Before: `0`. After: `0`.

## 2. F0111 source and status

I continued Michel Talagrand, *Are Many Small Sets Explicitly Small?*, STOC 2010, Problem 10.9 (`F0111`) only as **successor-screening mathematics**, not as an admitted R20 target.

For the threshold up-class

`A_{n,k}={X subset [n] : |X|>=k}`,

write

`F_{n,k}(t)=-log P_t(N<k)`,

where `N=sum_i X_i` and `P(X_i=1)=1-exp(-t_i)` independently.

Talagrand's Definition 10.1 asks whether one universal `gamma>0` has the property that, for every base point `q>=0`, there is a multilinear polynomial with nonnegative coefficients and no constant term,

`P(t)=sum_{empty != I subset [n]} beta_I t_I`, `beta_I>=0`,

such that

`F_{n,k}(t)<=P(t)` for all `t>=0`,

and

`P(gamma q)<=gamma F_{n,k}(q)`.

The original source PDF was checked at Problem 10.9 and Theorem 10.7. Fresh dated searches used the exact title plus `Problem 10.9`, `C_gamma`, `cardinality threshold`, `positive polynomial majorant`, and nearby `p-small` terminology. They recovered the original STOC source and related DeMarco--Kahn (2015) and Frankston--Kahn--Park (2022) work, but no accessible later theorem explicitly resolving this exact heterogeneous-`q` positive-polynomial statement. This is bounded negative evidence, not a novelty certificate.

The previous R20 run established, with `y_i=exp(t_i)-1` and

`Z_j(y)=sum_{r=0}^j e_r(y)`, `Z_{-1}=0`,

that

`F_{m,k}(t)=sum_i t_i-log Z_{k-1}(y)`,

and introduced the adjacent-threshold gaps

`D_j(t):=F_{m,j}(t)-F_{m,j+1}(t)=log(Z_j/Z_{j-1})`, `1<=j<=m`.

It also proved the exact insertion identity

`F_{m+1,k}(x,t)=F_{m,k}(t)+G(x,D_{k-1}(t))`,

where

`G(u,v)=-log(exp(-u)+exp(-v)-exp(-u-v))`.

The previous report proposed a conditional route: if every gap `D_j` itself had a uniform Talagrand-style positive multilinear certificate, then Theorem 10.7 for `G` would close the threshold problem. This run identifies the exact invariant behind the gap dynamics **and proves that separate-gap certificate route impossible already at `j=1`**.

All claims below are `SELF_CHECK_ONLY`: complete arguments are written here, but no independent fleet audit is claimed.

## 3. Method #1 — CHANGE THE CATEGORY: gaps are reverse hazards / uniform-matroid partition ratios

The quantity

`1-exp(-D_j)=1-Z_{j-1}/Z_j=e_j(y)/Z_j(y)`

has the probabilistic interpretation

`1-exp(-D_j)=P_t(N=j | N<=j)`.

Thus `D_j` is the logarithmic reverse-hazard transform of the Poisson-binomial lower tail.

Equivalently, `Z_j` is the weighted independence-set partition function of the uniform matroid `U_{j,m}` evaluated at activities `y_i`, and `D_j=log(Z_j/Z_{j-1})` is the log ratio of consecutive truncation partition functions.

This change of language is useful because the elementary-symmetric sequence is log-concave and the coordinate-insertion rule for `Z_j` is exact and subtraction-free.

### R20-F0111-C1 — the gap ladder is ordered

For every `t>=0`,

`D_1(t)>=D_2(t)>=...>=D_m(t)>=0`.                       (C1)

#### Proof

The elementary symmetric sequence `e_r(y)` is log-concave for nonnegative `y` (Newton inequalities), so the ratios `e_{r+1}/e_r` are nonincreasing whenever the denominators are positive; zero cases follow by continuity.

It suffices to prove the cumulative sequence `Z_j=sum_{r<=j}e_r` is log-concave. We have

`Z_j^2-Z_{j-1}Z_{j+1}=e_j Z_j-e_{j+1}Z_{j-1}`.

For every `0<=r<=j-1`, ratio monotonicity gives

`e_{j+1} e_r <= e_j e_{r+1}`.

Summing over `r=0,...,j-1`,

`e_{j+1} Z_{j-1} <= e_j sum_{s=1}^j e_s <= e_j Z_j`.

Hence `Z_j^2>=Z_{j-1}Z_{j+1}`, so `Z_j/Z_{j-1}` is nonincreasing, which is exactly (C1). QED.

I make no novelty claim for this log-concavity mechanism; it is consistent with standard ultra-log-concavity facts for Poisson-binomial distributions and matroid independence polynomials.

## 4. Method #12 — FIND WHAT IS CONSERVED: coordinate insertion is a conservative flux

Insert one new coordinate of intensity `x>=0`, and write

`z=exp(x)-1`.

Use superscript `+` for the enlarged `(m+1)`-coordinate system. Then exactly

`Z_j^+=Z_j+z Z_{j-1}`.                                      (4.1)

Set

`a_j:=Z_j/Z_{j-1}=exp(D_j)`,

`s_j:=a_j-1`,

and define the residual free-energy increment

`R_j:=log(Z_j^+/Z_j)=log(1+z/a_j)`, `R_0:=0`.               (4.2)

### R20-F0111-C2 — barycentric odds update

The inserted odds satisfy

`a_j^+=a_{j-1}(a_j+z)/(a_{j-1}+z)`,                         (4.3)

and therefore

`s_j^+ = [a_{j-1}s_j + z s_{j-1}]/(a_{j-1}+z).`             (4.4)

Because (C1) gives `s_{j-1}>=s_j`, equation (4.4) shows that the new odds `s_j^+` lie in the old interval `[s_j,s_{j-1}]`. Insertion therefore performs an exact adjacent barycentric averaging on the reverse-hazard odds.

#### Proof

Divide (4.1) for `j` by (4.1) for `j-1`:

`a_j^+=(Z_j+zZ_{j-1})/(Z_{j-1}+zZ_{j-2})
      =a_{j-1}(a_j+z)/(a_{j-1}+z)`.

Subtract one to obtain (4.4). QED.

### R20-F0111-C3 — discrete conservation law

For every `1<=j<=m`,

`D_j^+-D_j = R_j-R_{j-1}.`                                  (4.5)

Also, for every threshold `k`,

`F_{m+1,k}(x,t)-F_{m,k}(t)=x-R_{k-1}.`                      (4.6)

For `j>=2`, putting

`Delta_j:=D_{j-1}-D_j>=0`,

we furthermore have the subtraction-free form

`R_j-R_{j-1}=G(R_j,Delta_j)`.                               (4.7)

Finally,

`R_j=x-G(x,D_j)`,                                           (4.8)

so each inserted intensity splits **exactly** as

`x = G(x,D_j)+R_j`.                                         (4.9)

#### Proof

Equation (4.5) is simply

`(log Z_j^+-log Z_{j-1}^+)-(log Z_j-log Z_{j-1})
 =log(Z_j^+/Z_j)-log(Z_{j-1}^+/Z_{j-1})`.

Equation (4.6) follows from `F=sum t_i-log Z_{k-1}` and (4.2).

For (4.8), using `a_j=exp(D_j)` and `z=exp(x)-1`,

`G(x,D_j)=log[a_j(1+z)/(a_j+z)]`,

hence

`x-G(x,D_j)=log[(a_j+z)/a_j]=R_j`.

For (4.7), `exp(-R_j)=a_j/(a_j+z)` and `exp(-Delta_j)=a_j/a_{j-1}`. Substitution into the definition of `G` gives

`G(R_j,Delta_j)
 =log[a_{j-1}(a_j+z)/(a_j(a_{j-1}+z))]
 =R_j-R_{j-1}`.

QED.

Equations (4.5)--(4.9) are the strongest structural information found in this screening line so far. The gap vector evolves by a **discrete conservative flux**: `R_j` is the flux across level `j`, while `D_j^+-D_j` is its discrete gradient. The threshold hazard pays only the boundary flux `x-R_{k-1}`. Any proof architecture that estimates every gap or every insertion increment separately destroys exactly the cancellation that (4.5) preserves.

## 5. Method #20 — FIND WHY THE ALGORITHM FAILS: separate gap certification is impossible

The previous R20 report's conditional implication was correct, but its hypothesis is impossible. The obstruction appears at the first gap.

### R20-F0111-NOGO3 — `D_1` has no Talagrand-style positive certificate at a homogeneous positive base

For `m>=2`,

`D_1(t)=log(1+sum_i(exp(t_i)-1)).`                           (5.1)

Fix the base point `q=(1,...,1) in R_+^m`. For **every** `gamma>0`, there is no multilinear polynomial with nonnegative coefficients and no constant term such that simultaneously

`D_1(t)<=P(t)` for all `t>=0`,                              (5.2)

and

`P(gamma q)<=gamma D_1(q)`.                                 (5.3)

#### Proof

Restrict (5.2) to the `i`-th coordinate axis, `t=s e_i`. Equation (5.1) gives exactly

`D_1(s e_i)=s`.

Because `P` is multilinear and has no constant term, on that axis only the singleton coefficient survives:

`P(s e_i)=beta_{ {i} } s`.

Thus `beta_{ {i} }>=1` for every `i`. Positivity then forces

`P(gamma q)>=gamma sum_i beta_{ {i} }>=gamma m`.            (5.4)

But

`D_1(q)=log(1+m(e-1))<m` for `m>=2`; indeed

`1+m(e-1)<e^m=(1+(e-1))^m`

by the strict binomial expansion. Hence (5.4) contradicts (5.3). QED.

Therefore the previous sufficient reduction “certify every `D_{m,j}` and compose with Theorem 10.7” cannot possibly solve Problem 10.9. The implication remains mathematically valid, but its premise already fails for `j=1`.

## 6. A stronger failure theorem: even isolated insertion increments cannot have one universal certificate scale

One might try to avoid certifying `D_1` itself and certify only the insertion increment

`H_m(x,t):=G(x,D_1(t))`                                    (6.1)

as a positive object. This also fails uniformly.

### R20-F0111-NOGO4 — no universal `gamma` for isolated first-gap increments

There is no `gamma>0` such that for every `m` and every base point one can find a positive multilinear polynomial `Q` globally majorizing `H_m` and obeying the Talagrand budget at that same `gamma`.

#### Proof

Fix `gamma>0`. Let

`g0:=G(1,1)=-log(2e^{-1}-e^{-2})>0`

(`g0≈0.5101198743`).

Suppose `Q` is a positive multilinear global majorant for `H_m`. Write `a` for the coefficient of `x`, `b_i` for the coefficient of `t_i`, and `c_i` for the coefficient of `x t_i`.

On the slice with only `t_i=s` nonzero, (5.1) gives `D_1(s e_i)=s`, hence

`H_m(x,s e_i)=G(x,s)`.

Evaluating at `x=s=1` gives, for every `i`,

`a+b_i+c_i>=g0`.                                           (6.2)

Now use the base point

`x_0=m`, `t_0=(1,...,1)`.

At the scaled point, positivity of all other coefficients gives

`Q(gamma m, gamma 1_m)
 >= gamma m a + gamma sum_i b_i + gamma^2 m sum_i c_i`.     (6.3)

Choose `m>=1/gamma`. Then `gamma^2 m>=gamma`, and summing (6.2) yields

`Q(gamma m, gamma 1_m)
 >= gamma[m a+sum_i b_i+sum_i c_i]
 >= gamma m g0`.                                           (6.4)

On the other hand,

`H_m(m,1_m)=G(m,log(1+m(e-1)))
           <=log(1+m(e-1))`,                               (6.5)

because `G(u,v)<=v` for `u,v>=0`.

For fixed `gamma`, choose `m` still larger so that

`m g0>log(1+m(e-1))`.

Then (6.4)--(6.5) contradict the required budget

`Q(gamma m,gamma1_m)<=gamma H_m(m,1_m)`.

QED.

This theorem does **not** refute Talagrand Problem 10.9. It says something narrower and operationally important: a dimension-free proof cannot be an additive induction that gives each insertion increment its own source-style certificate and then sums the budgets. The obstruction is not merely a poor coefficient choice; every positive multilinear isolated-increment certificate has the same asymptotic overpayment.

## 7. What a successful proof now has to contain

The exact conservation law changes the target. A successful positive route must postpone positivity until **after** the gap fluxes have telescoped. It cannot separately certify

- every gap `D_j`, or
- every insertion increment `G(x,D_j)`.

The remaining constructive target is therefore:

> Build a **joint** positive multilinear certificate for the full threshold ladder, or an equivalent coupled state, so that coordinate insertion uses the conservative identities
> 
> `D_j^+-D_j=R_j-R_{j-1}` and `x=G(x,D_j)+R_j`,
> 
> and the Talagrand budget is enforced only after the residual flux terms telescope.

A useful equivalent viewpoint is that the `R_j` are logarithmic increments of consecutive uniform-matroid truncation partition functions. The desired certificate must exploit the shared `R_j` between neighboring threshold levels rather than upper-bound each one independently.

This is a sharper obligation than the previous report's gap-certificate premise. It also explains, in one mechanism, the earlier failures of pure degree `k`, single degree-drop envelopes, one-scale tangents, and separate-gap composition: all of those destroy the finite-scale cancellation visible in (4.5).

I did not find a source-level dual obstruction to F0111 itself, and I do not relabel the source as REFUTED. F0111 remains

`OPEN-looking / mathematically sharpened / HARD-leaning / NOT CLOSABLE-ready / NOT CLAIMED`.

## 8. Prior-art / nearest solved shape

Dated searches on 2026-09-18 included:

- exact Talagrand title + `Problem 10.9` + `C_gamma`;
- `Poisson binomial reverse hazard`, `reverse hazard rate`, and cumulative log-concavity;
- `uniform matroid independence polynomial` + log-concavity / Lorentzian;
- nearby `p-small` / threshold work.

The searches recovered standard Poisson-binomial recursion/log-concavity material and modern complete-log-concavity/Lorentzian results for matroid independence polynomials. These support treating (C1) as a standard-shape consequence, not as a novelty claim. They did **not** recover the exact conservative flux identities above packaged as a solution to Talagrand 10.9, nor a source-matching resolution of Problem 10.9. A negative search is not a novelty certificate.

The nearest source-solved mechanism remains Talagrand's own Theorem 10.7 for the two-variable kernel `G`, but NOGO3--NOGO4 show why applying that theorem independently at every gap/insertion cannot scale to the full threshold ladder.

## 9. Admission conclusion

No source inspected in this bounded pass satisfied all gates simultaneously:

1. exact outside source and source-matching scope;
2. current-open status after later-author/citing checks;
3. genuinely CLOSABLE full-source metric;
4. no canonical owner/reservation.

The newest coordinator reconciliation likewise leaves admission/report gaps explicit rather than manufacturing READY entries. Therefore

`E_ready = 0 -> 0`.

I created no successor claim, no finite checker, and no decorative artifact. The new results are general analytic identities/no-go theorems with complete proofs on the page; there is no finite computation whose exact output is load-bearing.

## 10. Model/control boundary

This run actually used **GPT-5.6 Sol**. Authenticated reasoning-effort telemetry is not exposed, so the reasoning level is **UNVERIFIED**.

The exposed scheduler/task-management surface still offers prompt/title, schedule or relative start, timing mode, enabled state, and ordinary task metadata. It exposes **no binding model-family selector, no reasoning-effort selector, no authenticated applied-model receipt, and no guaranteed full-hour execution control**. Thus `GPT-6 / maximum` remains a prompt request, not a setting this worker can certify or enforce.

The historical P26 `You cannot modify this task` response was authorization-context dependent: repository evidence records later successful P26 updating from another authorized context. The lawful workaround is the task-owning/admin-authorized product surface, supported ownership reassignment, or platform support. I did not duplicate tasks, bypass permissions, or change any scheduler state.

## 11. Next methods

Next run, if no newly admitted CLOSABLE successor appears first, use a fresh triple:

- **#2 ATTACK THE NEGATION FIRST:** search for a genuine F0111 dual obstruction that respects the new joint-flux structure rather than isolated gaps;
- **#14 FIND THE GROUP ACTING:** exploit permutation symmetry after sorting the base point into equal-activity blocks, looking for a finite block-state certificate without assuming homogeneous `q`;
- **#29 ADD THE POINTS AT INFINITY:** compactify activity coordinates by `p_i=1-exp(-t_i)` so saturated coordinates live on boundary faces and test whether the conservative flux admits a continuous certificate on the closed cube.

## 12. Structured ledger_delta

```yaml
ledger_delta:
  worker: R20
  allocation: CLOSABLE_OUTSIDE
  repository: yspennstate/math-open-problems
  branch: master
  original_source:
    id: I0100
    source: "Afonso S. Bandeira / Randomstrasse101 Conjecture 26"
    status: OPEN_PARTIAL_RETIRED_HANDOFF
    metric_name: largest_admissible_prime_with_matching_exact_primal_dual_certificates
    metric_before: 1213
    metric_after: 1213
    retirement_count_before: 6
    retirement_count_after: 6
    covered_primes: [5,13,17,29,41,181,241,317,421,541,601,661,1009,1021,1033,1049,1061,1093,1201,1213]
    current_source_checked: 2026-09-18
  admission:
    metric_name: E_ready
    metric_before: 0
    metric_after: 0
    unchanged_count: UNKNOWN
    status: SUCCESSOR_ADMISSION_REQUIRED
  screening_problem:
    id: F0111
    source: "Michel Talagrand, Are Many Small Sets Explicitly Small?, STOC 2010, Problem 10.9"
    disposition: OPEN_LOOKING_HARD_NOT_CLOSABLE_READY_NOT_CLAIMED
    ownership_check: "operations/claims/F0111.md returned 404 immediately before report; bounded evidence only"
    new_self_checked_results:
      - ordered_reverse_hazard_gap_ladder_C1
      - barycentric_odds_update_C2
      - conservative_flux_identity_C3
      - D1_positive_certificate_impossibility_NOGO3
      - isolated_increment_uniform_gamma_impossibility_NOGO4
  tried_moves: [1,12,20]
  next_moves: [2,14,29]
  remaining_obligation: "find a source-clean current-open ownership-clear genuinely CLOSABLE successor; for F0111 specifically, any successful positive route must use a joint/telescoping threshold-ladder certificate rather than separate gap or insertion certificates"
  evidence:
    - runs/R20/2026-09-18T06-08-00Z_successor_admission_f0111_gap_insertion_4d7a2c.md
    - runs/R15/20260918_0612Z_successor_admission_f0111_fkg_sendov_g51a.md
    - operations/task_health/runs/2026-09-18T065500Z/status.md
    - operations/claims/I0100.md
    - "current Jig #7 Open page for Randomstrasse101 Conjecture 26, checked 2026-09-18"
    - "Talagrand STOC 2010 original Problem 10.9 and Theorem 10.7, checked 2026-09-18"
  audits: []
  artifacts: NONE_NEW
  shared_root_edits: NONE
  scheduler_changes: NONE
```

**NO I0100 CLOSURE CLAIM. NO F0111 CLAIM. R20 remains `SUCCESSOR_ADMISSION_REQUIRED`.**

Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6/maximum was requested, but no authenticated applied-model/reasoning-effort telemetry is exposed, so GPT-6/maximum is not claimed. SUBSTANTIVE MOVEMENT: the Lyons--Pemantle--Peres parent problem remains OPEN, but the preceding adjacent-two-point defect wedge is extended to arbitrary finitely supported no-leaf offspring laws whose mean lies within `delta` of their minimum degree. If `d=min supp(nu)>=2`, `mu=E[nu]-d<=delta`, and `0<delta<=1`, then strict parent-bias decrease is proved on `0<=lambda<=d-delta`; moreover `ell'_lambda<=-delta/[2(d(d-1)+delta)]<0` on `1<=lambda<=d-delta`. Equivalently, child-bias speed has strictly positive derivative for `1/(d-delta)<=beta<=1`. No simulated sign is used.**

# NM13-05 T06 — mean-excess escape-tilt wedge beyond adjacent offspring laws

Date: 2026-09-20.  
Repository: private `yspennstate/math-open-problems`, branch `master`.  
Own root: `proofnet24/NM13-05/progress-tree-speed`.  
Parent target: T06 / P0066, Lyons--Pemantle--Peres monotonicity of biased-walk speed on a supercritical Galton--Watson tree without leaves.  
Status: **PARTIAL / OPEN parent; NEW RESTRICTED THEOREM CANDIDATE pending later independent review.**

## 1. Compact continuity handoff

The controlling instruction is `operations/PROGRESS20_2026-09-20.md`; current LIVE20 assigns NM13-05 to T06 by escape-probability/regeneration coupling, complementary to P01's analytic regeneration-derivative route.

Historical P0066 remains `attempted_unsolved`. Its earlier argument only observed that, for fixed offspring count `k`, the local radial drift

`(k-lambda)/(k+lambda)`

decreases with parent bias `lambda`. The obstruction was and remains that the environment seen from the walker changes with `lambda`; no sign for that measure-change term followed from local drift alone.

The immediate predecessor is

`proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T04-23-44Z__parametric-defect-budget-wedge.md`.

It proved, only for adjacent laws

`P(nu=d)=1-p,  P(nu=d+1)=p`,

that endpoint defect mass at most `delta` implies strict decrease through `lambda=d-delta`. The present run removes the adjacent-two-point restriction and replaces endpoint defect probability by a first-moment defect budget.

The latest complementary P01 report consumed is

`proofnet24/P01-progress-speed/runs/2026-09-20/2026-09-20T05-00-49Z__run-report.md`.

P01 proves a different analytic covariance theorem at minimum offspring one and records its previous broad bounded-support result for minimum at least two (for example every law `3<=nu<=44` through `lambda=2.01`). The present result instead uses branch-addition monotonicity of the Aidekon escape tilt plus a uniform quenched escape-elasticity bound; its endpoint depends on the **mean excess above the minimum degree**, not on the maximum support width.

The newest PROB10-06 state consumed remains the global `{2,3}` coupled-tilt work. Two failed routes recorded there remain relevant and are not retried: differentiating the static branch-addition ratio in the desired direction is false in general, and a central two-type first-generation contraction has Perron radius above one. The proof below differentiates the exact tilted mean instead and never differentiates the branch-addition inequality itself.

`POSTED.md` was checked through current repository search. No posted source-wide P0066 closure is recorded; restricted T06 theorems do not close the parent problem.

## 2. Frozen offspring assumptions and bias convention

Let `nu` have a **finitely supported** offspring law on positive integers and assume

`d := min supp(nu) >= 2`.                                      (2.1)

Thus there are no leaves and the Galton--Watson tree is automatically supercritical. Put

`m := E[nu]`,
`mu := m-d = E[nu-d]`.                                         (2.2)

Fix a parameter

`0 < delta <= 1`                                                (2.3)

and assume the new mean-defect condition

`mu <= delta`.                                                   (2.4)

Use parent bias `lambda`:

`P(parent | nu=k)=lambda/(lambda+k)`,
`P(each fixed child | nu=k)=1/(lambda+k)`.                      (2.5)

Increasing `lambda` pushes toward the root, so the target sign is `ell'_lambda<0`.

The Ben Arous--Fribergh--Sidoravicius child-bias convention is reciprocal:

`beta=1/lambda`.                                                (2.6)

Thus, where differentiable,

`v'(beta)=-ell'_{1/beta}/beta^2`.                               (2.7)

Because `lambda<=d-delta<d<=m`, every new point lies on the transient side.

## 3. Primary-source and current-literature recovery

Recovered/refreshed on 2026-09-20:

1. Ben Arous--Fribergh--Sidoravicius, arXiv:1111.5865, *A proof of the Lyons-Pemantle-Peres monotonicity conjecture for high biases*. The arXiv abstract states that in child-bias notation the speed is increasing for `beta>=717` on Galton--Watson trees without leaves.
2. He--Wang--Xiang, arXiv:1610.08151, published online 5 March 2025 as *The speed of a biased walk on a Galton--Watson tree without leaves is monotonic for low values of bias*, Journal of Applied Probability 62 (2025), 1044--1052. For minimum offspring `d>=2`, they prove strict parent-bias decrease on

   `0<=lambda<=d/(1+sqrt(1-1/d))`.                              (3.1)

   Their escape derivative estimate used below is the same inherited dependency already consumed in the predecessor: for `lambda<d`, if `B` is the quenched probability of escaping to infinity before hitting the parent and `U=-dB/dlambda`, then

   `0<=U<=B/(d-lambda)`.                                        (3.2)

3. The same regular-tree comparison used in the predecessor gives

   `B>=1-lambda/d`                                               (3.3)

   when every vertex has at least `d` children.
4. Bowditch--Tokushige give differentiability/analyticity results in the ballistic regime; these regularity results do not themselves provide the monotonicity sign.
5. Song--Liu (2026) treats regular trees, not genuinely random offspring laws.

Bounded fresh searches on 2026-09-20 for biased-walk speed monotonicity combined with minimum offspring, mean offspring, and offspring-distribution restrictions did not surface a checked theorem matching the mean-excess wedge below. This is bounded negative evidence only, not a novelty certificate.

## 4. Parent-problem before/after and demonstrated mechanism gain

### Parent problem

Before: **OPEN**.  
After: **OPEN**.

No all-law solution on the full transient interval is claimed.

### Restricted source-level scope before

NM13-05's strongest near-minimum-degree theorem was restricted to adjacent two-point laws `{d,d+1}`:

`p<=delta or 1-p<=delta  =>  strict decrease through lambda=d-delta`.  (4.1)

### Restricted source-level scope after

### Theorem A — arbitrary finite-support mean-excess wedge

Let `nu` be any finitely supported offspring law satisfying (2.1), and let `mu=E[nu]-d`. For every `0<delta<=1`, if

`mu<=delta`,                                                     (4.2)

then the parent-bias speed is strictly decreasing throughout

`0<=lambda<=d-delta`.                                           (4.3)

More sharply, on the new derivative segment

`1<=lambda<=d-delta`,                                           (4.4)

one has the explicit uniform bound

`ell'_lambda <= - delta/[2(d(d-1)+delta)] < 0`.                 (4.5)

Equivalently, in child-bias notation,

`v'(beta)>0  for  1/(d-delta)<=beta<=1`.                        (4.6)

The full monotonicity interval (4.3) is obtained by stitching (4.4) to the published He--Wang--Xiang low-parent-bias theorem on a segment extending past `lambda=1`.

### Concrete genuinely non-adjacent gain

Take

`P(nu=3)=99/100,  P(nu=13)=1/100`.                              (4.7)

Then `d=3`, `mu=1/10`, and Theorem A proves

`ell'_lambda <= -1/122 <0  for 1<=lambda<=29/10`,               (4.8)

and strict monotonicity on `0<=lambda<=29/10`. This law has support gap ten and was not covered by the predecessor's adjacent-family theorem. It also reaches substantially beyond the `lambda=2.01` broad `[3,44]` rectangle advertised in the latest P01 companion report.

Even very distant finite outliers are allowed if their first-moment cost is small; for example

`P(nu=3)=999/1000,  P(nu=103)=1/1000`                           (4.9)

has the same `mu=1/10` and receives the same `lambda<=2.9` conclusion.

### Demonstrated mechanism gain

The new mechanism is **escape-tilt stochastic domination**:

> the conditional Aidekon escape weight `c_k` is decreasing in the current offspring count `k`; therefore the escape-tilted offspring mean is never larger than the original offspring mean.

This removes the maximum-degree dependence from the previous endpoint argument. The derivative's entire environment-change term can then be charged to the tilted first moment `M-d`, which is at most the original mean defect `mu`. Thus the singular `1/(d-lambda)` escape sensitivity is paid by a **mean-excess budget**, not by a two-point mixture probability or a support-width bound.

This is complementary to P01's analytic pairwise-Gini/support-width certificate.

## 5. Exact Aidekon tilt for an arbitrary finite support

Work on `1<=lambda<d`. Conditional on current offspring count `k`, take iid copies

`B_0,...,B_k`

of the quenched escape probability `B`, and put

`S_k=sum_{i=0}^k B_i`,
`D_k=lambda-1+S_k`.                                              (5.1)

Define

`c_k := E[ S_k / ((k+1)D_k) ]`.                                 (5.2)

With `p_k=P(nu=k)`, set

`C := sum_k p_k c_k`,
`q_k := p_k c_k/C`,
`M := sum_k k q_k`.                                              (5.3)

The same symmetrized Aidekon speed representation used by the predecessor and by P01 reduces exactly to

`ell_lambda=(M-lambda)/(M+lambda)`.                              (5.4)

Therefore

`ell'_lambda=2(lambda M'-M)/(M+lambda)^2`.                       (5.5)

It is enough to prove `M-lambda M'>0`.

## 6. New lemma: branch addition makes `c_k` decreasing

For `lambda>1`, define

`phi(s)=s/(lambda-1+s)`.                                        (6.1)

Then `phi` is increasing, concave, and `phi(0)=0`. Let `x_1,...,x_n` be nonnegative and `S=sum_i x_i`. Concavity between `0` and `S` gives, for each `i`,

`phi(S-x_i) >= ((S-x_i)/S) phi(S)`                              (6.2)

when `S>0`. Summing gives

`sum_i phi(S-x_i) >= (n-1)phi(S)`.                              (6.3)

Apply this pointwise to `n=k+2` iid escape variables and take expectation. Every leave-one-out sum has the law of a `(k+1)`-branch sum, so

`(k+2) E[phi(S_{k+1})] >= (k+1) E[phi(S_{k+2})]`.               (6.4)

Dividing by `(k+1)(k+2)` yields

`c_k >= c_{k+1}`.                                               (6.5)

At `lambda=1`, every escape variable is positive and `phi(S)=1`, hence `c_k=1/(k+1)` directly, so (6.5) still holds.

Thus `k -> c_k` is decreasing for every `1<=lambda<d`.

## 7. Consequence: the escape tilt lowers the offspring mean

Let `K` have the original law `p_k`. From (5.3),

`M = E[K c_K]/E[c_K]`.                                          (7.1)

Since `K` is increasing in `k` while `c_k` is decreasing,

`Cov(K,c_K)<=0`.                                                 (7.2)

Therefore

`M<=E[K]=m=d+mu`,                                               (7.3)

and in particular

`0<=M-d<=mu`.                                                    (7.4)

This is the first transfer that was unavailable in the adjacent-only proof: arbitrary support gaps are compressed to one first-moment number.

## 8. Uniform logarithmic derivative budget for every conditioned degree

Let

`U_i=-dB_i/dlambda>=0`.

Differentiating (5.2), as in the predecessor, gives

`c'_k=-h_k`,                                                     (8.1)

where

`h_k := E[ (1/(k+1)) *`
`          sum_i (B_i+(lambda-1)U_i) / D_k^2 ]`.                 (8.2)

Put

`a_k:=h_k/c_k=-c'_k/c_k>=0`.                                   (8.3)

By (3.2),

`sum_i(B_i+(lambda-1)U_i)`
` <= S_k [1+(lambda-1)/(d-lambda)]`
` = S_k (d-1)/(d-lambda).                                       (8.4)

By (3.3), `B_i>=1-lambda/d`, and because `k>=d`,

`D_k`
` >= lambda-1+(d+1)(1-lambda/d)`
` = (d^2-lambda)/d`.                                            (8.5)

Hence

`E[S_k/D_k^2] <= d/(d^2-lambda) E[S_k/D_k]`.                    (8.6)

Combining (5.2), (8.2), (8.4), and (8.6) gives the **degree-uniform score bound**

`0<=a_k<=H_d(lambda)`,                                          (8.7)

where

`H_d(lambda):=d(d-1)/[(d-lambda)(d^2-lambda)]`.                 (8.8)

No maximum offspring degree appears.

## 9. New covariance compression: charge the derivative to `M-d`

Differentiate the tilted probabilities in (5.3). Since `c'_k/c_k=-a_k`,

`q'_k=q_k(-a_k+E_q[a_K])`.                                     (9.1)

Therefore

`M'=-Cov_q(K,a_K)`.                                              (9.2)

Let `(K,a_K)` and `(K',a_{K'})` be iid under the tilted law. The pairwise covariance identity gives

`M' = (1/2) E[(K-K')(a_{K'}-a_K)]`.                             (9.3)

Using only `0<=a_k<=H_d(lambda)`,

`M'`
` <= (H_d(lambda)/2) E|K-K'|`.                                 (9.4)

Because `K,K'>=d`,

`|K-K'| <= (K-d)+(K'-d)`.                                      (9.5)

Thus

`M'<=H_d(lambda)(M-d)`.                                         (9.6)

Finally (7.4) gives the source-level first-moment bound

`M'<=H_d(lambda) mu`.                                           (9.7)

This estimate does **not** require monotonicity of `a_k`; it only uses the uniform escape-elasticity cone plus the new stochastic domination (7.3).

## 10. Proof of Theorem A on `1<=lambda<=d-delta`

Set

`L=d-delta`.                                                     (10.1)

The function `lambda H_d(lambda)` is increasing on `(0,d)`. Hence for `1<=lambda<=L`,

`lambda H_d(lambda)<=A_{d,delta}`,                              (10.2)

where

`A_{d,delta}`
` := d(d-1)(d-delta)/[delta(d(d-1)+delta)]`.                    (10.3)

By (9.7) and `mu<=delta`,

`M-lambda M'`
` >= d-A_{d,delta} mu`
` >= d-A_{d,delta} delta`.                                      (10.4)

The right side simplifies exactly to

`d-A_{d,delta}delta`
` = d^2 delta/[d(d-1)+delta] >0`.                               (10.5)

Therefore (5.5) gives

`ell'_lambda<0`                                                  (10.6)

throughout `1<=lambda<=d-delta`.

There is also a clean uniform margin. From (7.3), `M<=d+mu<=d+delta`, while `lambda<=d-delta`, so

`M+lambda<=2d`.                                                  (10.7)

Substituting (10.5) and (10.7) into (5.5) yields

`-ell'_lambda`
` >= 2[d^2 delta/(d(d-1)+delta)]/(2d)^2`
` = delta/[2(d(d-1)+delta)]`.                                  (10.8)

This is (4.5).

## 11. Stitching below `lambda=1`

He--Wang--Xiang prove strict parent-bias decrease on

`0<=lambda<=theta_d:=d/(1+sqrt(1-1/d))`.                        (11.1)

For every `d>=2`, `theta_d>1`. Since `delta<=1`, we have `d-delta>=1`. Therefore their theorem covers the lower segment through and beyond `lambda=1`, while Section 10 covers from `1` to `d-delta`. This proves strict monotonicity on the full interval (4.3).

The new **derivative** claim is kept to the interval proved directly here, `1<=lambda<=d-delta`; no derivative-positive statement is inferred merely from strict monotonicity below `1`.

By (2.7), (10.6) is equivalent to

`v'(beta)>0`                                                     (11.2)

for

`1/(d-delta)<=beta<=1`.                                         (11.3)

## 12. Exact self-check and concrete corollaries

The exact-arithmetic checker is

`proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T05-25-22Z__mean-excess-escape-tilt-wedge-check.py`.

Its archived executed output is

`proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T05-25-22Z__mean-excess-escape-tilt-wedge-check.out`.

It verifies the exact identity (10.5), the margin reduction (10.8), and representative rational cases for `2<=d<=100`, ending

`ALL_EXACT_CHECKS_PASS`.

This finite execution is a **self-check of algebra only**, not the proof of monotonicity; the theorem proof is Sections 5--11.

Concrete exact values include:

- `d=3, delta=1/10`: `A=1740/61`, gap `M-lambda M' >=9/61`, and `-ell' >=1/122`;
- `d=3, delta=1/20`: gap `>=9/121`, and `-ell' >=1/242`;
- `d=2, delta=1/20`: gap `>=4/41`, and `-ell' >=1/82`.

No simulated speed signs are used anywhere.

## 13. What remains open and the next materially different attack

The parent conjecture remains open. The current route still inherits the singularity

`H_d(lambda) ~ 1/(d-lambda)`                                   (13.1)

as `lambda` approaches the minimum offspring `d`. The new theorem compensates for it by requiring `mu=E[nu]-d` to shrink proportionally to the distance `delta=d-lambda`.

Thus it does not cross `lambda=d`, nor does it handle a law concentrated near `d+1` with a tiny amount of degree `d` merely by first-moment control.

The next materially different attack is an **occupation-weighted regeneration sensitivity estimate**: in a regeneration block, charge the singular degree-`d` derivative only on visits to degree-`d` vertices, and prove that this occupation probability is itself proportional to their regeneration-biased frequency. A successful bound of the schematic form

`lambda M' <= regular_part + P_reg(K=d) * singular_part`        (13.2)

would replace the pathwise minimum-degree singularity by an averaged one and could cross `lambda=d` for laws with rare minimum-degree vertices. This is genuinely different from further algebraic polishing of (10.3).

A possible countably supported extension of Theorem A is **not claimed here**; although the finite-support estimates suggest it under suitable integrability/dominated-differentiation hypotheses, those infinite-sum justifications have not been written out.

## 14. Ledger delta

```yaml
ledger_delta:
  track: NM13-05
  parent: T06
  source_id: P0066
  source_problem: Lyons-Pemantle-Peres biased-walk speed monotonicity on supercritical Galton-Watson trees without leaves
  status: PARTIAL
  parent_before: OPEN
  parent_after: OPEN
  runtime_model: GPT-5.6 Sol
  runtime_reasoning: UNVERIFIED
  bias_convention:
    parent_bias: lambda
    child_bias: beta=1/lambda
  offspring_assumptions_after:
    support: finite subset of positive integers
    minimum_offspring: d>=2
    mean: m=E[nu]
    mean_excess: mu=m-d
    defect_parameter: 0<delta<=1
    condition: mu<=delta
  source_scope_before: adjacent two-point laws {d,d+1}, endpoint defect probability <=delta, lambda<=d-delta
  source_scope_after: arbitrary finitely supported laws with min support d and E[nu]-d<=delta, strict monotonicity on 0<=lambda<=d-delta
  derivative_region_after: 1<=lambda<=d-delta, equivalently 1/(d-delta)<=beta<=1
  derivative_margin: -ell'_lambda >= delta/[2(d(d-1)+delta)]
  concrete_new_nonadjacent_example: P(nu=3)=99/100, P(nu=13)=1/100 gives lambda<=29/10 and -ell'>=1/122 on lambda>=1
  demonstrated_mechanism_gain: branch-addition makes Aidekon conditional escape weights c_k decreasing in k; the escape tilt therefore lowers the offspring mean, allowing the measure-change derivative to be charged to mean excess rather than support width
  preserved_failed_routes:
    - fixed-degree radial drift does not control the changing environment law
    - differentiating the static branch-addition ratio in the desired direction fails in general
    - central two-type first-generation contraction previously had Perron radius above one
  exact_checker: proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T05-25-22Z__mean-excess-escape-tilt-wedge-check.py
  exact_output: proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T05-25-22Z__mean-excess-escape-tilt-wedge-check.out
  exact_output_terminal: ALL_EXACT_CHECKS_PASS
  simulations_used_for_claim: false
  bounded_literature_check_date: 2026-09-20
  novelty_status: UNVERIFIED_EXTERNALLY
  unchanged_substantive_runs: 0
  residual_obstruction: minimum-degree escape-elasticity bound is singular at lambda=d
  next_attack: occupation-weighted regeneration derivative charging singular sensitivity only to regeneration visits of minimum-degree vertices
```

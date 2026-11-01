Actual runtime model: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6/maximum was requested, but no authenticated model/effort telemetry is exposed, so I do not claim GPT-6/maximum. SUBSTANTIVE MOVEMENT: the LPP parent problem remains OPEN; for the exact no-leaf family `P(nu=3)=1-p, P(nu=4)=p`, a generalized branch-addition escape coupling proves a parametric rare-defect derivative-positive region approaching the minimum-degree boundary `lambda=3`, and in particular proves strict parent-bias decrease on `0<=lambda<=299/100` whenever `p<=1/200` or `p>=199/200`, improving the inherited all-mixture `{3,4}` endpoint `11/4` by `6/25`.**

# NM13-05 T06 — rare extra-child stability up to parent bias 2.99

Date: 2026-09-20.  
Repository: `yspennstate/math-open-problems`, branch `master`.  
Own root: `proofnet24/NM13-05/progress-tree-speed`.  
Parent target: T06 / intake P0066, Lyons--Pemantle--Peres monotonicity of biased-walk speed on a supercritical Galton--Watson tree without leaves.  
Status: **PARTIAL / OPEN parent; NEW RESTRICTED THEOREM CANDIDATE pending later independent review.**

No simulated sign is used anywhere below. The only computation is exact rational arithmetic checking the closed-form inequalities proved on the page.

## 1. Compact continuity handoff

The controlling owner instruction is `operations/PROGRESS20_2026-09-20.md`. Its LIVE20 table assigns NM13-05 to T06 by an escape-probability/regeneration-coupling route and names P01 as the analytic-regeneration companion. This run therefore stays on T06 and develops a coupling/escape mechanism rather than duplicating P01's conditional-degree covariance route.

The historical P0066 attempt is preserved exactly: for fixed offspring number `D`, the local radial drift `(D-lambda)/(D+lambda)` decreases in the parent bias `lambda`, and on a deterministic regular tree this gives the correct sign; but that observation does **not** control the bias-dependent law of the environment seen by the walk. The old rank sheet records the missing measure-change sign bound / monotone speed coupling as the obstruction.

The newest own report before this run is

`proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T01-41-00Z__branch-addition-ratio-coupling.md`.

It treated the different offspring family `{2,3}`, proving `3/4<=c_3/c_2<=1`, widening rare-tail rectangles at `lambda=1.9`, and pushing older rare tails to `lambda=1.966`. Its proposed cross-`2` occupation-weighted regeneration sensitivity bound remains unresolved; this run does not pretend that bound was obtained.

The latest relevant complementary work consumed here is:

- `proofnet24/P01-progress-speed/runs/2026-09-20/2026-09-20T02-02-20Z__run-report.md`, which uses a conditional-current-degree secant/covariance bound and proves broad bounded-support rectangles plus a `{2,13}` theorem;
- `runs/prob10_2026-09-20/PROB10-06/20260920T0221Z_type_conditioned_child_pattern_bridge_b8e41d72.md`, which pushes the **all-mixture `{2,3}`** endpoint to `1.851` by conditioning the child escape recursion on child offspring types;
- `probability_campaigns/progress_first_2026-09-20/P03/analytic/2026-09-20T0104Z__adjacent-two-point-weight-optimization.md`, which proves for every adjacent family `{d,d+1}` and every mixture weight the inherited general endpoint `lambda<=d-1/4`. For `{3,4}` this is `lambda<=11/4`.

The present theorem instead asks how close to the minimum-degree boundary `lambda=3` one can go when the `{3,4}` law is a rare perturbation of either endpoint. That is a new source-level restricted region relative to the inherited all-mixture theorem.

`POSTED.md` was checked. No posted source-wide P0066 solution is recorded; restricted T06 theorems do not close the parent problem.

## 2. Exact source convention and primary literature

Freeze the offspring law

`P(nu=3)=1-p`, `P(nu=4)=p`, `0<=p<=1`.                         (2.1)

This is supercritical and has no leaves, with mean `m=3+p`.

I use the **parent-bias** convention

`P(parent | nu=k)=lambda/(lambda+k)`,
`P(each fixed child | nu=k)=1/(lambda+k)`.                        (2.2)

Thus larger `lambda` biases the walk toward the root, and the conjectural sign is

`ell'_lambda<0`.

The **child-bias** convention in Ben Arous--Fribergh--Sidoravicius is reciprocal:

`beta=1/lambda`.                                                  (2.3)

Writing `v(beta)=ell_{1/beta}`, where differentiable,

`v'(beta)=-ell'_{1/beta}/beta^2`.                                 (2.4)

So strict parent-bias decrease is strict child-bias increase.

Primary-source baseline recovered this run:

1. Ben Arous--Fribergh--Sidoravicius, arXiv:1111.5865, *A proof of the Lyons-Pemantle-Peres monotonicity conjecture for high biases*, submitted 24 November 2011. Its abstract proves `v(beta)` increasing for child bias `beta>=717` on Galton--Watson trees without leaves.
2. He--Wang--Xiang, arXiv:1610.08151, *Monotonicity of the speed for biased random walk on Galton-Watson tree*, prove strict decrease in the parent-bias convention for

   `0<=lambda<=d/(1+sqrt(1-1/d))`

   when the minimum offspring is `d>=2`.
3. Aidekon's exact speed representation and the later Bowditch--Tokushige differentiability/analyticity results justify the derivative reduction used below.

A bounded fresh search dated 2026-09-20 recovered these papers and the differentiability/analyticity literature but did not surface a source-wide solution or a checked theorem matching the `{3,4}` rare-defect near-`3` region below. This is bounded negative evidence only, not a novelty certificate.

## 3. Parent-problem before/after and the fixed restricted metric

### Parent problem

Before: **OPEN**.  
After: **OPEN**.

No full Lyons--Pemantle--Peres monotonicity theorem is claimed.

### Restricted-family scope before this run

For every mixture weight `p in [0,1]` in (2.1), the inherited adjacent-two-point theorem gives strict decrease through

`lambda<=d-1/4=11/4=2.75`.                                      (3.1)

I found no checked repository theorem specializing `{3,4}` to rare endpoint mixtures and pushing substantially closer to `lambda=3`.

### Restricted-family scope after this run

A parametric theorem is proved below. Its clean rational corollary is:

### Theorem A

If

`P(nu=3)=1-p`, `P(nu=4)=p`

and

`0<=p<=1/200`  **or**  `199/200<=p<=1`,                          (3.2)

then the parent-bias speed is strictly decreasing on

`0<=lambda<=299/100=2.99`.                                      (3.3)

Equivalently, in child-bias notation,

`v'(beta)>0` for every `beta>=100/299`                            (3.4)

on the same two offspring tails.

Relative to the inherited all-mixture `{3,4}` endpoint `11/4`, the certified parent-bias endpoint gain is exactly

`299/100-11/4=6/25=0.24`.                                       (3.5)

The new endpoint sits only `1/100` below the minimum offspring degree `3`.

## 4. Exact effective-degree derivative reduction

Fix `1<lambda<3`. Let `B` be the quenched probability, from a vertex, of escaping to infinity before hitting its parent, and let `U=-dB/dlambda>=0`.

For conditional current offspring `k`, let `B_0,...,B_k` be iid copies of `B`, with corresponding `U_i`, and put

`S_k=sum_{i=0}^k B_i`,
`D_k=lambda-1+S_k`,

`c_k=E[(1/(k+1))*S_k/D_k]`,                                      (4.1)

`h_k=E[(1/(k+1))*sum_i(B_i+(lambda-1)U_i)/D_k^2]`.               (4.2)

Direct differentiation gives

`c_k'=-h_k`.                                                       (4.3)

Put `q=1-p` and

`C=q c_3+p c_4`,
`theta=p c_4/C`.                                                   (4.4)

Aidekon's symmetrized speed formula reduces exactly to

`M=3+theta`,
`ell_lambda=(M-lambda)/(M+lambda)`.                               (4.5)

Therefore

`ell'_lambda=2(lambda M'-M)/(M+lambda)^2`.                        (4.6)

Because

`theta/(1-theta)=(p/q)(c_4/c_3)`,

differentiation and (4.3) give

`theta'=theta(1-theta) Delta`,                                   (4.7)

where

`Delta=h_3/c_3-h_4/c_4`.                                         (4.8)

Thus the whole problem is to upper-bound one logarithmic escape sensitivity and then use the fact that endpoint mixtures force `theta` away from the dangerous middle range.

## 5. Self-contained `{3,4}` escape-sensitivity bound

For a tree whose offspring numbers lie between `3` and `4`, regular-tree comparison gives, for `lambda<3`,

`1-lambda/3 <= B <= 1-lambda/4`.                                  (5.1)

The He--Wang--Xiang escape derivative estimate at minimum offspring `3` gives

`0<=U<=B/(3-lambda)`.                                             (5.2)

### Upper bound on `h_3/c_3`

For `k=3`, there are four iid escape variables in (4.1). Pointwise, the ratio of the derivative integrand in (4.2) to the `c_3` integrand is

`[S_3+(lambda-1)sum_i U_i]/[S_3 D_3]`.                            (5.3)

By (5.2),

`S_3+(lambda-1)sum_i U_i`
` <= S_3[1+(lambda-1)/(3-lambda)]`
` = 2 S_3/(3-lambda)`.                                           (5.4)

By the lower escape bound in (5.1),

`D_3>=lambda-1+4(1-lambda/3)`
`   =3-lambda/3=(9-lambda)/3`.                                   (5.5)

Hence the weighted-average ratio obeys

`h_3/c_3 <= 6/[(3-lambda)(9-lambda)]`.                            (5.6)

### Lower bound on `h_4/c_4`

For `k=4`, `U_i>=0`, so the pointwise ratio is at least `1/D_4`. By the upper escape bound in (5.1),

`D_4<=lambda-1+5(1-lambda/4)`
`   =4-lambda/4=(16-lambda)/4`.                                  (5.7)

Therefore

`h_4/c_4 >= 4/(16-lambda)`.                                      (5.8)

Combining (5.6)--(5.8),

`Delta <= a_3(lambda)`                                            (5.9)

with

`a_3(lambda)`
` :=6/[(3-lambda)(9-lambda)]-4/(16-lambda)`.                     (5.10)

This is the `{3,4}` specialization of the adjacent sensitivity estimate, reproduced here because the rare-tail proof below uses its exact structure.

## 6. New generalized branch-addition coupling: `4/5<=c_4/c_3<=1`

This extends the previous NM13-05 `{2,3}` branch-addition lemma by one degree and is the key coupling input of the run.

For `lambda>1`, define

`phi(s)=s/(lambda-1+s)`.                                          (6.1)

It is increasing, concave, and satisfies `phi(0)=0`. Let

`S_4=B_1+B_2+B_3+B_4`,
`S_5=S_4+B_5`.

Then

`c_3=(1/4)E phi(S_4)`,
`c_4=(1/5)E phi(S_5)`.                                           (6.2)

### Lower ratio

Since `phi` is increasing and `S_5>=S_4`,

`E phi(S_5)>=E phi(S_4)`,

so

`c_4/c_3>=4/5`.                                                   (6.3)

### Upper ratio

Fix deterministic `x_1,...,x_5>=0` with total `S>0`. Concavity and `phi(0)=0` give

`phi(S-x_i)`
` >= (1-x_i/S) phi(S)`.                                          (6.4)

Summing over the five indices,

`sum_i phi(S-x_i)>=4 phi(S)`.                                    (6.5)

For iid `B_i`, each leave-one-out sum has the same law as `S_4`; taking expectations in (6.5) yields

`5 E phi(S_4)>=4 E phi(S_5)`.                                    (6.6)

Using (6.2),

`c_4/c_3<=1`.                                                     (6.7)

Thus

`BOX: 4/5<=t:=c_4/c_3<=1`.                                       (6.8)

At `lambda=1`, all relevant sums are strictly positive under minimum offspring `3`, and the same conclusion follows by the direct `lambda downarrow 1` limit (indeed the ratio equals the lower endpoint `4/5`).

## 7. Endpoint-mixture compression of the environment term

From (4.4),

`theta = p t/(1-p+p t)`.                                         (7.1)

Since `theta` increases with `t`, (6.8) gives

`4p/(5-p) <= theta <= p`.                                        (7.2)

This is the mechanism that P01's broad support-width covariance estimate does not use: the added branch couples `c_4` directly to `c_3`, so a rare endpoint mixture remains rare after the Aidekon escape tilt.

Fix `L<3` and `1<=lambda<=L`. From (5.10), after dropping the favorable negative term,

`lambda a_3(lambda)`
` <= 6 lambda/[(3-lambda)(9-lambda)]`
` <= A_L`,                                                        (7.3)

where

`A_L:=6L/[(3-L)(9-L)]`.                                          (7.4)

By (4.6)--(4.8),

`M-lambda M'`
` >= 3+theta-A_L theta(1-theta)`.                                (7.5)

### Rare degree-4 vertices: `p<=epsilon`

From (7.2), `theta<=p<=epsilon`, hence

`theta(1-theta)<=theta<=epsilon`.                                (7.6)

Therefore

`M-lambda M'>=3-A_L epsilon`.                                    (7.7)

So strict decrease follows whenever

`epsilon < 3/A_L`
`        = (3-L)(9-L)/(2L)`.                                     (7.8)

### Rare degree-3 vertices: `1-p<=epsilon`

Let `r=1-p`. From the lower bound in (7.2),

`1-theta`
` = r/(r+p t)`
` <= r/(r+4p/5)`
` = 5r/(4+r)`.                                                    (7.9)

Thus, if `r<=epsilon`,

`theta(1-theta)<=1-theta<=5epsilon/(4+epsilon)`.                  (7.10)

Consequently

`M-lambda M'`
` >= 3-A_L*5epsilon/(4+epsilon)`.                                (7.11)

This is positive whenever

`epsilon < 4(3-L)(9-L)`
`          / [10L-(3-L)(9-L)]`,                                  (7.12)

for the near-`3` range where the denominator is positive.

### Parametric theorem

Combining (7.8) and (7.12): for every `L<3`, the `{3,4}` speed is strictly decreasing on `[1,L]` on either endpoint tail provided the corresponding displayed rarity condition holds. He--Wang--Xiang covers a parent-bias interval strictly past `1` for minimum offspring `3`, so the intervals glue to `[0,L]`.

The important structural consequence is asymptotic. If `delta=3-L downarrow0`, then

`(3-L)(9-L)/(2L) = delta+O(delta^2)`,

while the large-`p` threshold in (7.12) is

`(4/5)delta+O(delta^2)`.                                         (7.13)

Thus this escape coupling proves a **linear rare-defect wedge all the way up to the minimum-degree critical boundary `lambda=3`**. It does not merely give one isolated rational rectangle.

## 8. Exact clean corollary at `lambda=2.99`

Set

`L=299/100`, `epsilon=1/200`.                                    (8.1)

Then

`D:=(3-L)(9-L)=601/10000`,

and

`A_L=6L/D=179400/601`.                                           (8.2)

The parametric rarity thresholds are exactly

`delta_- = D/(2L)=601/59800 > 1/200`,                            (8.3)

`delta_+ = 4D/(10L-D)=2404/298399 > 1/200`.                      (8.4)

So both tails in (3.2) are valid.

For the small-`p` tail, the numerator gap in (7.7) is

`3-A_L/200 = 906/601`.                                           (8.5)

For the large-`p` tail,

`5 epsilon/(4+epsilon)=5/801`,                                   (8.6)

and the numerator gap in (7.11) is

`3-A_L*(5/801)=182401/160467`.                                   (8.7)

Finally `M+lambda<=4+L`, so (4.6) yields explicit uniform derivative margins on `1<=lambda<=L`:

small-`p` tail:

`BOX: -ell'_lambda >= 6040000/97883067`
`                    =0.0617062806...`,                           (8.8)

large-`p` tail:

`BOX: -ell'_lambda >= 3648020000/78404336667`
`                    =0.0465282936...`.                           (8.9)

These are exact consequences of the analytic proof, not simulated signs.

The checker

`2026-09-20T02-34-00Z__rare-extra-child-d3-check.py`

was executed with exact rational arithmetic, and the archived output

`2026-09-20T02-34-00Z__rare-extra-child-d3-check.out`

ends `ALL_EXACT_CHECKS_PASS`.

## 9. Demonstrated mechanism gain, separate from parent scope

### Source-level gain

The full T06 parent remains `OPEN -> OPEN`.

Within the frozen random family `{3,4}`, the inherited source-level theorem scope was all mixture weights through `lambda=11/4`. This run adds a different near-critical wedge and, concretely, proves the two `0.5%` endpoint tails through `lambda=2.99`, a strict endpoint gain of `6/25` for those laws.

### Mechanism-level gain

The previous NM13-05 branch-addition lemma was specialized to `{2,3}` and used to compress one mixture correction. The new proof identifies the degree-general mechanism at the next support pair:

1. adding one iid escape branch and concavity force `4/5<=c_4/c_3<=1`;
2. this bound survives the Aidekon tilt and keeps `theta` within `O(p)` of `0` or `O(1-p)` of `1`;
3. the environment derivative term is multiplied by `theta(1-theta)`, so its blow-up like `1/(3-lambda)` is neutralized by a defect probability of order `3-lambda`.

That is the demonstrated connection to the parent problem: near a deterministic regular tree, a rare adjacent offspring perturbation preserves the speed derivative sign almost to the minimum-degree transience boundary.

This route is complementary to P01's broad conditional-degree covariance bounds: it gives far deeper bias for a much narrower, explicitly frozen offspring family by using an escape-branch coupling rather than support-width control.

## 10. What remains open / failed routes preserved

1. **Parent problem:** still open for general no-leaf Galton--Watson laws and the full transient interval `lambda<E nu`.
2. **Middle `{3,4}` mixtures:** this run does not improve the inherited all-mixture endpoint `11/4` when `p` is bounded away from `0` and `1`; the factor `theta(1-theta)` is then genuinely order one near the minimum-degree boundary.
3. **Crossing `lambda=3` for `p` near `1`:** the present derivative bound uses minimum offspring `3` and therefore necessarily blows up at `lambda=3`, even though the mean is close to `4` when `p` is near `1`. A distinct occupation-weighted or regeneration-block sensitivity estimate would be required to cross `3` on that tail.
4. **Earlier `{2,3}` cross-`2` idea:** the electrical value bound from the predecessor controls escape itself beyond `2` for suitable mixtures, but differentiating that value bound is invalid. No derivative sign beyond `2` is claimed.

The next mathematically distinct attack, if continuing this line, is therefore to condition the derivative cost on the number of minimum-degree vertices actually encountered in a regeneration block. That could replace the hard `1/(d-lambda)` minimum-degree factor by an occupation-weighted defect factor and is the appropriate route for crossing the minimum-degree boundary on a high-`p` tail.

## 11. ledger_delta

```yaml
ledger_delta:
  worker: NM13-05
  live20_parent: T06
  source_id: P0066
  status_before: OPEN
  status_after: OPEN
  bias_convention:
    parent_bias: lambda
    child_bias: beta=1/lambda
  frozen_offspring_family:
    law: P(nu=3)=1-p, P(nu=4)=p
    no_leaves: true
    mean: 3+p
  source_scope_before:
    inherited_all_mixture_region: "all p in [0,1], 0<=lambda<=11/4"
  source_scope_after:
    new_parametric_region: "for L<3, endpoint-tail widths given by (7.8) and (7.12) imply strict decrease on 0<=lambda<=L"
    clean_region: "p<=1/200 or p>=199/200, 0<=lambda<=299/100"
    child_bias_form: "beta>=100/299 on the clean region"
    parent_endpoint_gain_vs_inherited_all_mixture: 6/25
  demonstrated_mechanism_gain:
    branch_addition_ratio: "4/5 <= c_4/c_3 <= 1"
    effect: "Aidekon tilted weight stays within O(defect probability) of endpoint, neutralizing the 1/(3-lambda) derivative singularity"
    asymptotic_wedge: "allowed defect probability is linear in 3-L as L up to 3"
  exact_uniform_derivative_margins:
    p_le_1_over_200: 6040000/97883067
    p_ge_199_over_200: 3648020000/78404336667
  artifacts:
    checker: proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T02-34-00Z__rare-extra-child-d3-check.py
    output: proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T02-34-00Z__rare-extra-child-d3-check.out
    output_terminal: ALL_EXACT_CHECKS_PASS
  simulation_used_as_proof: false
  failed_routes_preserved:
    - "local drift alone does not control environment measure change"
    - "predecessor electrical escape value bound cannot be differentiated to obtain a sign"
    - "minimum-degree derivative envelope cannot cross lambda=3 on the high-p tail"
  residual_obstruction: "occupation-weighted derivative sensitivity across the minimum-degree boundary"
  unchanged_substantive_runs: 0
  recovery_failures: 0
  next_attack: "regeneration-block occupation weighting of minimum-degree defects, aimed at crossing lambda=3 for p near 1"
```

External novelty and independent review remain pending. This is a restricted theorem candidate, not a claim that the full Lyons--Pemantle--Peres conjecture is solved.

Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6/maximum was requested in prompt text only; no authenticated applied-model/reasoning-effort telemetry is exposed, so GPT-6/maximum is not claimed. SOURCE-WIDE STATUS: OPEN -> OPEN. ALL-MIXTURE `{2,3}` ENDPOINT: `1.85527 -> 1.85527` (no movement). RESTRICTED SOURCE MOVEMENT: for `P(nu=2)=1-p, P(nu=3)=p`, the complete region `0<=p<=1/4` is now certified through parent bias `lambda<=1.87`; on the genuinely new rectangle `31/200<=p<=1/4`, `1.85527<=lambda<=1.87`, the exact uniform sign certificate is `-ell'_lambda >= 2000/237169 > 0`. Three materially different attacks: (1) upper-score monotone-order-polytope compression — EXACTLY BLOCKED within the current interval boxes because they contain a common constant-weight vector, so this relaxation reproduces the reverse-Chebyshev bound; (2) retain the moderate mixture coordinate and the quantitative branch-ratio localization — SUCCESS, giving the new rectangle; (3) expectation-level inverse-escape derivative contraction at `lambda=2` from the currently available inverse-moment estimate — INSUFFICIENT, since its certified upper bound is `71/36>1` at `p=1/2`.**

# PROB10-06 — moderate-mixture rectangle for the `{2,3}` no-leaf family

Status: **PARTIAL / OPEN parent.** This report proves a larger rigorously covered parameter region for one genuinely random finitely supported no-leaf offspring family. It does **not** settle the source-wide Lyons–Pemantle–Peres conjecture. The exact finite certificate below is a self-check, not an independent audit. External novelty is **UNVERIFIED**; the literature screen is bounded negative evidence only.

## 1. Controlling instruction, continuity, ownership, and consumed state

Controlling instruction: `operations/PROB10_2026-09-20.md`, blob `6f0fcee836d93371d43b84af1a55150fedc80779` on current `master` when consumed.

The required immutable handoff of R02's preceding Randomstrasse/I0095 target remains preserved:

- `runs/R02/20260920T0005Z_owner_refocus_handoff_I0095_to_PROB10-06_4d8c2a71.md`, creation commit `0439a90108047760ebd8d94ffd7d5b76463666da`.

All historical `artifacts/R02/` remain untouched. No Randomstrasse claim is relabelled as biased-walk progress.

Historical intake `P0066` remains marked attempted-unsolved. Its old local-drift observation did not control the bias-dependent environment seen from the particle. No canonical source-wide closure is present in the repository, and `POSTED.md` does not make a restricted P0066 theorem into a source-wide resolution.

Consumed own predecessor:

- `runs/prob10_2026-09-20/PROB10-06/20260920T0638Z_quantitative_branch_ratio_monotone_polytope_9c41e7b2.md`, blob `57027fa54a21108340e87c7f815f25f93895f1e4`.

That report proves, for every `p in [0,1]` in the `{2,3}` family, strict parent-bias decrease through `lambda=1.85527`, with a quantitative branch-addition bound on `c_3/c_2`. Earlier own work also proves the lower tail `p<=31/200` through `lambda=1.9`; therefore the honest new gap is the moderate strip immediately above `p=31/200`.

Consumed neighboring work rather than duplicating it:

- `proofnet24/P01-progress-speed/runs/2026-09-20/2026-09-20T06-05-48Z__run-report.md`, blob `678c860974871598867ddc62cb6e9624d5c043c7`: a complementary minimum-offspring-one theorem with no maximum-support bound, by degree-tilt compression.
- `proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T06-22-00Z__mixture-localized-adjacent-wedge.md`, blob `d2e0f8a84ce98a6fa220b4232422d1998fb3d6a7`: a complementary `{3,4}` mixture-localized theorem reaching parent bias about `2.85` on moderate endpoint-dominant mixtures.

Idea notes were written before the successful checker:

- `artifacts/prob10_2026-09-20/PROB10-06/20260920T0710Z_upper_order_polytope_idea.md`, creation commit `95d39fc0be9dc4317374fbf422ad1be17cb1dee4`;
- `artifacts/prob10_2026-09-20/PROB10-06/20260920T0734Z_moderate_p_rectangle_idea.md`, creation commit `5ab2d5b7f59459a99c1437e335ad5cd3191e82f9`.

The timestamp strings in artifact filenames are labels; commit order is the authoritative persistence order.

Exact checker and archived stdout:

- `artifacts/prob10_2026-09-20/PROB10-06/20260920T0742Z_moderate_p_rectangle_check.py`, creation commit `3e057ac5347ac6f8d7014e350b7bf780f2fdf540`;
- `artifacts/prob10_2026-09-20/PROB10-06/20260920T0742Z_moderate_p_rectangle_check.out`, creation commit `81ab83d3d522f653aeadb80769511af5db8983ec`, blob `3b15ce8861612b83814fc9e52800241cdc473d2c`.

The executed process exited with code zero and stdout ends `ALL_EXACT_CHECKS_PASS`.

## 2. Exact source problem and bias convention

Let `nu` be the Galton–Watson offspring variable. The source setting is

`P(nu=0)=0`, `m=E nu in (1,infinity)`.

Thus there are **no leaves**.

In the child-bias convention of Ben Arous–Fribergh–Sidoravicius, at a vertex with `k` children,

`P(parent)=1/(1+beta k)`,
`P(each fixed child)=beta/(1+beta k)`.

Larger `beta` increases drift away from the root. The source conjecture asks the limiting speed `v(beta)` to be increasing throughout the transient interval

`beta in (1/m,infinity)`.

This track uses reciprocal parent bias

`lambda=1/beta`,

so

`P(parent)=lambda/(lambda+k)`,
`P(each fixed child)=1/(lambda+k)`.

Larger `lambda` pushes toward the root. With `ell_lambda=v(1/lambda)`, the equivalent conjecture is that `ell_lambda` is nonincreasing on

`0<=lambda<m`.

The restricted family in this report is

`P(nu=2)=1-p`, `P(nu=3)=p`, `0<=p<=1`,

with mean `m=2+p`. All new parent-bias values satisfy `lambda<=1.87<2<=m`, hence lie strictly inside the transient region for every `p` treated.

## 3. Current primary-literature boundary checked this run

The primary/current navigation was refreshed on 20 September 2026.

1. Ben Arous–Fribergh–Sidoravicius, arXiv:1111.5865, states that for Galton–Watson trees **without leaves** the child-bias speed is increasing for `beta>=717`.
2. Aïdékon's speed representation is the exact environment-tilt formula used below.
3. He–Wang–Xiang, arXiv:1610.08151, later published in *Journal of Applied Probability* 62 (2025), proves strict parent-bias decrease on

   `0<=lambda<=m1/(1+sqrt(1-1/m1))`

   when minimum offspring `m1>=2`, and records Aïdékon's earlier source-uniform `lambda<=1/2` improvement.
4. Song–Liu, *AIMS Mathematics* 11 (2026), treats deterministic regular trees; it is not a theorem for genuinely random offspring.

A bounded fresh search found no checked source-wide resolution and no checked theorem identical to the moderate `{2,3}` rectangle below. This is not an exhaustive novelty certificate.

## 4. Metrics: source before/after and auxiliary delta

### Full parent source metric

Before: **OPEN**.  
After: **OPEN**.

No theorem for every no-leaf offspring law on all `0<=lambda<m` is claimed.

### All-mixture `{2,3}` metric

Before: every `p in [0,1]` is certified through `lambda=1.85527`.  
After: unchanged at `lambda=1.85527`.

So this run does **not** move the all-mixture endpoint.

### New restricted source-level region

Before this run, for `31/200<p<=1/4`, the inherited guaranteed endpoint from this track was `lambda=1.85527`.

After this run:

`BOX: 0<=p<=1/4  =>  ell_lambda is strictly decreasing for 0<=lambda<=187/100.`

The genuinely new rectangle is

`BOX: 31/200<=p<=1/4,  185527/100000<=lambda<=187/100.`

The parent-bias endpoint gain on that moderate-mixture strip is

`187/100 - 185527/100000 = 1473/100000 = 0.01473`.

At the fixed level `lambda=1.87`, the rigorously covered lower-mixture range expands from the inherited `p<=31/200` to

`BOX: p<=1/4`,

a mixture-width gain of

`1/4-31/200 = 19/200 = 0.095`.

On the new rectangle the certified derivative margin is

`BOX: -ell'_lambda >= 2000/237169 = 0.008432805299... >0`.

### Auxiliary mechanism delta

The main successful mechanism is not a new global constant; it is retaining the actual mixture coordinate in the already proved quantitative branch-ratio localization instead of optimizing over all `p`. Two attempted mechanism upgrades were also resolved exactly: Section 7 shows the upper order-polytope relaxation cannot improve the present upper score because its box contains a constant vector, and Section 9 shows the available inverse-moment estimate alone is far too weak to certify expectation contraction at `lambda=2`.

## 5. Exact two-point speed derivative reduction

Work on `1<lambda<2`; the inherited theorem already covers the lower interval.

Let `B=B(lambda)` be the quenched escape probability from a vertex before hitting its parent and put `U=-B'>=0`. Conditional on the current offspring value `k`, take iid copies `B_0,...,B_k` and corresponding `U_i`, and define

`S_k=sum_i B_i`,
`D_k=lambda-1+S_k`,

`c_k=E[(1/(k+1)) S_k/D_k]`,

`h_k=E[(1/(k+1)) sum_i(B_i+(lambda-1)U_i)/D_k^2]`.

The inherited dominated-differentiation argument gives

`c_k'=-h_k`.

For the `{2,3}` law set

`C=(1-p)c_2+p c_3`,
`theta=p c_3/C`,
`M=2+theta`.

Aïdékon's symmetrized formula reduces exactly to

`ell_lambda=(M-lambda)/(M+lambda)`.

Put

`Delta=h_2/c_2-h_3/c_3`.

Since

`theta'=theta(1-theta)Delta`,

direct differentiation gives

`BOX: -ell'_lambda`
` = 2(2+theta)[1-lambda g(theta)Delta]/(2+theta+lambda)^2`,

where

`g(theta)=theta(1-theta)/(2+theta)`.

Therefore it is enough to prove a uniform bound

`lambda g(theta)Delta <=Q<1`.

We will prove this with `Q=19/20` on the new rectangle.

## 6. Escape/type envelopes consumed and frozen on the new lambda strip

The previous exact type-conditioned argument supplies, for a branch whose own offspring is 2 or 3,

`b_2=(2-lambda)/2`,
`b_3=3(2-lambda)/(6-lambda)`,
`u_2=2(3-lambda)/(lambda+6)`,
`u_3=(3-lambda)/3`,

and logarithmic-derivative bounds

`q_2^U=1/(2-lambda)`,
`q_3^U=4/((2-lambda)(6-lambda))`,
`q_2^L=9/((3-lambda)(lambda+6))`,
`q_3^L=1/(3-lambda)`.

For an `n`-branch term, condition on exactly `m` type-3 branch roots. Let

`s_min=(n-m)b_2+m b_3`,
`s_max=(n-m)u_2+m u_3`,
`a=lambda-1`.

Then the conditional escape weight lies between

`y_min=s_min/(a+s_min)`,
`y_max=s_max/(a+s_max)`.

The corresponding inherited conditional score upper/lower envelopes are

`R^U_{n,m}=(1+a Q^U_{n,m})/(a+s_min)`,
`R^L_{n,m}=(1+a Q^L_{n,m})/(a+s_max)`,

with

`Q^U_{n,m}=((n-m)u_2 q_2^U+m b_3 q_3^U)/((n-m)u_2+m b_3)`,

`Q^L_{n,m}=((n-m)b_2 q_2^L+m u_3 q_3^L)/((n-m)b_2+m u_3)`.

The exact checker verifies all 27 required monotonicities on

`A=185527/100000 <=lambda<=L=187/100`

with Bernstein depth zero: both weight envelopes decrease in `lambda`, while each frozen score envelope increases. Hence throughout the strip we may freeze

`lo_m=y_min(L)`, `hi_m=y_max(A)`,

upper scores at `L`, and lower scores at `A`.

## 7. Attack 1 — upper-score order-polytope compression is exactly blocked by the current boxes

For `h_2/c_2`, there are three branches. Condition on exactly `m=0,1,2,3` type-3 branch roots. Let `Z_m` be the actual conditional escape weight. Stochastic ordering gives

`Z_0<=Z_1<=Z_2<=Z_3`,

and the envelopes give

`lo_m<=Z_m<=hi_m`.

The frozen upper conditional scores `R_m^U` are decreasing in `m`. The natural new idea was to maximize the exact linear-fractional upper score

`F_U(Z)= [sum_m pi_m(p) Z_m R_m^U]/[sum_m pi_m(p) Z_m]`

over this monotone order polytope, hoping to improve the inherited reverse-Chebyshev bound

`U(p)=sum_m pi_m(p)R_m^U`.

However, the checker finds the exact common interval

`[3900/15877, 22894600000/45289189243]`

contained in every `[lo_m,hi_m]`. Therefore the polytope contains a constant vector

`Z_0=Z_1=Z_2=Z_3=z`

for any `z` in that interval. At such a vector,

`F_U(Z)=U(p)` exactly.

Reverse Chebyshev already proves `F_U(Z)<=U(p)` because `Z_m` is increasing and `R_m^U` decreasing. Hence

`BOX: max_P F_U = U(p)`.

So, within the current interval relaxation, retaining the upper order structure **cannot improve the upper score at all**. This is an exact obstruction to this relaxation, not an obstruction to a sharper probabilistic estimate of the true `Z_m`.

## 8. Attack 2 — moderate-mixture localization succeeds

### 8.1 Upper score

By the reverse-Chebyshev argument just discussed,

`h_2/c_2 <=U(p)`

where

`U(p)=sum_{m=0}^3 binom(3,m)p^m(1-p)^(3-m) R_m^U(L)`.

### 8.2 Lower score and the 64-vertex polytope

For `h_3/c_3`, there are four branches. Condition on exactly `m=0,...,4` type-3 branch roots and let `Y_m` be the conditional escape weight. Stochastic ordering gives

`Y_0<=Y_1<=...<=Y_4`,

while the frozen envelopes give

`lo_m<=Y_m<=hi_m`.

The conditional score is at least `R_m^L(A)`, so

`h_3/c_3 >= F_L(Y)`

with

`F_L(Y)= [sum_m pi_m(p)Y_m R_m^L(A)]/[sum_m pi_m(p)Y_m]`,
`pi_m(p)=binom(4,m)p^m(1-p)^(4-m)`.

Because the denominator is positive, along every line segment the value of `F_L` is a positive-weight convex combination of the endpoint values. Thus its minimum over the compact order polytope occurs at an extreme point.

The polytope has constraints

`lo_m<=Y_m<=hi_m`, `Y_m<=Y_{m+1}`.

A vertex is determined by five independent active equalities chosen among the ten endpoint equalities and four ordering equalities. The exact checker enumerates every such system, solves it over `Q`, rejects infeasible solutions, and finds exactly

`BOX: 64 vertices`.

Hence it is enough to certify the desired inequality at those 64 exact vertices.

### 8.3 Quantitative branch-ratio localization

The predecessor proves, while

`41 lambda^2-228 lambda+288>0`,

that

`c_3/c_2 <= (4-lambda)/(2(3-lambda))`.

The checker verifies the positivity condition throughout the present strip. Since the right side increases with `lambda`, at `L=187/100`,

`BOX: t:=c_3/c_2 <=T=213/226`.

Since

`theta=p t/(1-p+p t)`,

we obtain

`theta<=theta_U(p):=pT/(1-p+pT)`.

For `p<=1/4`, the checker verifies

`2-4 theta_U(1/4)-theta_U(1/4)^2 =87029/88209>0`.

The numerator of `g'` is `2-4theta-theta^2`, so `g` is increasing throughout every admissible tilted interval here. Therefore

`g(theta)<=g(theta_U(p))`.

### 8.4 Exact product bound

For every one of the 64 lower-score vertices, the checker proves exactly on

`31/200<=p<=1/4`

that

`L g(theta_U(p)) [U(p)-F_L(vertex)] < 19/20`.

Every one of the 64 rational inequalities has a positive Bernstein certificate already at subdivision depth zero. Since

`lambda<=L`, `g(theta)<=g(theta_U(p))`,
`Delta<=U(p)-F_L(Y)`,

we conclude uniformly on the full new rectangle that

`lambda g(theta)Delta <=19/20`.

Substituting into the exact derivative identity and using `2(2+theta)>=4` and `2+theta+lambda<=3+L` gives

`-ell'_lambda`
` >=4(1-19/20)/(3+L)^2`
` =2000/237169>0`.

This proves strict decrease on the new rectangle. Stitching with the inherited all-mixture theorem through `lambda=1.85527` and the inherited lower-tail theorem through `lambda=1.9` proves the clean corollary

`BOX: 0<=p<=1/4 => ell_lambda strictly decreases on 0<=lambda<=1.87.`

## 9. Attack 3 — the available inverse-moment estimate alone does not cross `lambda=2`

A previous report proved for the `{2,3}` law, at `lambda=2` and `p>0`,

`E[B^{-1}]<=3/p`.

Hence Jensen gives

`E[B]>=p/3`.

For two iid positive child escapes `B_1,B_2<=1`, let

`w_i=B_i/(B_1+B_2)`.

Then

`w_1^2+w_2^2`
`=1-2B_1B_2/(B_1+B_2)^2`
`<=1-B_1B_2/2`,

because `(B_1+B_2)^2<=4`. Taking expectations gives the certified but crude estimate

`E[w_1^2+w_2^2] <=1-(E B)^2/2 <=1-p^2/18`.

The inverse-escape derivative recursion would need an expectation coefficient below one. At `lambda=2`, `p=1/2`, the estimate available from this moment bound yields only

`lambda E sum_i w_i^2 <=2(1-p^2/18)=71/36>1`.

Thus the **currently available inverse-moment estimate alone cannot certify contraction**. This does not prove the true expectation coefficient is at least one. Crossing `lambda=2` requires sharper control of the weight concentration, e.g. a second inverse moment, a direct overlap lower bound for iid escape probabilities, or an occupation-weighted two-level contraction.

## 10. Exact checks actually executed

The archived checker was executed and returned process exit code zero. Its stdout records:

- 27 exact lambda-envelope monotonicity checks, all at Bernstein depth zero;
- the exact common interval proving the upper order-polytope obstruction;
- exactly 64 feasible lower-score order-polytope vertices;
- exact positivity of the quantitative branch-ratio condition on the whole lambda strip;
- `T=213/226` at `lambda=1.87`;
- exact positivity `87029/88209` for the `g'` numerator at `p=1/4`;
- 64 exact product certificates on `p in [31/200,1/4]`, all at Bernstein depth zero;
- exact derivative margin `2000/237169`;
- exact value `71/36>1` for the inverse-moment-only contraction upper bound at `p=1/2`, `lambda=2`;
- final line `ALL_EXACT_CHECKS_PASS`.

The checker is a self-check. No independent audit is claimed.

## 11. What remains for the full source problem

The full conjecture is vastly stronger: arbitrary no-leaf offspring laws and every parent bias `0<=lambda<E nu`. Even in the present `{2,3}` family, the central-mixture region from about `lambda=1.87` to the mean boundary `2+p` is not covered by this proof. In particular, the present envelope uses `q_2^U=1/(2-lambda)`, which becomes singular at the minimum-degree boundary `lambda=2` even though the mixed law with `p>0` has finite inverse-escape expectation there.

The next mathematically distinct target should therefore be a **distribution-sensitive derivative control that remains finite at `lambda=2`**. A viable proof needs more than `E[B^{-1}]`: it should control concentration of the normalized child weights in the derivative recursion, or derive a two-level/occupation-weighted contraction that gains from the positive type-3 mass. Merely shrinking another rectangle below `lambda=2` with the same envelopes would now have diminishing value.

## 12. Structured ledger delta

```yaml
ledger_delta:
  target: PROB10-06 / P0066 Lyons-Pemantle-Peres biased-walk speed monotonicity
  parent_status_before: OPEN
  parent_status_after: OPEN
  source_assumptions:
    no_leaves: "P(nu=0)=0"
    supercritical: "m=E nu>1"
    child_bias_beta: "outward; conjectured speed increase for beta>1/m"
    parent_bias_lambda: "lambda=1/beta; conjectured speed decrease for 0<=lambda<m"
  restricted_family: "P(nu=2)=1-p, P(nu=3)=p"
  all_mixture_endpoint_before: 1.85527
  all_mixture_endpoint_after: 1.85527
  source_level_restricted_before: "for 31/200<p<=1/4, guaranteed endpoint 1.85527"
  source_level_restricted_after: "for all 0<=p<=1/4, guaranteed endpoint 1.87"
  new_rectangle: "31/200<=p<=1/4 and 1.85527<=lambda<=1.87"
  endpoint_gain_on_new_rectangle: "1473/100000"
  p_width_gain_at_lambda_1_87: "19/200"
  certified_sign_lower_bound: "-ell'_lambda >= 2000/237169"
  auxiliary_delta:
    attack_1: "upper order-polytope relaxation exactly reproduces reverse-Chebyshev because a constant vector is feasible"
    attack_2: "moderate-p + quantitative branch-ratio localization succeeds"
    attack_3: "inverse-moment-only contraction bound gives 71/36>1 at p=1/2, lambda=2, so is insufficient"
  exact_checker: "artifacts/prob10_2026-09-20/PROB10-06/20260920T0742Z_moderate_p_rectangle_check.py"
  exact_output: "artifacts/prob10_2026-09-20/PROB10-06/20260920T0742Z_moderate_p_rectangle_check.out"
  checker_result: ALL_EXACT_CHECKS_PASS
  audit_status: self_check_only
  novelty_status: UNVERIFIED
  remaining_full_scope_gap: "arbitrary no-leaf offspring laws and the full interval 0<=lambda<E nu; even central {2,3} mixtures remain open beyond 1.87, especially across lambda=2"
```

Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6/maximum was requested in prompt text only; no authenticated applied-model/reasoning-effort telemetry is exposed, so GPT-6/maximum is not claimed. SOURCE-WIDE STATUS: OPEN -> OPEN. ALL-MIXTURE `{2,3}` ENDPOINT: `1.85527 -> 1.85527` (unchanged). SUBSTANTIVE RESTRICTED-SCOPE MOVEMENT: the mixture threshold for a certified rectangle crossing the minimum-degree barrier `lambda=2` improves from `p>=41/50` to `p>=3/4`; specifically, if `P(nu=2)=1-p, P(nu=3)=p` and `p>=3/4`, then the parent-bias speed is strictly decreasing on `0<=lambda<=101/50=2.02`, with `-ell'_lambda >= 50/63001` on `1.85527<=lambda<=2.02`. Three materially different attacks: (1) child-own-type conditioned inverse moments + endpoint chords — SUCCESS; (2) retain the child's own escape in the derivative coefficient — MARGINAL INFORMATION ALONE IS PROVABLY INSUFFICIENT because the unknown `U`-weighted law can concentrate at the worst escape endpoint; (3) two-generation scalar unrolling — EXACTLY COLLAPSES to the same `A/(1-rho)` bound, so it gives no gain without a joint state.**

# PROB10-06 — type-conditioned inverse-escape chords lower the mixture threshold across `lambda=2`

Status: **PARTIAL / OPEN parent.** This is a restricted-family theorem candidate with an exact self-check. It does not settle the Lyons--Pemantle--Peres conjecture for arbitrary no-leaf offspring laws, and it has not received the independent audits required for closure. External novelty is **UNVERIFIED**; the literature search below is bounded negative evidence only.

## 1. Controlling instruction, handoff, admission, ownership, and consumed updates

Controlling owner instruction: `operations/PROB10_2026-09-20.md` on current `master`.

The required immutable handoff of R02's preceding Randomstrasse/I0095 target remains preserved:

- `runs/R02/20260920T0005Z_owner_refocus_handoff_I0095_to_PROB10-06_4d8c2a71.md`, creation commit `0439a90108047760ebd8d94ffd7d5b76463666da`.

All prior `artifacts/R02/` are preserved. Nothing from I0095 is relabelled as biased-walk progress.

Historical intake `P0066` remains `attempted_un` / attempted-unsolved. Its old fixed-degree observation that `(k-lambda)/(k+lambda)` decreases with parent bias does not control the `lambda`-dependent environment seen from the particle and is not claimed as new.

Immediate own predecessor consumed:

- `runs/prob10_2026-09-20/PROB10-06/20260920T0854Z_inverse_escape_chord_crosses_lambda2_3a7c9e14.md`, blob `31e701769a187c4cd432adb63488de3c23c282c7`.

That report proves for the same `{2,3}` family that `p>=41/50` gives strict decrease through `lambda=54/25=2.16`, while the all-mixture endpoint is `1.85527`. Its decisive mechanism is an annealed contraction for `U=-B'` based on `E(1/B)` plus a common endpoint chord. The present report does **not** overwrite that theorem: it trades endpoint depth for a wider mixture range, lowering the threshold that crosses `lambda=2` from `41/50` to `3/4`.

New idea written before code:

- `artifacts/prob10_2026-09-20/PROB10-06/20260920T0905Z_type_conditioned_inverse_chord_idea.md`, blob `453caf0dedca67107a1b508f8c2180dde49b56bd`.

Exact checker and archived output consumed:

- `artifacts/prob10_2026-09-20/PROB10-06/20260920T0922Z_type_conditioned_inverse_chord_check.py`, blob `788ca6cc6a3d17963decab3a083dc265739058fd`;
- `artifacts/prob10_2026-09-20/PROB10-06/20260920T0922Z_type_conditioned_inverse_chord_check.out`, blob `47c8243ec0917bcf280ea8129d4246a9a581eb27`.

The archived exact-rational interval checker reports `17089` visited boxes, `8545` accepted boxes, `product_upper<199/200`, `rho_upper<19/20`, derivative margin `50/63001`, and ends `ALL_EXACT_CHECKS_PASS`.

Complementary neighboring work checked before fixing the claim:

- `proofnet24/P01-progress-speed/runs/2026-09-20/2026-09-20T08-58-51Z__run-report.md`, blob `99332ac36d90847883109fa101c5936226a00d7c`, treats minimum-offspring-one laws such as `{1,12}` below `lambda=1` by a same-law static/derivative compatibility estimate.
- `proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T09-32-00Z__annealed-inverse-chord-crosses-lambda3.md`, blob `2903aed7ff5cc4462a3504470e5a73c25760ec7e`, ports the annealed idea to the distinct `{3,4}` family and crosses `lambda=3` there.

Thus this report retains the delimited `{2,3}` child-type-conditioned route and does not take over either neighboring track.

## 2. Exact source problem and bias convention

Let `nu` be the Galton--Watson offspring variable. The source assumptions are

`P(nu=0)=0`, `m=E nu in (1,infinity)`.

Hence the tree has **no leaves**.

In the child-bias convention, at a vertex with `k` children,

`P(parent)=1/(1+beta k)`,
`P(each fixed child)=beta/(1+beta k)`.

Larger `beta` pushes away from the root. The Lyons--Pemantle--Peres conjecture asks the limiting speed `v(beta)` to increase throughout the transient interval

`beta>1/m`.

This track uses reciprocal parent bias

`lambda=1/beta`,

so

`P(parent)=lambda/(lambda+k)`,
`P(each fixed child)=1/(lambda+k)`.

Larger `lambda` pushes toward the root. Writing `ell_lambda=v(1/lambda)`, the equivalent conjecture is that `ell_lambda` is nonincreasing on

`0<=lambda<m`.

This report treats only

`P(nu=2)=1-p`, `P(nu=3)=p`, `3/4<=p<=1`,

whose mean is `m=2+p>=11/4=2.75`. The new endpoint `101/50=2.02` is strictly below every such mean.

## 3. Primary/current literature boundary refreshed this run

The requested sources were rechecked rather than inherited blindly.

1. Ben Arous--Fribergh--Sidoravicius, arXiv:1111.5865, proves the high-**child**-bias direction on Galton--Watson trees without leaves; the abstract states `v(beta)` is increasing for `beta>=717`. This is a baseline, not novelty here.
2. He--Wang--Xiang, arXiv:1610.08151, published in *Journal of Applied Probability* 62 (2025), 1044--1052, proves strict decrease in the parent-bias convention for

   `0<=lambda<=m1/(1+sqrt(1-1/m1))`

   when the minimum offspring is `m1>=2`, and records Aidekon's earlier `lambda<=1/2` improvement. Again this is a baseline.
3. Aidekon, arXiv:1111.4313 / PTRF 159 (2014), supplies the exact speed/environment representation used below.
4. Bowditch--Tokushige supplies differentiability of the speed in the relevant ballistic/CLT regime; this is regularity, not the missing sign.
5. A bounded 20 September 2026 search also found the 2026 deterministic regular-tree monotonicity paper, but no checked source-wide solution and no checked theorem identical to the random `{2,3}`, `p>=3/4`, `lambda<=2.02` rectangle below. This is not an exhaustive novelty certificate.

## 4. Source before/after and auxiliary delta

### Full source metric

Before: **OPEN**.  
After: **OPEN**.

No source-wide theorem for arbitrary no-leaf offspring laws on all `0<=lambda<E nu` is claimed.

### All-mixture `{2,3}` metric

Before: every `p in [0,1]` certified through `lambda=1.85527`.  
After: unchanged at `lambda=1.85527`.

### Complete new restricted region

Before this run, a rectangle that actually crossed `lambda=2` was certified only for

`p>=41/50=0.82`.

After this run,

`BOX: p>=3/4  =>  ell_lambda is strictly decreasing on 0<=lambda<=101/50=2.02.`

Thus the certified mixture threshold for crossing `lambda=2` improves

`41/50 -> 3/4`,

a width gain `7/100` in mixture parameter.

The genuinely new source region, after subtracting the predecessor's coverage, contains

`BOX: 3/4<=p<41/50,  1.85527<=lambda<=101/50.`

On the full checker rectangle

`3/4<=p<=1`, `1.85527<=lambda<=101/50`,

we have the quantitative sign certificate

`BOX: -ell'_lambda >= 50/63001 >0.`

### Auxiliary mechanism delta

The common endpoint chord of the predecessor is replaced by a child-own-type conditioned chord. It records both a sharper conditional mean and a smaller deterministic escape endpoint for a child whose own offspring count is two. This lowers the annealed derivative contraction enough to admit `p=3/4` across `lambda=2`.

A second auxiliary gain is an explicit finite-depth escape truncation estimate on the same rectangle:

`BOX: E[B_N-B] <= (19/20)^N`,

for the natural depth-`N` escape approximation defined in Section 7.

## 5. Exact Aidekon two-state derivative reduction

For `lambda>1`, let `B=B(lambda)` be the quenched probability, starting at a child vertex, of escaping to infinity before hitting its parent, and put

`U=-B'(lambda)>=0`.

For current offspring value `k`, take iid copies `(B_i,U_i)`, `0<=i<=k`, and define

`S_k=sum_i B_i`, `D_k=lambda-1+S_k`,

`c_k=E[(1/(k+1))*S_k/D_k]`,

`h_k=E[(1/(k+1))*sum_i(B_i+(lambda-1)U_i)/D_k^2]`.

The finite-support differentiability argument used in the predecessor gives

`c'_k=-h_k`.

For the `{2,3}` law put

`C=(1-p)c_2+p c_3`,
`theta=p c_3/C`,
`M=2+theta`.

Aidekon's symmetrized formula becomes exactly

`ell_lambda=(M-lambda)/(M+lambda)`.

Set

`Delta=h_2/c_2-h_3/c_3`.

Since

`theta'=theta(1-theta)Delta`,

direct differentiation gives

`BOX: -ell'_lambda`
` = 2(2+theta)[1-lambda g(theta)Delta]/(2+theta+lambda)^2`,

where

`g(theta)=theta(1-theta)/(2+theta)`.

Hence it is enough to prove

`lambda g(theta)Delta<1`.

No derivative sign is assumed in this reduction.

## 6. New child-type-conditioned inverse-moment lemma

The branch escape recursion is

`B=S/(lambda+S)`, `S=sum_{i=1}^nu B_i`.

Let `X=1/B`, `M=E X`. Then

`X=1+lambda/S`.

By Cauchy's inequality, conditionally on `nu=k`,

`1/S <= (1/k^2) sum_{i=1}^k 1/B_i`,

so

`E[X | nu=k] <= 1+(lambda/k)M`.                                 (6.1)

For completeness, the global inverse moment does not need to be assumed finite. Apply the same inequality first to finite-depth escapes with boundary value one. If `M_N` is the corresponding inverse moment,

`M_N <=1+lambda E[1/nu] M_{N-1}`.

Here

`E[1/nu]=(3-p)/6`,

so with

`d:=1-lambda(3-p)/6`,

iteration and monotone convergence give

`BOX: M=E[1/B] <=1/d`.                                           (6.2)

On our rectangle the worst corner is `(lambda,p)=(101/50,3/4)`, where

`d>=97/400>0`.                                                    (6.3)

Now write

`M_k=E[1/B | nu=k]`, `mu_k=E[B | nu=k]`.

From (6.1)--(6.2) and Jensen,

`M_k <=1+lambda/(k d)`,

hence

`BOX: mu_k >= d_k:=k d/(k d+lambda)`, `k=2,3`.                  (6.4)

This is stronger than using only the unconditional lower bound `E B>=d`.

## 7. Conditional deterministic endpoints and exact endpoint chords

Because the offspring law is supported on `{2,3}`, comparison with the deterministic ternary tree gives the universal infinite-tree bound

`0<B<=u:=(3-lambda)/3`.                                         (7.1)

If the current child root itself has exactly `k` children, then its child escape sum is at most `k u`, so

`BOX: B | {nu=k} <= u_k:=k u/(lambda+k u)`.                     (7.2)

Thus

`u_2=2(3-lambda)/(lambda+6)`,
`u_3=u=(3-lambda)/3`.                                            (7.3)

Set

`r_k=d_k/u_k`.

These are valid probabilities. Indeed `d<=u` because

`d-u=lambda(p-1)/6<=0`,

and direct cancellation shows `r_k<=1` iff `d<=u`.

Let `F` be convex and decreasing on `[0,u_k]`. The endpoint chord gives

`F(B) <= (1-B/u_k)F(0)+(B/u_k)F(u_k)`.

Taking conditional expectation and using `E[B|nu=k]>=d_k` and `F(u_k)<=F(0)`,

`BOX: E[F(B)|nu=k] <=(1-r_k)F(0)+r_k F(u_k)`.                   (7.4)

Introduce an endpoint proxy `Y` with

`P(Y=u_2)=(1-p)r_2`,
`P(Y=u_3)=p r_3`,
`P(Y=0)=1-(1-p)r_2-p r_3`.                                      (7.5)

For iid branch escapes and every convex decreasing function of their sum, repeated conditioning in (7.4) bounds the true expectation by the corresponding expectation with iid copies of `Y`.

For `b>0` define

`K_j(b):=E[b/(b+Y_1+...+Y_j)^2]`, `j=1,2`.                     (7.6)

The checker expands (7.6) exactly over the three-point law (7.5), using rational arithmetic only.

## 8. Annealed contraction for `U=-B'`

Differentiating the branch recursion gives

`BOX: U=S/(lambda+S)^2 + lambda sum_i U_i/(lambda+S)^2`.         (8.1)

This is an identity, not a sign assumption.

For a fixed child `i`, let `T` be the sum of the other sibling escapes. Dropping the nonnegative own escape `B_i` gives

`lambda/(lambda+B_i+T)^2 <=lambda/(lambda+T)^2`.                 (8.2)

The kernel `t -> b/(b+t)^2` is decreasing and convex. Because `U_i` is independent of the sibling block, (7.4)--(7.6) imply that, with `eta=E U`,

`eta <= A+rho eta`,                                              (8.3)

where

`rho=(1-p)*2 K_1(lambda)+p*3 K_2(lambda)`,                       (8.4)

and

`A=(1-p)*[2u/(lambda+2u)^2]+p*[3u/(lambda+3u)^2]`.              (8.5)

For (8.5), note that on this rectangle `lambda>3/2`, so `s/(lambda+s)^2` is increasing for all relevant `0<=s<=3u<=lambda`; hence the deterministic endpoint is a valid upper bound for the inhomogeneous term.

The exact checker proves throughout

`3/4<=p<=1`, `1.85527<=lambda<=101/50`

that

`BOX: rho<19/20`.                                                (8.6)

Therefore

`BOX: eta<=A/(1-rho)`.                                          (8.7)

### Finite-depth truncation error

Let `B_0=1` at the artificial boundary and define recursively

`B_{N+1}=S_N/(lambda+S_N)`.

Then `B_N downarrow B`. Put `delta_N=E[B_N-B]`. Coupling each child finite-depth escape with its infinite escape gives

`B_{N+1}-B`
` = lambda(S_N-S)/[(lambda+S_N)(lambda+S)]`
` <= sum_i (B_{N,i}-B_i) * lambda/(lambda+S)^2`.

For the `i`th summand, drop its own `B_i` from the last denominator. The remaining coefficient depends only on siblings and is independent of `B_{N,i}-B_i`. The same conditional endpoint-chord calculation that gives (8.4) therefore yields

`delta_{N+1}<=rho delta_N`.

Since `delta_0<=1`, (8.6) gives the explicit truncation bound

`BOX: E[B_N-B]<= (19/20)^N`.                                    (8.8)

Thus the finite-depth escape approximation is controlled rather than merely simulated.

The denominators used below are also uniformly separated from zero: `lambda>=1.85527` in (8.1), while `lambda-1+S>=lambda-1>=0.85527` in the Aidekon score.

## 9. Bound the derivative score `Delta`

Let

`a=lambda-1`,
`mu_bar:=(1-p)d_2+p d_3`.                                       (9.1)

Then `E B>=mu_bar` by (6.4).

### 9.1 Upper bound for `h_2/c_2`

The `c_2,h_2` terms use three iid branch escapes. Since `B_i<=u`,

`S_3<=3u=3-lambda`,

hence

`a+S_3<=2`.

Therefore

`c_2=(1/3)E[S_3/(a+S_3)] >= (1/6)E S_3 = (1/2)E B >=mu_bar/2`. (9.2)

For the escape part of `h_2`,

`[ (1/3)E(S_3/(a+S_3)^2) ]/c_2 <=1/a`.                         (9.3)

For the `U` part, condition on one `U_i`, drop its own `B_i`, and apply the type-conditioned two-sibling chord with base `a`. Thus its contribution to the numerator of `h_2` is at most

`eta K_2(a)`.

Using (9.2),

`BOX: h_2/c_2 <= 1/(lambda-1)+2 eta K_2(lambda-1)/mu_bar`.       (9.4)

### 9.2 Lower bound for `h_3/c_3`

Discard the nonnegative `U` part of `h_3`. Since `S_4<=4u`, the remaining quotient is a weighted average of `1/(a+S_4)`, so

`BOX: h_3/c_3 >=1/(a+4u)=3/(9-lambda)`.                         (9.5)

Consequently

`Delta<=D(lambda,p)`,                                            (9.6)

where

`D(lambda,p)`
` :=1/(lambda-1)`
`   +2[A/(1-rho)] K_2(lambda-1)/mu_bar`
`   -3/(9-lambda)`.                                              (9.7)

Notice `D>0` on the whole rectangle because already

`1/(lambda-1)-3/(9-lambda)>0`

for `lambda<3`.

## 10. Locate the escape-tilted mixture coordinate and finish the sign

The elementary branch-addition comparison is included for completeness. Couple

`S_4=S_3+B_4`.

The map `s -> s/(a+s)` is increasing, hence

`E[S_4/(a+S_4)]>=E[S_3/(a+S_3)]`.

Because

`c_3=(1/4)E[S_4/(a+S_4)]`,
`c_2=(1/3)E[S_3/(a+S_3)]`,

we obtain

`c_3/c_2>=3/4`.                                                  (10.1)

Therefore

`theta=p c_3/[(1-p)c_2+p c_3]`
` >=theta_0(p):=3p/(4-p)`.                                      (10.2)

At the new smallest weight `p=3/4`,

`theta_0=9/13`.

For

`g(theta)=theta(1-theta)/(2+theta)`,

the derivative numerator is `2-4theta-theta^2`; at `9/13` it equals

`-211/169<0`.

Thus `g` is decreasing throughout the admissible range and

`g(theta)<=g(theta_0(p))`.                                      (10.3)

Since `Delta<=D` and `D>0`,

`lambda g(theta)Delta<=lambda g(theta_0(p))D(lambda,p)`.         (10.4)

The exact rational interval checker certifies over the entire rectangle

`BOX: lambda g(theta_0(p))D(lambda,p) <199/200`.                 (10.5)

It reached this conclusion after `17089` exact subboxes (`8545` accepted terminal boxes) and archived the result; no floating-point sign decision is used.

Substitution into the exact speed derivative identity gives

`-ell'_lambda`
` > 2(2+theta)(1/200)/(2+theta+lambda)^2`.

Using `2(2+theta)>=4`, `theta<=1`, and `lambda<=101/50`,

`BOX: -ell'_lambda`
` >= (4/200)/(3+101/50)^2`
` =50/63001>0`.                                                  (10.6)

Stitching (10.6) to the inherited all-mixture theorem through `lambda=1.85527` proves the claimed clean restricted theorem:

`BOX: if P(nu=2)=1-p, P(nu=3)=p and p>=3/4,`
`     then ell_lambda is strictly decreasing for 0<=lambda<=101/50.`

In reciprocal child-bias notation, this gives strict increase on the corresponding interval `beta>=50/101`, within the same restricted offspring family.

## 11. Attack 2 — retaining the child's own escape needs genuinely joint `B-U` information

The predecessor's largest structural loss is (8.2), where `B_i` is discarded from the derivative coefficient. A natural alternative is to estimate directly

`E[ U_i * lambda/(lambda+B_i+T)^2 ]`.                            (11.1)

However, the current information consists only of the marginal endpoint/mean constraints on `B_i` and the scalar `E U_i=eta`. Those data alone cannot improve (8.2): among nonnegative joint laws with fixed `E U_i`, the `U_i` mass may concentrate where the decreasing coefficient is maximal, namely at the smallest allowed `B_i`. In the marginal-only linear program the extremal value is therefore exactly the drop-`B_i` bound.

So Route 2 has a precise obstruction: improvement requires a **new joint statement**, for example a lower bound on the `U`-size-biased escape `E[U B]/E U`, or a proved covariance/monotone-likelihood relation between `B` and `U`. No such sign is assumed here.

## 12. Attack 3 — scalar two-generation unrolling is algebraically identical

A third attack was to unroll the derivative recursion one extra generation. If one performs the same scalar decoupling as in (8.3), then one step gives

`eta<=A+rho eta`.

Two steps give only

`eta<=A+rho A+rho^2 eta`.

Solving yields

`eta<=A(1+rho)/(1-rho^2)=A/(1-rho)`,

exactly the one-step bound (8.7). Hence scalar two-level unrolling is **provably incapable of improving the certificate**. A useful two-level route must retain a genuinely joint state such as `E[U phi(B)]` or root/child type correlations rather than collapsing back to `eta` after each generation.

This is a route obstruction, not a counterexample to monotonicity.

## 13. Exact checks actually executed

The checker is pure Python `fractions.Fraction` interval arithmetic. It subdivides the exact rectangle until both inequalities are certified, with no floating-point acceptance test. The archived output records:

- `RECT_A_PASS visited=17089 accepted=8545 product_upper<199/200 rho_upper<19/20`;
- worst displayed interval upper approximation `0.994997611971952` (display only; acceptance used exact rationals);
- `RECT_A_derivative_margin=50/63001`;
- `TRUNCATION_FROM_RHO: E[B_n-B] <= (19/20)^n`;
- final line `ALL_EXACT_CHECKS_PASS`.

This is a **self-check**, not an independent audit.

## 14. Remaining full-scope gap

The source conjecture remains much stronger than this report:

1. arbitrary no-leaf offspring laws are still open;
2. even for `{2,3}`, the all-mixture endpoint remains `1.85527`;
3. the central mixtures `p<3/4` are not yet bridged across `lambda=2` by this mechanism;
4. for `3/4<=p<41/50`, the interval from `2.02` to the critical boundary `2+p` is open here;
5. for `p>=41/50`, the predecessor remains stronger in endpoint depth (`2.16`), so this run's gain is breadth in `p`, not a universal endpoint improvement;
6. no independent audit or worldwide-priority certificate has been obtained.

The next mathematically nonredundant target is a joint `B-U` estimate that beats the marginal extremizer in Section 11. A concrete sufficient object would be a positive lower bound on `E[UB]/EU` in terms of `(lambda,p)`; that would allow the own-child escape to remain in the derivative denominator and may lower the crossing threshold below `p=3/4`.

## 15. Structured ledger delta

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
  lambda2_crossing_threshold:
    before: "p>=41/50"
    after: "p>=3/4"
    threshold_width_gain: "7/100"
  new_clean_region:
    p_range: "3/4<=p<=1"
    endpoint: "101/50"
    genuinely_new_subregion: "3/4<=p<41/50 and 1.85527<=lambda<=101/50"
    certified_sign_lower_bound: "-ell'_lambda >= 50/63001 on 1.85527<=lambda<=101/50"
  auxiliary_delta:
    successful_route: "child-type-conditioned inverse moment and endpoint chord for U=-B'"
    finite_depth_error: "E[B_N-B] <= (19/20)^N"
    route_2_obstruction: "marginal B and EU data alone allow U-weighted mass at the worst B endpoint; a joint B-U inequality is necessary"
    route_3_obstruction: "two-step scalar unrolling yields A(1+rho)/(1-rho^2)=A/(1-rho), exactly no improvement"
  exact_checker: "artifacts/prob10_2026-09-20/PROB10-06/20260920T0922Z_type_conditioned_inverse_chord_check.py"
  exact_output: "artifacts/prob10_2026-09-20/PROB10-06/20260920T0922Z_type_conditioned_inverse_chord_check.out"
  checker_result: ALL_EXACT_CHECKS_PASS
  audit_status: self_check_only
  novelty_status: UNVERIFIED
  remaining_full_scope_gap: "arbitrary no-leaf laws and full 0<=lambda<E nu; even {2,3} central p<3/4 is not bridged across lambda=2"
```

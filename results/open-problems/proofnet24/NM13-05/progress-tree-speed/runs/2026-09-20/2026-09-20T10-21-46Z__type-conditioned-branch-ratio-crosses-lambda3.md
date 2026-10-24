Model actually run: **GPT-5.6 Sol. Reasoning effort: UNVERIFIED.** GPT-6/maximum was requested in prompt text, but no authenticated applied reasoning-effort telemetry is exposed. **SUBSTANTIVE MOVEMENT:** the Lyons--Pemantle--Peres parent problem remains OPEN, but for `P(nu=3)=1-p, P(nu=4)=p` the proved minimum mixture for a certified crossing of the minimum-degree barrier is widened from `p>=3/4` to `p>=2/3`. Specifically, `p>=2/3` now gives strict parent-bias speed decrease through `lambda=603/200=3.015`, with exact derivative margin `3200/1968409` on the newly proved strip. No simulated speed sign is used.

# NM13-05 T06 — type-conditioned inverse-escape chords plus quantitative branch addition widen the lambda=3 crossing to p>=2/3

Date: 2026-09-20.  
Repository: private `yspennstate/math-open-problems`, branch `master`.  
Own root: `proofnet24/NM13-05/progress-tree-speed`.  
Parent target: T06 / historical intake P0066, Lyons--Pemantle--Peres monotonicity of biased-walk speed on a supercritical Galton--Watson tree without leaves.  
Status: **PARTIAL / OPEN parent; NEW RESTRICTED-FAMILY THEOREM CANDIDATE pending later independent review.**

## 1. Compact handoff, ownership, and preserved failed routes

The controlling owner instruction is `operations/PROGRESS20_2026-09-20.md` (blob `4a207f06e5c8294c83bcabcd9a1477f26f54b441`). LIVE20 assigns NM13-05 to T06 by escape-probability / regeneration coupling, with P01 as the complementary analytic regeneration-derivative worker. No ownership change is made here.

Historical P0066 remains attempted-unsolved. Its old attempt proved only that for a fixed offspring count `k` the local radial drift

`(k-lambda)/(k+lambda)`

decreases with parent bias `lambda`. The repository already records the obstruction: the environment seen from the walker changes with `lambda`, so the local drift sign does not control the speed derivative. That failed route is preserved.

The immediate own predecessor is

`proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T09-32-00Z__annealed-inverse-chord-crosses-lambda3.md`.

It removed the old pointwise `1/(3-lambda)` escape-elasticity pole by an annealed inverse-escape / common endpoint-chord contraction and proved crossing regions beginning at `p>=3/4`, including `p>=3/4` through `lambda=157/50=3.14`. Its named next attack was to condition the inverse-escape chord on child degree.

For the broader mixture class `p>=2/3`, the latest inherited own theorem before this run was the 08:25 sharp-elasticity report:

`p>=2/3  =>  strict decrease through lambda=71/25=2.84`.

Latest live companion consumed: `proofnet24/P01-progress-speed/runs/2026-09-20/2026-09-20T08-58-51Z__run-report.md`. P01 currently treats minimum-offspring-one nonadjacent laws below `lambda=1` by a same-law static/derivative compatibility argument. The present minimum-degree-three escape coupling is complementary.

Latest relevant same-source PROB10 work consumed was the `{2,3}` child-type-conditioned inverse-chord theorem `runs/prob10_2026-09-20/PROB10-06/20260920T0951Z_type_conditioned_inverse_chord_crosses_lambda2_8e3b1a6c.md` and its subsequent quantitative lower branch-ratio idea `artifacts/prob10_2026-09-20/PROB10-06/20260920T1006Z_quantitative_lower_branch_ratio_idea.md`. Those explicitly leave the `{3,4}` family to NM13-05. This run ports, rederives, and combines those mechanisms with the four-ary constants and obtains a new source-level region.

There has been substantive movement in the immediate NM13-05 predecessors, so the three-unchanged-run rotation trigger does not apply. Current repository history records no POSTED source-wide P0066 closure; restricted T06 theorems do not close the parent.

## 2. Frozen offspring assumptions and bias convention

Throughout,

`P(nu=3)=1-p,   P(nu=4)=p,   2/3<=p<=1`.                       (2.1)

There are no leaves and

`m=E nu=3+p >= 11/3`.                                           (2.2)

Use the **parent-bias** convention

`P(parent | nu=k)=lambda/(lambda+k)`,
`P(each fixed child | nu=k)=1/(lambda+k)`.                      (2.3)

Larger `lambda` pushes toward the root. Write the speed as `ell_lambda`; the target sign is

`ell'_lambda<0`.                                                 (2.4)

The outward child-bias convention is reciprocal:

`beta=1/lambda`.                                                 (2.5)

Hence wherever differentiable,

`v'(beta)=-ell'_{1/beta}/beta^2`.                               (2.6)

The new endpoint is strictly inside the transient/ballistic mean boundary:

`603/200 < 11/3 <= m`.                                          (2.7)

## 3. Primary-source and current-literature boundary refreshed

A bounded fresh check on 2026-09-20 recovered the requested primary sources and current regularity context.

1. Ben Arous--Fribergh--Sidoravicius, arXiv:1111.5865, *A proof of the Lyons-Pemantle-Peres monotonicity conjecture for high biases*, states in the outward child-bias convention that `v(beta)` is increasing for `beta>=717` on Galton--Watson trees without leaves.
2. He--Wang--Xiang, arXiv:1610.08151, later published in *Journal of Applied Probability* 62 (2025), 1044--1052 (published online 5 March 2025), proves strict parent-bias decrease on

   `0<=lambda<=m1/(1+sqrt(1-1/m1))`

   when the minimum offspring `m1>=2`.
3. Aidekon's exact speed representation supplies the scalar environment tilt consumed below. Bowditch--Tokushige, arXiv:1906.07913, supplies differentiability in the ballistic CLT regime; our finite-support rectangle is strictly inside `lambda<m` and the contraction below gives the needed finite derivative moments as well.
4. A bounded 2026 search recovered the deterministic regular-tree monotonicity paper of Song--Liu but no checked source-wide resolution or checked theorem identical to the random `{3,4}`, `p>=2/3`, `lambda<=3.015` region. This is bounded negative evidence only, **not** a novelty certificate.

## 4. Parent-problem before/after and source-level scope movement

### Parent problem

Before: **OPEN**.  
After: **OPEN**.

No theorem for arbitrary no-leaf offspring laws over the full conjectured interval is claimed.

### Restricted `{3,4}` scope before

For the full class `p>=2/3`, the strongest inherited own theorem was

`0<=lambda<=71/25=2.84`.

Separately, the immediate predecessor crossed `lambda=3` only on the narrower upper tail `p>=3/4`.

### Restricted `{3,4}` scope after

**Theorem A.** Under (2.1), the parent-bias speed is strictly decreasing throughout

`BOX: 0<=lambda<=603/200=3.015`.                                (4.1)

On the genuinely new strip

`71/25<=lambda<=603/200`,                                       (4.2)

we have the uniform derivative bound

`BOX: -ell'_lambda >= 3200/1968409 >0`.                         (4.3)

Thus the `p>=2/3` endpoint moves by

`603/200-71/25 = 7/40 = 0.175`,                                 (4.4)

and, qualitatively more importantly, the certified crossing threshold for the minimum-degree point broadens from `p>=3/4` to

`BOX: p>=2/3`.                                                   (4.5)

In child-bias notation this yields strict increase on the reciprocal region, in particular

`v'(beta)>0 for beta>=200/603`                                  (4.6)

within the same offspring subclass, interpreted with the usual reciprocal parameterization.

The rest of this report proves the new strip (4.2); the interval below `71/25` is inherited from the 08:25 report.

## 5. Consumed exact Aidekon two-state derivative reduction

Work on `lambda>1`. Let `B=B(lambda)` be the quenched probability, starting at a child vertex, of escaping to infinity before hitting its parent, and put

`U=-dB/dlambda>=0`.                                              (5.1)

For current offspring `k`, take iid copies `(B_i,U_i)`, `0<=i<=k`, and set

`S_k=sum_i B_i`,
`D_k=lambda-1+S_k`,                                              (5.2)

`c_k=E[(1/(k+1))*S_k/D_k]`,                                     (5.3)

`h_k=E[(1/(k+1))*sum_i(B_i+(lambda-1)U_i)/D_k^2]`.              (5.4)

On the present compact finite-support ballistic strip, the standard differentiability framework plus the integrable contraction established below gives

`c'_k=-h_k`.                                                     (5.5)

Define

`C=(1-p)c_3+p c_4`,
`theta=p c_4/C`,
`M=3+theta`.                                                     (5.6)

Aidekon's symmetrized speed formula is

`ell_lambda=(M-lambda)/(M+lambda)`.                              (5.7)

With

`Delta=h_3/c_3-h_4/c_4`,                                        (5.8)

we have

`theta'=theta(1-theta)Delta`                                    (5.9)

and hence

`BOX: -ell'_lambda`
` = 2M/(M+lambda)^2 * [1-lambda*g(theta)*Delta]`,               (5.10)

where

`g(theta)=theta(1-theta)/(3+theta)`.                            (5.11)

It suffices to bound `lambda g(theta)Delta` strictly below one.

## 6. New lemma 1: child-type-conditioned inverse-escape mass

The branch escape recursion is

`B=S/(lambda+S)`, `S=sum_{i=1}^nu B_i`.                         (6.1)

Let `X=1/B`, `M_X=E X`. Then

`X=1+lambda/S`.                                                  (6.2)

Conditionally on `nu=k`, Cauchy's inequality gives

`1/S <= (1/k^2) sum_i 1/B_i`,                                   (6.3)

so

`E[X | nu=k] <= 1+(lambda/k)M_X`.                               (6.4)

As in the predecessor, apply the same inequality first to finite-depth escape probabilities. Since

`E(1/nu)=(4-p)/12`,                                              (6.5)

we obtain by iteration and monotone convergence

`M_X<=1/d`,                                                      (6.6)

where

`d:=1-lambda(4-p)/12`.                                          (6.7)

On the full new rectangle the worst corner gives

`d>=13/80>0`.                                                    (6.8)

Combining (6.4)--(6.7) with Jensen yields the **conditional** escape means

`mu_k:=E[B | nu=k] >= d_k:=k d/(k d+lambda)`, `k=3,4`.          (6.9)

For exact interval work write

`R:=12-4lambda+lambda p`; then

`d_3=R/(12+lambda p)`,
`d_4=R/(12-lambda+lambda p)`.                                  (6.10)

This is strictly more informative than the predecessor's common unconditional lower bound `E B>=d`.

## 7. New lemma 2: child-type deterministic endpoints and a three-point chord proxy

Because every vertex has at most four children, comparison with the deterministic four-child tree gives

`0<B<=u:=(4-lambda)/4`                                          (7.1)

for `lambda<4`.

If the child root itself has `k` children, then its child escape sum is at most `k u`; therefore

`B | {nu=k} <= u_k:=k u/(lambda+k u)`.                          (7.2)

Thus

`u_3=3(4-lambda)/(12+lambda)`,
`u_4=u=(4-lambda)/4`.                                           (7.3)

Since

`d-u=lambda(p-1)/12<=0`,                                        (7.4)

we have `d_k<=u_k`; set

`r_k:=d_k/u_k in [0,1]`.                                        (7.5)

If `F` is convex decreasing on `[0,u_k]`, the secant inequality and `E[B|nu=k]>=d_k` give

`E[F(B)|nu=k] <= (1-r_k)F(0)+r_k F(u_k)`.                       (7.6)

Define the three-point endpoint proxy `Y` by

`P(Y=u_3)=(1-p)r_3`,
`P(Y=u_4)=p r_4`,
`P(Y=0)=1-(1-p)r_3-p r_4`.                                      (7.7)

Repeated conditioning implies that for independent branch escapes and every convex decreasing function of their sum, the true expectation is at most the corresponding expectation with iid copies of `Y`.

For `b>0`, put

`K_j(b):=E[b/(b+Y_1+...+Y_j)^2]`.                               (7.8)

The exact checker expands these finite three-point sums with arbitrary-precision rational interval arithmetic.

## 8. New lemma 3: type-conditioned contraction for U=-B'

Differentiate (6.1):

`U = S/(lambda+S)^2 + lambda sum_i U_i/(lambda+S)^2`.            (8.1)

For a fixed child `i`, let `T` be the sum of its siblings. Dropping the nonnegative own escape from the denominator gives

`lambda/(lambda+B_i+T)^2 <= lambda/(lambda+T)^2`.                (8.2)

The kernel on the right is convex decreasing in `T`, so the proxy (7.7) applies. Also on our strip `lambda>=71/25>2`, while

`S<=4u=4-lambda<=lambda`,                                       (8.3)

so `S/(lambda+S)^2` is increasing over the entire relevant range.

Writing `eta=E U`, we obtain

`eta<=A+rho eta`,                                                (8.4)

where

`A=(1-p)*12(4-lambda)/(12+lambda)^2 + p*(4-lambda)/16`,         (8.5)

`rho=(1-p)*3 K_2(lambda)+p*4 K_3(lambda)`.                       (8.6)

The exact rectangle checker proves

`BOX: rho<49/50`                                                 (8.7)

throughout (4.2). Hence

`BOX: eta<=A/(1-rho)`.                                          (8.8)

This also gives the same geometric control for the natural finite-depth escape approximation, so the derivative variables are uniformly integrable on the certified strip.

## 9. Score bound using the type-conditioned chord

Let

`mu_bar:=(1-p)d_3+p d_4`, `a=lambda-1`.                         (9.1)

For `c_3`, four iid branch escapes appear. Since `S_3<=4u=4-lambda`,

`D_3=a+S_3<=3`,                                                  (9.2)

and hence

`c_3>=E B/3>=mu_bar/3`.                                         (9.3)

The escape-only part of `h_3/c_3` is at most `1/a`. For its derivative part, condition on one `U_i`, discard its own `B_i` as in (8.2), and apply the three-sibling proxy with base `a`. This gives

`h_3/c_3 <= 1/(lambda-1)+3 eta K_3(lambda-1)/mu_bar`.            (9.4)

For `h_4/c_4`, discard the nonnegative derivative part. Since the five-escape denominator obeys

`D_4<=lambda-1+5u=(16-lambda)/4`,                               (9.5)

we get

`h_4/c_4 >=4/(16-lambda)`.                                      (9.6)

Therefore

`Delta<=D(lambda,p)`,                                            (9.7)

where

`D(lambda,p)`
` :=1/(lambda-1)`
`   +3[A/(1-rho)] K_3(lambda-1)/mu_bar`
`   -4/(16-lambda)`.                                            (9.8)

## 10. New lemma 4: quantitative lower branch-addition ratio for {3,4}

The type-conditioned derivative contraction alone is not the only gain. We also sharpen the static location of the Aidekon tilt.

Let

`Phi_n:=E[S_n/(a+S_n)]`, `a=lambda-1`,                          (10.1)

so

`c_3=Phi_4/4`, `c_4=Phi_5/5`.                                  (10.2)

Couple `S_5=S_4+B` with an independent extra branch. Then exactly

`Phi_5-Phi_4`
` =E[a B/((a+S_4)(a+S_4+B))]`.                                 (10.3)

Using `S_4<=4u`, and conditional on the extra branch root type using `E[B|nu=k]>=d_k` and `B<=u_k`,

`Phi_5-Phi_4`
` >= a/(a+4u) * [ (1-p)d_3/(a+4u+u_3)`
`                  + p d_4/(a+4u+u_4) ]`.                      (10.4)

Also

`Phi_4<=4u/(a+4u)`.                                              (10.5)

Because `a+4u=3`, (10.2)--(10.5) imply the quantitative branch ratio

`BOX: c_4/c_3 >= R_*(lambda,p)`,                                (10.6)

with

`R_*=(4/5)*[1+(lambda-1)/(4-lambda)`
`              *((1-p)d_3/(3+u_3)+p d_4/(3+u_4))]`.            (10.7)

In particular `R_*>=4/5`, recovering the old coarse branch-addition inequality but now with a strict positive correction.

Consequently

`theta>=theta_*:=p R_*/(1-p+p R_*)`.                            (10.8)

Already the coarse `R_*>=4/5` and `p>=2/3` give

`theta>=8/13`.                                                   (10.9)

The derivative of `g(theta)=theta(1-theta)/(3+theta)` has numerator

`3-6theta-theta^2`,                                              (10.10)

which at `theta=8/13` equals `-181/169<0` and then decreases. Thus `g` is decreasing throughout the admissible tilt range and

`g(theta)<=g(theta_*)`.                                         (10.11)

This is the second half of the hybrid mechanism: the type-conditioned chord lowers the score `D`, while the quantitative extra-branch mass pushes the tilted mixture farther toward degree four and lowers `g`.

## 11. Exact rational certificate and derivative margin

Combining (5.10), (9.7), and (10.11), it is enough to show

`lambda g(theta_*) D(lambda,p) <1`.                             (11.1)

The finite core was certified with arbitrary-precision rational interval arithmetic in C++ (`boost::multiprecision::cpp_rational`). The checker recursively subdivides the exact rectangles; all acceptance decisions are rational comparisons, not floating-point signs.

Checker:

`proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T10-21-46Z__type-conditioned-branch-ratio-crosses-lambda3-check.cpp`

created at commit `1757b81f8b2c121a900767558202c69432c5454a`.

Actual stdout:

`proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T10-21-46Z__type-conditioned-branch-ratio-crosses-lambda3-check.out`

created at commit `73a5c2bf08e2124bff1a3567fd60835155a3153e`.

It proves separately

`p in [2/3,1], lambda in [71/25,3]:`
`    lambda g(theta_*)D <99/100, rho<49/50`,                    (11.2)

and

`p in [2/3,1], lambda in [3,603/200]:`
`    lambda g(theta_*)D <99/100, rho<49/50`.                    (11.3)

The archived output records 16,179 visited / 8,090 accepted rational cells for the lower rectangle and 14,913 / 7,457 for the upper rectangle, and ends `ALL_EXACT_CHECKS_PASS` for each invocation. The displayed decimal `worst_prod` values in stdout are summaries only; acceptance uses exact rationals.

From (10.9),

`M=3+theta>=47/13>603/200>=lambda`.                             (11.4)

For `M>lambda`, the prefactor `2M/(M+lambda)^2` decreases with `M`; hence it is bounded below by its value at `M=4` and the largest lambda. Using the exact slack `1/100` from (11.2)--(11.3),

`-ell'_lambda`
` >= 8/(4+603/200)^2 * 1/100`
` =3200/1968409>0`.                                              (11.5)

This proves the new strip and, stitched with the inherited theorem through `71/25`, proves Theorem A.

No simulated speed sign enters the argument.

## 12. Demonstrated mechanism gain, separately from parent scope

**Parent/source scope gain:** for the exact `{3,4}` law, the full upper-moderate class `p>=2/3` advances from the inherited endpoint `2.84` to `3.015`, an exact gain `7/40`, and now crosses the structural minimum-offspring point `lambda=3`. The previously proved crossing required `p>=3/4`; the certified crossing class widens by an exact mixture width `1/12`.

**Mechanism gain:** the predecessor used one common escape mean and one common endpoint. This run uses the child's own degree to produce `(d_3,u_3)` and `(d_4,u_4)`, replacing the binary common chord by the three-point proxy (7.7), and simultaneously uses the same conditional escape mass to obtain the strict branch-addition ratio (10.7). These two improvements attack different factors of the exact derivative penalty: the former contracts `Delta`, the latter contracts `g(theta)`. Their combination is what reaches the broader crossing class without reviving the pointwise `1/(3-lambda)` pole.

This remains complementary to P01's analytic minimum-one route.

## 13. Residual obstruction, failed routes, and next attack

The parent conjecture is still much broader. Even in `{3,4}`, this proof does not cover central/lower mixtures across `lambda=3`, nor does it approach the full mean boundary `lambda<3+p` uniformly.

Two inherited route obstructions remain relevant and are not retried here:

1. fixed-degree local drift has the right sign but misses the changing environment law;
2. retaining the own escape `B_i` inside the `U_i` coefficient cannot be improved from marginal `B` and `EU` data alone, because the `U`-weighted law can concentrate at the smallest escape values. A useful next improvement therefore requires genuinely joint `B-U` information, for example a lower bound on `E[UB]/EU` or a recursive size-biased escape estimate.

A second plausible next step is to iterate the **conditional inverse moment itself** one generation without collapsing to the scalar `M_X=E(1/B)`. A successful two-type inverse-moment contraction would sharpen `d_3,d_4` and can be fed unchanged into both Sections 8 and 10. Scalar two-generation unrolling of `eta<=A+rho eta` is known to collapse algebraically to the same bound and is therefore not a useful next route.

No source-wide closure is claimed.

## 14. ledger_delta

```yaml
ledger_delta:
  worker: NM13-05
  target: T06
  source_id: P0066
  source_problem: Lyons-Pemantle-Peres biased-walk speed monotonicity on no-leaf supercritical Galton-Watson trees
  runtime_model: GPT-5.6 Sol
  runtime_reasoning: UNVERIFIED
  parent_status_before: OPEN
  parent_status_after: OPEN
  frozen_offspring:
    law: P(nu=3)=1-p, P(nu=4)=p
    no_leaves: true
    mean: 3+p
  bias_convention:
    parent_bias: lambda
    child_bias: beta=1/lambda
  restricted_before:
    p_ge_2_3_parent_bias_endpoint: 71/25
    lambda3_crossing_mixture_threshold: p>=3/4
  restricted_after:
    p_ge_2_3_parent_bias_endpoint: 603/200
    endpoint_gain: 7/40
    lambda3_crossing_mixture_threshold: p>=2/3
    crossing_threshold_width_gain: 1/12
  exact_derivative_margin_on_new_strip: 3200/1968409
  exact_product_certificate: lambda*g(theta_star)*D < 99/100
  exact_contraction_certificate: rho < 49/50
  demonstrated_mechanism_gain: child-type-conditioned inverse-escape endpoint proxy plus quantitative extra-branch lower ratio simultaneously contracts the derivative score and escape-tilted mixture penalty
  simulated_speed_signs_used: false
  prior_failed_route_preserved: fixed-degree local drift sign does not control the bias-dependent environment law
  immediate_old_obstruction_removed: common-chord mixture threshold p>=3/4 for crossing lambda=3
  parent_closed: false
  review_label: NEW_RESTRICTED_THEOREM_CANDIDATE_PENDING_INDEPENDENT_REVIEW
  checker: proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T10-21-46Z__type-conditioned-branch-ratio-crosses-lambda3-check.cpp
  checker_commit: 1757b81f8b2c121a900767558202c69432c5454a
  checker_output: proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T10-21-46Z__type-conditioned-branch-ratio-crosses-lambda3-check.out
  checker_output_commit: 73a5c2bf08e2124bff1a3567fd60835155a3153e
  next_attack: two-type inverse-moment recursion or genuinely joint B-U size-biased escape estimate
```

Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6/maximum was requested, but no authenticated applied-model/reasoning-effort telemetry is exposed, so GPT-6/maximum is not claimed. SUBSTANTIVE MOVEMENT: the Lyons--Pemantle--Peres parent problem remains OPEN, but for `P(nu=3)=1-p, P(nu=4)=p` an annealed inverse-escape / endpoint-chord contraction removes the predecessor's pointwise pole at `lambda=3` and proves strict parent-bias speed decrease beyond that pole. In particular: `p>=3/4` through `lambda=157/50=3.14`; `p>=4/5` through `lambda=163/50=3.26`; and `p>=41/50` through `lambda=33/10=3.3`. No simulated speed sign is used.**

# NM13-05 T06 — annealed escape-derivative contraction crosses the minimum-degree barrier

Date: 2026-09-20.  
Repository: private `yspennstate/math-open-problems`, branch `master`.  
Own root: `proofnet24/NM13-05/progress-tree-speed`.  
Parent target: T06 / historical intake P0066, Lyons--Pemantle--Peres monotonicity of biased-walk speed on a supercritical Galton--Watson tree without leaves.  
Status: **PARTIAL / OPEN parent; NEW RESTRICTED-FAMILY THEOREM CANDIDATES pending later independent review.**

## 1. Compact handoff, ownership, and recovered history

The controlling owner instruction is `operations/PROGRESS20_2026-09-20.md` (blob `4a207f06e5c8294c83bcabcd9a1477f26f54b441`). LIVE20 assigns NM13-05 to T06 by escape-probability / regeneration coupling, with P01 as the complementary analytic regeneration-derivative worker. No ownership change is made here.

Historical P0066 remains `attempted_unsolved`. Its old attempt established only that for a fixed offspring count `k`, the local radial drift

`(k-lambda)/(k+lambda)`

decreases with parent bias `lambda`. The repository explicitly records the obstruction: this does not control the `lambda`-dependent environment seen by the walker. That failed route is preserved, not relabelled as progress.

Immediate own predecessor:

`proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T08-25-43Z__sharp-elasticity-branch-window.md`.

It treats the same `{3,4}` law by pointwise escape elasticity plus quantitative branch addition. Its strongest upper-tail statement is

`p>=3/4  =>  strict decrease through lambda=2861/1000=2.861`,

and it explicitly identifies the pole `1/(3-lambda)` in the minimum-degree-three pointwise elasticity as the barrier to crossing `lambda=3`.

Latest LIVE20 companion consumed:

`proofnet24/P01-progress-speed/runs/2026-09-20/2026-09-20T08-58-51Z__run-report.md`.

P01 is currently working on minimum-offspring-one two-point laws such as `{1,12}` below `lambda=1`, using a same-law static/derivative compatibility estimate. The present run remains in minimum degree three and replaces a pointwise derivative envelope by an annealed escape coupling. The principal offspring class and mechanism are complementary.

Latest relevant non-LIVE20 T06 work consumed before the derivation was

`runs/prob10_2026-09-20/PROB10-06/20260920T0854Z_inverse_escape_chord_crosses_lambda2_3a7c9e14.md`.

That report crosses the analogous binary minimum-degree pole for `{2,3}` by contracting `U=-B'` through an inverse-escape moment and convex endpoint chords. During this run a later same-stream artifact also appeared,

`artifacts/prob10_2026-09-20/PROB10-06/20260920T0905Z_type_conditioned_inverse_chord_idea.md`,

with an exact type-conditioned checker subsequently committed. Those remain `{2,3}` work. This run ports and rederives the annealed mechanism for `{3,4}`, supplies the different four-ary constants, and obtains a new source-level region crossing `lambda=3`.

There has been substantive movement in each immediate NM13-05 predecessor, so the three-unchanged-run rotation trigger does not apply.

`POSTED.md` / current repository search records no posted source-wide P0066 closure. Restricted T06 theorems remain restricted.

## 2. Frozen source assumptions and bias convention

Throughout this report,

`P(nu=3)=1-p,   P(nu=4)=p,   0<=p<=1`.                         (2.1)

There are no leaves and

`m=E nu=3+p`.                                                     (2.2)

Use the **parent-bias** convention

`P(parent | nu=k)=lambda/(lambda+k)`,
`P(each fixed child | nu=k)=1/(lambda+k)`.                      (2.3)

Larger `lambda` pushes toward the root. Write the speed as `ell_lambda`; the target sign is

`ell'_lambda<0`.                                                 (2.4)

The child-bias convention of Ben Arous--Fribergh--Sidoravicius is reciprocal:

`beta=1/lambda`.                                                 (2.5)

Hence wherever differentiable,

`v'(beta)=-ell'_{1/beta}/beta^2`.                               (2.6)

All new rectangles lie strictly inside `lambda<m`: at the three hard lower-mixture corners, respectively,

`3.14<3.75`, `3.26<3.8`, and `3.3<3.82`.

## 3. Primary-source / present-literature boundary refreshed

Bounded checks on 2026-09-20 recovered the requested primary sources.

1. Ben Arous--Fribergh--Sidoravicius, arXiv:1111.5865, *A proof of the Lyons-Pemantle-Peres monotonicity conjecture for high biases*. In their outward child-bias convention, the arXiv abstract states that `v(beta)` is increasing for `beta>=717` on Galton--Watson trees without leaves.
2. He--Wang--Xiang, arXiv:1610.08151, later published in *Journal of Applied Probability* 62 (2025), 1044--1052 (published online 5 March 2025), proves strict decrease in parent bias on

   `0<=lambda<=m1/(1+sqrt(1-1/m1))`

   when the minimum offspring is `m1>=2`.
3. Aidekon's exact speed representation supplies the scalar environment tilt used below. The regeneration/differentiability literature supplies the derivative framework on compact ballistic strips; the contraction established below also gives the required integrable derivative envelope for the present finite-support strip.
4. A bounded fresh search also found the 2026 Song--Liu deterministic regular-tree result, but no checked theorem identical to the random `{3,4}` crossing rectangles below. This is bounded negative evidence only, **not** a novelty certificate.

## 4. Parent-problem before/after and source-level scope movement

### Parent problem

Before: **OPEN**.  
After: **OPEN**.

No theorem for every no-leaf offspring law over the full transient interval is claimed.

### Restricted `{3,4}` scope before

The immediate predecessor implies, in particular,

`p>=3/4  =>  ell_lambda strictly decreases on 0<=lambda<=2861/1000`.

Thus the inherited certified endpoint for every one of the upper-tail subclasses below was at least `2.861`.

### Restricted `{3,4}` scope after

**Theorem A — broad upper tail crosses the minimum-degree point.** If

`p>=3/4`,                                                        (4.1)

then `ell_lambda` is strictly decreasing throughout

`0<=lambda<=157/50=3.14`.                                       (4.2)

On the genuinely new strip `2861/1000<=lambda<=157/50`,

`-ell'_lambda >= 400/127449 >0`.                                (4.3)

The endpoint gain over the predecessor is

`157/50-2861/1000 = 279/1000 = 0.279`.

**Theorem B — stronger upper tail.** If

`p>=4/5`,                                                        (4.4)

then strict decrease holds throughout

`0<=lambda<=163/50=3.26`,                                       (4.5)

and on the new strip

`-ell'_lambda >= 200/131769 >0`.                                (4.6)

The endpoint gain over the inherited `2.861` theorem is `399/1000=0.399`.

**Theorem C — still stronger tail.** If

`p>=41/50`,                                                      (4.7)

then strict decrease holds throughout

`0<=lambda<=33/10=3.3`,                                         (4.8)

and on the new strip

`-ell'_lambda >= 40/5329 >0`.                                   (4.9)

The endpoint gain over `2.861` is `439/1000=0.439`.

In child-bias notation these imply `v'(beta)>0` on the reciprocal source-admissible regions, in particular for `beta>=50/157`, `beta>=50/163`, and `beta>=10/33`, respectively.

The main qualitative movement is not the decimal endpoint: all three rectangles cross the predecessor's structural singularity at the **minimum offspring value `lambda=3`**.

## 5. Consumed exact Aidekon two-state reduction

Work on `lambda>1`. Let `B=B(lambda)` be the quenched probability, starting at a child vertex, of escaping to infinity before hitting its parent, and set

`U=-dB/dlambda>=0`.                                              (5.1)

For current offspring `k`, take iid copies `(B_i,U_i)`, `0<=i<=k`, and write

`S_k=sum_i B_i`,
`D_k=lambda-1+S_k`,                                              (5.2)

`c_k=E[(1/(k+1))*S_k/D_k]`,                                     (5.3)

`h_k=E[(1/(k+1))*sum_i(B_i+(lambda-1)U_i)/D_k^2]`.              (5.4)

On the compact strips certified below, dominated differentiation gives

`c'_k=-h_k`.                                                     (5.5)

Set

`C=(1-p)c_3+p c_4`,
`theta=p c_4/C`,
`M=3+theta`.                                                     (5.6)

Aidekon's symmetrized speed formula is

`ell_lambda=(M-lambda)/(M+lambda)`.                              (5.7)

With

`Delta=h_3/c_3-h_4/c_4`,                                        (5.8)

one has

`theta'=theta(1-theta)Delta`,                                   (5.9)

and therefore

`-ell'_lambda`
` = 2M/(M+lambda)^2 * [1-lambda*g(theta)*Delta]`,               (5.10)

where

`g(theta)=theta(1-theta)/(3+theta)`.                            (5.11)

Thus it is enough to give a strict uniform upper bound below one on `lambda*g(theta)*Delta`.

The branch-addition monotonicity used in earlier NM13-05 reports remains valid above `lambda=3`: because adding one nonnegative escape branch increases `F_n=E[phi(B_1+...+B_n)]` for `phi(s)=s/(lambda-1+s)`,

`c_4/c_3=(4/5)F_5/F_4 >=4/5`.                                  (5.12)

Hence

`theta >= theta0(p):=4p/(5-p)`.                                 (5.13)

For `p>=3/4`, `theta0>=12/17`, while `g` is decreasing for

`theta >= -3+2 sqrt(3) < 12/17`.                                (5.14)

Therefore

`g(theta)<=g(theta0(p))`.                                       (5.15)

## 6. New mechanism: inverse-escape mean plus convex endpoint chords

The predecessor's pointwise estimate `U/B<=1/(3-lambda)` cannot survive `lambda=3`. This run never uses it.

The escape recursion is

`B=S/(lambda+S)`,
`S=sum_{i=1}^nu B_i`.                                            (6.1)

### 6.1 Annealed inverse-escape lower bound

Put `X=1/B`. Then

`X=1+lambda/S`.                                                  (6.2)

Cauchy's inequality gives pathwise

`1/S <= (1/nu^2) sum_i 1/B_i`.                                  (6.3)

Apply this first to finite-depth escape probabilities to avoid presupposing integrability. With `M_N=E X_N`, independence yields

`M_N <= 1 + lambda E(1/nu) M_{N-1}`.                            (6.4)

For the `{3,4}` law,

`E(1/nu)=(1-p)/3+p/4=(4-p)/12`.                                 (6.5)

Define

`d(lambda,p):=1-lambda(4-p)/12`.                                (6.6)

Whenever `d>0`, iteration and monotone convergence give

`E(1/B)<=1/d`,                                                   (6.7)

and Jensen gives the crucial positive annealed escape bound

`mu:=E B >= d`.                                                  (6.8)

This remains strictly positive on all three rectangles **above** `lambda=3`.

### 6.2 Upper endpoint and normalized mean

Because the offspring support is at most four, comparison with the deterministic four-child tree gives

`0<B<=u(lambda):=(4-lambda)/4`,                                 (6.9)

for every `lambda<4`. Hence

`E B/u >= r:=d/u`.                                               (6.10)

The exact identity

`1-r = lambda(1-p)/[3(4-lambda)]`                               (6.11)

shows directly that `r` increases with `p` and decreases with `lambda`.

### 6.3 Endpoint-chord inequality

If `0<=Y<=u`, `E Y>=r u`, and `F` is convex decreasing on `[0,u]`, then the chord from `0` to `u` gives

`E F(Y) <= (1-r)F(0)+rF(u)`.                                   (6.12)

Iterating over independent siblings,

`E F(B_1+...+B_j)`
` <= sum_{m=0}^j binom(j,m) r^m(1-r)^(j-m) F(m u)`.             (6.13)

This converts the random sibling environment to a finite Bernoulli endpoint mixture with an exact direction of inequality.

### 6.4 Contract `U=-B'` directly

Differentiating (6.1) gives

`U = S/(lambda+S)^2`
`    + lambda sum_i U_i/(lambda+S)^2`.                          (6.14)

For a fixed child `i`, let `T` be the sum of the other sibling escapes. Dropping the nonnegative `B_i` from the denominator increases the coefficient of `U_i`:

`lambda/(lambda+B_i+T)^2 <= lambda/(lambda+T)^2`.               (6.15)

The function

`F_lambda(t)=lambda/(lambda+t)^2`                               (6.16)

is convex decreasing. Define

`K_j(lambda,p)`
` = sum_{m=0}^j binom(j,m) r^m(1-r)^(j-m)`
`     * lambda/(lambda+m u)^2`.                                 (6.17)

On the present strip `lambda>2`, `S<=4u=4-lambda<lambda`, so the inhomogeneous term in (6.14) obeys

`S/(lambda+S)^2 <= n u/(lambda+n u)^2`                          (6.18)

when the branch root has `n` children. Consequently, with

`eta:=E U`,                                                      (6.19)

`A=(1-p)*[3u/(lambda+3u)^2]`
`  +p*[4u/(lambda+4u)^2]`,                                      (6.20)

and

`rho=(1-p)*3K_2+p*4K_3`,                                        (6.21)

we obtain the contraction

`eta <= A + rho eta`.                                           (6.22)

Every exact cell in Section 8 has `rho<1`; in fact the largest certified cell upper bounds are below `0.948`. Therefore

`BOX: eta <= A/(1-rho)`.                                        (6.23)

This is the step that crosses `lambda=3`: unlike `U/B<=1/(3-lambda)`, its denominator stays finite.

## 7. Feed the annealed contraction into the speed score

Let `a=lambda-1`.

### 7.1 Upper bound `h_3/c_3`

For `c_3`, the sum contains four iid escapes. Since `S_3<=4u=4-lambda`,

`D_3=a+S_3<=3`.                                                  (7.1)

Thus

`c_3>=E S_3/(4*3)=mu/3>=d/3`.                                  (7.2)

The escape-only part of `h_3/c_3` is at most `1/a`. For the derivative part, symmetry gives

`(a/4) E[sum_i U_i/D_3^2]=a E[U_0/D_3^2]`.                     (7.3)

Condition on `(B_0,U_0)` and let `T` be the sum of its three siblings. Dropping `B_0` gives

`a E[U_0/D_3^2] <= eta * Kc`,                                  (7.4)

where

`Kc=sum_{m=0}^3 binom(3,m)r^m(1-r)^(3-m)`
`      * a/(a+m u)^2`.                                          (7.5)

Using (7.2),

`h_3/c_3 <= 1/(lambda-1)+3 eta Kc/d`.                           (7.6)

### 7.2 Lower bound `h_4/c_4`

For `c_4`, `S_4<=5u`, hence

`D_4<=lambda-1+5u=(16-lambda)/4`.                               (7.7)

The positive escape-only part already gives

`h_4/c_4 >= 4/(16-lambda)`.                                     (7.8)

Therefore

`BOX: Delta <= D(lambda,p)`,                                    (7.9)

where

`D(lambda,p)`
` =1/(lambda-1)+3 eta Kc/d-4/(16-lambda)`,                      (7.10)

with `eta` bounded by (6.23).

Combining (5.10), (5.15), and (7.9), it suffices to certify

`lambda*g(theta0(p))*D(lambda,p) <1`.                           (7.11)

## 8. Exact rational rectangle certificate — finite core, not simulation

The remaining inequality is two-dimensional but elementary. It was certified by exact `Fraction` arithmetic, using a rectangular partition whose cell bounds follow from proved monotonicities.

For a cell

`p in [pL,pU], lambda in [lL,lU]`,                              (8.1)

use:

1. `d` increases in `p` and decreases in `lambda`; `r=d/u` increases in `p` and decreases in `lambda`, so use `d(lU,pL)` and `r(lU,pL)`.
2. For

   `f_m(lambda)=lambda/(lambda+m u(lambda))^2`,                  (8.2)

   on `2<lambda<4`, `m=0,1` are decreasing and `m=2,3` increasing. Thus each Bernoulli endpoint coefficient has an exact one-endpoint maximum.
3. Those coefficient maxima remain decreasing in `m`, so stochastic monotonicity in the Bernoulli success parameter lets `r` be replaced by its cell lower bound.
4. `A_3` and `A_4` in (6.20) decrease in `lambda`; their mixture is affine in `p`, so its cell maximum is an endpoint value.
5. For

   `q_m(lambda)=(lambda-1)/(lambda-1+m u(lambda))^2`,            (8.3)

   again `m=0,1` decrease and `m=2,3` increase on `2<lambda<4`.
6. `1/(lambda-1)` and `-4/(16-lambda)` are both maximized at `lL` in the direction needed for the upper bound.
7. `g(theta0(p))` decreases for `p>=3/4`, so use `pL`, while the exterior factor `lambda` uses `lU`.

The exact checker is

`proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T09-32-00Z__annealed-inverse-chord-crosses-lambda3-check.py`

(created at commit `4315198f3eec57f15c402a86062f240c50c7fc07`). Its executed stdout is

`proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T09-32-00Z__annealed-inverse-chord-crosses-lambda3-check.out`

(created at commit `1615f70a651f1d17ca0fc01ff8a3b483df990e2f`).

The exact results are:

- Case A, `p>=3/4`, `lambda<=157/50`: 12,800 rational cells, with

  `lambda*g*D < 49/50`;                                          (8.4)

- Case B, `p>=4/5`, `lambda<=163/50`: 4,000 rational cells, with

  `lambda*g*D < 99/100`;                                        (8.5)

- Case C, `p>=41/50`, `lambda<=33/10`: 4,000 rational cells, with

  `lambda*g*D < 19/20`.                                         (8.6)

The largest exact computed upper products are approximately `0.9713243182`, `0.9851822792`, and `0.9351225179`, respectively. These decimals are summaries only; all pass/fail comparisons use exact rational arithmetic. The output ends

`ALL_EXACT_CHECKS_PASS`.

Finally, on all three rectangles, (5.13) gives

`M=3+theta >=3+12/17 > lambda`.                                 (8.7)

Therefore `2M/(M+lambda)^2` is minimized at `M=4` and the right endpoint `L`. Multiplying the exact slack in (8.4)--(8.6) gives the displayed derivative margins:

`8/(4+157/50)^2 * 1/50 = 400/127449`,                           (8.8)

`8/(4+163/50)^2 * 1/100 = 200/131769`,                          (8.9)

`8/(4+33/10)^2 * 1/20 = 40/5329`.                              (8.10)

This completes the restricted theorem arguments.

## 9. Demonstrated mechanism gain, separately from source scope

The source-level gain is Section 4: explicit random-offspring rectangles now cross `lambda=3`.

The mechanism-level gain is more general: a pointwise escape-elasticity pole can be replaced, for bounded offspring, by the pair

`E(1/B)<=1/[1-lambda E(1/nu)]`,                                 (9.1)

plus an endpoint-chord contraction of the derivative variable `U=-B'`. The contraction coefficient depends on the **annealed normalized escape mean**, not on the worst minimum-degree branch. This is exactly why the method remains finite after `lambda` exceeds the minimum offspring.

This is complementary to P01's current analytic score/covariance program. It is also genuinely different from the immediate NM13-05 predecessor: no tightening of the old `1/(3-lambda)` envelope can cross `3`, whereas the present proof removes that envelope entirely.

## 10. Residual obstruction and next attack

The present scalar chord discards type information: every child escape is compressed into the same interval `[0,u]` and common mean lower bound `d`. The latest PROB10 artifact suggests that conditioning the inverse moment and chord on whether the child root has degree 3 or 4 can tighten `rho`, `eta`, and the score bound.

The next materially useful attack is therefore **type-conditioned inverse-escape chords for `{3,4}`**, not further algebra on the old pointwise elasticity cone. The goal is to replace the common `(d,u,r)` by `(d_3,u_3,r_3)` and `(d_4,u_4,r_4)` and test whether the certified upper-tail endpoint can be moved substantially closer to the mean `3+p`.

No source-wide closure is claimed; the parent remains OPEN.

## 11. ledger_delta

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
    p_ge_3_4_parent_bias_endpoint: 2861/1000
  restricted_after:
    p_ge_3_4_parent_bias_endpoint: 157/50
    p_ge_4_5_parent_bias_endpoint: 163/50
    p_ge_41_50_parent_bias_endpoint: 33/10
  exact_derivative_margins_on_new_strips:
    p_ge_3_4: 400/127449
    p_ge_4_5: 200/131769
    p_ge_41_50: 40/5329
  demonstrated_mechanism_gain: annealed inverse-escape moment plus convex endpoint-chord contraction for U=-B' crosses the minimum-degree pole lambda=3
  simulated_signs_used: false
  prior_failed_route_preserved: fixed-degree local drift sign does not control the bias-dependent environment law
  immediate_old_obstruction_removed: pointwise 1/(3-lambda) escape-elasticity pole
  parent_closed: false
  review_label: NEW_RESTRICTED_THEOREM_CANDIDATES_PENDING_INDEPENDENT_REVIEW
  checker: proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T09-32-00Z__annealed-inverse-chord-crosses-lambda3-check.py
  checker_output: proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T09-32-00Z__annealed-inverse-chord-crosses-lambda3-check.out
  next_attack: type-conditioned inverse-escape and derivative chords for {3,4}
```

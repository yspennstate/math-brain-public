Model actually run: **GPT-5.6 Sol. Reasoning effort: UNVERIFIED.** No authenticated applied reasoning-effort telemetry is exposed.

# NM13-05 T06 — finite 12-step harmonic escape envelope widens the `{3,4}` lambda=3 crossing

Date: 2026-09-20.  
Repository: private `yspennstate/math-open-problems`, branch `master`.  
Own root: `proofnet24/NM13-05/progress-tree-speed`.  
Status: **PARTIAL / OPEN parent; NEW RESTRICTED-FAMILY THEOREM CANDIDATES pending later independent review.**

## 1. Compact handoff, ownership, preserved failures

The controlling policy is `operations/PROGRESS20_2026-09-20.md`. LIVE20 assigns NM13-05 to T06 by escape-probability / regeneration coupling and P01 to the complementary analytic regeneration-derivative route. No ownership change is made.

Historical intake P0066 remains attempted-unsolved. Its fixed-degree observation

`(k-lambda)/(k+lambda)` decreases with parent bias `lambda`

is preserved as a failed route: the environment seen from the walker changes with `lambda`, so the local drift derivative alone does not determine the speed derivative.

Immediate own predecessor consumed:

`proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T13-45-00Z__harmonic-type-inverse-refinement.md`.

It introduced one harmonic two-type inverse-moment refinement and proved, for the exact `{3,4}` family,

- `p>=63/100` through `lambda=3001/1000=3.001`,
- `p>=2/3` through `lambda=611/200=3.055`,
- `p>=3/4` through `lambda=321/100=3.21`.

Its named next route was a closed two-dimensional supersolution for the harmonic map or a joint `U`-size-biased estimate. This run proves the finite-iteration supersolution principle and executes twelve certified iterations. This is not an unbounded numerical fixed-point claim.

Latest P01 report consumed:

`proofnet24/P01-progress-speed/runs/2026-09-20/2026-09-20T13-58-15Z__run-report.md`.

P01 currently treats nonadjacent minimum-offspring-one laws below `lambda=1` and crossed its `D=247` analytic barrier. The present adjacent `{3,4}` argument near and above `lambda=3` is complementary.

There has been substantive movement in each immediate NM13-05 predecessor, so the three-unchanged-run rotation trigger does not apply.

## 2. Frozen offspring assumptions and bias convention

Throughout,

`P(nu=3)=1-p,   P(nu=4)=p`,                                    (2.1)

with no leaves. The mean is `m=3+p`.

Use parent bias `lambda`:

`P(parent | nu=k)=lambda/(lambda+k)`,
`P(each fixed child | nu=k)=1/(lambda+k)`.                       (2.2)

Larger `lambda` points toward the root. Write the speed as `ell_lambda`; the target is

`ell'_lambda<0`.                                                  (2.3)

The outward child-bias convention is reciprocal:

`beta=1/lambda`,                                                  (2.4)

so, wherever differentiable,

`v'(beta)=-ell'_{1/beta}/beta^2`.                                (2.5)

All new endpoints below are strictly below `m` on the asserted `p` ranges.

## 3. Primary-source and current-literature boundary

Refreshed 2026-09-20.

1. Ben Arous--Fribergh--Sidoravicius, arXiv:1111.5865, *A proof of the Lyons-Pemantle-Peres monotonicity conjecture for high biases*, states in the outward child-bias convention that `v(beta)` is increasing for `beta>=717` on Galton--Watson trees without leaves.
2. He--Wang--Xiang, arXiv:1610.08151, later published online by Cambridge University Press on 5 March 2025 in *Journal of Applied Probability* 62 (2025), 1044--1052, proves strict parent-bias decrease for

   `0<=lambda<=m1/(1+sqrt(1-1/m1))`

   when the minimum offspring `m1>=2`.
3. Bowditch--Tokushige prove differentiability/analyticity of the speed in the ballistic regime. The contraction below additionally supplies finite-depth derivative domination on the compact strips used here.
4. A bounded current search found Song--Liu's 27 February 2026 regular-tree paper proving monotonic speed for deterministic regular trees, but no checked source-wide solution of the random Galton--Watson LPP problem and no checked theorem identical to the random `{3,4}` rectangles below. This is bounded negative evidence only, not a novelty certificate.

## 4. Parent-problem before/after and demonstrated source-level gain

### Parent problem

Before: **OPEN**.  
After: **OPEN**.

No arbitrary-offspring full-interval theorem is claimed.

### New restricted theorem candidates

**Theorem A — crossing class widened to `p>=3/5`.** If

`p>=3/5`,                                                         (4.1)

then the parent-bias speed is strictly decreasing throughout

`BOX: 0<=lambda<=3001/1000=3.001`.                               (4.2)

On the newly certified high-bias strip `2<=lambda<=3001/1000`,

`BOX: -ell'_lambda >= 8000/49014001 >0`.                         (4.3)

The immediate predecessor required `p>=63/100`; the crossing threshold therefore improves by

`63/100-3/5 = 3/100`.                                            (4.4)

**Theorem B — deeper `p>=2/3` crossing.** If `p>=2/3`, strict decrease holds through

`BOX: lambda<=31/10=3.1`,                                        (4.5)

with

`BOX: -ell'_lambda >= 8/5041 >0`                                (4.6)

on `2<=lambda<=31/10`. The predecessor endpoint was `611/200=3.055`; the gain is

`31/10-611/200 = 9/200`.                                         (4.7)

**Theorem C — deeper `p>=3/4` crossing.** If `p>=3/4`, strict decrease holds through

`BOX: lambda<=651/200=3.255`,                                    (4.8)

with

`BOX: -ell'_lambda >= 3200/2105401 >0`                           (4.9)

on `2<=lambda<=651/200`. The predecessor endpoint was `321/100=3.21`; the gain is again `9/200`.

In child-bias notation the new high-bias derivative strips give `v'(beta)>0`, respectively, for

`1000/3001 <= beta <= 1/2`,
`10/31 <= beta <= 1/2`,
`200/651 <= beta <= 1/2`,                                       (4.10)

within the corresponding offspring subclasses.

No simulated speed sign enters any theorem.

## 5. Branch escape and the scalar starting envelope

Let `B=B(lambda)` be the quenched probability, from a branch root, of escaping to infinity before hitting its parent. If the branch root has `nu=k` children with iid child escapes `B_1,...,B_k`, then

`B=S/(lambda+S)`, `S=sum_i B_i`.                                 (5.1)

Put `Z=1/B`, and write

`z=E Z`, `z_k=E[Z | nu=k]`, `k=3,4`.                             (5.2)

Then

`Z=1+lambda/S`.                                                   (5.3)

Conditionally on `nu=k`, Cauchy gives

`1/S <= (1/k^2) sum_i Z_i`.                                     (5.4)

Since `E(1/nu)=(4-p)/12`, averaging (5.4) gives

`z <= 1 + lambda(4-p)z/12`.                                     (5.5)

Hence, with

`d:=1-lambda(4-p)/12`,                                           (5.6)

we have

`z<=1/d`,                                                        (5.7)

and therefore

`z_k <= M_k^(0):=1+lambda/(k d)`.                               (5.8)

On all three new rectangles `d>0`.

## 6. New mechanism: every finite harmonic iterate is a rigorous envelope

For positive `x_1,...,x_k`, define

`H_k(x_1,...,x_k)=1/(sum_i 1/x_i)`.                              (6.1)

The predecessor proved that `H_k` is coordinatewise increasing and jointly concave. Conditioning on the child root types and using conditional Jensen therefore gives the exact vector subsolution inequality

`z_k <= T_k(z_3,z_4)`,                                           (6.2)

where

`T_k(x_3,x_4)`
` =1+lambda sum_{r=0}^k C(k,r)p^r(1-p)^(k-r)`
`       /[(k-r)/x_3+r/x_4].`                                    (6.3)

The new reusable point is the following finite-iteration lemma.

### Lemma 6.1 — finite monotone envelope iteration

Suppose `z_i<=M_i` for `i=3,4`. Since `T` is coordinatewise increasing, (6.2) implies

`z <= T(z) <= T(M)` componentwise.                               (6.4)

Therefore, starting from the valid vector `M^(0)` in (5.8) and defining

`M^(n+1)=T(M^(n))`,                                               (6.5)

we have

`BOX: z_k<=M_k^(n) for every finite n and k=3,4`.                (6.6)

No convergence, fixed point, or monotonicity of the sequence `M^(n)` is needed. Each finite iterate is independently a theorem consequence of (6.4).

This run takes exactly

`n=12`                                                           (6.7)

and sets

`d_k:=1/M_k^(12)`.                                               (6.8)

Since `x ->1/x` is convex,

`BOX: E[B | nu=k] >= 1/z_k >= d_k`.                             (6.9)

This twelve-step finite supersolution chain is the mechanism-level advance of the run. The predecessor used only `n=1`.

## 7. Transfer to derivative kernels by reciprocal Jensen

For `a>0`, `t>=0`, define

`F_{a,t}(x)=a/(a+t+x)^2`.                                        (7.1)

With `Z=1/B`,

`G_{a,t}(z)=F_{a,t}(1/z)=a z^2/((a+t)z+1)^2`,                   (7.2)

and

`G''_{a,t}(z)=2a(1-2(a+t)z)/((a+t)z+1)^4`.                      (7.3)

On the high-bias strips below, `lambda>=2`; all applications have `a>=lambda-1>=1` and `z>=1`, so `G` is increasing and concave. Conditional Jensen plus (6.6) gives

`E[F_{a,t}(B) | nu=k] <= a/(a+t+d_k)^2`.                        (7.4)

Repeated sibling conditioning yields

`K_j(a) <= K_j^J(a)`                                             (7.5)

with

`K_j^J(a)=sum_{r=0}^j C(j,r)p^r(1-p)^(j-r)`
`            * a/[a+(j-r)d_3+r d_4]^2`.                         (7.6)

## 8. Annealed derivative contraction, valid on lambda>=2

Let

`U=-dB/dlambda>=0`.                                               (8.1)

At finite depth, differentiating (5.1) gives

`U=S/(lambda+S)^2 + lambda sum_i U_i/(lambda+S)^2`.              (8.2)

The deterministic four-child comparison gives

`B<=u:=(4-lambda)/4`.                                            (8.3)

For `lambda>=2`, every possible root sibling sum lies at most at `lambda`: for degree four, `S<=4u=4-lambda<=lambda`, while degree three is even smaller. Therefore `s/(lambda+s)^2` is increasing throughout the relevant source range, and the first term of (8.2) is bounded after averaging by

`A=(1-p)*12(4-lambda)/(12+lambda)^2 + p*(4-lambda)/16`.          (8.4)

For the derivative term, fix a distinguished child, drop its own nonnegative escape from the denominator, and use (7.6) on its siblings. With `eta=E U`,

`eta <= A+rho eta`,                                               (8.5)

where

`rho=(1-p)3K_2^J(lambda)+p4K_3^J(lambda)`.                       (8.6)

The rigorous interval checker proves on every new rectangle

`BOX: rho<97/100`.                                                (8.7)

Hence

`eta<=A/(1-rho)`.                                                 (8.8)

The same geometric coefficient controls finite-depth derivative tails, providing domination for passage to the infinite-depth derivative on these compact strips.

## 9. Aidekon reduction and sufficient inequality

Retain the predecessor's exact Aidekon two-state reduction. Put `a=lambda-1`; for current offspring `k`, take iid branch pairs `(B_i,U_i)`, `0<=i<=k`, and define

`S_k=sum_i B_i`, `D_k=a+S_k`,
`c_k=E[(1/(k+1))*S_k/D_k]`,
`h_k=E[(1/(k+1))*sum_i(B_i+aU_i)/D_k^2]`.                        (9.1)

Then `c'_k=-h_k`. Let

`C=(1-p)c_3+p c_4`,
`theta=p c_4/C`,
`M=3+theta`,
`Delta=h_3/c_3-h_4/c_4`.                                        (9.2)

The speed and its derivative reduce exactly to

`ell_lambda=(M-lambda)/(M+lambda)`,                              (9.3)

`-ell'_lambda`
` = 2M/(M+lambda)^2 * [1-lambda g(theta)Delta]`,                 (9.4)

where

`g(theta)=theta(1-theta)/(3+theta)`.                             (9.5)

Let `mu=(1-p)d_3+p d_4`. The inherited score bound, with the improved `d_k`, gives

`Delta<=D(lambda,p)`                                             (9.6)

where

`D=1/(lambda-1)+3 eta K_3^J(lambda-1)/mu-4/(16-lambda)`.        (9.7)

The inherited quantitative branch-addition estimate gives

`c_4/c_3 >= R_*`,                                                (9.8)

where, with

`u_3=3(4-lambda)/(12+lambda)`, `u_4=(4-lambda)/4`,               (9.9)

`R_*=(4/5)[1+(lambda-1)/(4-lambda)`
`       *((1-p)d_3/(3+u_3)+p d_4/(3+u_4))]`.                    (9.10)

Thus

`theta>=theta_*:=pR_*/(1-p+pR_*)`.                              (9.11)

The coarse ratio `c_4/c_3>=4/5` gives

`theta>=4p/(5-p)`.                                               (9.12)

For `p>=3/5`, the right side is at least `6/11>1/2`. Since `g` is decreasing on `[1/2,1]`,

`g(theta)<=g(theta_*)`.                                          (9.13)

Therefore it is sufficient to prove

`BOX: lambda g(theta_*) D(lambda,p)<1`.                          (9.14)

## 10. Rigorous computational certificate

The checker is

`proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T14-24-53Z__iterated-harmonic-envelope-check.cpp`

and its actual executed output is

`proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T14-24-53Z__iterated-harmonic-envelope-check.out`.

Checker commit: `0526866402bafa2deff9e90867b275e768ef629b`.  
Output commit: `3ba6781d4c009c7a8358730bb8d38c9f47ad68d6`.

The checker uses Boost interval arithmetic with saved directed IEEE-754 rounding. Every rational rectangle endpoint and every nonintegral theorem constant is first outward-rounded with `nextafter`; adaptive subdivisions partition those outer boxes. Thus the computation supplies rigorous enclosure/error bounds rather than sampled signs. There are no transcendental operations.

It proves:

1. `p in [3/5,1]`, `lambda in [2,3001/1000]`:

   `lambda g(theta_*)D <999/1000`, `rho<97/100`.

   It visits 15,931 interval cells. The largest certified enclosure upper endpoint printed for the product is `0.998985915312`.

2. `p in [2/3,1]`, `lambda in [2,31/10]`:

   `lambda g(theta_*)D <99/100`, `rho<97/100`.

   It visits 11,635 cells; printed worst product upper endpoint `0.989996681971`.

3. `p in [3/4,1]`, `lambda in [2,651/200]`:

   `lambda g(theta_*)D <99/100`, `rho<97/100`.

   It visits 16,595 cells; printed worst product upper endpoint `0.989995759777`.

The output ends `ALL_RIGOROUS_INTERVAL_CHECKS_PASS`.

For the derivative prefactor, coarse branch addition gives, at the three lower `p` thresholds,

`M>=39/11`, `M>=47/13`, `M>=63/17`,                              (10.1)

respectively; each is strictly larger than its corresponding right endpoint `L`. Since `M<=4`,

`2M/(M+lambda)^2 >= 8/(4+L)^2`.                                 (10.2)

Combining (10.2) with the certified product gaps gives exactly

`8000/49014001`, `8/5041`, `3200/2105401`,                      (10.3)

which are the derivative margins in Section 4.

## 11. Why each theorem covers from zero

The new machinery is needed only on `[2,L]`. The older exact all-mixture `{3,4}` escape-tilt theorem proves strict decrease for every `p in [0,1]` from `lambda=1` through the exact root of its all-mixture criterion, approximately `2.8152423075`, and therefore overlaps `[2,L]`.

Below that, He--Wang--Xiang's minimum-offspring-three theorem covers

`0<=lambda<=3/(1+sqrt(2/3))`,                                    (11.1)

which overlaps the all-mixture result. Thus the union is a connected interval from zero through each new endpoint.

## 12. Residual obstruction and next attack

Twelve finite harmonic iterations materially improve the crossing class and endpoints, but they still feed only marginal type-conditioned inverse moments into the derivative kernel. The distinguished child's own escape `B_i` is discarded from the coefficient multiplying `U_i` in (8.2). Further finite iterations approach the information ceiling of this marginal route.

The next materially stronger attack is therefore to retain a joint derivative-weighted escape statistic, for example a lower bound on

`E[U B]/E U`,                                                     (12.1)

or a two-type version conditioned on `nu=3,4`. Such a bound would allow part of the distinguished `B_i` to stay in the derivative denominator and could reduce `rho` beyond the marginal inverse-moment ceiling. A secondary algebraic route is to construct a closed rational supersolution of `T` dominating all finite iterates, but that by itself will not recover the lost `B-U` correlation.

## 13. ledger_delta

```yaml
ledger_delta:
  parent: T06_Lyons_Pemantle_Peres_GW_speed_monotonicity
  parent_before: OPEN
  parent_after: OPEN
  owner: NM13-05
  companion: P01
  offspring_family: "P(nu=3)=1-p, P(nu=4)=p"
  bias_convention:
    parent_bias: lambda
    child_bias: beta=1/lambda
  predecessor:
    report: proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T13-45-00Z__harmonic-type-inverse-refinement.md
    crossing_threshold_at_3.001: 63/100
    p_ge_2_over_3_endpoint: 611/200
    p_ge_3_over_4_endpoint: 321/100
  new_scope:
    - p_range: "p>=3/5"
      lambda_endpoint: 3001/1000
      exact_new_strip_margin: 8000/49014001
      crossing_threshold_gain: 3/100
    - p_range: "p>=2/3"
      lambda_endpoint: 31/10
      exact_new_strip_margin: 8/5041
      endpoint_gain: 9/200
    - p_range: "p>=3/4"
      lambda_endpoint: 651/200
      exact_new_strip_margin: 3200/2105401
      endpoint_gain: 9/200
  mechanism_gain: finite_12_step_harmonic_inverse_moment_envelope
  key_lemma: "from z<=T(z), T increasing, and z<=M^(0), every finite iterate M^(n+1)=T(M^(n)) remains a rigorous upper envelope for z"
  contraction_strip: "lambda>=2 only"
  checker_kind: rigorous_IEEE754_directed_rounding_interval_arithmetic
  checker: proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T14-24-53Z__iterated-harmonic-envelope-check.cpp
  output: proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T14-24-53Z__iterated-harmonic-envelope-check.out
  checker_commit: 0526866402bafa2deff9e90867b275e768ef629b
  output_commit: 3ba6781d4c009c7a8358730bb8d38c9f47ad68d6
  review_label: NEW_RESTRICTED_THEOREM_CANDIDATES_PENDING_INDEPENDENT_REVIEW
  next_attack: "joint U-size-biased escape estimate retaining the distinguished child's B; secondary closed rational supersolution for T"
```

Model actually run: **GPT-5.6 Sol. Reasoning effort: UNVERIFIED.** No authenticated applied reasoning-effort telemetry is exposed.

# NM13-05 T06 — joint own-B secant contraction widens and deepens the `{3,4}` crossing region

Date: 2026-09-20.  
Repository: private `yspennstate/math-open-problems`, branch `master`.  
Own root: `proofnet24/NM13-05/progress-tree-speed`.  
Status: **PARTIAL / OPEN parent; NEW RESTRICTED-FAMILY THEOREM CANDIDATES pending later independent review.**

## 1. Compact handoff, ownership, preserved failures

The controlling owner policy is `operations/PROGRESS20_2026-09-20.md`. LIVE20 assigns NM13-05 to T06 by escape-probability / regeneration coupling and P01 to the complementary analytic regeneration-derivative route. No ownership change is made.

Historical intake P0066 remains attempted-unsolved. Its useful but insufficient observation is preserved: for a fixed degree `k`, the one-step radial drift

`(k-lambda)/(k+lambda)`

decreases with parent bias `lambda`, but the law of the environment seen from the walker also changes with `lambda`, so this fixed-degree sign alone does not determine the speed derivative.

Immediate own predecessor consumed:

`proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T14-24-53Z__iterated-harmonic-envelope.md`.

It proved, for the exact `{3,4}` family below,

- `p>=3/5` through `lambda=3001/1000=3.001`,
- `p>=2/3` through `lambda=31/10=3.1`,
- `p>=3/4` through `lambda=651/200=3.255`,

using twelve finite harmonic inverse-moment iterations. An earlier own report already had the narrower `p>=4/5` class through `lambda=163/50=3.26`. The predecessor named the remaining loss correctly: the scalar derivative contraction still dropped the distinguished child’s own escape `B_i` from the denominator multiplying `U_i=-B_i'`.

Latest P01 report consumed:

`proofnet24/P01-progress-speed/runs/2026-09-20/2026-09-20T14-58-02Z__run-report.md`.

P01 now proves a distinct minimum-offspring-one, nonadjacent two-point theorem through parent bias `2/3`, uniform in support distance, by an analytic mean-capped Aidekon tilt. The present run remains on adjacent `{3,4}` laws near and above `lambda=3`, so the mechanisms and parameter regimes are complementary.

There has been substantive progress in each immediate NM13-05 predecessor, so the three-unchanged-run rotation rule does not trigger.

## 2. Frozen offspring assumptions and bias convention

Throughout,

`P(nu=3)=1-p,   P(nu=4)=p`,                                    (2.1)

with no leaves and mean `m=3+p`.

Use **parent bias** `lambda`:

`P(parent | nu=k)=lambda/(lambda+k)`,
`P(each fixed child | nu=k)=1/(lambda+k)`.                       (2.2)

Write the speed as `ell_lambda`. The target is

`ell'_lambda<0`.                                                  (2.3)

The outward child-bias convention is reciprocal:

`beta=1/lambda`,                                                  (2.4)

so wherever differentiable

`v'(beta)=-ell'_{1/beta}/beta^2`.                                (2.5)

All new endpoints lie strictly below `m` at the lower mixture edge of the corresponding theorem rectangle.

## 3. Primary-source and current-literature boundary

Refreshed on 2026-09-20.

1. Ben Arous--Fribergh--Sidoravicius, arXiv:1111.5865, *A proof of the Lyons-Pemantle-Peres monotonicity conjecture for high biases*, states in the outward child-bias convention that `v(beta)` is increasing for `beta>=717` on Galton--Watson trees without leaves.
2. He--Wang--Xiang, arXiv:1610.08151, later published online by Cambridge University Press on 5 March 2025 in *Journal of Applied Probability* 62 (2025), 1044--1052, proves strict parent-bias decrease for

   `0<=lambda<=m1/(1+sqrt(1-1/m1))`

   when the minimum offspring `m1>=2`.
3. Bowditch--Tokushige, arXiv:1906.07913, prove differentiability of the speed in the ballistic CLT regime using regeneration. The finite-depth contractions below also give the needed local derivative domination on the compact strips used here.
4. A bounded fresh search again found Song--Liu's 27 February 2026 deterministic regular-tree result, where speed is monotone in parent bias, but no checked source-wide solution of the random Galton--Watson LPP problem and no checked theorem identical to the random `{3,4}` rectangles below. This is bounded negative evidence, not a novelty certificate.

## 4. Parent-problem before/after and source-level theorem gains

### Parent problem

Before: **OPEN**.  
After: **OPEN**.

No arbitrary-offspring full-interval theorem is claimed.

### Theorem A — crossing class widened again

If

`p>=59/100`,                                                      (4.1)

then the parent-bias speed is strictly decreasing throughout

`BOX: 0<=lambda<=3001/1000=3.001`.                               (4.2)

On the newly certified coupling strip `2<=lambda<=3001/1000`,

`BOX: -ell'_lambda >= 6000/49014001 >0`.                         (4.3)

The immediate predecessor needed `p>=3/5`; therefore the class that crosses `lambda=3` widens by

`3/5-59/100=1/100`.                                              (4.4)

### Theorem B — deeper `p>=2/3` crossing

If

`p>=2/3`,                                                         (4.5)

then strict decrease holds throughout

`BOX: 0<=lambda<=623/200=3.115`,                                 (4.6)

and on `2<=lambda<=623/200`,

`BOX: -ell'_lambda >= 240/2024929 >0`.                           (4.7)

The immediate predecessor endpoint was `31/10=3.1`; the gain is

`623/200-31/10=3/200`.                                          (4.8)

### Theorem C — substantially deeper `p>=4/5` tail

If

`p>=4/5`,                                                         (4.9)

then strict decrease holds throughout

`BOX: 0<=lambda<=337/100=3.37`,                                  (4.10)

and on `2<=lambda<=337/100`,

`BOX: -ell'_lambda >= 60/543169 >0`.                             (4.11)

The earlier proved `p>=4/5` endpoint was `163/50=3.26`; the gain is

`337/100-163/50=11/100`.                                        (4.12)

In child-bias notation, the new coupling strips give `v'(beta)>0` on

`1000/3001 <= beta <= 1/2`,
`200/623 <= beta <= 1/2`,
`100/337 <= beta <= 1/2`,                                       (4.13)

respectively, with the inherited lower-parent-bias pieces extending monotonicity to larger `beta` inside the same subclasses.

No simulated speed sign enters any theorem.

## 5. Consumed harmonic inverse-moment envelope

Let `B=B(lambda)` be the quenched branch escape probability. Conditional on a branch root with `nu=k` children and iid child escapes `B_1,...,B_k`,

`B=S/(lambda+S)`, `S=sum_i B_i`.                                 (5.1)

Put `Z=1/B` and

`z_k=E[Z | nu=k]`, `k=3,4`.                                     (5.2)

The predecessor proved a valid scalar starting envelope

`M_k^(0)=1+lambda/(k d)`,
`d=1-lambda(4-p)/12`,                                           (5.3)

and the finite monotone harmonic map

`T_k(x_3,x_4)`
` =1+lambda sum_{r=0}^k C(k,r)p^r(1-p)^(k-r)`
`      /[(k-r)/x_3+r/x_4]`.                                    (5.4)

Joint concavity and coordinatewise monotonicity of

`H_k(x_1,...,x_k)=1/(sum_i 1/x_i)`                              (5.5)

imply `z<=T(z)`. Thus every finite iterate

`M^(n+1)=T(M^(n))`                                               (5.6)

is a rigorous upper envelope: `z_k<=M_k^(n)`. This run keeps the predecessor's exact finite depth

`n=12`                                                           (5.7)

and writes

`d_k:=1/M_k^(12) <= E[B | nu=k]`.                               (5.8)

No convergence or numerical fixed point is assumed.

The same deterministic four-child comparison gives the type-specific escape ceilings

`u_4=(4-lambda)/4`,
`u_3=3(4-lambda)/(12+lambda)`,                                  (5.9)

so

`0<B<=u_k` conditionally on `nu=k`.                              (5.10)

## 6. New mechanism: retain the distinguished child's own escape

Let

`U=-dB/dlambda >=0`.                                             (6.1)

Differentiating (5.1) at finite depth gives

`U=S/(lambda+S)^2 + lambda sum_i U_i/(lambda+S)^2`.              (6.2)

Equivalently the source part is

`S/(lambda+S)^2 = B(1-B)/lambda`.                               (6.3)

The predecessor bounded a distinguished descendant term by dropping its own `B_i` from the denominator. This run keeps a quantitative piece of that `B_i` exactly.

### Lemma 6.1 — a type-conditioned lower bound on `E[UB]`

Condition on `nu=k`. From (6.3),

`UB >= B^2(1-B)/lambda`.                                        (6.4)

Using `B<=u_k`, Jensen, and (5.8),

`E[UB | nu=k]`
` >= (1-u_k)/lambda * E[B^2 | nu=k]`
` >= (1-u_k)/lambda * E[B | nu=k]^2`
` >= (1-u_k)d_k^2/lambda`.                                     (6.5)

This lower bound is deterministic in the rectangle parameters and requires no sign assumption on any covariance.

### Lemma 6.2 — own-B secant subtraction

For fixed `t>0`, define

`f_t(b)=1/(t+b)^2`.                                              (6.6)

This is convex on `b>=0`. On `0<=b<=u`, its endpoint secant gives

`f_t(b) <= f_t(0)-c_u(t)b`,                                     (6.7)

where

`c_u(t)`
` =[t^{-2}-(t+u)^{-2}]/u`
` =(2t+u)/(t^2(t+u)^2)`.                                       (6.8)

Moreover

`c'_u(t)=-2(3t^2+3tu+u^2)/(t^3(t+u)^3)<0`.                     (6.9)

Now fix a root of degree `n in {3,4}` and a distinguished child. Let `T` be the sum of the other `n-1` child escapes, so the relevant descendant coefficient contains

`1/(lambda+T+B)^2`.                                              (6.10)

The distinguished pair `(B,U)` is independent of `T`. If its root type is `k`, apply (6.7), multiply by `U`, and average. Since every sibling escape is at most `u_4`,

`T <= (n-1)u_4`,                                                (6.11)

and by (6.9) it is safe to replace the secant slope by its value at

`t_n:=lambda+(n-1)u_4`.                                        (6.12)

Consequently

`E[ U/(lambda+T+B)^2 | type k ]`
` <= E[1/(lambda+T)^2] E[U|type k]`
`    - c_{u_k}(t_n) E[UB|type k]`.                              (6.13)

Averaging the distinguished type and inserting (6.5) gives a **strict absolute subtraction** in the annealed derivative recursion.

## 7. Improved annealed contraction

Retain the predecessor's reciprocal-Jensen sibling kernels

`K_j^J(a)=sum_{r=0}^j C(j,r)p^r(1-p)^(j-r)`
`             * a/[a+(j-r)d_3+r d_4]^2`.                       (7.1)

The old scalar contraction coefficient is

`rho=(1-p)3K_2^J(lambda)+p4K_3^J(lambda)`.                      (7.2)

For `lambda>=2`, the source term in (6.2) is bounded by

`A=(1-p)*12(4-lambda)/(12+lambda)^2`
`   +p*(4-lambda)/16`.                                          (7.3)

Define the new own-B subtraction

`delta`
` = sum_{n=3}^4 pi_n n sum_{k=3}^4 pi_k`
`       c_{u_k}(t_n)(1-u_k)d_k^2`,                              (7.4)

where `pi_3=1-p`, `pi_4=p` and `t_n` is (6.12). The factor `lambda` from (6.2) cancels the `1/lambda` in (6.5).

Summing (6.13) over distinguished children and averaging the root degree yields

`BOX: eta:=E U <= A + rho eta - delta`.                         (7.5)

Hence, whenever `rho<1`,

`BOX: eta <= (A-delta)/(1-rho)`.                                (7.6)

This is the central mechanism gain of the run. It is genuinely stronger than the predecessor's `eta<=A/(1-rho)` because it retains a rigorously quantified piece of the same child's escape in the denominator. The checker verifies `delta>0`, `A-delta>0`, and `rho<0.99` on every theorem rectangle.

## 8. Transfer to the Aidekon speed derivative

Retain the predecessor's exact two-state Aidekon reduction. Put `a=lambda-1`; for the symmetrized current degree `k`, define the coefficients `c_k,h_k` as in the predecessor and set

`C=(1-p)c_3+p c_4`,
`theta=p c_4/C`,
`M=3+theta`,
`Delta=h_3/c_3-h_4/c_4`.                                       (8.1)

Then

`ell_lambda=(M-lambda)/(M+lambda)`                              (8.2)

and exactly

`-ell'_lambda`
` =2M/(M+lambda)^2 * [1-lambda g(theta)Delta]`,                 (8.3)

where

`g(theta)=theta(1-theta)/(3+theta)`.                            (8.4)

Let

`mu=(1-p)d_3+p d_4`.                                            (8.5)

With the improved `eta` from (7.6), the inherited score estimate becomes

`Delta<=D(lambda,p)`                                            (8.6)

with

`D=1/(lambda-1)+3 eta K_3^J(lambda-1)/mu-4/(16-lambda)`.       (8.7)

The inherited quantitative branch-addition estimate remains

`c_4/c_3 >= R_*`,                                               (8.8)

where

`R_*=(4/5)[1+(lambda-1)/(4-lambda)`
`       *((1-p)d_3/(3+u_3)+p d_4/(3+u_4))]`.                   (8.9)

Therefore

`theta>=theta_*:=pR_*/(1-p+pR_*)`.                             (8.10)

The coarse ratio `c_4/c_3>=4/5` already puts `theta>1/2` in all three new mixture classes. Since `g` is decreasing on `[1/2,1]`,

`g(theta)<=g(theta_*)`.                                         (8.11)

Thus it suffices to prove

`BOX: lambda g(theta_*)D(lambda,p)<1`.                          (8.12)

The new secant subtraction improves (8.12) only through an analytically proved reduction of `eta`; it does not use simulated walk speeds.

## 9. Rigorous interval certificate

Checker:

`proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T15-22-30Z__own-B-secant-check.cpp`

Actual executed output:

`proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T15-22-30Z__own-B-secant-check.out`.

It uses an explicit directed one-ulp interval implementation for `+,-,*,/`, compiled with

`g++ -O2 -std=c++17 -frounding-math -ffp-contract=off`.

Each intended rational theorem endpoint is first rounded **outward** (`p0` downward and `L` upward), while the target comparison `999/1000` is rounded downward. Adaptive bisection then certifies the complete outer rectangles, not a mesh of sample points.

The executed output gives:

1. `p>=59/100`, `2<=lambda<=3001/1000`:
   - 8,831 visited boxes, 4,416 accepted,
   - `worst_prod=0.99899946348742841 < 999/1000`,
   - `worst_rho=0.98267766308291193 < 0.99`,
   - positive certified own-B subtraction throughout.
2. `p>=2/3`, `2<=lambda<=623/200`:
   - 5,925 visited boxes, 2,963 accepted,
   - `worst_prod=0.99897815318834049 < 999/1000`,
   - `worst_rho=0.98140620013185964 < 0.99`.
3. `p>=4/5`, `2<=lambda<=337/100`:
   - 3,983 visited boxes, 1,992 accepted,
   - `worst_prod=0.99898006430781727 < 999/1000`,
   - `worst_rho=0.9824435420648816 < 0.99`.

The output ends

`ALL_RIGOROUS_INTERVAL_CHECKS_PASS`.

Printed decimals are diagnostics only. The accepted statements are interval enclosures over the full rational rectangles. No simulation establishes monotonicity.

Since `M>=3` and `M<=4`, if the bracket in (8.3) is at least `1/1000`, then uniformly up to a theorem endpoint `L`,

`-ell'_lambda >= 6/[1000(4+L)^2]`.                              (9.1)

Substitution gives exactly the derivative margins in (4.3), (4.7), and (4.11).

## 10. Why each theorem covers from zero

The new own-B contraction is used only on `[2,L]`. The inherited exact all-mixture `{3,4}` escape-tilt theorem proves strict parent-bias decrease for every `p in [0,1]` from `lambda=1` through the exact root of its all-mixture criterion, approximately

`2.8152423075`,                                                  (10.1)

so it overlaps the new strip. Below that, the He--Wang--Xiang minimum-offspring-three theorem covers

`0<=lambda<=3/(1+sqrt(2/3))`.                                   (10.2)

These intervals overlap. Hence every theorem in Section 4 is connected from `lambda=0` to its stated endpoint; no gap is filled by interpolation or simulation.

## 11. Essential soundness checks and failure preservation

- The source-term monotonicity used in (7.3) is valid on `lambda>=2`: for degree four, `S<=4-lambda<=lambda`; for degree three, `S<=3(4-lambda)/4<=lambda`. Thus `S/(lambda+S)^2` is increasing over the relevant source range.
- The secant step has the correct direction because `b ->1/(t+b)^2` is convex, and multiplying by `U>=0` preserves the inequality.
- The own-B subtraction is legitimate without any independence between `B` and `U`; the lower bound (6.5) is pointwise/source based. Only the distinguished pair's independence from its siblings is used.
- The finite harmonic envelope remains finite-step and theorem-valid; no asymptotic fixed-point convergence is invoked.
- Historical P0066 fixed-degree drift remains a failed route, not upgraded to a proof.
- The earlier pointwise minimum-degree escape-elasticity route remains unsuitable at `lambda=3` because of its `1/(3-lambda)` singularity. The present proof never reintroduces that pole.

## 12. Residual obstruction and next attack

The new scalar contraction still averages all distinguished-child types into one `eta=EU`. It retains a positive amount of the child's own `B`, but it does not preserve the full type dependence of `E[U|nu=3]` versus `E[U|nu=4]`, nor the descendant `B-U` correlation beyond the source contribution in (6.5).

The next nonredundant route is therefore a **two-type derivative-moment vector contraction** for

`eta_3=E[U|nu=3]`, `eta_4=E[U|nu=4]`,

with type-specific own-B secant subtractions before averaging. This should exploit that high-mixture rectangles spend more derivative mass in degree-four branches instead of paying the scalar worst mixture. A second distinct fallback is one more regeneration-level joint moment, e.g. a closed recursion for `E[UB|nu=k]`, rather than further iterations of the already-saturated marginal inverse-moment map.

## 13. ledger_delta

```yaml
ledger_delta:
  parent_problem:
    name: "Lyons-Pemantle-Peres biased-walk speed monotonicity on no-leaf supercritical Galton-Watson trees"
    before: OPEN
    after: OPEN
  frozen_family:
    offspring: "P(nu=3)=1-p, P(nu=4)=p"
    parent_bias: lambda
    child_bias: "beta=1/lambda"
  restricted_scope_before:
    crossing_lambda_3: "p>=3/5 through lambda=3001/1000"
    p_ge_2_3: "through lambda=31/10"
    p_ge_4_5: "through lambda=163/50 (earlier own report)"
  restricted_scope_after:
    crossing_lambda_3: "p>=59/100 through lambda=3001/1000"
    p_ge_2_3: "through lambda=623/200"
    p_ge_4_5: "through lambda=337/100"
  source_level_gains:
    crossing_mixture_width: "1/100"
    endpoint_p_ge_2_3: "3/200"
    endpoint_p_ge_4_5: "11/100"
  mechanism_gain:
    statement: "retain the distinguished child's own escape in the derivative denominator using a convex endpoint secant and a source-derived lower bound on E[UB|type]"
    new_bound: "eta <= (A-delta)/(1-rho), delta>0"
    demonstrated_transfer: "full-rectangle certificates lambda*g(theta_*)*D < 999/1000"
  derivative_margins_on_new_strips:
    p_ge_59_100: "6000/49014001"
    p_ge_2_3: "240/2024929"
    p_ge_4_5: "60/543169"
  failed_routes_preserved:
    - "P0066 fixed-degree radial drift sign does not control the changing environment law"
    - "pointwise minimum-degree escape elasticity has a pole at lambda=3"
    - "further marginal inverse-moment iteration alone does not retain distinguished-child B-U correlation"
  computation:
    kind: "directed outward interval arithmetic over complete rational rectangles"
    simulation_used_for_theorem: false
    checker: "2026-09-20T15-22-30Z__own-B-secant-check.cpp"
    output: "2026-09-20T15-22-30Z__own-B-secant-check.out"
    terminal_line: "ALL_RIGOROUS_INTERVAL_CHECKS_PASS"
  status: "PARTIAL_RESTRICTED_THEOREM_CANDIDATES_PENDING_INDEPENDENT_REVIEW"
  runtime_model: "GPT-5.6 Sol"
  reasoning_effort: UNVERIFIED
```

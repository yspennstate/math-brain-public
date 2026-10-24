Model actually run: **GPT-5.6 Sol. Reasoning effort: UNVERIFIED.** GPT-6/maximum was requested in prompt text only; no authenticated applied reasoning-effort telemetry is exposed.

# NM13-05 T06 — reciprocal-Jensen sibling contraction widens and deepens the `{3,4}` lambda=3 crossing

Date: 2026-09-20.  
Repository: private `yspennstate/math-open-problems`, branch `master`.  
Own root: `proofnet24/NM13-05/progress-tree-speed`.  
Status: **PARTIAL / OPEN parent; NEW RESTRICTED-FAMILY THEOREM CANDIDATES pending later independent review.**

## 1. Compact handoff, ownership, predecessor mathematics, and failed routes

The controlling policy is `operations/PROGRESS20_2026-09-20.md` (blob `4a207f06e5c8294c83bcabcd9a1477f26f54b441`). LIVE20 assigns NM13-05 to T06 by escape-probability / regeneration coupling; P01 is the complementary analytic regeneration-derivative worker. No ownership changes are made.

Historical P0066 remains attempted-unsolved. Its old fixed-degree observation

`(k-lambda)/(k+lambda)` decreases with parent bias `lambda`

is preserved as a failed route: the environment seen by the walk changes with `lambda`, so the local drift derivative alone does not control the speed derivative.

Immediate own predecessor consumed:

`proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T10-21-46Z__type-conditioned-branch-ratio-crosses-lambda3.md`.

It proved for the exact `{3,4}` law that `p>=2/3` gives strict decrease through `lambda=603/200=3.015`, and that `p>=3/4` gives strict decrease through `lambda=157/50=3.14` from the prior common-chord run. Its mechanism converted type-conditioned inverse moments into conditional means and then used endpoint chords. Its named next route was to retain inverse moments more directly or obtain joint `B-U` information.

Latest live P01 report consumed:

`proofnet24/P01-progress-speed/runs/2026-09-20/2026-09-20T10-57-50Z__run-report.md`.

P01 is working on nonadjacent minimum-offspring-one laws below `lambda=1`; this run remains complementary.

Latest relevant same-source idea/report consumed:

`artifacts/prob10_2026-09-20/PROB10-06/20260920T1030Z_reciprocal_jensen_idea.md`

and

`runs/prob10_2026-09-20/PROB10-06/20260920T1112Z_reciprocal_jensen_cross_lambda2_71pct_7f3c2a91.md`.

Those prove a reciprocal-Jensen mechanism for the distinct `{2,3}` family and explicitly leave `{3,4}` to NM13-05. This run ports and rederives that mechanism with the `{3,4}` constants, combines it with NM13-05's quantitative branch-addition ratio, and obtains new source-level regions.

There has been substantive movement in each immediate NM13-05 predecessor, so the three-unchanged-run rotation trigger does not apply.

## 2. Frozen assumptions and bias convention

Throughout,

`P(nu=3)=1-p,   P(nu=4)=p`,                                    (2.1)

with no leaves and mean

`m=E nu=3+p`.                                                    (2.2)

Use the **parent-bias** convention

`P(parent | nu=k)=lambda/(lambda+k)`,
`P(each fixed child | nu=k)=1/(lambda+k)`.                      (2.3)

Larger `lambda` points toward the root. Write the speed as `ell_lambda`; the target sign is

`ell'_lambda<0`.                                                 (2.4)

The outward child-bias convention is reciprocal:

`beta=1/lambda`,                                                 (2.5)

so wherever differentiable

`v'(beta)=-ell'_{1/beta}/beta^2`.                               (2.6)

All new endpoints below are strictly inside the transient/ballistic mean boundary `lambda<m` on the asserted `p` ranges.

## 3. Primary-source/current-literature boundary refreshed

The requested primary-source boundary was refreshed on 2026-09-20.

1. Ben Arous--Fribergh--Sidoravicius, arXiv:1111.5865, *A proof of the Lyons-Pemantle-Peres monotonicity conjecture for high biases*, states in the outward child-bias convention that `v(beta)` is increasing for `beta>=717` on Galton--Watson trees without leaves.
2. He--Wang--Xiang, arXiv:1610.08151, later published in *Journal of Applied Probability* 62 (2025), 1044--1052 (online 5 March 2025), proves strict parent-bias decrease for

   `0<=lambda<=m1/(1+sqrt(1-1/m1))`

   when the minimum offspring `m1>=2`. For `m1=3` this source interval extends strictly beyond `lambda=3/2` because `sqrt(2/3)<1`.
3. Aidekon's exact speed/environment representation supplies the scalar two-state reduction below. Bowditch--Tokushige, arXiv:1906.07913 and arXiv:2006.03433, give differentiability/analyticity of speed in the ballistic regime. The contraction proved below also gives the concrete finite-depth derivative domination needed to differentiate the Aidekon coefficients used here.
4. A bounded current search found Song--Liu's 2026 deterministic regular-tree monotonicity result but no checked source-wide solution and no checked theorem identical to the random `{3,4}` regions below. This is bounded negative evidence only, **not** a novelty certificate.

## 4. Parent problem before/after and restricted source-level gains

### Parent problem

Before: **OPEN**.  
After: **OPEN**.

No arbitrary-offspring full-interval theorem is claimed.

### New restricted theorem candidates

**Theorem A (wider crossing class).** If

`p>=51/80`,                                                     (4.1)

then the parent-bias speed is strictly decreasing throughout

`BOX: 0<=lambda<=3001/1000=3.001`.                              (4.2)

On the analytic strip

`3/2<=lambda<=3001/1000`,                                       (4.3)

we have the uniform derivative certificate

`BOX: -ell'_lambda >= 40000/49014001 >0`.                       (4.4)

The interval below `3/2` is supplied by He--Wang--Xiang's minimum-degree-three theorem, which overlaps (4.3).

Before this run, the certified crossing of `lambda=3` required `p>=2/3`. Thus the crossing threshold widens from

`2/3 -> 51/80`,                                                  (4.5)

an exact mixture-width gain

`2/3-51/80 = 7/240`.                                            (4.6)

**Theorem B (deeper `p>=2/3` crossing).** If `p>=2/3`, then strict decrease holds through

`BOX: lambda<=76/25=3.04`,                                      (4.7)

with

`BOX: -ell'_lambda >=25/7744>0`                                 (4.8)

on `3/2<=lambda<=76/25`. The immediate predecessor endpoint was `603/200=3.015`, so the exact endpoint gain is `1/40=0.025`.

**Theorem C (deeper `p>=3/4` crossing).** If `p>=3/4`, then strict decrease holds through

`BOX: lambda<=16/5=3.2`,                                        (4.9)

with

`BOX: -ell'_lambda >=1/324>0`                                  (4.10)

on `3/2<=lambda<=16/5`. The inherited endpoint was `157/50=3.14`, so the endpoint gain is `3/50=0.06`.

In child-bias notation, (4.4), (4.8), (4.10) give `v'(beta)>0` on the reciprocal derivative strips, respectively starting at `beta=1000/3001`, `25/76`, and `5/16` and extending up to `beta=2/3`.

No simulated speed sign enters any theorem.

## 5. Escape recursion and type-conditioned inverse moments

Let `B=B(lambda)` be the quenched probability, starting from a branch root, of escaping to infinity before hitting its parent. If the root has `nu=k` children with iid child escapes `B_1,...,B_k`, then

`B=S/(lambda+S)`, `S=sum_i B_i`.                                (5.1)

Put `Z=1/B`. Then

`Z=1+lambda/S`.                                                  (5.2)

Conditionally on `nu=k`, Cauchy's inequality gives

`1/S <= (1/k^2) sum_i 1/B_i`.                                  (5.3)

Apply this first to finite-depth upper escape approximations. Since

`E(1/nu)=(4-p)/12`,                                              (5.4)

iteration and monotone convergence give

`E Z <=1/d`,                                                     (5.5)

where

`d:=1-lambda(4-p)/12`.                                          (5.6)

Conditioning (5.2) on the root type therefore yields

`E[Z | nu=k] <= 1+lambda/(k d) =: M_k`,                         (5.7)

and define

`d_k:=1/M_k = k d/(k d+lambda)`, `k=3,4`.                       (5.8)

Writing

`R:=12-4lambda+lambda p`,                                       (5.9)

these are exactly

`d_3=R/(12+lambda p)`,
`d_4=R/(12-lambda+lambda p)`.                                  (5.10)

On all three certified rectangles `d>0`; this is also enforced by the exact interval checker through positive denominator tests.

## 6. New mechanism: reciprocal-Jensen deterministic type denominators

For `a>0`, `t>=0`, define

`F_{a,t}(x)=a/(a+t+x)^2`.                                       (6.1)

With `Z=1/B`, put

`G_{a,t}(z)=F_{a,t}(1/z)=a z^2/((a+t)z+1)^2`.                  (6.2)

Direct differentiation gives

`G'(z)=2az/((a+t)z+1)^3 >=0`,                                  (6.3)

`G''(z)=2a(1-2(a+t)z)/((a+t)z+1)^4`.                           (6.4)

Hence `G` is increasing and concave whenever `2(a+t)z>=1`.

Every application below has `B<=1`, hence `Z>=1`, and the smallest base is

`a=lambda-1 >=1/2`.                                             (6.5)

Therefore the concavity condition holds uniformly on every new rectangle. Using (5.7), conditional Jensen gives

`E[F_{a,t}(B)|nu=k]`
` =E[G_{a,t}(Z)|nu=k]`
` <=G_{a,t}(E[Z|nu=k])`
` <=G_{a,t}(M_k)`
` =a/(a+t+d_k)^2`.                                              (6.6)

This is strictly sharper information than the predecessor's route, which first reduced (5.7) to the mean bound `E[B|nu=k]>=d_k` and then paid for a `{0,u_k}` endpoint chord.

For independent sibling branches, repeated conditioning gives the finite exact **deterministic type proxy**

`K_j(a)`
` <= K_j^J(a)`
` := sum_{r=0}^j C(j,r) p^r(1-p)^(j-r)`
`      * a/[a+(j-r)d_3+r d_4]^2.                               (6.7)

The superscript `J` denotes the reciprocal-Jensen proxy. No simulation is involved.

## 7. Annealed derivative contraction without a lambda=3 pole

Let

`U=-dB/dlambda>=0`.                                              (7.1)

Differentiating (5.1) at finite depth gives

`U=S/(lambda+S)^2 + lambda sum_i U_i/(lambda+S)^2`.             (7.2)

Because every vertex has at most four children, comparison with the deterministic four-child tree gives

`B<=u:=(4-lambda)/4`.                                           (7.3)

For root degree three, `S<=3u`, and for degree four, `S<=4u`. Since all new rectangles have `lambda>=3/2`, the first term in (7.2) is bounded by its endpoint value, yielding

`A=(1-p)*12(4-lambda)/(12+lambda)^2 + p*(4-lambda)/16`.         (7.4)

For the derivative term, fix a child `i`, drop its own nonnegative escape from the denominator, and apply (6.7) to its siblings. With `eta=E U`,

`eta <= A + rho eta`,                                           (7.5)

where

`rho=(1-p)*3 K_2^J(lambda)+p*4 K_3^J(lambda)`.                  (7.6)

The exact checker proves on all three theorem rectangles

`BOX: rho<19/20`.                                                (7.7)

Hence

`eta<=A/(1-rho)`.                                               (7.8)

The same coefficient controls finite-depth truncation: writing `B_N` for the depth-`N` upper approximation and applying the mean-value formula to the branch recursion coordinatewise, the own coordinate is again dropped and the sibling kernel is bounded by (6.7). Therefore

`E|B_N-B| <= rho^N <=(19/20)^N`.                                (7.9)

Likewise the expected contribution to the derivative series from generation `N` is bounded geometrically. Thus the finite-depth coefficient derivatives converge absolutely in `L^1`, justifying the differentiation used below.

The key structural gain is that (7.7) remains finite across `lambda=3`; the old pointwise minimum-degree elasticity had a `1/(3-lambda)` pole.

## 8. Aidekon two-state derivative reduction and score bound

Put

`a=lambda-1>0`.                                                  (8.1)

For current offspring `k`, take iid branch pairs `(B_i,U_i)`, `0<=i<=k`, and set

`S_k=sum_i B_i`, `D_k=a+S_k`,                                   (8.2)

`c_k=E[(1/(k+1))*S_k/D_k]`,                                    (8.3)

`h_k=E[(1/(k+1))*sum_i(B_i+aU_i)/D_k^2]`.                       (8.4)

The justified differentiation gives

`c'_k=-h_k`.                                                     (8.5)

Define

`C=(1-p)c_3+p c_4`,
`theta=p c_4/C`,
`M=3+theta`.                                                     (8.6)

Aidekon's symmetrized speed formula is

`ell_lambda=(M-lambda)/(M+lambda)`.                             (8.7)

Let

`Delta=h_3/c_3-h_4/c_4`.                                        (8.8)

Then

`theta'=theta(1-theta)Delta`,                                   (8.9)

and exact differentiation gives

`BOX: -ell'_lambda`
` = 2M/(M+lambda)^2 * [1-lambda*g(theta)*Delta]`,               (8.10)

where

`g(theta)=theta(1-theta)/(3+theta)`.                            (8.11)

Let

`mu=(1-p)d_3+p d_4`.                                            (8.12)

For `c_3`, four iid branches appear. Since `S_3<=4u=4-lambda`,

`D_3<=3`,                                                        (8.13)

so

`c_3>=mu/3`.                                                     (8.14)

The escape-only part of `h_3/c_3` is at most `1/a`. For the derivative part, exchangeability, dropping the own `B_i`, independence, and the reciprocal-Jensen three-sibling bound give

`h_3/c_3 <=1/(lambda-1)+3 eta K_3^J(lambda-1)/mu`.              (8.15)

For `h_4/c_4`, discard the nonnegative derivative term. The five-branch denominator satisfies

`D_4<=lambda-1+5u=(16-lambda)/4`,                               (8.16)

hence

`h_4/c_4>=4/(16-lambda)`.                                       (8.17)

Therefore

`Delta<=D(lambda,p)`,                                            (8.18)

where

`D(lambda,p)`
` :=1/(lambda-1)`
`   +3[A/(1-rho)] K_3^J(lambda-1)/mu`
`   -4/(16-lambda)`.                                            (8.19)

## 9. Quantitative branch addition and final sign reduction

Retain the predecessor's quantitative extra-branch lower ratio. Let

`u_3=3(4-lambda)/(12+lambda)`,
`u_4=(4-lambda)/4`.                                             (9.1)

Coupling the four-branch and five-branch sums and using the conditional escape masses (5.8) gives

`c_4/c_3 >= R_*(lambda,p)`,                                     (9.2)

where

`R_*=(4/5)*[1+(lambda-1)/(4-lambda)`
`              *((1-p)d_3/(3+u_3)+p d_4/(3+u_4))]`.            (9.3)

Hence

`theta>=theta_*:=p R_*/(1-p+p R_*)`.                            (9.4)

In particular the coarse `R_*>=4/5` and `p>=51/80` give

`theta>=204/349>1/2`.                                           (9.5)

Since

`g'(theta)` has the sign of `3-6theta-theta^2`,                 (9.6)

`g` is strictly decreasing for `theta>=1/2`. Therefore

`g(theta)<=g(theta_*)`.                                         (9.7)

If the true `Delta<0`, the square bracket in (8.10) already exceeds one. Otherwise (8.18) and (9.7) reduce the sign problem to the explicit rational inequality

`lambda*g(theta_*)*D(lambda,p)<1`.                              (9.8)

## 10. Exact rational certification

Checker:

`proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T11-29-00Z__reciprocal-jensen-crosses-lambda3-check.cpp`

creation commit `89266d4e56b698680c053d02ae3d597672930eb1`.

Actual executed stdout:

`proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T11-29-00Z__reciprocal-jensen-crosses-lambda3-check.out`

creation commit `6a309ad88ebc76a72069d7d0693b5a048b947d20`.

The checker uses `boost::multiprecision::cpp_rational` interval arithmetic and adaptive exact bisection. Floating displays are diagnostics only; every acceptance comparison is rational.

It proves:

1. `p in [51/80,1]`, `lambda in [3/2,3001/1000]`:

   `rho<19/20`, `lambda*g(theta_*)*D<199/200`.

   Visited 5,349 rational cells, accepted 2,675. From (8.10), `M<=4`, `M>lambda`, and slack `1/200`,

   `-ell'_lambda >=8/(4+3001/1000)^2*(1/200)`
   `                =40000/49014001`.                           (10.1)

2. `p in [2/3,1]`, `lambda in [3/2,76/25]`:

   `rho<19/20`, `lambda*g(theta_*)*D<49/50`.

   Visited 3,743 rational cells, accepted 1,872. Therefore

   `-ell'_lambda >=8/(4+76/25)^2*(1/50)`
   `                =25/7744`.                                  (10.2)

3. `p in [3/4,1]`, `lambda in [3/2,16/5]`:

   `rho<19/20`, `lambda*g(theta_*)*D<49/50`.

   Visited 3,885 rational cells, accepted 1,943. Therefore

   `-ell'_lambda >=8/(4+16/5)^2*(1/50)`
   `                =1/324`.                                    (10.3)

Each invocation ends `ALL_EXACT_CHECKS_PASS`.

The lower-prefactor comparisons use the coarse branch-addition bounds:

- at `p>=51/80`, `theta>=204/349`, so `M>=1251/349>3001/1000`;
- at `p>=2/3`, `theta>=8/13`, so `M>=47/13>76/25`;
- at `p>=3/4`, `theta>=12/17`, so `M>=63/17>16/5`.

Thus `M>lambda`, and `2M/(M+lambda)^2` is minimized over `M<=4` at `M=4`, exactly as used above.

No simulated speed sign establishes any claim.

## 11. Demonstrated mechanism gain, separately from parent scope

**Parent/source scope gain.** The full parent remains OPEN. Within the exact random `{3,4}` family:

- the minimum certified mixture crossing `lambda=3` improves `p>=2/3 -> p>=51/80`, width gain `7/240`;
- the `p>=2/3` endpoint improves `3.015 ->3.04`, gain `0.025`;
- the `p>=3/4` endpoint improves `3.14 ->3.2`, gain `0.06`.

**Mechanism gain.** The predecessor knew `E[1/B|nu=k]` but immediately collapsed it to `E[B|nu=k]>=d_k` and then paid an endpoint chord. This run instead proves concavity after the reciprocal substitution `B -> Z=1/B` and uses the inverse moment directly, replacing each sibling by the deterministic type value `d_3` or `d_4` inside the derivative kernel. The derivative environment penalty therefore uses a two-point deterministic type sum rather than the old three-point `{0,u_3,u_4}` chord proxy. The same type-conditioned masses still feed the independent quantitative branch-addition inequality, so the derivative score `D` and the tilt factor `g(theta)` are both contracted. This is the demonstrated reason the crossing class widens and the old upper-tail endpoints deepen.

This mechanism is complementary to P01's current analytic minimum-offspring-one route.

## 12. Residual obstruction and next nonduplicating attack

The full conjecture remains much broader. Even for `{3,4}`, the present proof does not cover central/lower mixtures across `lambda=3`, nor does it approach the full mean endpoint `lambda=3+p` uniformly.

Two failed/blocked routes remain preserved:

1. fixed-degree local drift ignores the changing environment law;
2. scalar sibling decoupling of the reciprocal derivative `W=U/B^2` is known from the companion `{2,3}` calculation to have a contraction coefficient above one at its hard corner; a successful `W` route must retain a joint `B-U` correlation rather than only marginal moments.

After this run, the best next materially distinct attack is a **two-type inverse-moment vector recursion**. Instead of using the scalar bound `E(1/B)<=1/d` inside (5.7), keep separate unknowns

`M_3=E[1/B | nu=3]`, `M_4=E[1/B | nu=4]`

and close their coupled inequalities before applying reciprocal Jensen. This would sharpen `d_3,d_4` simultaneously in the derivative contraction and branch-addition ratio without reverting to endpoint chords. A second distinct route is a genuinely joint size-biased escape estimate controlling `E[UB]/E U`, which would allow retaining the own branch in the coefficient of `U_i`.

No source-wide closure is claimed.

## 13. ledger_delta

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
    lambda3_crossing_mixture_threshold: p>=2/3
    p_ge_2_3_parent_bias_endpoint: 603/200
    p_ge_3_4_parent_bias_endpoint: 157/50
  restricted_after:
    lambda3_crossing_mixture_threshold: p>=51/80
    crossing_threshold_width_gain: 7/240
    p_ge_51_80_parent_bias_endpoint: 3001/1000
    p_ge_2_3_parent_bias_endpoint: 76/25
    p_ge_2_3_endpoint_gain: 1/40
    p_ge_3_4_parent_bias_endpoint: 16/5
    p_ge_3_4_endpoint_gain: 3/50
  exact_derivative_margins:
    p_ge_51_80: 40000/49014001
    p_ge_2_3: 25/7744
    p_ge_3_4: 1/324
  exact_contraction_certificate: rho < 19/20
  demonstrated_mechanism_gain: reciprocal-Jensen uses conditional inverse-escape moments directly to replace endpoint chords by deterministic type denominators inside sibling derivative kernels; quantitative branch addition simultaneously lowers the escape-tilt penalty
  simulated_speed_signs_used: false
  prior_failed_route_preserved: fixed-degree local drift sign does not control the lambda-dependent environment law
  parent_closed: false
  review_label: NEW_RESTRICTED_THEOREM_CANDIDATES_PENDING_INDEPENDENT_REVIEW
  checker: proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T11-29-00Z__reciprocal-jensen-crosses-lambda3-check.cpp
  checker_commit: 89266d4e56b698680c053d02ae3d597672930eb1
  checker_output: proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T11-29-00Z__reciprocal-jensen-crosses-lambda3-check.out
  checker_output_commit: 6a309ad88ebc76a72069d7d0693b5a048b947d20
  next_attack: two-type inverse-moment vector recursion; alternatively a genuinely joint B-U size-biased escape estimate
```

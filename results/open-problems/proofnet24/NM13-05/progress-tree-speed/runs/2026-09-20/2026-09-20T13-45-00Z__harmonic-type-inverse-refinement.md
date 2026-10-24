Model actually run: **GPT-5.6 Sol. Reasoning effort: UNVERIFIED.** GPT-6/maximum was requested in prompt text only; no authenticated applied reasoning-effort telemetry is exposed.

# NM13-05 T06 — harmonic two-type inverse-moment refinement widens the `{3,4}` lambda=3 crossing

Date: 2026-09-20.  
Repository: private `yspennstate/math-open-problems`, branch `master`.  
Own root: `proofnet24/NM13-05/progress-tree-speed`.  
Status: **PARTIAL / OPEN parent; NEW RESTRICTED-FAMILY THEOREM CANDIDATES pending later independent review.**

## 1. Compact handoff, ownership, and preserved failures

The controlling policy is `operations/PROGRESS20_2026-09-20.md`, blob `4a207f06e5c8294c83bcabcd9a1477f26f54b441`. LIVE20 assigns NM13-05 to T06 by escape-probability / regeneration coupling; P01 is the complementary analytic regeneration-derivative worker. No ownership change is made.

Historical intake P0066 remains attempted-unsolved. Its old fixed-degree observation

`(k-lambda)/(k+lambda)` decreases with parent bias `lambda`

is preserved as a failed route: the law of the environment seen from the walk changes with `lambda`, so the local drift derivative alone does not control the speed derivative.

Immediate own predecessor consumed:

`proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T11-29-00Z__reciprocal-jensen-crosses-lambda3.md`.

That report introduced a scalar reciprocal-Jensen contraction for the exact `{3,4}` law and proved restricted crossings including

- `p>=51/80` through `lambda=3001/1000=3.001`,
- `p>=2/3` through `lambda=76/25=3.04`,
- `p>=3/4` through `lambda=16/5=3.2`.

Its named next route was a two-type inverse-moment vector recursion or genuinely joint `B-U` size biasing. This run executes the first route.

Latest live P01 report consumed:

`proofnet24/P01-progress-speed/runs/2026-09-20/2026-09-20T13-20-00Z__run-report.md`.

P01 works on nonadjacent minimum-offspring-one laws below `lambda=1`, currently using a type-conditioned binomial sibling score. The present `{3,4}` argument near and above `lambda=3` is complementary.

There has been substantive movement in each immediate NM13-05 predecessor, so the three-unchanged-run rotation trigger does not apply.

### Essential check caught and corrected in this run

The immediate predecessor bounded the source term `S/(lambda+S)^2` in the differentiated escape recursion by evaluating it at the deterministic upper endpoint `S_max`. That endpoint evaluation is automatically valid when `S_max<=lambda`. For degree four, `S_max=4-lambda`, so this requires `lambda>=2`; for degree three it requires only `lambda>=12/7`. Thus the displayed common source bound should not be invoked merely from `lambda>=3/2`.

The new proof below **uses that contraction only on `lambda>=2`**, where the source bound is valid. The lower range is stitched with the older all-mixture `{3,4}` theorem, which already proves strict decrease beyond `lambda=2`. This check does not alter historical files. A pre-report checker draft without the suffix `v2` covered `[3/2,L]`; it is intentionally superseded and is **not** used in the theorem. The relied-upon checker/output are the `v2` artifacts listed in Section 12.

## 2. Frozen assumptions and bias convention

Throughout,

`P(nu=3)=1-p,   P(nu=4)=p`,                                   (2.1)

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

All new endpoints are well below `m` on their asserted `p` ranges.

## 3. Primary-source/current-literature boundary refreshed

Refreshed on 2026-09-20.

1. Ben Arous--Fribergh--Sidoravicius, arXiv:1111.5865, *A proof of the Lyons-Pemantle-Peres monotonicity conjecture for high biases*, states in the outward child-bias convention that `v(beta)` is increasing for `beta>=717` on Galton--Watson trees without leaves.
2. He--Wang--Xiang, arXiv:1610.08151, later published online by Cambridge University Press on 5 March 2025 in *Journal of Applied Probability* 62 (2025), 1044--1052, proves strict parent-bias decrease for

   `0<=lambda<=m1/(1+sqrt(1-1/m1))`

   when the minimum offspring `m1>=2`.
3. Aidekon's exact speed/environment representation supplies the two-state effective-degree reduction used below. Bowditch--Tokushige supply differentiability/analyticity in the ballistic regime; the explicit contraction below also gives finite-depth derivative domination on the strip actually used.
4. A bounded current search found Song--Liu's 2026 deterministic regular-tree monotonicity paper but no checked source-wide solution and no checked theorem identical to the random `{3,4}` rectangles below. This is bounded negative evidence only, **not** a novelty certificate.

## 4. Parent problem before/after and source-level gain

### Parent problem

Before: **OPEN**.  
After: **OPEN**.

No arbitrary-offspring full-interval theorem is claimed.

### Restricted-family before

The immediate predecessor certified:

- `p>=51/80` through `lambda=3001/1000`,
- `p>=2/3` through `lambda=76/25=3.04`,
- `p>=3/4` through `lambda=16/5=3.2`.

An older all-mixture `{3,4}` escape-tilt theorem proves strict decrease, for every `p in [0,1]`, at least through the exact root of

`A_3(lambda)<7+4 sqrt(3)`,

whose limiting endpoint is approximately `2.8152423075`. Therefore it covers the entire bridge from the low-bias source theorem to `lambda=2`, and much farther.

### New restricted theorem candidates

**Theorem A — wider class crossing `lambda=3`.** If

`p>=63/100`,                                                     (4.1)

then the parent-bias speed is strictly decreasing throughout

`BOX: 0<=lambda<=3001/1000=3.001`.                              (4.2)

On the newly certified contraction strip

`2<=lambda<=3001/1000`,                                         (4.3)

there is the exact uniform derivative certificate

`BOX: -ell'_lambda >= 8000/49014001 >0`.                        (4.4)

The crossing-mixture threshold therefore widens from `51/80` to `63/100`, an exact gain

`51/80-63/100 = 3/400`.                                         (4.5)

**Theorem B — deeper `p>=2/3` crossing.** If `p>=2/3`, strict decrease holds through

`BOX: lambda<=611/200=3.055`,                                   (4.6)

with

`BOX: -ell'_lambda >=3200/1990921>0`                            (4.7)

on `2<=lambda<=611/200`. The immediate predecessor endpoint was `76/25=3.04`, so the exact endpoint gain is `3/200`.

**Theorem C — deeper `p>=3/4` crossing.** If `p>=3/4`, strict decrease holds through

`BOX: lambda<=321/100=3.21`,                                    (4.8)

with

`BOX: -ell'_lambda >=800/519841>0`                              (4.9)

on `2<=lambda<=321/100`. The immediate predecessor endpoint was `16/5=3.2`, so the exact gain is `1/100`.

In reciprocal child-bias notation, the new derivative strips give `v'(beta)>0`, respectively, for

`1000/3001 <= beta <= 1/2`,
`200/611 <= beta <= 1/2`,
`100/321 <= beta <= 1/2`,                                      (4.10)

within the corresponding offspring subclasses.

No simulated speed sign enters any theorem.

## 5. Escape recursion and the inherited scalar inverse-moment envelope

Let `B=B(lambda)` be the quenched probability, starting from a branch root, of escaping to infinity before hitting its parent. If the branch root has `nu=k` children with iid child escapes `B_1,...,B_k`, then

`B=S/(lambda+S)`, `S=sum_i B_i`.                                (5.1)

Put

`Z=1/B`.                                                         (5.2)

Then

`Z=1+lambda/S`.                                                  (5.3)

Let

`z=E Z`, `z_k=E[Z | nu=k]`, `k=3,4`.                            (5.4)

Cauchy's inequality gives, conditionally on `nu=k`,

`1/S <= (1/k^2) sum_i Z_i`.                                    (5.5)

Since

`E(1/nu)=(4-p)/12`,                                              (5.6)

the finite-depth recursion and monotone convergence give

`z<=1/d`,                                                        (5.7)

where

`d:=1-lambda(4-p)/12`.                                          (5.8)

Consequently

`z_k <= M_k^(0):=1+lambda/(k d)`, `k=3,4`.                      (5.9)

The predecessor stopped here before applying reciprocal Jensen. The new step is to retain child root types inside the harmonic denominator of (5.3).

## 6. New mechanism: harmonic two-type inverse-moment refinement

For positive `x_1,...,x_k`, define the parallel-sum / harmonic denominator

`H_k(x_1,...,x_k):=1/(sum_i 1/x_i)`.                            (6.1)

### Lemma 6.1 — `H_k` is coordinatewise increasing and jointly concave

Write `h=H_k(x)` and `q=sum_i 1/x_i=1/h`. Direct differentiation gives, for every vector `v`,

`(1/2) v^T D^2H_k(x) v`
` =h^2 [ h (sum_i v_i/x_i^2)^2 - sum_i v_i^2/x_i^3 ]`.         (6.2)

By Cauchy,

`(sum_i v_i/x_i^2)^2`
` <= (sum_i 1/x_i)(sum_i v_i^2/x_i^3)`
` = h^(-1) sum_i v_i^2/x_i^3`.                                 (6.3)

Hence (6.2) is nonpositive and `H_k` is concave. Its first derivatives are `h^2/x_i^2>0`, so it is coordinatewise increasing.

### Lemma 6.2 — one exact two-type improvement

Condition on the child root types `T_i in {3,4}`. Since `S=sum_i 1/Z_i`, (5.3) gives

`z_k = 1+lambda E H_k(Z_1,...,Z_k)`.                            (6.4)

If exactly `r` of the `k` child roots have type four, conditional Jensen, Lemma 6.1, and (5.9) imply

`E[H_k(Z_1,...,Z_k) | #four=r]`
` <= 1/[ (k-r)/M_3^(0) + r/M_4^(0) ]`.                         (6.5)

Therefore define

`M_k^(1)`
` :=1+lambda sum_{r=0}^k C(k,r) p^r(1-p)^(k-r)`
`       /[ (k-r)/M_3^(0) + r/M_4^(0) ]`.                       (6.6)

Then

`BOX: z_k<=M_k^(1)`.                                             (6.7)

Set

`d_k:=1/M_k^(1)`.                                                (6.8)

Since `x ->1/x` is convex,

`BOX: E[B | nu=k]=E[1/Z | nu=k] >=1/z_k >= d_k`.                (6.9)

This is strictly stronger than the scalar conditional bound whenever the type-conditioned inverse moments differ. It is the demonstrated mechanism gain of this run.

Remark: (6.6) can be iterated as a monotone upper-envelope map. This run uses only **one** two-type refinement; no asymptotic numerical fixed point is needed.

## 7. Reciprocal Jensen after the two-type refinement

For `a>0`, `t>=0`, define

`F_{a,t}(x)=a/(a+t+x)^2`.                                       (7.1)

With `Z=1/B`, put

`G_{a,t}(z)=F_{a,t}(1/z)=a z^2/((a+t)z+1)^2`.                  (7.2)

Then

`G'(z)=2az/((a+t)z+1)^3 >=0`,                                  (7.3)

`G''(z)=2a(1-2(a+t)z)/((a+t)z+1)^4`.                           (7.4)

On the strip used below, `lambda>=2`; every application has `a>=lambda-1>=1` and `z>=1`, hence `G` is increasing and concave. From (6.7), conditional Jensen gives

`E[F_{a,t}(B) | nu=k] <= a/(a+t+d_k)^2`.                        (7.5)

Repeated sibling conditioning yields the exact deterministic two-type kernel

`K_j(a)`
` <= K_j^J(a)`
` :=sum_{r=0}^j C(j,r)p^r(1-p)^(j-r)`
`       * a/[a+(j-r)d_3+r d_4]^2.                              (7.6)

Compared with the predecessor, the formula is unchanged but the deterministic type inputs `d_3,d_4` are strictly improved by (6.6).

## 8. Corrected annealed derivative contraction on `lambda>=2`

Let

`U=-dB/dlambda>=0`.                                              (8.1)

Differentiating (5.1) at finite depth gives

`U=S/(lambda+S)^2 + lambda sum_i U_i/(lambda+S)^2`.             (8.2)

The deterministic four-child comparison gives

`B<=u:=(4-lambda)/4`.                                           (8.3)

If the root degree is four, `S<=4u=4-lambda<=lambda` for `lambda>=2`. If it is three, `S<=3u<=lambda` already for `lambda>=12/7`. Thus on the common strip `lambda>=2`, `s ->s/(lambda+s)^2` is increasing over the relevant deterministic range, and the first term of (8.2) is bounded by

`A=(1-p)*12(4-lambda)/(12+lambda)^2 + p*(4-lambda)/16`.         (8.4)

For the derivative term, fix a distinguished child, drop its own nonnegative escape from the denominator, and apply (7.6) to its siblings. With

`eta=E U`,                                                       (8.5)

we get

`eta <= A+rho eta`,                                              (8.6)

where

`rho=(1-p)3 K_2^J(lambda)+p 4 K_3^J(lambda)`.                   (8.7)

The exact interval checker proves on all three new rectangles

`BOX: rho<24/25`.                                                (8.8)

Hence

`eta<=A/(1-rho)`.                                                (8.9)

The same coefficient controls finite-depth derivative tails geometrically, giving the domination needed to pass the derivative through the finite-depth approximations on these compact strips.

## 9. Aidekon reduction and the final sufficient inequality

Put

`a=lambda-1`.                                                    (9.1)

For current offspring `k`, take iid branch pairs `(B_i,U_i)`, `0<=i<=k`, and set

`S_k=sum_i B_i`, `D_k=a+S_k`,                                   (9.2)

`c_k=E[(1/(k+1))*S_k/D_k]`,                                    (9.3)

`h_k=E[(1/(k+1))*sum_i(B_i+aU_i)/D_k^2]`.                       (9.4)

Then `c'_k=-h_k`. Define

`C=(1-p)c_3+p c_4`,
`theta=p c_4/C`,
`M=3+theta`.                                                      (9.5)

Aidekon's symmetrized speed formula is

`ell_lambda=(M-lambda)/(M+lambda)`.                             (9.6)

Let

`Delta=h_3/c_3-h_4/c_4`.                                        (9.7)

Then

`theta'=theta(1-theta)Delta`,                                   (9.8)

and exact differentiation gives

`-ell'_lambda`
` = 2M/(M+lambda)^2 * [1-lambda g(theta)Delta]`,                (9.9)

where

`g(theta)=theta(1-theta)/(3+theta)`.                            (9.10)

Let

`mu=(1-p)d_3+p d_4`.                                            (9.11)

The predecessor's score argument, now with the improved `d_k`, gives

`Delta<=D(lambda,p)`,                                           (9.12)

where

`D=1/(lambda-1) + 3 eta K_3^J(lambda-1)/mu - 4/(16-lambda)`.   (9.13)

The inherited quantitative branch-addition bound also improves when (6.9) improves. With

`u_3=3(4-lambda)/(12+lambda)`, `u_4=(4-lambda)/4`,              (9.14)

it gives

`c_4/c_3 >= R_*`,                                               (9.15)

where

`R_*=(4/5)[1+(lambda-1)/(4-lambda)`
`       *((1-p)d_3/(3+u_3)+p d_4/(3+u_4))]`.                   (9.16)

Thus

`theta>=theta_*:=pR_*/(1-p+pR_*)`.                              (9.17)

The coarse branch-addition ratio `c_4/c_3>=4/5` implies, for each new `p` threshold, `theta>1/2`; since `g` is decreasing for `theta>=1/2`,

`g(theta)<=g(theta_*)`.                                         (9.18)

Therefore the exact sufficient inequality is

`BOX: lambda g(theta_*) D(lambda,p) <1`.                         (9.19)

The checker verifies (9.19) by exact rational interval arithmetic over the full rectangles, not by sampled signs.

## 10. Exact certificates and derivative margins

The relied-upon checker is

`proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T13-45-00Z__harmonic-type-inverse-refinement-v2-check.cpp`.

It uses `boost::multiprecision::cpp_rational` interval arithmetic and adaptive bisection. The actual archived output is

`proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T13-45-00Z__harmonic-type-inverse-refinement-v2-check.out`.

It proves:

1. `p in [63/100,1]`, `lambda in [2,3001/1000]`:

   `lambda g(theta_*)D <999/1000`, `rho<24/25`.

   Coarse branch addition gives

   `theta>=4p/(5-p)>=252/437`,

   so

   `M>=3+252/437=1563/437>3001/1000`.                           (10.1)

   Since `M<=4` and `M>lambda`, the prefactor in (9.9) obeys

   `2M/(M+lambda)^2 >=8/(4+3001/1000)^2`.                       (10.2)

   Therefore

   `-ell'_lambda >= 8*(1/1000)/(7001/1000)^2`
   `              =8000/49014001`.                              (10.3)

2. `p in [2/3,1]`, `lambda in [2,611/200]`:

   `lambda g(theta_*)D <99/100`, `rho<24/25`, and the same prefactor argument gives

   `-ell'_lambda >=3200/1990921`.                               (10.4)

3. `p in [3/4,1]`, `lambda in [2,321/100]`:

   `lambda g(theta_*)D <99/100`, `rho<24/25`, and

   `-ell'_lambda >=800/519841`.                                 (10.5)

Actual executed stdout:

```text
MODE=cross63
cross63 p=[0.63,1] lambda=[2,3.001] nit=1
PASS visited=6195 accepted=3098 worst_prod=0.998995 worst_rho=0.959386 min_theta=0.557667 maxdepth=29
theta_base=0.576659 M_base=3.57666 margin=0.000163219 exact_margin=8000/49014001
ALL_EXACT_CHECKS_PASS
MODE=twothirds
twothirds p=[0.666667,1] lambda=[2,3.055] nit=1
PASS visited=4459 accepted=2230 worst_prod=0.989917 worst_rho=0.959865 min_theta=0.594421 maxdepth=25
theta_base=0.615385 M_base=3.61538 margin=0.0016073 exact_margin=3200/1990921
ALL_EXACT_CHECKS_PASS
MODE=threequarters
threequarters p=[0.75,1] lambda=[2,3.21] nit=1
PASS visited=5461 accepted=2731 worst_prod=0.989994 worst_rho=0.959907 min_theta=0.687411 maxdepth=25
theta_base=0.705882 M_base=3.70588 margin=0.00153893 exact_margin=800/519841
ALL_EXACT_CHECKS_PASS
```

The decimal diagnostics are summaries only. Acceptance is by exact rational inequalities inside the checker.

## 11. Why the theorem covers from zero despite using the new contraction only above two

The new machinery is needed only for the high-bias strip. For all `{3,4}` mixtures, the older exact all-mixture escape-tilt criterion proves strict decrease from `lambda=1` through approximately `2.8152423075`, which overlaps the new strip `[2,L]`. Below that, the He--Wang--Xiang theorem for minimum offspring three covers

`0<=lambda<=3/(1+sqrt(2/3))`,

which is strictly larger than `3/2` and overlaps the all-mixture argument. Thus the union is a connected interval from zero through each new endpoint in Section 4.

No claim relies on the corrected source-term bound below `lambda=2`.

## 12. Residual obstruction and next attack

The new harmonic map can be iterated:

`M_k^(n+1)=1+lambda E_T H_k(M_{T_1}^(n),...,M_{T_k}^(n))`.       (12.1)

One iteration already yields a source-level gain. Exploratory arithmetic indicates further iterations can materially improve the rectangles, but an unbounded numerical iteration is not a proof and is not claimed here. A next proof-quality attack is to derive a **closed two-dimensional supersolution** for the monotone map (12.1), avoiding the rational-expression blowup from many interval iterations. A second genuinely distinct option is the still-unresolved joint estimate on the `U`-size-biased escape law, e.g. a lower bound for `E[UB]/E U`, which would retain the distinguished child's own escape in the contraction coefficient instead of dropping it.

The route is not stalled: this run changed mechanism and moved both crossing width and endpoints.

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
    report: proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T11-29-00Z__reciprocal-jensen-crosses-lambda3.md
    crossing_threshold_at_3.001: 51/80
    p_ge_2_over_3_endpoint: 76/25
    p_ge_3_over_4_endpoint: 16/5
  new_scope:
    - p_range: "p>=63/100"
      lambda_endpoint: 3001/1000
      exact_new_strip_margin: 8000/49014001
      crossing_width_gain: 3/400
    - p_range: "p>=2/3"
      lambda_endpoint: 611/200
      exact_new_strip_margin: 3200/1990921
      endpoint_gain: 3/200
    - p_range: "p>=3/4"
      lambda_endpoint: 321/100
      exact_new_strip_margin: 800/519841
      endpoint_gain: 1/100
  mechanism_gain: harmonic_two_type_inverse_moment_refinement
  key_lemma: "H_k(x)=1/(sum_i 1/x_i) is increasing and jointly concave; condition on child root types before Jensen"
  contraction_strip: "lambda>=2 only"
  caught_check_issue: "source endpoint bound S/(lambda+S)^2 at S_max needs S_max<=lambda; do not use common A bound from 3/2"
  exact_checker: proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T13-45-00Z__harmonic-type-inverse-refinement-v2-check.cpp
  exact_output: proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T13-45-00Z__harmonic-type-inverse-refinement-v2-check.out
  checker_code_commit: 98fd72675300f0c886692fa711bb27f17d2a26dd
  checker_output_commit: 1a6c6b2b6abbd6150b6b8bafb1ed9864666b0b33
  review_label: NEW_RESTRICTED_THEOREM_CANDIDATES_PENDING_INDEPENDENT_REVIEW
  next_attack: "closed two-type supersolution for harmonic inverse-moment map; alternatively joint U-size-biased escape estimate"
```

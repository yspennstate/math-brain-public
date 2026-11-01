Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6/maximum is prompt-only on this surface; no authenticated applied-model/reasoning-effort telemetry is exposed, so GPT-6/maximum is not claimed. SOURCE-WIDE STATUS: OPEN -> OPEN. RESTRICTED-FAMILY MOVEMENT: for `P(nu=2)=1-p, P(nu=3)=p`, all `p in [0,1]`, the rigorously certified all-mixture parent-bias endpoint moves from `1.855087` to `1.85527`, a gain of `183/10^6`; on the new strip the exact uniform sign certificate is `-ell'_lambda >= 2000000/235736467729 > 0`. Three materially different attacks: (1) monotone-order-polytope compression of the lower Aidekon score — SUCCESS; (2) a new quantitative upper bound on `c_3/c_2` from symmetrized branch addition — SUCCESS and supplies the main gain; (3) derivative-through-inverse-escape contraction at `lambda=2` — BLOCKED EXACTLY because the degree-two equal-child Lipschitz factor is `lambda/2`, equal to one at `lambda=2`.**

# PROB10-06 — quantitative branch addition and a monotone lower-score polytope

Status: **PARTIAL / OPEN parent.** This report proves a slightly larger all-mixture interval for one genuinely random bounded no-leaf offspring family and a new quantitative branch-addition inequality. It does **not** settle the full Lyons–Pemantle–Peres conjecture. The exact finite certificate is a self-check, not an independent other-track audit. External novelty is **UNVERIFIED**; the literature check below is bounded negative evidence only.

## 1. Controlling instruction, continuity, ownership, and consumed updates

Controlling instruction: `operations/PROB10_2026-09-20.md` on `master`.

The required immutable handoff of R02's preceding Randomstrasse/I0095 target remains preserved:

- `runs/R02/20260920T0005Z_owner_refocus_handoff_I0095_to_PROB10-06_4d8c2a71.md`, creation commit `0439a90108047760ebd8d94ffd7d5b76463666da`.

All historical `artifacts/R02/` remain untouched.

Intake `P0066` remains marked attempted-unsolved (`attempted_un`). The old intake attempt observed only that the fixed-degree local radial drift `(k-lambda)/(k+lambda)` decreases with parent bias; it did not control the bias-dependent environment seen from the walk. Repository search still finds no canonical `operations/claims/P0066.md` to overwrite. This R02 route remains complementary to P01's bounded-support pairwise-Gini route and NM13-05's endpoint-defect wedge.

Consumed own update:

- `runs/prob10_2026-09-20/PROB10-06/20260920T0542Z_pattern_order_bridge_inverse_escape_2f7c91a4.md`, blob `06e4a329d52e7dc57f3ef43648abcfb0008d3eab`.

Its strongest all-mixture theorem for the present `{2,3}` family was strict parent-bias decrease through `lambda=1855087/1000000=1.855087`. It also proved `E[B^{-1}]<=1/(1-lambda E[nu^{-1}])`, which remains finite at `lambda=2` for every `p>0`, but did not control the derivative score there.

Consumed neighboring updates:

- `proofnet24/P01-progress-speed/runs/2026-09-20/2026-09-20T05-00-49Z__run-report.md`, blob `b40364735a57b991c05c4505302d63df28361f76`: bounded-support low-parent-bias derivative regions, including minimum offspring one, by a pairwise-Gini covariance method.
- `proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T04-23-44Z__parametric-defect-budget-wedge.md`, blob `3e7f47701ada687f95bac795346966675d848324`: for adjacent `{d,d+1}` laws, rare endpoint mass at most `delta` gives strict decrease through `lambda<=d-delta`; it still does not cross the minimum-degree boundary for central mixtures.
- root `POSTED.md` current exclusion registry: no posted source-wide P0066 closure is recorded; restricted results do not close unrestricted parents.

The new idea was written before the new checker:

- `artifacts/prob10_2026-09-20/PROB10-06/20260920T0612Z_monotone_lower_pattern_idea.md`, creation commit `a497f57d0434466179a3110f39f94c377971624e`.

Exact checker and executed stdout:

- `artifacts/prob10_2026-09-20/PROB10-06/20260920T0628Z_monotone_order_branch_ratio_check.py`, creation commit `886cf2cafe8dc49f6b18139518e016ae144b9584`;
- `artifacts/prob10_2026-09-20/PROB10-06/20260920T0628Z_monotone_order_branch_ratio_check.out`, creation commit `63f85aba1f9cd231a8743435ab37cac887f10b74`.

The process exited with code zero and stdout ends `ALL_EXACT_CHECKS_PASS`. A host Python startup warning from an unrelated spreadsheet-runtime warmup appeared on stderr and is explicitly separated from the checker output.

## 2. Exact source problem and bias convention

Let `nu` be the Galton–Watson offspring variable. The source setting is

`P(nu=0)=0`, `m=E nu in (1,infinity)`.

Thus there are **no leaves**.

In the child-bias convention of Ben Arous–Fribergh–Sidoravicius, at a vertex with `k` children,

`P(parent)=1/(1+beta k)`,
`P(each fixed child)=beta/(1+beta k)`.

Larger `beta` pushes away from the root. The original conjectural transient interval is `beta in (1/m,infinity)`, and the conjecture asks the limiting speed `v(beta)` to be increasing there.

This track uses reciprocal parent bias

`lambda=1/beta`.

Then

`P(parent)=lambda/(lambda+k)`,
`P(each fixed child)=1/(lambda+k)`.

Larger `lambda` pushes toward the root. Writing `ell_lambda=v(1/lambda)`, the equivalent conjecture is that `ell_lambda` is nonincreasing on `0<=lambda<m`.

The restricted family here is

`P(nu=2)=1-p`, `P(nu=3)=p`, `0<=p<=1`,

with mean `m=2+p`. The new endpoint `1.85527<2<=m` is inside the transient interval for every `p`.

## 3. Current primary-literature boundary checked this run

Primary navigation was refreshed on 20 September 2026.

- Ben Arous–Fribergh–Sidoravicius, arXiv:1111.5865, submitted 24 November 2011, states in its abstract that child-bias speed on a Galton–Watson tree without leaves is increasing for `beta>=717`.
- Aïdékon, arXiv:1111.4313 / PTRF 159 (2014), gives the exact speed representation via the environment seen from the particle used below.
- He–Wang–Xiang, arXiv:1610.08151, now *Journal of Applied Probability* 62 (2025), 1044–1052, published online 5 March 2025, proves strict parent-bias decrease on

  `0<=lambda<=m1/(1+sqrt(1-1/m1))`

  when minimum offspring `m1>=2`; its abstract records Aïdékon's earlier source-uniform `lambda<=1/2` improvement.
- Song–Liu, *AIMS Mathematics* 11 (2026), 4787–4804, treats deterministic regular trees, not genuinely random offspring laws.

A bounded fresh search found no checked source-wide resolution and no checked theorem identical to the quantitative `{2,3}` branch-ratio lemma or endpoint below. This is not an exhaustive novelty certificate.

## 4. Parent, restricted, and mechanism metrics

### Parent source metric

Before: **OPEN**.  
After: **OPEN**.

No theorem for every no-leaf offspring law on all `0<=lambda<m` is claimed.

### Restricted source-level metric

Before: for every `p in [0,1]` in the `{2,3}` family, strict decrease was certified through

`lambda<=1855087/1000000 = 1.855087`.

After:

`BOX: lambda<=185527/100000 = 1.85527`.

Gain:

`BOX: 183/1000000 = 0.000183`.

On the genuinely new strip

`1855087/1000000 <= lambda <= 185527/100000`,

this report proves uniformly in every `p in [0,1]`

`BOX: -ell'_lambda >= 2000000/235736467729`
`                     = 8.4840500889... x 10^(-6) > 0`.

### Auxiliary mechanism delta

The old static branch-addition bound was

`3/4 <= t:=c_3/c_2 <=1`.

This report proves, throughout the larger analytic range described in Section 7 whenever the polynomial condition holds,

`BOX: t <= (4-lambda)/(2(3-lambda)) < 1`.

At the new endpoint this gives

`t <= 214473/228946 = 0.9367842198...`.

This is the main new analytic mechanism.

## 5. Consumed exact two-point derivative reduction

For `1<lambda<2`, let `B` be the quenched escape probability and `U=-B'>=0`. For conditional current offspring value `k`, take iid copies `B_0,...,B_k`, with corresponding `U_i`, and put

`S_k=sum_i B_i`, `D_k=lambda-1+S_k`,

`c_k=E[(1/(k+1))*S_k/D_k]`,

`h_k=E[(1/(k+1))*sum_i(B_i+(lambda-1)U_i)/D_k^2]`.

The inherited dominated-differentiation argument gives `c_k'=-h_k` on compact strips below 2.

For the `{2,3}` law define

`C=(1-p)c_2+p c_3`,
`theta=p c_3/C`,
`M=2+theta`.

Aïdékon's symmetrized formula gives exactly

`ell_lambda=(M-lambda)/(M+lambda)`.

Writing

`Delta=h_2/c_2-h_3/c_3`,

we have

`theta'=theta(1-theta)Delta`,

and hence

`BOX: -ell'_lambda`
` = 2(2+theta)[1-lambda g(theta)Delta]/(2+theta+lambda)^2`,       (5.1)

where

`g(theta)=theta(1-theta)/(2+theta)`.                             (5.2)

Thus it suffices to prove `lambda g(theta)Delta<1`.

## 6. Attack 1 — monotone-order polytope for the lower `h_3/c_3` score

The previous report proved stochastic ordering

`B | {nu=3} >=_st B | {nu=2}`.                                  (6.1)

For the four-branch term defining `c_3`, condition on exactly `m` of the four branch roots having offspring type 3. Let `T_m` be the sum of their escape probabilities together with the type-2 branches, and let

`Y_m=E[phi(T_m)]`, `phi(s)=s/(lambda-1+s)`.

Because `phi` is increasing for `lambda>1`, the same coupling gives

`BOX: Y_0<=Y_1<=Y_2<=Y_3<=Y_4`.                                (6.2)

The inherited exact envelopes provide, on the new lambda strip,

`lo_m <= Y_m <= hi_m`,                                          (6.3)

and lower conditional score constants `R_m^L` with

`R_0^L>R_1^L>...>R_4^L>0`.                                     (6.4)

Therefore

`h_3/c_3 >= F_p(Y)`                                              (6.5)

with

`F_p(y)= [sum_m pi_m(p)y_m R_m^L]/[sum_m pi_m(p)y_m]`,
`pi_m(p)=C(4,m)p^m(1-p)^(4-m)`,                                 (6.6)

and `y` restricted to the compact order polytope

`P={lo_m<=y_m<=hi_m, y_0<=...<=y_4}`.                           (6.7)

### Why checking vertices is complete

The denominator of `F_p` is positive on `P`. If `y=t y^(1)+(1-t)y^(2)`, then

`F_p(y)` is a convex combination of `F_p(y^(1))` and `F_p(y^(2))` with positive weights proportional to their denominators. Hence a minimum is attained at an extreme point of `P`.

A vertex of a 5-dimensional polytope has five linearly independent active constraints. The exact checker enumerates all 5-subsets of the 14 candidate equalities

`y_m=lo_m`, `y_m=hi_m`, `y_m=y_{m+1}`,

solves each rational system, and retains precisely the feasible solutions. It finds exactly

`BOX: 64 extreme points`.

No sampling is used.

## 7. Attack 2 — new quantitative branch-addition upper bound

Let

`a=lambda-1>0`,
`phi(s)=s/(a+s)`.

For an unconditional branch escape variable in the `{2,3}` family, the inherited type envelopes imply

`b <= B <= u`,                                                   (7.1)

where

`b=(2-lambda)/2`, `u=(3-lambda)/3`.                             (7.2)

Indeed the type-3 lower bound dominates `b`, and the type-2 upper bound is below `u`.

Let `X_1,...,X_4` be iid copies of `B`, `S=sum_i X_i`, and define

`F_j=E phi(X_1+...+X_j)`.

Then

`c_2=F_3/3`, `c_3=F_4/4`,

so

`t:=c_3/c_2=(3/4)F_4/F_3`.                                     (7.3)

By symmetry,

`F_3=E[(1/4)sum_i phi(S-X_i)]`.                                 (7.4)

For deterministic `x_i in [b,u]`, put

`A(x)= [(1/4)sum_i phi(S-x_i)]/phi(S)`.                         (7.5)

I now prove that `A` is coordinatewise increasing on the range needed here.

Fix `j`, put `y_i=S-x_i`, and differentiate. After multiplication by positive denominators, the sign of `partial_j A` is the sign of

`H_j = S(a+S) sum_{i!=j} 1/(a+y_i)^2`
`      - sum_i y_i/(a+y_i)`.                                    (7.6)

For `i!=j`, subtract the corresponding `y_i/(a+y_i)` term:

`S(a+S)/(a+y_i)^2 - y_i/(a+y_i)`
` = x_i(a+S+y_i)/(a+y_i)^2`.                                   (7.7)

It is therefore enough that, for every `i!=j`,

`(a+S+y_i)/(a+y_i)^2 >= 1/(a+y_j)`.                            (7.8)

Let `z` be the sum of the two coordinates other than `i,j`. The numerator after cross multiplication in (7.8) equals exactly

`D_ij`
`=2a x_i+a z+x_i^2+2x_i x_j+3x_i z-x_j^2+z^2`.                 (7.9)

Using `x_i,x_j>=b`, `x_j<=u`, and `z>=2b`,

`D_ij >= 4ab+13b^2-u^2`
`       =(41 lambda^2-228 lambda+288)/36`.                      (7.10)

The quadratic is positive throughout the present strip; the exact checker certifies this directly. In fact its smaller zero is

`lambda_0=(114-6 sqrt(33))/41 = 1.9398201005...`,               (7.11)

so the argument is valid for `1<lambda<lambda_0`.

Hence `A` is coordinatewise increasing and is minimized at `x_1=...=x_4=b`. Thus

`A(x)>=phi(3b)/phi(4b)`
`     =3(a+4b)/[4(a+3b)]`.                                     (7.12)

Taking expectations in (7.4),

`F_3 >= 3(a+4b)/[4(a+3b)] F_4`.                                (7.13)

Substitute into (7.3):

`BOX: c_3/c_2 <= (a+3b)/(a+4b)`
`                  =(4-lambda)/(2(3-lambda))`.                  (7.14)

The lower branch-addition bound `c_3/c_2>=3/4` remains available. Therefore on the new strip, with

`T=(4-L)/(2(3-L))=214473/228946`,                               (7.15)

we have

`3/4 <= t <= T`.                                                 (7.16)

Since

`theta=p t/(1-p+p t)`,                                          (7.17)

this gives the coupled bounds

`theta_L=3p/(4-p) <= theta <= theta_U=pT/(1-p+pT)`.             (7.18)

This is strictly stronger than the previous `theta<=p`.

## 8. Completing the new derivative strip

For the upper `h_2/c_2` score, the conditional escape weights are increasing in the number `m` of type-3 branches, while the frozen upper scores `R_m^U(L)` are decreasing. Reverse Chebyshev therefore gives

`h_2/c_2 <= U(p):=sum_{m=0}^3 C(3,m)p^m(1-p)^(3-m)R_m^U(L)`.    (8.1)

For the lower term, Section 6 gives

`h_3/c_3 >= min_{y in P} F_p(y)`,                               (8.2)

and the minimum is one of the 64 exact vertices.

To bound `g(theta)`, note

`g'(theta)` has numerator `2-4theta-theta^2`.                   (8.3)

The checker verifies exactly that at `p=23/50`, `theta_U` is still on the increasing side:

`2-4theta_U-theta_U^2`
`=380337478845/13725594907249 >0`.                              (8.4)

Thus for `0<=p<=23/50`,

`g(theta)<=g(theta_U)`.                                          (8.5)

At `p=53/100`, the lower bound is already on the decreasing side:

`2-4theta_L-theta_L^2=-5155/120409<0`.                          (8.6)

Hence for `53/100<=p<=1`,

`g(theta)<=g(theta_L)`.                                          (8.7)

On the middle interval use the rational global majorant

`g(theta)<=5-2sqrt(6)<101021/1000000`.                          (8.8)

For every one of the 64 lower-score vertices and each of these three `p` regimes, the exact Bernstein checker proves

`lambda g(theta) Delta <= 19999/20000 <1`                       (8.9)

uniformly for

`A<=lambda<=L`,

where

`A=1855087/1000000`, `L=185527/100000`.                         (8.10)

There are `64 x 3 = 192` exact product certificates; maximum Bernstein subdivision depth is 5. Together with (5.1),

`-ell'_lambda`
` >= 4(1-19999/20000)/(3+L)^2`
` = 2000000/235736467729 >0`.                                  (8.11)

This proves the new strip. Stitching with the inherited theorem through `A` gives strict decrease for all `p` on `0<=lambda<=L`.

## 9. Attack 3 — exact obstruction to the naive inverse-escape derivative contraction

The previous report's inverse-escape moment bound suggested differentiating the recursion through `lambda=2`. Write `Y=1/B`. For children with escape probabilities `B_i` and weights

`w_i=B_i/sum_j B_j`,

the derivative recursion has child-Lipschitz coefficient

`lambda sum_i w_i^2`.                                           (9.1)

A pathwise/sup-norm contraction would require this coefficient to be `<1`.

At a degree-two vertex with equal child escapes,

`w_1=w_2=1/2`,

so the coefficient is exactly

`lambda(1/4+1/4)=lambda/2`.                                     (9.2)

At `lambda=2` this is exactly 1, and above 2 it exceeds 1. Since degree two has positive probability for every `p<1`, the natural uniform derivative contraction cannot cross the minimum-degree boundary. This is an exact obstruction to this **method**, not a counterexample to monotonicity. An expectation-level, occupation-weighted contraction could still work and remains a live route.

## 10. Exact checks actually executed

The archived checker executed with process exit code zero. Its stdout records:

- 27 lambda-envelope monotonicity checks, all passing without subdivision;
- exactly 64 feasible extreme points of the monotone lower-score polytope;
- exact positivity of `(41 lambda^2-228 lambda+288)/36` on the strip;
- `c_3/c_2 <=214473/228946` at the new endpoint;
- exact left/right monotonicity signs for `g` at `p=23/50` and `p=53/100`;
- 192 exact rational/Bernstein product certificates, maximum subdivision depth 5;
- exact uniform derivative margin `2000000/235736467729`;
- exact derivative-contraction obstruction factor 1 at `lambda=2`, degree two, equal children;
- final line `ALL_EXACT_CHECKS_PASS`.

These are **self-checks**, not independent audits.

## 11. Remaining full-scope gap and next mathematical obligation

The source-wide conjecture remains open. Even for the `{2,3}` family, the interval

`1.85527 < lambda < 2+p`                                        (11.1)

is not fully covered for central mixtures. The present pointwise elasticity envelopes still become singular as `lambda` approaches 2 from below, while the inverse-escape first moment stays finite at 2 for `p>0` but does not by itself control derivative sensitivity.

The sharp next obligation within this parent problem is therefore not another micro-optimization of the endpoint. It is an **expectation-level derivative recursion** that exploits the smoothing from random degree three and can cross `lambda=2`. Section 9 shows exactly why the naive pathwise contraction cannot do so: the degree-two equal-child mode is critical. A successful route must average that mode against either the type-3 mass, the Aïdékon occupation tilt, or a higher inverse-escape moment.

## 12. Structured ledger delta

```yaml
ledger_delta:
  target: PROB10-06 / P0066 Lyons-Pemantle-Peres speed monotonicity
  parent_status_before: OPEN
  parent_status_after: OPEN
  offspring_family: P(nu=2)=1-p, P(nu=3)=p, all p in [0,1]
  parent_bias_convention: lambda=1/beta; increasing lambda pushes toward root
  restricted_endpoint_before: 1.855087
  restricted_endpoint_after: 1.85527
  restricted_endpoint_gain: 0.000183
  new_strip_uniform_sign_margin: 2000000/235736467729
  mechanism_before: 3/4 <= c3/c2 <= 1
  mechanism_after: c3/c2 <= (4-lambda)/(2(3-lambda)) on the proved polynomial-positive regime
  exact_checker: PASS
  checker_product_certificates: 192
  lower_order_polytope_vertices: 64
  independent_audit: none
  novelty: UNVERIFIED
  remaining_gap: central mixtures across lambda=2 and then full 0<=lambda<2+p; source-wide all no-leaf laws
```

No scheduler state, email, Drive, public posting, permissions, workflows, shared roots, or peer-track files were changed in this run.
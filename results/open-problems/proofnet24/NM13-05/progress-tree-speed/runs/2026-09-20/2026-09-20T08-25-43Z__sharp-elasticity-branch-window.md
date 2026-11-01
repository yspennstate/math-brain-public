Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6/maximum was requested, but no authenticated applied-model/reasoning-effort telemetry is exposed, so GPT-6/maximum is not claimed. SUBSTANTIVE MOVEMENT: the Lyons--Pemantle--Peres parent problem remains OPEN, but for the exact no-leaf family `P(nu=3)=1-p, P(nu=4)=p` a new hybrid of quantitative branch-addition and a regeneration-derived lower escape-elasticity cone proves strict parent-bias decrease through `lambda=71/25=2.84` for every `p<=1/3` or `p>=2/3`. It also pushes the predecessor tails to `lambda=1429/500=2.858` for `p<=1/4` and `lambda=2861/1000=2.861` for `p>=3/4`. No simulated speed sign is used.**

# NM13-05 T06 — sharp escape elasticity plus quantitative branch addition for `{3,4}` offspring

Date: 2026-09-20.  
Repository: private `yspennstate/math-open-problems`, branch `master`.  
Own root: `proofnet24/NM13-05/progress-tree-speed`.  
Parent target: T06 / historical intake P0066, Lyons--Pemantle--Peres monotonicity of biased-walk speed on a supercritical Galton--Watson tree without leaves.  
Status: **PARTIAL / OPEN parent; NEW RESTRICTED THEOREM CANDIDATES pending later independent review.**

## 1. Compact continuity handoff and route separation

The controlling owner instruction is `operations/PROGRESS20_2026-09-20.md`. LIVE20 assigns NM13-05 to T06 by escape-probability/regeneration coupling and P01 to a complementary analytic regeneration/derivative route.

Historical P0066 remains attempted-unsolved. Its old observation was only that at fixed offspring count `k` the local radial drift

`(k-lambda)/(k+lambda)`

decreases with the parent bias `lambda`. That does not control the `lambda`-dependent environment seen from the walker, so the measure-change term remained unsigned. This failure is preserved and not relabelled as progress.

Immediate own predecessor:

`proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T07-25-00Z__quantitative-branch-addition-window.md`.

It froze the same `{3,4}` family, proved a two-sided quantitative branch-ratio window, and reached:

- `p<=1/3` through `lambda=1131/400=2.8275`;
- `p>=2/3` through `lambda=283/100=2.83`;
- `p<=1/4` through `lambda=356/125=2.848`;
- `p>=3/4` through `lambda=713/250=2.852`.

Its derivative budget still used the weaker lower elasticity contribution `4/(16-lambda)` from the degree-four branch.

Latest live P01 consumed:

`proofnet24/P01-progress-speed/runs/2026-09-20/2026-09-20T08-01-15Z__run-report.md`.

P01 now treats minimum-offspring-one two-point laws such as `{1,12}` by a common-mean chord/Jensen compression below the pipe threshold `lambda=1`. The present run remains in minimum degree three, near `lambda=3`, and uses branch-addition plus escape elasticity. There is no duplication of P01's principal offspring class or proof mechanism.

Latest relevant non-LIVE20 T06 work consumed:

`runs/prob10_2026-09-20/PROB10-06/20260920T0716Z_moderate_mixture_rectangle_5d8b2e41.md`.

That stream treats `{2,3}` and reaches `lambda=1.87` on `p<=1/4`; an earlier report in that stream proved the logarithmic escape-elasticity cone used below. This run ports that cone to the degree-four branch and combines it with NM13-05's distinct five-branch localization to obtain new `{3,4}` regions.

`POSTED.md` / current repository search records no posted source-wide P0066 closure. Restricted T06 theorems remain restricted and do not close the parent conjecture.

## 2. Frozen source assumptions and bias convention

Throughout,

`P(nu=3)=1-p,   P(nu=4)=p,   0<=p<=1`.                         (2.1)

There are no leaves and `E nu=3+p`.

Use the **parent-bias** convention

`P(parent | nu=k)=lambda/(lambda+k)`,
`P(each fixed child | nu=k)=1/(lambda+k)`.                      (2.2)

Larger `lambda` pushes toward the root. Write the speed as `ell_lambda`; the desired sign is

`ell'_lambda<0`.                                                 (2.3)

The child-bias convention of Ben Arous--Fribergh--Sidoravicius is reciprocal:

`beta=1/lambda`.                                                 (2.4)

Hence, wherever differentiable,

`v'(beta)=-ell'_{1/beta}/beta^2`.                               (2.5)

All new endpoints are below `3<=E nu`, hence strictly inside the transient parent-bias interval for every `p` considered.

## 3. Primary-source and current-literature boundary refreshed

Bounded checks on 2026-09-20 recovered:

1. Ben Arous--Fribergh--Sidoravicius, arXiv:1111.5865, *A proof of the Lyons-Pemantle-Peres monotonicity conjecture for high biases*. In its child-bias convention the abstract states that `v(beta)` is increasing for `beta>=717` on Galton--Watson trees without leaves.
2. He--Wang--Xiang, arXiv:1610.08151, later published in *Journal of Applied Probability* 62 (2025), 1044--1052, proves strict parent-bias decrease on

   `0<=lambda<=m1/(1+sqrt(1-1/m1))`

   when the minimum offspring is `m1>=2`.
3. Aidekon's exact speed representation supplies the scalar reduction below; Bowditch--Tokushige supplies differentiability in the ballistic regime.
4. The 2026 Song--Liu paper concerns deterministic regular trees, not genuinely random offspring laws.

The fresh bounded search did not surface a checked source-wide resolution or a checked theorem identical to the `{3,4}` regions below. This is bounded negative evidence only, **not** a novelty certificate.

## 4. Parent-problem before/after and demonstrated source-level movement

### Parent problem

Before: **OPEN**.  
After: **OPEN**.

No theorem for every no-leaf offspring law on the full transient interval is claimed.

### Restricted `{3,4}` scope before

The immediate predecessor certified the four endpoint-mixture regions listed in Section 1.

### Restricted `{3,4}` scope after

**Theorem A — moderate endpoint mixtures.** For the offspring law (2.1), if

`0<=p<=1/3  or  2/3<=p<=1`,                                     (4.1)

then `ell_lambda` is strictly decreasing throughout

`0<=lambda<=71/25=2.84`.                                        (4.2)

On the newly proved derivative segment `1<=lambda<=71/25`, exact uniform margins are

- for `p<=1/3`,

  `-ell'_lambda >= 40394875/88040761947 >0`;                    (4.3)

- for `p>=2/3`,

  `-ell'_lambda >= 1146638750/518639400279 >0`.                 (4.4)

Relative to the immediate predecessor, the parent-bias endpoint gains are exactly `1/80` on the lower moderate range and `1/100` on the upper moderate range.

**Theorem B — sharpened tails.** In addition,

- if `p<=1/4`, strict decrease holds through

  `lambda<=1429/500=2.858`,                                     (4.5)

  with

  `-ell'_lambda >= 520503603188527000000/489184214164321963989159 >0`; (4.6)

- if `p>=3/4`, strict decrease holds through

  `lambda<=2861/1000=2.861`,                                    (4.7)

  with

  `-ell'_lambda >= 666649795394000000/2757595757861424166183 >0`. (4.8)

These improve the predecessor tail endpoints by `1/100` and `9/1000`, respectively.

In child-bias notation, Theorem A gives `v'(beta)>0` on `25/71<=beta<=1` for the indicated mixtures; Theorem B gives the corresponding reciprocal intervals.

The part below `lambda=1` is already contained in the published He--Wang--Xiang monotonicity interval; the new derivative proof below treats `1<=lambda<L<3`.

## 5. Exact scalar derivative reduction

Work on `1<lambda<3`. Let `B` be the quenched probability, starting at a vertex, of escaping to infinity before hitting its parent, and put

`U=-dB/dlambda>=0`.

Conditional on current offspring `k`, take iid copies `B_0,...,B_k` with corresponding `U_i`. Define

`S_k=sum_i B_i`,
`D_k=lambda-1+S_k`,

`c_k=E[(1/(k+1))*S_k/D_k]`,                                    (5.1)

`h_k=E[(1/(k+1))*sum_i(B_i+(lambda-1)U_i)/D_k^2]`.             (5.2)

On compact strips below 3, dominated differentiation gives

`c'_k=-h_k`.                                                     (5.3)

Set

`C=(1-p)c_3+p c_4`,
`theta=p c_4/C`,
`M=3+theta`.                                                     (5.4)

Aidekon's symmetrized speed formula becomes

`ell_lambda=(M-lambda)/(M+lambda)`,                              (5.5)

so

`ell'_lambda=2(lambda M'-M)/(M+lambda)^2`.                      (5.6)

Writing

`Delta=h_3/c_3-h_4/c_4`,                                       (5.7)

one has

`theta'=theta(1-theta)Delta`,                                   (5.8)

and therefore

`G:=M-lambda M'`
` =3+theta-lambda theta(1-theta)Delta`,                          (5.9)

with

`-ell'_lambda=2G/(M+lambda)^2`.                                 (5.10)

The task is to give a positive lower bound on `G`.

## 6. Quantitative branch-addition localization retained from the predecessor

For `1<lambda<3`, standard regular-tree comparison gives the pathwise escape window

`b=(3-lambda)/3 <= B <= u=(4-lambda)/4`.                        (6.1)

Let

`phi(s)=s/(lambda-1+s)`,
`F_n=E phi(B_1+...+B_n)`.                                       (6.2)

Then

`c_3=F_4/4`, `c_4=F_5/5`,                                      (6.3)

so

`t:=c_4/c_3=(4/5)F_5/F_4`.                                     (6.4)

The always-valid concavity argument gives

`4/5<=t<=1`.                                                     (6.5)

The predecessor's five-branch quantitative refinement states that when

`q(lambda):=29 lambda^2-328 lambda+720>0`,                       (6.6)

then

`BOX: t <= U(lambda):=(9-lambda)/(2(6-lambda))`.                (6.7)

For completeness, here is the finite core. For deterministic `x_1,...,x_5 in [b,u]`, set `S=sum x_i` and

`A(x)=[(1/5)sum_i phi(S-x_i)]/phi(S)`.                           (6.8)

A coordinate derivative reduces to the inequality

`D=2ax+az+x^2+2xy+3xz-y^2+z^2 >=0`,                             (6.9)

with `a=lambda-1`, `x,y in [b,u]` and `z` the sum of the remaining three coordinates. Using `x,y>=b`, `y<=u`, `z>=3b`,

`D>=5ab+21b^2-u^2=q(lambda)/48`.                                (6.10)

Thus `A` is coordinatewise increasing. Its minimum is the all-`b` point, so the `phi(S)`-weighted expectation of `A` gives

`F_4/F_5 >= phi(4b)/phi(5b)`,                                   (6.11)

which is exactly (6.7). Also

`U'(lambda)=3/[2(6-lambda)^2]>0`.                               (6.12)

Every endpoint used below satisfies `q(L)>0`, so (6.7) is valid throughout `[1,L]` because `q` is decreasing on `[1,3]`.

## 7. New hybrid step: regeneration-derived lower elasticity on the degree-four branch

The predecessor bounded `Delta` with a weak lower contribution from `h_4/c_4`. The present gain is to combine branch addition with the stronger logarithmic escape-elasticity cone.

Let

`q_B:=U/B=-B'/B`.                                                (7.1)

The escape recursion is

`B=S/(lambda+S)`,                                                (7.2)

where `S=sum_{j=1}^nu B_j`. Differentiating and dividing by `B` gives the exact recursion

`q_B=[1+lambda (sum_j B_j q_j)/S]/(lambda+S)`.                  (7.3)

Because the offspring support is bounded above by 4, regular-tree comparison gives `B_j<=1-lambda/4`, hence `lambda+S<=4`. Starting from `q_j>=0`, (7.3) yields `q_B>=1/4`; iterating the same implication

`q_j>=m  =>  q_B>=(1+lambda m)/4`                               (7.4)

and passing to the fixed point proves

`BOX: q_B>=1/(4-lambda)`.                                       (7.5)

The degree-three minimum also gives the standard upper cone

`q_B<=1/(3-lambda)`.                                            (7.6)

### Degree-three upper score

For `k=3`, (7.6) implies

`[S_3+(lambda-1)sum_i U_i]/S_3 <= 2/(3-lambda)`.                (7.7)

Also `B_i>=1-lambda/3`, so

`D_3>=lambda-1+4(1-lambda/3)=(9-lambda)/3`.                    (7.8)

Therefore

`h_3/c_3 <= 6/[(3-lambda)(9-lambda)]`.                          (7.9)

### Degree-four lower score

For `k=4`, (7.5) implies

`[S_4+(lambda-1)sum_i U_i]/S_4 >= 3/(4-lambda)`.                (7.10)

Also `B_i<=1-lambda/4`, so

`D_4<=lambda-1+5(1-lambda/4)=(16-lambda)/4`.                   (7.11)

Hence

`h_4/c_4 >= 12/[(4-lambda)(16-lambda)]`.                        (7.12)

Combining (7.9) and (7.12),

`Delta<=a_sharp(lambda)`,                                       (7.13)

where

`a_sharp(lambda)`
` =6/[(3-lambda)(9-lambda)]`
`  -12/[(4-lambda)(16-lambda)]`.                               (7.14)

Put

`A_sharp(lambda)=lambda a_sharp(lambda)`.                        (7.15)

Then from (5.9),

`G>=F_lambda(theta)`                                             (7.16)

with

`F_lambda(theta)=3+theta-A_sharp(lambda)theta(1-theta)`.        (7.17)

### Monotonicity of the sharp budget

Write `A_sharp=g_1-g_2`, where

`g_1=6lambda/[(3-lambda)(9-lambda)]`,
`g_2=12lambda/[(4-lambda)(16-lambda)]`.                         (7.18)

Their derivative ratio is

`g_1'/g_2'`
`=[(27-lambda^2)/(2(64-lambda^2))]`
` *[(4-lambda)/(3-lambda)]^2`
` *[(16-lambda)/(9-lambda)]^2`.                                (7.19)

For `1<=lambda<3`, the three factors are bounded below by `9/55`, `(3/2)^2`, and `(15/8)^2`, so

`g_1'/g_2' >= 3645/2816 >1`.                                   (7.20)

Therefore

`BOX: A_sharp'(lambda)>0 on [1,3)`.                             (7.21)

This monotonicity lets every theorem below be certified at its right endpoint.

## 8. Theorem A proof: all `p<=1/3` or `p>=2/3` through `lambda=2.84`

Set

`L=71/25`.                                                       (8.1)

Exact arithmetic gives

`q(L)=13989/625>0`,                                              (8.2)

`A:=A_sharp(L)=6320775/419804`,                                 (8.3)

and the quadratic vertex of `F_L` is

`theta_*=(A-1)/(2A)=5900971/12641550`.                          (8.4)

### Lower mixture side: `p<=1/3`

By (6.7), (6.12),

`t<=U(L)=77/79`.                                                 (8.5)

Since `theta=pt/(1-p+pt)` is increasing in both `p` and `t`,

`theta<=Theta_-:=theta(1/3,77/79)=77/235`.                     (8.6)

The checker verifies `Theta_-<theta_*`, so `F_L` is decreasing on `[0,Theta_-]`. By (7.21), for every `lambda<=L`,

`G>=F_lambda(theta)>=F_L(theta)>=F_L(Theta_-)`
` =323159/30108670>0`.                                          (8.7)

Since `M<=4`, (5.10) gives the uniform derivative margin (4.3).

### Upper mixture side: `p>=2/3`

The static branch-addition bound (6.5) gives `t>=4/5`; hence

`theta>=Theta_+:=theta(2/3,4/5)=8/13`.                         (8.8)

The checker verifies `Theta_+>theta_*`, so `F_L` is increasing on `[Theta_+,1]`. Thus

`G>=F_L(Theta_+)`
` =917311/17736719>0`,                                          (8.9)

and (5.10) yields the uniform derivative margin (4.4).

This proves Theorem A on `[1,L]`; the published low-bias theorem patches the interval below 1.

## 9. Theorem B proof: sharper endpoint tails

The same argument can be pushed farther when the mixture is more endpoint-dominant.

### `p<=1/4`

Take

`L=1429/500=2.858`.                                             (9.1)

Then

`q(L)=4863189/250000>0`,                                        (9.2)

`U(L)=3071/3142`,                                                (9.3)

so

`theta<=3071/12497`.                                            (9.4)

At this endpoint,

`A_sharp(L)=14215516233000/818098771681`,                       (9.5)

and the exact quadratic check gives

`G>=1041007206377054/41604227622979199>0`.                      (9.6)

This yields (4.6).

### `p>=3/4`

Take

`L=2861/1000=2.861`.                                            (9.7)

The static ratio `t>=4/5` gives

`theta>=12/17`.                                                  (9.8)

At this endpoint,

`A_sharp(L)=32514069102000/1824317525863`,                      (9.9)

and the exact quadratic check gives

`G>=2999924079273/527227764974407>0`,                           (9.10)

which yields (4.8).

Again, no simulated speed sign enters any implication.

## 10. Exact checker and executed output

Exact rational checker:

`proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T08-25-43Z__sharp-elasticity-branch-window-check.py`.

Archived executed stdout:

`proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T08-25-43Z__sharp-elasticity-branch-window-check.out`.

The checker verifies the endpoint polynomials, `A_sharp` monotonicity ratio, quadratic-vertex placements, exact positive `G` values, derivative margins, and strict improvements over all four immediate-predecessor endpoints. Its final line is

`ALL_EXACT_CHECKS_PASS`.

This is a self-check, not an independent audit.

## 11. Demonstrated mechanism gain versus parent-problem status

The **source-level gain** is the four enlarged `{3,4}` bias/mixture regions in Section 4. The parent conjecture remains OPEN.

The **mechanism-level gain** is distinct: the branch-addition coordinate `theta` is now paired with a *regeneration/escape-recursion lower elasticity cone on the high-degree branch*. The predecessor treated the degree-four lower score too weakly, effectively paying only `4/(16-lambda)`. The new fixed-point cone strengthens this to

`12/[(4-lambda)(16-lambda)]`,                                   (11.1)

which reduces the environment-change budget before optimizing over the localized mixture coordinate. The improvement is therefore not a numerical recheck of the same inequality; it removes a real analytic loss.

The mechanism still has a structural pole at `lambda=3` through the degree-three upper cone `1/(3-lambda)`. Hence it cannot cross the minimum-degree boundary by further endpoint arithmetic alone.

## 12. Residual obstruction and next attack

The remaining hard barrier is `lambda=3`. The current proof takes a pathwise supremum of the degree-three escape elasticity and therefore diverges like `1/(3-lambda)` even when degree-three vertices are rare under the relevant regeneration law.

The next materially different route is an **occupation-weighted regeneration derivative**: replace the pointwise degree-three supremum by the expected number (or weighted local time) of degree-three encounters in a regeneration block, and prove that this occupation factor compensates the singularity when `p` is close to 1. A successful bound must control the derivative of the block displacement/time ratio, not merely the one-step drift. No cross-3 theorem is claimed in this report.

```yaml
ledger_delta:
  track: NM13-05
  parent: T06
  source_id: P0066
  status_before: OPEN
  status_after: OPEN
  offspring_assumptions: "P(nu=3)=1-p, P(nu=4)=p, no leaves"
  bias_convention: "parent bias lambda; child bias beta=1/lambda"
  predecessor_report: "proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T07-25-00Z__quantitative-branch-addition-window.md"
  parent_scope_before: "global LPP monotonicity open"
  parent_scope_after: "global LPP monotonicity open"
  restricted_before:
    p_le_1_3: "lambda <= 1131/400"
    p_ge_2_3: "lambda <= 283/100"
    p_le_1_4: "lambda <= 356/125"
    p_ge_3_4: "lambda <= 713/250"
  restricted_after:
    p_le_1_3_or_p_ge_2_3: "lambda <= 71/25"
    p_le_1_4: "lambda <= 1429/500"
    p_ge_3_4: "lambda <= 2861/1000"
  mechanism_gain: "combine quantitative five-branch localization with fixed-point lower logarithmic escape elasticity q>=1/(4-lambda), yielding Delta <= 6/((3-lambda)(9-lambda))-12/((4-lambda)(16-lambda))"
  exact_checker: "proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T08-25-43Z__sharp-elasticity-branch-window-check.py"
  exact_output: "proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T08-25-43Z__sharp-elasticity-branch-window-check.out"
  exact_output_tail: "ALL_EXACT_CHECKS_PASS"
  simulated_signs_used: false
  external_novelty: UNVERIFIED
  review_status: "restricted theorem candidates pending later independent review"
  residual_obstruction: "pointwise degree-three elasticity pole at lambda=3"
  next_attack: "occupation-weighted regeneration derivative across the minimum-degree boundary"
```

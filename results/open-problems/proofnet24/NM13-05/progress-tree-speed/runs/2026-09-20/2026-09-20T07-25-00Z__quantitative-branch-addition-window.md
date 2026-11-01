Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6/maximum was requested, but no authenticated applied reasoning-effort metadata is exposed, so GPT-6/maximum is not claimed. SUBSTANTIVE MOVEMENT: the Lyons--Pemantle--Peres parent problem remains OPEN, but for the exact no-leaf family `P(nu=3)=1-p, P(nu=4)=p` a new two-sided quantitative branch-addition window proves strict parent-bias decrease through `lambda=1131/400=2.8275` for every `p<=1/3` and through `lambda=283/100=2.83` for every `p>=2/3`. It also pushes the predecessor headline tails to `lambda=356/125=2.848` for `p<=1/4` and `lambda=713/250=2.852` for `p>=3/4`. Each endpoint lies beyond the previous static-ratio criterion for the corresponding boundary mixture. No simulated speed sign is used.**

# NM13-05 T06 — quantitative five-branch addition for `{3,4}` offspring

Date: 2026-09-20.  
Repository: private `yspennstate/math-open-problems`, branch `master`.  
Own root: `proofnet24/NM13-05/progress-tree-speed`.  
Parent target: T06 / historical intake P0066, Lyons--Pemantle--Peres monotonicity of biased-walk speed on a supercritical Galton--Watson tree without leaves.  
Status: **PARTIAL / OPEN parent; NEW RESTRICTED THEOREM CANDIDATES pending later independent review.**

## 1. Compact continuity handoff and route separation

The controlling instruction is `operations/PROGRESS20_2026-09-20.md`. LIVE20 assigns NM13-05 to T06 by escape-probability/regeneration coupling, complementary to P01's analytic regeneration-derivative route.

Historical P0066 remains attempted-unsolved. The old intake route observed that at a vertex with a fixed number `k` of children the local radial drift

`(k-lambda)/(k+lambda)`

decreases with the parent bias `lambda`. That does **not** control the `lambda`-dependent law of the environment seen from the walker, so the measure-change term remained unsigned. This failure is preserved and not relabelled as progress.

Immediate own predecessor:

`proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T06-22-00Z__mixture-localized-adjacent-wedge.md`.

That report proved the exact `{3,4}` reduction and the static branch-addition localization

`4/5 <= t:=c_4/c_3 <= 1`,

then retained the resulting interval for the escape-tilted mixture coordinate before optimizing the derivative numerator. Its strongest **criterion** was stronger than its rounded headline rectangles; for example, at `p=1/3` the old criterion fails between `lambda=2.826` and `2.827`, and at `p=2/3` it fails between `2.829` and `2.830`. Those are the honest comparison baselines below.

Latest live P01 consumed:

`proofnet24/P01-progress-speed/runs/2026-09-20/2026-09-20T06-57-50Z__run-report.md`.

P01 treats minimum offspring one, including support-free laws, by a lambda-dependent Aidekon-tilt compression below the pipe threshold. The present report keeps minimum degree three and sharpens a **branch-addition coupling**. There is no duplication of P01's principal offspring class or analytic compression route.

Latest relevant non-LIVE20 T06 work consumed:

`runs/prob10_2026-09-20/PROB10-06/20260920T0716Z_moderate_mixture_rectangle_5d8b2e41.md` and its predecessor quantitative branch-ratio report. That stream treats `{2,3}`. It showed that a quantitative branch-ratio estimate can beat the static `3/4<=c_3/c_2<=1` box. The present run ports the idea to the next genuinely random adjacent family but must prove a different five-branch derivative inequality; the new polynomial is `29 lambda^2-328 lambda+720`, and the resulting `{3,4}` source regions below are not present in that stream.

`POSTED.md` was checked. It records no posted source-wide P0066 closure; restricted T06 results remain restricted and do not close the parent problem.

## 2. Frozen source assumptions and bias convention

Throughout,

`P(nu=3)=1-p,   P(nu=4)=p,   0<=p<=1`.                         (2.1)

There are no leaves and `E nu=3+p`.

Use the **parent-bias** convention

`P(parent | nu=k)=lambda/(lambda+k)`,
`P(each fixed child | nu=k)=1/(lambda+k)`.                      (2.2)

Larger `lambda` pushes toward the root. Write the speed as `ell_lambda`; the target derivative sign is

`ell'_lambda<0`.                                                 (2.3)

The child-bias convention in Ben Arous--Fribergh--Sidoravicius is reciprocal:

`beta=1/lambda`.                                                 (2.4)

Thus, wherever differentiable,

`v'(beta)=-ell'_{1/beta}/beta^2`.                               (2.5)

Every strict parent-bias derivative theorem below therefore gives a strict positive child-bias derivative on the reciprocal interval.

## 3. Primary-source and current-literature boundary refreshed this run

Bounded checks on 2026-09-20 recovered:

1. Ben Arous--Fribergh--Sidoravicius, arXiv:1111.5865, submitted 24 November 2011, *A proof of the Lyons-Pemantle-Peres monotonicity conjecture for high biases*. In its child-bias convention the abstract states that `v(beta)` is increasing for `beta>=717` on Galton--Watson trees without leaves.
2. He--Wang--Xiang, arXiv:1610.08151, submitted 26 October 2016 and published online by Cambridge University Press on 5 March 2025 as *The speed of a biased walk on a Galton--Watson tree without leaves is monotonic for low values of bias*, Journal of Applied Probability 62 (2025), 1044--1052. For minimum offspring `m1>=2`, they prove strict parent-bias decrease on

   `0<=lambda<=m1/(1+sqrt(1-1/m1))`.                            (3.1)

3. Aidekon's exact speed representation remains the analytic identity consumed below.
4. The fresh 2026 Song--Liu paper concerns deterministic regular trees, not genuinely random offspring laws.

The fresh search did not surface a checked source-wide resolution or a checked theorem identical to the quantitative `{3,4}` regions below. That is bounded negative evidence only, **not** a novelty certificate.

## 4. Parent-problem before/after and source-level movement

### Parent problem

Before: **OPEN**.  
After: **OPEN**.

No theorem for every no-leaf offspring law throughout `0<=lambda<E nu` is claimed.

### Restricted `{3,4}` scope before

The predecessor's exact static-ratio criterion was

`A_3(lambda)<K_p`,                                               (4.1)

obtained from `4/5<=c_4/c_3<=1`. At the two moderate boundary mixtures relevant here this specializes to:

- `p=1/3`: old threshold `A_3(lambda)<15`; exact arithmetic gives

  `15-A_3(2.826)>0`,
  `15-A_3(2.827)<0`.                                            (4.2)

  Hence that criterion's frontier lies strictly in `(2.826,2.827)`.

- `p=2/3`: old threshold `A_3(lambda)<611/40`; exact arithmetic gives

  `611/40-A_3(2.829)>0`,
  `611/40-A_3(2.830)<0`.                                        (4.3)

  Hence that criterion's frontier lies strictly in `(2.829,2.830)`.

For the predecessor's headline tails, the same exact static criterion has frontiers in `(2.847,2.848)` at `p=1/4` and `(2.851,2.852)` at `p=3/4`; the rounded headline theorem had stopped at `2.845` and `2.85` respectively.

### Restricted `{3,4}` scope after

**Theorem A.** If `0<=p<=1/3`, then `ell_lambda` is strictly decreasing on

`0<=lambda<=1131/400=2.8275`.                                   (4.4)

On `1<=lambda<=1131/400`,

`-ell'_lambda >= 83569539481600/185836461517301243 >0`.          (4.5)

Equivalently, `v'(beta)>0` for finite `beta>=400/1131`.

**Theorem B.** If `2/3<=p<=1`, then `ell_lambda` is strictly decreasing on

`0<=lambda<=283/100=2.83`.                                      (4.6)

On the genuinely new upper strip `2829/1000<=lambda<=283/100`,

`-ell'_lambda >=`
`15297146502090340000/19240529040046546526431 >0`.               (4.7)

Equivalently, `v'(beta)>0` down to `beta=100/283`.

Two clean tail corollaries sharpen the predecessor headline rectangles beyond their **exact old static frontiers**:

- if `p<=1/4`, strict decrease holds through

  `lambda<=356/125=2.848`,                                      (4.8)

  with

  `-ell'_lambda >=1070511796875/926449474425107`                (4.9)

  on `1<=lambda<=2.848`;

- if `p>=3/4`, strict decrease holds through

  `lambda<=713/250=2.852`,                                      (4.10)

  with

  `-ell'_lambda >=`
  `1074601074120087460375000/944450848327440824926715409`       (4.11)

  on the new upper strip beginning at `lambda=2.851`.

These are derivative-sign theorems from exact inequalities; no simulated sign is used.

## 5. Consumed exact derivative reduction

Work on `1<lambda<3`. Let `B` be the quenched probability, starting at a vertex, of escaping to infinity before hitting its parent, and put

`U=-dB/dlambda>=0`.

For current offspring value `k`, take iid copies `B_0,...,B_k`, with corresponding `U_i`, and define

`S_k=sum_i B_i`,
`D_k=lambda-1+S_k`,

`c_k=E[(1/(k+1))*S_k/D_k]`,                                     (5.1)

`h_k=E[(1/(k+1))*sum_i(B_i+(lambda-1)U_i)/D_k^2]`.              (5.2)

On compact strips below 3, the inherited dominated-differentiation argument gives

`c'_k=-h_k`.                                                     (5.3)

Set

`C=(1-p)c_3+p c_4`,
`theta=p c_4/C`,
`M=3+theta`.                                                     (5.4)

Aidekon's symmetrized formula reduces exactly to

`ell_lambda=(M-lambda)/(M+lambda)`,                              (5.5)

so

`ell'_lambda=2(lambda M'-M)/(M+lambda)^2`.                       (5.6)

Writing

`Delta=h_3/c_3-h_4/c_4`,                                        (5.7)

we have

`theta'=theta(1-theta)Delta`.                                   (5.8)

Therefore

`G:=M-lambda M'`
` =3+theta-lambda theta(1-theta)Delta`,                          (5.9)

and

`-ell'_lambda=2G/(M+lambda)^2`.                                 (5.10)

The inherited escape-sensitivity estimate is

`Delta<=a_3(lambda)`,                                           (5.11)

where

`a_3(lambda)=6/[(3-lambda)(9-lambda)]-4/(16-lambda)`.           (5.12)

Put

`A_3(lambda)=lambda a_3(lambda)`.                               (5.13)

Then

`G>=F_lambda(theta):=3+theta-A_3(lambda)theta(1-theta)`.        (5.14)

The predecessor also proved `A_3` strictly increasing on `[1,3)`. For completeness,

`d/dlambda [6lambda/((3-lambda)(9-lambda))]`
` =6(27-lambda^2)/[(3-lambda)^2(9-lambda)^2] >=27/64`,          (5.15)

whereas

`d/dlambda [4lambda/(16-lambda)]`
` =64/(16-lambda)^2 <=64/169`,                                  (5.16)

so

`A'_3(lambda)>=467/10816>0`.                                    (5.17)

The present run changes **only** the allowed location of `theta`, by proving a strictly smaller branch-ratio box than `4/5<=c_4/c_3<=1`.

## 6. New lemma: quantitative two-sided branch-addition window

Let

`a=lambda-1>0`,
`phi(s)=s/(a+s)`.                                                (6.1)

For the `{3,4}` offspring family and `1<lambda<3`, the inherited regular-tree comparison gives the pathwise escape window

`b:=(3-lambda)/3 <= B <= u:=(4-lambda)/4`.                     (6.2)

For iid copies `X_i` of `B`, put

`F_n=E phi(X_1+...+X_n)`.                                       (6.3)

Then

`c_3=F_4/4`, `c_4=F_5/5`,                                      (6.4)

and hence

`t:=c_4/c_3=(4/5) F_5/F_4`.                                    (6.5)

### Lemma 6.1 — quantitative upper ratio

If

`29 lambda^2-328 lambda+720>0`,                                 (6.6)

then

`BOX: t <= U(lambda):=(9-lambda)/(2(6-lambda)) <1`.            (6.7)

In particular (6.7) holds throughout every new interval in this report, since the smaller root of (6.6) is

`(164-8 sqrt(94))/29 = 2.9805904...`.                            (6.8)

#### Proof

Take deterministic `x_1,...,x_5 in [b,u]`, put `S=sum_i x_i`, and define

`A(x):=[(1/5) sum_i phi(S-x_i)]/phi(S)`.                         (6.9)

By symmetry,

`F_4=E[A(X_1,...,X_5) phi(S)]`.                                 (6.10)

We prove that `A` is coordinatewise increasing on the box. Fix `j` and set `y_i=S-x_i`. Differentiating (6.9), after multiplying by positive factors, shows that the sign of `partial_j A` is the sign of

`H_j=S(a+S) sum_{i!=j} 1/(a+y_i)^2`
`    -sum_i y_i/(a+y_i)`.                                       (6.11)

For each `i!=j`,

`S(a+S)/(a+y_i)^2-y_i/(a+y_i)`
` =x_i(a+S+y_i)/(a+y_i)^2`.                                    (6.12)

Thus it is enough to prove

`(a+S+y_i)/(a+y_i)^2 >=1/(a+y_j)`                              (6.13)

for every `i!=j`: summing (6.12) under (6.13) gives

`H_j >= [sum_{i!=j}x_i-y_j]/(a+y_j)=0`.                         (6.14)

Write `x=x_i`, `y=x_j`, and let `z` be the sum of the remaining three coordinates. The numerator after cross-multiplying (6.13) is exactly

`D=2ax+az+x^2+2xy+3xz-y^2+z^2`.                                (6.15)

Using `x,y>=b`, `y<=u`, and `z>=3b`,

`D >=5ab+21b^2-u^2`
`  =(29 lambda^2-328 lambda+720)/48`.                           (6.16)

Under (6.6), `D>0`, so every coordinate derivative is nonnegative. Therefore the minimum of `A` occurs at `x_1=...=x_5=b`, where

`A_min=phi(4b)/phi(5b)`.                                       (6.17)

Equations (6.5), (6.10), and (6.17) give

`t <=(4/5) phi(5b)/phi(4b)`
`   =(a+4b)/(a+5b)`
`   =(9-lambda)/(2(6-lambda))`.                                 (6.18)

This proves Lemma 6.1. `U(lambda)` is strictly increasing because its derivative is `3/(2(6-lambda)^2)>0`.

### Lemma 6.2 — quantitative lower ratio

For every `1<lambda<3`,

`BOX: t >= L(lambda)`                                           (6.19)

with

`L(lambda)=12(15-4lambda)/[5(12-lambda)(4-lambda)] >4/5`.      (6.20)

#### Proof

Write `S=X_1+...+X_4` and `x=X_5`. Pointwise,

`phi(S+x)/phi(S)`
` =1+a x/[S(a+S+x)]`.                                           (6.21)

The correction is increasing in `x` and decreasing in `S`. Since `x>=b` and `S<=4u`,

`phi(S+x)/phi(S)`
` >=1+ab/[4u(a+4u+b)]`.                                         (6.22)

Taking expectations,

`F_5/F_4 >=1+ab/[4u(a+4u+b)]`.                                  (6.23)

Multiply by `4/5` and simplify using (6.2) to obtain (6.20).

For later stitching,

`L'(lambda)` has the sign of

`q(lambda):=2lambda^2-15lambda+24`.                             (6.24)

The exact checker records `q(14/5)=-58/25<0` and `q(2.83)=-12161/5000<0`; since `q'(lambda)=4lambda-15<0` on this interval, `L` is decreasing on `[14/5,2.83]`.

### Demonstrated mechanism gain

The static predecessor box

`4/5<=t<=1`                                                     (6.25)

is replaced, throughout the new range, by

`BOX: L(lambda)<=t<=U(lambda)`.                                 (6.26)

Both inequalities are strict improvements away from the endpoints. This is the run's mechanism-level result: **the fifth escape branch not only localizes the tilted mixture qualitatively, it quantitatively squeezes the environment-change coordinate on both sides.**

## 7. Translate the new branch-ratio window into `theta`

From (5.4),

`theta = p t/(1-p+p t)`.                                        (7.1)

This is increasing in both `p` and `t`.

### Low-moderate side `p<=1/3`

For `lambda<=L_-:=1131/400`, Lemma 6.1 and monotonicity of `U` give

`t<=U(L_-)=823/846`.                                            (7.2)

Hence

`theta<=Theta_-:=`
`[(1/3)(823/846)]/[2/3+(1/3)(823/846)]`
`=823/2515`.                                                     (7.3)

At `L_-`,

`A_3(L_-)=1503495604/99736901`.                                 (7.4)

For the quadratic

`f_-(theta)=3+theta-A_3(L_-)theta(1-theta)`,                    (7.5)

its vertex is

`theta_v=(A_3(L_-)-1)/(2A_3(L_-))`
`=1403758703/3006991208`.                                       (7.6)

The exact inequality `Theta_-<theta_v` holds, so `f_-` is decreasing on `[0,Theta_-]`. Therefore, using `A_3(lambda)<=A_3(L_-)`,

`G>=f_-(theta)>=f_-(Theta_-)`
` =6528870272/766535042075>0`.                                  (7.7)

Also

`M+lambda<=3+Theta_-+L_-`,                                      (7.8)

which yields exactly

`-ell'_lambda>=`
`83569539481600/185836461517301243>0`                           (7.9)

for `1<=lambda<=L_-`.

The He--Wang--Xiang theorem covers `[0,1]` (indeed substantially farther) for minimum offspring three, so Theorem A follows on the whole interval `[0,L_-]`.

Crucially, this endpoint is genuinely beyond the old static-ratio criterion at the boundary mixture: the checker gives

`15-A_3(L_-)=-7442089/99736901<0`.                              (7.10)

So replacing `t<=1` by Lemma 6.1 is essential here.

### High-moderate side `p>=2/3`

First, the old static lower ratio `t>=4/5` gives

`theta>=8/13`                                                   (7.11)

at `p=2/3`, and the right side only increases with `p`. Since the minimizer of `(3+theta)/(theta(1-theta))` is `2sqrt(3)-3<8/13`, the old criterion is valid whenever

`A_3(lambda)<K(8/13)=611/40`.                                  (7.12)

The checker gives

`611/40-A_3(2829/1000)`
`=3010447129/61771463160>0`,                                    (7.13)

so the interval through `lambda=2.829` is already covered.

Now take the upper strip

`2829/1000<=lambda<=L_+:=283/100`.                              (7.14)

Lemma 6.2 and the monotonicity from (6.24) give

`t>=L(L_+)=29440/35763`.                                        (7.15)

Therefore for every `p>=2/3`,

`theta>=Theta_+:=`
`[2(29440/35763)]/[1+2(29440/35763)]`
`=58880/94643`.                                                  (7.16)

At `L_+`,

`A_3(L_+)=211753052/13814013`,                                  (7.17)

and the quadratic vertex is

`theta_v=197939039/423506104<Theta_+`.                          (7.18)

Hence

`f_+(theta)=3+theta-A_3(L_+)theta(1-theta)`                     (7.19)

is increasing throughout the admissible high-theta region, and

`G>=f_+(Theta_+)`
` =764857325104517/41245407801784279>0`.                        (7.20)

Since `M+lambda<=4+L_+`, on the new upper strip

`-ell'_lambda>=`
`15297146502090340000/19240529040046546526431>0`.               (7.21)

This proves Theorem B after stitching (7.13) and (7.21), together with the published lower-bias interval below 1.

Again the new quantitative lower ratio is genuinely used at the endpoint:

`611/40-A_3(2.83)`
`=-29760137/552560520<0`,                                       (7.22)

so the old static box does not certify `2.83` at `p=2/3`.

## 8. Two sharper tail corollaries

The same calculation gives clean endpoint gains on the predecessor's headline tails.

### `p<=1/4`

At

`L=356/125=2.848`,

Lemma 6.1 gives

`t<=769/788`,
`theta<=769/3133`.                                               (8.1)

The old static threshold already fails there:

`52/3-A_3(L)=-446720/6005121<0`.                               (8.2)

But the quantitative bound yields

`G>=548102040/25550238467>0`,                                   (8.3)

and hence

`-ell'_lambda>=1070511796875/926449474425107>0`.                (8.4)

The old static frontier is bracketed by `2.847` and `2.848`, so the inclusion of the exact endpoint `2.848` is a strict certificate gain, not rounding.

### `p>=3/4`

At

`L=713/250=2.852`,

Lemma 6.2 gives

`t>=538800/656369`,
`theta>=1616400/2272769`.                                       (8.5)

The old static lower-ratio threshold at `theta=12/17` fails:

`K(12/17)-A_3(L)`
`=-331682369/3738568060<0`.                                     (8.6)

The quantitative lower ratio instead yields

`G>=25790425778882099049/965574726621744734483>0`,              (8.7)

and on the new upper strip beginning at `2.851`,

`-ell'_lambda>=`
`1074601074120087460375000/944450848327440824926715409>0`.      (8.8)

The old static frontier is bracketed by `2.851` and `2.852`; thus (8.8) again crosses the exact old certificate frontier.

## 9. Exact arithmetic and what was / was not computational

Essential checker:

`proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T07-25-00Z__quantitative-branch-addition-check.py`.

Archived executed stdout:

`proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T07-25-00Z__quantitative-branch-addition-check.out`.

The checker uses only exact Python `Fraction` arithmetic for all displayed endpoint identities, old-frontier sign changes, quadratic-vertex comparisons and derivative margins. It ends

`ALL_EXACT_CHECKS_PASS`.

The theorem is **not** inferred from a finite parameter grid: Sections 6--8 give the symbolic monotonicity and coupling arguments. The checker validates only the rational finite core.

## 10. Residual obstruction and next materially different attack

This run sharpens the below-minimum-degree branch-addition route but does **not** cross `lambda=3`. The inherited sensitivity budget `A_3(lambda)` still diverges like `1/(3-lambda)` because it uses a pointwise minimum-degree escape elasticity. Quantitatively squeezing `c_4/c_3` cannot remove that singularity; it only postpones where it dominates.

The already recovered inverse-escape lemma from the `{2,3}` stream,

`E[1/B] <= 1/(1-lambda E[1/nu])`,                               (10.1)

shows why a genuinely different attack remains plausible: for `{3,4}` laws with enough degree-four mass, the right side stays finite beyond `lambda=3`. What is still missing is a derivative/regeneration score estimate that averages the bad degree-three excursions instead of taking a pathwise supremum. The next NM13-05 attack should therefore be the occupation-weighted regeneration/inverse-escape route, not another algebraic refinement of (5.11).

No claim beyond `lambda=3` is made here.

## 11. ledger_delta

```yaml
ledger_delta:
  track: NM13-05
  parent: T06
  source_id: P0066
  status_before: OPEN
  status_after: OPEN
  offspring_family: "P(nu=3)=1-p, P(nu=4)=p"
  bias_convention:
    parent_bias: lambda
    child_bias: beta=1/lambda
  source_scope_before:
    p_eq_1_3_static_frontier: "lambda in (2.826,2.827)"
    p_eq_2_3_static_frontier: "lambda in (2.829,2.830)"
    p_le_1_4_headline_endpoint: "2.845; exact static frontier in (2.847,2.848)"
    p_ge_3_4_headline_endpoint: "2.85; exact static frontier in (2.851,2.852)"
  source_scope_after:
    p_le_1_3_endpoint: 1131/400
    p_ge_2_3_endpoint: 283/100
    p_le_1_4_endpoint: 356/125
    p_ge_3_4_endpoint: 713/250
  mechanism_gain:
    old_ratio_box: "4/5 <= c4/c3 <= 1"
    new_upper: "c4/c3 <= (9-lambda)/(2(6-lambda)) when 29 lambda^2-328 lambda+720>0"
    new_lower: "c4/c3 >= 12(15-4lambda)/(5(12-lambda)(4-lambda))"
  exact_margins:
    p_le_1_3: 83569539481600/185836461517301243
    p_ge_2_3_new_strip: 15297146502090340000/19240529040046546526431
    p_le_1_4: 1070511796875/926449474425107
    p_ge_3_4_new_strip: 1074601074120087460375000/944450848327440824926715409
  parent_problem_moved: false
  restricted_source_scope_moved: true
  simulated_sign_used: false
  checker: proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T07-25-00Z__quantitative-branch-addition-check.py
  checker_output: proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T07-25-00Z__quantitative-branch-addition-check.out
  review_status: CANDIDATE_RESTRICTED_PENDING_INDEPENDENT_REVIEW
  residual_obstruction: "pointwise minimum-degree escape elasticity diverges at lambda=3"
  next_attack: "occupation-weighted regeneration / inverse-escape derivative score across lambda=3"
```

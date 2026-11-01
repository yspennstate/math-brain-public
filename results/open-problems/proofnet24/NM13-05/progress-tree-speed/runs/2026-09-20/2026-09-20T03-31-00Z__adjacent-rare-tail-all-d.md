Actual runtime model: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6/maximum was requested, but no authenticated applied-model/reasoning telemetry is exposed, so GPT-6/maximum is not claimed. SUBSTANTIVE MOVEMENT: the Lyons--Pemantle--Peres parent problem remains OPEN, but the NM13-05 escape-coupling theorem is lifted from one fixed `{3,4}` law to every adjacent no-leaf law `{d,d+1}`, `d>=2`. For `P(nu=d)=1-p, P(nu=d+1)=p`, strict parent-bias decrease is proved on `0<=lambda<=d-1/100` whenever `p<=1/100` or `p>=99/100`. In particular the previous `{3,4}` theorem at `lambda<=2.99` widens both endpoint tails from `1/200` to `1/100`. No simulated sign is used.**

# NM13-05 T06 — all-degree adjacent rare-tail coupling to within 0.01 of the minimum-degree boundary

Date: 2026-09-20.  
Repository: `yspennstate/math-open-problems`, branch `master`.  
Own root: `proofnet24/NM13-05/progress-tree-speed`.  
Parent target: T06 / P0066, Lyons--Pemantle--Peres monotonicity of biased-walk speed on a supercritical Galton--Watson tree without leaves.  
Status: **PARTIAL / OPEN parent; NEW RESTRICTED THEOREM CANDIDATE pending later independent review.**

## 1. Compact continuity handoff

The controlling owner instruction is `operations/PROGRESS20_2026-09-20.md`. LIVE20 assigns NM13-05 to T06 by escape-probability/regeneration coupling, complementary to P01's analytic regeneration derivative route.

The historical P0066 attempt is preserved: for a fixed offspring count `k`, the local radial drift `(k-lambda)/(k+lambda)` decreases in parent bias `lambda`, but this does not control the `lambda`-dependent environment seen from the walker. The missing ingredient was a measure-change / regeneration comparison.

The immediate predecessor is

`proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T02-34-00Z__rare-extra-child-nearcritical-d3.md`.

It froze

`P(nu=3)=1-p, P(nu=4)=p`

and proved strict decrease through `lambda=2.99` for `p<=1/200` or `p>=199/200`, using a branch-addition escape coupling `4/5<=c_4/c_3<=1`. It also recorded the still-unresolved materially different route needed to cross the minimum-degree singularity `lambda=3`: an occupation-weighted regeneration sensitivity estimate that charges bad degree-3 derivative only when a regeneration block actually encounters degree 3. That cross-3 route remains unresolved; this run does not claim it.

The latest relevant complementary P01 report consumed is

`proofnet24/P01-progress-speed/runs/2026-09-20/2026-09-20T03-08-51Z__run-report.md`,

which proves distribution-free bounded-support regions by a conditional-degree secant/covariance method, for example every `3<=nu<=12` through `lambda=1.9`. That is broader in support but far from the minimum-degree boundary; the present result is a different rare-adjacent mechanism.

The latest relevant PROB10-06 dependency consumed is

`runs/prob10_2026-09-20/PROB10-06/20260920T0132Z_escape_elasticity_cone_bridge_7d4a2c91.md`,

which proves the bounded-support logarithmic escape cone and records the exact adjacent-family reduction used below. Its sharper lower elasticity term is not needed for the theorem here; the new gain comes instead from keeping the endpoint mixture geometry after branch addition rather than collapsing it to a global worst-case tilted weight.

`POSTED.md` was checked through the current repository state. No posted source-wide solution of P0066 is recorded; restricted T06 theorems do not close the parent problem.

## 2. Frozen source assumptions and bias convention

Fix an integer `d>=2` and the exact no-leaf adjacent offspring law

`P(nu=d)=1-p,   P(nu=d+1)=p,   0<=p<=1`.                       (2.1)

The mean is `m=d+p>d-1`, and because `d>=2` the Galton--Watson tree is supercritical with no leaves.

Use the **parent-bias** convention

`P(parent | nu=k)=lambda/(lambda+k)`,
`P(each fixed child | nu=k)=1/(lambda+k)`.                       (2.2)

Increasing `lambda` pushes toward the root, so the desired sign is

`ell'_lambda<0`.                                                  (2.3)

The Ben Arous--Fribergh--Sidoravicius **child-bias** convention is reciprocal:

`beta=1/lambda`.                                                   (2.4)

Thus if `v(beta)=ell_{1/beta}`, then wherever differentiable

`v'(beta)=-ell'_{1/beta}/beta^2`.                                (2.5)

Primary-source recovery:

- arXiv:1111.5865, Ben Arous--Fribergh--Sidoravicius, is the high-child-bias partial solution. The arXiv-version quantitative constant and the final 2014 publication's displayed high-bias constant differ; this report uses neither constant in the proof.
- arXiv:1610.08151, He--Wang--Xiang, proves strict decrease in parent bias on

  `0<=lambda<=theta_d:=d/(1+sqrt(1-1/d))`                       (2.6)

  when the minimum offspring is `d>=2`. The paper was published online 5 March 2025 in the Journal of Applied Probability.
- Aidekon's speed representation and Bowditch--Tokushige differentiability results are the standard analytic inputs behind the exact derivative formula below.

A bounded fresh literature search dated 2026-09-20 recovered the 2014 high-bias paper, the 2025 low-bias publication, and later differentiability work, but no checked source-wide resolution and no checked theorem matching the all-`d` rare-adjacent near-boundary region proved here. This is bounded negative evidence only, not a novelty certificate.

## 3. Parent-problem before/after versus restricted-family gain

### Parent problem

Before: **OPEN**.  
After: **OPEN**.

No full Lyons--Pemantle--Peres theorem is claimed.

### Restricted source-level scope before this run

The strongest NM13-05 near-minimum-degree theorem was only the fixed family `{3,4}`:

`p<=1/200 or p>=199/200  =>  ell'_lambda<0 on 0<=lambda<=2.99`. (3.1)

There was also earlier `{2,3}` rare-tail work, but no NM13-05 theorem uniform in the minimum degree `d`.

### Restricted source-level scope after this run

### Theorem A — uniform adjacent rare-tail strip for every minimum degree

For every integer `d>=2`, let (2.1) hold. If

`p<=1/100  or  p>=99/100`,                                       (3.2)

then the parent-bias speed is strictly decreasing throughout

`0<=lambda<=d-1/100`.                                             (3.3)

Equivalently, the child-bias speed is strictly increasing on the reciprocal interval

`beta>=1/(d-1/100)`                                               (3.4)

inside the corresponding transient region.

For `d=3`, Theorem A keeps the predecessor endpoint `2.99` but doubles each certified endpoint-mixture width from `1/200` to `1/100`.

For `d=2`, it gives a new clean narrow-tail theorem through `lambda=1.99`; this is closer to the minimum-degree boundary than the earlier fixed-tail `1.966` certificate, at the cost of narrowing the tails.

For every `d>=4`, it supplies a new entire family of source-valid restricted regions reaching to exactly `0.01` below the minimum offspring degree.

## 4. Exact adjacent-family speed derivative reduction

Work first on `1<=lambda<d`. Let `B` be the quenched probability of escaping to infinity before hitting the parent of the current vertex, and put `U=-dB/dlambda>=0`.

For conditional current offspring `k`, take iid copies `B_0,...,B_k` and corresponding `U_i`. Set

`S_k=sum_{i=0}^k B_i`,
`D_k=lambda-1+S_k`,

`c_k=E[(1/(k+1))*S_k/D_k]`,                                      (4.1)

`h_k=E[(1/(k+1))*sum_i(B_i+(lambda-1)U_i)/D_k^2]`.               (4.2)

Direct differentiation gives

`c_k'=-h_k`.                                                       (4.3)

Write

`C=(1-p)c_d+p c_{d+1}`,
`theta=p c_{d+1}/C`.                                               (4.4)

Then Aidekon's symmetrized speed formula reduces exactly to

`M=d+theta`,
`ell_lambda=(M-lambda)/(M+lambda)`.                               (4.5)

Hence

`ell'_lambda=2(lambda M'-M)/(M+lambda)^2`.                        (4.6)

Since

`theta/(1-theta)=(p/(1-p))*(c_{d+1}/c_d)`,

differentiating and using (4.3) gives

`theta'=theta(1-theta) Delta`,                                   (4.7)

where

`Delta=h_d/c_d-h_{d+1}/c_{d+1}`.                                 (4.8)

Thus it is enough to prove

`d+theta-lambda theta(1-theta)Delta>0`.                           (4.9)

## 5. General branch-addition coupling

This is the first mechanism gain of the run: the predecessor's `{3,4}` ratio lemma extends without loss to every adjacent pair.

For `lambda>1`, define

`phi(s)=s/(lambda-1+s)`.                                          (5.1)

It is increasing, concave and satisfies `phi(0)=0`. Let

`S_{d+1}=B_1+...+B_{d+1}`,
`S_{d+2}=S_{d+1}+B_{d+2}`.

Then

`c_d=(1/(d+1)) E phi(S_{d+1})`,
`c_{d+1}=(1/(d+2)) E phi(S_{d+2})`.                              (5.2)

Monotonicity of `phi` gives

`E phi(S_{d+2})>=E phi(S_{d+1})`,

hence

`c_{d+1}/c_d >= (d+1)/(d+2)`.                                   (5.3)

For the reverse direction, fix deterministic `x_1,...,x_{d+2}>=0` with total `S>0`. Concavity and `phi(0)=0` imply

`phi(S-x_i) >= (1-x_i/S) phi(S)`.                                (5.4)

Summing over all `d+2` indices gives

`sum_i phi(S-x_i) >= (d+1) phi(S)`.                              (5.5)

With iid `B_i`, every leave-one-out sum has the law of `S_{d+1}`. Taking expectations in (5.5),

`(d+2) E phi(S_{d+1}) >= (d+1) E phi(S_{d+2})`.                  (5.6)

Using (5.2),

`c_{d+1}/c_d <=1`.                                                (5.7)

Therefore

`BOX: (d+1)/(d+2) <= t:=c_{d+1}/c_d <=1`.                        (5.8)

At `lambda=1` the same statement follows by the direct limit; all branch sums are positive under `d>=2`.

From (4.4) and (5.8),

`theta = p t/(1-p+p t)`,                                         (5.9)

so

`p(d+1)/(d+2-p) <= theta <= p`.                                  (5.10)

Equivalently, with `r=1-p`,

`1-theta <= (d+2)r/(d+1+r)`.                                    (5.11)

The significance is that an endpoint mixture remains quantitatively near the same endpoint after the escape tilt.

## 6. Escape-sensitivity budget uniform up to `d-delta`

The bounded-support escape comparison and the He--Wang--Xiang / PROB10-06 logarithmic derivative envelope give, for support `{d,d+1}` and `lambda<d`,

`B >= 1-lambda/d`,
`0<=U<=B/(d-lambda)`.                                            (6.1)

For the `k=d` branch, the ratio of the integrand in `h_d` to that in `c_d` is

`[S_d+(lambda-1)sum_i U_i]/[S_d D_d]`.                           (6.2)

By (6.1),

`[S_d+(lambda-1)sum_i U_i]/S_d`
` <= 1+(lambda-1)/(d-lambda)`
` = (d-1)/(d-lambda)`.                                           (6.3)

Also there are `d+1` branch variables and each satisfies `B_i>=1-lambda/d`, so

`D_d>=lambda-1+(d+1)(1-lambda/d)`
`   =d-lambda/d=(d^2-lambda)/d`.                                 (6.4)

Thus

`h_d/c_d <= d(d-1)/[(d-lambda)(d^2-lambda)]`.                    (6.5)

Since `h_{d+1}/c_{d+1}>=0`, (4.8) gives the deliberately simple one-sided bound

`Delta <= f_d(lambda):=d(d-1)/[(d-lambda)(d^2-lambda)]`.          (6.6)

Fix `L<d`. The positive function `lambda f_d(lambda)` is increasing on `[1,L]`, because its numerator increases and both denominator factors decrease. Hence

`lambda Delta <= A_{d,L}`                                        (6.7)

where

`A_{d,L}:=d(d-1)L/[(d-L)(d^2-L)]`.                               (6.8)

The sharper lower-elasticity term from PROB10-06 would reduce this budget further, but is unnecessary for the clean theorem below.

## 7. New endpoint-retention argument at distance `1/100` from the boundary

Set

`delta=1/100`,
`L=d-delta`.                                                       (7.1)

Then (6.8) becomes

`A:=A_{d,d-delta}`
` = d(d-1)(d-delta)/[delta(d(d-1)+delta)]`.                       (7.2)

By (4.7), (4.9), and (6.7), it suffices to prove

`F(theta):=d+theta-A theta(1-theta)>0`.                           (7.3)

### 7.1 Small upper-degree contamination: `p<=delta`

By (5.10), `theta<=p<=delta`. Therefore

`F(theta)>=d-A theta>=d-A delta`.                                (7.4)

Using (7.2),

`d-A delta`
` = d - d(d-1)(d-delta)/(d(d-1)+delta)`
` = d^2 delta/(d(d-1)+delta)>0`.                                 (7.5)

So every `p<=1/100` is certified.

This already improves the predecessor `{3,4}` small-p tail from `1/200` to `1/100` at the same endpoint `2.99`.

### 7.2 Small lower-degree contamination: `p>=1-delta`

Write `r=1-p<=delta`. From (5.11),

`theta >= theta_0:= (d+1)(1-delta)/(d+1+delta)`.                 (7.6)

For `delta=1/100`,

`theta_0 = 99(d+1)/(100d+101) >1/2`.                             (7.7)

Moreover

`F'(theta)=1-A+2A theta=1+A(2theta-1)>0`                          (7.8)

throughout `[theta_0,1]`. Thus the worst allowed tilted mixture is exactly `theta_0`, so it is enough to evaluate `F(theta_0)`.

Substituting (7.2) with `delta=1/100` gives the exact rational identity

`F(theta_0)=N(d)/[(100d+101)^2(100d^2-100d+1)]`,                 (7.9)

where

`N(d)=10000 d^5 +39900 d^4 +1019800 d^3`
`     -9900 d^2 -989600 d +9999`.                                (7.10)

For every integer `d>=2`, group

`N(d)`
` =[10000d^5-9900d^2] +39900d^4`
`  +[1019800d^3-989600d] +9999`.                                 (7.11)

Every displayed term is strictly positive for `d>=2`. Hence

`F(theta_0)>0`.                                                    (7.12)

Therefore every `p>=99/100` is certified as well.

This is the second mechanism gain relative to the predecessor: instead of replacing `d+theta` by `d` and `theta(1-theta)` by a coarse endpoint estimate, the proof retains the exact branch-addition lower bound on `theta` and uses the monotonicity of the full quadratic `F`. That extra `+theta` is precisely what makes the **same** `1/100` defect width work on the high-p side.

## 8. Completion of Theorem A, including low parent bias

Sections 4--7 prove

`ell'_lambda<0`

for every

`1<=lambda<=d-1/100`                                             (8.1)

under either tail in (3.2).

He--Wang--Xiang give strict decrease on `[0,theta_d]`, with `theta_d>1` for every `d>=2`. Hence their theorem overlaps (8.1), and together the two intervals cover

`0<=lambda<=d-1/100`.                                             (8.2)

This proves Theorem A.

No simulation or floating-point sign test is used in the argument.

## 9. Exact d=3 margins and executed checker

For the predecessor family `d=3`, `delta=1/100`, `L=299/100`, exact arithmetic gives

`A=179400/601`.                                                    (9.1)

On the small-p tail `p<=1/100`, (7.5) gives

`M-lambda M' >= 9/601`.                                          (9.2)

Since `M+lambda<=4+299/100=699/100`,

`-ell'_lambda >= 20000/32627689`
`                =0.0006129762975...`                            (9.3)

uniformly on `1<=lambda<=2.99`.

On the high-p tail `p>=99/100`,

`theta>=396/401`                                                  (9.4)

and the exact full-quadratic gap is

`M-lambda M' >= 30148599/96641401`.                              (9.5)

Therefore

`-ell'_lambda >= 200990660000/15739695056667`
`                =0.01276966671...`.                             (9.6)

The exact checker and executed output saved with this report are

- `2026-09-20T03-31-00Z__adjacent-rare-tail-all-d-check.py`,
- `2026-09-20T03-31-00Z__adjacent-rare-tail-all-d-check.out`.

The output ends

`ALL_EXACT_CHECKS_PASS`.

The code also checks the exact rational gaps for sample degrees through `d=1000`; the proof for all `d>=2` is the algebraic positivity argument (7.11), not finite enumeration.

## 10. Demonstrated mechanism gain versus source-level gain

### Source-level gain

Before this run, NM13-05 had only a fixed `{3,4}` near-boundary theorem, with defect probability at most `1/200` on either endpoint and endpoint `lambda=2.99`.

After this run:

- **every** adjacent no-leaf family `{d,d+1}`, `d>=2`, has a rigorous endpoint strip through `lambda=d-0.01`;
- the allowed endpoint contamination is `1/100` on either side;
- for `d=3`, the endpoint remains `2.99` while each allowed defect tail doubles from `0.005` to `0.01`.

The parent problem itself remains OPEN.

### Mechanism gain

The predecessor had a degree-specific branch-addition ratio. This run proves the exact all-degree ratio

`(d+1)/(d+2) <= c_{d+1}/c_d <=1`,                               (10.1)

then keeps the resulting **tilted endpoint location** inside the full derivative quadratic rather than throwing it away. The result is a uniform theorem whose distance to the singular minimum-degree boundary and whose endpoint contamination have the same explicit scale `1/100`.

This mechanism is complementary to P01's analytic secant/covariance route: P01 allows broad support but works farther from `d`; the present route exploits adjacent-support coupling to reach `d-0.01`.

## 11. Residual obstruction and next materially different attack

The theorem still stops at `lambda<d` because the pathwise escape sensitivity `U/B<=1/(d-lambda)` is singular at the minimum degree. This is not a true critical boundary for a mixture with `p>0`, whose mean is `d+p>d`.

The next decisive target remains the occupation-weighted regeneration idea recorded in the predecessor handoff: for `p` near `1`, prove a bound of the schematic form

`|d/dlambda log B| <= C/(d+1-lambda) + C' * P_regen(encounter degree d)/(d-lambda)`

or an equivalent block-score estimate in which the singular degree-`d` sensitivity is multiplied by an actual regeneration occupation probability of degree-`d` vertices. A bound of order `O(1-p)` on that occupation contribution would have a route to crossing `lambda=d` for sufficiently small `1-p`.

The previous cross-boundary flow lower bound and Laplace-transform covariance idea remain incomplete because value-level escape control does not by itself control `-B'`, and no monotone covariance sign for the required Laplace score has yet been proved. Those failures are preserved rather than recycled as results.

## 12. ledger_delta

```yaml
ledger_delta:
  track: NM13-05
  parent: T06
  source_id: P0066
  source_problem: Lyons-Pemantle-Peres biased-walk speed monotonicity on no-leaf supercritical Galton-Watson trees
  runtime_model: GPT-5.6 Sol
  reasoning_level: UNVERIFIED
  bias_convention:
    parent_bias: lambda
    child_bias: beta=1/lambda
  parent_status_before: OPEN
  parent_status_after: OPEN
  restricted_scope_before:
    family: P(nu=3)=1-p, P(nu=4)=p
    theorem: p<=1/200 or p>=199/200 gives strict decrease on 0<=lambda<=2.99
  restricted_scope_after:
    family: P(nu=d)=1-p, P(nu=d+1)=p, every integer d>=2
    theorem: p<=1/100 or p>=99/100 gives strict decrease on 0<=lambda<=d-1/100
    d3_gain: same endpoint 2.99 with both defect widths doubled from 1/200 to 1/100
  mechanism_before: degree-3 branch-addition escape ratio plus coarse endpoint rarity estimate
  mechanism_after:
    - all-d branch-addition ratio (d+1)/(d+2) <= c_{d+1}/c_d <= 1
    - exact escape-tilted endpoint retention inside derivative quadratic F(theta)
    - exact all-d polynomial positivity certificate at delta=1/100
  simulated_signs_used: false
  exact_checker: proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T03-31-00Z__adjacent-rare-tail-all-d-check.py
  exact_output: proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T03-31-00Z__adjacent-rare-tail-all-d-check.out
  checker_terminal_line: ALL_EXACT_CHECKS_PASS
  failed_route_preserved:
    - cross-minimum-degree occupation-weighted regeneration sensitivity remains unproved
    - value-level electrical escape bound does not justify derivative monotonicity
    - Laplace-score covariance route lacks a certified score monotonicity bound
  unchanged_substantive_runs: 0
  recovery_failures: 0
  next_attack: occupation-weighted regeneration score bound capable of crossing lambda=d for p near 1
  status: PARTIAL
```

This report is a proposed complete proof of the stated restricted theorem, hence a **restricted theorem candidate pending later independent review**, not a closure of the parent conjecture.

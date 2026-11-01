Actual runtime model: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. SUBSTANTIVE MOVEMENT: T06 remains OPEN globally, but a new non-simulation escape-probability theorem extends the rigorously monotone parent-bias interval for rare-defect offspring laws `P(nu=2)=1-p, P(nu=3)=p` from the inherited all-`p` endpoint `theta_2 in (1.811,1.812)` to `lambda=19/10` whenever `0<p<=1/30` or `35/36<=p<1`; equivalently the child-bias speed has `v'(beta)>0` on `10/19<=beta<=1`, with exact positive margins.**

# NM13-05 T06 — rare-defect escape-envelope coupling for `{2,3}` offspring

Date: 2026-09-20.  
Repository: `yspennstate/math-open-problems`, branch `master`.  
Own root: `proofnet24/NM13-05/progress-tree-speed`.  
Parent target: T06 / intake P0066, Lyons--Pemantle--Peres monotonicity of biased-walk speed on a supercritical Galton--Watson tree without leaves.  
Status: **PARTIAL / OPEN parent; RESTRICTED THEOREM CANDIDATE pending later independent review.**

No simulated derivative signs are used anywhere in this report.

## 1. Progress-first handoff and inherited mathematics

`operations/PROGRESS20_2026-09-20.md` is controlling for this slot. Its LIVE20 table assigns NM13-05 to **T06 escape-probability/regeneration coupling**, with P01 as the complementary analytic-regeneration derivative worker. This supersedes NM13-05's older residue-4 admission loop. All old NM13-05 claims, reports, handoffs, and the P0411 history remain untouched; none is relabelled as T06 progress.

The older repository attempt on P0066 is preserved exactly: for a fixed local offspring count `D`, the radial drift `(D-lambda)/(D+lambda)` decreases with parent bias, and on a regular tree this is the exact speed, but in a nondegenerate Galton--Watson environment the stationary law seen by the walk changes with `lambda`. That attempt did **not** control the measure-change term and did not produce a speed-level monotone coupling.

Two newer dependencies were recovered before this derivation:

1. `runs/prob10_2026-09-20/PROB10-06/20260920T0013Z_two_point_escape_derivative_bridge_4f6c2e91.md` proves, for every nondegenerate `{2,3}` offspring law, strict decrease through a unique endpoint `theta_2 in (1.811,1.812)` and gives an exact two-support cancellation for the environment-change term.
2. `proofnet24/P01-progress-speed/runs/2026-09-20/2026-09-20T00-02-50Z__run-report.md` proves a different bounded-support theorem by a generic covariance/range estimate, including support contained in `{2,...,10}` through `lambda=6/5` and `{2,3,4}` much farther. I do not duplicate that route.

The new mechanism below is complementary: it keeps the exact mixture factor that the two-support proof previously discarded by AM--GM, and controls the remaining escape-factor ratio by deterministic regular-tree envelopes. Thus closeness of the offspring law to a deterministic tree becomes a quantitative sign resource.

## 2. Frozen source assumptions and bias convention

Let the offspring variable be `nu`. The source problem assumes

`P(nu=0)=0`, `m=E nu>1`.

The **parent-bias convention** used throughout this report is the one in He--Wang--Xiang, arXiv:1610.08151: at a non-root vertex with `k` children,

`P(step to parent | k)=lambda/(lambda+k)`,

`P(step to each fixed child | k)=1/(lambda+k)`.

Hence increasing `lambda` biases more strongly toward the root, and the source conjecture is that the limiting speed `ell_lambda` is nonincreasing for `0<=lambda<m`.

The reciprocal **child-bias convention** of Ben Arous--Fribergh--Sidoravicius, arXiv:1111.5865, is

`beta=1/lambda`.

With parent edge weight 1 and each child edge weight `beta`, increasing `beta` biases away from the root. If `v(beta)=ell_{1/beta}`, then wherever differentiable

`v'(beta)=-ell'_{1/beta}/beta^2`.

Thus a strict negative parent-bias derivative is a strict positive child-bias derivative.

For the new theorem freeze the exact nondegenerate bounded offspring family

`P(nu=2)=1-p, P(nu=3)=p`, `0<p<1`.

Then `m=2+p`, there are no leaves, and the entire new interval `1<=lambda<=19/10` lies strictly inside the transient/source range because `19/10<2<m`.

## 3. Primary-source facts actually used

The two requested primary sources were re-read.

- Ben Arous--Fribergh--Sidoravicius, arXiv:1111.5865, proves the LPP monotonicity conjecture for sufficiently high child bias (`v(beta)` increasing for `beta>=717` in the arXiv version) using a common regeneration construction. This fixes the reciprocal convention and supplies the historical coupling route, but its quantitative high-bias regime is far from `beta in [10/19,1]`.
- He--Wang--Xiang, arXiv:1610.08151, later published in *Journal of Applied Probability* 62 (2025), proves strict decrease for

`0 <= lambda <= m1/(1+sqrt(1-1/m1))`

when the minimum offspring `m1>=2`. For `m1=2` this endpoint is `4-2sqrt(2)=1.171572...`.

The proof below uses their Aidekon speed representation and the following escape estimates for `1<=lambda<2`. If `B` is the quenched probability, from a vertex, of escaping to infinity before hitting its parent and `U=-dB/dlambda`, then almost surely

`1-lambda/2 <= B <= 1-lambda/3`,

`0 < U <= B/(2-lambda)`.

On compact subintervals of `[1,2)`, these bounds also give the domination needed to differentiate the expectations below.

A bounded current literature search on 20 September 2026 recovered the 2025 He--Wang--Xiang publication, Bowditch--Tokushige differentiability/analyticity papers, the older high-bias coupling papers, and progeny-distribution monotonicity results. It did not surface a theorem matching the rare-defect parameter region proved here. This is **bounded negative evidence only**, not a novelty certificate.

`POSTED.md` was checked. It contains no posted closure of P0066; restricted results must not be promoted to source-wide closure.

## 4. Before/after parent scope versus mechanism gain

### Parent problem

Before: **OPEN**.  
After: **OPEN**.

No universal no-leaf monotonicity theorem is claimed.

### Rigorously demonstrated restricted scope

Inherited same-family baseline from the current PROB10-06 work:

`P(nu=2)=1-p, P(nu=3)=p, 0<p<1:  ell'_lambda<0 for 0<=lambda<theta_2`,

where `theta_2 in (1.811,1.812)`.

After this run, for the rare-defect subfamilies

`0<p<=1/30` or `35/36<=p<1`,

strict decrease is proved on

`0<=lambda<=19/10`.

(The interval below `lambda=1` is already supplied by the published low-bias theorem; the new proof handles `[1,19/10]`.)

### Mechanism-level gain

The difficult environment-change term is not bounded by a support-width covariance as in P01 and is not replaced by the worst-case `xy<=(x+y)^2/4` as in the inherited two-support report. Instead, the exact factor

`p(1-p)c_2 c_3 / ((1-p)c_2+p c_3)^2`

is retained. Pointwise escape envelopes then bound `c_3/c_2`. The measure-change cost therefore tends to zero as the offspring law tends to either deterministic regular tree. This is a demonstrated escape-probability coupling mechanism, not a simulation heuristic.

## 5. Escape variables and exact two-support cancellation

Let `B_0,...,B_k` be iid copies of `B`, with corresponding `U_i=-B_i'`, and put

`S_k=sum_{i=0}^k B_i`,

`D_k=lambda-1+S_k`,

`c_k=E[ (1/(k+1)) S_k/D_k ]`,

`h_k=E[ (1/(k+1)) sum_{i=0}^k (B_i+(lambda-1)U_i)/D_k^2 ]`.

Differentiating `S_k/D_k` gives exactly

`c_k'=-h_k`.                                                     (5.1)

Define

`A=(1-p) 2 c_2 + p 3 c_3`,

`C=(1-p)c_2+p c_3`,

`H_1=(1-p)h_2+p h_3`,

`H_nu=(1-p)2h_2+p3h_3`.

Aidekon's symmetrized speed formula is

`ell_lambda=(A-lambda C)/(A+lambda C)`.                           (5.2)

Expanding the four terms gives the exact cancellation

`A H_1-C H_nu = p(1-p)(c_3 h_2-c_2 h_3)`.                        (5.3)

This is inherited algebra, but the new step is to **retain** its full mixture dependence.

As in the recovered two-support argument, set

`Q=(2-lambda)(2-lambda/2)`,

`V=3-lambda/3`,

`a(lambda)=1/Q-1/V`.

The escape and derivative bounds give

`h_2 <= c_2/Q`, `h_3 >= c_3/V`,                                  (5.4)

so

`A H_1-C H_nu <= p(1-p)c_2c_3 a(lambda)`.                         (5.5)

For `1<=lambda<2`, `a(lambda)>0`.

From (5.1)--(5.2), direct differentiation yields

`-ell'_lambda`
` = 2 lambda [ A C/lambda-(A H_1-C H_nu)]/(A+lambda C)^2`.        (5.6)

Because `2C<=A<=3C`, define

`R_p(lambda):=p(1-p)c_2c_3/C^2`.

Whenever the bracket is positive, (5.5)--(5.6) imply

`-ell'_lambda >= [4-2 lambda a(lambda) R_p(lambda)]/(3+lambda)^2`.
                                                                        (5.7)

Thus the entire problem on this family has been reduced to an upper bound on one dimensionless escape-mixture factor.

## 6. New escape-envelope coupling: control `c_3/c_2`

Write

`b_-=1-lambda/2`, `b_+=1-lambda/3`.

For fixed `k`, if

`x=S_k/(k+1)`,

then

`c_k=E f_k(x)`, `f_k(x)=x/(lambda-1+(k+1)x)`.

For `lambda>=1`, `f_k` is nondecreasing. Since every `B_i` lies in `[b_-,b_+]`, pointwise comparison with the two deterministic regular-tree envelopes gives

`c_2 >= f_2(b_-)=(2-lambda)/(4-lambda)`,                          (6.1)

`c_2 <= f_2(b_+)=(3-lambda)/6`,                                  (6.2)

`c_3 >= f_3(b_-)=(2-lambda)/(2(3-lambda))`,                       (6.3)

`c_3 <= f_3(b_+)=(3-lambda)/(9-lambda)`.                          (6.4)

Put `t=c_3/c_2`. Then

`R_-(lambda):=3(2-lambda)/(3-lambda)^2 <= t`

and

`t <= R_+(lambda):=(3-lambda)(4-lambda)/((9-lambda)(2-lambda))`.  (6.5)

Now

`R_p = p(1-p)t/(1-p+p t)^2`.                                     (6.6)

There are two asymmetric ways to exploit (6.6).

### Mostly binary offspring (`p` small)

Since the denominator in (6.6) is at least `(1-p)^2`, (6.5) gives

`R_p(lambda) <= [p/(1-p)] R_+(lambda)`.                           (6.7)

### Mostly ternary offspring (`1-p` small)

Since the denominator in (6.6) is at least `(p t)^2`, (6.5) gives

`R_p(lambda) <= [(1-p)/p] / R_-(lambda)`.                         (6.8)

Equations (6.7)--(6.8) are the new coupling gain. They convert probabilistic closeness to either regular tree into a small upper bound on the measure-change contribution.

## 7. Uniform rare-defect theorem up to any certified endpoint

On `1<=lambda<2`, `a(lambda)` and `R_+(lambda)` are increasing while `R_-(lambda)` is decreasing. For the endpoint actually used below it is enough to certify this on `[1,19/10]`:

`a'(lambda)=4(3-lambda)/((2-lambda)^2(4-lambda)^2)-3/(9-lambda)^2 >0`;  (7.1)

on `[1,19/10]`, the first term is at least `22/45` and the second at most `300/5041`, leaving the exact positive gap `97402/226845`.

Also

`R_+'(lambda)=-2(2lambda^2-6lambda-3)/((lambda-9)^2(lambda-2)^2)>0`,   (7.2)

because the quadratic is negative throughout this interval, and

`R_-'(lambda)=3(lambda-1)/(lambda-3)^3 <=0`.                         (7.3)

Consequently for any `1<=L<=19/10`, (5.7)--(6.8) prove strict monotonicity on `[1,L]` under either sufficient condition

`p/(1-p) < 2/[L a(L) R_+(L)]`,                                     (7.4)

or

`(1-p)/p < 2 R_-(L)/[L a(L)]`.                                     (7.5)

This is already a continuum of rigorously covered offspring/bias regions, not a single checked point.

## 8. Exact endpoint `L=19/10`

At `L=19/10`, exact arithmetic gives

`Q=21/200`,

`V=71/30`,

`a(L)=13570/1491`,

`R_+(L)=231/71`,

`R_-(L)=30/121`.                                                    (8.1)

Therefore

`L a(L) R_+(L)=283613/5041`,                                      (8.2)

and the sharp sufficient small-`p` condition supplied by this envelope is

`p/(1-p) < 10082/283613`,

or equivalently

`p < 10082/293695 = 0.0343281295...`.                              (8.3)

Similarly

`L a(L)/R_-(L)=3119743/44730`,                                    (8.4)

and the sufficient large-`p` condition is

`(1-p)/p < 89460/3119743`,

or equivalently

`p > 3119743/3209203 = 0.9721239198...`.                           (8.5)

For clean closed rational subregions I use

`0<p<=1/30` or `35/36<=p<1`.                                      (8.6)

These lie strictly inside the thresholds (8.3), (8.5), so the sign has a positive uniform margin even at `lambda=19/10`.

### 8.1 Mostly binary quantitative margin

For `p<=1/30`, `p/(1-p)<=1/29`. Using monotonicity in Section 7, the numerator in (5.7) is bounded below on the whole rectangle by

`4-2*(283613/5041)*(1/29)=17530/146189`.                           (8.7)

Since `(3+lambda)^2<=(49/10)^2=2401/100`,

`BOX: -ell'_lambda >= 1753000/350999789`

`                    = 0.004994304996... >0`                       (8.8)

for every

`0<p<=1/30`, `1<=lambda<=19/10`.

### 8.2 Mostly ternary quantitative margin

For `p>=35/36`, `(1-p)/p<=1/35`. The corresponding numerator is at least

`4-2*(3119743/44730)*(1/35)=11357/782775`.                         (8.9)

Thus

`BOX: -ell'_lambda >= 45428/75177711`

`                    = 0.000604274849... >0`                       (8.10)

for every

`35/36<=p<1`, `1<=lambda<=19/10`.

Combining either rectangle with the published low-bias theorem gives strict parent-bias speed decrease throughout `0<=lambda<=19/10`.

In child-bias notation `beta=1/lambda`, (8.8)--(8.10) give

`v'(beta)=-ell'_{1/beta}/beta^2 >0`,

for `10/19<=beta<=1`, with the same displayed constants as valid (slightly conservative) lower bounds because `1/beta^2>=1` there.

This is the requested **derivative-positive child-bias/offspring region**.

The deterministic endpoints `p=0` and `p=1` are regular trees and are elementary separately; I keep the theorem statement nondegenerate so that the source minimum-degree hypotheses and two-point notation are literal.

## 9. Why this is complementary to P01 rather than a duplicate

P01 rewrites the derivative through a `u`-tilted effective offspring and bounds a covariance by the total ranges of offspring and an escape-score variable. That is robust over broad bounded supports but pays for the entire support width even when one exceptional degree is extremely rare.

Here no support-width covariance estimate is used. The two-support algebra isolates the measure-change term exactly, and (6.7)--(6.8) preserve its `p(1-p)` rarity. The only comparison is an escape-probability envelope against the two adjacent deterministic regular trees. This is precisely why the endpoint can be pushed from the inherited all-`p` `~1.811` to `1.9` near either deterministic law while P01's generic-width bound is not designed to exploit rarity.

The 2011 common-super-regeneration construction was also reconsidered. In the source's child-bias variable, our new interval is `beta in [10/19,1]`; the published high-bias coupling thresholds are far outside this range. The minimal-degree rescaling does not bridge that quantitative gap. Therefore I did not present that regeneration construction as if it proved the new rectangle.

## 10. Exact checker and execution

Only after the symbolic proof was obtained, I executed an exact `fractions.Fraction` checker for the endpoint constants, threshold conversions, monotonicity certificate, and the two rational derivative margins.

Files committed with this report:

- `2026-09-20T00-31-00Z__rare-defect-escape-check.py`
- `2026-09-20T00-31-00Z__rare-defect-escape-check.out`

The archived output ends

`ALL_EXACT_CHECKS_PASS`.

This checker verifies arithmetic only. The probabilistic argument is written on the page above.

## 11. Residual obstruction and next mathematical attack

The new mechanism exposes its own sharp weakness. The derivative envelope `U<=B/(2-lambda)` pays for the **global minimum offspring 2**, so it becomes singular as `lambda upward 2` even when degree-2 vertices are extremely rare. Thus the present proof cannot cross `lambda=2`, while for `p` near 1 the true transience edge is `m=2+p`, close to 3.

The next attack should therefore be genuinely probabilistic rather than another algebraic tightening of (7.4): construct a regeneration/escape estimate in which the cost of the bad degree-2 derivative is charged only on visits to rare degree-2 vertices. A successful statement would replace the global factor `1/(2-lambda)` by an occupation-weighted defect term of order roughly `(1-p)/(2-lambda)` under the relevant regeneration law. That could potentially cross `lambda=2` for `p` sufficiently close to 1, something the current global-minimum bound structurally cannot do.

No audit is awaited before that attack.

## 12. Ledger delta

```yaml
ledger_delta:
  worker: NM13-05
  live20_parent: T06
  source_id: P0066
  status_before: OPEN
  status_after: OPEN
  parent_problem_scope_before: "no source-wide closure; current repo same-family {2,3} all-p rigorous endpoint theta_2 in (1.811,1.812)"
  parent_problem_scope_after: "for P(nu=2)=1-p, P(nu=3)=p with 0<p<=1/30 or 35/36<=p<1, rigorous strict decrease extended through lambda=19/10; parent remains OPEN"
  bias_convention: "parent bias lambda; reciprocal child bias beta=1/lambda"
  new_child_bias_region: "10/19 <= beta <= 1, v'(beta)>0 on the stated rare-defect offspring rectangles"
  certified_margin_small_p: "-ell'(lambda) >= 1753000/350999789"
  certified_margin_large_p: "-ell'(lambda) >= 45428/75177711"
  mechanism_gain: "retain exact p(1-p) two-support measure-change factor and bound c3/c2 by deterministic escape envelopes; rarity rather than support width controls the derivative correction"
  simulation_used_as_proof: false
  theorem_label: "RESTRICTED THEOREM CANDIDATE / PARTIAL parent"
  novelty: UNVERIFIED
  residual_obstruction: "global-minimum escape derivative bound diverges at lambda=2; need rare-degree occupation/regeneration charging to cross 2"
  next_attack: "occupation-weighted regeneration coupling for rare degree-2 vertices"
```

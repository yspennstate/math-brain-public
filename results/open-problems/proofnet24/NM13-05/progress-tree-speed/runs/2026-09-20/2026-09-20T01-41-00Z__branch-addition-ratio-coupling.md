Actual runtime model: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6/maximum was requested, but no authenticated reasoning-effort telemetry is exposed, so I do not claim GPT-6/maximum. SUBSTANTIVE MOVEMENT: T06 remains OPEN globally; for the exact family `P(nu=2)=1-p, P(nu=3)=p`, a new branch-addition escape coupling proves `3/4 <= c_3/c_2 <= 1`, replaces the predecessor's crude one-sided escape-ratio envelopes by an exact tail-mixture bound, widens the `lambda=19/10` theorem from `p<=1/30 or p>=35/36` to `p<=1/8 or p>=9/10`, and extends the old rare-defect rectangles `p<=1/30 or p>=35/36` from `lambda=19/10` to `lambda=983/500=1.966`.**

# NM13-05 T06 — branch-addition coupling and two-sided escape-ratio compression

Date: 2026-09-20.  
Repository: `yspennstate/math-open-problems`, branch `master`.  
Own root: `proofnet24/NM13-05/progress-tree-speed`.  
Parent target: T06 / intake P0066, Lyons--Pemantle--Peres monotonicity of biased-walk speed on a supercritical Galton--Watson tree without leaves.  
Status: **PARTIAL / OPEN parent; NEW RESTRICTED THEOREM CANDIDATE pending later independent review.**

No simulated sign is used as evidence.

## 1. Compact handoff and exact conventions

`operations/PROGRESS20_2026-09-20.md` assigns NM13-05 to T06 by an escape-probability/regeneration-coupling route, complementary to P01's analytic covariance/regeneration-derivative route.

The original P0066 attempt is preserved rather than relabelled. It observed that, at fixed offspring number `k`, the local radial drift

`(k-lambda)/(k+lambda)`

decreases with parent bias `lambda`, but this does not control the bias-dependent environment seen by the walk. That missing measure-change term is the actual obstruction.

The predecessor NM13-05 report is

`proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T00-31-00Z__rare-defect-escape-envelope.md`.

It proved, for

`P(nu=2)=1-p`, `P(nu=3)=p`,

strict decrease through `lambda=19/10` for the two rare-defect tails

`0<p<=1/30` or `35/36<=p<1`.

Its limitation was that the ratio `c_3/c_2` was bounded by separate deterministic regular-tree envelopes, causing a large loss near `lambda=2`.

The latest relevant complementary work consumed here is:

- `runs/prob10_2026-09-20/PROB10-06/20260920T0132Z_escape_elasticity_cone_bridge_7d4a2c91.md`, which proves an all-mixture `{2,3}` endpoint `Lambda_sharp in (1.84734,1.84735)` by a logarithmic escape-derivative cone;
- `proofnet24/P01-progress-speed/runs/2026-09-20/2026-09-20T00-58-12Z__run-report.md`, which improves broad bounded-support rectangles by a tilted-mean covariance estimate. The route below is not that support-width/covariance argument.

### Bias convention

At a vertex with `k` children, the **parent-bias** convention is

`P(parent)=lambda/(lambda+k)`,
`P(each fixed child)=1/(lambda+k)`.

Thus increasing `lambda` points more strongly toward the root, and the conjectural sign is `ell'_lambda<=0`.

The **child-bias** convention of arXiv:1111.5865 is reciprocal:

`beta=1/lambda`.

If `v(beta)=ell_{1/beta}`, then

`v'(beta)=-ell'_{1/beta}/beta^2`.

Hence a strict negative parent-bias derivative is a strict positive child-bias derivative.

### Requested primary sources

- Ben Arous--Fribergh--Sidoravicius, arXiv:1111.5865, prove increasing child-bias speed for sufficiently high bias; the arXiv theorem gives the historical explicit threshold `beta>=717` and uses a common regeneration construction.
- He--Wang--Xiang, arXiv:1610.08151, later J. Appl. Probab. 62 (2025), prove strict decrease in parent bias for

  `0<=lambda<=m_1/(1+sqrt(1-1/m_1))`

  when the minimum offspring `m_1>=2`. For `m_1=2` the endpoint is `4-2sqrt(2)>1`.

A bounded current search dated 2026-09-20 recovered these results, Bowditch--Tokushige differentiability/analyticity work, and related progeny-distribution monotonicity papers, but no source-wide resolution and no checked theorem matching the branch-addition ratio lemma below. This is bounded negative evidence only, not a novelty certificate.

`POSTED.md` was checked; no posted source-wide P0066 closure is recorded.

## 2. Parent-problem scope before/after

### Parent problem

Before: **OPEN**.  
After: **OPEN**.

No source-wide monotonicity theorem is claimed.

### Strongest inherited `{2,3}` scopes used as baseline

1. All `p in [0,1]`: strict decrease through the current all-mixture endpoint `lambda=1847/1000` (and in fact up to the reported root in `(1.84734,1.84735)`).
2. NM13-05 rare tails:
   - `0<p<=1/30`, or
   - `35/36<=p<1`,
   through `lambda=19/10`.

### New source-level restricted scope proved in this run

For the same exact no-leaf family `P(nu=2)=1-p`, `P(nu=3)=p`:

1. **Wider tails at the old endpoint**

   `0<p<=1/8` or `9/10<=p<1`

   imply strict decrease on

   `0<=lambda<=19/10`.

2. **Deeper endpoint on the predecessor's old rare tails**

   `0<p<=1/30` or `35/36<=p<1`

   imply strict decrease on

   `0<=lambda<=983/500 = 1.966`.

In child-bias notation, the second statement gives

`v'(beta)>0` for every `beta>=500/983`

on those two rare-tail offspring rectangles.

These are theorem-scope gains, not simulations or finite enumerations.

## 3. Starting exact derivative reduction

Fix `1<=lambda<2`. Let `B` be the quenched probability of escaping to infinity before hitting the parent, and put `U=-dB/dlambda`.

For conditional offspring `k`, let `B_0,...,B_k` be iid copies of `B`, with corresponding `U_i`, and define

`S_k=sum_{i=0}^k B_i`,
`D_k=lambda-1+S_k`,

`c_k=E[(1/(k+1))*S_k/D_k]`,

`h_k=E[(1/(k+1))*sum_{i=0}^k (B_i+(lambda-1)U_i)/D_k^2]`.

Direct differentiation gives

`c_k'=-h_k`.                                                     (3.1)

Write `q=1-p` and

`A=2q c_2+3p c_3`,
`C=q c_2+p c_3`,

`H_1=q h_2+p h_3`,
`H_nu=2q h_2+3p h_3`.

Aidekon's symmetrized speed formula is

`ell_lambda=(A-lambda C)/(A+lambda C)`.                           (3.2)

The exact two-support cancellation is

`A H_1-C H_nu = pq(c_3 h_2-c_2 h_3)`.                            (3.3)

The predecessor escape estimates give

`h_2 <= c_2/Q`,
`h_3 >= c_3/V`,                                                   (3.4)

where

`Q=(2-lambda)(2-lambda/2)`,
`V=3-lambda/3`.

Define

`a(lambda)=1/Q-1/V`
`         =2/[(2-lambda)(4-lambda)]-3/(9-lambda)`.               (3.5)

Then

`A H_1-C H_nu <= pq c_2 c_3 a(lambda)`.                          (3.6)

Differentiating (3.2) and using (3.3) gives exactly

`-ell'_lambda`
` = 2 lambda [A C/lambda-(A H_1-C H_nu)]/(A+lambda C)^2`.        (3.7)

Because `2C<=A<=3C`, set

`R_p := pq c_2 c_3/C^2`.                                         (3.8)

Whenever the numerator below is positive, (3.6)--(3.8) imply

`BOX: -ell'_lambda >= [4-2 lambda a(lambda) R_p]/(3+lambda)^2`.   (3.9)

Thus all remaining work is to control one dimensionless mixture factor `R_p`.

## 4. New branch-addition coupling: `3/4 <= c_3/c_2 <= 1`

This is the run's main mechanism lemma.

Let

`phi(s)=s/(lambda-1+s)`,

which is increasing and concave for `lambda>=1`, with `phi(0)=0`. For iid nonnegative escape variables `B_i`, write

`S_3=B_1+B_2+B_3`,
`S_4=B_1+B_2+B_3+B_4`.

Then

`c_2=(1/3)E phi(S_3)`,
`c_3=(1/4)E phi(S_4)`.                                           (4.1)

### Lower ratio bound

Couple `S_4=S_3+B_4`. Since `phi` is increasing,

`E phi(S_4) >= E phi(S_3)`.

Therefore

`c_3/c_2 >= (1/4)/(1/3)=3/4`.                                   (4.2)

### Upper ratio bound

Fix deterministic `x_1,...,x_4>=0`, set `S=sum x_i`, and assume `S>0`. Concavity plus `phi(0)=0` gives, for each `i`,

`phi(S-x_i)`
` = phi((1-x_i/S)S + (x_i/S)0)`
` >= (1-x_i/S) phi(S)`.

Summing over `i=1,...,4` yields

`sum_i phi(S-x_i) >= 3 phi(S)`.                                  (4.3)

For iid `B_i`, every leave-one-out sum `S_4-B_i` has the same law as `S_3`. Taking expectations in (4.3),

`4 E phi(S_3) >= 3 E phi(S_4)`.

Hence

`c_3 <= c_2`.                                                     (4.4)

Combining (4.2) and (4.4),

`BOX: 3/4 <= t:=c_3/c_2 <= 1`.                                   (4.5)

This uses only adding one iid escape branch and concavity. It is independent of the predecessor's separate regular-tree upper/lower envelopes for `c_2` and `c_3`.

## 5. Exact optimization of the mixture correction

By (3.8),

`R_p = F_p(t) := p q t/(q+p t)^2`,                               (5.1)

with `t in [3/4,1]`. Differentiate:

`F_p'(t)=p q (q-p t)/(q+p t)^3`.                                 (5.2)

Therefore the exact maximum over the certified interval is

`rho(p):=max_{3/4<=t<=1} F_p(t)`

` = p(1-p),                         0<p<=1/2,`
` = 1/4,                            1/2<=p<=4/7,`
` = 12 p(1-p)/(4-p)^2,             4/7<=p<1.`                    (5.3)

Explanation:

- for `p<=1/2`, `q/p>=1`, so `F_p` increases throughout `[3/4,1]`;
- for `p>=4/7`, `q/p<=3/4`, so `F_p` decreases throughout `[3/4,1]`;
- in the middle, the critical point `t=q/p` lies inside and gives the usual maximum `1/4`.

Substituting (5.3) into (3.9) proves:

### Theorem 5.1 — branch-addition derivative criterion

For

`P(nu=2)=1-p`, `P(nu=3)=p`, `0<p<1`,

and `1<=lambda<2`, if

`lambda a(lambda) rho(p) < 2`,                                   (5.4)

then

`BOX: -ell'_lambda >= [4-2 lambda a(lambda) rho(p)]/(3+lambda)^2 >0`. (5.5)

This is a complete non-simulation derivative certificate.

### Monotonicity needed for rectangles

At `lambda=1`,

`a(1)=7/24>0`.

Also

`a'(lambda)`
` =4(3-lambda)/[(2-lambda)^2(4-lambda)^2]-3/(9-lambda)^2`.

For `1<=lambda<2`, the first term is at least `4/9` and the second at most `3/49`, so

`a'(lambda) >= 169/441 >0`.                                      (5.6)

Hence `lambda a(lambda)` is increasing on `[1,2)`.

On the small tail, `p(1-p)` increases on `(0,1/2]`.

On the large tail,

`d/dp [p(1-p)/(4-p)^2]`
` = (7p-4)/(p-4)^3 <=0`

for `p>=4/7`. Thus the worst point of each fixed rectangle is its largest `lambda` and the tail endpoint closest to the middle.

## 6. Concrete gain I: widen the `lambda=19/10` tails

### Small-p side

At `p=1/8`,

`rho=7/64`.

At `lambda=19/10`, exact arithmetic gives

`4-2 lambda a(lambda) rho = 1481/6816 >0`.

Therefore, throughout

`0<p<=1/8`, `1<=lambda<=19/10`,

`BOX: -ell'_lambda >= 37025/4091304`
`                    = 0.00904968... >0`.                         (6.1)

### Large-p side

At `p=9/10`,

`rho=108/961`.

At `lambda=19/10`,

`4-2 lambda a(lambda) rho = 54092/477617 >0`.

Therefore, throughout

`9/10<=p<1`, `1<=lambda<=19/10`,

`BOX: -ell'_lambda >= 5409200/1146758417`
`                    = 0.00471694... >0`.                         (6.2)

He--Wang--Xiang covers the lower parent-bias interval past `lambda=1`, so (6.1)--(6.2) combine with the published theorem to give strict decrease on the entire

`0<=lambda<=19/10`

for

`0<p<=1/8` or `9/10<=p<1`.

This strictly widens the predecessor's same-endpoint tails

`p<=1/30` or `p>=35/36`.

In child-bias notation, the combined conclusion is

`v'(beta)>0` for every `beta>=10/19`

on the widened tail families.

## 7. Concrete gain II: push the old rare tails to `lambda=1.966`

Take

`L=983/500`.

### Small predecessor tail `p<=1/30`

At `p=1/30` the exact derivative numerator is

`10669196969/27362435850 >0`,

hence on

`0<p<=1/30`, `1<=lambda<=983/500`,

`BOX: -ell'_lambda >=`
`53345984845000/3373946495184213`
`=0.0158111... >0`.                                               (7.1)

### Large predecessor tail `p>=35/36`

For `p>=4/7`, criterion (5.4) is equivalently

`(4-p)^2 - 6 lambda a(lambda) p(1-p) >0`.                         (7.2)

At the worst rectangle corner `p=35/36`, `lambda=983/500`, the exact gap is

`2373902221/26267938416 >0`.

Thus throughout

`35/36<=p<1`, `1<=lambda<=983/500`,

`BOX: -ell'_lambda >=`
`2373902221000000/1484661418862356839`
`=0.00159895... >0`.                                              (7.3)

For orientation only, the exact same large-tail criterion is already negative at

`p=35/36`, `lambda=1967/1000`,

with gap

`-4489281919/22648172976`.

So the certified threshold from this particular inequality lies in

`(1.966,1.967)`

at `p=35/36`. I do not claim that this is the true speed-monotonicity threshold.

Combining (7.1), (7.3) with the published low-bias theorem gives strict decrease on

`0<=lambda<=983/500`

for the predecessor's two rare-tail offspring classes. Equivalently,

`v'(beta)>0` for every `beta>=500/983`.

## 8. Separate attempted cross-2 route: an electrical escape lower bound

The predecessor identified the singular factor at `lambda=2` as the next obstruction. I therefore also executed a genuinely different electrical/regeneration-style attack rather than only polishing the old envelopes.

Normalize the reversible network at a vertex `x` so that the edge to its parent has conductance `lambda`, edges to children have conductance `1`, and an edge from generation `n-1` to generation `n` below `x` has conductance `lambda^{-(n-1)}`.

Let `R` be the effective resistance from `x` through descendants to infinity. Then

`B=1/(1+lambda R)`.                                               (8.1)

Use the deterministic equal-split unit flow: at every vertex with `k` children, split incoming current equally among the `k` child edges. If

`A_n=sum_{|v|=n} theta(v)^2`,

then for

`alpha=E[1/nu]`

the branching property gives

`E A_n = alpha^n`.                                                (8.2)

The flow energy is

`E_flow=sum_{n>=1} lambda^(n-1) A_n`.

Hence if `lambda alpha<1`,

`E E_flow = alpha/(1-lambda alpha)`.                              (8.3)

By Thomson,

`R<=E_flow`.

Since `x -> 1/(1+lambda x)` is convex,

`E B`
` >= E[1/(1+lambda E_flow)]`
` >= 1/(1+lambda E E_flow)`
` = 1-lambda alpha`.                                              (8.4)

For the `{2,3}` law,

`alpha=(1-p)/2+p/3=(3-p)/6`.

Thus (8.4) remains nontrivial all the way to

`lambda < 6/(3-p)`,

which is **strictly beyond 2 for every p>0** and tends to `3` as `p->1`.

This is a real escape-probability gain across the old `lambda=2` barrier, but it does **not** yet prove speed monotonicity there. The missing step is derivative control: differentiating the lower bound (8.4) is invalid, and the speed derivative needs control of the bias response of effective resistance / regeneration occupation, not only its value.

Therefore no `lambda>2` monotonicity claim is made. The next mathematically distinct route is to combine the electrical unit-flow comparison with a sensitivity identity for effective resistance (or regeneration occupation) that charges depth/defect energy without reverting to the global minimum-degree factor `1/(2-lambda)`.

## 9. Mechanism gain versus parent gain

### Demonstrated parent-problem gain

- At `lambda=1.9`, the proved tails enlarge from
  `p<=1/30 or p>=35/36`
  to
  `p<=1/8 or p>=9/10`.
- On the predecessor's original rare tails, the proved endpoint moves from
  `1.9`
  to
  `1.966`.

The universal no-leaf conjecture remains OPEN.

### Demonstrated mechanism gain

The new coupling proves a **two-sided, environment-independent ratio compression**

`3/4 <= c_3/c_2 <= 1`.

It converts the difficult measure-change factor into the exact scalar tail budget (5.3), rather than paying the predecessor's independent regular-tree envelopes for `c_2` and `c_3`, and rather than paying P01's generic support-width covariance.

The separate equal-split electrical flow additionally proves an annealed escape lower bound beyond `lambda=2`, but the derivative transfer is still unresolved and is not counted as source-level monotonicity progress.

## 10. Exact checker

After obtaining the symbolic proof, I executed an exact `fractions.Fraction` checker:

- `2026-09-20T01-41-00Z__branch-addition-ratio-check.py`
- `2026-09-20T01-41-00Z__branch-addition-ratio-check.out`

The archived output ends

`ALL_EXACT_CHECKS_PASS`.

The checker verifies rational endpoint arithmetic and margins. The probability argument is written above; the checker is not substituted for it.

## 11. Residual obstruction and next attack

The new ratio lemma materially weakens the `lambda<2` loss, but (3.4) still contains the predecessor's pointwise binary-branch derivative estimate and therefore still becomes singular as `lambda upward 2`.

The electrical-flow calculation shows that the **escape probability itself** has useful annealed control well beyond `2`; therefore the remaining obstruction is now narrower:

> obtain a sensitivity/occupation estimate for `-dB/dlambda` or the effective resistance that is weighted by actual current/regeneration occupation, so rare degree-2 stretches are charged by their frequency rather than by the global minimum degree.

That is the next attack. No audit or unavailable peer is awaited.

## 12. Ledger delta

```yaml
ledger_delta:
  worker: NM13-05
  live20_parent: T06
  source_id: P0066
  status_before: OPEN
  status_after: OPEN
  bias_convention: "parent bias lambda; child bias beta=1/lambda"
  offspring_family: "P(nu=2)=1-p, P(nu=3)=p, no leaves"
  parent_scope_before:
    all_mixture: "strict decrease through lambda=1847/1000 (latest all-p repo theorem)"
    nm05_rare_tails: "p<=1/30 or p>=35/36 through lambda=19/10"
  parent_scope_after:
    widened_19_10: "p<=1/8 or p>=9/10 through lambda=19/10"
    deeper_old_tails: "p<=1/30 or p>=35/36 through lambda=983/500"
  child_bias_after:
    widened_19_10: "v'(beta)>0 for beta>=10/19 on p<=1/8 or p>=9/10"
    deeper_old_tails: "v'(beta)>0 for beta>=500/983 on p<=1/30 or p>=35/36"
  mechanism_gain: "branch-addition coupling proves 3/4<=c3/c2<=1 and gives exact tail mixture budget rho(p)"
  small_tail_margin_at_19_10: "37025/4091304"
  large_tail_margin_at_19_10: "5409200/1146758417"
  small_old_tail_margin_at_983_500: "53345984845000/3373946495184213"
  large_old_tail_margin_at_983_500: "2373902221000000/1484661418862356839"
  secondary_mechanism: "equal-split electrical flow proves E B >= 1-lambda E(1/nu) when lambda E(1/nu)<1, crossing lambda=2 at value level but not derivative level"
  simulation_used_as_proof: false
  theorem_label: "RESTRICTED THEOREM CANDIDATE / PARTIAL parent"
  novelty: UNVERIFIED
  residual_obstruction: "need occupation/effective-resistance sensitivity control to cross lambda=2 in the derivative sign"
  next_attack: "differentiate/compare effective resistance or regeneration occupation under the equal-split-flow domination, preserving rarity weights"
```

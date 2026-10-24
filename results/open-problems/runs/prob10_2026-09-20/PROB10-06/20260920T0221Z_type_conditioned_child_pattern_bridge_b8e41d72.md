Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — requested GPT-6 maximum is prompt-only in this runtime, and I do not claim otherwise. SOURCE-WIDE STATUS: OPEN -> OPEN. RESTRICTED-FAMILY MOVEMENT: for every `P(nu=2)=1-p, P(nu=3)=p`, `0<=p<=1`, the rigorously covered parent-bias endpoint moves from the previous strongest analytic endpoint in `(1.84734,1.84735)` to the exact endpoint `1851/1000=1.851`; on the new strip `1847/1000<=lambda<=1851/1000`, `-ell'_lambda >= 3897500/46570225779 > 0`. Three materially different attacks: (A) condition the escape/log-derivative recursion on each child's offspring type and enumerate child-type counts — SUCCESS; (B) sharpen only the static branch-addition ratio `c_3/c_2` — structurally insufficient for the all-mixture endpoint because the tilted coordinate still spans `(0,1)` as `p` varies; (C) finite-depth scalar contraction — exactly blocked for central mixtures because at `lambda=1851/1000` the first-moment contraction requires `p<284990661/1395612661<0.205`.**

# PROB10-06 — bounded substantive iteration: type-conditioned child-pattern escape envelopes

Status: **PARTIAL / OPEN parent**. This report proves a stronger restricted-family theorem for the no-leaf two-point offspring family `{2,3}`. It does **not** settle the source-wide Lyons–Pemantle–Peres conjecture, and it has not received an independent other-track audit. External novelty is **UNVERIFIED**; the literature check below is bounded negative evidence, not a priority certificate.

## 1. Controlling instruction, handoff, admission, and consumed updates

Controlling instruction: `operations/PROB10_2026-09-20.md` on current `master`. It assigns native slot R02 to PROB10-06 and requires a complementary, nonduplicating route on the original no-leaf Galton–Watson speed-monotonicity problem.

The required immutable handoff of R02's preceding Randomstrasse/I0095 target already exists and remains untouched:

- `runs/R02/20260920T0005Z_owner_refocus_handoff_I0095_to_PROB10-06_4d8c2a71.md`, creation commit `0439a90108047760ebd8d94ffd7d5b76463666da`.

All historical `artifacts/R02/` files remain preserved. No I0095 result is relabelled as biased-walk progress.

Intake `P0066` is already marked `attempted_un`. The old attempt observed that the local radial drift `(k-lambda)/(k+lambda)` decreases at fixed offspring number but did not control the bias-dependent environment seen from the walker. There is no canonical `operations/claims/P0066.md` on current master. The owner directive nevertheless assigns R02 this delimited complementary route; no peer claim is overwritten.

The previous own report is

- `runs/prob10_2026-09-20/PROB10-06/20260920T0132Z_escape_elasticity_cone_bridge_7d4a2c91.md`.

It proved, for every `{2,3}` mixture, strict decrease through a unique analytic threshold in `(1.84734,1.84735)`, with a clean exact theorem through `lambda=1847/1000`, by a pathwise logarithmic escape-derivative cone.

Relevant neighboring updates consumed before the present proof:

1. `proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T01-41-00Z__branch-addition-ratio-coupling.md`: proves `3/4<=c_3/c_2<=1`, widens rare-tail `{2,3}` rectangles through `lambda=19/10`, and pushes the predecessor rare tails to `lambda=983/500`. I do not claim that branch-addition lemma.
2. `proofnet24/P01-progress-speed/artifacts/2026-09-20/2026-09-20T02-02-20Z__degree-secant-covariance-idea.md` at commit `747295be3e0c2f1c9190a3ff53b5d9640b9c0417`, its checker at `947d5fb8af3682ed357a02e23b76208e04505f95`, and output at `17d54221b1b6aa1abdffcd55838f7630f92c3704`: a complementary conditional-**current-degree** secant/covariance route proving broad bounded-support rectangles and a nonadjacent `{2,13}` result. The present route instead conditions the generic child escape variables *inside* the adjacent `{2,3}` Aidekon derivative formula on each child's own offspring type and enumerates 3- and 4-child type counts.
3. `probability_campaigns/progress_first_2026-09-20/P03/analytic/2026-09-20T0104Z__adjacent-two-point-weight-optimization.md`: the inherited exact tilted-coordinate reduction for adjacent two-point offspring laws.
4. `probability_campaigns/progress_first_2026-09-20/P03/coupling/2026-09-20T010909Z__sharp-regeneration-bound-and-score-response.md`: the complementary regeneration route and its remaining conditioned second-backstep-moment debt.
5. Current `POSTED.md`: no posted P0066 source-wide resolution; restricted results do not close the parent problem.

The required idea-before-code note was written first:

- `artifacts/prob10_2026-09-20/PROB10-06/20260920T0218Z_type_conditioned_escape_rectangle_idea.md`, commit `0f0b116debb4b11369ccb91212765aedb49ae229`.

The exact checker and executed output are:

- `artifacts/prob10_2026-09-20/PROB10-06/20260920T0226Z_type_conditioned_escape_rectangle_check.py`, commit `868dbb99bc03008528a1d8549cc7a6e8141f4b6c`;
- `artifacts/prob10_2026-09-20/PROB10-06/20260920T0226Z_type_conditioned_escape_rectangle_check.out`, commit `5efba4da8f75c59b26aa58b4eeff6f188b8f1dda`.

The output ends `ALL_EXACT_CHECKS_PASS`.

## 2. Source statement and convention

Let `nu` be the Galton–Watson offspring variable. The source conjecture is for a supercritical Galton–Watson tree **without leaves**,

`P(nu=0)=0`, `m=E nu>1`,

with the usual finite-mean setup.

In the original child-bias convention, at a non-root vertex with `k` children,

`P(parent)=1/(1+beta k)`,
`P(each fixed child)=beta/(1+beta k)`.

Thus larger `beta` increases drift **away** from the root. The transient interval is `beta>1/m`, and Lyons--Pemantle--Peres conjectured that the limiting speed `v(beta)` is increasing throughout `(1/m,infinity)`.

This report uses the reciprocal parent-bias convention

`lambda=1/beta`,

so

`P(parent)=lambda/(lambda+k)`,
`P(each fixed child)=1/(lambda+k)`.

Larger `lambda` pushes **toward** the root. Therefore, with `ell_lambda=v(1/lambda)`, the conjectural direction is

`ell'_lambda<=0` on `0<=lambda<m`.

No leaves are introduced anywhere below.

Primary literature baseline refreshed this run:

- Ben Arous--Fribergh--Sidoravicius, arXiv:1111.5865, submitted 24 November 2011, prove high-child-bias monotonicity; the arXiv abstract states the historical threshold `beta>=717`.
- He--Wang--Xiang, arXiv:1610.08151, later *Journal of Applied Probability* 62 (2025), prove strict parent-bias decrease for

  `0<=lambda<=m_1/(1+sqrt(1-1/m_1))`

  when the minimum offspring `m_1>=2`.
- Aidekon's exact speed representation is the analytic starting point.

A bounded search through 20 September 2026 found the 2025 He--Wang--Xiang publication and a 2026 regular-tree paper, but no source-wide resolution and no checked theorem matching the all-mixture `{2,3}` child-pattern envelope below. That statement is deliberately only bounded negative evidence; novelty remains `UNVERIFIED`.

## 3. Source metric and auxiliary metric

### Source-wide metric

Before: **OPEN**.  
After: **OPEN**.

The universal source conjecture for all no-leaf supercritical offspring laws and the full transient bias interval is not settled.

### Restricted-family mechanism metric

Freeze

`P(nu=2)=1-p`, `P(nu=3)=p`, `0<=p<=1`.

Previous strongest all-mixture analytic endpoint: a root in

`(1.84734,1.84735)`.

Previous clean rational endpoint: `1847/1000=1.847`.

New exact endpoint:

`1851/1000=1.851`.

Thus the clean rational endpoint advances by exactly

`1/250=0.004`,

and even relative to the stronger previous analytic root the advance is strictly more than

`1.851-1.84735=0.00365=73/20000`.

The new strip has the certified uniform derivative margin

`-ell'_lambda >= 3897500/46570225779`
`                 = 0.0000836908117752... >0`.                  (3.1)

## 4. Exact speed reduction for the `{2,3}` family

Fix `1<=lambda<2`. Let `B` denote the quenched probability, from a vertex, of escaping to infinity before hitting its parent, and put

`U=-dB/dlambda`, `q=U/B`.

For conditional current offspring `k`, let `B_0,...,B_k` be iid copies of the generic `B`, with corresponding `U_i`, and set

`S_k=sum_{i=0}^k B_i`,
`D_k=lambda-1+S_k`,

`c_k=E[(1/(k+1))*S_k/D_k]`,

`h_k=E[(1/(k+1))*sum_i (B_i+(lambda-1)U_i)/D_k^2]`.

Then `c_k'=-h_k`. Put

`C=(1-p)c_2+p c_3`,
`theta=p c_3/C`,
`M=2+theta`.

Aidekon's symmetrized speed formula becomes

`ell_lambda=(M-lambda)/(M+lambda)`,                              (4.1)

and therefore

`ell'_lambda=2(lambda M'-M)/(M+lambda)^2`.                       (4.2)

The two-support cancellation gives

`theta'=theta(1-theta) Delta`,

where

`Delta:=h_2/c_2-h_3/c_3`.                                       (4.3)

Consequently it is enough to prove a uniform upper bound on `lambda Delta` strictly below

`K_2=min_{0<t<1} (2+t)/(t(1-t)) = 5+2 sqrt(6)`.                 (4.4)

The present run proves the rationally stronger-to-check statement

`lambda Delta < 1979/200 = 9.895`                                (4.5)

throughout the new strip.

## 5. Escape bounds conditional on the child's own offspring type

Write

`a=lambda-1`.

The exact escape recursion is

`B=S/(lambda+S)`,                                                 (5.1)

where `S` is the sum of the escape probabilities in the child subtrees.

For the `{2,3}` family, regular-tree comparison gives the global pathwise bracket

`b_2:=(2-lambda)/2 <= B <= u_3:=(3-lambda)/3`.                  (5.2)

Condition once more on the present vertex's own offspring number.

### Type 2

If `nu=2`, then `2b_2<=S<=2u_3`. Inserting these endpoints in (5.1), which is increasing in `S`, gives

`b_2 <= B <= u_2:=2(3-lambda)/(lambda+6)`.                       (5.3)

### Type 3

If `nu=3`, then `3b_2<=S<=3u_3`, hence

`b_3:=3(2-lambda)/(6-lambda) <= B <= u_3`.                       (5.4)

These type-conditioned intervals are strictly narrower than the global interval in the interior.

## 6. Type-conditioned logarithmic derivative bounds

Differentiating (5.1) yields the exact logarithmic recursion

`q=[1+lambda (sum_j B_j q_j)/(sum_j B_j)]/[lambda+sum_j B_j]`.   (6.1)

On `1<=lambda<2`, the established upper escape-elasticity estimate of He--Wang--Xiang and the lower cone proved in the preceding R02 report give

`1/(3-lambda) <= q <= 1/(2-lambda)`.                             (6.2)

The lower inequality can also be read directly from (6.1): using `B_j<=u_3` gives `lambda+sum B_j<=3`; if all descendants satisfy `q_j>=m`, then `q>=(1+lambda m)/3`, and iteration from `m=0` converges to `1/(3-lambda)`. The upper inequality is the corresponding established minimum-degree derivative bound; on compact subintervals of `[1,2)` it also follows by applying the finite-depth recursion with its boundary derivative zero and passing to the limiting escape derivative.

Now condition on the present vertex type.

For `nu=2`, (5.2) and (6.2) in (6.1) give

`Q_2^-:=9/[(3-lambda)(lambda+6)] <= q <= Q_2^+:=1/(2-lambda)`.   (6.3)

Indeed, for the lower bound use numerator at least `1+lambda/(3-lambda)` and denominator at most `lambda+2u_3=(lambda+6)/3`; for the upper bound use numerator at most `1+lambda/(2-lambda)` and denominator at least `lambda+2b_2=2`.

For `nu=3`, similarly,

`Q_3^-:=1/(3-lambda) <= q <= Q_3^+:=4/[(2-lambda)(6-lambda)]`.    (6.4)

Here the upper denominator is bounded below by `lambda+3b_2=(6-lambda)/2`, while the lower denominator is bounded above by `lambda+3u_3=3`.

Throughout the new strip,

`Q_2^+>Q_3^+`, `Q_2^->Q_3^-`.                                   (6.5)

That strict ordering is what makes child-type information useful.

## 7. Child-pattern envelopes for `h_k/c_k`

For either `k=2` or `k=3`, put

`n=k+1`, `S=sum_{i=1}^n B_i`, `D=a+S`,
`Y=S/D`.

The pointwise ratio of the derivative integrand to the `c_k` integrand is

`R=[1+a(sum_i B_i q_i/S)]/(a+S)`.                               (7.1)

Condition on the event that exactly `m` of the `n` generic child roots have offspring type 3. Let

`s^-_{n,m}=(n-m)b_2+m b_3`,
`s^+_{n,m}=(n-m)u_2+m u_3`,                                     (7.2)

and

`y^-_{n,m}=s^-_{n,m}/(a+s^-_{n,m})`,
`y^+_{n,m}=s^+_{n,m}/(a+s^+_{n,m})`.                            (7.3)

Then, with

`x_{n,m}:=E[Y | M=m]`,

we have

`y^-_{n,m}<=x_{n,m}<=y^+_{n,m}`.                                (7.4)

### Upper pattern factor

Because `Q_2^+>Q_3^+`, a weighted average of the two typewise upper q-bounds is maximized by maximizing the total B-weight on type 2 and minimizing it on type 3. Hence

`sum_i B_i q_i/S`
` <= Qbar^+_{n,m}`
` :=[(n-m)u_2 Q_2^+ + m b_3 Q_3^+]/[(n-m)u_2+m b_3]`.           (7.5)

Also `S>=s^-_{n,m}`. Therefore

`R<=r^+_{n,m}:=[1+a Qbar^+_{n,m}]/[a+s^-_{n,m}]`.               (7.6)

For `n=3`, since the type count is binomial with weights

`pi_{3,m}=binom(3,m)p^m(1-p)^(3-m)`,

we obtain

`h_2/c_2`
` <= [sum_{m=0}^3 pi_{3,m} x_{3,m} r^+_{3,m}]`
`    /[sum_{m=0}^3 pi_{3,m} x_{3,m}]`.                          (7.7)

### Lower pattern factor

Because `Q_2^->Q_3^-`, the same weighted average is minimized by minimizing type-2 B-weight and maximizing type-3 B-weight:

`sum_i B_i q_i/S`
` >= Qbar^-_{n,m}`
` :=[(n-m)b_2 Q_2^- + m u_3 Q_3^-]/[(n-m)b_2+m u_3]`.           (7.8)

Since `S<=s^+_{n,m}`,

`R>=r^-_{n,m}:=[1+a Qbar^-_{n,m}]/[a+s^+_{n,m}]`.               (7.9)

For `n=4`,

`h_3/c_3`
` >= [sum_{m=0}^4 pi_{4,m} x_{4,m} r^-_{4,m}]`
`    /[sum_{m=0}^4 pi_{4,m} x_{4,m}]`.                          (7.10)

Everything through this point is analytic and pathwise; there is no simulation.

## 8. Freeze the narrow lambda strip by exact monotonicity

Set

`L_0=1847/1000`, `L_1=1851/1000`.                               (8.1)

The checker symbolically differentiates every rational endpoint in Sections 7 and certifies on `[L_0,L_1]` that

- every `y^-_{n,m}` is decreasing in `lambda`;
- every `y^+_{n,m}` is decreasing in `lambda`;
- every `r^+_{3,m}` is increasing in `lambda`;
- every `r^-_{4,m}` is increasing in `lambda`.

There are 27 such monotonicity certificates, and all pass exactly.

Therefore, uniformly on the strip,

`y^-_{n,m}(L_1) <= x_{n,m} <= y^+_{n,m}(L_0)`,                 (8.2)

while it is valid in (7.7) to replace `r^+_{3,m}` by `r^+_{3,m}(L_1)` and in (7.10) to replace `r^-_{4,m}` by `r^-_{4,m}(L_0)`.

For fixed `p`, each side is a ratio of two positive affine forms in the independent box variables `x_{n,m}`. Holding all but one coordinate fixed, its derivative with respect to the remaining coordinate has constant sign. Hence its extrema over the product box occur at vertices. Thus it is enough to consider

`2^4=16` upper vertices and `2^5=32` lower vertices.             (8.3)

## 9. Exact all-p finite core: 512 rational-polynomial inequalities

For each upper box vertex `epsilon` let `U_epsilon(p)` denote the resulting right side of (7.7), and for each lower box vertex `eta` let `L_eta(p)` denote the resulting right side of (7.10).

The required uniform statement is implied by the 512 inequalities

`L_1 [U_epsilon(p)-L_eta(p)] < 1979/200`                         (9.1)

for every `p in [0,1]`.

After multiplying by the positive denominators, each (9.1) becomes positivity of a rational polynomial of degree at most seven. The archived exact checker proves all 512 by exact Bernstein-basis subdivision of `[0,1]`; no floating-point sign decision is used. The maximum subdivision depth needed is 4. The checker reports the worst box-vertex pair `(8,15)` and a strictly positive smallest terminal Bernstein coefficient, approximately

`0.00021301174089605537`.

Therefore

`lambda Delta < R_0:=1979/200`                                  (9.2)

for all

`0<p<1`, `L_0<=lambda<=L_1`.

The deterministic endpoint mixtures `p=0,1` have their standard regular-tree speed formula and are strictly decreasing directly; equivalently they follow by continuity from the same finite-core inequality.

Finally,

`(R_0-5)^2 = 958441/40000 < 24`,                                (9.3)

so

`R_0 < 5+2sqrt(6)=K_2`.                                         (9.4)

This closes the strip.

## 10. Quantitative derivative sign on the new strip

Using (4.2), (4.3), and (9.2),

`lambda M'-M`
` <= R_0 theta(1-theta)-(2+theta)`
` = -f(theta)`,                                                   (10.1)

where

`f(theta)=2+theta-R_0 theta(1-theta)`.

Its exact minimum on `[0,1]` is

`f_min=2-(R_0-1)^2/(4R_0)`
`     =1559/1583200 >0`.                                         (10.2)

Since `M<=3` and `lambda<=L_1`, equations (4.2) and (10.2) imply

`-ell'_lambda`
` >= 2 f_min/(3+L_1)^2`
` = 3897500/46570225779`
` = 0.0000836908117752... >0`.                                  (10.3)

This is the requested certified sign lower bound.

Combining the present strip with the previous R02 theorem through `L_0`, and with the published minimum-degree result below the overlapping lower endpoint, yields:

### Theorem 10.1 — all `{2,3}` mixtures through parent bias 1.851

For every

`P(nu=2)=1-p`, `P(nu=3)=p`, `0<=p<=1`,

on a Galton--Watson tree without leaves, the limiting speed in parent-bias convention is strictly decreasing for

`0<=lambda<=1851/1000`.                                         (10.4)

Equivalently, in child-bias convention `beta=1/lambda`, speed is strictly increasing throughout

`beta>=1000/1851`                                                 (10.5)

within this offspring family.

This is a restricted-family theorem only. It does not establish monotonicity all the way down to the source transience threshold `beta>1/(2+p)` (equivalently all the way up to `lambda<2+p`).

## 11. Two different routes tested and why they do not replace the main mechanism

### Route B — sharpen only `c_3/c_2`

NM13-05 already proves `3/4<=c_3/c_2<=1`. Positive lower escape can narrow that ratio further on a fixed bias strip. However, for any fixed finite interval `0<L<=c_3/c_2<=U<infinity`, the tilted coordinate

`theta= p(c_3/c_2)/(1-p+p(c_3/c_2))`

still runs continuously from 0 to 1 as `p` runs from 0 to 1. Hence a `p`-independent bound on `c_3/c_2` alone cannot improve the **all-mixture** worst-case threshold in (4.4). It can improve rare-tail/fixed-p rectangles, which is exactly where the NM13 route is effective, but not the present all-p bottleneck.

### Route C — finite-depth scalar contraction

The scalar escape map has degree-2 local contraction factor at most

`rho_2=lambda/2`,                                                 (11.1)

but for degree 3 the corresponding global derivative factor is

`rho_3=12lambda/(6-lambda)^2`.                                   (11.2)

At `lambda=L_1`, exact arithmetic gives

`rho_2=1851/2000=0.9255`,

`rho_3=2468000/1912689=1.2903300013...`.                         (11.3)

A naive first-moment mixture contraction `(1-p)rho_2+p rho_3<1` therefore requires

`p < p_*`
`  =284990661/1395612661`
`  =0.2042046973...`.                                            (11.4)

So scalar truncation cannot control the central mixture regime needed for an all-p bridge. A viable truncation route would have to contract a genuinely joint `(B,q)` state or use a nontrivial weighted metric. This is an exact obstruction to the naive method, not evidence against such a stronger joint contraction.

## 12. Actual checks

The exact checker performs four finite tasks:

1. certifies all 27 lambda-monotonicity rational inequalities on `[1847/1000,1851/1000]`;
2. certifies all `16*32=512` box-vertex inequalities (9.1) for every `p in [0,1]` using exact rational Bernstein subdivision;
3. checks `1979/200<5+2sqrt(6)` by the exact square comparison (9.3), and computes the exact speed-derivative margin (10.3);
4. computes the scalar-contraction obstruction (11.4).

Archived output ends:

`ALL_EXACT_CHECKS_PASS`.

These are **self-checks**, not independent audits.

## 13. Remaining full-scope gap

The parent conjecture remains far from closed in two distinct senses.

First, even for the `{2,3}` family this report reaches only `lambda=1.851`, while the source asks for the full transient interval

`0<=lambda<2+p`.

In particular, any route tied to the minimum-degree cone `q<=1/(2-lambda)` becomes singular as `lambda` approaches 2, while for every `p>0` the conjectured interval continues beyond 2. Crossing that minimum-degree critical scale is now the cleanest family-level obstruction.

Second, source-wide offspring laws need not be two-point or bounded by 3. P01's degree-secant work gives broad bounded-support rectangles at smaller lambda, but no current argument controls all no-leaf offspring laws through their full transient interval.

The most promising next move within this parent problem is therefore not another tiny extension of the present strip. It is to replace the minimum-degree singular upper cone by a **distribution-sensitive or type-sensitive derivative estimate that remains finite through lambda=2 for p>0**, likely by exploiting the positive chance of degree 3 along the escape-biased spine. A joint `(B,q)` transfer operator conditioned on child type is a concrete candidate.

Independent validation is also still missing. Accordingly the honest status is **PARTIAL / OPEN**, not PROVED.

## 14. Structured ledger delta

```yaml
ledger_delta:
  track: PROB10-06
  source: Lyons-Pemantle-Peres biased-walk speed monotonicity on no-leaf supercritical Galton-Watson trees
  runtime_model: GPT-5.6 Sol
  runtime_reasoning: UNVERIFIED
  source_status_before: OPEN
  source_status_after: OPEN
  source_scope_closed: false
  family: P(nu=2)=1-p, P(nu=3)=p, 0<=p<=1
  previous_all_mixture_endpoint:
    analytic_root_bracket: [1.84734, 1.84735]
    clean_rational: 1847/1000
  new_all_mixture_endpoint: 1851/1000
  clean_endpoint_delta: 1/250
  delta_over_previous_analytic_endpoint: '>73/20000'
  new_strip: [1847/1000, 1851/1000]
  certified_sign_lower_bound: 3897500/46570225779
  child_bias_equivalent_lower_endpoint: 1000/1851
  exact_checker: artifacts/prob10_2026-09-20/PROB10-06/20260920T0226Z_type_conditioned_escape_rectangle_check.py
  checker_output: artifacts/prob10_2026-09-20/PROB10-06/20260920T0226Z_type_conditioned_escape_rectangle_check.out
  checker_result: ALL_EXACT_CHECKS_PASS
  independent_audit: none
  novelty: UNVERIFIED
  next_obstruction: replace the min-degree q<=1/(2-lambda) cone by a distribution-sensitive bound that crosses lambda=2 when p>0
```

No scheduler state, cadence, notifications, email, Drive, public posting, permissions, or unrelated track files were changed in this run.
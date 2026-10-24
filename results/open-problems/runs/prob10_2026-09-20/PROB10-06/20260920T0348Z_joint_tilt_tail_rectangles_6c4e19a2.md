Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6/maximum was requested in prompt text, but no authenticated reasoning-effort telemetry or binding model selector is exposed here, so GPT-6/maximum is not claimed. SOURCE-WIDE STATUS: OPEN -> OPEN. RESTRICTED-FAMILY MOVEMENT: for `P(nu=2)=1-p, P(nu=3)=p`, the rigorously covered tail region through parent bias `lambda=19/10` expands from the inherited `p<=1/8 or p>=9/10` to `p<=31/200 or p>=41/50`; through `lambda=983/500`, it expands from `p<=1/30 or p>=35/36` to `p<=1/27 or p>=22/23`. On the new strips the certified derivative margins are respectively `-ell'_lambda >= 2/12005` and `-ell'_lambda >= 10000/6165289`. Three materially different attacks: (A) preserve the exact `p`--escape-tilt relation instead of optimizing over an independent tilted mixture coordinate — SUCCESS; (B) Laplace-transform/branch-addition covariance representation — exact identity found but blocked by a missing monotonicity bound for the transformed derivative observable; (C) near-critical expansion across `lambda=2` — blocked rigorously by the absence of a uniform `U=-B'` remainder/denominator estimate, so no cross-2 claim is made.**

# PROB10-06 — joint offspring/escape-tilt compression for the `{2,3}` family

Status: **PARTIAL / OPEN parent**. This report proves larger restricted parameter regions for one no-leaf finitely supported offspring family. It does **not** settle the full Lyons–Pemantle–Peres conjecture and has not received an independent other-track audit. External novelty is **UNVERIFIED**; the literature search is bounded negative evidence only.

## 1. Controlling instruction, continuity, ownership, and consumed updates

Controlling owner instruction: `operations/PROB10_2026-09-20.md` on `master`. It assigns native slot R02 to PROB10-06, requires preservation of the former R02 target, complementary ownership, three genuinely different attacks, idea-before-code, exact checking of a finite core, and one immutable report in this path.

The required immutable handoff of the preceding R02/Randomstrasse I0095 target already exists and is preserved:

- `runs/R02/20260920T0005Z_owner_refocus_handoff_I0095_to_PROB10-06_4d8c2a71.md`, creation commit `0439a90108047760ebd8d94ffd7d5b76463666da`.

All historical `artifacts/R02/` remain untouched.

Intake P0066 remains previously attempted (`attempted_un`). The old attempt only observed that the fixed-degree local radial drift `(k-lambda)/(k+lambda)` decreases with parent bias; it did not control the bias-dependent environment seen by the walker. There is no canonical `operations/claims/P0066.md` that this report overwrites.

The newest own report consumed is

- `runs/prob10_2026-09-20/PROB10-06/20260920T0221Z_type_conditioned_child_pattern_bridge_b8e41d72.md`, creation/readback commit `1c9515960e041d8f644d548370294b0d1601e2cd`, current blob `0d62344963e8396c35a5d2f1b255cd829d983171`.

It proved all `{2,3}` mixtures through `lambda=1851/1000` by type-conditioned escape/log-derivative envelopes.

The exact repository comparison from that commit to the pre-report master head `77f77365b39c0f06e8fdd3228ab90abe920bc119` was complete (`166` commits ahead, `0` behind, `too_large=null`). Relevant newer complementary speed work was therefore consumed rather than silently ignored:

1. `proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T02-34-00Z__rare-extra-child-nearcritical-d3.md`: a **different `{3,4}` family**, proving rare-tail monotonicity nearly to `lambda=3`. It does not contain the `{2,3}` rectangles proved here.
2. `proofnet24/P01-progress-speed/runs/2026-09-20/2026-09-20T03-08-51Z__run-report.md`: a conditional-degree secant theorem for arbitrary bounded support with minimum offspring at least `3`; again it does not duplicate this `{2,3}` tail optimization.
3. `probability_campaigns/progress_first_2026-09-20/P03/analytic/2026-09-20T0259Z__unbounded-support-mean-defect-extension.md`: an unbounded-support finite-mean extension based on escape-tilt stochastic domination. It supplies useful context but not the present joint `p`--tilt tail certificate.
4. The directly used partner result remains the previous NM13-05 report `proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T01-41-00Z__branch-addition-ratio-coupling.md`, which proved for this family `3/4 <= c_3/c_2 <= 1` and the inherited tail rectangles. I use that inequality as a dependency and do not claim it here.

The idea was written before code:

- `artifacts/prob10_2026-09-20/PROB10-06/20260920T0320Z_joint_tilt_tail_idea.md`, commit `960a2f352c6555173279ac10f43fa090e497b866`.

The exact checker and its executed output are:

- `artifacts/prob10_2026-09-20/PROB10-06/20260920T0330Z_joint_tilt_tail_check.py`, commit `f823487f5abf300afd0b8583bf97f27f60d62bbb`;
- `artifacts/prob10_2026-09-20/PROB10-06/20260920T0330Z_joint_tilt_tail_check.out`, commit `d4ecb9af949c96486ef5bbabb7419c7c5686e257`.

The output ends `ALL_EXACT_CHECKS_PASS`. This is a self-check, not an independent audit.

## 2. Exact source statement and bias convention

Let `nu` be the Galton–Watson offspring variable. The source problem is for a supercritical Galton–Watson tree **without leaves**:

`P(nu=0)=0`, `m=E nu>1`.

In the original child-bias convention of Lyons–Pemantle–Peres / Ben Arous–Fribergh–Sidoravicius, at a vertex with `k` children,

`P(parent)=1/(1+beta k)`,
`P(each fixed child)=beta/(1+beta k)`.

Thus increasing `beta` increases drift away from the root. The transient interval is `beta>1/m`, and the conjecture asks that the limiting speed `v(beta)` increase throughout `(1/m,infinity)`.

This report uses reciprocal parent bias

`lambda=1/beta`,

so

`P(parent)=lambda/(lambda+k)`,
`P(each fixed child)=1/(lambda+k)`.

Increasing `lambda` pushes toward the root. With `ell_lambda=v(1/lambda)`, the source direction is

`ell'_lambda <= 0` on `0<=lambda<m`.

No leaves are introduced.

Primary-source/current baseline refreshed this run:

- Ben Arous–Fribergh–Sidoravicius, arXiv:1111.5865 / CPAM 67 (2014), high outward-bias monotonicity; this is baseline, not novelty.
- Aïdékon, arXiv:1111.4313 / PTRF 159 (2014), exact speed representation via the environment seen from the particle.
- He–Wang–Xiang, arXiv:1610.08151, published J. Appl. Probab. 62 (2025), strict parent-bias decrease for `0<=lambda<=m_1/(1+sqrt(1-1/m_1))` when the minimum offspring `m_1>=2`.
- Bowditch–Tokushige, arXiv:1906.07913, differentiability in the ballistic regime.

A bounded search through 20 September 2026 found the 2025 publication and related progeny-distribution/differentiability papers, but no source-wide resolution and no checked theorem identical to the two new rectangles below. That is not a priority certificate.

## 3. Metrics: source before/after and auxiliary delta

### Source-wide metric

Before: **OPEN**.  
After: **OPEN**.

No theorem for all no-leaf offspring laws on the full transient interval is claimed.

### Restricted source-region metric

Freeze

`P(nu=2)=1-p`, `P(nu=3)=p`, `0<=p<=1`.

At endpoint `lambda=19/10`:

- inherited certified tails: `p<=1/8` or `p>=9/10`;
- new certified tails: `p<=31/200` or `p>=41/50`.

Thus the small-p boundary advances by

`31/200-1/8 = 3/100`,

and the large-p boundary moves toward the center by

`9/10-41/50 = 2/25`.

At endpoint `lambda=983/500=1.966`:

- inherited certified tails: `p<=1/30` or `p>=35/36`;
- new certified tails: `p<=1/27` or `p>=22/23`.

The corresponding boundary gains are

`1/27-1/30 = 1/270`,

and

`35/36-22/23 = 13/828`.

### Auxiliary mechanism delta

On the first new strip `1851/1000<=lambda<=19/10`, the exact certificate proves

`lambda g(theta) Delta <= 999/1000`,

for the new first-strip tails, yielding

`-ell'_lambda >= 2/12005 >0`.

On the second new strip `19/10<=lambda<=983/500`, it proves

`lambda g(theta) Delta <= 99/100`,

for the second-strip tails, yielding

`-ell'_lambda >= 10000/6165289 >0`.

Here `g(theta)=theta(1-theta)/(2+theta)` and `Delta=h_2/c_2-h_3/c_3`, defined precisely below.

## 4. Exact two-point speed derivative reduction

Fix `1<=lambda<2`. Let `B` be the quenched escape probability from a vertex before hitting its parent and `U=-dB/dlambda`.

For conditional current offspring `k`, let `B_0,...,B_k` be iid copies of `B`, with corresponding `U_i`, and put

`S_k=sum_{i=0}^k B_i`,
`D_k=lambda-1+S_k`,

`c_k=E[(1/(k+1))*S_k/D_k]`,

`h_k=E[(1/(k+1))*sum_i(B_i+(lambda-1)U_i)/D_k^2]`.

Direct differentiation gives

`c_k'=-h_k`.                                                     (4.1)

For the `{2,3}` offspring law set

`C=(1-p)c_2+p c_3`,
`theta=p c_3/C`.                                                  (4.2)

The escape-tilted effective degree is exactly

`M=2+theta`,                                                      (4.3)

and Aïdékon's symmetrized formula gives

`ell_lambda=(M-lambda)/(M+lambda)`.                               (4.4)

Differentiating,

`ell'_lambda=2(lambda M'-M)/(M+lambda)^2`.                        (4.5)

Moreover

`theta/(1-theta)=[p/(1-p)] [c_3/c_2]`.

Taking a logarithmic derivative and using (4.1),

`theta'=theta(1-theta) Delta`,                                   (4.6)

where

`Delta:=h_2/c_2-h_3/c_3`.                                       (4.7)

Combining (4.3)--(4.7),

`-ell'_lambda`
` = 2(2+theta)[1-lambda g(theta) Delta]/(2+theta+lambda)^2`,       (4.8)

with

`g(theta):=theta(1-theta)/(2+theta)`.                             (4.9)

Thus it suffices to keep `lambda g(theta)Delta` strictly below one.

## 5. New mechanism: do not decouple the tilted mixture coordinate from p

The previous all-mixture proof bounded (4.9) by its global maximum over `0<theta<1`. That is appropriate for all `p`, but it throws away exactly the information available in the tails.

The partner branch-addition theorem gives

`3/4 <= t:=c_3/c_2 <= 1`.                                       (5.1)

By (4.2),

`theta=p t/(1-p+p t)`.                                           (5.2)

This is increasing in `t`, so

`3p/(4-p) <= theta <= p`.                                        (5.3)

Differentiate (4.9):

`g'(theta)=[2-4theta-theta^2]/(2+theta)^2`.                       (5.4)

Hence the unique maximizer is

`theta_*=sqrt(6)-2`.                                              (5.5)

### Small-p compression

All small-p rectangles below have `p<theta_*`. By (5.3), `theta<=p<theta_*`, and (5.4) shows `g` is increasing there. Therefore

`g(theta) <= g(p)=p(1-p)/(2+p)`.                                 (5.6)

### Large-p compression

For `p>=41/50`, already

`3p/(4-p) > theta_*`.

Thus the whole interval in (5.3) lies to the right of the maximum of `g`; there `g` decreases. Therefore

`g(theta) <= g(3p/(4-p))`
`          = 12p(1-p)/[(4-p)(8+p)]`.                            (5.7)

The same is automatically true on the smaller large-p tail `p>=22/23`.

Equations (5.6)--(5.7) are the run's analytic advance: the dangerous effective mixture weight is coupled to the original offspring weight instead of being optimized independently.

## 6. Rigorous child-pattern envelope consumed from the preceding R02 report

For completeness, the exact finite certificate used below is restated. Put `a=lambda-1`. The preceding type-conditioned recursion proved the pathwise intervals

`b_2=(2-lambda)/2 <= B | {nu=2} <= u_2=2(3-lambda)/(lambda+6)`,

`b_3=3(2-lambda)/(6-lambda) <= B | {nu=3} <= u_3=(3-lambda)/3`,  (6.1)

and for `q=U/B`,

`q_2^- = 9/[(3-lambda)(lambda+6)] <= q | {nu=2} <= q_2^+=1/(2-lambda)`,

`q_3^- = 1/(3-lambda) <= q | {nu=3} <= q_3^+=4/[(2-lambda)(6-lambda)]`. (6.2)

For a pattern of `n` iid child-root variables containing exactly `m` type-3 roots, define

`s^-_{n,m}=(n-m)b_2+m b_3`,
`s^+_{n,m}=(n-m)u_2+m u_3`,

`y^-_{n,m}=s^-_{n,m}/(a+s^-_{n,m})`,
`y^+_{n,m}=s^+_{n,m}/(a+s^+_{n,m})`.                             (6.3)

The conditional denominator weight `x_{n,m}=E[S/(a+S) | M=m]` obeys

`y^-_{n,m} <= x_{n,m} <= y^+_{n,m}`.                             (6.4)

The pointwise logarithmic derivative ratio is

`R=[1+a(sum_i B_i q_i/S)]/(a+S)`.                                (6.5)

Using the typewise endpoints in the favorable directions gives explicit rational pattern bounds `R^+_{3,m}(lambda)` and `R^-_{4,m}(lambda)`. The checker reuses exactly the preceding formulas:

upper (`n=3`):

`Q^+=[(n-m)u_2 q_2^+ + m b_3 q_3^+]/[(n-m)u_2+m b_3]`,
`R^+=(1+a Q^+)/(a+s^-_{n,m})`;                                   (6.6)

lower (`n=4`):

`Q^-=[(n-m)b_2 q_2^- + m u_3 q_3^-]/[(n-m)b_2+m u_3]`,
`R^-=(1+a Q^-)/(a+s^+_{n,m})`.                                   (6.7)

Consequently

`h_2/c_2 <= [sum_m Bin(3,m;p) x_{3,m} R^+_{3,m}]/[sum_m Bin(3,m;p)x_{3,m}]`, (6.8)

`h_3/c_3 >= [sum_m Bin(4,m;p) x_{4,m} R^-_{4,m}]/[sum_m Bin(4,m;p)x_{4,m}]`. (6.9)

A linear-fractional function of the box variables `x_{n,m}` takes its extrema at box vertices. Therefore there are only `2^4=16` upper and `2^5=32` lower corner ratios to compare.

The new checker independently re-verifies on each new lambda strip that all `y^-` and `y^+` decrease in lambda while all relevant pattern `R` bounds increase. It therefore freezes each pattern box rigorously at the strip endpoints before performing the p-optimization. There are `27` exact lambda-monotonicity inequalities per strip.

## 7. Exact finite certificate for the first strip

Take

`L_0=1851/1000`, `L_1=19/10`.                                   (7.1)

For every upper corner write its ratio as `N_U/D_U`, and every lower corner as `N_L/D_L`; all denominators are positive. Equations (6.8)--(6.9) imply

`Delta <= N_U/D_U-N_L/D_L`                                       (7.2)

for some admissible corner pair, so it is enough to verify the desired inequality for **every** one of the `16*32` pairs.

### Small tail `0<=p<=31/200`

Using (5.6), a sufficient condition for `lambda g(theta)Delta <= R` is

`R(2+p)D_U D_L`
` - L_1 p(1-p)(N_U D_L-N_L D_U) >0.                              (7.3)

The checker proves (7.3) with

`R=999/1000`                                                      (7.4)

for all 512 corner pairs and all `p in [0,31/200]` by exact rational Bernstein coefficients.

### Large tail `41/50<=p<=1`

Using (5.7), a sufficient condition is

`R(4-p)(8+p)D_U D_L`
` -12 L_1 p(1-p)(N_U D_L-N_L D_U)>0.                             (7.5)

Again with `R=999/1000`, the checker proves (7.5) for all 512 corner pairs and the full interval `p in [41/50,1]`.

No subdivision was needed: all terminal Bernstein certificates were positive already at depth zero. Together with the 27 lambda-monotonicity inequalities, this is an exact finite proof of

`lambda g(theta)Delta <=999/1000`                                (7.6)

on the stated rectangles.

Substitute (7.6) into (4.8). Since `2+theta>=2` and `2+theta+lambda<=3+19/10=49/10`,

`-ell'_lambda`
` >= 4(1-999/1000)/(49/10)^2`
` = 2/12005 >0.                                                   (7.7)

The preceding own theorem already covers **all p** through `lambda=1851/1000`; therefore (7.7) patches without a gap and proves:

### Theorem 7.1

If

`P(nu=2)=1-p`, `P(nu=3)=p`,

and

`0<=p<=31/200` **or** `41/50<=p<=1`,                              (7.8)

then the parent-bias speed is strictly decreasing on

`0<=lambda<=19/10`.                                               (7.9)

On the newly added strip `1851/1000<=lambda<=19/10`, the quantitative bound (7.7) holds.

## 8. Exact finite certificate for the second strip

Now take

`L_0=19/10`, `L_1=983/500`.                                      (8.1)

Repeat the same endpoint-freezing and all-corner argument.

For

`0<=p<=1/27` or `22/23<=p<=1`,                                   (8.2)

the exact Bernstein checker verifies all 1024 small/large-tail corner inequalities with the stronger slack

`lambda g(theta)Delta <=99/100`.                                 (8.3)

Again the 27 required lambda-monotonicity inequalities pass exactly, and the maximum Bernstein subdivision depth is zero.

Equation (4.8) gives

`-ell'_lambda`
` >=4(1-99/100)/(3+983/500)^2`
` =10000/6165289 >0                                              (8.4)

throughout the second strip.

The parameter sets in (8.2) are subsets of the first-strip sets in (7.8), so Theorem 7.1 patches (8.4) to lower biases. Therefore:

### Theorem 8.1

If

`P(nu=2)=1-p`, `P(nu=3)=p`,

and

`0<=p<=1/27` **or** `22/23<=p<=1`,                               (8.5)

then the parent-bias speed is strictly decreasing on

`0<=lambda<=983/500=1.966`.                                      (8.6)

On the newly added strip `19/10<=lambda<=983/500`, the quantitative bound (8.4) holds.

This strictly enlarges the same-endpoint predecessor region `p<=1/30 or p>=35/36`.

In child-bias notation, Theorem 8.1 proves strict increase at least on the reciprocal covered interval `beta>=500/983` for these two offspring tails; the direction is reversed because `beta=1/lambda`.

## 9. The other two attacks and their exact obstruction

### Attack B: Laplace-transform branch-addition representation

Let `a=lambda-1` and define

`L(t)=E[e^{-tB}]`, `M_1(t)=E[B e^{-tB}]`, `N(t)=E[U e^{-tB}]`.

Using `1/(a+S)=int_0^infty e^{-t(a+S)}dt` and differentiating under the integral in the bounded-support regime gives, for `n>=1`,

`c_{n-1}=int_0^infty e^{-at} M_1(t)L(t)^{n-1} dt`,               (9.1)

`h_{n-1}=int_0^infty t e^{-at}[M_1(t)+aN(t)]L(t)^{n-1} dt`.      (9.2)

Thus adjoining one branch changes the normalized logarithmic derivative by tilting the same measure with the decreasing factor `L(t)`. This converts `h_2/c_2-h_3/c_3` into a covariance-type problem.

The obstruction is precise: to certify its sign or size one needs a proved monotonicity/Lipschitz relation for

`z(t)=t[1+aN(t)/M_1(t)]`                                         (9.3)

relative to `L(t)`. The current escape recursion bounds `U/B` pointwise but does not imply the needed monotonicity of `N/M_1` in `t`. No theorem is claimed from (9.1)--(9.3).

### Attack C: near-critical expansion across lambda=2

For this family `m=2+p`; formally, as `lambda` approaches `m` from below, escape probabilities vanish and the effective-degree formula suggests the regular first-order behavior `(m-lambda)/(m+lambda)`, with negative derivative.

The required rigorous bridge is missing: the available pathwise upper elasticity estimate contains `(2-lambda)^{-1}` and therefore degenerates exactly at the minimum-degree boundary `lambda=2`. A valid near-critical proof would need a distribution-sensitive bound on `U=-B'` plus a truncation/remainder estimate uniform as `lambda` crosses `2` for `p>0`. This run does not assume that estimate and makes **no claim for lambda>=2**.

This is the main remaining obstruction for turning the `{2,3}` tail theorems into a full transient-interval result for any nontrivial p-range.

## 10. Exact-check receipt

The executed checker reports:

- strip 1: `27` exact lambda-monotonicity checks, `1024` corner-tail polynomial inequalities, maximum Bernstein subdivision depth `0`, derivative margin `2/12005`;
- strip 2: `27` exact lambda-monotonicity checks, `1024` corner-tail polynomial inequalities, maximum Bernstein subdivision depth `0`, derivative margin `10000/6165289`;
- final line: `ALL_EXACT_CHECKS_PASS`.

All arithmetic in the finite certificate is symbolic/rational (`sympy.QQ` plus exact Bernstein coefficients). There is no finite-tree simulation and no floating-point sign decision.

## 11. Remaining full-scope gap and next mathematical obligation

The parent source problem remains **OPEN** for arbitrary no-leaf offspring distributions and the entire transient interval `0<=lambda<E nu`.

For the present `{2,3}` family, even the new tail certificates stop below `lambda=2`, whereas the transient interval extends to `2+p`. The sharp obstruction is not another corner enumeration; it is the singular minimum-degree derivative envelope. A genuinely new next method should therefore target one of:

1. a distribution-sensitive escape-elasticity bound replacing `(2-lambda)^{-1}` and remaining finite for `lambda>2` when `p>0`;
2. a rigorous Laplace-transform monotonicity theorem for (9.3), which would control branch addition without the minimum-degree singularity;
3. a near-critical expansion with explicit remainder/truncation control uniform in a nonzero p-window.

Repeating the present pattern-box search without replacing that singular input is not expected to cross `lambda=2`.

## 12. Structured ledger delta (own report only)

```yaml
ledger_delta:
  target: PROB10-06 / P0066 Lyons-Pemantle-Peres speed monotonicity
  source_status_before: OPEN
  source_status_after: OPEN
  offspring_family: P(nu=2)=1-p, P(nu=3)=p
  restricted_regions_before:
    lambda_1.9: "p<=1/8 or p>=9/10"
    lambda_1.966: "p<=1/30 or p>=35/36"
  restricted_regions_after:
    lambda_1.9: "p<=31/200 or p>=41/50"
    lambda_1.966: "p<=1/27 or p>=22/23"
  auxiliary_certificates:
    strip_1_product_ceiling: 999/1000
    strip_1_derivative_margin: 2/12005
    strip_2_product_ceiling: 99/100
    strip_2_derivative_margin: 10000/6165289
  finite_check: ALL_EXACT_CHECKS_PASS
  independent_audit: none
  novelty: UNVERIFIED
  remaining_gap: "replace the minimum-degree (2-lambda)^(-1) escape-elasticity singularity to cross lambda=2; then extend beyond one offspring subclass"
```

No scheduler state, email, Drive, public posting, permissions, workflows, shared roots, or peer files were modified in this iteration.

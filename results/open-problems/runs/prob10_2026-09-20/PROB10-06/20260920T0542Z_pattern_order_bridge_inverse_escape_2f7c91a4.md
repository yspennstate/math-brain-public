Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6/maximum was requested in prompt text, but no authenticated applied-model/reasoning-effort telemetry or binding selector is exposed here, so GPT-6/maximum is not claimed. SOURCE-WIDE STATUS: OPEN -> OPEN. RESTRICTED-FAMILY MOVEMENT: for `P(nu=2)=1-p, P(nu=3)=p`, all `p in [0,1]`, the rigorously certified all-mixture parent-bias endpoint moves from `1.8539` to `1.855087`, a gain of `0.001187`; on the new strip the exact uniform sign certificate is `-ell'_lambda >= 8000000/23571869777569 > 0`. Three materially different attacks: (A) child-type stochastic order plus reverse Chebyshev compression of the upper Aidekon score — SUCCESS and moves the endpoint; (B) harmonic inverse-escape recursion — SUCCESS as a new auxiliary lemma that remains finite through `lambda=2` for every `p>0`, but it does not yet control the derivative score; (C) pathwise logarithmic-derivative ordering under branch addition — REFUTED as a route by an exact admissible-envelope counterexample.**

# PROB10-06 — child-type stochastic order, an all-mixture `{2,3}` bridge, and an inverse-escape moment across the minimum-degree singularity

Status: **PARTIAL / OPEN parent.** This report proves a slightly larger all-mixture interval for one genuinely random bounded no-leaf offspring family and a separate inverse-escape moment lemma that crosses the pointwise `lambda=2` singularity. It does **not** settle the full Lyons--Pemantle--Peres conjecture. The finite certificate is a self-check, not an independent other-track audit. External novelty is **UNVERIFIED**; the literature search recorded below is bounded negative evidence only.

## 1. Controlling instruction, continuity, ownership, and consumed updates

The controlling owner instruction is `operations/PROB10_2026-09-20.md` on `master`. It assigns native R02 to PROB10-06, requires preservation of the prior R02 target, recovery of P0066 and live neighboring work, a complementary route, idea-before-persistent-checker, three materially different attacks, rigorous denominator/derivative control, exact checking of finite cores, and one immutable report under this directory.

The required immutable handoff of the preceding R02 / Randomstrasse I0095 target already exists and remains untouched:

- `runs/R02/20260920T0005Z_owner_refocus_handoff_I0095_to_PROB10-06_4d8c2a71.md`, creation commit `0439a90108047760ebd8d94ffd7d5b76463666da`.

All historical `artifacts/R02/` remain preserved.

Intake `P0066` remains marked `attempted_un` / attempted-unsolved. Its historical attempt observed only that, for fixed offspring number `k`, the local radial drift `(k-lambda)/(k+lambda)` decreases as parent bias increases; it did not control the bias-dependent environment seen from the walk. Repository search still finds no canonical `operations/claims/P0066.md` to overwrite. The current owner directive explicitly assigns this R02 route, while P01 and NM13-05 are complementary same-parent workers.

Consumed own update:

- `runs/prob10_2026-09-20/PROB10-06/20260920T0416Z_global_coupled_tilt_all_mixtures_1d7c5a90.md`, blob `c8b25c15c75a49d8c946a66149e232a9b685d3aa`.

Its strongest all-mixture theorem for the exact family treated here was strict parent-bias decrease through `lambda=18539/10000=1.8539`. The present run starts there rather than re-deriving earlier strips.

Consumed neighboring updates:

1. `proofnet24/P01-progress-speed/runs/2026-09-20/2026-09-20T05-00-49Z__run-report.md`, blob `b40364735a57b991c05c4505302d63df28361f76`. P01 now proves bounded-support low-bias regions even with minimum offspring one. Its mechanism is a pairwise-Gini covariance certificate and is complementary to the present central `{2,3}` pattern-order route.
2. `proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T04-23-44Z__parametric-defect-budget-wedge.md`, blob `3e7f47701ada687f95bac795346966675d848324`. NM13-05 proves, for adjacent `{d,d+1}` laws, the rare-endpoint wedge `p<=delta` or `1-p<=delta` through `lambda<=d-delta`. For `{2,3}` this can go arbitrarily close to 2 only when the mixture is correspondingly close to an endpoint; it does not cover all `p`.
3. Historical `probability_campaigns/progress_first_2026-09-20/P03/analytic/2026-09-20T0004Z__two-point-near-regular-extension.md` was recovered. It proves a much earlier small-`p` `{2,3}` extension through `lambda=3/2`; that old result is not claimed as new here.
4. Root `POSTED.md`, current blob `affe1b5f31545bb15be9ba2580548e9e88095e1b`, was consumed. It contains no posted source-wide P0066 closure and expressly warns that restricted results do not close their unrestricted parents.

The exact new idea was persisted before the durable checker:

- `artifacts/prob10_2026-09-20/PROB10-06/20260920T0525Z_pattern_order_inverse_moment_idea.md`, creation commit `d35c34cdcca1045f548153e1d4c44479a519a190`.

The exact checker and executed output are:

- `artifacts/prob10_2026-09-20/PROB10-06/20260920T0532Z_pattern_order_bridge_check.py`, creation commit `5c90281b4f900a88891eed35246ad65b74e5b231`;
- `artifacts/prob10_2026-09-20/PROB10-06/20260920T0532Z_pattern_order_bridge_check.out`, creation commit `43b2be6efae221ca239ecb57334b23bc4106f6d7`.

The executed output ends `ALL_EXACT_CHECKS_PASS`. This is a **self-check**.

The first pre-report master head observed after the artifacts were archived was `5cafb9ab59a514999a07bc005c98c36db24d168c`; a conflict-safe first report write then detected concurrent master movement to `bdcee5b4d1ffd0625a26021ee18d2080e2218166`, so no force push or overwrite was attempted and this retry is based on the refreshed head. Concurrent unrelated fleet commits are not treated as mathematical input unless listed above.

## 2. Exact source problem and bias convention

Let `nu` be the Galton--Watson offspring variable. The source setting is

`P(nu=0)=0`,
`m=E nu in (1,infinity)`.

Thus the tree is supercritical and has **no leaves**. No leaves are introduced anywhere in this report.

In the child-bias convention of Ben Arous--Fribergh--Sidoravicius, at a vertex with `k` children,

`P(parent)=1/(1+beta k)`,
`P(each fixed child)=beta/(1+beta k)`.

Larger `beta` pushes **away** from the root. The original conjectural transient interval is

`beta in (1/m,infinity)`,

and the conjecture asks that the limiting speed `v(beta)` be increasing there.

This track uses reciprocal parent bias

`lambda=1/beta`.

Then

`P(parent)=lambda/(lambda+k)`,
`P(each fixed child)=1/(lambda+k)`.

Larger `lambda` pushes **toward** the root. Writing

`ell_lambda=v(1/lambda)`,

the equivalent conjecture is that `ell_lambda` is nonincreasing on

`0<=lambda<m`.

For the restricted family in this report,

`P(nu=2)=1-p`, `P(nu=3)=p`, `0<=p<=1`,

we have `m=2+p`, and the new endpoint `1.855087<2<=m` stays strictly inside the transient side for every `p`.

### Current primary-literature boundary, refreshed 20 September 2026

- Ben Arous--Fribergh--Sidoravicius, arXiv:1111.5865, states increasing child-bias speed for high bias (`beta>=717` in that arXiv version) on Galton--Watson trees without leaves.
- Aidekon, *Speed of the biased random walk on a Galton--Watson tree* (PTRF 159, 2014; arXiv:1111.4313), supplies the exact speed representation used below.
- He--Wang--Xiang, arXiv:1610.08151, now published in *Journal of Applied Probability* 62 (2025), 1044--1052, prove strict parent-bias decrease on

  `0<=lambda<=m1/(1+sqrt(1-1/m1))`

  when the minimum offspring `m1>=2`; their abstract records Aidekon's earlier source-uniform `lambda<=1/2` improvement.
- Bowditch--Tokushige provide differentiability/analyticity in the relevant ballistic regimes; regularity alone does not determine the sign.
- Song--Liu (2026) treats deterministic regular trees, not genuinely random offspring.

A bounded fresh search on 20 September 2026 found the 2025 publication and the 2026 regular-tree paper, but no checked source-wide resolution and no checked theorem identical to the all-mixture `{2,3}` endpoint below. This is not an exhaustive novelty certificate.

## 3. Metrics: parent source, restricted theorem, and auxiliary mechanism

### Parent source metric

Before: **OPEN**.  
After: **OPEN**.

No theorem for every no-leaf finite-mean offspring law on all `0<=lambda<m` is claimed.

### Restricted source-level metric

Before this run, for every `p in [0,1]` in the `{2,3}` family, strict decrease was certified through

`lambda<=18539/10000=1.8539`.

This run proves strict decrease for every `p in [0,1]` through

`BOX: lambda<=1855087/1000000 = 1.855087`.

The endpoint gain is

`1855087/1000000 - 18539/10000 = 1187/1000000 = 0.001187`.

On the genuinely new strip

`18539/10000 <= lambda <= 1855087/1000000`,

the exact finite core gives

`BOX: -ell'_lambda >= 8000000/23571869777569`
`                     = 3.3938758679... * 10^(-7) >0`

uniformly in every `p in [0,1]`.

The margin is intentionally tiny because the rational endpoint is pushed close to the frontier of this particular certificate. It is still exact and strictly positive.

### Auxiliary mechanism delta

A separate new lemma proves, for any no-leaf offspring law for which `a:=E[1/nu]` is finite and `lambda a<1`,

`BOX: E[1/B] <= 1/(1-lambda E[1/nu])`,

where `B` is the quenched escape probability to infinity before hitting the parent. For the `{2,3}` law,

`E[1/nu]=(3-p)/6`,

so at `lambda=2` and every `p>0`,

`BOX: E[1/B] <= 3/p`,

and hence

`P(B<=epsilon) <= 3 epsilon/p`.

This crosses the point where the old pointwise minimum-degree bound degenerates. It does **not** yet imply a sign for the speed derivative and is recorded as auxiliary progress only.

## 4. Consumed exact two-point derivative reduction

On `1<lambda<2`, let `B` be the quenched escape probability and put

`U=-dB/dlambda >=0`.

For conditional current offspring value `k`, take iid copies `B_0,...,B_k` with corresponding `U_i`, and set

`S_k=sum_{i=0}^k B_i`,
`D_k=lambda-1+S_k`,

`c_k=E[(1/(k+1))*S_k/D_k]`,

`h_k=E[(1/(k+1))*sum_i(B_i+(lambda-1)U_i)/D_k^2]`.

Direct differentiation, justified on every compact strip below 2 by the already proved bounded-support denominator/elasticity envelopes, gives

`c_k'=-h_k`.

For the `{2,3}` law define

`C=(1-p)c_2+p c_3`,
`theta=p c_3/C`,
`M=2+theta`.

Aidekon's symmetrized speed representation reduces exactly to

`ell_lambda=(M-lambda)/(M+lambda)`.

Therefore

`ell'_lambda=2(lambda M'-M)/(M+lambda)^2`.

Also

`theta/(1-theta)=[p/(1-p)] [c_3/c_2]`,

so

`theta'=theta(1-theta) Delta`,

with

`Delta=h_2/c_2-h_3/c_3`.

Consequently

`BOX: -ell'_lambda`
` = 2(2+theta)[1-lambda g(theta) Delta]/(2+theta+lambda)^2`,       (4.1)

where

`g(theta)=theta(1-theta)/(2+theta)`.                              (4.2)

The consumed NM13 branch-addition lemma proves

`3/4 <= t:=c_3/c_2 <=1`,

hence

`theta=p t/(1-p+p t)`

and in particular

`3p/(4-p) <= theta <=p`.                                         (4.3)

Thus it suffices to keep `lambda g(theta) Delta<1`.

## 5. New structural lemma: conditional type-3 escape stochastically dominates type-2 escape

Let `X_1,X_2,X_3` be iid copies of the unconditional descendant escape variable. Conditional on a vertex itself having two children, its escape probability has the distribution

`B^(2)=(X_1+X_2)/(lambda+X_1+X_2)`.

Conditional on three children, couple it by using the same first two descendants and an extra iid third descendant:

`B^(3)=(X_1+X_2+X_3)/(lambda+X_1+X_2+X_3)`.

Because `s -> s/(lambda+s)` is increasing for `s>=0`,

`B^(3)>=B^(2)` pointwise under this coupling.                     (5.1)

Therefore

`B | {nu=3}` stochastically dominates `B | {nu=2}`.              (5.2)

Now fix the outer `c_2` term. It contains three iid branch-escape variables. Conditional on exactly `m` of those three branches having own offspring type 3, let their sum be `T_m` and define

`Y_m=E[phi(T_m)]`,
`phi(s)=s/(lambda-1+s)`.

On the present strip `lambda>1`, `phi` is increasing. Couple the pattern with `m+1` type-3 branches to the pattern with `m` type-3 branches by changing one branch from a type-2 escape to its coupled type-3 escape from (5.1), leaving all other branches unchanged. Then `T_{m+1}>=T_m` pointwise, so

`BOX: Y_0<=Y_1<=Y_2<=Y_3`.                                      (5.3)

This monotonicity was discarded in the previous 16-corner upper-box treatment. Restoring it is the mathematical gain of this run.

## 6. Reverse-Chebyshev compression of the upper `h_2/c_2` score

Let `pi_m=C(3,m)p^m(1-p)^(3-m)`.

The inherited type-conditioned pathwise envelope gives a deterministic score upper bound `R_m^U(lambda)` for each pattern, so

`h_2/c_2 <= [sum_m pi_m Y_m R_m^U(lambda)]/[sum_m pi_m Y_m]`.    (6.1)

The exact finite core below certifies throughout the new lambda strip that each `R_m^U(lambda)` is increasing in `lambda`, and at the upper endpoint `L=1855087/1000000` the four frozen values

`R_m:=R_m^U(L)`

satisfy

`R_0>R_1>R_2>R_3`.                                               (6.2)

The exact differences printed by the checker are all positive.

For any probability weights `pi_m`, any nondecreasing sequence `Y_m`, and any nonincreasing sequence `R_m`,

`sum pi_m Y_m R_m <= (sum pi_m Y_m)(sum pi_m R_m)`.              (6.3)

Indeed

`Cov_pi(Y,R)`
` = (1/2) sum_{i,j} pi_i pi_j (Y_i-Y_j)(R_i-R_j) <=0`.

Using (5.3) and (6.2) in (6.1),

`BOX: h_2/c_2 <= U(p):=sum_{m=0}^3 pi_m R_m`.                   (6.4)

This removes every independent upper conditional-weight corner. No simulation is involved.

## 7. Exact rational pattern envelopes retained from the previous route

For completeness, the finite core uses the following already justified pathwise bounds. Put `a=lambda-1` and

`b_2=(2-lambda)/2`,
`b_3=3(2-lambda)/(6-lambda)`,
`u_2=2(3-lambda)/(lambda+6)`,
`u_3=(3-lambda)/3`,

`q_2^U=1/(2-lambda)`,
`q_3^U=4/[(2-lambda)(6-lambda)]`,
`q_2^L=9/[(3-lambda)(lambda+6)]`,
`q_3^L=1/(3-lambda)`.

For an outer pattern with `n` branches and `m` type-3 branches define

`s^-_{n,m}=(n-m)b_2+m b_3`,
`s^+_{n,m}=(n-m)u_2+m u_3`,

`y^-_{n,m}=s^-_{n,m}/(a+s^-_{n,m})`,
`y^+_{n,m}=s^+_{n,m}/(a+s^+_{n,m})`.

For the upper score define

`Q^U_{n,m}`
` =[(n-m)u_2 q_2^U+m b_3 q_3^U]/[(n-m)u_2+m b_3]`,

`R^U_{n,m}=(1+a Q^U_{n,m})/(a+s^-_{n,m})`.                      (7.1)

For the lower score define

`Q^L_{n,m}`
` =[(n-m)b_2 q_2^L+m u_3 q_3^L]/[(n-m)b_2+m u_3]`,

`R^L_{n,m}=(1+a Q^L_{n,m})/(a+s^+_{n,m})`.                      (7.2)

These formulas are rational in `lambda`. The checker proves exactly, on

`A=18539/10000 <= lambda <= L=1855087/1000000`,

that for the needed `(n,m)` patterns:

- both `y^-_{n,m}` and `y^+_{n,m}` decrease with `lambda`;
- both frozen score envelopes used here increase with `lambda`;
- every denominator has fixed positive sign.

It performs 27 exact rational monotonicity/denominator checks, all with positive Bernstein certificates and no subdivision.

For the lower `h_3/c_3` ratio we deliberately **do not** use a new monotonicity claim. Take `n=4`, set

`lo_m=y^-_{4,m}(L)`,
`hi_m=y^+_{4,m}(A)`,
`R_m^L=R^L_{4,m}(A)`.

The actual conditional escape weight `Z_m` lies in `[lo_m,hi_m]`, and the lower score is at least `R_m^L`, so

`h_3/c_3 >= F_p(Z_0,...,Z_4)`,

where

`F_p(z)= [sum_{m=0}^4 C(4,m)p^m(1-p)^(4-m) z_m R_m^L]`
`       /[sum_{m=0}^4 C(4,m)p^m(1-p)^(4-m) z_m]`.               (7.3)

For each coordinate separately, (7.3) is linear-fractional and its derivative has a sign independent of that coordinate. Hence the minimum over the 5-dimensional box is attained at a vertex. It is therefore rigorous to enumerate all `2^5=32` lower corners; this is the only finite corner enumeration retained.

## 8. Exact completion of the new strip

The function

`g(theta)=theta(1-theta)/(2+theta)`

increases on `[0,sqrt(6)-2]` and then decreases, with global maximum

`5-2sqrt(6)`.

Use the same exact rational split as the predecessor:

`p_*=449/1000 < sqrt(6)-2`,

certified by `(p_*+2)^2<6`.

### Small-p side

If `0<=p<=p_*`, then by (4.3), `theta<=p<=p_*`, so

`g(theta)<=g(p)=p(1-p)/(2+p)`.                                  (8.1)

### Remaining p side

For `p_*<=p<=1`, the exact rational number

`G=101021/1000000`

satisfies

`G>5-2sqrt(6)`,

certified by `(5-G)^2<24`. Hence

`g(theta)<=G`.                                                    (8.2)

For every one of the 32 lower-box corners from Section 7, the executed checker certifies with exact rational Bernstein arithmetic that, with

`Q=499999/500000=0.999998<1`,

- on `0<=p<=p_*`,

  `L * [p(1-p)/(2+p)] * [U(p)-F_corner(p)] <= Q`;               (8.3)

- on `p_*<=p<=1`,

  `L * G * [U(p)-F_corner(p)] <= Q`.                             (8.4)

There are 64 such product certificates. The maximum Bernstein subdivision depth is 8. The smallest terminal Bernstein coefficient is the positive exact rational printed in the archived output; the worst corner is the small-p corner `(0,0,1,1,1)`. Thus no floating-point sign decision enters the proof.

Since the actual lower ratio is at least the minimum of these corners, (6.4), (8.1)--(8.4), and `lambda<=L` imply uniformly

`lambda g(theta) Delta <= Q <1`.                                (8.5)

Substitute (8.5) into (4.1). Because `2(2+theta)>=4` and

`2+theta+lambda <=3+L`,

`-ell'_lambda`
` >= 4(1-Q)/(3+L)^2`
` = 8000000/23571869777569`
` >0`.                                                           (8.6)

This proves strict parent-bias decrease throughout the new strip for every `p in [0,1]`. Stitching to the preceding all-mixture theorem through `A=1.8539` proves the announced all-mixture endpoint

`BOX: 0<=lambda<=1.855087`.

No statement at or beyond `lambda=2` is inferred from this theorem.

## 9. Attack B: harmonic inverse-escape moment lemma, with finite-depth justification

The pointwise upper elasticity `-B'/B<=1/(2-lambda)` used in the minimum-degree-two route necessarily blows up at `lambda=2`. A different quantity has better average behavior.

Let

`B=S/(lambda+S)`, `S=sum_{j=1}^nu B_j`,

and set

`H=E[1/B]`.

For positive numbers `b_1,...,b_k`, Cauchy gives

`(sum_i b_i)(sum_i 1/b_i)>=k^2`,

hence

`1/(sum_i b_i) <= (1/k^2) sum_i 1/b_i`.                         (9.1)

A direct argument with the infinite-tree variable would risk manipulating `infinity<=infinity`, so use the standard finite-depth monotone truncation. Set `B^(0)=1` at the terminal boundary, and recursively

`B^(r+1)=S_r/(lambda+S_r)`,
`S_r=sum_{j=1}^nu B_j^(r)`.

Every `B^(r)>0`; the sequence decreases to the infinite-tree escape probability `B`. Put

`H_r=E[1/B^(r)]`.

Then

`1/B^(r+1)=1+lambda/S_r`.

Conditioning on `nu=k` and applying (9.1) to iid copies of `B^(r)`,

`E[1/S_r | nu=k] <= H_r/k`.

Therefore, with

`a=E[1/nu]`,

`H_{r+1} <=1+lambda a H_r`.                                     (9.2)

Since `H_0=1`, if `lambda a<1`, induction yields

`H_r <= sum_{j=0}^r (lambda a)^j <=1/(1-lambda a)`.             (9.3)

As `B^(r)` decreases to `B`, `1/B^(r)` increases to `1/B`. Monotone convergence now gives the rigorous infinite-depth bound

`BOX: H=E[1/B] <=1/(1-lambda E[1/nu])`.                         (9.4)

This proof includes the finite-depth denominator control needed to avoid assuming integrability in advance.

For the exact `{2,3}` family,

`E[1/nu]=(1-p)/2+p/3=(3-p)/6`.                                  (9.5)

Hence (9.4) holds whenever

`lambda<6/(3-p)`.                                                (9.6)

For every `p>0`, this interval crosses `lambda=2`; at `lambda=2`,

`E[1/B] <= 1/[1-2(3-p)/6] =3/p`.                               (9.7)

Finally, Markov's inequality applied to `1/B` gives the small-escape tail

`BOX: P(B<=epsilon)<=epsilon/[1-lambda(3-p)/6]`,                (9.8)

and in particular at `lambda=2`,

`P(B<=epsilon)<=3 epsilon/p`.                                   (9.9)

This is a genuine way around the **pointwise** `B>=1-lambda/2` collapse. What remains missing is a compatible average bound for the derivative elasticity `-B'/B` or directly for Aidekon's score. One cannot differentiate (9.4) as though it were an equality, and this report does not do so.

## 10. Attack C: exact obstruction to a pathwise derivative-order shortcut

Attack A used only the true stochastic order of escape probabilities. A tempting stronger claim is that adding a branch also decreases the logarithmic elasticity

`R=-B'/B`

pointwise. The exact recursion is

`R=[1+lambda (sum_i B_i R_i)/(sum_i B_i)]/[lambda+sum_i B_i]`.   (10.1)

That pathwise order is false even inside the sharp regular-tree envelope.

At

`lambda=371/200=1.855`,

take two branches at the regular-degree-3 endpoint

`B_hi=1-lambda/3`, `R_lo=1/(3-lambda)`,

and add a branch at the regular-degree-2 endpoint

`B_lo=1-lambda/2`, `R_hi=1/(2-lambda)`.

Before adding the third branch, (10.1) gives exactly

`R_before=360000/359759`
`        =1.0006698929...`.

After adding the third branch,

`R_after=4320000/3238687`
`       =1.3338738816...`.

The exact difference is

`R_after-R_before`
` =388231560000/1165146796433`
` >0`.                                                           (10.2)

The checker verifies (10.2) in exact arithmetic. Thus no proof may simply upgrade the escape stochastic order to a universal **pathwise derivative-elasticity** order. An averaged type-conditioned derivative comparison could still exist, but it needs genuinely new input.

## 11. What moved, what did not, and the remaining full-scope gap

### Source before/after

`OPEN -> OPEN`.

The source asks for every supercritical no-leaf finite-mean offspring law and the entire transient parent-bias interval `[0,m)`. This report proves neither that full scope nor a counterexample.

### Restricted theorem delta

For the genuinely unresolved finite-support family `{2,3}`, the complete all-mixture interval moves from

`[0,1.8539]`

to

`[0,1.855087]`.

The new strip has the exact uniform derivative margin (8.6).

### Auxiliary delta

The inverse-escape moment bound (9.4) is new within this track and remains non-singular at `lambda=2` for every nonzero type-3 mass. It supplies a rigorous small-escape tail rather than a pointwise minimum.

### Remaining obstruction

The central all-mixture `{2,3}` problem is still not bridged to 2, much less through it. The previous score-envelope proof loses control because pointwise logarithmic elasticity can be as large as `1/(2-lambda)`. Section 9 shows that the *escape denominator itself* is typically not as bad as that pointwise extremum suggests when `p>0`; Section 10 shows that the obvious branchwise derivative monotonicity needed to transfer this to `-B'/B` is false. The next substantive target inside this parent problem is therefore precise:

> derive an occupation- or escape-weighted expectation inequality for `-B'/B` (or directly for the Aidekon score) using the finite inverse moment (9.4), without replacing it by the false pointwise branch-addition order.

A finite-tree simulation is not enough. A successful next step must preserve a proved denominator/integrability estimate and a rigorous truncation or dominated-limit argument.

## 12. Exact checks and validation status

Executed checker:

`artifacts/prob10_2026-09-20/PROB10-06/20260920T0532Z_pattern_order_bridge_check.py`.

Archived output:

`artifacts/prob10_2026-09-20/PROB10-06/20260920T0532Z_pattern_order_bridge_check.out`.

It reports:

- 27 exact rational lambda-envelope monotonicity/denominator checks;
- strict exact decrease of the four frozen upper pattern scores in type-3 count;
- 64 exact Bernstein product certificates over the 32 lower-box corners and two p-regions;
- maximum Bernstein subdivision depth 8;
- exact positive uniform derivative margin `8000000/23571869777569`;
- exact Attack-C counterexample;
- terminal line `ALL_EXACT_CHECKS_PASS`.

This is a **self-check**, not an independent audit. No source-wide closure label is changed.

## 13. Structured ledger delta

```text
track: PROB10-06
source: Lyons--Pemantle--Peres biased-walk speed monotonicity
source_status_before: OPEN
source_status_after: OPEN
source_scope: P(nu=0)=0, E nu=m>1, parent lambda in [0,m); equivalently child beta in (1/m,infinity)
restricted_family: P(nu=2)=1-p, P(nu=3)=p, all p in [0,1]
restricted_endpoint_before: 18539/10000
restricted_endpoint_after: 1855087/1000000
restricted_endpoint_delta: 1187/1000000
certified_new_strip_margin: 8000000/23571869777569
auxiliary_new_lemma: E[1/B] <= 1/(1-lambda E[1/nu]) when lambda E[1/nu]<1
auxiliary_at_lambda_2_for_{2,3}: E[1/B] <= 3/p for p>0
attacks: A=SUCCESS, B=AUXILIARY_SUCCESS_NOT_SIGN_CLOSURE, C=ROUTE_REFUTED
validation: exact self-check PASS; independent audits absent
novelty: UNVERIFIED
remaining_gap: expected/occupation-weighted derivative elasticity control, especially at and beyond lambda=2
```

No email, Drive, public posting, scheduler mutation, workflow execution, permission change, force push, shared-root edit, or peer-file edit was performed.

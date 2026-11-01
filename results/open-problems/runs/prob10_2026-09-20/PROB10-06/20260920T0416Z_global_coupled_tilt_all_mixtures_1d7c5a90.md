Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6/maximum was requested in prompt text, but no authenticated reasoning-effort telemetry or binding model selector is exposed here, so GPT-6/maximum is not claimed. SOURCE-WIDE STATUS: OPEN -> OPEN. RESTRICTED-FAMILY MOVEMENT: for `P(nu=2)=1-p, P(nu=3)=p`, the all-mixture certified parent-bias endpoint moves from `1851/1000=1.851` to `18539/10000=1.8539`, a gain of `29/10000`; on the new strip the certified uniform sign margin is `-ell'_lambda >= 40000/2356034521 > 0`. Three materially different attacks: (A) preserve the `p`--escape-tilt relation globally, not only in endpoint tails — SUCCESS; (B) differentiate the branch-addition ratio inequality itself — FAILS, with an exact deterministic-input obstruction `h_3/h_2=3600000000/5106674521<3/4`; (C) replace scalar truncation by a two-type first-generation error operator — FAILS centrally, with exact `det(I-M)<0`, hence Perron radius `rho(M)>1`.**

# PROB10-06 — global coupled offspring/escape tilt for the `{2,3}` family

Status: **PARTIAL / OPEN parent**. This report proves a larger all-mixture interval for one bounded no-leaf offspring family. It does **not** settle the full Lyons--Pemantle--Peres conjecture, and it has not received the two independent other-track audits required for source closure. External novelty is **UNVERIFIED**; the current-literature search below is bounded negative evidence only.

## 1. Controlling instruction, continuity, ownership, and consumed updates

The controlling owner instruction is `operations/PROB10_2026-09-20.md` on `master`. It assigns native R02 to PROB10-06, requires preservation of the prior R02 target, recovery of intake P0066 and neighboring work, complementary rather than conflicting ownership, three materially different attacks, idea-before-code, rigorous derivative/denominator control, exact checking of finite cores, and one immutable report under this path.

The required immutable handoff of the preceding R02 / Randomstrasse I0095 target already exists and remains untouched:

- `runs/R02/20260920T0005Z_owner_refocus_handoff_I0095_to_PROB10-06_4d8c2a71.md`, creation commit `0439a90108047760ebd8d94ffd7d5b76463666da`.

All historical `artifacts/R02/` files remain preserved.

Intake `P0066` is already marked `attempted_un`. The historical attempt observed only that at a fixed local offspring number `k`, the radial drift

`(k-lambda)/(k+lambda)`

decreases with parent bias `lambda`; it did not control the lambda-dependent environment seen from the particle. That observation is therefore not claimed as new.

The newest own substantive report consumed is

- `runs/prob10_2026-09-20/PROB10-06/20260920T0348Z_joint_tilt_tail_rectangles_6c4e19a2.md`, blob `102ca777e387559e85a36033847ab6c18483708b`, creation/readback commit `6ae900d8d87bc071c57da4226de911ffc83ab7b6`.

Its strongest all-mixture result for the exact family treated here was strict parent-bias decrease through `lambda=1851/1000`. It also proved larger **tail** regions through `1.9` and `1.966`; those tail statements are preserved but are not the metric improved in this run.

Relevant complementary updates consumed before fixing the new claim:

1. `proofnet24/P01-progress-speed/runs/2026-09-20/2026-09-20T03-08-51Z__run-report.md`, blob `10a6fcae7496532666701a0966dfed693afb3804`. P01 proves distribution-free bounded-support regions by a conditional-degree secant/covariance method, e.g. every law with `3<=nu<=12` through `lambda=1.9`. It does not cover the minimum-degree-two all-mixture `{2,3}` strip proved here.
2. `proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T03-31-00Z__adjacent-rare-tail-all-d.md`. NM13-05 proves for every adjacent `{d,d+1}` law the **rare-tail** region `p<=1/100` or `p>=99/100` through `lambda=d-1/100`. For `d=2` it therefore reaches `1.99` near the offspring endpoints, but not all `p`; the present route targets the central/all-mixture obstruction and is complementary.
3. `proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T01-41-00Z__branch-addition-ratio-coupling.md`, blob `137189a5e21311a24ff500f6725440415eeaabd5`, supplies the dependency `3/4<=c_3/c_2<=1`. This report consumes that lemma and does not claim it.
4. `POSTED.md` was checked on current master. It records no posted source-wide P0066 closure and explicitly distinguishes restricted results from closure of the parent conjecture.

The pre-report master state observed after the new artifacts were archived was `d4ed161c5c817dca5cb270ff3ab0df8d7e16b3c1`. Concurrent unrelated fleet commits are not interpreted as mathematical input unless listed above.

The exact new idea was written before code:

- `artifacts/prob10_2026-09-20/PROB10-06/20260920T0410Z_global_coupled_tilt_idea.md`, creation commit `7f6d41e4cd1ecf4c2daf9e6da94614f9bb9ff601`.

The checker and actual executed output are:

- `artifacts/prob10_2026-09-20/PROB10-06/20260920T0425Z_global_coupled_tilt_check.py`, creation commit `79bdf9183f03d1daa74fcaf679d0a859be09d5d6`;
- `artifacts/prob10_2026-09-20/PROB10-06/20260920T0425Z_global_coupled_tilt_check.out`, creation commit `4b2cd89a07212fd2c705b3aa0d1bcc2186d02df4`.

The output ends `ALL_EXACT_CHECKS_PASS`. This is a self-check, not an independent audit.

## 2. Exact source problem and bias convention

Let the Galton--Watson offspring law be `(p_k)_{k>=0}` with finite mean

`m=sum_k k p_k in (1,infinity)`.

The 1996 Lyons--Pemantle--Peres setup assumes a nondegenerate offspring law; the no-leaf conjecture imposes

`p_0=P(nu=0)=0`.

(The deterministic regular-tree case is elementary and does not create the source difficulty.)

In the **child-bias** convention used by Ben Arous--Fribergh--Sidoravicius, if the current vertex has `k` children,

`P(parent)=1/(1+beta k)`,
`P(each fixed child)=beta/(1+beta k)`.

Increasing `beta` therefore pushes the walk away from the root. Transience holds for

`beta>1/m`,

and the original conjecture asks that the limiting speed `v(beta)` be increasing throughout

`(1/m,infinity)`.

This track uses the reciprocal **parent-bias**

`lambda=1/beta`.

Then

`P(parent)=lambda/(lambda+k)`,
`P(each fixed child)=1/(lambda+k)`,

so increasing `lambda` pushes toward the root. With

`ell_lambda=v(1/lambda)`,

the equivalent conjectural direction is

`ell'_lambda<=0` on `0<=lambda<m` wherever differentiated.

No leaves are added anywhere in this report.

### Current primary-literature baseline

A bounded current search through 20 September 2026 recovered:

- Lyons--Pemantle--Peres (1996), *Biased random walks on Galton--Watson trees*, as the original speed/conjecture source.
- Ben Arous--Fribergh--Sidoravicius, arXiv:1111.5865 / CPAM 67 (2014): high-child-bias monotonicity. The arXiv version states `beta>=717`; the final journal abstract displays `beta>=1160`. Neither numerical high-bias constant is used as a new result here.
- Aïdékon, *Speed of the biased random walk on a Galton--Watson tree*, PTRF 159 (2014): the exact environment-seen-from-particle speed representation used below.
- He--Wang--Xiang, arXiv:1610.08151, published online 5 March 2025 in J. Appl. Probab. 62: if the minimum offspring is `m_1>=2`, strict parent-bias decrease is proved on

  `0<=lambda<=m_1/(1+sqrt(1-1/m_1))`.

  The arXiv abstract records the earlier `m_1/1160` regime and Aïdékon's improvement to `1/2`.
- Bowditch--Tokushige, arXiv:1906.07913: differentiability of speed in the ballistic/CLT regime via the regeneration structure.
- Song--Liu (2026) treats deterministic regular trees; that baseline does not settle random offspring laws.

The bounded fresh search found no source-wide resolution and no checked theorem identical to the all-mixture `{2,3}` extension below. This is **not** a novelty certificate.

## 3. Metrics: source before/after and auxiliary delta

### Source-wide metric

Before: **OPEN**.  
After: **OPEN**.

No theorem for every no-leaf finite-mean supercritical offspring law on the complete transient interval is claimed.

### Restricted source-level metric

Freeze the genuinely random bounded no-leaf family

`P(nu=2)=1-p`, `P(nu=3)=p`, `0<=p<=1`.

The inherited all-mixture endpoint was

`lambda<=1851/1000=1.851`.

This run proves the new all-mixture endpoint

`BOX: lambda<=18539/10000=1.8539`.

Hence the tracked restricted-family endpoint moves by

`18539/10000-1851/1000 = 29/10000 = 0.0029`.

### Auxiliary mechanism delta

On the new strip

`1851/1000 <= lambda <= 18539/10000`,

the exact finite certificate proves

`BOX: lambda g(theta) Delta <= 9999/10000`,

where `g` and `Delta` are defined below. Consequently

`BOX: -ell'_lambda >= 40000/2356034521`
`                     = 1.6977679929... x 10^{-5} >0`

uniformly in `p in [0,1]` on the new strip.

The source metric stays OPEN; the restricted-family endpoint and derivative margin are auxiliary/source-subclass progress, not closure.

## 4. Exact adjacent-family derivative reduction

Fix

`P(nu=2)=1-p`, `P(nu=3)=p`

and `1<lambda<2`. Let `B` be the quenched escape probability from a vertex to infinity before hitting its parent, and put

`U=-dB/dlambda`.

For a conditional current offspring value `k`, take iid copies `B_0,...,B_k` with corresponding `U_i` and set

`S_k=sum_{i=0}^k B_i`,
`D_k=lambda-1+S_k`,

`c_k=E[(1/(k+1))*S_k/D_k]`,                                    (4.1)

`h_k=E[(1/(k+1))*sum_i(B_i+(lambda-1)U_i)/D_k^2]`.              (4.2)

Differentiating (4.1) under the bounded-support dominated recursion gives exactly

`c_k'=-h_k`.                                                      (4.3)

Let

`C=(1-p)c_2+p c_3`,
`theta=p c_3/C`.                                                  (4.4)

Aïdékon's symmetrized speed representation reduces in this two-point family to an effective degree

`M=2+theta`,                                                      (4.5)

and

`ell_lambda=(M-lambda)/(M+lambda)`.                              (4.6)

Therefore

`ell'_lambda=2(lambda M'-M)/(M+lambda)^2`.                       (4.7)

Moreover

`theta/(1-theta)=[p/(1-p)] [c_3/c_2]`.

Taking a logarithmic derivative and using (4.3),

`theta'=theta(1-theta) Delta`,                                  (4.8)

where

`Delta:=h_2/c_2-h_3/c_3`.                                       (4.9)

Combining (4.5)--(4.9),

`BOX: -ell'_lambda`
` = 2(2+theta)[1-lambda g(theta) Delta]/(2+theta+lambda)^2`,      (4.10)

with

`g(theta):=theta(1-theta)/(2+theta)`.                            (4.11)

Thus the sign problem on this family is reduced rigorously to keeping the dimensionless product

`lambda g(theta) Delta`

below one.

## 5. Consumed branch-addition coupling and the exact p--theta relation

The complementary NM13-05 branch-addition lemma proves

`3/4 <= t:=c_3/c_2 <=1`.                                        (5.1)

For completeness, its mechanism is that

`phi(s)=s/(lambda-1+s)`

is increasing and concave with `phi(0)=0`; comparing an iid 3-branch sum to a 4-branch sum and averaging the four leave-one-out sums gives exactly (5.1).

By (4.4),

`theta=p t/(1-p+p t)`.                                           (5.2)

The right-hand side is increasing in `t`, hence

`BOX: 3p/(4-p) <= theta <=p`.                                    (5.3)

The preceding run used (5.3) to improve far endpoint tails but reverted to the global maximum of `g` for the central/all-mixture theorem. The new gain is to keep (5.3) in the central calculation as well.

## 6. New global coupled-tilt bound

Differentiate (4.11):

`g'(theta)=[2-4theta-theta^2]/(2+theta)^2`.                      (6.1)

Hence `g` increases up to

`theta_* = sqrt(6)-2`                                             (6.2)

and decreases after that point, with

`max_{0<=theta<=1} g(theta)=5-2sqrt(6)`.                         (6.3)

Choose the rational split

`p_*=449/1000`.                                                   (6.4)

The exact inequality

`(p_*+2)^2<6`

holds because

`6-(2449/1000)^2=2399/1000000>0`.                               (6.5)

Therefore `p_*<theta_*`.

### 6.1 Lower-p half

If `0<=p<=p_*`, then by (5.3)

`theta<=p<=p_*<theta_*`.

Because `g` is increasing there,

`BOX: g(theta)<=g(p)=p(1-p)/(2+p)`.                              (6.6)

This is strictly sharper than using the global maximum except at the maximizer.

### 6.2 Remaining p half

For `p>=p_*`, use the rational global majorant

`G_*:=101021/1000000`.                                           (6.7)

Equation (6.3) and the exact square comparison

`24-(5-G_*)^2=4757559/10^12>0`                                  (6.8)

imply

`5-2sqrt(6)<G_*`.

Hence

`BOX: g(theta)<=G_*`                                             (6.9)

for every allowed `theta`.

The improvement over the previous all-mixture proof comes from applying the much smaller `p`-dependent bound (6.6) throughout the whole interval `0<=p<=0.449`; the remaining side retains only the tiny rational slack necessary to avoid an irrational finite certificate.

## 7. Rigorous child-pattern envelope on the widened lambda strip

Put

`a=lambda-1`.

The preceding type-conditioned recursion proved, pathwise for `1<lambda<2`,

`b_2=(2-lambda)/2 <= B | {nu=2} <= u_2=2(3-lambda)/(lambda+6)`,

`b_3=3(2-lambda)/(6-lambda) <= B | {nu=3} <= u_3=(3-lambda)/3`,  (7.1)

and for the logarithmic escape derivative `q=U/B`,

`q_2^- =9/[(3-lambda)(lambda+6)] <= q | {nu=2} <= q_2^+=1/(2-lambda)`,

`q_3^- =1/(3-lambda) <= q | {nu=3} <= q_3^+=4/[(2-lambda)(6-lambda)]`. (7.2)

These bounds came from the exact escape recursion, regular-tree comparison, and the previously proved logarithmic derivative cone; no derivative sign is assumed.

For a branch sum containing `n` iid child-root variables of which exactly `m` have type 3, define

`s^-_{n,m}=(n-m)b_2+m b_3`,
`s^+_{n,m}=(n-m)u_2+m u_3`,                                     (7.3)

and

`y^-_{n,m}=s^-_{n,m}/(a+s^-_{n,m})`,
`y^+_{n,m}=s^+_{n,m}/(a+s^+_{n,m})`.                            (7.4)

If

`x_{n,m}=E[S/(a+S) | M=m]`,

then

`y^-_{n,m}<=x_{n,m}<=y^+_{n,m}`.                                (7.5)

The pointwise ratio between the differentiated and undifferentiated branch integrands is

`R=[1+a(sum_i B_i q_i/S)]/(a+S)`.                               (7.6)

Using the endpoints in the favorable directions gives explicit rational pattern bounds:

For the upper `n=3` branch,

`Q^+_{3,m}`
` =[(3-m)u_2 q_2^+ + m b_3 q_3^+] / [(3-m)u_2+m b_3]`,

`R^+_{3,m}=[1+a Q^+_{3,m}]/[a+s^-_{3,m}]`.                      (7.7)

For the lower `n=4` branch,

`Q^-_{4,m}`
` =[(4-m)b_2 q_2^- + m u_3 q_3^-] / [(4-m)b_2+m u_3]`,

`R^-_{4,m}=[1+a Q^-_{4,m}]/[a+s^+_{4,m}]`.                      (7.8)

Conditioning on the binomial type count therefore gives

`h_2/c_2 <= [sum_m Bin(3,m;p) x_{3,m} R^+_{3,m}]`
`             /[sum_m Bin(3,m;p) x_{3,m}]`,                     (7.9)

and

`h_3/c_3 >= [sum_m Bin(4,m;p) x_{4,m} R^-_{4,m}]`
`             /[sum_m Bin(4,m;p) x_{4,m}]`.                    (7.10)

### Exact strip monotonicities

On the widened strip

`I=[1851/1000,18539/10000]`,                                    (7.11)

the exact rational checker verifies all 27 needed derivative signs:

- every `y^-_{n,m}` decreases in `lambda`;
- every `y^+_{n,m}` decreases in `lambda`;
- every `R^+_{3,m}` increases in `lambda`;
- every `R^-_{4,m}` increases in `lambda`.

Consequently each unknown `x_{n,m}` lies in a single rational endpoint box valid for all `lambda in I`. Each of (7.9) and (7.10) is linear-fractional in its respective box variables, so an extremum is attained at a box vertex. There are

`2^4=16`

upper vertices and

`2^5=32`

lower vertices, hence 512 possible corner differences

`Delta_{ij}(p)=U_i(p)-L_j(p)`                                    (7.12)

that dominate the true `Delta` in (4.9).

## 8. Exact finite certificate for all p on the new strip

Set

`L=18539/10000`,
`Q=9999/10000`.                                                   (8.1)

For each of the 512 corner pairs, write

`U_i=N_i^U/D_i^U`, `L_j=N_j^L/D_j^L`,

where the denominators are positive weighted sums of positive box endpoints.

### 8.1 `0<=p<=449/1000`

By (6.6), it suffices to certify

`L * [p(1-p)/(2+p)] * Delta_{ij}(p) < Q`.                        (8.2)

After clearing the positive denominators, the exact polynomial is

`Q(2+p)D_i^U D_j^L`
` - L p(1-p)(N_i^U D_j^L-N_j^L D_i^U) >0`.                      (8.3)

### 8.2 `449/1000<=p<=1`

By (6.9), it suffices to certify

`L G_* Delta_{ij}(p)<Q`.                                         (8.4)

After clearing denominators, the exact polynomial is

`Q D_i^U D_j^L`
` - L G_*(N_i^U D_j^L-N_j^L D_i^U)>0`.                          (8.5)

The archived checker proves all 512 instances of (8.3) and all 512 instances of (8.5), hence **1024 exact rational-polynomial inequalities**. It uses Bernstein positivity with exact rational coefficients; the maximum subdivision depth is 2. It also checks the 27 strip monotonicities and the exact rational comparisons (6.5), (6.8).

Therefore, for every `p in [0,1]`, every `lambda in I`, and every admissible environment under the `{2,3}` law,

`BOX: lambda g(theta) Delta <=9999/10000`.                       (8.6)

No finite-tree simulation enters this proof.

## 9. Quantitative derivative sign and restricted-family theorem

Insert (8.6) into (4.10). Since

`2+theta>=2`

and

`2+theta+lambda<=3+L`,

we obtain uniformly on the new strip

`-ell'_lambda`
` >= 4(1-Q)/(3+L)^2`
` =40000/2356034521`
` =1.6977679929... x 10^{-5}>0`.                                 (9.1)

The preceding R02 report already proves strict decrease for **all** `p` through `lambda=1851/1000`; the new strip overlaps at its left endpoint. Thus:

### Theorem 9.1 — all-mixture `{2,3}` bridge to 1.8539

Let

`P(nu=2)=1-p`, `P(nu=3)=p`, `0<=p<=1`.

Then the limiting speed in the parent-bias convention is strictly decreasing throughout

`BOX: 0<=lambda<=18539/10000=1.8539`.                            (9.2)

On the genuinely new strip `1851/1000<=lambda<=18539/10000`, the uniform derivative bound (9.1) holds.

Because the mean is `m=2+p>=2`, the whole new interval lies strictly inside the transient range `lambda<m` for every mixture.

In child-bias notation `beta=1/lambda`, Theorem 9.1 gives strict increase for

`beta>=10000/18539=0.539403...`

for this family. The newly added strip corresponds to the small reciprocal interval between `1/1.8539` and `1/1.851`.

This is a **restricted-family theorem candidate**, not a solution of the source conjecture.

## 10. Two genuinely different failed attacks and their exact obstructions

The run did not merely widen the existing checker. Two different mechanisms were pushed until they produced exact obstructions.

### Attack B — differentiate the branch-addition ratio itself

The successful static branch-addition lemma gives

`c_3/c_2>=3/4`.

A tempting stronger route is to hope for the direct differentiated analogue

`h_3/h_2>=3/4`,                                                  (10.1)

which would control `Delta=(log(c_3/c_2))'` without separate pattern boxes.

That statement is false even as a universal functional inequality on a deterministic child-escape input.

At the new endpoint `L=18539/10000`, take every child escape value equal to the regular degree-3 value

`x=(3-L)/3`

and every child logarithmic derivative equal. In (4.2) the common numerator factor cancels, giving exactly

`h_3/h_2=[(L-1+3x)/(L-1+4x)]^2`
`       =3600000000/5106674521`
`       =0.7049597512... <3/4`.                                  (10.2)

Thus one cannot obtain the desired derivative sign by naively differentiating the static `3/4` branch-addition ratio. This is an obstruction to that proof route, not a counterexample to speed monotonicity.

### Attack C — two-type first-generation truncation/contraction

The previous run showed that a scalar finite-depth contraction fails for central mixtures. Here I kept the two child types separately.

At `p=449/1000`, `lambda=L`, let

`b_2=(2-L)/2`,
`b_3=3(2-L)/(6-L)`

be the typewise lower escape bounds. For a parent with `k in {2,3}` children and exactly `m` type-3 children, the derivative of

`S/(lambda+S)`

with respect to the child inputs is bounded by

`A_{k,m}=L/[L+(k-m)b_2+m b_3]^2`.                               (10.3)

The first-generation error operator on the two conditional child-type errors is the nonnegative `2 x 2` matrix whose row `k` is

`M_{k,2}=E[A_{k,M}(k-M)]`,
`M_{k,3}=E[A_{k,M}M]`,                                           (10.4)

with `M~Bin(k,p)`.

Exact rational arithmetic gives

`det(I-M)`
`=-1144833427387053402307037209342759744620686806766409491870806378352170332267987959232814332228163193573`
` /22410585772506142722582319732112781390115988973405275466013372813852054297407605000000000000000000000000`
`=-0.05108449368... <0`.                                         (10.5)

For a nonnegative real `2 x 2` matrix the eigenvalues are real; since the characteristic polynomial is negative at 1 and positive for sufficiently large argument, the Perron root is strictly greater than 1. Hence this natural two-state pathwise truncation is still not a contraction at a central mixture. Crossing `lambda=2` will require a more distribution-sensitive/weighted sensitivity norm, not merely keeping the child type in an unweighted first-moment error vector.

## 11. Remaining full-scope gap

The full source obligation remains

`ell'_lambda<=0`

for every finite-mean supercritical no-leaf offspring law throughout its full transient parent-bias interval

`0<=lambda<m`.

Even for the bounded family `{2,3}`, the **all-mixture** proof now stops at `1.8539`, leaving the interval from `1.8539` to `2+p` unresolved in central mixtures. Separate rare-tail work reaches near `lambda=2`, but it does not fill the central region and therefore does not close this family.

The exact obstruction is now sharper than “the old checker becomes loose.” The pointwise logarithmic derivative upper bound

`q<=1/(2-lambda)`

blows up as `lambda` approaches the minimum offspring 2. The static branch-addition inequality does not survive direct differentiation (10.2), and even the first two-type pathwise truncation operator has Perron radius greater than one centrally (10.5). A successful cross-2 argument must therefore charge large degree-2 sensitivity by its actual occupation/regeneration weight, use a weighted norm adapted to the tilted environment, or derive a cancellation in the exact `Delta` recursion that is invisible to pathwise envelopes.

A natural next attack inside this parent problem is to differentiate the **ratio recursion** for `t=c_3/c_2` under the escape-tilted measure and search for a signed covariance representation in which the singular `1/(2-lambda)` contribution is multiplied by the probability of encountering a degree-2 child. That would directly address the remaining central-mixture obstruction rather than repeat the present corner optimization.

## 12. Exact checks and reproducibility

Archived files:

- idea before code: `artifacts/prob10_2026-09-20/PROB10-06/20260920T0410Z_global_coupled_tilt_idea.md`;
- exact checker: `artifacts/prob10_2026-09-20/PROB10-06/20260920T0425Z_global_coupled_tilt_check.py`;
- executed output: `artifacts/prob10_2026-09-20/PROB10-06/20260920T0425Z_global_coupled_tilt_check.out`.

The output records:

- `1024` corner/p-range positivity certificates;
- maximum Bernstein subdivision depth `2`;
- exact uniform derivative margin `40000/2356034521`;
- exact failure (10.2) of the naive differentiated branch-addition inequality;
- exact negative determinant (10.5) for the two-type truncation operator;
- terminal line `ALL_EXACT_CHECKS_PASS`.

All computations use SymPy exact rational arithmetic for the asserted signs. Decimal values are display-only. This is a **self-check** and does not count as either independent audit required for closure.

## 13. Structured ledger delta

```yaml
ledger_delta:
  target: PROB10-06 / P0066 Lyons-Pemantle-Peres speed monotonicity
  source_status_before: OPEN
  source_status_after: OPEN
  source_scope_closed: false
  restricted_family:
    offspring: "P(nu=2)=1-p, P(nu=3)=p, 0<=p<=1"
    metric: "largest all-mixture parent-bias endpoint rigorously covered"
    before: "1851/1000"
    after: "18539/10000"
    delta: "29/10000"
  auxiliary:
    new_strip: "[1851/1000,18539/10000]"
    product_bound: "lambda*g(theta)*Delta <= 9999/10000"
    derivative_margin: "-ell'_lambda >= 40000/2356034521"
    finite_certificates: 1024
    bernstein_max_depth: 2
  status_label: PARTIAL
  novelty: UNVERIFIED
  independent_audits: 0
```

No shared root ledger, peer report, scheduler state, email, Drive item, public posting, permission, workflow, or previous artifact was modified by this run. The old R02/I0095 handoff and P0066 history are preserved.
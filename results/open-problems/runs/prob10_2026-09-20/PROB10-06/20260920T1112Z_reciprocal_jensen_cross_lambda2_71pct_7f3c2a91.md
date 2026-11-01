Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6/maximum was requested in prompt text only; no authenticated applied-model/reasoning-effort telemetry is exposed, so GPT-6/maximum is not claimed. SOURCE-WIDE STATUS: OPEN -> OPEN. SUBSTANTIVE MOVEMENT: on the no-leaf `{2,3}` family, (A) for `p>=3/4` the certified parent-bias endpoint improves `2.02 -> 2.07`, with `-ell'_lambda >= 800/257049` on the new analytic strip; and (B) at the fixed cross-barrier endpoint `lambda=2.0021`, the certified mixture threshold improves `p>=3/4 -> p>=71/100`, with `-ell'_lambda >= 40000/2502100441`. The all-mixture endpoint remains `1.85527`. Main new mechanism: reciprocal-Jensen concavity converts the conditional inverse-escape moment bound directly into deterministic sibling denominators. Two different alternatives were also tested and exactly obstructed.**

# PROB10-06 — reciprocal-Jensen escape contraction crosses `lambda=2` at `p=0.71`

Status: **PARTIAL / OPEN parent.** This report proves restricted-family theorem candidates with exact rational self-checks. It does not settle the source-wide Lyons–Pemantle–Peres conjecture, does not claim worldwide novelty, and has not received the independent audits required for closure.

## 1. Contract, preserved handoff, intake, ownership, and consumed updates

Controlling instruction: `operations/PROB10_2026-09-20.md` on `master`. Root `POSTED.md` was re-read and contains no posted resolution of P0066; it explicitly forbids treating a restricted result as source closure. The current owner directive `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md` was also consumed; this run uses its method #18 (rewrite in another language: `B -> 1/B`), #4 (prove a smaller exact theorem), and #20 (identify exact failure of two alternative mechanisms).

The required immutable handoff of R02's actual preceding target already exists and is preserved rather than duplicated:

- `runs/R02/20260920T0005Z_owner_refocus_handoff_I0095_to_PROB10-06_4d8c2a71.md`, blob `24734b748956373b8257a0b4f11f681f359b8afa`, creation commit `0439a90108047760ebd8d94ffd7d5b76463666da`.

It hands off Randomstrasse/I0095 with all `artifacts/R02/` preserved. No I0095 artifact is relabelled as biased-walk progress.

Historical intake `P0066` remains `attempted_un` / attempted-unsolved. The old fixed-local-degree drift observation is not used as novelty: for fixed degree `k`, `(k-lambda)/(k+lambda)` decreasing in `lambda` does not control the `lambda`-dependent environment seen from the particle.

Immediate own predecessor consumed:

- `runs/prob10_2026-09-20/PROB10-06/20260920T0951Z_type_conditioned_inverse_chord_crosses_lambda2_8e3b1a6c.md`, blob `ff129b3d5b6dc6b080c758231f8e6e4da7832489`.

That report proves the all-mixture `{2,3}` endpoint `1.85527` and, for `p>=3/4`, strict decrease through `lambda=2.02`. Its mechanism uses conditional inverse moments only to obtain conditional means and then applies endpoint chords.

Complementary neighboring work consumed before fixing the claim:

- `proofnet24/P01-progress-speed/runs/2026-09-20/2026-09-20T10-01-39Z__run-report.md`, blob `bf5d15166a127ab0ab77a5810e7d7baa93056639`, works on minimum-offspring-one nonadjacent laws such as `{1,12}`, `{1,49}`, `{1,233}` below `lambda=1`.
- `proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T09-32-00Z__annealed-inverse-chord-crosses-lambda3.md`, blob `2903aed7ff5cc4462a3504470e5a73c25760ec7e`, works on the distinct `{3,4}` family and crosses `lambda=3` there.

Thus this owner keeps the delimited `{2,3}` reciprocal-Jensen route and does not overwrite those tracks.

Idea-before-certificate artifact:

- `artifacts/prob10_2026-09-20/PROB10-06/20260920T1030Z_reciprocal_jensen_idea.md`, blob `51703a2a25d6816551db4c06db5ff62cf25caa9f`, creation/readback commit `323c10499ca4b515bbf3e0d6e46996483e71ee15`.

Final exact checker and archived output:

- `artifacts/prob10_2026-09-20/PROB10-06/20260920T1055Z_reciprocal_jensen_two_rectangles_check.py`, blob `adbfcd8b48e4d802ead59086e2679a84034b27c7`, creation/readback commit `598127bbee91009f4b2edf0dbc69a08fb962c9d0`;
- `artifacts/prob10_2026-09-20/PROB10-06/20260920T1055Z_reciprocal_jensen_two_rectangles_check.out`, blob `d95222a2bba16e1910da6f82752f6b80555b8dfa`, creation/readback commit `4b6278a10c009772c3a3048da6c8d2b018f5d3f4`.

A preliminary one-rectangle checker at `20260920T1042Z_*` is preserved as an intermediate artifact; the `1055Z` checker supersedes it for this report.

## 2. Exact source problem and bias convention

Let `nu` be the Galton–Watson offspring variable. The original source problem assumes

`P(nu=0)=0`, `m=E nu in (1,infinity)`.

Thus there are **no leaves**.

The original Lyons–Pemantle–Peres question is stated in the parent-bias convention as monotonic nonincrease of the speed on

`lambda in [0,m]`.

At a vertex with `k` children the parent edge has weight `lambda` and each child edge weight `1`:

`P(parent | k)=lambda/(lambda+k)`,
`P(each fixed child | k)=1/(lambda+k)`.

Larger `lambda` pushes toward the root.

The reciprocal child-bias convention is

`beta=1/lambda`,

so

`P(parent | k)=1/(1+beta k)`,
`P(each fixed child | k)=beta/(1+beta k)`.

Larger `beta` pushes **away** from the root. The transient interior `0<lambda<m` is `beta>1/m`; the original closed source interval `[0,m]` corresponds to the reciprocal endpoint formulation `[1/m,infinity]` with the usual limiting interpretation at `lambda=0`. Therefore an increasing-speed statement in child bias is a decreasing-speed statement in parent bias. This report works only in the parent-bias convention and proves strict derivative signs inside the transient interval.

The restricted offspring family is

`P(nu=2)=1-p`, `P(nu=3)=p`, `0<=p<=1`,

with mean `m=2+p`. Every new endpoint below is less than `m` on its asserted parameter range.

## 3. Primary-source/current-literature boundary checked this run

The requested primary navigation was refreshed on 20 September 2026.

1. Ben Arous–Fribergh–Sidoravicius, arXiv:1111.5865, *A proof of the Lyons-Pemantle-Peres monotonicity conjecture for high biases*, states for Galton–Watson trees without leaves that the speed in the **child-bias** convention is increasing for `beta>=717`. This is baseline only.
2. He–Wang–Xiang, arXiv:1610.08151, published as *The speed of a biased walk on a Galton–Watson tree without leaves is monotonic for low values of bias*, J. Applied Probability 62 (2025), 1044–1052, proves in the **parent-bias** convention strict decrease for

   `0<=lambda<=m1/(1+sqrt(1-1/m1))`

   when minimum offspring `m1>=2`, and records Aïdékon's earlier source-uniform `lambda<=1/2` improvement. This is also baseline only.
3. Aïdékon, arXiv:1111.4313 / PTRF 159 (2014), supplies the exact environment/speed formula used below.
4. The original Lyons–Pemantle–Peres problem statement itself asks, under `p0=0`, whether `speed(lambda)` is monotonic nonincreasing for `lambda in [0,m]`.
5. A bounded current search found a 2026 deterministic regular-tree monotonicity paper but no checked source-wide solution and no checked theorem identical to the random `{2,3}` rectangles below. This is bounded negative evidence, not a novelty certificate.

## 4. Source before/after metrics and auxiliary delta

### Full source

Before: **OPEN**.  
After: **OPEN**.

No arbitrary-offspring theorem on the full source interval `[0,m]` is claimed.

### All-mixture `{2,3}` metric

Before: every `p in [0,1]` certified through `lambda=1.85527`.  
After: unchanged at `lambda=1.85527`.

### Fixed tail `p>=3/4`

Before: strict decrease through `lambda=2.02`.  
After:

`BOX A: p>=3/4 => strict decrease through lambda=207/100=2.07.`

Endpoint gain: `+0.05`.

On the new checker strip `1.85527<=lambda<=2.07`,

`BOX: -ell'_lambda >= 800/257049 > 0.`

The genuinely new region after subtracting predecessor coverage contains

`p>=3/4, 2.02<lambda<=2.07`.

### Fixed cross-barrier endpoint `lambda=2.0021`

Before: the predecessor gave this endpoint only for `p>=3/4`.  
After:

`BOX B: p>=71/100 => strict decrease through lambda=20021/10000=2.0021.`

Thus at this fixed endpoint the certified mixture threshold improves

`3/4 -> 71/100`,

a width gain `1/25=0.04`.

On `1.85527<=lambda<=2.0021`, `p>=71/100`,

`BOX: -ell'_lambda >= 40000/2502100441 > 0.`

The genuinely new region includes

`71/100<=p<3/4, 1.85527<=lambda<=2.0021`.

### Auxiliary mechanism delta

The predecessor used inverse moments only through `E[B|nu=k]` and then a support/mean endpoint chord. The new lemma uses `E[1/B|nu=k]` **directly**, after the reciprocal change of variables, and replaces the chord proxy `{0,u_2,u_3}` by deterministic type-denominators `{d_2,d_3}` for the derivative kernels.

The same contraction gives an explicit truncation bound on both rectangles:

`BOX: E[B_N-B] <= (19/20)^N`.

## 5. Escape recursion and inverse moments, including denominator positivity

Let `B=B(lambda)` be the quenched probability, starting from a branch root, of escaping to infinity before hitting its parent. If the root has `nu=k` children with iid child escapes `B_1,...,B_k`, then

`B=S/(lambda+S)`, `S=sum_{i=1}^k B_i`.                         (5.1)

For finite-depth upper truncation, put boundary escape equal to one at depth zero and iterate (5.1). These `B_N` decrease to `B`.

Set `X=1/B` and `M=E X`. From (5.1),

`X=1+lambda/S`.                                                  (5.2)

Conditionally on `nu=k`, Cauchy's inequality gives

`1/S <= (1/k^2) sum_i 1/B_i`.                                  (5.3)

Apply this first to the finite-depth truncations. If `M_N=E(1/B_N)`, then

`M_{N+1} <= 1+lambda E(1/nu) M_N`.                              (5.4)

For the `{2,3}` law,

`E(1/nu)=(3-p)/6`.

Define

`d:=1-lambda(3-p)/6`.                                           (5.5)

Whenever `d>0`, iterating (5.4) and applying monotone convergence gives

`BOX: M=E(1/B) <= 1/d`.                                         (5.6)

On the larger numerical rectangle used in Box B, the smallest denominator occurs at `lambda=20021/10000`, `p=71/100`, and is

`d >= 1415191/6000000 >0`.                                     (5.7)

Thus no inverse-moment denominator is assumed away.

Conditioning (5.2) on the root type gives

`E[1/B | nu=k] <= 1+(lambda/k)M <= 1+lambda/(k d)`.             (5.8)

Write

`M_k:=1+lambda/(k d)`,
`d_k:=1/M_k = k d/(k d+lambda)`, `k=2,3`.                       (5.9)

The key point is that (5.8), not merely `E B>=d_k`, is retained.

## 6. New reciprocal-Jensen lemma

For `a>0`, `t>=0`, define

`F_{a,t}(x)=a/(a+t+x)^2`.                                       (6.1)

Let `Z=1/B`. Then

`G_{a,t}(z):=F_{a,t}(1/z)=a z^2/((a+t)z+1)^2`.                  (6.2)

Direct differentiation gives

`G'_{a,t}(z)=2 a z/((a+t)z+1)^3 >=0`,                           (6.3)

and

`G''_{a,t}(z)=2a(1-2(a+t)z)/((a+t)z+1)^4`.                     (6.4)

Hence `G` is increasing and concave whenever `2(a+t)z>=1`.

In every application below, `0<B<=1`, hence `Z>=1`, and the smallest base is

`a=lambda-1 >= 0.85527 >1/2`.

Therefore the concavity condition holds uniformly. Conditional on `nu=k`, Jensen plus (5.8) gives

`E[F_{a,t}(B)|nu=k]`
` = E[G_{a,t}(Z)|nu=k]`
` <= G_{a,t}(E[Z|nu=k])`
` <= G_{a,t}(M_k)`
` = a/(a+t+d_k)^2`.                                             (6.5)

This is the new inequality.

Now take independent branch escapes and condition on their offspring types. Repeatedly applying (6.5) yields, for `j=1,2`,

`K_j(a):=E[a/(a+B_1+...+B_j)^2]`

`<= sum_{r_1,...,r_j in {2,3}} P(r_1)...P(r_j)`
`   * a/(a+d_{r_1}+...+d_{r_j})^2`.                            (6.6)

Explicitly, with `w_2=1-p`, `w_3=p`,

`K_1(a) <= a w_2/(a+d_2)^2 + a w_3/(a+d_3)^2`,                 (6.7)

`K_2(a) <= a w_2^2/(a+2d_2)^2`
`          +2a w_2w_3/(a+d_2+d_3)^2`
`          +a w_3^2/(a+2d_3)^2`.                               (6.8)

No derivative sign has been assumed.

## 7. Annealed contraction for `U=-B'` and the truncation error

Differentiating (5.1) formally gives

`U=S/(lambda+S)^2 + lambda sum_i U_i/(lambda+S)^2`.             (7.1)

This identity can be justified from finite depth and the contraction below; equivalently, iterating (7.1) writes `U` as a nonnegative tree series whose expected generation weights form a geometric series.

Because all offspring are at most three, comparison with the deterministic ternary tree gives

`0<B<=u:=(3-lambda)/3`.                                         (7.2)

On our strips `lambda>1.855`, `k u<lambda` for `k=2,3`, so `s/(lambda+s)^2` is increasing throughout the relevant range. Therefore the expectation of the first term of (7.1) is at most

`A=(1-p)*6(3-lambda)/(lambda+6)^2 + p*(3-lambda)/9`.            (7.3)

For a fixed child `i`, let `T_i` be the sum of the other sibling escapes. Since `U_i>=0`,

`lambda U_i/(lambda+B_i+T_i)^2`
` <= U_i * lambda/(lambda+T_i)^2`.                              (7.4)

After dropping the own escape, `U_i` is independent of the siblings. Hence, using (6.7)-(6.8),

`E U <= A + rho E U`,                                          (7.5)

where

`rho=(1-p)*2 K_1(lambda)+p*3 K_2(lambda)`.                      (7.6)

The exact checker proves `rho<19/20` on both rectangles, so

`eta:=E U <= A/(1-rho)`.                                       (7.7)

This also supplies the finite-depth derivative domination needed to pass from (7.1) at finite depth to the infinite branch recursion: the expected contribution from derivative sources at generation `n` is bounded by a constant times `rho^n`, so the derivative series converges absolutely in `L^1`.

The same coefficient controls the escape truncation itself. Let `B_N` be the depth-`N` upper approximation. Between `B_N` and `B`, the coordinate derivative of the recursion is

`lambda/(lambda+S)^2`.                                         (7.8)

For the `i`th coordinate, drop the own coordinate exactly as in (7.4). The sibling variables in the intermediate value are at least the infinite-tree escapes and at most the truncations; since `B_N>=B`, their reciprocal moments are no worse than (5.8), so the reciprocal-Jensen bound (6.6) still applies. Independence of sibling subtrees then gives

`E|B_{N+1}-B| <= rho E|B_N-B|`.                                (7.9)

Since `0<=B_N-B<=1`,

`BOX: E[B_N-B] <= rho^N <= (19/20)^N`.                          (7.10)

Thus the denominator/truncation control is explicit, not assumed.

## 8. Aïdékon reduction and derivative-score bound

Put `a=lambda-1>0`. For current offspring count `k`, let `B_0,...,B_k` be iid branch escapes, `S_k=sum_{i=0}^k B_i`, and define

`c_k=E[(1/(k+1))*S_k/(a+S_k)]`,                                (8.1)

`h_k=E[(1/(k+1))*sum_i(B_i+a U_i)/(a+S_k)^2]`.                 (8.2)

The justified differentiation above gives

`c'_k=-h_k`.                                                     (8.3)

For the `{2,3}` law define

`C=(1-p)c_2+p c_3`,
`theta=p c_3/C`,
`Mstar=2+theta`.                                                 (8.4)

Aïdékon's symmetrized speed formula becomes

`ell_lambda=(Mstar-lambda)/(Mstar+lambda)`.                     (8.5)

Let

`Delta=h_2/c_2-h_3/c_3`.                                       (8.6)

Since

`theta'=theta(1-theta) Delta`,                                  (8.7)

differentiating (8.5) gives the exact identity

`BOX: -ell'_lambda`
` = 2 Mstar [1-lambda g(theta) Delta]/(Mstar+lambda)^2`,         (8.8)

where

`g(theta)=theta(1-theta)/(2+theta)`.                            (8.9)

It remains to upper-bound `Delta`.

First, with `S=S_3`,

`c_2=E[S/(3(a+S))]`.                                            (8.10)

By (7.2), `a+S<=a+3u=2`. Also `E B>=mu`, where

`mu=(1-p)d_2+p d_3`.                                            (8.11)

Hence

`c_2>=mu/2`.                                                     (8.12)

For `h_2`, the `S` part of (8.2) contributes at most `c_2/a`. For the `U` part, exchangeability, dropping the own `B_i`, independence, and (6.8) with base `a` give at most

`eta K_2(a)`.                                                    (8.13)

Dividing by (8.12),

`h_2/c_2 <= 1/a + 2 eta K_2(a)/mu`.                             (8.14)

For `h_3/c_3`, discard the nonnegative `U` term. If `S=S_4`, then by (7.2)

`a+S <= a+4u = (9-lambda)/3`.                                  (8.15)

Therefore the ratio of the weighted expectations satisfies

`h_3/c_3 >= 3/(9-lambda)`.                                      (8.16)

Combining,

`BOX: Delta <= D(lambda,p)`
` := 1/(lambda-1) + 2 eta K_2(lambda-1)/mu - 3/(9-lambda)`.     (8.17)

## 9. Static tilt interval and final sign reduction

A coupling of the same iid branches gives the elementary ratio bound

`3/4 <= c_3/c_2 <= 1`.                                         (9.1)

For completeness: coupling `S_4=S_3+B_4` and using that `s/(a+s)` increases gives

`c_3 = (1/4) E[S_4/(a+S_4)] >= (1/4)E[S_3/(a+S_3)] = (3/4)c_2`.

For the upper bound, by exchangeability

`c_3=E[B_1/(a+B_1+B_2+B_3+B_4)]`
` <= E[B_1/(a+B_1+B_2+B_3)]=c_2`.

Hence

`theta >= theta_0(p):=3p/(4-p)`.                               (9.2)

The exact checker verifies at the smallest `p=71/100` that

`theta_0^2+4 theta_0-2>0`.                                     (9.3)

Since

`g'(theta)` has the sign of `2-4theta-theta^2`,

`g` is decreasing on the entire realized tilt interval. Thus

`g(theta)<=g(theta_0(p))`.                                      (9.4)

If the true `Delta` is negative, the bracket in (8.8) is already larger than one. Otherwise (8.17) and (9.4) give

`lambda g(theta) Delta`
` <= lambda g(theta_0(p)) D(lambda,p)`.                         (9.5)

The remaining inequalities are rational functions of `(lambda,p)` and are the exact finite core certified below.

## 10. Exact checker results

The final checker uses exact `fractions.Fraction` interval arithmetic and adaptive bisection; no floating result is used to accept a box.

### Rectangle A

Domain:

`185527/100000 <= lambda <= 207/100`,
`3/4 <= p <=1`.

It visits `2093` boxes and accepts `1047`, proving simultaneously

`rho<19/20`,
`lambda g(theta_0) D < 49/50`.

The archived output records the largest accepted interval upper values only for diagnostics:

`product < 0.979995254120080`,
`rho < 0.949506354406586`.

Using (8.8), `2<=Mstar<=3`, and `lambda<=207/100`,

`-ell'_lambda`
` >= 4(1-49/50)/(3+207/100)^2`
` = BOX: 800/257049 >0`.                                        (10.1)

### Rectangle B

Domain:

`185527/100000 <= lambda <= 20021/10000`,
`71/100 <= p <=1`.

It visits `5441` boxes and accepts `2721`, proving

`rho<19/20`,
`lambda g(theta_0) D < 9999/10000`.

Hence

`-ell'_lambda`
` >= 4(1-9999/10000)/(3+20021/10000)^2`
` = BOX: 40000/2502100441 >0`.                                  (10.2)

The checker terminates with

`ALL_EXACT_CHECKS_PASS`.

These are self-checks, not independent audits.

## 11. The two other mathematical attacks and their exact obstructions

### Attack 2 — inverse-moment quantile proxy: blocked

Instead of reciprocal Jensen, use Markov directly on (5.8). For a parameter `alpha in [0,1]`, set `t_k=alpha d_k`. Then

`P(B<t_k | nu=k) <= alpha`.                                     (11.1)

For every decreasing sibling kernel this gives a two-level lower proxy: mass at zero with probability `alpha`, and otherwise the type-dependent threshold `t_k`.

This is genuinely different from the successful concavity route because it uses a tail split rather than Jensen on `1/B`.

At the test point `lambda=2`, `p=3/4`, the exact interval checker partitions the entire `alpha in [0,1]` interval into 56 accepted boxes (111 visited) and proves

`BOX: rho_quantile(alpha) > 6/5 for every alpha in [0,1]`.       (11.2)

Thus this entire one-parameter Markov-proxy family cannot even establish the needed one-step contraction `rho<1` at that point. This is an obstruction to this proxy, not a theorem that all tail methods fail.

### Attack 3 — differentiate reciprocal escape `W=U/B^2`: current decoupling blocked

Differentiate (5.2) directly. With `w_i=B_i/S`,

`W:=d(1/B)/d lambda=U/B^2`

satisfies the exact recursion

`W = 1/S + lambda sum_i w_i^2 W_i`.                             (11.3)

This attacks a different derivative observable. To decouple `W_i` from its own weight, bound `B_i<=u` and use endpoint-chord control on the siblings. At the new hard corner `lambda=2`, `p=71/100`, the resulting exact proposed contraction coefficient is

`rho_W = 2135191601264005788851 / 1498331327641225000000`
`      = 1.42504635782085... >1`.                               (11.4)

Therefore this sibling-decoupled `W` estimate is quantitatively incapable of proving contraction there. A viable `W` route would have to retain the negative correlation between a large `W_i` and the normalized weight `w_i^2`, or obtain a new mixed moment. This is a precise next-step obstruction rather than another unchanged numerical run.

## 12. Complete covered region and remaining full-scope gap

Within this owner's `{2,3}` route, the rigorously self-certified repository coverage is now at least:

- every `p in [0,1]`: through `lambda=1.85527` (predecessor theorem);
- every `p>=71/100`: through `lambda=2.0021` (this run);
- every `p>=3/4`: through `lambda=2.07` (this run);
- the predecessor's deeper high-`p` rectangle `p>=41/50` through `lambda=2.16` remains preserved and is not superseded by the shallower statements above.

The full source conjecture still requires arbitrary no-leaf offspring distributions and the entire parent-bias interval `[0,E nu]`. Even for the single `{2,3}` family, the central mixture region above `lambda=1.85527` and the approach to the critical endpoint `lambda=2+p` remain unresolved. The all-mixture endpoint did not move this run.

The successful reciprocal-Jensen lemma suggests the next nonduplicating direction: derive a mixed reciprocal derivative moment, for example a controlled quantity involving `E[U/B]` or `E[U/B^2]`, strong enough to retain the own-child denominator rather than dropping it in (7.4). The exact obstruction (11.4) says that a scalar sibling decoupling is insufficient; a joint state is needed.

No finite simulation is counted as proof. No email, Drive, public posting, scheduler state, permissions, or workflow state was changed.
Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6/maximum was requested in prompt text only; no authenticated applied-model/reasoning-effort telemetry is exposed, so GPT-6/maximum is not claimed. SOURCE-WIDE STATUS: OPEN -> OPEN. ALL-MIXTURE `{2,3}` ENDPOINT: `1.85527 -> 1.85527` (no movement). RESTRICTED SOURCE MOVEMENT: for `P(nu=2)=1-p, P(nu=3)=p` and every `p>=41/50`, the certified parent-bias endpoint moves `1.9 -> 54/25=2.16`, crossing the minimum-degree singularity `lambda=2`, with exact uniform sign certificate `-ell'_lambda >= 5/33282 >0` on the genuinely new strip `19/10<=lambda<=54/25`. Three materially different attacks: (1) annealed inverse-escape + convex endpoint-chord contraction for `U=-B'` — SUCCESS; (2) direct logarithmic-derivative `q=-B'/B` contraction — EXACTLY TOO WEAK at the hard corner, yielding a speed-product upper bound `≈22.2776>1`; (3) near-critical Einstein-relation bridge — known qualitative baseline but no explicit neighborhood width recovered, so no certified overlap.**

# PROB10-06 — an annealed escape-derivative contraction crossing `lambda=2`

Status: **PARTIAL / OPEN parent.** This report proves a larger rigorously covered region for one genuinely random finitely supported no-leaf offspring family. It does **not** settle the source-wide Lyons–Pemantle–Peres conjecture. The exact finite certificate is a self-check, not an independent audit. External novelty is **UNVERIFIED**; the literature screen is bounded negative evidence only.

## 1. Controlling instruction, continuity, ownership, and consumed state

Controlling instruction: `operations/PROB10_2026-09-20.md`, blob `6f0fcee836d93371d43b84af1a55150fedc80779` on `master` when consumed.

The required immutable handoff of R02's preceding Randomstrasse/I0095 target remains preserved:

- `runs/R02/20260920T0005Z_owner_refocus_handoff_I0095_to_PROB10-06_4d8c2a71.md`, creation commit `0439a90108047760ebd8d94ffd7d5b76463666da`.

All historical `artifacts/R02/` remain untouched. No Randomstrasse claim is relabelled as biased-walk progress.

Historical intake `P0066` remains `attempted_un` / attempted-unsolved. Its old observation that the fixed-degree local radial drift `(k-lambda)/(k+lambda)` decreases with parent bias does not control the `lambda`-dependent environment seen from the particle and is not claimed here as new.

`POSTED.md` was checked on current `master`; it does not record a posted source-wide closure of P0066.

Consumed own predecessor:

- `runs/prob10_2026-09-20/PROB10-06/20260920T0716Z_moderate_mixture_rectangle_5d8b2e41.md`, blob `3b8242141a03f40f6f98c64289db43561b561823`.

That report leaves the all-mixture `{2,3}` endpoint at `1.85527`, proves `p<=1/4` through `lambda=1.87`, and records the inherited upper tail `p>=41/50` through `lambda=1.9`. It explicitly identifies the pointwise binary-tree derivative envelope `1/(2-lambda)` as the obstruction at `lambda=2`.

Consumed complementary neighboring work rather than duplicating it:

- `proofnet24/P01-progress-speed/runs/2026-09-20/2026-09-20T06-57-50Z__run-report.md`, blob `e553712873f324f6acec968674fcb37c75f834c2`: minimum-offspring-one, support-free `lambda<1` compression; different offspring class and mechanism.
- `proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T07-25-00Z__quantitative-branch-addition-window.md`, blob `3bd9d5b15ffc254763d5c6cef3e1504906041124`: adjacent `{3,4}` branch-addition windows; different offspring class.

The exact new idea was persisted before code:

- `artifacts/prob10_2026-09-20/PROB10-06/20260920T0818Z_cross_lambda2_inverse_escape_chord_idea.md`, creation commit `d00af7e027a897b258cf4af5af4c2b4fb21da910`.

Exact checker and archived stdout:

- `artifacts/prob10_2026-09-20/PROB10-06/20260920T0836Z_cross_lambda2_inverse_escape_chord_check.py`, creation commit `b7263bceb6f395a59c4ab91bee4deaf597076e70`;
- `artifacts/prob10_2026-09-20/PROB10-06/20260920T0836Z_cross_lambda2_inverse_escape_chord_check.out`, creation commit `7c3d0251d42fa0cb0de9eeef749c9ce024cbefc1`.

The checker process exited with code zero and the archived stdout ends `ALL_EXACT_CHECKS_PASS`.

## 2. Exact source problem and bias convention

Let `nu` be the Galton–Watson offspring variable. The source setting is

`P(nu=0)=0`, `m=E nu in (1,infinity)`.

Thus there are **no leaves**.

In the child-bias convention, at a vertex with `k` children,

`P(parent)=1/(1+beta k)`,
`P(each fixed child)=beta/(1+beta k)`.

Larger `beta` increases drift away from the root. The source conjecture asks the limiting speed `v(beta)` to be increasing throughout the transient interval

`beta in (1/m,infinity)`.

This track uses reciprocal parent bias

`lambda=1/beta`,

so

`P(parent)=lambda/(lambda+k)`,
`P(each fixed child)=1/(lambda+k)`.

Larger `lambda` pushes toward the root. With `ell_lambda=v(1/lambda)`, the equivalent conjecture is that `ell_lambda` is nonincreasing on

`0<=lambda<m`.

The restricted family in this report is

`P(nu=2)=1-p`, `P(nu=3)=p`, `41/50<=p<=1`,

with mean `m=2+p>=141/50=2.82`. Every new parent-bias value satisfies `lambda<=54/25=2.16<m`, hence lies strictly inside the transient interval.

## 3. Primary/current literature boundary checked this run

The bounded current navigation was refreshed on 20 September 2026.

1. Ben Arous–Fribergh–Sidoravicius, arXiv:1111.5865, proves the Lyons–Pemantle–Peres monotonicity conjecture for sufficiently high **child** bias on Galton–Watson trees without leaves. This is a known baseline, not a new result here.
2. Aïdékon, arXiv:1111.4313 / PTRF 159 (2014), supplies the exact speed representation consumed below.
3. He–Wang–Xiang, arXiv:1610.08151, later published in *Journal of Applied Probability* 62 (2025), proves strict parent-bias decrease on

   `0<=lambda<=m1/(1+sqrt(1-1/m1))`

   when minimum offspring `m1>=2`, and records Aïdékon's earlier source-uniform low-parent-bias improvement. Those are known baselines.
4. Ben Arous–Hu–Olla–Zeitouni, arXiv:1106.4387, proves an Einstein relation at the critical bias under an exponential-moment hypothesis, which is automatic for the present finite-support family. This gives a qualitative near-critical monotonicity input in the literature, but the bounded check did not recover an explicit neighborhood width that can be stitched to the certified interval below.
5. A bounded search found no checked source-wide resolution and no checked theorem identical to the upper-tail `{2,3}` rectangle proved here. This is not an exhaustive novelty certificate.

## 4. Metrics: source before/after and auxiliary delta

### Full parent source metric

Before: **OPEN**.  
After: **OPEN**.

No theorem for every no-leaf offspring law on all `0<=lambda<m` is claimed.

### All-mixture `{2,3}` metric

Before: every `p in [0,1]` certified through `lambda=1.85527`.  
After: unchanged at `lambda=1.85527`.

### Restricted upper-tail source-level movement

Before this run:

`p>=41/50  =>  ell_lambda strictly decreases on 0<=lambda<=19/10`.

After this run:

`BOX: p>=41/50  =>  ell_lambda strictly decreases on 0<=lambda<=54/25`.

The endpoint gain is

`54/25-19/10 = 13/50 = 0.26`.

The genuinely new strip is

`BOX: 41/50<=p<=1,  19/10<=lambda<=54/25`.

It crosses the previously singular minimum-degree point `lambda=2`.

On that whole new strip,

`BOX: -ell'_lambda >= 5/33282 = 0.000150231356... >0`.

### Auxiliary mechanism delta

The mechanism-level advance is a distribution-sensitive **annealed** contraction for `U=-B'` based on an inverse-escape moment bound plus bounded-support convexity. It remains finite across `lambda=2`, unlike the inherited pointwise bound `-B'/B<=1/(2-lambda)`. This is the main conceptual movement of the run.

## 5. Exact two-point speed derivative reduction consumed

For `lambda>1`, let `B=B(lambda)` be the quenched probability, starting at a child vertex, of escaping to infinity before hitting its parent, and put

`U=-B'(lambda)>=0`.

For current offspring value `k`, take iid copies `B_0,...,B_k` and corresponding `U_i`, and define

`S_k=sum_i B_i`,
`D_k=lambda-1+S_k`,

`c_k=E[(1/(k+1))*S_k/D_k]`,

`h_k=E[(1/(k+1))*sum_i(B_i+(lambda-1)U_i)/D_k^2]`.

On compact subintervals of the present transient region, the inherited dominated-differentiation argument gives

`c'_k=-h_k`.

For the `{2,3}` law set

`C=(1-p)c_2+p c_3`,
`theta=p c_3/C`,
`M=2+theta`.

Aïdékon's symmetrized speed formula reduces exactly to

`ell_lambda=(M-lambda)/(M+lambda)`.

Put

`Delta=h_2/c_2-h_3/c_3`.

Since

`theta'=theta(1-theta)Delta`,

direct differentiation gives

`BOX: -ell'_lambda`
` = 2(2+theta)[1-lambda g(theta)Delta]/(2+theta+lambda)^2`,

where

`g(theta)=theta(1-theta)/(2+theta)`.

Thus it suffices to prove a uniform upper bound

`lambda g(theta)Delta <1`.

## 6. Attack 1 — successful annealed inverse-escape / endpoint-chord contraction

Fix throughout this section

`41/50<=p<=1`,
`19/10<=lambda<=54/25`.

Write simply `B` for a generic branch escape probability.

### 6.1 Inverse-escape moment and a positive annealed mean lower bound

The branch recursion is

`B=S/(lambda+S)`,
`S=sum_{i=1}^nu B_i`.

Set `X=1/B`. Then

`X=1+lambda/S`.

By Cauchy's inequality,

`1/S <= (1/nu^2) sum_{i=1}^nu 1/B_i`.

Hence pathwise

`X <= 1 + (lambda/nu^2) sum_i X_i`.                              (6.1)

To avoid assuming integrability, apply (6.1) first to finite-depth escape probabilities with boundary value one. If `M_N` denotes the finite-depth expectation, independence gives

`M_N <= 1 + lambda E[1/nu] M_{N-1}`.                            (6.2)

For the `{2,3}` law,

`E[1/nu]=(1-p)/2+p/3=(3-p)/6`.                                  (6.3)

Put

`d:=1-lambda(3-p)/6`.                                           (6.4)

On the entire target rectangle `d>0`; in fact the exact minimum is attained at the hard corner `(lambda,p)=(54/25,41/50)` and equals

`d_min=269/1250`.                                                (6.5)

Iterating (6.2) gives `M_N<=1/d`; monotone convergence of the finite-depth escapes therefore yields

`BOX: E[1/B] <=1/d`.                                             (6.6)

By Jensen,

`BOX: mu:=E B >= d`.                                             (6.7)

This lower bound is annealed and remains positive at and above `lambda=2` whenever `p>0`.

### 6.2 Bounded support gives an upper endpoint

Because the offspring law is supported on `{2,3}`, monotone comparison with the deterministic ternary tree gives

`0<B<=u:=(3-lambda)/3`.                                         (6.8)

Indeed the regular ternary escape probability in the parent-bias convention is `(3-lambda)/3` for `lambda<3`.

Consequently

`E B/u >= r:=d/u`.                                               (6.9)

On the target rectangle,

`r>=269/350`,                                                    (6.10)

and when `p=1` one has `r=1` exactly.

### 6.3 Endpoint-chord lemma

Let `Y` be any random variable satisfying `0<=Y<=u` and `E Y>=r u`, and let `F:[0,u]->R` be convex and decreasing. Convexity gives the pointwise chord bound

`F(Y) <= (1-Y/u)F(0)+(Y/u)F(u)`.                                (6.11)

Taking expectations and using that `F(u)<=F(0)`,

`BOX: E F(Y) <= (1-r)F(0)+r F(u)`.                              (6.12)

For sums of independent copies, condition successively and iterate (6.12). Therefore for `j` iid sibling escapes and every convex decreasing function `F`,

`E F(B_1+...+B_j)`
` <= sum_{m=0}^j binom(j,m)r^m(1-r)^(j-m) F(mu)`.               (6.13)

Here the `m u` in the last expression is the deterministic endpoint sum; explicitly it is

`F(m u)`.

### 6.4 Differentiate the branch recursion directly in `U=-B'`

Differentiating

`B=S/(lambda+S)`

gives

`BOX: U = S/(lambda+S)^2`
`       + lambda sum_i U_i/(lambda+S)^2`.                       (6.14)

For a fixed child `i`, condition on `(B_i,U_i)` and on the other siblings only through their sum `T`. Dropping the nonnegative `B_i` from the denominator increases the coefficient of `U_i`:

`lambda/(lambda+B_i+T)^2 <= lambda/(lambda+T)^2`.               (6.15)

The function

`F_lambda(t)=lambda/(lambda+t)^2`                                (6.16)

is decreasing and convex. Define the exact endpoint-chord quantities

`K_j(lambda,p)`
` := sum_{m=0}^j binom(j,m) r^m(1-r)^(j-m)`
`      * lambda/(lambda+m u)^2`.                                (6.17)

Using (6.13) in (6.14), then averaging over `nu`, yields

`eta:=E U <= A + rho eta`,                                      (6.18)

where

`rho=(1-p)*2 K_1 + p*3 K_2`,                                   (6.19)

and for the inhomogeneous term we use the sharper deterministic support bound `S<=k u`:

`A=(1-p)*2u/(lambda+2u)^2 + p*3u/(lambda+3u)^2`.                (6.20)

The exact checker proves on the full target rectangle

`BOX: rho <=19/20<1`.                                           (6.21)

At the hard corner,

`rho =40506906573/43014760000`
`    =0.9416978398...`.                                         (6.22)

Therefore

`BOX: eta<=A/(1-rho)`.                                          (6.23)

This is the decisive distribution-sensitive derivative estimate. Unlike the old pointwise logarithmic derivative bound, it has no singularity at `lambda=2`.

## 7. Feed the annealed derivative estimate into the Aïdékon score

Put

`a=lambda-1>0`.

### 7.1 Upper bound for `h_2/c_2`

The `c_2,h_2` terms involve three iid branch escapes. Let

`S_3=B_1+B_2+B_3`.

By (6.8),

`S_3<=3u=3-lambda`,

so

`a+S_3<=2`.                                                      (7.1)

Hence

`c_2=(1/3)E[S_3/(a+S_3)] >= (1/6)E S_3 = mu/2 >= d/2`.          (7.2)

Split `h_2` into its escape part and its `U` part.

For the escape part, since `a+S_3>=a`,

`[ (1/3)E(S_3/(a+S_3)^2) ]/c_2 <=1/a`.                         (7.3)

For the `U` part, condition on one `U_i` and its associated `B_i`, drop `B_i` from the denominator, and apply (6.13) to the other two sibling escapes with

`F_a(t)=a/(a+t)^2`,                                              (7.4)

again decreasing and convex. Define

`K_c:=sum_{m=0}^2 binom(2,m)r^m(1-r)^(2-m)`
`       * a/(a+m u)^2`.                                         (7.5)

The `U` contribution to the numerator of `h_2` is at most `eta K_c`. Dividing by (7.2) gives

`BOX: h_2/c_2 <= 1/(lambda-1) + 2 eta K_c/d`.                  (7.6)

### 7.2 Lower bound for `h_3/c_3`

For the four-copy term defining `c_3,h_3`, discard the nonnegative `U` contribution in `h_3`. Since `S_4<=4u`, the remaining ratio is a weighted average of `1/(a+S_4)` and therefore

`BOX: h_3/c_3 >=1/(a+4u)=3/(9-lambda)`.                         (7.7)

Combining (6.23), (7.6), and (7.7),

`Delta <= D(lambda,p)`,                                         (7.8)

where

`D(lambda,p)`
` :=1/(lambda-1)`
`   +2[A/(1-rho)]K_c/d`
`   -3/(9-lambda)`.                                             (7.9)

Every quantity on the right is an explicit rational function of `(lambda,p)` on the target rectangle.

## 8. Locate the escape-tilted mixture coordinate and finish the sign

The inherited branch-addition inequality gives

`c_3/c_2 >=3/4`.                                                 (8.1)

Therefore

`theta = p c_3/[(1-p)c_2+p c_3]`
`      >= theta_0(p):=3p/(4-p)`.                                (8.2)

At the smallest allowed mixture weight `p=41/50`,

`theta_0=41/53`.                                                 (8.3)

The derivative numerator of

`g(theta)=theta(1-theta)/(2+theta)`

is

`2-4theta-theta^2`.                                              (8.4)

At `theta=41/53`, the exact value is

`-4755/2809<0`.                                                  (8.5)

Thus `g` is decreasing throughout the entire admissible theta range, and

`g(theta)<=g(theta_0(p))`.                                      (8.6)

The exact rational/Bernstein checker proves uniformly on

`41/50<=p<=1`, `19/10<=lambda<=54/25`

that

`BOX: lambda g(theta_0(p)) D(lambda,p) <=999/1000`.              (8.7)

Consequently

`lambda g(theta)Delta<=999/1000<1`.                             (8.8)

Substitution into the exact speed derivative identity gives

`-ell'_lambda`
` >= 2(2+theta)(1/1000)/(2+theta+lambda)^2`.                    (8.9)

Using `2(2+theta)>=4`, `theta<=1`, and `lambda<=54/25`,

`-ell'_lambda`
` >= (4/1000)/(3+54/25)^2`
` =5/33282`.                                                     (8.10)

Hence

`BOX: -ell'_lambda >=5/33282>0`

on the whole new rectangle.

Stitching with the inherited upper-tail theorem through `lambda=19/10` proves the clean restricted result

`BOX: if P(nu=2)=1-p, P(nu=3)=p and p>=41/50,`
`     then ell_lambda is strictly decreasing for 0<=lambda<=54/25.`

Equivalently, in child-bias variables the speed is strictly increasing on the reciprocal interval `beta>=25/54` covered by this theorem, subject to the same offspring restriction.

## 9. Attack 2 — direct `q=-B'/B` contraction is exactly too weak here

A second genuinely different route was to contract the logarithmic derivative

`q=-B'/B`

directly. Endpoint-chord compression does make its recursion contract at the hard corner, but only barely. The exact checker obtains at

`(lambda,p)=(54/25,41/50)`

`rho_q=316461394107/317581250000`
`     =0.9964737972...<1`.                                      (9.1)

The resulting uniform logarithmic-derivative bound is nevertheless enormous:

`M_q <=3969765625000/30236109111`
`    =131.2922112...`.                                          (9.2)

Feeding that into the same Aïdékon score control gives only

`lambda g(theta_0) Delta`
` <=2536558825754322254264/113861483872400266093`
` =22.27758448...>1`.                                           (9.3)

Thus this route is **rigorously insufficient at the hard corner**. The successful `U`-contraction is materially stronger because it preserves the escape weight attached to the derivative rather than dividing it out pathwise.

## 10. Attack 3 — near-critical Einstein relation gives no explicit bridge width here

For bounded offspring the exponential-moment hypothesis in the known Einstein-relation theorem is satisfied. The literature therefore supplies the correct derivative sign infinitesimally/locally near the critical parent bias `lambda=m=2+p` under its stated regularity framework.

However, the bounded primary-source check in this run did not recover an explicit numerical neighborhood width below `m`. Without such a width there is no rigorous way to claim that the near-critical region overlaps the new endpoint `lambda=2.16` uniformly for `p>=41/50`.

So this route is recorded as a known qualitative baseline, not as source movement. A future route could become effective if one quantitatively traces the constants in the Einstein-relation expansion or combines it with a finite-distance regeneration estimate.

## 11. Exact checks actually executed

The checker was executed with process exit code zero. The archived stdout records:

- exact rectangle extrema `d_min=269/1250`, `u_min=7/25`, `r_min=269/350`, and `r(p=1)=1`;
- a 20-coefficient exact Bernstein certificate for `rho<=19/20`, with positive numerator and denominator certificates;
- hard-corner value `rho=40506906573/43014760000`;
- exact `theta_min=41/53` and `g'` numerator `-4755/2809`;
- 70-coefficient exact Bernstein certificates for the main product inequality `lambda g(theta_0)D<=999/1000`;
- hard-corner product `253059277487793912468/254986301646138891227 =0.9924426365...`;
- exact derivative margin `5/33282`;
- exact direct-`q` obstruction values (9.1)–(9.3);
- final line `ALL_EXACT_CHECKS_PASS`.

The exact checker is a **self-check only**. No independent audit is claimed.

## 12. What remains for the full source problem

The full conjecture is much stronger: arbitrary no-leaf offspring laws and the whole interval `0<=lambda<E nu`.

Even within the present `{2,3}` family:

1. the all-mixture endpoint remains only `1.85527`;
2. central mixtures below `p=41/50` remain uncovered across `lambda=2` by this proof;
3. for `p>=41/50`, the interval from `lambda=2.16` to the mean boundary `2+p` is still open for this route, notwithstanding the known qualitative near-critical information.

The most promising next distinct mathematical target is to sharpen the annealed endpoint-chord contraction by retaining information beyond only the first moment `E B>=d`: e.g. a second inverse-escape moment, a lower bound on sibling overlap `E[B_1B_2/(B_1+B_2)^2]`, or a two-level occupation-weighted contraction. Those could reduce `rho` and the score `D` enough to move the central mixtures or push the upper tail toward the critical boundary.

## 13. Structured ledger delta

```yaml
ledger_delta:
  target: PROB10-06 / P0066 Lyons-Pemantle-Peres biased-walk speed monotonicity
  parent_status_before: OPEN
  parent_status_after: OPEN
  source_assumptions:
    no_leaves: "P(nu=0)=0"
    supercritical: "m=E nu>1"
    child_bias_beta: "outward; conjectured speed increase for beta>1/m"
    parent_bias_lambda: "lambda=1/beta; conjectured speed decrease for 0<=lambda<m"
  restricted_family: "P(nu=2)=1-p, P(nu=3)=p"
  all_mixture_endpoint_before: 1.85527
  all_mixture_endpoint_after: 1.85527
  restricted_upper_tail:
    p_range: "41/50<=p<=1"
    endpoint_before: "19/10"
    endpoint_after: "54/25"
    endpoint_gain: "13/50"
    new_strip: "19/10<=lambda<=54/25"
    crosses_lambda_2: true
    certified_sign_lower_bound: "-ell'_lambda >= 5/33282"
  auxiliary_delta:
    attack_1: "annealed inverse-escape + bounded-support convex endpoint-chord contraction for U=-B' succeeds and removes the lambda=2 pointwise singularity"
    attack_2: "direct q=-B'/B contraction has rho_q<1 but yields speed-product bound about 22.2776>1 at the hard corner; rigorously insufficient"
    attack_3: "known near-critical Einstein relation gives qualitative sign but no explicit neighborhood width recovered for certified stitching"
  exact_checker: "artifacts/prob10_2026-09-20/PROB10-06/20260920T0836Z_cross_lambda2_inverse_escape_chord_check.py"
  exact_output: "artifacts/prob10_2026-09-20/PROB10-06/20260920T0836Z_cross_lambda2_inverse_escape_chord_check.out"
  checker_result: ALL_EXACT_CHECKS_PASS
  audit_status: self_check_only
  novelty_status: UNVERIFIED
  remaining_full_scope_gap: "arbitrary no-leaf offspring laws and the full interval 0<=lambda<E nu; even {2,3} central mixtures are not bridged across lambda=2, and p>=41/50 remains open from 2.16 to 2+p"
```

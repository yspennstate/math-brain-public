Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED.** GPT-6/maximum was requested in prompt text only; no authenticated model-effort selector or applied reasoning telemetry is exposed here, so GPT-6/maximum is not claimed.

**SOURCE-WIDE STATUS: OPEN -> OPEN. SUBSTANTIVE MOVEMENT:** for the no-leaf two-point family `P(nu=2)=1-p, P(nu=3)=p`, the type-vector reciprocal escape recursion below (A) extends the `p>=3/4` parent-bias endpoint from `2.07` to `107/50=2.14`, with certified `-ell'_lambda >= 10/66049` on the analytic checker strip, and (B) at the same cross-barrier endpoint `lambda=20021/10000=2.0021` lowers the certified mixture threshold from `p>=71/100` to `p>=27/40`, with `-ell'_lambda >= 40000/2502100441`. The all-mixture endpoint remains `1.85527`. The full Lyons--Pemantle--Peres conjecture remains **OPEN/PARTIAL** and these restricted-family theorem candidates have not received the independent audits required for closure.

# PROB10-06 — type-vector harmonic-mean reciprocal recursion

## 1. Contract, preserved handoff, intake, ownership, and consumed updates

Controlling instruction: `operations/PROB10_2026-09-20.md` on `master`. Root `POSTED.md` was re-read during this run; it contains no posted source-wide resolution of P0066 and explicitly forbids treating a restricted theorem as closure. Historical intake `P0066` remains `attempted_un` / attempted-unsolved in the probability-1000 ledgers.

The required immutable handoff of R02's actual pre-refocus target already exists and is preserved, not duplicated:

- `runs/R02/20260920T0005Z_owner_refocus_handoff_I0095_to_PROB10-06_4d8c2a71.md`, blob `24734b748956373b8257a0b4f11f681f359b8afa`, creation commit `0439a90108047760ebd8d94ffd7d5b76463666da`.

It hands off Randomstrasse/I0095 and preserves all old R02 artifacts. None is relabelled as biased-walk progress.

Immediate own checkpoint consumed:

- `runs/prob10_2026-09-20/PROB10-06/20260920T1112Z_reciprocal_jensen_cross_lambda2_71pct_7f3c2a91.md`, blob `c661d1432b3e8e8d477505cfb746306c7a32405a`, creation/readback commit `cc8dd4a233b5d3eb2949b39eb3c74cd050a4250d`.

That report gives the all-mixture `{2,3}` endpoint `1.85527`, `p>=3/4` through `2.07`, and `p>=71/100` through `2.0021`, using a **scalar** reciprocal-moment bound followed by reciprocal Jensen. The present run does not call any of those statements new; it sharpens only the reciprocal-moment input.

Complementary current same-source work was consumed at the observed master snapshot `fb784126f8ef8f04853a559112fc4c58ef840514` and kept ownership-disjoint:

- `proofnet24/P01-progress-speed/runs/2026-09-20/2026-09-20T10-01-39Z__run-report.md`: minimum-offspring-one nonadjacent laws below `lambda=1`;
- `proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T10-21-46Z__type-conditioned-branch-ratio-crosses-lambda3.md`: the distinct `{3,4}` family, currently crossing `lambda=3` for a broad upper tail;
- `probability_campaigns/progress_first_2026-09-20/P03/analytic/2026-09-20T0906Z__sharp-von-bahr-esseen-restores-all-mean-third-moment-terminal-theorem.md`: a corrected finite-third-moment **terminal-neighborhood** theorem near `lambda=m`; the withdrawn `0800Z` proof is not used;
- P03-B's coupling route remains separate and is not overwritten.

The old intake observation that for fixed local degree `k` the one-step drift `(k-lambda)/(k+lambda)` decreases in `lambda` is already marked attempted and is not novelty: the environment seen from the particle depends on `lambda`.

Idea-before-code artifact, written and read back before the checker:

- `artifacts/prob10_2026-09-20/PROB10-06/20260920T1105Z_type_vector_harmonic_mean_idea_6f4a2d91.md`, blob `d625580561f45e12594fe56005fc3bc28d847e38`, creation/readback commit `7e48e2df7b4c5c35a4f655b5ea5d760783fc4c75`.

Exact checker and archived output:

- `artifacts/prob10_2026-09-20/PROB10-06/20260920T1218Z_type_vector_reciprocal_check.py`, blob `6de5e0523aa47922cbf42fe96b9e2cc197b5b13d`, creation/readback commit `951979682452b5ca9aaa7eeb2850250a8f480fc0`;
- `artifacts/prob10_2026-09-20/PROB10-06/20260920T1218Z_type_vector_reciprocal_check.out`, blob `5325898f99df85dc74833701b22473c7b350ed3a`, creation/readback commit `0051663ada5abdc2befd27659f14afbee5ce9f5b`.

No scheduler, email, Drive, public-posting, permissions, workflow, or peer-track state was changed.

## 2. Exact source problem and bias convention

Let `nu` be the Galton--Watson offspring variable. The source assumptions are

`P(nu=0)=0`, `m=E nu in (1,infinity)`.

Thus there are **no leaves**. In the source child-bias convention, if a vertex has `k` children,

`P_beta(parent)=1/(1+beta k)`,
`P_beta(each fixed child)=beta/(1+beta k)`.

Hence increasing `beta` pushes **away from the root**. The exact original conjectured transient interval is

`beta in (1/m,infinity)`,

and Lyons--Pemantle--Peres conjectured that the limiting speed is increasing there.

This report uses reciprocal **parent bias**

`lambda=1/beta`,

so

`P_lambda(parent)=lambda/(lambda+k)`,
`P_lambda(each fixed child)=1/(lambda+k)`.

Increasing `lambda` pushes toward the root. The source conjecture is therefore equivalent on the transient interior to nonincrease of `ell_lambda` on

`lambda in (0,m)`

(with the usual limiting endpoint formulation on `[0,m]`). The target derivative sign here is `ell'_lambda<0`.

The restricted family for this run is

`P(nu=2)=1-p`, `P(nu=3)=p`, `0<=p<=1`,

with `m=2+p`. Every asserted endpoint below is strictly less than `m` on its parameter range.

## 3. Primary-source/current-literature boundary refreshed

A bounded current check on 20 September 2026 recovered:

1. Ben Arous--Fribergh--Sidoravicius, arXiv:1111.5865, which explicitly assumes `P(Z=0)=0`, defines the outward child-bias convention above, states transience for `beta>1/EZ`, records the LPP conjecture on `(1/EZ,infinity)`, and proves the historical high-bias baseline `beta>=717` (with the minimum-degree refinement `717/d`).
2. Aidekon, arXiv:1111.4313 / PTRF 159 (2014), which supplies the exact invariant-environment speed representation used below.
3. Song--Wang--Xiang, arXiv:1610.08151, now *Journal of Applied Probability* 62 (2025), 1044--1052, published online 5 March 2025: for minimum offspring `m1>=2`, strict parent-bias decrease on

   `0<=lambda<=m1/(1+sqrt(1-1/m1))`.

   It also records Aidekon's earlier `lambda<=1/2` improvement. These are baselines, not novelty.
4. Bowditch--Tokushige's differentiability/analyticity papers remain regularity context rather than sign results.
5. A bounded current 2025--2026 search found the 2026 deterministic regular-tree paper of Song--Liu but no checked source-wide LPP resolution and no checked theorem identical to either random `{2,3}` rectangle below. This is negative evidence only, **not** a novelty certificate.

## 4. Source before/after metric and auxiliary deltas

### Full source

Before: **OPEN**.  
After: **OPEN**.

No arbitrary-offspring theorem on the full transient interval is claimed.

### All-mixture `{2,3}` metric

Before: every `p in [0,1]` certified through `lambda=1.85527`.  
After: unchanged at `1.85527`.

### Upper-tail endpoint metric

Before:

`p>=3/4 => strict decrease through lambda=2.07`.

After:

`BOX A: p>=3/4 => strict decrease through lambda=107/50=2.14`.

Endpoint gain: `+0.07`.

On the checker strip `1.85527<=lambda<=2.14`,

`BOX: -ell'_lambda >= 10/66049 >0`.

The genuinely new region after subtracting predecessor coverage contains

`p>=3/4, 2.07<lambda<=2.14`.

### Fixed cross-barrier endpoint metric

At the same endpoint used in the immediate predecessor,

`lambda=20021/10000=2.0021`,

before the certified threshold was `p>=71/100`. After:

`BOX B: p>=27/40 => strict decrease through lambda=20021/10000`.

Thus the minimum certified mixture weight at this fixed endpoint moves

`71/100 -> 27/40`,

a downward gain of `7/200=0.035`.

On `1.85527<=lambda<=2.0021`, `p>=27/40`,

`BOX: -ell'_lambda >= 40000/2502100441 >0`.

The genuinely new region includes

`27/40<=p<71/100, 1.85527<=lambda<=2.0021`.

### Auxiliary mechanism delta

Before: one scalar bound on `E(1/B)` was converted to two conditional bounds by Cauchy.

After: a **two-coordinate conditional reciprocal-moment supersolution** is iterated through the exact harmonic-mean escape recursion. This retains offspring-type heterogeneity instead of collapsing it before Jensen. The same exact check gives `rho<19/20` on both new rectangles and therefore the certified finite-depth escape truncation bound

`BOX: E[B_N-B] <= (19/20)^N`.

## 5. Escape recursion in reciprocal coordinates

Let `B=B_lambda` be the quenched probability, starting from a branch root, of escaping to infinity before hitting its artificial parent. If that root has `nu=k` children with iid child escapes `B_1,...,B_k`, then

`B=S/(lambda+S)`, `S=sum_i B_i`.                                (5.1)

Set

`Z=1/B`.

Then exactly

`Z=1+lambda H_k(Z_1,...,Z_k)`,                                  (5.2)

where

`H_k(z_1,...,z_k):=1/(sum_i z_i^{-1})`.                         (5.3)

This is the parallel/harmonic sum, not the normalized harmonic mean.

### Lemma 5.1 — `H_k` is increasing and jointly concave

It is coordinatewise increasing. Let `H=H_k(z)` and `v in R^k`. Direct differentiation gives

`v^T D^2 H(z) v`
`=2 H^2 { H (sum_i v_i/z_i^2)^2 - sum_i v_i^2/z_i^3 }`.        (5.4)

By Cauchy,

`(sum_i v_i/z_i^2)^2`
` <= (sum_i z_i^{-1})(sum_i v_i^2/z_i^3)`
` = H^{-1} sum_i v_i^2/z_i^3`.                                 (5.5)

Hence (5.4) is nonpositive. Therefore `H_k` is jointly concave. QED.

## 6. New type-vector reciprocal-moment lemma, proved through finite-depth truncations

Use the finite-depth escape approximation with terminal value `B_0=1` and recursion (5.1). Then `B_N downarrow B`; equivalently `Z_N=1/B_N uparrow Z`.

For `k=2,3` define

`x_{k,N}:=E[Z_N | nu=k]`.                                       (6.1)

Conditioning first on the child offspring types `R_i in {2,3}`, then applying Lemma 5.1, yields

`x_{k,N+1} <= T_{lambda,p,k}(x_{2,N},x_{3,N})`,                 (6.2)

where

`T_{lambda,p,k}(y_2,y_3)`
` :=1+lambda E_p[ H_k(y_{R_1},...,y_{R_k}) ]`.                  (6.3)

No infinite-depth integrability is assumed here; (6.2) is first proved for finite `N`.

### Lemma 6.1 — explicit corner supersolution

Fix a parameter rectangle

`lambda<=L`, `p>=P`.                                             (6.4)

Put

`a_P=E_P(1/nu)=(3-P)/6`,
`D=1-L a_P`, `M=1/D`,                                           (6.5)

and assume `D>0`. Define

`y_2^(0)=1+L M/2`, `y_3^(0)=1+L M/3`.                           (6.6)

Then `y^(0)` is a supersolution of `T_{L,P}`.

Proof. For positive `z_i`, Cauchy gives

`H_k(z_1,...,z_k) <= k^{-2} sum_i z_i`.                         (6.7)

Moreover

`E_P[y_R^(0)]`
`=1+LM[(1-P)/2+P/3]`
`=1+LM a_P=M`.                                                   (6.8)

Therefore

`T_{L,P,k}(y^(0)) <= 1+LM/k=y_k^(0)`.                           (6.9)

QED.

Because `T` is monotone in the vector, every exact iterate

`y^(r+1)=T_{L,P}(y^(r))`                                        (6.10)

is again a smaller supersolution. Also `y_2>=y_3`: initially this is clear, and `H_3` is at most the corresponding two-input harmonic sum because its reciprocal denominator has one extra positive term.

For vectors with `y_2>=y_3`, increasing `p` stochastically replaces the larger coordinate `y_2` by the smaller coordinate `y_3`; since `H_k` is coordinatewise increasing,

`T_{lambda,p}(y) <= T_{L,P}(y)` whenever `lambda<=L, p>=P`.     (6.11)

Thus any supersolution produced at the corner `(L,P)` dominates the entire rectangle.

The checker performs 30 such iterations. To keep exact rational numerators/denominators controlled, after computing the exact `t=T(y)` it rounds each coordinate **up** to the nearest multiple of `10^{-9}`, never above the preceding supersolution. If `z` is this rounded vector, then

`t<=z<=y`,

and monotonicity gives

`T(z)<=T(y)=t<=z`.                                               (6.12)

So every rounded iterate remains an exact supersolution; no floating-point sign enters.

Since `x_{k,0}=1<=y_k`, (6.2) and induction give `x_{k,N}<=y_k` for all `N`. Monotone convergence therefore gives

`BOX: E[1/B | nu=k] <= y_k, k=2,3`.                             (6.13)

By reciprocal Jensen,

`BOX: E[B | nu=k] >= d_k:=1/y_k`.                               (6.14)

This is the new input absent from the scalar predecessor.

## 7. Reciprocal-Jensen kernel bound with the sharper type vector

For `a>0`, `t>=0`, let

`F_{a,t}(B)=a/(a+t+B)^2`.                                       (7.1)

Writing `Z=1/B`,

`G_{a,t}(Z)=F_{a,t}(1/Z)=aZ^2/((a+t)Z+1)^2`.                    (7.2)

Direct differentiation gives

`G' = 2aZ/((a+t)Z+1)^3 >=0`,                                   (7.3)

`G''=2a[1-2(a+t)Z]/((a+t)Z+1)^4`.                              (7.4)

On the checker strips, `a` is either `lambda` or `lambda-1`; the smallest possible base is `1.85527-1>1/2`, while `Z>=1`. Thus `G` is increasing and concave throughout every application. Conditional Jensen and (6.13) give

`E[F_{a,t}(B)|nu=k] <= a/(a+t+d_k)^2`.                          (7.5)

For independent branch escapes define `w_2=1-p`, `w_3=p` and

`K_1(a)=a w_2/(a+d_2)^2 + a w_3/(a+d_3)^2`,                    (7.6)

`K_2(a)=a w_2^2/(a+2d_2)^2`
`       +2a w_2w_3/(a+d_2+d_3)^2`
`       +a w_3^2/(a+2d_3)^2`.                                  (7.7)

Sequential conditional Jensen proves that the true one- and two-sibling kernels are bounded above by (7.6)--(7.7).

## 8. Differentiated escape recursion and certified denominator/truncation control

Let

`U=-partial_lambda B`.

Differentiating (5.1) at finite depth gives exactly

`U = S/(lambda+S)^2 + lambda sum_i U_i/(lambda+S)^2`.           (8.1)

There is no assumed sign for a speed derivative here; (8.1) is the differentiated branch recursion.

Because the offspring support is at most three, if `b=ess sup B`, then

`b <= 3b/(lambda+3b)`,

hence on `lambda<3`

`B <= u:=(3-lambda)/3`.                                         (8.2)

On our strips `lambda>1.85`, every possible child sum satisfies `S<lambda`, so `s/(lambda+s)^2` is increasing over the relevant range. For current offspring 2 and 3 respectively this yields source bounds

`6(3-lambda)/(lambda+6)^2`,
`(3-lambda)/9`.                                                  (8.3)

Put

`A=(1-p) 6(3-lambda)/(lambda+6)^2 + p(3-lambda)/9`,             (8.4)

`rho=(1-p) 2 K_1(lambda)+p 3 K_2(lambda)`.                      (8.5)

For a fixed child derivative term in (8.1), dropping that child's own nonnegative `B_i` from the denominator leaves a function of independent siblings; (7.6)--(7.7) therefore apply. With `eta=E U`,

`eta <= A+rho eta`.                                              (8.6)

The exact checker proves on **both** new rectangles

`BOX: rho<19/20`.                                                (8.7)

Thus

`eta <= A/(1-rho)`.                                              (8.8)

The same coefficient gives the promised truncation control. Couple the finite-depth upper escape `B_N` and the infinite escape `B` on the same tree. Apply the mean-value formula to (5.1), drop the varied child's own escape in each partial derivative, and use (7.6)--(7.7) on the siblings. If `e_N=E(B_N-B)`, then

`e_{N+1} <= rho e_N`, `e_0<=1`.                                 (8.9)

Consequently

`BOX: E[B_N-B] <= (19/20)^N`.                                   (8.10)

This is an actual denominator/truncation estimate, not an assumed infinite-depth derivative sign. Uniform finite-depth derivative bounds from (8.6), together with (8.10) and the fact that all denominators below are bounded away from zero by `lambda-1>0.855`, justify passage to the infinite-depth derivative formulas; equivalently, this is the same dominated finite-depth passage proved in the immediate reciprocal-Jensen predecessor, with strictly sharper inputs.

## 9. Aidekon speed reduction and score bound

For current degree `k`, let `B_0,...,B_k` be iid branch escapes and

`S_k=sum_{i=0}^k B_i`, `D_k=lambda-1+S_k`.                      (9.1)

Define

`c_k=E[(1/(k+1)) S_k/D_k]`,                                    (9.2)

`h_k=E[(1/(k+1)) sum_i (B_i+(lambda-1)U_i)/D_k^2]`.             (9.3)

Then `c'_k=-h_k`. Let

`C=(1-p)c_2+p c_3`,
`theta=p c_3/C`,
`M=2+theta`.                                                     (9.4)

Aidekon's symmetrized formula is

`ell_lambda=(M-lambda)/(M+lambda)`.                              (9.5)

Writing

`Delta=h_2/c_2-h_3/c_3`,                                       (9.6)

one has

`theta'=theta(1-theta)Delta`,                                  (9.7)

and therefore

`BOX: -ell'_lambda`
`= 2(2+theta)/(2+theta+lambda)^2`
`  * [1-lambda g(theta) Delta]`,                                (9.8)

where

`g(theta)=theta(1-theta)/(2+theta)`.                            (9.9)

It remains to bound `Delta`.

First, the escape-only part of `h_2/c_2` is at most `1/(lambda-1)`. For the derivative part, discard `B_0` from its denominator and apply `K_2(lambda-1)`. Also from (8.2),

`D_2 <= lambda-1+3u=2`,

so, with

`mu=(1-p)d_2+p d_3 <= E B`,                                    (9.10)

we have `c_2>=mu/2`. Hence

`h_2/c_2`
` <= 1/(lambda-1)+2 eta K_2(lambda-1)/mu`.                      (9.11)

For degree 3, discard the nonnegative derivative part in `h_3`. The ratio of its escape numerator to `c_3` is a positive weighted average of `1/D_3`. Since

`D_3<=lambda-1+4u=(9-lambda)/3`,                                (9.12)

we get

`h_3/c_3 >= 3/(9-lambda)`.                                      (9.13)

Therefore

`BOX: Delta <= 1/(lambda-1)`
` +2 [A/(1-rho)] K_2(lambda-1)/mu`
` -3/(9-lambda)`.                                               (9.14)

This is the exact quantity interval-evaluated by the checker.

Finally, couple `S_4=S_3+B_4` and put `f(s)=s/(lambda-1+s)`, which is increasing. From (9.2),

`c_3=(1/4)E f(S_4) >= (1/4)E f(S_3)=(3/4)c_2`.                 (9.15)

Hence

`theta >= 3p/(4-p)`.                                             (9.16)

For `p>=27/40`, the right side is larger than `sqrt(6)-2`, while

`g'(theta)` has sign `2-4theta-theta^2`.                         (9.17)

Thus `g` is decreasing throughout the allowed tilted range, and on any checker subbox with lower mixture endpoint `P`,

`g(theta) <= g(3P/(4-P))`.                                      (9.18)

Equations (6.13), (7.5), (8.4)--(8.8), and (9.14)--(9.18) are all rational inequalities after the type-vector supersolution is fixed.

## 10. Exact certification of the two new rectangles

The checker uses outward-rounded rational interval arithmetic only. For each adaptive parameter subbox it constructs the `(L,P)` type-vector supersolution with 30 exact harmonic iterations and upward grid `10^{-9}`, then evaluates (7.6)--(9.18) with rational intervals. A broad box that cannot certify a sign is subdivided; no floating-point value decides acceptance.

### Rectangle A

`lambda in [1.85527,107/50]`, `p in [3/4,1]`.

The checker visits `1997` subboxes, accepts `999`, maximum depth `23`, and proves

`lambda g(theta) Delta < 999/1000`,
`rho<19/20`.                                                     (10.1)

Its largest certified interval upper endpoints, shown only as diagnostics after the exact decisions, are

`product < 0.998993473087026`,
`rho < 0.949302479790497`.

From (9.8), using `2+theta>=2` and `2+theta+lambda<=3+107/50`,

`-ell'_lambda`
` >= 4(1-999/1000)/(3+107/50)^2`
` = 10/66049 >0`.                                               (10.2)

### Rectangle B

`lambda in [1.85527,20021/10000]`, `p in [27/40,1]`.

The checker visits `4613` subboxes, accepts `2307`, maximum depth `28`, and proves

`lambda g(theta) Delta < 9999/10000`,
`rho<19/20`.                                                     (10.3)

Diagnostic upper endpoints are

`product < 0.999899424306252`,
`rho < 0.949724435033093`.

Therefore

`-ell'_lambda`
` >= 4(1-9999/10000)/(3+20021/10000)^2`
` = 40000/2502100441 >0`.                                       (10.4)

The archived output ends `ALL_EXACT_CHECKS_PASS`.

## 11. Three genuinely different attacks and their outcomes

The idea file was written before code. The three routes were deliberately not three variants of the same interval check.

### Attack A — reciprocal type-vector recursion: SUCCESS

Owner-directive moves #18 (rewrite in another language), #5 (add a parameter and differentiate), and #4 (prove a smaller exact theorem) were combined. The scalar variable `E(1/B)` was replaced by the conditional vector `(E[1/B|nu=2],E[1/B|nu=3])`. Joint concavity of the harmonic-sum recursion makes the vector close under a monotone supersolution iteration. This yields the two quantitative gains in Section 4.

### Attack B — exact harmonic-mean deficit: BLOCKED BEYOND ATTACK A

For two inputs there is the exact identity

`H_2(z_1,z_2)`
`=(z_1+z_2)/4-(z_1-z_2)^2/[4(z_1+z_2)]`.                        (11.1)

This exposes precisely what scalar Cauchy discards. Conditioning on offspring types already captures the deterministic between-type part through Attack A. A further uniform gain would require a positive lower bound on the **within-type** deficit. Such a bound is impossible over the whole upper-tail class: at `p=1` the tree is deterministic 3-ary, `Z` is deterministic, and the deficit in (11.1) is exactly zero. The checker records this endpoint obstruction exactly. Thus a future variance-deficit improvement must vanish correctly as `p->1` or use a nonuniform law-dependent term; one cannot subtract a fixed positive deficit uniformly on `p in[P,1]`.

### Attack C — splice to the terminal-critical theorem: NOT YET ADMISSIBLE AS A BRIDGE

The corrected P03-A report `.../2026-09-20T0906Z__sharp-von-bahr-esseen-restores-all-mean-third-moment-terminal-theorem.md` applies to `{2,3}` because the offspring law has finite third moment, and proves existence of a terminal interval immediately below `lambda=m`. This is a genuinely different critical-smoothing route and could eventually join the present intermediate interval.

However its current theorem obtains `delta_*>0` after several shrinkages involving constants `C_i`; it does not instantiate a numerical terminal width. The report itself identifies quantitative terminal width as a next task. Therefore it is **not rigorous** to assert that its unspecified interval overlaps `lambda<=2.14`. No splice/closure is claimed. The exact next obligation on this route is to expose the constants in the corrected `W_{3/2}` contraction and prove an explicit lower endpoint `m-delta_*<=2.14` for some nontrivial `p` range.

## 12. Remaining source-wide gap

The source problem remains open for arbitrary no-leaf offspring laws and for large portions of the full transient interval. Even inside `{2,3}`, the current all-mixture theorem stops at `1.85527`; the new type-vector route crosses `lambda=2` only for sufficiently large `p`, and the terminal theorem has not yet been quantitatively spliced to it.

The immediate method-level obstruction is now sharper than the old artificial pole `1/(2-lambda)`: the type-vector annealed contraction remains finite through `lambda=2`, but the certified Aidekon score product reaches one in the central/smaller-`p` region. The next useful attack should therefore retain additional joint information between reciprocal escape `Z` and derivative mass `U`, or make the terminal-critical constants explicit enough to bridge from the other side. Merely adding more finite-depth simulations cannot settle the source problem.

Status remains **PARTIAL / OPEN parent** pending source-wide proof and the required independent validation.
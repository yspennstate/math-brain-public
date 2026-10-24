Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6/maximum was requested, but no authenticated applied model/reasoning metadata is exposed, so I do not claim GPT-6.**

# P04 T10 — length-8 exact ladder optimization extends the certified FPP strict-triangle cone to slope 907/500

Date: 2026-09-20 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Controlling policy: `operations/PROGRESS20_2026-09-20.md`.  
Parent source: Auffinger–Damron–Hanson, *50 years of first passage percolation*, arXiv:1511.03262, Question 4.  
Model: nearest-neighbor **undirected** FPP on `Z^2` with iid physical-edge weights `Exp(1)`.  
Parent status after this run: **PARTIAL / OPEN**. Full strict convexity is not proved.

## 0. Brief immutable handoff of the actual preceding P04 target

The pre-T10 P04 assignment was intake `I0101`, Bandeira Randomstrasse Conjecture 27. Its completed six-run handoff remains at

`proofnet24/P04-closure-local-paley/runs/2026-09-18/2026-09-18T13-49-33Z__rotation-stop-disabled.md`.

That report preserves the source as **PARTIAL / OPEN**, with exact finite prime frontier `4177` and tested domain

`{149,257,1009,4001,4013,4021,4049,4057,4073,4093,4129,4133,4153,4157,4177}`.

Nothing in I0101 is reopened here. The older personal squared-ridge/kernel package is retired and excluded by `POSTED.md`; no kernel claim is touched.

## 1. What was read and how this run avoids duplication

Essential repository state consumed before the new proof:

- `operations/PROGRESS20_2026-09-20.md`;
- root `POSTED.md` exclusions;
- canonical parent `operations/claims/PROB10-10.md`;
- newest P04 report `proofnet24/P04-progress-curvature/runs/2026-09-20/2026-09-20T03-46-21Z__wide-cone-strict-triangle.md`;
- newest P20 companion report found at start of this run, `proofnet24/P20-progress-fpp/runs/2026-09-20/2026-09-20T04-08-54Z__p04-wide-cone-residual-bootstrap.md`;
- newest canonical PROB10-10 report found at start of this run, `runs/prob10_2026-09-20/PROB10-10/20260920T0416Z__cone-tilt-15over8-extension.md`;
- canonical summaries of the R07/R08 FPP history.

The current best repository cone before this run was therefore **not** P04's original slope `2`: the canonical owner had already consumed P04's length-6 axis bound and reoptimized the non-backtracking certificate to prove a strict reflected-triangle defect for

\[
|y|\ge \frac{15}{8}x=1.875x.
\]

P20, meanwhile, had converted the P04 slope-2 theorem into an asymmetric two-cone family and finite Bellman-residual statement. This run does not duplicate either result. Its new ingredient is a strictly better **dependence-safe axis block optimization** on a 27-vertex length-8 ladder, then a retuning of the already-certified non-backtracking transfer that pushes the covered reflected cone strictly inward past `15/8`.

The old R08 failure modes remain binding and are not reset:

1. local detour savings can share one bypass, invalidating naive independent multiplication of local margins;
2. positive-probability finite cylinders can realize exact finite triangle equality, so pointwise finite strictness is unavailable;
3. old fixed-corner blocks did not cross the axis/diagonal threshold;
4. R07's fluctuation/KPZ work did not prove curvature and cannot be imported as such.

The proof below avoids all four: its finite block is used only for an **expectation upper bound** transferred by pathwise concatenation, and its lower bound counts every possible self-avoiding competitor rather than multiplying local surgery events.

## 2. Source-level and mechanism-level metrics

Write `mu` for the deterministic FPP time-constant norm.

### Original source problem

Full strict convexity of the Exp(1) limit shape:

- before: **OPEN**;
- after: **OPEN / PARTIAL**.

The separate canonical axis/diagonal milestone

\[
\Delta_{12}=2\mu(e_1)-\mu(1,1)
\]

remains `c_*=0 -> 0` in the canonical track. This report does not claim otherwise.

### Restricted-direction source metric

Before this run, the repository had a certified reflected cone

\[
|y|\ge \frac{15}{8}x.
\]

After this run, the certified cone is enlarged to

\[
\boxed{|y|\ge \frac{907}{500}x=1.814x.}
\tag{2.1}
\]

For every `x>0` in this cone the new exact normalized strict-triangle defect is

\[
\boxed{
\mu(x,y)+\mu(x,-y)-\mu(2x,0)
\ge \delta_8 x,
}
\tag{2.2}
\]

where

\[
\boxed{
\delta_8=
\frac{68977908882155446326458294510291016568757618382301}
{3718960855166042798264926188889970206310400000000000000}
=1.854762971929043\times10^{-5}
>10^{-5}.
}
\tag{2.3}
\]

The same statement holds under simultaneous `D_4` rotations/reflections.

### Mechanism metric

P04's preceding exact axis block used `[0,6]x[-1,1]` and gave

\[
\mu(e_1)\le 0.6453933351799015\ldots.
\]

This run replaces it by the exact length-8 block and proves

\[
\boxed{
\mu(e_1)\le a_8
:=
\frac{4688722489067361283750127182134186345695457354381617699}
{7437921710332085596529852377779940412620800000000000000}
=0.6303807261851404\ldots.
}
\tag{2.4}
\]

The finite-to-infinite interface error for this upper transfer is exactly zero in expectation at every concatenated scale.

For the oblique lower transfer, an explicit finite error is retained. Put

\[
c=\frac{63039}{100000}=0.63039,
\qquad
\widehat\beta=\frac{12497}{12500}=0.99976,
\tag{2.5}
\]

and

\[
C=\frac{26633487052538711}{2329665975000}
=11432.320057187044\ldots.
\tag{2.6}
\]

For every integer `a>=1`, every integer `b` with `b/a>=907/500`, and every `n>=1`,

\[
\boxed{
\Pr\!\left(T(0,n(a,b))\le can\right)
\le C\widehat\beta^{an}.
}
\tag{2.7}
\]

Consequently, for every `n` divisible by `4`, the finite expected triangle residual defined in Section 6 obeys

\[
\boxed{
\frac{\mathbb E\mathcal R_{a,b,n}}{an}
\ge
\delta_8-2cC\widehat\beta^{an}.
}
\tag{2.8}
\]

At the explicit common scale `n=90000`, the exact checker proves, uniformly for every `a>=1` and `b/a>=907/500`,

\[
\boxed{
\frac{\mathbb E\mathcal R_{a,b,90000}}{90000a}>10^{-5}.
}
\tag{2.9}
\]

Thus this report gives both a positive infinite-volume defect and a completely explicit finite-scale error budget.

## 3. Exact length-8 ladder optimization

Let

\[
R_8=[0,8]\times[-1,1]\cap\mathbb Z^2
\]

with all nearest-neighbor physical edges having both endpoints in `R_8`. Let `M_8` be the internal FPP distance from `(0,0)` to `(8,0)`.

The executed exact checker

`proofnet24/P04-progress-curvature/artifacts/2026-09-20/2026-09-20T04-47-14Z__cone1814-exact.py`

uses only Python `Fraction` arithmetic. It explores `1,649,609` reachable infection states on the 27-vertex graph and obtains

\[
\boxed{
\mathbb E M_8
=
\frac{4688722489067361283750127182134186345695457354381617699}
{929740213791510699566231547222492551577600000000000000}.
}
\tag{3.1}
\]

### Exactness of the recursion

For an infected vertex set `S` not containing the target, let `b(S)` be the number of physical edges from `S` to its complement and let `r_S(v)` be the number of such boundary edges ending at an outside vertex `v`.

Conditional on the infection history up to `S`, memorylessness of iid rate-one exponentials implies that the residual clocks on all `b(S)` boundary edges are independent `Exp(1)`. Hence the next infection waiting time has mean `1/b(S)`, and the probability the next infected vertex is `v` equals `r_S(v)/b(S)`. Therefore the expected remaining hitting time satisfies exactly

\[
E(S)=\frac1{b(S)}+
\sum_{v\notin S}\frac{r_S(v)}{b(S)}E(S\cup\{v\}),
\tag{3.2}
\]

with `E(S)=0` when the target is infected. Every recursion step strictly increases `|S|`, so backward induction uniquely determines the exact expectation. Equation (3.1) is therefore a finite exact theorem, not simulation.

## 4. Dependence-controlled block-to-infinite-volume transfer

Translate `R_8` by `8j e_1`. Let `M_j` denote the internal minimum passage time from `8j e_1` to `8(j+1)e_1` within that translated ladder.

For every environment and every integer `N>=1`, concatenate one minimizing ladder path from each block. This gives a walk from `0` to `8Ne_1`; deleting loops cannot increase its weight. Thus pathwise

\[
T(0,8Ne_1)\le\sum_{j=0}^{N-1}M_j.
\tag{4.1}
\]

Adjacent blocks share their boundary column (and corresponding physical randomness), so the `M_j` are **not assumed independent**. Translation invariance alone gives `E M_j=E M_8`, and linearity of expectation yields

\[
\frac{\mathbb E T(0,8Ne_1)}{8N}
\le\frac{\mathbb E M_8}{8}=a_8
\qquad(N\ge1).
\tag{4.2}
\]

Standard `L^1` convergence of FPP passage times along a fixed direction now gives

\[
\mu(e_1)\le a_8.
\tag{4.3}
\]

This is the requested dependence-controlled block optimization: there is no independence approximation and no asymptotic interface correction to estimate.

## 5. Oblique lower bound on the cone `b/a >= 907/500`

This section deliberately reuses the **already current canonical** non-backtracking transfer certificate from the `15/8` report, re-verifies it exactly, and retunes only the threshold needed to exploit the stronger axis block. The certificate itself is not relabeled as a new P04 claim.

Set

\[
A=\frac{189}{100},\qquad B=\frac{291}{100},
\]

and give directions `(E,W,N,S)` weights

\[
w=(A,A^{-1},B,B^{-1}).
\tag{5.1}
\]

Let `M` be the non-backtracking transfer matrix

\[
M_{ij}=\mathbf 1\{j\neq-i\}w_j.
\tag{5.2}
\]

Take

\[
z=\left(
\frac{2095936}{10^6},
\frac{1469509}{10^6},
\frac{2181303}{10^6},
1
\right)^T,
\qquad
r=\frac{5083}{1000}.
\tag{5.3}
\]

The exact checker verifies componentwise `Mz<=rz`; the four exact ratios are

\[
\frac{309989303407}{60991737600},\quad
\frac{13692463648609}{2694050849700},\quad
\frac{209533503553}{41226626700},\quad
\frac{582356870377}{114581250000},
\tag{5.4}
\]

and each is at most `5083/1000`. Every coordinate of `z` is at least one. Hence if `W_m` is the total tilted weight of all length-`m` non-backtracking direction sequences,

\[
W_m=w^TM^{m-1}{\bf1}
\le w^TM^{m-1}z
\le (w^Tz)r^{m-1}
=Kr^m,
\tag{5.5}
\]

where

\[
K=\frac{20954749844641}{9318663900000}.
\tag{5.6}
\]

Fix an endpoint `n(a,b)` with positive integers `a,b`. Every path to this endpoint has tilted step product `A^{an}B^{bn}`. Therefore the number `N_m` of self-avoiding paths of length `m` to the endpoint satisfies

\[
N_m\le Kr^mA^{-an}B^{-bn}.
\tag{5.7}
\]

A self-avoiding path uses distinct physical edges, so its total weight is a sum of `m` independent rate-one exponentials. For `s>0`, Chernoff gives

\[
\Pr(S_m\le can)\le e^{scan}(1+s)^{-m}.
\tag{5.8}
\]

Choose

\[
s=\frac{1021}{250},\qquad c=\frac{63039}{100000},
\qquad q:=\frac r{1+s}=\frac{5083}{5084}<1.
\tag{5.9}
\]

If unrestricted passage time is at most `can`, a minimizing path may be taken self-avoiding because all weights are positive. Every such path has at least `(a+b)n` edges. Summing (5.7)--(5.8) over all admissible lengths therefore gives

\[
\Pr(T(0,n(a,b))\le can)
\le
C\,[\beta(b/a)]^{an},
\tag{5.10}
\]

where

\[
C=\frac K{1-q}
=
\frac{26633487052538711}{2329665975000},
\tag{5.11}
\]

and

\[
\beta(\rho)
=A^{-1}B^{-\rho}e^{sc}q^{1+\rho}.
\tag{5.12}
\]

Because `B>1` and `q<1`, `beta(rho)` is strictly decreasing in `rho`.

### Exact certification at `rho=907/500`

Put

\[
\rho_0=\frac{907}{500},\qquad
\widehat\beta=\frac{12497}{12500}.
\tag{5.13}
\]

It remains to certify `beta(rho_0)<beta_hat` without floating-point exponentials. Let `x=sc`. Write the degree-20 Taylor sum for `e^x`. Since all terms are positive and for every tail index `k>=21` the next-term ratio is at most `x/22<1`,

\[
e^x
<
\sum_{k=0}^{20}\frac{x^k}{k!}
+
\frac{x^{21}/21!}{1-x/22}
=:\overline E.
\tag{5.14}
\]

Every quantity in `Ebar` is rational. Since `rho_0=907/500`,

\[
\beta(\rho_0)^{500}
=A^{-500}B^{-907}e^{500x}q^{1407}
<
A^{-500}B^{-907}\overline E^{500}q^{1407}
=:U.
\tag{5.15}
\]

The executed exact-rational checker verifies

\[
\boxed{U<\left(\frac{12497}{12500}\right)^{500}},
\tag{5.16}
\]

with decimal rendering `U=0.8836829093029724...`. Hence

\[
\beta(\rho_0)<\widehat\beta<1.
\tag{5.17}
\]

Monotonicity of `beta` now proves (2.7) for every `b/a>=rho_0`.

Letting `n` tend to infinity, standard convergence in probability of `T(0,n(a,b))/n` to `mu(a,b)` contradicts (2.7) if `mu(a,b)<ca`. Thus

\[
\mu(a,b)\ge ca
\qquad\text{whenever }b/a\ge907/500.
\tag{5.18}
\]

Reflection handles negative `b`; homogeneity plus continuity of the time-constant norm extends from integer/rational vectors to every real `(x,y)` with `x>=0` and `|y|>=907x/500`:

\[
\boxed{\mu(x,y)\ge cx.}
\tag{5.19}
\]

## 6. Strict triangle defect and explicit finite residual error

For `x>0`, `|y|>=907x/500`, apply (5.19) to `(x,y)` and `(x,-y)`. By (4.3), homogeneity and axis symmetry,

\[
\mu(2x,0)=2x\mu(e_1)\le2a_8x.
\tag{6.1}
\]

Therefore

\[
\mu(x,y)+\mu(x,-y)-\mu(2x,0)
\ge2(c-a_8)x=\delta_8x.
\tag{6.2}
\]

The exact checker verifies the fraction (2.3) and `delta_8>1/100000`. This proves the infinite-volume theorem.

For the finite error, let integers `a>=1`, `b/a>=907/500`, and let `n` be divisible by `4`. Put

\[
u=n(a,b),\qquad z=n(2a,0),
\]

and define the nonnegative samplewise triangle residual

\[
\mathcal R_{a,b,n}
:=T(0,u)+T(u,z)-T(0,z)\ge0.
\tag{6.3}
\]

By translation invariance and reflection,

\[
\mathbb E T(u,z)=\mathbb E T(0,n(a,-b))
=\mathbb E T(0,n(a,b)).
\tag{6.4}
\]

From (2.7) and nonnegativity,

\[
\mathbb E T(0,n(a,b))
\ge can\left(1-C\widehat\beta^{an}\right).
\tag{6.5}
\]

Because `4|n`, the axis distance `2an` is a multiple of `8`; (4.2) gives

\[
\mathbb E T(0,2an e_1)\le2ana_8.
\tag{6.6}
\]

Combining (6.3)--(6.6),

\[
\frac{\mathbb E\mathcal R_{a,b,n}}{an}
\ge2(c-a_8)-2cC\widehat\beta^{an}
=\delta_8-2cC\widehat\beta^{an},
\tag{6.7}
\]

which is (2.8). This is a fully explicit block-to-infinite-volume error estimate, not an unproved limiting transfer.

The same exact artifact checks at `n=90000`

\[
2cC\widehat\beta^{90000}
=5.98255919858657\ldots\times10^{-6},
\]

while

\[
\delta_8-2cC\widehat\beta^{90000}
=1.25650705207038\ldots\times10^{-5}>10^{-5}.
\tag{6.8}
\]

Since the error decreases with `a`, (2.9) holds uniformly for all integer `a>=1` in the covered cone.

## 7. Literature boundary checked on 20 September 2026

A bounded fresh search was performed for ordinary iid undirected nearest-neighbor FPP strict convexity, Exp(1) square-lattice curvature, and recent planar-FPP shape results.

Relevant source distinctions:

1. Auffinger–Damron–Hanson, arXiv:1511.03262, remains the source navigation for the strict-convexity question. The present theorem is only a restricted-direction partial result.
2. Antonin Jacquet, arXiv:2412.20779 (2024), proves strict comparison between unrestricted and **directed** FPP time constants. That does not imply the undirected direction-to-direction strict triangle inequalities required here.
3. Dembin–Elboim–Peled, *GAFA* 34 (2024), prove quantitative planar geodesic coalescence under the assumption that the limit shape has more than 32 extreme points. That hypothesis cannot be used as a proof of the missing shape property.
4. Dembin–Elboim–Peled, *Annals of Probability* 53 (2025), study influential edges under compactly supported positive-density laws. Besides addressing a different question, those hypotheses do not include unbounded `Exp(1)` weights.
5. 2026 papers found in the search on correlated/long-range/continuous-space FPP concern different models and do not close this exact iid nearest-neighbor Exp(1) target.

No exact source-matching closure was found in this bounded search. That search miss is **not** asserted as proof of worldwide openness or novelty.

## 8. What moved, what did not, and the next mathematical obstruction

### Original problem before/after

- full Exp(1) limit-shape strict convexity: `OPEN -> OPEN`;
- canonical axis/diagonal `c_*`: `0 -> 0`;
- proved reflected-cone boundary: `15/8 -> 907/500`;
- positive normalized defect on the new cone: `unproved -> delta_8 > 10^-5`;
- finite transfer error on the new cone: explicit `2cC(12497/12500)^(an)`.

### Mechanism gain

The decisive new step is not another checker-only extension. It is the exact theorem

\[
\mu(e_1)\le0.6303807261851404\ldots
\]

obtained from a larger finite block with a proof that is insensitive to inter-block dependence. That stronger axis control creates enough slack to retune an already validated global path-entropy lower bound and move the source-valid direction regime substantially inward.

### Residual obstruction

The present method still cannot approach the axis/diagonal pair. Its two quantitative bottlenecks are now explicit:

1. the strip-block upper bound on `mu(e1)`;
2. the entropy loss in replacing self-avoiding paths by all non-backtracking direction sequences.

A further cone reduction must improve at least one. Merely sampling curvature or importing directed integrability does not address either bottleneck.

### Next attack

The next P04 run should avoid recomputing the same certificate. The preferred route is a memory-efficient **frontier-layer exact recursion** for longer width-three blocks (targeting length 9 or beyond) so the axis upper bound improves without storing all infected subsets simultaneously; in parallel, test whether a finite-memory two-step path-count transfer strictly lowers the non-backtracking entropy radius while preserving an exact Collatz certificate. Whichever produces a rigorous gain first should be transferred through (5.10)--(6.7).

## 9. Exact artifact and execution

Checker:

`proofnet24/P04-progress-curvature/artifacts/2026-09-20/2026-09-20T04-47-14Z__cone1814-exact.py`

creation commit: `bab04691ae46a27c1da018b16ad22c40eb1a5a09`.

Archived executed output:

`proofnet24/P04-progress-curvature/artifacts/2026-09-20/2026-09-20T04-47-14Z__cone1814-exact.out`

creation commit: `898a3a13cd63957ea2ea43e9a63f7de12aadb8b7`.

The output begins `ALL_EXACT_CHECKS_PASS` and records the exact ladder expectation, `1,649,609` recursion states, the Collatz ratios, the rational exponential comparison, `delta_8>10^-5`, and the explicit `n=90000` finite-margin check.

## ledger_delta

```text
track: P04
parent: T10 / ADH Q4 / iid Exp(1) undirected nearest-neighbor Z^2 FPP
parent_status: OPEN -> OPEN (PARTIAL only)
canonical_axis_diagonal_c_star: 0 -> 0
restricted_reflected_cone_boundary: 15/8 -> 907/500
new_cone_lower_bound: mu(x,y) >= (63039/100000) x for |y| >= (907/500)x
new_cone_strict_defect: delta_8 = 1.854762971929043e-5 > 1e-5
axis_upper_bound: 0.6453933351799015... (length 6) -> 0.6303807261851404... (length 8)
finite_error: 2*c*C*(12497/12500)^(a n), n divisible by 4
finite_uniform_example: n=90000 gives expected normalized residual >1e-5 for every a>=1 in cone
full_strict_convexity: NOT PROVED
novelty/worldwide_open_status: UNVERIFIED beyond bounded dated search
```

**End of complete run report.**

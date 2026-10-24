Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — METRIC MOVEMENT on active R09 successor G0013: `U_* = UNMEASURED -> 1/6`; Tang remains RETIRED/FROZEN at `UNBOUNDED_ABOVE` with supported unchanged count `6`, and G0002 remains handed off at `Delta_8=UNMEASURED`. Methods used: B1 CHANGE THE CATEGORY, B11 DUALIZE, B30 DO ONE SCALE / ONE DIRECTION AT A TIME.** GPT-6 / maximum was requested in prompt text, but this runtime exposes no authenticated model-family selector or reasoning-effort selector, so I do not claim otherwise.

# R09 CLOSABLE OUTSIDE — G0013 first active run: weighted Brenier reduction, outer Kantorovich dual, and a source-valid global bracket

Date: 2026-09-17 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.

## 1. Continuity and controlling state

I did **not** reopen Tang Question 4.11. Its periodic-tree clause remains refuted and retired in R09, with the frozen metric `UNBOUNDED_ABOVE` and supported retirement count 6. I also did not reopen G0002 / Cerf Conjecture 53.1, which R09 already handed off because the source-exact definitions (51.1)--(52.1) were inaccessible; its frozen metric remains `Delta_8=UNMEASURED`.

The previous R09 report ended on `ROTATION_HOLD / SUCCESSOR_ADMISSION_REQUIRED`. Since then, the repository acquired the create-only canonical claim

`operations/claims/G0013.md`,

which assigns G0013 exclusively to **R09 (CLOSABLE OUTSIDE)**. That newer ownership state controls this run. I therefore continue G0013 rather than screening another queue item.

Before new mathematics I reread/recovered the required campaign/control state: `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the newest R09 handoff report `runs/R09/20260917T1234Z_g0002_handoff_successor_screen_7c1a4e.md`, the current G0013 claim, the newest available neighboring R08 and R10 reports, the G-intake G0013 row and G0013-A001/A002 attempts, and the September 12 G0013 scripts surfaced by repository search. Oversized intake JSONL files are connector-truncated when rendered wholesale; I used the exact current G/H rows and attempt records relevant to the ownership/admission state and do **not** claim a literal byte-for-byte visual reread of all roughly 780 intake rows.

The frozen G0013 metric from the canonical claim is

`U_* = the smallest rigorous source-valid global upper bound on M established by R09`,

where

`M = sup_{pi in Pi(lambda,lambda)} W_2^2(pi, lambda tensor lambda)`

and `lambda` is uniform on `[0,1]`. The source conjecture is `M=1/10`, with the diagonal and antidiagonal as the maximizers. The pre-run value was `U_*=UNMEASURED`.

## 2. Source/current-status/ownership refresh

Primary source: Marta Catalano and Hugo Lavenant, *Measures of Dependence based on Wasserstein distances*, arXiv:2510.06034, Remark 3. In the current PDF, Remark 3 formulates exactly

`sup_{gamma in Pi(lambda,lambda)} W_2(gamma, lambda^2)`

for the Euclidean quadratic Wasserstein metric on the unit square, says the computation is still open, and conjectures that the supremum is attained when `X=Y` or `X=1-Y`. The same remark explicitly stresses that the earlier Manhattan-cost upper-bound proposition does **not** solve this Euclidean problem.

Latest later primary source found: Stefan Schrott, *Couplings Farthest from the Independent Gaussian*, arXiv:2609.10467v1, manuscript date 11 September 2026. Its Conjecture 1.1 restates the exact uniform problem and says it **remains open to the best of our knowledge**, while the paper proves the Gaussian analogue over the full coupling class. Its proof route is important here: write the quadratic transport cost in terms of a Brenier potential, then use coarea + Gaussian isoperimetry + a PSD matrix inequality to lower-bound the Laplacian.

Fresh bounded searches on 2026-09-17 used the exact source/conjecture titles, author names, `uniform copula`, `farthest from independence`, `Wasserstein`, `diagonal antidiagonal`, and constants `1/10` / `1/6`. They found the two primary sources above and no later source-matching resolution. This is bounded negative evidence, not a worldwide novelty certificate.

Ownership is unambiguous: `operations/claims/G0013.md` currently names R09 as exclusive owner. I create no new claim and do not touch shared roots.

Prior fleet work is preserved rather than restarted. In particular:

- G0013-A001 rewrote the problem as minimizing a maximal-correlation functional but did not find the uniform analogue of the Gaussian isoperimetric step;
- G0013-A002 used convexity/Bauer to reduce to extreme copulas, recorded the obstruction that nonatomic extreme copulas need not be deterministic maps, and verified the finite permutation model through `n<=7`;
- September 12 scripts explored permutation/exchange/block-reversal routes and did not bridge the full continuous problem.

This run therefore avoids another finite permutation search.

## 3. B30 — one coordinate at a time: the first source-valid global upper bound

There is an elementary coupling which immediately gives a full continuous upper bound.

Let `(X,Y) ~ pi`, where `pi in Pi(lambda,lambda)`, and let `Y' ~ lambda` be independent of `(X,Y)`. Then

`(X,Y') ~ lambda tensor lambda`.

Therefore the joint law of `((X,Y),(X,Y'))` is an admissible transport plan from `pi` to the independent coupling, and

`W_2^2(pi, lambda tensor lambda)`
` <= E[ |(X,Y)-(X,Y')|^2 ]`
` = E[(Y-Y')^2]`
` = 2 Var(lambda)`
` = 1/6`.

The same bound follows by keeping the second coordinate and independently resampling the first. Consequently

`M <= 1/6`.

This is not claimed as a novel mechanism: it is the natural one-coordinate resampling bound behind the generalized-mean-discrepancy normalizations discussed in the Wasserstein-dependence literature. What matters for R09 is that it is **source-valid for the Euclidean squared cost** and supplies the first frozen global bound for the current claim.

Hence the tracked quantity moves rigorously:

`U_* : UNMEASURED -> 1/6`.

This is real movement but **PARTIAL**, since `1/6 > 1/10`.

### Exact lower endpoint: the diagonal has value `1/10`

For completeness, here is a self-contained calculation of the conjectured value; this is also a normalization check for every later route.

Let `pi_D = Law(S,S)` with `S ~ Unif[0,1]`, and let `(U,V)` have the independent uniform-square law. For any coupling of `S` with `(U,V)`, put

`R=(U+V)/2`.

The Euclidean square cost decomposes identically as

`(U-S)^2 + (V-S)^2 = (U-V)^2/2 + 2(R-S)^2`.

The first expectation is fixed:

`E[(U-V)^2]/2 = (1/6)/2 = 1/12`.

The law of `R` has cdf

`F_R(r)=2r^2` for `0<=r<=1/2`,
`F_R(r)=1-2(1-r)^2` for `1/2<=r<=1`.

Thus its quantile is

`Q_R(t)=sqrt(t/2)` for `0<=t<=1/2`,
`Q_R(t)=1-sqrt((1-t)/2)` for `1/2<=t<=1`.

The remaining one-dimensional optimal transport cost is

`W_2^2(lambda, Law(R))`
` = int_0^1 (t-Q_R(t))^2 dt`
` = 2 int_0^(1/2) (t-sqrt(t/2))^2 dt`
` = 1/120`.

Therefore

`W_2^2(pi_D, lambda tensor lambda) = 1/12 + 2(1/120) = 1/10`.

Reflection of the second coordinate gives the same value for the antidiagonal. We now have the rigorous source bracket

`1/10 <= M <= 1/6`.

The remaining squared-distance gap is exactly

`1/6 - 1/10 = 1/15`.

## 4. B1 — change the category: an exact weighted-Hessian problem on the square

Schrott's Gaussian proof suggests changing categories from "maximize a Wasserstein distance over copulas" to "minimize a second-derivative functional of a convex Brenier potential". On the unit square this produces a different, boundary-weighted object, and that difference cleanly identifies why the Gaussian proof does not transplant verbatim.

Let

`Q=(0,1)^2`, `nu = Leb|_Q`,

and fix any copula `pi in Pi(lambda,lambda)`. Since `nu` is absolutely continuous, let

`T = grad phi`

be the Brenier map transporting `nu` to `pi`, with `phi` convex. Each component `T_i` has uniform `[0,1]` law.

Because both `nu` and `pi` have total second moment `2/3`,

`W_2^2(pi,nu) = 4/3 - 2 int_Q x dot T(x) dx`.

Set

`c_i = int_Q (x_i-1/2) T_i(x) dx`.

Since `int x_i dx = int T_i dx = 1/2`,

`int_Q x_i T_i dx = 1/4 + c_i`,

and hence

`W_2^2(pi,nu) = 1/3 - 2(c_1+c_2)`.        (4.1)

Now use convexity. For almost every value of the other coordinate, the one-dimensional slice

`t -> T_i(...,t,...)`

is a bounded nondecreasing BV function. Put `w(t)=t(1-t)`. Since `w(0)=w(1)=0` and `w'(t)=1-2t`, one-dimensional Stieltjes integration by parts gives

`int_0^1 (t-1/2) h(t) dt = (1/2) int_0^1 t(1-t) dh(t)`

for every such monotone slice `h`. Integrating the slice identity over the other coordinate gives

`2 c_i = int_Q x_i(1-x_i) d(D_i T_i)(x)`.

As `T=grad phi`, `D_i T_i = D^2_{ii} phi` is a nonnegative Radon measure. Substituting in (4.1) yields the exact identity

`W_2^2(pi,nu)`
` = 1/3 - J(phi)`,

where

`J(phi) := int_Q x_1(1-x_1) d(D^2_{11} phi)`
`          + int_Q x_2(1-x_2) d(D^2_{22} phi)`.       (4.2)

The pushforward constraints are simply

`(partial_i phi)_# nu = lambda`,  i=1,2.

Therefore the full Catalano--Lavenant conjecture is **equivalent** to the following weighted convex-analytic inequality:

> For every convex `phi` on the square whose two gradient components are uniform on `[0,1]`,
>
> `J(phi) >= 7/30`,
>
> with equality only for the Brenier potentials whose gradient pushes the square onto the diagonal or antidiagonal copula.

Indeed, `1/3-7/30=1/10`.

The one-coordinate resampling bound `M<=1/6` is equivalently the already established but nonsharp inequality

`J(phi) >= 1/6`.

Thus the entire remaining obligation has become a sharp **weighted Hessian gap**

`J(phi): 1/6 -> 7/30`,

of size exactly `1/15`.

### Why this is not merely Schrott's Gaussian proof with the density changed

In the Gaussian case, integration by parts converts the covariance directly into an **unweighted** Gaussian integral of `Delta phi`; coarea plus Gaussian isoperimetry then gives a sharp scalar BV lower bound, and a PSD matrix inequality combines the two components.

On the square, the exact no-boundary integration by parts necessarily introduces the Wright--Fisher weight

`x_i(1-x_i)`,

which vanishes on the two faces normal to coordinate `i`. Ordinary relative isoperimetry in the square therefore does not directly control (4.2) sharply: variation can migrate toward low-weight boundary regions. This is a concrete obstruction, not a vague statement that "the Gaussian proof does not apply".

A promising new target is consequently a **weighted/an\-isotropic coarea inequality calibrated to the square and to PSD Hessians**, not another permutation exchange lemma. Any such inequality strong enough to upgrade `J>=1/6` to `J>=7/30` closes the value part of the source conjecture.

## 5. B11 — dualize: remove the extreme-copula classification obstruction entirely

There is a second exact reformulation that bypasses the obstacle recorded in G0013-A002 (nonatomic extreme copulas need not be deterministic maps).

For a continuous potential `f:Q->R`, define its quadratic c-transform by

`f^c(x) = inf_{y in Q} { |x-y|^2 - f(y) }`.

Kantorovich duality on the compact square gives

`W_2^2(pi,nu) = sup_f [ int_Q f d pi + int_Q f^c d nu ]`.

Taking the supremum over all copulas and commuting the two suprema,

`M = sup_f [ A(f) + int_Q f^c d nu ]`,              (5.1)

where

`A(f) := sup_{pi in Pi(lambda,lambda)} int_Q f(s,t) d pi(s,t)`.

But `A(f)` is now an ordinary **one-dimensional-marginal optimal-assignment problem**. Its own Kantorovich dual is

`A(f) = inf_{a,b} { int_0^1 a(s) ds + int_0^1 b(t) dt : a(s)+b(t) >= f(s,t) }`.     (5.2)

Equations (5.1)--(5.2) are source-equivalent and do not require classifying extreme copulas at all.

They give a concrete closure certificate architecture:

> To prove `M<=1/10`, it is enough to prove that for every quadratic c-concave `f` one can choose one-dimensional functions `a,b` with `a+b>=f` and
>
> `int a + int b + int f^c d nu <= 1/10`.

Conversely, any `f` for which the bracket exceeds `1/10` would yield a route to a source counterexample through an optimizer of `A(f)`.

This reframes the earlier "non-deterministic extreme copula" obstruction as a **potential inequality on the square plus a one-dimensional assignment dual**. It is especially compatible with exact discretisation: a grid now approximates `f,a,b` and its c-transform, rather than pretending that finite permutation copulas exhaust the continuous extreme points.

I did not assert a new inequality beyond (5.1)--(5.2) this run. The point is to replace the failed extreme-point route by a source-equivalent certificate problem with no hidden deterministic-map assumption.

## 6. What moved, what did not, and the next route

### Fixed metric

Before:

`U_* = UNMEASURED`.

After:

`U_* = 1/6`.

This is a rigorous full-class upper bound, so the metric moved. The unchanged/stagnation count for the active G0013 metric resets to `0`.

### Status

`G0013 = OPEN_CURRENT / PARTIAL / CLAIMED_ACTIVE_BY_R09`.

Nothing in this run proves the conjecture. The source target remains `U_*=1/10` plus equality-case control.

### Strongest new structural reduction

The value problem is exactly

`inf J(phi) ?= 7/30`

over convex square potentials with both gradient components uniform, with

`J(phi)=sum_i int x_i(1-x_i) d(D^2_{ii}phi)`.

The already certified floor is `J>=1/6`; the missing amount is `1/15`.

### Next three methods

The next run should **not** repeat B1/B11/B30. The strongest genuinely different triple is:

- **B21 ASK WHO ELSE HAS THIS SHAPE:** search sharp weighted isoperimetry / Wright--Fisher or Jacobi diffusion BV inequalities for the weight `x(1-x)` and identify the exact two-dimensional anisotropic profile relevant to (4.2);
- **B15 BREAK THE SYMMETRY ON PURPOSE:** test whether near-boundary asymmetric Brenier potentials can drive `J` below `7/30`, rather than presuming the diagonal symmetry that one wants to prove;
- **B3 PROVE SOMETHING STRONGER:** seek a matrix-valued weighted coarea inequality whose equality cases are rank-one diagonal/antidiagonal Hessians; a sharp theorem of that form would simultaneously give the value and equality classification.

If that route does not move `U_*`, the report should say so rather than manufacture another finite-grid certificate.

## 7. Verification / prior art / artifact discipline

No finite exhaustive claim was made in this run, so no checker artifact was manufactured. The new mathematical statements are analytic identities with full proofs on the page. The exact rational constants were checked independently during the run (`Var(Unif[0,1])=1/12`, the triangular-mean quantile integral is `1/120`), but there is no reason to spend the run on a receipt-only checker.

Prior-art status is explicit:

- the source itself says the Euclidean supremum is open;
- Schrott (11 September 2026) says the exact uniform conjecture remains open while proving the Gaussian analogue;
- the `1/6` one-coordinate resampling mechanism is elementary / known-type and is **not** claimed as novel;
- the weighted-Hessian identity and the outer-dual certificate architecture are presented here as research reductions, not as literature-priority claims. A future paper would still need a dedicated novelty search if either reduction becomes part of a proof.

## 8. Model / scheduler-control status

The scheduler/control surface available to this worker still exposes prompt/title/schedule/timing/enabled state but **no model-family selector, no reasoning-effort selector, and no authenticated applied-run telemetry**. GPT-6 / maximum therefore remains prompt text only here.

Actually enforcing GPT-6 / maximum requires product/API fields for model and reasoning plus applied-runtime telemetry, or an authorized owning workspace that exposes those controls. The historical `You cannot modify this task` response for P26 is an authorization-context boundary; the lawful workaround is the owning authorized context, an ownership/admin transfer, or platform support, not duplication or a permission bypass. No scheduler modification was attempted.

## 9. Structured ledger_delta (R09-owned immutable report only)

```json
{
  "worker": "R09",
  "deployment": "NEW-METHODS-2026-09-16",
  "predecessor": {
    "target": "TANG-2020-Q4.11 periodic-tree clause",
    "metric": "greatest rigorous lower bound for theta'' at a certified admissible parameter",
    "value": "UNBOUNDED_ABOVE",
    "status": "RETIRED_FROZEN",
    "supported_unchanged_count": 6
  },
  "prior_handoff": {
    "target": "G0002 / Cerf Conjecture 53.1",
    "metric": "Delta_8",
    "value": "UNMEASURED",
    "status": "HANDOFF_FROM_R09"
  },
  "active": {
    "target": "G0013 / Catalano-Lavenant uniform-copula Wasserstein conjecture",
    "metric": "U_* = smallest rigorous source-valid global upper bound on M",
    "before": "UNMEASURED",
    "after": "1/6",
    "source_target": "1/10",
    "status": "OPEN_CURRENT__PARTIAL__CLAIMED_ACTIVE_R09",
    "unchanged_count": 0,
    "new_exact_reduction": "M = 1/3 - inf J(phi), J=sum_i int x_i(1-x_i) dD^2_ii phi; source conjecture iff J>=7/30",
    "dual_reduction": "M=sup_f[A(f)+int f^c dnu], A(f)=sup_{copulas}int f = inf_{a+b>=f}(int a+int b)",
    "remaining_value_gap": "1/15"
  },
  "methods_used": [1, 11, 30],
  "next_methods": [21, 15, 3],
  "finite_checker_created": false,
  "shared_roots_edited": false,
  "peer_files_edited": false,
  "email": false,
  "drive": false,
  "public_posting": false,
  "scheduler_change": false
}
```

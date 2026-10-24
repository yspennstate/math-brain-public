Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6/maximum was requested, but no authenticated applied model/reasoning receipt is exposed, so I do not claim GPT-6.**

# P04 T10 — moving-centered strip transfer and a certified reflected strict-triangle cone at slope 41/25

Date: 2026-09-20 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Controlling policy: `operations/PROGRESS20_2026-09-20.md`.  
Canonical parent: `operations/claims/PROB10-10.md`.  
Model: undirected nearest-neighbor FPP on `Z^2` with iid physical-edge weights `Exp(1)`.  
Status: **PARTIAL / OPEN** for full strict convexity. The restricted theorem proved below is `CANDIDATE_PROVED` pending later independent review.

## 1. Immutable handoff of the actual pre-T10 P04 target

P04's actual predecessor was intake `I0101`, Afonso S. Bandeira / Randomstrasse 2025 Conjecture 27, the two-localized Paley-graph theta bound. Its terminal immutable handoff is

`proofnet24/P04-closure-local-paley/runs/2026-09-18/2026-09-18T13-49-33Z__rotation-stop-disabled.md`.

That target remains **PARTIAL / source OPEN**, with exact finite prime frontier `4177` and complete tested domain preserved there. The six-run handoff was completed. Nothing in this run reopens I0101, changes its claim, or reopens the retired Target-1/squared-ridge kernel package or retired kernel Targets 2-4.

## 2. Source, ownership, exclusions, and current state consumed

The source remains Auffinger--Damron--Hanson, *50 years of first passage percolation*, arXiv:1511.03262, Question 4 in the limit-shape section: prove strict convexity for continuous passage-time laws. The canonical repository specialization is the iid `Exp(1)`, undirected, nearest-neighbor `Z^2` model.

I read and preserved the essential current state:

- `operations/PROGRESS20_2026-09-20.md`;
- root `POSTED.md` exclusions;
- `operations/claims/PROB10-10.md`;
- P04's preceding report `proofnet24/P04-progress-curvature/runs/2026-09-20/2026-09-20T06-53-21Z__strip7-carry-cone1702.md`;
- canonical-owner report `runs/prob10_2026-09-20/PROB10-10/20260920T0722Z__ten-local-saw-cone-1701.md` and its exact ten-local artifact;
- P20's current report `proofnet24/P20-progress-fpp/runs/2026-09-20/2026-09-20T07-12-00Z__finite-hjb-flatness-budget.md`;
- canonical R08 failure history, especially `runs/R08/20260916T1623Z_stuck_diagblock_4c19a7.md`, and the neighboring R07 fluctuation/KPZ history.

Ownership is unchanged. `PROB10-10` remains the canonical parent owner. P04 develops the complementary block-to-infinite-volume upper construction. The canonical owner develops the oblique finite-memory self-avoiding-path compiler. P20 develops Busemann/HJB mechanisms. This report consumes the canonical ten-local endpoint-count theorem and does not overwrite or relabel it.

The R08 failures remain binding: shared bypasses invalidate multiplication of local surgery gains; positive-probability finite cylinders can have exact finite triangle equality; fixed-corner blocks did not pay the old diagonal threshold. R07 fluctuation/overlap statements are not curvature theorems. The new route avoids all three issues by constructing one explicit global path and paying one explicit sublinear endpoint correction.

## 3. Original-problem before/after and mechanism gain

Write `mu` for the deterministic time-constant norm and

`Delta_12 = 2 mu(e1) - mu(1,1)`.

The canonical full-source metric remains

`c_* = sup{c>=0 : Delta_12 >= c is rigorously proved in the canonical track}`.

- **before:** `c_*=0`;
- **after:** `c_*=0`.

So this run does not prove axis/diagonal strictness and does not close full strict convexity.

The restricted-direction source scope does move substantially. Immediately before this run the best available reflected cone was the canonical owner's

`|y| >= (1701/1000)x = 1.701x`.

This run proves a strict triangle inequality already on

`|y| >= (41/25)x = 1.64x`, `x>0`.

Thus the covered slope boundary improves

`1.701 -> 1.64`.

At the new boundary the certified infinite-volume defect coefficient is

`delta = 23/125000 = 0.000184`.

The mechanism-level gain is an axis upper bound. P04's preceding seven-column fixed-strip carry theorem gave

`mu(e1) <= a_7 = 0.6049757734885347...`.

The moving-centered construction below gives the stronger rigorous cap

`mu(e1) < 294639/500000 = 0.589278`.

The important change is conceptual: **do not keep the strip pinned to the global axis. Recenter the next fresh block vertically at the random endpoint of the previous block.** The vertical drift is a mean-zero bounded random walk, so one final fresh-column repair costs only `O(sqrt(N))`, while every block starts from the favorable center lane.

## 4. The eight-column moving-centered block

Fix `L=8`. In local coordinates use rows `{-1,0,1}` and columns `0,...,8`. In departure columns `0,...,7`, permit both orientations of each physical vertical edge and permit each horizontal physical edge only eastward. Omit all vertical edges in terminal column `8`.

Start at local center `(0,0)` and let `tau` be the restricted passage time to the first vertex in terminal column `8`. Let `xi in {-1,0,1}` be the terminal row relative to the local center.

For the exponential model, Dijkstra/Richardson exploration is a finite-state continuous-time infection process. If the current infected set is `S`, each physical boundary edge contributes one independent residual rate-one exponential clock. If `m_j(S)` is the number of boundary edges leading to an uninfected vertex `j` and `m(S)=sum_j m_j(S)`, then the exact expectation satisfies

`E_S tau = 1/m(S) + sum_j [m_j(S)/m(S)] E_{S union {j}} tau`,

with terminal-hit states absorbing. The infected mask strictly grows, so this is a finite DAG recurrence.

### Rigorous computational core

The new artifact evaluates the center-start recurrence on exactly

`856569`

reachable masks. Rather than repeat the failed gigantic exact-Fraction length-eight calculation, it uses Python `Decimal` with precision `50` and `ROUND_CEILING` for **every positive division, multiplication and addition** in the recurrence. By induction backward on the infection-state DAG, every stored value is therefore an upper bound on the exact rational recurrence value. No subtraction or cancellation is used in this block calculation.

The executed certificate gives

`E tau <= 4.7142203024798824790150527878104939997183998570715`

and therefore

`E tau / 8 <= 0.58927753780998530987688159847631174996479998213394`

which is strictly below the rational cap

`a_* := 294639/500000 = 0.589278`.

This is a rigorous directed-rounding error bound, not an ordinary floating-point sign test.

## 5. Moving-centered concatenation theorem

### P04-T10-MOVING-STRIP8-AXIS-1 — CANDIDATE_PROVED

For iid undirected `Exp(1)` nearest-neighbor FPP on `Z^2`,

`mu(e1) <= a_* = 294639/500000 = 0.589278`.

### Proof

Let block `j` occupy horizontal departure columns

`8j,8j+1,...,8j+7`.

Suppose the current endpoint after `j` blocks is `(8j,S_j)`. Translate the local three-row block vertically so that its center is exactly `(8j,S_j)`, choose an optimal restricted path to the first point of column `8(j+1)`, and define the relative terminal displacement `xi_j in {-1,0,1}`. Then

`S_{j+1}=S_j+xi_j`.

The crucial dependence point is clean. The random vertical shift is measurable from previous slabs, but block `j` uses only physical edges whose departure `x`-coordinate lies in `{8j,...,8j+7}`. Different blocks therefore use disjoint physical-edge sets regardless of the random heights. Conditional on the past, the next selected slab edges are fresh iid `Exp(1)` variables. Vertical translation invariance makes the block law independent of `S_j`. Hence the pairs `(tau_j,xi_j)` are iid copies of `(tau,xi)`.

Reflection across the local center row sends `xi` to `-xi` and preserves the block law, so `E xi=0`. Also `|xi|<=1`, hence

`E S_N^2 = N E xi^2 <= N`

and by Cauchy--Schwarz

`E|S_N| <= sqrt(N)`.

After `N` blocks the concatenated restricted path ends at `(8N,S_N)`. Correct vertically to `(8N,0)` using the terminal column. No block used a vertical edge in that column, so these repair edges are fresh. Conditional on `S_N`, their expected total weight is exactly `|S_N|`. Therefore

`E T(0,8N e1) <= N E tau + E|S_N|`

`                 <= 8N a_* + sqrt(N)`.

Divide by `8N` and let `N->infinity`. Standard `L^1` convergence of FPP passage times to the time constant yields

`mu(e1) <= a_*`.

QED.

This is the requested dependence-controlled block-to-infinite-volume transfer. Adjacent blocks are adaptively recentered but remain fresh because physical-edge ownership is separated by horizontal slabs. The entire dependence cost is the final `O(sqrt(N))` vertical repair.

## 6. Consumed ten-local self-avoiding-path compiler with an explicit coarse constant

The canonical owner has already proved an exact ten-local transfer theorem. Its artifact certifies:

- `44100` ten-local states;
- a strictly positive Collatz vector with `z_min=1`, `z_max=10^14`;
- tilted step weights

`A=3889/2000`, `B=27893/10000`;

- transfer growth bound

`r=1993/400`.

I do not duplicate that claim. For this report's explicit finite error, it is enough to derive a simple coarse startup constant from those exact certified facts.

Let `L_ell` be the total tilted weight of length-`ell` ten-local paths. Since every state weight is at most `B^10`, for `ell>=10` the consumed Collatz inequality gives

`L_ell <= Kbar r^ell`

with

`Kbar = 44100 * 10^14 * (B/r)^10`

`     = 8238929532962105878831551056872795868088655007514624 / 617949527283939289422235868959530625`

`     = 1.3332690080975548e16...`.

For `ell<10`, the crude bound by all `4^ell` direction words gives

`L_ell/r^ell <= (4B/r)^ell < Kbar`,

as checked exactly in the new artifact. Thus the same `Kbar` is valid at every length.

Consequently, if `N_ell(n;a,b)` counts globally self-avoiding `ell`-edge paths from `0` to `n(a,b)`, then

`N_ell(n;a,b) <= Kbar r^ell A^(-an) B^(-bn)`.

The only new work here is the explicit safe `Kbar` used in the finite error; the ten-local transfer itself remains the canonical owner's result.

## 7. Oblique lower tail at slope 41/25

Choose

`s = 398251/100000`,

`q = r/(1+s) = 498250/498251 < 1`,

`c = 58937/100000 = 0.58937`,

`rho_0 = 41/25 = 1.64`,

`beta_hat = 9999/10000`.

For a fixed self-avoiding path of length `ell`, the passage sum is `Gamma(ell,1)`. With horizontal scale `m=an`, Chernoff gives

`P(Gamma(ell,1) <= c m) <= exp(s c m) (1+s)^(-ell)`.

Every geodesic can be chosen self-avoiding because passage times are positive, and every path from `0` to `n(a,b)` has `ell >= (a+b)n`. Therefore, for `rho=b/a`,

`P(T(0,n(a,b)) <= c m)`

` <= Cbar [A^(-1) B^(-rho) exp(sc) q^(1+rho)]^m`,

where

`Cbar = Kbar/(1-q)`

`     = 4105054878727902216233699145637927414071040446149168922624 / 617949527283939289422235868959530625`

`     = 6.643026165536148e21...`.

Let

`beta(rho)=A^(-1) B^(-rho) exp(sc) q^(1+rho)`.

It is decreasing in `rho` because `B>1` and `q<1`.

### Exact logarithmic certification

For `x>1`, with `z=(x-1)/(x+1)`, use

`log x = 2 sum_{k>=0} z^(2k+1)/(2k+1)`.

A finite partial sum is a rational lower bound and the omitted positive tail is bounded geometrically. The new exact-Fraction checker applies these bounds to `A`, `B`, `1/q`, and `1/beta_hat` and proves

`log beta(rho_0) <= -0.000134950448515686...`

while

`log(beta_hat) >= -0.00010000500033335833...`.

Hence

`beta(rho) <= beta(rho_0) < 9999/10000`

for every `rho>=41/25`.

Thus

`P(T(0,n(a,b)) <= c an) <= Cbar (9999/10000)^(an)`.

It follows that

`E T(0,n(a,b)) >= c an [1-Cbar(9999/10000)^(an)]`,

and passage to the time-constant limit gives

`mu(a,b) >= c a`

for every positive integer direction with `b/a>=41/25`. Homogeneity and continuity extend this to all real `(x,y)` with `x>0`, `y/x>=41/25`; reflection covers negative `y`.

## 8. New source-valid reflected strict-triangle theorem

### P04-T10-MOVING-STRIP8-CONE1640-2 — CANDIDATE_PROVED / PARTIAL

For every real `x>0` and `|y| >= (41/25)x`,

`mu(x,y)+mu(x,-y)-mu(2x,0) >= (23/125000)x`.

Equivalently,

`mu(x,y)+mu(x,-y)-mu(2x,0) >= 0.000184 x`.

### Proof

The lower-tail theorem gives

`mu(x,y) >= c x`, `mu(x,-y) >= c x`

with `c=58937/100000`. The moving-strip theorem gives

`mu(2x,0)=2x mu(e1) <= 2 a_* x`

with `a_*=294639/500000`. Hence

`mu(x,y)+mu(x,-y)-mu(2x,0)`

` >= 2(c-a_*)x`

` = (23/125000)x > 0`.

QED.

By simultaneous square-lattice `D_4` symmetries, all rotated/reflected copies of this cone are covered. This is a genuine infinite-volume strict triangle inequality in the exact undirected Exp(1) model. It is still only a restricted-direction theorem and remains **PARTIAL** relative to full strict convexity.

## 9. Explicit finite-to-infinite error

Let positive integers `a,b,n` satisfy `b/a>=41/25`, set `m=an`, and suppose `4|m`. Define

`R_{a,b,n} = T(0,n(a,b)) + T(n(a,b),n(2a,0)) - T(0,n(2a,0))`.

The first two terms have equal expectation by translation/reflection. The oblique lower-tail estimate gives

`E T(0,n(a,b)) >= c m [1-Cbar beta_hat^m]`.

For the axis term, `2m=8N` with `N=m/4`. The moving-centered construction gives

`E T(0,(2m,0)) <= 2m a_* + sqrt(N)`

`                     = 2m a_* + sqrt(m/4)`.

Therefore

`E R_{a,b,n}/m`

` >= delta - 2 c Cbar beta_hat^m - 1/(2 sqrt(m))`,

where `delta=23/125000`.

At the explicit common scale

`m=16000000`,

the endpoint term is exactly at most

`1/(2 sqrt(m)) = 1/8000 = 0.000125`.

Also

`beta_hat^m = (1-1/10000)^m <= exp(-1600)`.

Using the single positive Taylor term

`exp(1600) >= 1600^50/50!`

gives the exact rational upper bound

`exp(-1600) <= 50!/1600^50`.

The checker proves

`2 c Cbar exp(-1600) <= 1.4820393132313935e-74...`.

Hence

`E R_{a,b,n}/m > 5.89e-5`

at `m=16000000`, and the same lower bound mechanism only improves for larger multiples of four because both error terms decrease.

This is an explicit finite-to-infinite error estimate. The relatively large finite scale is caused by the deliberately coarse all-length `Kbar`, not by an unproved limiting step.

## 10. Why this route avoids the historical failures

1. **No multiplication of local surgery gains.** The proof builds one concatenated restricted path. Shared bypasses cannot invalidate an upper bound obtained from a single explicit path.
2. **No pointwise finite strictness.** The strict defect appears only after an asymptotic lower bound in the oblique directions and an explicit sublinear endpoint error on the axis. Cylinder events with exact finite triangle equality are harmless.
3. **No fixed-corner block.** Each block terminates at its best of three lanes and the whole strip is recentered at that random endpoint. The former fixed-axis outer-lane stationary penalty is removed and replaced by a diffusive final repair.
4. **No directed-integrable substitution.** Horizontal motion is restricted eastward only inside an admissible upper-bound path construction; all source passage times and the final theorem are for ordinary undirected FPP.
5. **No use of R07 fluctuation estimates as curvature.** The proof is a direct time-constant comparison with explicit errors.

P20's current finite-HJB theorem is complementary rather than duplicated. P20 shows that hypothetical axis/diagonal flatness would force only `O(sqrt(n log n))` mixed-HJB residual along the actual axis geodesic. This run does not supply that disagreement lower bound, so the canonical axis/diagonal metric remains zero.

## 11. Fresh literature check, 20 September 2026

Queries included:

- `first passage percolation strict convexity limit shape exponential weights Z2 2025 2026`;
- `site:arxiv.org first passage percolation strict convexity limit shape Exp(1) Z2 2026`;
- targeted checks for Jacquet's unrestricted-versus-directed comparison;
- targeted checks for Dembin--Elboim--Peled planar coalescence/extreme-point hypotheses.

Recovered scope:

- Auffinger--Damron--Hanson arXiv:1511.03262 remains the source navigation for the continuous-law strict-convexity question.
- Antonin Jacquet, arXiv:2412.20779, proves strict comparison between unrestricted and directed FPP time constants. That is a different inequality and does not give direction-to-direction strict convexity of the undirected norm.
- Dembin--Elboim--Peled, arXiv:2204.02332 / GAFA 2024, prove quantitative planar coalescence under an additional hypothesis of more than 32 extreme points of the limit shape. It cannot be used to establish the missing shape property without circularity.
- Bakhtin--Dow's differentiability work concerns different continuous-action/Riemannian/Poissonian models, not ordinary nearest-neighbor iid Exp(1) FPP.
- 2025--2026 FPP papers found in the bounded search on logarithmic subgraphs, Brochette/correlated FPP, critical FPP and directed last-passage models address different models or questions.

No source-matching closure of ordinary iid `Exp(1)` nearest-neighbor undirected `Z^2` strict convexity was found in this bounded search. This is **negative search evidence only**, not a proof of worldwide openness, novelty or priority.

## 12. Sanity checks and computational artifact

New artifact:

`proofnet24/P04-progress-curvature/artifacts/2026-09-20/2026-09-20T07-44-45Z__moving-strip8-cone1640-rigorous.py`

creation commit `ec4c3a815cbcd03ac2dfdb5eb7b05a90dfc578f3`.

Executed output:

`proofnet24/P04-progress-curvature/artifacts/2026-09-20/2026-09-20T07-44-45Z__moving-strip8-cone1640-rigorous.out`

creation commit `78604e0c749b6fe982a96c6f6f6475f2412dc664`, read back at that exact commit; blob `3c45010f83fc821ba370f8db55939d19e19cfcf6`.

The output begins

`P04 T10 moving-centered strip-8 / cone-1.64 rigorous certificate`

and then

`ALL_RIGOROUS_CHECKS_PASS = True`.

It records `856569` exact combinatorial infection states, 50-digit upward rounding, the strict cap `a8_upper_decimal < 0.589278`, exact rational logarithmic inequalities, `delta=23/125000`, and finite residual margin `>5.89e-5` at `m=16000000`.

## 13. Residual obstruction and next attack

Full strict convexity remains open. The present mechanism still combines an axis upper bound with an entropy lower bound far from the axis, so it cannot by itself approach the diagonal. With the current ten-local constants, even taking the Chernoff parameter toward its convergence boundary leaves a cone barrier near slope `1.6395` for the present axis cap. Thus merely retuning constants is nearly exhausted.

The next nonduplicating P04 attack is **not** another stationary carry calculation. It is one of:

1. compute a longer moving-centered block with memory-efficient directed interval recursion (center start only, because outer-state data are now unnecessary), or
2. widen the moving strip and optimize the center-start free-terminal block while keeping horizontal-slab edge ownership, then recompile the oblique cone.

The length-eight center-only computation succeeded precisely because the new recentering lemma removed the need to solve the expensive outer-start state. A length-nine center-only frontier/interval implementation is therefore the natural next quantitative test. If that route ceases to move the cone for three substantive runs, P04 should change mechanism rather than manufacture larger finite certificates.

## 14. ledger_delta

```text
P04 | T10 iid Exp(1) undirected Z2 FPP strict convexity | full source c_*: 0 -> 0 (OPEN/PARTIAL); best certified reflected-cone boundary: 1701/1000=1.701 -> 41/25=1.64; new defect on cone: delta=23/125000=0.000184; axis upper bound mechanism: 0.6049757734885347... -> <294639/500000=0.589278; finite residual at m>=16000000, 4|m: >5.89e-5 with error <=1/8000 + 1.4821e-74; new mechanism = adaptively recentered disjoint x-slab blocks with O(sqrt N) final vertical repair; canonical axis/diagonal strictness remains unproved.
```

**End of complete run report.**

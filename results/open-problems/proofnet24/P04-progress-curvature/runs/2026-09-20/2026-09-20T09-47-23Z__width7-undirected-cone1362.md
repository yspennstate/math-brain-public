Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6/maximum was requested, but no authenticated applied model/reasoning receipt is exposed, so I do not claim GPT-6.**

# P04 T10 — wider undirected moving slab, axis cap 0.51779, and strict-triangle cone down to slope 1.362

Date: 2026-09-20 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Controlling policy: `operations/PROGRESS20_2026-09-20.md`.  
Canonical parent: `operations/claims/PROB10-10.md`.  
Model: undirected nearest-neighbor FPP on `Z^2` with iid physical-edge weights `Exp(1)`.  
Status: **PARTIAL / OPEN** for full strict convexity. The restricted theorems below are **CANDIDATE_PROVED pending later independent review**.

## 1. Brief immutable handoff of P04's actual pre-T10 target

P04's actual predecessor was intake `I0101`, Afonso S. Bandeira / Randomstrasse 2025 Conjecture 27, the two-localized Paley-graph theta bound. Its terminal immutable handoff remains

`proofnet24/P04-closure-local-paley/runs/2026-09-18/2026-09-18T13-49-33Z__rotation-stop-disabled.md`.

That target remains **PARTIAL / source OPEN** with exact finite frontier `4177` and retained tested domain

`{149,257,1009,4001,4013,4021,4049,4057,4073,4093,4129,4133,4153,4157,4177}`.

Nothing in this run reopens I0101 or the retired squared-ridge/kernel package.

## 2. Current T10 state, dependencies, ownership and failures consumed

The source remains Auffinger--Damron--Hanson, *50 years of first passage percolation*, arXiv:1511.03262, Question 4 in the limit-shape discussion: prove strict convexity for continuous passage-time laws. The repository freezes the iid `Exp(1)` undirected nearest-neighbor `Z^2` special case.

Before doing new mathematics I consumed the essential state:

- `operations/PROGRESS20_2026-09-20.md`;
- root `POSTED.md` exclusions relevant to FPP;
- canonical `operations/claims/PROB10-10.md`;
- P04's preceding report `2026-09-20T08-45-54Z__moving-strip9-cone16377.md`;
- canonical owner report `runs/prob10_2026-09-20/PROB10-10/20260920T0820Z__critical-threshold-cone-163952.md` and its ten-local weighted-SAW dependency;
- P20's latest report `proofnet24/P20-progress-fpp/runs/2026-09-20/2026-09-20T09-18-00Z__single-edge-residual-clock-compiler.md`;
- R08's stuck FPP report `runs/R08/20260916T1623Z_stuck_diagblock_4c19a7.md`;
- the distinct R07 KPZ/variance report `runs/R07/2026-09-16T1525Z_kpz_deep_edges_03.md`.

Ownership remains nonduplicating. `PROB10-10` owns the parent and the oblique finite-memory self-avoiding-path compiler. P04 owns a complementary block-to-infinite-volume upper construction. P20 owns the actual-geodesic/Busemann/HJB disagreement route. I consume the canonical ten-local constants and do not overwrite or duplicate its claim.

The old R08 failures remain binding: shared bypasses defeat naive multiplication of local surgery gains; positive-probability finite cylinder events can have exact finite triangle equality; and old fixed-corner blocks did not reach the diagonal threshold. R07's fluctuation/KPZ results are not curvature. The present proof uses one explicit global path assembled from disjoint physical-edge slabs and therefore does not invoke any of those failed steps.

## 3. Original-problem before/after and mechanism movement

Let `mu` be the time-constant norm and

`Delta_12 := 2 mu(e1)-mu(1,1)`.

The canonical full-source metric is the largest proved `c>=0` with `Delta_12>=c`.

- **before:** `c_*=0`;
- **after:** `c_*=0`.

Thus this run does **not** prove axis/diagonal strictness and does not close full strict convexity.

The restricted-direction source theorem does move sharply. P04's preceding strip-9 result had

`mu(e1) <= 13247968739227/22500000000000 = 0.5887986106323111...`

and, with the canonical ten-local compiler,

`1.6376495 < rho_*^(9) < 1.6376496`, with a convenient closed cone `|y|>=1.6377x`.

This run proves

`mu(e1) <= a_47 := 1035580351964689/2000000000000000`

`                    = 0.5177901759823445...`,

an axis-cap improvement of

`1278151823699399/18000000000000000 = 0.0710084346499666...`.

Combining with the same canonical ten-local compiler now gives

`1.3619684 < rho_*^(47) < 1.3619685`

and a clean closed theorem for

`|y| >= (681/500)x = 1.362x`.

So the proved reflected-cone boundary moves from about `1.63765` to about `1.36197`. This is a source-valid infinite-volume expansion of covered directions, not a finite sampling statistic.

## 4. New idea: spend block complexity on width and true undirected motion

The preceding P04 blocks used only three rows and, inside a slab, allowed horizontal physical edges only eastward. That makes the state recursion cheap, but it suppresses two real features of undirected FPP: lateral competition across more rows and beneficial horizontal backtracking inside a slab.

Instead of extending the length-9 three-row recursion to length 10, I changed the block category. Use a **shorter but wider** slab with seven rows and horizontal length four, and retain every physical horizontal edge inside the slab as an ordinary undirected edge. The slab is still assigned to one horizontal departure interval, so the stronger within-block optimization does not create cross-block dependence.

This was the decisive change. The finite state space is larger (`35,188,637` reachable infection states), but a compiled fixed-point upward recursion remains feasible and gives a much smaller mean cost per horizontal unit.

## 5. Finite width-7, length-4 undirected slab

Let

`V = {0,1,2,3,4} x {-3,-2,-1,0,1,2,3}`.

The allowed physical edges are:

1. every nearest-neighbor horizontal edge between columns `x` and `x+1` for `x=0,1,2,3`, traversable in either direction;
2. every vertical nearest-neighbor edge in departure columns `x=0,1,2,3`;
3. no terminal-column vertical edge at `x=4`.

Start from `(0,0)`. Let `tau` be the passage time in this restricted undirected slab to the first hit of column `4`, and let `xi in {-3,-2,-1,0,1,2,3}` be the terminal row.

Because this is a subgraph of the ordinary undirected FPP environment, every slab path is a valid path in the source model.

### 5.1 Exact exponential-infection recurrence

For an infected vertex set `S`, let `m_j(S)` be the number of active boundary physical edges from `S` to an uninfected vertex `j`, and `m(S)=sum_j m_j(S)`. Exponential memorylessness gives

`E(S) = 1/m(S) + sum_j [m_j(S)/m(S)] E(S union {j})`.

Every transition strictly enlarges the infected set, so this is a finite DAG recurrence. For the terminal second moment, put terminal value `xi^2` and use the same convex recurrence without the holding-time term.

### 5.2 Rigorous fixed-point upward lemma

Fix `Q=10^15`. Suppose every child has an integer `U_child` with

`E(child) <= U_child/Q`.

Then

`U(S) := ceil( [Q + sum_j m_j(S) U_child]/m(S) )`

satisfies `E(S)<=U(S)/Q`. This follows by direct substitution in the positive recurrence. Backward induction from terminal value zero certifies the root expectation.

Likewise, if terminal states carry the exact integer reward `xi^2 Q`, then

`V(S) := ceil( [sum_j m_j(S) V_child]/m(S) )`

is a rigorous upper bound on `E[xi^2 | S]`.

No floating-point sign is used anywhere in the finite theorem.

### 5.3 Executed finite certificate

The compiled checker visits exactly

`35,188,637`

reachable states and certifies

`E tau <= 2071160703929378/10^15`

`      = 2.071160703929378`,

hence

`E tau/4 <= a_47`

with

`a_47 = 1035580351964689/2000000000000000`

`     = 0.5177901759823445...`.

It also certifies

`E xi^2 <= 2496533430161757/10^15`

`        = 2.496533430161757`

and therefore the convenient rational bound

`E xi^2 < pbar := 124827/50000 = 2.49654`.

Reusable finite-core artifact:

`proofnet24/P04-progress-curvature/artifacts/2026-09-20/2026-09-20T09-47-23Z__width7-length4-undirected-moving-slab-rigorous.cpp`

creation commit `2f8b8d0c8c11600335c38156185de51ff1f6f6b8`.

Archived executed output:

`proofnet24/P04-progress-curvature/artifacts/2026-09-20/2026-09-20T09-47-23Z__width7-length4-undirected-moving-slab-rigorous.out`

creation commit `a9d7b928bed5e5454e0e277ad601badd4e47679f`, recording `ALL_RIGOROUS_CHECKS_PASS = True` and exit status zero.

## 6. Dependence-controlled moving-centered transfer

### P04-T10-W7L4-UNDIRECTED-AXIS — CANDIDATE_PROVED

For iid undirected `Exp(1)` nearest-neighbor FPP on `Z^2`, for every integer `N>=1`,

`E T(0,4N e1) <= 4N a_47 + sqrt(N pbar)`.

Consequently

`mu(e1) <= a_47`.

### Proof

Suppose block `j` starts at `(4j,S_j)`. Translate the seven-row local slab vertically so its center is that point. Inside the slab choose the restricted optimal path to the first vertex in column `4(j+1)` and let `(tau_j,xi_j)` be its cost and relative terminal row. Put

`S_{j+1}=S_j+xi_j`.

Block `j` uses horizontal physical edges with left endpoint x-coordinate `4j,...,4j+3` and vertical physical edges only in columns `4j,...,4j+3`. Therefore distinct blocks use disjoint physical-edge sets. The random vertical recentering depends on the past, but conditional on that past every edge selected for the next slab is untouched iid `Exp(1)`. Vertical translation invariance makes the law independent of `S_j`. Hence `(tau_j,xi_j)` are iid copies of `(tau,xi)`.

Reflection about the slab center sends `xi` to `-xi`, so `E xi=0`. Thus

`E S_N^2 = N E xi^2 <= N pbar`

and Cauchy--Schwarz gives

`E|S_N| <= sqrt(N pbar)`.

After `N` blocks the concatenated valid path ends at `(4N,S_N)`. Correct vertically to `(4N,0)` using the terminal column. No block used a vertical physical edge in column `4N`, so these correction edges are fresh and have conditional expected total weight exactly `|S_N|`. Therefore

`E T(0,4N e1)`

` <= N E tau + E|S_N|`

` <= 4N a_47 + sqrt(N pbar)`.

Divide by `4N` and let `N->infinity`; standard `L^1` time-constant convergence gives `mu(e1)<=a_47`. QED.

This is the requested dependence-controlled block-to-infinite-volume transfer. The stronger within-block undirected optimization costs no accumulating interface term; the complete endpoint mismatch is the explicit `O(sqrt N)` term above.

## 7. Consumed canonical ten-local lower-tail theorem

The canonical owner already proved the weighted all-length self-avoiding-path count

`N_l(M,R) <= Kbar r^l A^(-M) B^(-R)`

for `M,R>=0`, with

`A=3889/2000`,
`B=27893/10000`,
`r=1993/400`,

and

`Kbar = 44100 * 10^14 * (B/r)^10`.

I consume that theorem rather than create a duplicate claim.

For any `s>r-1`, set `q=r/(1+s)<1`. A fixed self-avoiding `l`-edge path has `Gamma(l,1)` passage sum, so for `c>0`,

`P(Gamma(l,1)<=cM) <= exp(scM)(1+s)^(-l)`.

Every path from `0` to `(M,rho M)` has `l>=(1+rho)M`. Summing the canonical count gives

`P(T(0,(M,rho M))<=cM)`

` <= C_s [beta_s(rho)]^M`,

where

`C_s=Kbar/(1-q)`

and

`beta_s(rho)=A^(-1) B^(-rho) exp(sc) q^(1+rho)`.

If `beta_s(rho)<1`, then

`E T(0,(M,rho M)) >= cM [1-C_s beta_s(rho)^M]`,

and the time-constant limit gives `mu(1,rho)>=c` (first for rational directions, then by homogeneity/continuity).

## 8. New critical slope of the fixed ten-local compiler plus the width-7 block

Define

`rho_*^(47) := ((r-1)a_47 - log A)/log B`.

The exact rational logarithm checker uses the positive atanh series

`log x = 2 sum_{k>=0} z^(2k+1)/(2k+1)`, `z=(x-1)/(x+1)`,

with an explicit geometric tail, and proves

`1.3619684 < rho_*^(47) < 1.3619685`.

For any `rho>rho_*^(47)`, put

`G(rho)=log A + rho log B - (r-1)a_47 >0`,

`c_rho=a_47 + G(rho)/(2(r-1))`,

`epsilon_rho=G(rho)/(4c_rho)`,

`s_rho=(r-1)+epsilon_rho`.

At the boundary `s_0=r-1`, formally `q=1`,

`log beta_{s_0}(rho) = -G(rho)/2`.

Increasing `s` to `s_rho` changes the log base by

`epsilon_rho c_rho - (1+rho) log(1+epsilon_rho/r)`

which is at most `epsilon_rho c_rho=G(rho)/4`. Hence

`log beta_{s_rho}(rho) <= -G(rho)/4<0`.

Therefore `mu(1,rho)>=c_rho`; reflection gives the same lower bound for `mu(1,-rho)`, while Section 6 gives `mu(2,0)<=2a_47`. Thus

`mu(1,rho)+mu(1,-rho)-mu(2,0)`

` >= G(rho)/(r-1)>0`.

By homogeneity:

### P04-T10-W7L4-CRITICAL-CONE — CANDIDATE_PROVED / PARTIAL

For every real `x>0` and every `rho=|y|/x>rho_*^(47)`,

`mu(x,y)+mu(x,-y)-mu(2x,0)`

` >= [G(rho)/(r-1)]x>0`.

The same statement holds after simultaneous `D_4` rotations/reflections. This is a genuine infinite-volume strict triangle inequality in the exact undirected `Exp(1)` model, but it is only a restricted reflected family and does not prove arbitrary chord strictness.

## 9. Clean closed cone at slope 1.362

Choose

`rho0=681/500=1.362`,

`c=129449/250000=0.517796`,

`s=39825001/10000000=(r-1)+10^(-7)`,

`q=49825000/49825001`,

`beta_hat=999991/1000000`.

The exact rational scalar checker proves

`log beta_s(rho0) <= -9.19045947122179e-6`

while

`log(beta_hat) >= -9.000040500243001e-6`.

Thus `beta_s(rho0)<beta_hat<1`; since the base decreases as `rho` increases, the bound is uniform on the whole cone. Combining the resulting oblique lower bound with the new axis cap gives

`delta_47 := 2(c-a_47)`

` = 11648035311/10^15`

` = 1.1648035311e-5`.

Hence:

### P04-T10-W7L4-CLOSED-CONE-1362 — CANDIDATE_PROVED / PARTIAL

For every real `x>0` and every `|y|>=(681/500)x`,

`mu(x,y)+mu(x,-y)-mu(2x,0)`

` >= (11648035311/10^15)x > 1.1e-5 x`.

For comparison only, on the already established `1.6377` cone the previous certified lower level `c=0.588807` remains valid, so the new axis cap strengthens the uniform defect there to

`142033648035311/10^15 = 0.142033648035311`.

Thus this run expands directions and strongly increases defect on the overlap.

Exact scalar artifact:

`proofnet24/P04-progress-curvature/artifacts/2026-09-20/2026-09-20T09-47-23Z__width7-cone1362-exact.py`

creation commit `d22a381b64d30f546c4be07bc20eb7e3c4b65431`.

Archived output:

`proofnet24/P04-progress-curvature/artifacts/2026-09-20/2026-09-20T09-47-23Z__width7-cone1362-exact.out`

creation commit `043d5a3633cf46727b4aac8fc84763af4b165e5e`, recording `ALL_EXACT_CHECKS_PASS = True`.

## 10. Explicit finite-to-infinite error

Let positive integers `a,b,n` satisfy

`b/a >= 681/500`,

put `m=an`, and assume `m` is even. Define

`R_{a,b,n}`

` := T(0,n(a,b)) + T(n(a,b),n(2a,0)) - T(0,n(2a,0))`.

The two oblique legs have equal law by reflection. Section 7 gives

`E T(0,n(a,b)) >= cm [1-Cbar beta_hat^m]`,

where `Cbar=Kbar/(1-q)`. For the axis target `2m e1`, Section 6 uses

`N=2m/4=m/2`

blocks and gives

`E T(0,2m e1) <= 2m a_47 + sqrt((m/2)pbar)`.

Therefore

`boxed{
 E R_{a,b,n}/m
 >= delta_47
    - 2c Cbar beta_hat^m
    - sqrt(pbar/(2m)).
}`

This is an explicit dependence-controlled finite-to-infinite error estimate.

At

`m=100000000000`,

the exact checker verifies

`sqrt((m/2)pbar) < 353309`,

so the normalized repair is below

`353309/10^11 = 3.53309e-6`.

Also

`beta_hat^m=(1-9e-6)^m <= exp(-900000) <= 20!/900000^20`,

and the complete lower-tail contribution is below `1.377e-77`. Hence the exact certified finite margin satisfies

`boxed{ E R_{a,b,n}/m > 8e-6 }`

at this scale, uniformly throughout the `1.362` cone. Both error terms decrease for larger even `m`, so the positive finite residual persists thereafter.

## 11. Complementary P20 mechanism and why this is not duplicated work

P20's newest theorem is a one-edge residual-clock Bellman compiler. It replaces a four-edge fresh-star condition by a single reserved exponential residual clock and proves the local modulus

`f(p)=p+(1-p)log(1-p) >= p^2/2`.

That is a genuine improvement toward the axis/diagonal target, but P20 still needs enough charged reserved edges along the **actual** axis geodesic to beat the `O(sqrt(n log n))` finite-target budget. P04's path above is an explicit comparison path, not the actual axis geodesic, so I do not insert it into P20's residual identity. The two routes remain complementary.

## 12. Fresh literature check, 20 September 2026

Queries included exact-model combinations of `first passage percolation`, `strict convexity`, `limit shape`, `Exp(1)`, `2025`, and `2026`, plus targeted searches for Jacquet, Dembin--Elboim--Peled, Hassler, and recent curvature work.

Scope recovered:

- Auffinger--Damron--Hanson remains the source navigation for the continuous-law strict-convexity question.
- Jacquet, arXiv:2412.20779 (2024), proves strict inequality between unrestricted and **directed** FPP time constants. It does not imply direction-to-direction strict convexity of the ordinary undirected norm.
- Dembin--Elboim--Peled, arXiv:2204.02332, prove quantitative planar coalescence under the extra hypothesis that the limit shape has more than 32 extreme points; that assumption cannot be used to establish the missing shape property here.
- Hassler, arXiv:2511.06166 (2025), proves lower bounds on non-random fluctuations under conditions, not strict convexity of the iid Exp(1) lattice shape.
- Bakhtin--Dow, arXiv:2406.09652, establish differentiability criteria in different continuous-action FPP models, not this discrete nearest-neighbor model.
- A 2025 paper on FPP/non-positive curvature concerns coarse geometry on general graphs and is not a lattice limit-shape strict-convexity theorem.

The bounded search found no primary-source theorem closing ordinary iid `Exp(1)` nearest-neighbor strict convexity on `Z^2`. This is dated search evidence, not a claim of exhaustive worldwide openness or novelty.

## 13. Failed/abandoned route this run

I also examined the direct rotated-diagonal analogue: fresh slabs between successive `x+y` levels, recentered in the transverse `x-y` coordinate. The transfer itself works by the same disjoint-edge and diffusive-repair principle, but the small finite blocks accessible without a new state-compression theorem remain far above the repository's sufficient diagonal target `mu(1,1)<0.6005646`. I therefore do not promote a diagonal finite estimate or confuse that experiment with source progress.

The useful lesson is structural: **widening the axis slab is currently much more profitable than lengthening a narrow slab or forcing a diagonal block.**

## 14. Residual obstruction and next attack

The canonical full-source obstruction remains

`Delta_12 = 2mu(e1)-mu(1,1)>0`.

This run greatly improves an axis **upper** bound, so by itself it does not combine with R08's axis lower bound to prove `Delta_12>0`. The reflected-cone compiler is now limited by the canonical ten-local endpoint-count constants and the new axis cap at the exact scalar threshold `rho_*^(47)≈1.3619684`.

A nonduplicating next P04 attack should therefore be one of:

1. a frontier-compressed wider/longer moving undirected slab that lowers `a_47` further without a 35M-state blowup; or
2. a dependence-controlled rotated slab whose diagonal cost finally crosses the known `0.6005646` sufficient threshold; or
3. a bridge from the moving-slab exploration to P20's reserved-edge compiler that certifies super-`sqrt(n log n)` charged mass along the actual axis geodesic.

Scalar Chernoff micro-retuning with the same `(A,B,r,a_47)` cannot pass below `rho_*^(47)` and should not consume another run.

## ledger_delta

`P04 | T10 Exp(1) undirected FPP strict convexity | canonical axis/diagonal c_*: 0 -> 0 (OPEN/PARTIAL); restricted reflected strict-triangle slope infimum: rho_* in (1.6376495,1.6376496) -> rho_* in (1.3619684,1.3619685); clean closed cone 1.6377 -> 1.362; new uniform defect on 1.362 cone = 11648035311/10^15 > 1.1e-5; explicit finite error at m=10^11 leaves >8e-6; mechanism axis cap 0.5887986106323111 -> 0.5177901759823445 via width-7 length-4 fully undirected moving slab with 35,188,637-state rigorous fixed-point certificate | CANDIDATE_PROVED restricted theorem / parent OPEN`

**End of complete run report.**

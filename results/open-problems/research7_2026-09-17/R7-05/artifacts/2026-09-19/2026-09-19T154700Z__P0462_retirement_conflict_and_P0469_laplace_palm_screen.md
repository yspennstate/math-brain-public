Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime reasoning-effort telemetry or binding model/effort selector is exposed.

# R7-05 — P0462 retirement-history correction and P0469 Laplace–Palm admission mathematics

Date: 2026-09-19 UTC  
Worker: `R7-05 Sharp Inequality Research`  
Native ID: `6aabe805f32881919992996e1c5cfad6`  
Repository: `yspennstate/math-open-problems`, branch `master`

## 1. Corrected continuity: P0462 is a retired route, so R7-05 must not continue it

The immediately preceding R7-05 admission/report treated canonical target `P0462` (Russell Lyons, *Determinantal Probability: Basic Properties and Conjectures*, Question 2.8) as fresh CLOSABLE inventory. A deeper path-scoped history search in this run recovered an earlier complete native campaign on the same source target:

`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-12/`.

The terminal report is

`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-12/runs/2026-09-16/2026-09-16T200347Z__report.md`

at creation commit

`1bf08d753b361094d73bf68ab849899d183ea378`.

That report explicitly states that Lyons Question 2.8 remained mathematically OPEN/PARTIAL but was **operationally retired from the native slot after its sixth consecutive unchanged frozen-metric run**. It then rotated the native slot to D0009. This is not a missing-report ambiguity: the retirement report and its predecessor history are present and readable.

The recovered earlier P0462 mathematics is also far stronger than the history summary used in the R7-05 admission. Among other things, PROB20-12 already had the finite-to-countable/Naimark reductions, signed Laplace/Jacobi full-marginal lift, pairwise disjoint couplings, K6 `2+2+2` perfect-matching formulation, 90-state polytope, 4450 known facet rays, seven wall orbits, linear-rank saturation, toric/integer-kernel certificates, Fourier feasible families and several exact wall-cone completions. Thus the preceding R7-05 report's description of prior work as essentially rank-one-only was a `HISTORY_GAP` error.

The owner rule says that retired routes are excluded from successor selection and that a stale/disabled predecessor never establishes release. Therefore this run does **not** perform a second P0462 research attack and does not count another `UC_RESOLVED=0` stagnation step. The newly created `operations/claims/P0462.md` remains untouched because attacking workers were authorized only for create-only canonical claims, not destructive/editing reconciliation. It should be treated as a coordinator-reconciliation item, not as permission for R7-05 to resurrect P0462.

Operational state after this correction: `PENDING_ADMISSION`; successor metric `UNKNOWN/UNMEASURED`; no inherited stagnation count.

## 2. Shard continuation and candidate chosen for substantive admission work

After excluding P0462, the exact case-sensitive residue-4 cursor continues to `P0469` in the Codex/DGFF block:

- canonical ID: `P0469`;
- source: Marek Biskup, *Extrema of the two-dimensional Discrete Gaussian Free Field*, PIMS-CRM lecture notes, Problem 16.4, PDF p.221;
- exact source request: determine the limiting maximum density `rho^D` explicitly, or characterize it by a PDE with a unique solution.

The source PDF still displays Problem 16.4 under the title “Nailing density explicitly.” The 2024 Biskup–Gufler–Louidor near-maxima paper identifies the critical LQG measure jointly with the extremal process but does not, in the bounded 2026-09-19 search, provide the requested explicit density/PDE. The search miss is negative evidence only.

This candidate is mathematically substantial but, after the calculation below, is classified **HARD / NOT CLOSABLE for this worker**: its exact endpoint is an explicit infinite-dimensional law/PDE, not a finite certificate, sharp scalar constant, or short counterexample-style statement.

## 3. Mathematical idea before any code

The source extremal-process representation already says that, conditional on the critical random measure `Z=Z^D`, extremal leaders form a Poisson point process on `D x R` with intensity

`Z(dx) exp(-alpha h) dh`.

Instead of trying to guess a PDE for `rho^D`, isolate exactly which transform of the random measure the density contains. This turns the admission question into a clean identifiability problem: does one need only the total mass `W=Z(D)`, or genuinely the joint law of total mass and normalized spatial measure?

No numerical checker is needed; all identities below are exact.

## 4. B16 — compute the smallest exact models: total-mass information does not determine the joint density

Let `Z` be any almost surely finite positive random measure on `D`, put

`W := Z(D) > 0`,  `M := Z/W`,

and condition on `Z`. If `(X,T)` is the location and height of the highest Poisson atom, then the usual one-point/void calculation gives

`P(X in dx, T in dt | Z)
 = Z(dx) exp(-alpha t) exp[-(W/alpha) exp(-alpha t)] dt.`

Set

`s(t) := exp(-alpha t)/alpha`.

After averaging,

`rho(dx,t) dt
 = exp(-alpha t) E[ Z(dx) exp(-s(t) W) ] dt.`

The height density is therefore

`f_T(t) = exp(-alpha t) E[ W exp(-s(t)W) ]`,

while the conditional location law at height `t` is

`mu_t(A)
 = E[ W M(A) exp(-s(t)W) ] / E[ W exp(-s(t)W) ].`  (1)

A two-point exact countermodel shows that neither the law of `W` nor even the law of `W` together with the unconditional mean location law determines `rho`.

Take `D={a,b}` and let `W` equal `1` or `2`, each with probability `1/2`.

Model A: `M(a)=M(b)=1/2` always.

Model B: `M(a)=3/4` when `W=1`, and `M(a)=1/4` when `W=2` (with the complementary masses at `b`).

Both models have exactly the same total-mass law and exactly the same unconditional mean normalized measure,

`E M(a)=E M(b)=1/2`.

But (1) gives

`mu_s^A(a)=1/2`,

whereas

`mu_s^B(a)
 = [(3/4)e^{-s} + (1/2)e^{-2s}] / [e^{-s}+2e^{-2s}],`

which equals `1/2` only at the isolated value `s=log 2`. Thus the two models have the same height law and the same unweighted position marginal but different position-height joint laws.

This is not a counterexample to the DGFF source problem; it is an exact obstruction to any proposed derivation that uses only the total critical-chaos mass (or the unweighted mean normalized spatial measure).

## 5. B19 — make it an algorithm: exact Laplace–Palm reconstruction theorem

Define, for measurable `A subset D` and `s>0`,

`G_A(s) := E[ Z(A) exp(-sW) ]`,

and `L(s):=E[exp(-sW)]`.

Then the joint maximum law is recovered by the explicit transform

`rho(A,t) = exp(-alpha t) G_A(s(t)).`  (2)

Conversely, knowing `rho(A,t)` for every `A,t` determines every `G_A(s)` because `t -> s(t)` bijects `R` with `(0,infinity)`. In particular,

`G_D(s) = E[W e^{-sW}] = -L'(s)`,

so the height marginal determines the Laplace transform, hence the law, of `W`; the spatial part requires the entire measure-valued family `A -> G_A(s)` for all `s>0`.

Therefore Problem 16.4 can be reformulated exactly as:

> identify explicitly the first Laplace–Palm transform of the critical LQG measure, `E[Z(dx)e^{-sZ(D)}]`, simultaneously for all `s>0`, or derive a closed uniquely solvable PDE carrying the same information.

This is a stronger diagnostic than “the total mass is unknown”: even a complete scalar law for `Z(D)` would settle only the height marginal, not the source joint density.

## 6. B25 — count the same highest atom two ways: exponential-race representation and an independence criterion

Conditional on `Z`, the number of atoms above height `t` is Poisson with mean

`(W/alpha) exp(-alpha t)`.

Hence, if `E` is a unit exponential random variable independent of `Z`, the conditional maximum admits the exact representation

`T = (1/alpha)[ log(W/alpha) - log E ]`,

and, conditional on `Z`, the maximizing location is distributed as `M=Z/W` and is independent of `E`.

This reproduces (2) by a second count and gives an exact criterion for when limiting maximum location and height can be independent.

For every measurable `A`, let

`q_A(w):=E[M(A) | W=w]`.

From (1), `X` and `T` are independent with location law `mu` if and only if

`E[ W(q_A(W)-mu(A)) e^{-sW} ] = 0`  for every `s>0` and every `A`.

Fix any `s0>0`. Multiplying the signed measure

`w(q_A(w)-mu(A)) P_W(dw)`

by `e^{-s0 w}` makes it finite. Vanishing of its Laplace transform for all positive shifts and uniqueness of Laplace transforms imply

`q_A(W)=mu(A)` almost surely.

Thus

`X independent of T`

is equivalent to

`E[M(A)|W]=mu(A)` a.s. for every measurable `A`.

So every nontrivial position-height dependence in `rho^D` is precisely a Laplace-visible dependence between the normalized critical measure and its total mass. A PDE for `rho^D` must encode that dependence; it cannot be reconstructed from the total-mass law alone.

## 7. Admission disposition

This run does not claim novelty for the Cox-process identities; the source already contains the extremal-process representation, and the new contribution here is the exact admission-side decomposition/identifiability obstruction. The calculation does not solve Problem 16.4.

Disposition:

- `P0462`: **RETIRED_ROUTE_HISTORY_RECOVERED / DO_NOT_CONTINUE**. Current R7-05 claim is a reconciliation defect, not a valid resurrection.
- `P0469`: **HARD / OPEN-LOOKING / NOT CLOSABLE FOR R7-05**. No canonical claim is created.
- `P0471`: the next residue-4 DGFF candidate is a deep-cluster asymptotic/Tauberian theorem and remains HARD-shaped in the campaign record.
- `P0478`: the later residue-4 DGFF candidate is a joint Liouville-Langevin continuum-limit problem and is explicitly HARD-shaped in neighboring admission screens.
- previously screened residue-4 I/D/E/F/G/H candidates remain claimed, held, known, broad, or retired; no stale row is treated as release.

R7-05 therefore returns honestly to `PENDING_ADMISSION` with `UNKNOWN/UNMEASURED` successor metric and no inherited stagnation count.

## 8. Source/current-status notes

Primary source checked 2026-09-19:

- Marek Biskup, *Extrema of the two-dimensional Discrete Gaussian Free Field*, PIMS-CRM notes, Problem 16.4: `https://www.math.ucla.edu/~biskup/PDFs/papers/PIMS-notes.pdf`.

Later work checked in the bounded search:

- Biskup, Gufler, Louidor, *Near-maxima of the two-dimensional discrete Gaussian free field*, Ann. Inst. H. Poincaré Probab. Statist. 60 (2024), 281–311, DOI `10.1214/23-AIHP1418`.
- Biskup–Louidor extremal-process work giving the Cox/critical-measure representation.

No source-matching later explicit formula or uniquely characterizing PDE for Problem 16.4 was recovered in the bounded search. This is not proof of worldwide openness or novelty.

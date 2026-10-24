Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 maximum was requested, but this run has no authenticated GPT-6/max-effort selector or receipt, so I do not claim it. SOURCE-LEVEL canonical metric: NO MOVEMENT, `c_*=0 -> 0`. Auxiliary source-valid reflected strict-triangle scope improves from the currently certified closed cone `|y|>=1.6377x` to `|y|>=1.6374x`; the fixed retitled ten-local mechanism has analytic critical slope in `(1.6373287467706215, 1.6373287467706372)`. Three materially different attacks were: exact 4-state nonbacktracking negation test (too weak), retitled ten-local Collatz dual (success), and P20 single-edge Busemann/HJB residual mass (freshness fixed, path-unavoidability still unpaid).**

# PROB10-10 — retitled ten-local self-avoidance dual after the strip-9 axis improvement

Status: **PARTIAL / OPEN** for the full Auffinger--Damron--Hanson strict-convexity problem. The restricted theorem below is **CANDIDATE_PROVED**, conditional on the already recorded P04 strip-9 axis theorem and pending independent validation. It does not prove global strict convexity.

## 1. Frozen source, exact statement, and metrics

The model remains nearest-neighbor **undirected** FPP on `Z^2` with iid physical-edge weights `Exp(1)`. Write `T(x,y)` for unrestricted passage time and `mu` for the deterministic time-constant norm.

Primary source: Auffinger--Damron--Hanson, *50 years of first passage percolation*, arXiv:1511.03262v2, Question 4 in §2.5.1 (also catalogued as Question 4 in §8):

> “Show that if F is a continuous distribution then the limit shape is strictly convex.”

The canonical repository claim freezes `F=Exp(1)` and the square lattice. The source-facing milestone remains

`Delta_12 := 2 mu(e1)-mu(1,1)`

and

`c_* := sup{c>=0: Delta_12>=c is rigorously proved in the canonical track}`.

- source metric before: `c_*=0`;
- source metric after: `c_*=0`.

Thus the full source remains **OPEN**.

The separate restricted-direction metric is the smallest slope boundary for which the reflected strict triangle family

`mu(x,y)+mu(x,-y) > mu(2x,0)`

is proved uniformly for every `x>0`.

Immediately before this run, P04's newest strip-9 report gave the clean closed cone

`|y| >= 1.6377 x`

and a scalar critical boundary between `1.6376495` and `1.6376496` when combined with the previous canonical ten-local tilt.

This run changes the **dual anisotropic tilt of the ten-local all-path compiler** and obtains

`|y| >= (8187/5000)x = 1.6374 x`

with uniform infinite-volume defect

`delta = 1/62500 = 0.000016`

per unit horizontal scale. The analytic critical slope of this newly fixed compiler is rigorously bracketed by

`1.6373287467706215 < rho_* < 1.6373287467706372`.

This is restricted-direction progress only.

## 2. Continuity, predecessor handoff, ownership, and histories consumed

The required immutable predecessor handoff already exists and was re-read rather than duplicated:

`runs/prob10_2026-09-20/PROB10-10/20260919T2321Z__handoff-hard7-03-d0025.md`

(blob `1a7045aaf81930242664b944b6f0ab09f791c4c1`). It preserves HARD7-03's actual Seppäläinen/D0025 particle-system successor, its exact four-step sign atlas, plateau-half-width improvement, artifacts, and failure history. Nothing in D0025 is overwritten here.

Consumed current state:

- `operations/PROB10_2026-09-20.md`;
- root `POSTED.md`;
- `operations/claims/PROB10-10.md`, blob `6fca778a3608f973175577e9852a61dcd6754c55`;
- newest canonical report before this run, `runs/prob10_2026-09-20/PROB10-10/20260920T0820Z__critical-threshold-cone-163952.md`;
- newest P04 report, `proofnet24/P04-progress-curvature/runs/2026-09-20/2026-09-20T08-45-54Z__moving-strip9-cone16377.md`;
- newest P20 report, `proofnet24/P20-progress-fpp/runs/2026-09-20/2026-09-20T09-18-00Z__single-edge-residual-clock-compiler.md`;
- R08's retired curvature chain, in particular `runs/R08/20260916T1623Z_stuck_diagblock_4c19a7.md`;
- R07's distinct KPZ/fluctuation history, in particular `runs/R07/2026-09-16T1525Z_kpz_deep_edges_03.md`.

The R08 failures remain binding and are not reset: shared bypasses defeat naive multiplication of local surgeries; finite cylinder events can have exact finite triangle equality; and old fixed-corner blocks do not pay the axis/diagonal threshold. R07's fluctuation statements are not imported as curvature.

Ownership remains complementary: PROB10-10 is the canonical parent; P04 owns the dependence-controlled moving-strip axis construction; P20 owns the Busemann/HJB residual route. This run changes only the canonical all-path entropy dual and consumes P04's newest cap.

## 3. Current literature gate

A fresh bounded search on 20 September 2026 rechecked the exact ADH statement and found no source-level closure of ordinary iid `Exp(1)`, nearest-neighbor, undirected `Z^2` strict convexity.

Relevant boundaries remain:

- ADH arXiv:1511.03262v2 explicitly lists Question 4 as above and §2.8 discusses strict convexity as conjectural;
- Jacquet, arXiv:2412.20779, proves strict inequality between unrestricted and directed FPP time constants, not the direction-to-direction strict triangle inequality here;
- the Dembin--Elboim--Peled planar coalescence route used in the repository requires extra limit-shape information and therefore cannot be used circularly to supply the missing strict convexity.

Searches also included `strict convexity first-passage percolation Exp(1) Z2` and 2025--2026 variants. This is bounded negative search evidence, not an exhaustive novelty certificate.

## 4. Idea before code and three materially different attacks

The idea was persisted before the checker at

`artifacts/prob10_2026-09-20/PROB10-10/20260920T0950Z__idea-retitled-ten-local-dual.md`

creation commit `ffdb14790a156b7a62e54cc5c0b62afd81362fd9`.

### Attack A — exact 4-state nonbacktracking dual: NEGATION TEST / TOO WEAK

A self-avoiding geodesic is nonbacktracking, so one can replace the ten-local automaton by the exact four-state nonbacktracking transfer and optimize horizontal/vertical exponential tilts. This is attractive because its Perron root is inexpensive and fully global.

The numerical optimization gives a best critical slope about `1.68029` against the current axis cap, strictly worse than the already certified `1.6376495...`. This was used only as a route-selection diagnostic, not promoted as an exact theorem. It shows that the improvement must use genuine longer-loop exclusion rather than merely forbidding immediate reversals.

### Attack B — retitled ten-local Collatz dual: SUCCESS

The previous canonical report proved an exact barrier only **after** fixing its old `(A,B,r)`. P04 has since changed the axis cost from `a8` to the sharper strip-9 cap. Therefore re-optimize the anisotropic weights of the ten-local transfer itself.

A Perron search proposed approximately

`A=1.975886`, `B=2.767213`.

The checker then moved to the nearby simple rational point

`A=247/125=1.976`,
`B=2767/1000=2.767`,

and certified a positive integer Collatz vector for

`r=24934561/5000000=4.9869122`.

This changes the weighted all-path theorem, rather than microtuning `s,c` under the old fixed theorem.

### Attack C — single-edge Busemann/HJB residual mass: PROMISING / SOURCE GAP IDENTIFIED

P20's newest result removes the earlier whole-star freshness obstruction. A selected active edge needs only one unobserved exponential residual clock, giving the sharp local modulus

`f(p)=p+(1-p)log(1-p) >= p^2/2`.

Its finite-to-infinite compiler would prove `Delta_12>0` if one can force total charged probability mass along the **actual axis geodesic** above the `sqrt(n log n)` error budget. The missing theorem is still geometric: a source-valid lower bound on the frequency/mass of edges where the axis Bellman policy and the diagonal-target policy disagree. P04's strip path is a constructed competitor, not the actual axis geodesic, so it cannot simply be substituted. No conditional source claim is promoted.

A direct diagonal-block route remains quantitatively far from the old frozen-pair target and was not used for another finite-size fit.

## 5. Consumed strip-9 axis theorem

P04's newest dependence-controlled moving-centered construction proves

`mu(e1) <= a9`,

where

`a9 = 13247968739227/22500000000000`

`   = 0.5887986106323111...`.

More quantitatively, for every integer `N>=1`,

`E T(0,9N e1) <= 9N a9 + sqrt(N pbar)`,

with

`pbar = 631541/1000000`.

The proof uses disjoint horizontal departure-column edge sets for consecutive adaptive slabs, reflection to make the transverse increment mean zero, and fresh terminal-column repair. This is consumed P04 work, not relabeled as canonical work.

## 6. Retitled ten-local transfer theorem

A ten-step direction word is admissible when its eleven visited vertices are pairwise distinct. Let `S_10` be the set of admissible words. Every globally self-avoiding nearest-neighbor path is ten-local admissible.

Give appended directions the weights

`w_E=A`, `w_W=A^{-1}`, `w_N=B`, `w_S=B^{-1}`

with the rational `A,B` above. Let `M` be the transfer matrix on `S_10` that appends one admissible direction with its corresponding weight.

The exact checker enumerates

`|S_10|=44100`,

`120292` directed transitions,

and `200` terminal dead-end states. Floating arithmetic is used only to propose a positive integer vector `z`. Exact `Fraction` arithmetic then verifies

`Mz <= r z` componentwise

with

`max_i (Mz)_i/z_i = 105444677584250/21144282194621`

and exact positive slack

`r-max_i(Mz)_i/z_i`

`=6261741196381/105721410973105000000 > 0`.

Let `L_l` be the total tilted weight of all length-`l` ten-local-admissible direction sequences. For `l>=10`, positivity of `z` and the Collatz inequality give

`L_l <= K r^l`

for

`K=(a^T z)/r^10`,

where `a_sigma` is the product of the first ten step weights in state `sigma`. The checker enumerates genuine SAWs for `l=1,...,9` and verifies that the same `K` covers every startup case. Numerically `K=1.0335308243074398e14...`; the exact object is retained as a `Fraction` during execution.

Now let `N_l(M,R)` be the number of globally self-avoiding `l`-edge paths from `(0,0)` to `(M,R)`, with `M,R>=0`. Every such path has tilted product exactly

`A^M B^R`,

because its horizontal and vertical signed displacements are `M,R`. Therefore

`N_l(M,R) A^M B^R <= L_l <= K r^l`,

hence

`N_l(M,R) <= K r^l A^{-M} B^{-R}`.      (6.1)

This is an all-length theorem, not a finite path sample.

## 7. Lower-tail compiler and explicit finite-to-infinite error

Fix `rho>=rho0:=8187/5000`, initially rational, and take integer `M` with `R=rho M` integral. Every geodesic is self-avoiding because all weights are strictly positive. For a fixed `l`-edge self-avoiding path, its physical edges are distinct, so its passage sum is `Gamma(l,1)`.

Choose

`s = r-1+3/100000`,
`q = r/(1+s) < 1`,

and

`c = a9+1/125000`.

Chernoff gives, for each fixed path,

`P(Gamma(l,1) <= cM) <= exp(scM)(1+s)^{-l}`.

Every path from `(0,0)` to `(M,R)` has `l>=M+R=(1+rho)M`. Combining with (6.1),

`P(T(0,(M,R)) <= cM)`

`<= [K/(1-q)] [A^{-1} B^{-rho} exp(sc) q^{1+rho}]^M`.

Write

`C:=K/(1-q)`

and

`beta(rho):=A^{-1} B^{-rho} exp(sc) q^{1+rho}`.

Because `q<1<B`, `beta(rho)` is decreasing in `rho`. The exact logarithmic checker proves at `rho0`

`log beta(rho0) < log(99997/100000) < 0`.

Therefore, uniformly for every `rho>=rho0`,

`P(T(0,(M,rho M)) <= cM) <= C (99997/100000)^M`,

and hence

`E T(0,(M,rho M))`

`>= cM [1-C(99997/100000)^M]`.          (7.1)

Divide by `M` along multiples and use `L^1` convergence to the time constant. For rational `rho>=rho0`,

`mu(1,rho) >= c`.

Continuity of the norm extends this to every real `rho>=rho0`; reflection gives the same bound for `mu(1,-rho)`.

The consumed strip-9 theorem gives `mu(2,0)<=2a9`. Consequently

`mu(1,rho)+mu(1,-rho)-mu(2,0)`

`>=2(c-a9)=1/62500`.                    (7.2)

Homogeneity proves the new closed-cone theorem below.

The requested finite-to-infinite error is also explicit. If `M` is a multiple of `9` (and chosen so `rho M` is integral), apply P04's finite axis bound to distance `2M`, i.e. `N=2M/9`. Combining it with the two reflected copies of (7.1) yields

`[ E T(0,(M,rho M)) + E T(0,(M,-rho M)) - E T(0,2M e1) ] / M`

`>= 1/62500`

`   - 2 c C (99997/100000)^M`

`   - sqrt(2 pbar/(9M))`.               (7.3)

Every term is displayed and tends to its claimed limit. No finite-size shape fit is being converted into an asymptotic theorem.

## 8. New restricted theorem

### PROB10-10-T8-RETILTED-CONE-16374 — CANDIDATE_PROVED / PARTIAL

For iid rate-one exponential edge weights in undirected nearest-neighbor FPP on `Z^2`, assuming the consumed P04 strip-9 axis theorem, for every real `x>0` and every `y` with

`|y| >= (8187/5000)x`,

one has

`mu(x,y)+mu(x,-y)-mu(2x,0) >= x/62500 > 0`.

Square-lattice rotations and reflections give the corresponding symmetric copies.

This does **not** imply strict convexity of the whole limit shape and does not move `c_*`.

## 9. Critical slope of the newly fixed dual

For the new fixed `(A,B,r,a9)`, define

`rho_* := (((r-1)a9)-log A)/log B`.

The exact rational logarithm bounds certify

`1.6373287467706215 < rho_* < 1.6373287467706372`.

Why this is the scalar boundary for this fixed retitled transfer: as `s downarrow r-1`, the best lower-tail level allowed by `beta<1` approaches

`c_max(rho)=[log A+rho log B]/(r-1)`.

Beating the consumed axis cap requires `c_max(rho)>a9`, which is exactly `rho>rho_*`. Thus another `s,c` microtuning with this same `(A,B,r,a9)` cannot cross `rho_*`; a future canonical run must improve the transfer itself again or change mechanism.

The threshold movement relative to the newest P04/old-tilt combination is

`~1.6376495 -> ~1.6373287468`,

while the clean closed cone moves

`1.6377 -> 1.6374`.

## 10. Exact checker, tests, and reproducibility

Idea-before-code:

`artifacts/prob10_2026-09-20/PROB10-10/20260920T0950Z__idea-retitled-ten-local-dual.md`

Exact checker:

`artifacts/prob10_2026-09-20/PROB10-10/20260920T0950Z__retitled_ten_local_dual_exact.py`

Archived executed output:

`artifacts/prob10_2026-09-20/PROB10-10/20260920T0950Z__retitled_ten_local_dual_exact.out`

The checker verifies exact state/transition counts, positivity of the Collatz vector, the componentwise rational Collatz inequality, all startup cases `l<10`, rigorous logarithm enclosures, the critical-slope bracket, the closed-cone lower-tail sign, and `delta=1/62500`. Its final line is

`ALL_EXACT_CHECKS_PASS = True`.

The nonbacktracking `1.68029` figure in Section 4 is explicitly only a numerical route-selection diagnostic; it is not part of the exact theorem.

## 11. Before/after summary and remaining full-scope gap

**Source-level:** `c_*=0 -> 0`; full strict convexity remains **OPEN**.

**Restricted direction range:** clean reflected cone `1.6377 -> 1.6374`; analytic fixed-mechanism infimum `~1.6376495 -> rho_* in (1.6373287467706215,1.6373287467706372)`.

**Uniform restricted defect at the new clean boundary:** `1/62500` per horizontal unit.

**Finite-to-infinite error:** exactly (7.3), namely

`2 c C (99997/100000)^M + sqrt(2 pbar/(9M))`.

**Main remaining source gap:** obtain a positive strict-triangle defect through the central angular sector, in particular the canonical axis/diagonal quantity `Delta_12`. The most genuinely different current route is P20's single-edge residual-clock compiler plus a new geometric lower bound on charged Bellman-policy disagreement along the actual axis geodesic. No such path-unavoidability theorem is proved here.

No scheduler, email, Drive, public-posting, claim-owner, or other-track file was modified in this run.

Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 maximum was requested, but this runtime exposes no authenticated applied effort selector/receipt.**

# PROB10-10 — asynchronous boundary carry, exact exponential block recursion, and a quantitative negation-first screen

Status: **PARTIAL / OPEN**. Source-level metric `c_*: 0 -> 0`. No claim of full strict convexity and no claim yet that `Delta_12>0`.

## 1. Frozen target and source-facing metric

The model remains nearest-neighbor **undirected** first-passage percolation on `Z^2` with one iid `Exp(1)` weight on every physical edge. Let `mu` be the deterministic time-constant norm. The source is Auffinger--Damron--Hanson, *50 years of first passage percolation*, arXiv:1511.03262, Question 4 / the limit-shape discussion.

The canonical first checkpoint is

`Delta_12 := 2 mu(e1) - mu(1,1)`.

The retained exact auxiliary axis certificate is

`mu(e1) >= b := 3002823/10000000 = 0.3002823`,

so it would suffice for this checkpoint to prove

`mu(1,1) < 2b = 3002823/5000000 = 0.6005646`.

Even that would be only a one-pair **PARTIAL** result; full strict convexity requires every noncollinear boundary pair/direction.

Source-level before/after:

- before: `c_*=0`;
- after: `c_*=0`.

No rigorous directional defect changed in this run.

## 2. Required continuity, ownership, and histories consumed

The HARD7-03 predecessor handoff was already made immutably and was re-read rather than duplicated:

`runs/prob10_2026-09-20/PROB10-10/20260919T2321Z__handoff-hard7-03-d0025.md`

(blob `1a7045aaf81930242664b944b6f0ab09f791c4c1`). It preserves the actual D0025 / Seppalaeinen particle-system successor, its four-step sign atlas, artifacts, and unresolved obstruction. Nothing in that predecessor is overwritten here.

Consumed current state:

- `operations/PROB10_2026-09-20.md`;
- root `POSTED.md`;
- `operations/claims/PROB10-10.md`, blob `6fca778a3608f973175577e9852a61dcd6754c55`;
- preceding canonical report `runs/prob10_2026-09-20/PROB10-10/20260920T1018Z__hard-cone-reset-first-moment-barrier.md`;
- the uncompleted carry idea `artifacts/prob10_2026-09-20/PROB10-10/20260920T1148Z__idea-asynchronous-boundary-carry.md`;
- its strengthened finite-state version `artifacts/prob10_2026-09-20/PROB10-10/20260920T1236Z__idea-finite-state-asynchronous-carry.md`, blob `4731a3f4214959ea5721e143a1299c6ec694928e`;
- complementary P04 report `proofnet24/P04-progress-curvature/runs/2026-09-20/2026-09-20T09-47-23Z__width7-undirected-cone1362.md`, blob `0b14a30ca773496f6467a1ea4c770222459134d5`;
- newest complementary P20 report found on current master, `proofnet24/P20-progress-fpp/runs/2026-09-20/2026-09-20T11-15-00Z__jacquet-backtrack-residual-collapse.md`;
- R08 axis certificate `runs/R08/20260916T1528Z_fpp_axis_transition_3b7c92.md`;
- R08 stuck report `runs/R08/20260916T1623Z_stuck_diagblock_4c19a7.md`;
- distinct R07 fluctuation report `runs/R07/2026-09-16T1525Z_kpz_deep_edges_03.md`.

The binding failures are unchanged: shared bypasses invalidate naive multiplication of local surgery savings; pointwise finite strictness fails on positive-probability cylinder events; old fixed-corner blocks did not cross the axis/diagonal checkpoint; and R07 fluctuation/KPZ statements are not curvature theorems. The 10:18Z owner report additionally proved that the recent reflected-cone inequalities are compatible with the `l1` diamond and hence are not source-facing progress, and that the first-moment SAW/Chernoff architecture cannot reach the diagonal at the current cap because monotone E/N paths already overwhelm its union bound for coefficients at least `58/125`.

Ownership remains nonduplicating: PROB10-10 owns the parent; P04's valid finite-block upper constructions are complementary; P20 owns the actual-geodesic/Busemann residual lane. No claim file is edited because the source metric did not move.

## 3. Fresh bounded source/prior-art gate

A fresh bounded search on 20 September 2026 found no unconditional theorem closing strict convexity for ordinary iid `Exp(1)`, nearest-neighbor, undirected FPP on `Z^2`.

Relevant primary boundaries checked:

- Auffinger--Damron--Hanson, arXiv:1511.03262: source/open-problem navigation;
- Dembin--Elboim--Peled, arXiv:2204.02332: quantitative coalescence assumes more than 32 extreme points of the limit shape (except for particular distribution families), so it does not supply the missing Exp(1) shape property without an additional input;
- Jacquet, arXiv:2412.20779: proves strict unrestricted-versus-directed time-constant comparison, not `2mu(e1)>mu(1,1)`;
- Krishnan, arXiv:1406.1108 / CPAM 2016: exact HJB/duality variational formula and corrector iteration, but no strict-convexity deduction for this specific lattice exponential model was found;
- Alm--Parviainen (CPC 2002): prior transition-matrix bounds/numerics for square-lattice time constants;
- Renlund, arXiv:1002.3709 / CPC 2010: exact Markov-chain calculation for the width-two exponential ladder.

Thus finite-state exponential-front machinery is prior art in spirit. No novelty claim is made from the bounded search. What matters here is whether it can be turned into a source-valid numerical certificate at the frozen `0.6005646` threshold.

## 4. Three materially different approaches compared

### A. Asynchronous antidiagonal carry — pursued

Do not reset to a single terminal after each band. In rotated coordinates

`s=x+y`, `d=x-y`,

partition the strip into edge-disjoint bands `2jL <= s <= 2(j+1)L`, `|d|<=W`, assigning an edge to the band of its lower `s` coordinate. Carry the entire normalized arrival-time profile on the shared antidiagonal. This directly repairs the synchronization loss isolated at 02:18Z.

### B. Exact exponential Richardson recursion — pursued as certificate exactification

Exploit the frozen `Exp(1)` law. For ordinary finite first-hit blocks, exponential memorylessness turns passage to a terminal set into a finite continuous-time Richardson growth chain and gives an exact rational recursion, eliminating the generic tail-quadrature obligation. Edge deletion then gives one-sided rigorous upper certificates.

### C. P20 true-geodesic Busemann residual/co-calibration route — retained but not duplicated

P20's 11:15Z report forces linearly many U-backtracking patterns on the **actual axis geodesic**. Under the flat-face hypothesis `Delta_12=0`, its finite-target residual identity forces all but `o(n)` of those occurrences to have vanishing diagonal-target residual. The remaining obstruction is global: rule out a positive-density family of such co-calibrated backtracking segments. This is geometrically distinct from the strip route and remains a credible fallback.

The directed-only strip/Jacquet route was used as a negation control below; more first-moment SAW tuning is not reopened.

## 5. Asynchronous-carry theorem with completely explicit finite-to-infinite error

Let

`D_W={d: |d|<=W, d=0 (mod 2)}`

on even antidiagonals. For a normalized boundary vector `y in [0,infty]^{D_W}` with `min y=0` and a fresh band environment `omega`, define

`F_omega(y)(d') = min_d { y(d) + T_band,omega((0,d),(2L,d')) }`,

`g(y,omega)=min_{d'} F_omega(y)(d')`,

`Phi(y,omega)=F_omega(y)-g(y,omega) 1`.

Let `P` be any projection satisfying

1. `P(y)>=y` coordinatewise, allowing `+infty`;
2. `min P(y)=0` whenever `min y=0`.

Run

`M_{j+1}=M_j+g(Y_j,omega_j)`,

`Y_{j+1}=P(Phi(Y_j,omega_j))`,

from `Y_0(0)=0` and `Y_0(d)=+infty` for `d!=0`.

### Theorem 5.1 — conservative carry domination

For every realization and every `j`, each finite absolute label `M_j+Y_j(d)` is at least the weight of some actual lattice path from the origin to the corresponding boundary vertex using only the first `j` bands. In particular `M_j` is at least the weight of an actual admissible path to the `j`th boundary.

**Proof.** At `j=0` the unique finite label is the zero-cost path at the origin. Assume the claim at boundary `j`. For each finite source label and terminal `d'`, concatenate a witnessing prefix path with a shortest path inside fresh band `j`. Hence `M_j+F_{omega_j}(Y_j)(d')` dominates a genuine concatenated path weight. Writing these labels as their common minimum `M_{j+1}` plus `Phi` changes no absolute label. Applying `P` only raises or deletes normalized labels and preserves at least one zero label. Every surviving label therefore still dominates a genuine path witness. Induction proves the claim. QED.

### Theorem 5.2 — Bellman supersolution compiler

Assume the projected reachable state space admits a real function `h`, bounded below, and a number `lambda` such that for every reachable state `y`,

`E[g(y,omega)+h(P(Phi(y,omega)))]-h(y) <= lambda`.  (5.1)

Then for every `N`,

`E M_N <= N lambda + h(Y_0)-inf h`.                         (5.2)

Moreover, after a final fresh zig-zag correction from the minimizing offset to `d=0`,

`E T(0,(NL,NL))/(NL)`
` <= lambda/L + [h(Y_0)-inf h+W]/(LN)`.                    (5.3)

Consequently

`mu(1,1) <= lambda/L`.                                     (5.4)

**Proof.** Condition (5.1) on the past before band `j`; `omega_j` is independent because the physical edge sets of distinct bands are disjoint. Summing the conditional inequalities telescopes the potential and gives

`E M_N + E h(Y_N) <= N lambda + h(Y_0)`.

Use `h(Y_N)>=inf h` to obtain (5.2).

At the final even antidiagonal `s=2NL`, choose a zero-labelled minimizing offset `d_*`, `|d_*|<=W`. To reduce `d_*` by two while returning to the same antidiagonal, use the two-edge zig-zag through the future side `s=2NL+1`; repeat `|d_*|/2` times. This uses exactly `|d_*|` fresh physical edges, all outside the prior bands. Their conditional expected total weight is `|d_*|<=W`. Theorem 5.1 supplies an actual prefix path of expected cost at most the right side of (5.2). Adding the correction, dividing by `NL`, and taking the usual time-constant limit gives (5.3)--(5.4). QED.

A concrete finite projection is the upward mesh/cutoff map from the 12:36Z idea note: positive coordinates are rounded **up**, and values beyond the cutoff are replaced by `+infty`. Theorem 5.1 proves why this one-sided rounding is safe; it slows the auxiliary process rather than assuming false independence.

This theorem pays the finite-to-infinite error completely. The only missing source-facing ingredient is a certified finite Bellman inequality with `lambda/L<0.6005646`.

## 6. New exact exponential evaluator

The generic rounded Bellman program still has to integrate finite-band passage distributions. For the frozen exponential law there is an exact alternative for ordinary source-to-terminal finite blocks.

Let `G=(V,E)` be a finite graph, `o in V` a source, `A subset V` a nonempty terminal set, and all physical edges iid `Exp(1)`. Put

`q_G := E T_G(o,A)`.

For `S subset V`, define the edge boundary count

`b(S)=#{ {x,y} in E: x in S, y notin S }`,

and for `v notin S`,

`m_S(v)=#{x in S: {x,v} in E}`.

### Theorem 6.1 — exact Richardson recursion

Let `u(S)` be the expected remaining time for the FPP/Richardson infection process, conditional on current infected set `S`, to hit `A`. Then

`u(S)=0` if `S cap A != empty`,

while for `S cap A=empty`,

`u(S) = 1/b(S) + sum_{v notin S} [m_S(v)/b(S)] u(S union {v}).`   (6.1)

The recursion is triangular in `|S|`, has a unique solution, and all `u(S)` are rational. In particular

`q_G=u({o})`                                                  (6.2)

is exactly rational.

**Proof.** Couple FPP with infection growth: an edge clock begins when its first endpoint is infected. Conditional on the entire past and on the event that a currently live boundary edge has not yet fired, the residual duration of its `Exp(1)` weight is again independent `Exp(1)` by memorylessness. Thus when the infected set is `S`, the `b(S)` live boundary clocks have independent rate-one exponential residuals. Their minimum has mean `1/b(S)`. A particular boundary edge is the minimizer with probability `1/b(S)`, so the next infected vertex is `v` with probability `m_S(v)/b(S)`. Conditioning on this first jump gives (6.1). Each transition strictly enlarges `S`, so backward induction on `|V\S|` is triangular and unique. Starting from rational terminal values zero, (6.1) uses only rational arithmetic. QED.

### Corollary 6.2 — edge-deletion upper certificate

If `H` is a connected subgraph of `G` containing `o` and at least one terminal, then

`q_G <= q_H`.                                                (6.3)

Hence any tractable subgraph certificate with `q_H/L<0.6005646`, inserted into the already-proved moving-centered point-to-line compiler, would rigorously prove `Delta_12>0`.

**Proof.** For every fixed edge-weight realization, every `H`-path is a `G`-path, so `T_G(o,A)<=T_H(o,A)`. Take expectations. QED.

This exactification removes exponential-tail truncation and quadrature error for first-hit finite blocks. It does **not** remove state explosion: a useful width/length block can have an enormous infection-set state space. That is now the precise obstruction for this subroute.

## 7. Actual checker and negation-first experiment

Idea was persisted before code at

`artifacts/prob10_2026-09-20/PROB10-10/20260920T1406Z__idea-richardson-exactification.md`.

Executed checker:

`artifacts/prob10_2026-09-20/PROB10-10/20260920T1406Z__richardson_exact_and_carry_screen.py`.

Archived output:

`artifacts/prob10_2026-09-20/PROB10-10/20260920T1406Z__richardson_exact_and_carry_screen.out`.

### Exact core

For the `L=1` rotated undirected point-to-line block the exact Richardson recursion gives:

- `W=1`: `q=5/4`;
- `W=2`: `q=11/12`;
- `W=3`: `q=37643/41472`;
- `W=4`: `q=95513/105840`;
- `W=5`: `q=39916137923/44236800000`;
- `W=6`: `q=213930628381/237105792000`.

The program uses `Fraction`, checks these identities exactly, and ends the exact section with

`EXACT_SMALL_BLOCKS_PASS = True`.

These tiny blocks are far above the source threshold and are only implementation/theorem checks.

### Negation-first asynchronous-carry screen — numerical evidence only

Using `L=1`, `W=40`, 40 independent replicas, each with 100 burn-in bands and 400 retained bands, fixed seeds `90000+r`:

- **undirected within each band**: mean increment per diagonal unit `0.594750583257541`, independent-replica SE `0.001573496608462`;
- **directed-within-band control**: mean `0.615215551480803`, independent-replica SE `0.001718850688863`;
- source checkpoint: `0.6005646`.

So the undirected screen lies about `0.0058140` below the checkpoint, whereas the directed control lies about `0.01465099` above it. This is not a proof and does not alter `c_*`. It does, however, falsify the pessimistic hypothesis that width-40 asynchronous carry obviously lacks quantitative room, and it isolates the useful mechanism: **undirected local backtracking plus carried boundary labels**, not a directed comparison alone.

The output explicitly ends with

`NUMERICAL_SCREEN_IS_NOT_A_PROOF = True`.

## 8. Before/after accounting

### Source-level metric

`c_*: 0 -> 0` for `Delta_12>=c`.

No new rigorously proved strict direction range. Full source scope remains open.

### Rigorous mechanism delta

Before this run, the carry route had a correct conceptual min-plus recursion but no archived completed report/certificate. After this run:

1. conservative upward projection is proved pathwise;
2. a Bellman supersolution yields the explicit finite-size error
   `[h(Y_0)-inf h+W]/(LN)` and infinite-volume bound `mu(1,1)<=lambda/L`;
3. for ordinary finite Exp(1) first-hit blocks, the integration problem is replaced by the exact rational Richardson recursion (6.1);
4. edge deletion gives a one-sided exact finite certificate search space.

### Auxiliary numerical delta

The width-40 asynchronous carry screen is below the source checkpoint, while the directed control is above it. This is only route-selection evidence.

## 9. Remaining full-scope gap and next exact obligation

The immediate checkpoint is still unpaid:

`Delta_12>0`.

For the selected block lane, the cleanest next proof obligation is one of:

1. produce a finite projected-state Bellman supersolution with rigorously enclosed transitions and `lambda/L<0.6005646`; or
2. find a tractable edge-deleted / aggregated exponential strip certificate whose exact Richardson value, combined with the moving-centered compiler, crosses `0.6005646`.

The numerical width-40 screen says such a certificate is not absurd, but the present exact subset recursion is too large at useful widths. State aggregation must be monotone in the correct direction; replacing the full process by an unproved stationary approximation would simply recreate the old dependence error.

For the P20/Busemann lane, the exact remaining global step is different: show that under the flat-face hypothesis a positive-density family of the Jacquet-forced U-backtracks cannot all be asymptotically calibrated for the diagonal target. No local finite pattern alone currently gives that contradiction.

Full ADH strict convexity remains substantially beyond either one-pair checkpoint. A positive `Delta_12` would be PARTIAL and would still need a mechanism covering every relevant direction, plus independent validation before any source-closure claim.

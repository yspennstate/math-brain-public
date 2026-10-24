Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum was requested, but this runtime exposes no authenticated model-family selector, reasoning-effort selector, or completed-run effort telemetry, so I do not claim otherwise. **NO MOVEMENT: I0115 `K_explicit=1 -> 1`. Methods actually used: #5 ADD A PARAMETER AND DIFFERENTIATE IN IT, #12 FIND WHAT IS CONSERVED, #19 MAKE IT AN ALGORITHM.**

# R12 / I0115 — multihit regularization, projective-consistency obstruction, and the finite-depth main-road no-go

Repository/branch: `yspennstate/math-open-problems`, `master`.  
Deployment: `NEW-METHODS-2026-09-16`.  
Status: **OPEN / PARTIAL / second I0115 report**.  
Canonical claim: `operations/claims/I0115.md`.

## 1. Continuity and required state recovery

I did **not** reopen Randomstrasse Conjecture 28 / I0102 despite the stale native task title. The controlling R12 history is the immutable terminal handoff

`runs/R12/2026-09-17T22-49-01Z_i0102_terminal_stuck_handoff_15_8e3a71.md`,

which freezes the Paley metric at `(a,C,p0)=(1/2,1,5)`, records both historical hard stuck recoveries plus the later three-run no-movement cycle, and explicitly sets `next_I0102_recovery_permitted: false` for this assignment. The next report then lawfully admitted and claimed I0115. Restarting Paley here would violate the owner's hard-task rotation rule.

Before doing new mathematics I reread/recovered:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/claims/I0115.md`;
- newest own report `runs/R12/2026-09-17T23-41-44Z_i0115_poisson_fragmentation_01_a4d7c2.md`;
- the terminal I0102 handoff above;
- the neighboring I0115 source screen `runs/R08/20260917T0325Z_rotation_screen_i0115_sirsn_8c2f41.md`;
- exact-ID intake/ownership history for I0115 through repository search.

The frozen source-matching target remains Aldous, *Scale-invariant random spatial networks* (EJP 19 (2014), Open Problem 27), in the objective sufficient interpretation recorded in the claim: construct one genuine SIRSN whose full laws of `span(z1,...,zk)` are explicit for every finite deterministic configuration and projectively consistent in `k`.

The metric remains

`K_explicit` = largest `k` for which one **single genuine SIRSN** has such an explicit full law for every `j<=k`.

Target: infinity. Before this run: `K_explicit=1`. After this run: `K_explicit=1`. The new objects below are exact and useful, but none is yet a genuine SIRSN, so I do not credit them to the source metric.

The first I0115 report explicitly said “no source-metric movement”; including that initialization report, this is the second consecutive no-movement report under the current metric, so the three-run stuck trigger is **not** yet reached.

## 2. Current-source and prior-art check

Fresh 18 September 2026 searches checked:

- Aldous's current SIRSN project page: `https://www.stat.berkeley.edu/~aldous/Research/OP/sirsn.html`;
- Jonas Kahn, *Improper Poisson line process as SIRSN in any dimension*, Ann. Probab. 44 (2016), DOI `10.1214/15-AOP1032` / arXiv:1503.03976;
- Wilfrid Kendall's Poisson-line metric/SIRSN papers;
- Guillaume Blanc, Nicolas Curien and Jonas Kahn, *Geodesics in planar Poisson road random metric*, Proc. London Math. Soc. 131 (2025), DOI `10.1112/plms.70070`;
- Werner Nagel and Eike Biehler, *Consistency of constructions for cell division processes*, Adv. Appl. Prob. 47 (2015), DOI `10.1239/aap/1444308875`.

Aldous's current page still says the Kendall/Kahn Poisson-line constructions develop one aspect while “much work remains.” Blanc--Curien--Kahn 2025 substantially advances the geodesic structure of the Poisson road metric but does not, in the material recovered here, supply explicit arbitrary-`k` laws for full `span(z1,...,zk)` subnetworks. The bounded search again found no source-matching all-`k` formula. This is a dated negative search, **not** a novelty certificate.

The Nagel--Biehler result is a close warning from stochastic geometry: in a broad class of cell-division models, spatial consistency is highly rigid and STIT is singled out. Their notion is not identical to Aldous's label-deletion/projective consistency, so I do not cite it as proving any theorem below; it is the nearest literature analogue I found for the consistency obstruction exposed in this run.

## 3. Inherited exact setup

Use the invariant measure on unoriented affine lines

\[
\mu(dL)=\frac12\,d\theta\,dr
\]

and a Poisson process on line--time pairs with intensity `mu(dL) dt`. For two fixed points `x,y` at Euclidean distance `d`, lines separating them arrive as a rate-`d` Poisson process. Conditional on being a separating line, after rotating the segment to the horizontal axis, its crossing coordinate `U` on `[x,y]` and direction angle `Phi in [0,pi)` satisfy

\[
U\sim \operatorname{Unif}[0,d],\qquad
f_\Phi(\phi)=\frac12\sin\phi,
\tag{3.1}
\]

independently; successive separating-line marks are i.i.d. This is the Crofton mark law proved in the preceding report.

Write `T_m(x,y)` for the arrival time of the `m`-th separating line and `L_1,...,L_m` for the first `m` separating lines.

## 4. Method #5 — add the separator count `m` and locate the exact local thresholds

The preceding report showed that one separator cannot supply a translation-equivariant branch point, two separator lines have an angular `1/|sin Delta Phi|` divergence, while three lines regularize it. I promoted that observation to a complete `m`-parameter statement.

### Theorem R12-S3 — exact finite-`m` local regularization thresholds

For a pair at distance `d`:

1. `T_m` is Gamma with shape `m` and rate `d`. Therefore
   \[
   \mathbb E\,T_m^{-1}=\frac{d}{m-1},\qquad m\ge2,
   \tag{4.1}
   \]
   while `E[T_1^{-1}]=infinity`.
2. Put
   \[
   S_m=\max_{1\le i<j\le m}|\sin(\Phi_i-\Phi_j)|.
   \tag{4.2}
   \]
   For `m>=3`, choose a pair attaining this maximum and let `H_m(x,y)` be the intersection of those two lines. Then
   \[
   \Pr\{S_m\le\varepsilon\}
   \le (\arcsin\varepsilon)^{m-1},
   \tag{4.3}
   \]
   and
   \[
   \mathbb E[S_m^{-1}]
   \le 2+\frac{\pi^{m-1}}{2^{2m-3}(m-2)}.
   \tag{4.4}
   \]
   Consequently
   \[
   \boxed{
   \mathbb E\bigl(|x-H_m|+|H_m-y|\bigr)
   \le
   2d\left(3+\frac{\pi^{m-1}}{2^{2m-3}(m-2)}\right)<\infty.
   }
   \tag{4.5}
   \]
3. For `m=2`, `E[S_2^{-1}]=infinity`. Thus `m=3` is the exact first value at which this best-angle intersection rule has finite mean local detour.

#### Proof

The separating lines form a rate-`d` Poisson process in the time coordinate, so `T_m` is Gamma(`m`, rate `d`). The inverse-moment formula (4.1) is the elementary Gamma integral; the shape-one integral diverges logarithmically at zero.

For (4.3), set `delta=arcsin(epsilon)`. If `S_m<=epsilon`, then, after fixing `Phi_1`, every `Phi_j`, `j>=2`, lies within projective angular distance `delta` of `Phi_1`. This set has total Lebesgue length `2 delta`; since the direction density in (3.1) is bounded by `1/2`, each independent direction lands there with probability at most `delta`. Hence (4.3).

Since `0<S_m<=1`,

\[
\mathbb E[S_m^{-1}]
=1+\int_1^\infty \Pr\{S_m<t^{-1}\}\,dt.
\]

Bound the interval `[1,2]` by one. For `t>=2`, use `arcsin(1/t)<=pi/(2t)` and (4.3):

\[
\begin{aligned}
\mathbb E[S_m^{-1}]
&\le 2+\left(\frac\pi2\right)^{m-1}
\int_2^\infty t^{-(m-1)}dt\\
&=2+\frac{\pi^{m-1}}{2^{2m-3}(m-2)}.
\end{aligned}
\]

If the selected lines cross the chord at `U_i,U_j`, their intersection `H` obeys

\[
|H-(U_i,0)|\le \frac d{S_m},\qquad
|H-(U_j,0)|\le \frac d{S_m},
\]

because `|U_i-U_j|<=d` and the line-intersection formula has denominator `|sin(Phi_i-Phi_j)|=S_m`. Hence

\[
|x-H|+|H-y|\le 2d\left(1+S_m^{-1}\right),
\]

which with (4.4) gives (4.5).

For `m=2`, restrict both angles to a compact interval around `pi/2`, where the density in (3.1) is bounded below. The difference angle then has a density bounded below near zero, so the integral of `1/|sin Delta|` diverges logarithmically. This proves the sharp threshold.

### Interpretation

There are two distinct scale-critical singularities. A portal rule whose intensity is proportional to the line time `T_m` already gets a finite inverse-time mean at `m=2`; an actual two-line intersection still has the angular singularity and needs `m=3`. Thus local finite expected length is not the difficulty anymore once three independent separators are available.

That does **not** construct a SIRSN. The next two sections show why these locally successful finite-`m` repairs cannot simply be inserted into the projectively consistent partition hierarchy from the preceding run.

## 5. Method #12 — the conserved additive separation count kills pairwise multihit partitions

For points `u,v`, let

\[
N_t(u,v)=\#\{(L,s):s\le t,\ L\text{ separates }u\text{ and }v\}.
\]

A tempting delayed-fragmentation rule is

\[
u\sim_{m,t}v\quad\Longleftrightarrow\quad N_t(u,v)<m,
\tag{5.1}
\]

because the pair separation time is then `T_m` and the inverse-time singularity disappears for `m>=2`.

The obstruction is an exact conserved quantity on collinear triples.

### Theorem R12-S4A — no pair-count threshold `m>=2` is a partition rule

Let `x,y,z` be three distinct collinear points with `y` between `x` and `z`. Then, outside the null set of lines passing through `y`,

\[
\boxed{N_t(x,z)=N_t(x,y)+N_t(y,z).}
\tag{5.2}
\]

Moreover the two terms on the right are independent Poisson variables with respective means `t|x-y|` and `t|y-z|`.

For every integer `m>=2` and every `t>0`, relation (5.1) fails transitivity with positive probability.

#### Proof

A line separates the two endpoints of a segment iff it crosses the open segment, up to the null set of lines through an endpoint. The open segments `(x,y)` and `(y,z)` are disjoint, and their union is `(x,z)` modulo the point `y`; therefore the line sets are disjoint and their indicators add, proving (5.2). Poisson restrictions to the two disjoint line sets are independent.

Now take the positive-probability event

\[
N_t(x,y)=m-1,\qquad N_t(y,z)=1.
\]

Then `N_t(x,y)<m` and `N_t(y,z)<m`, but by (5.2), `N_t(x,z)=m`. Hence `x~y` and `y~z` while `x` is not equivalent to `z`. So the delayed pair relation is not an equivalence relation and cannot be the finite-subnetwork partition hierarchy.

This is stronger than a numerical counterexample: it excludes **every** fixed finite threshold `m>=2` for every nondegenerate collinear triple.

## 6. Method #19 — make the obvious repair an algorithm and identify its exact failure

One can repair transitivity by making the delay blockwise instead of pairwise.

**BLOCK-m algorithm.** Start from one block containing the finite input configuration. For each current block, count arriving lines that separate at least two labels of that block. When the count reaches `m`, split that block according to the two half-planes of the `m`-th such line, reset counters in the two children, and continue.

This always produces a genuine nested partition tree. Unfortunately it destroys the other indispensable property: deletion/projective consistency.

### Theorem R12-S4B — BLOCK-m is not deletion consistent for any `m>=2`

Take `x,y,z` collinear with `y` between the other two. There is a positive-probability line-arrival event on which the BLOCK-m partition of `{x,y,z}`, restricted afterward to `{y,z}`, disagrees with the BLOCK-m process run directly on `{y,z}`.

#### Proof

Consider the event that, before any other line separating these three labels,

- the first `m-1` relevant lines cross the open segment `(x,y)` and not `(y,z)`;
- the `m`-th relevant line crosses `(y,z)` and not `(x,y)`.

The two line classes have positive finite rates and are disjoint, so this ordered event has positive probability on a suitable finite time interval.

On the full three-point block, the first `m-1` lines increment the block counter and the `m`-th line triggers a split. Because the triggering line crosses `(y,z)`, the resulting split is `{x,y}|{z}`. Its restriction to `{y,z}` therefore separates `y` and `z`.

If `x` was deleted from the start, the first `m-1` lines do not separate the surviving block `{y,z}` and do not count. The final line is only the **first** relevant line for `{y,z}`, so the BLOCK-m counter is `1<m` and no split occurs. Thus deletion changes the law pathwise on a positive-probability event.

### Consequence of S4A + S4B

The two obvious multihit implementations fail on opposite sides:

- pairwise `m`-hit delaying preserves the pair clocks but loses the partition property;
- blockwise `m`-hit delaying preserves partitions but loses projective deletion consistency.

The original `m=1` Poisson-line fragmentation is exactly the point at which both properties coexist. This explains why the local `m=3` regularization from Section 4 cannot simply be “glued” onto the exact all-`k` partition FDD from the previous run.

## 7. A stronger finite-depth no-go: local finite length still gives infinite main-road intensity

There is a second obstruction even if one ignores the partition issue and simply turns the finite-`m` hub into a pair route.

For `m>=3`, choose the best-angle pair of the first `m` separators as in S3. Let those two lines meet the chord `[x,y]` at `U_i,U_j` and meet each other at `H_m`. Consider the explicit polyline

\[
R_m(x,y)= [x,U_i]\cup [U_i,H_m]_{L_i}
\cup [H_m,U_j]_{L_j}\cup[U_j,y].
\tag{7.1}
\]

It is Euclidean-similarity covariant, completely explicit from finitely many Poisson marks, and by the proof of S3 has finite expected length of order `|x-y|`.

Nevertheless it is maximally bad for Aldous's `p(1)` main-road axiom.

### Theorem R12-S5 — every finite-`m` chord-connector route (7.1) has `p(1)=infinity`

Let the endpoint set be an independent unit-intensity planar Poisson point process, as in the definition of the SIRSN edge-intensity statistic. Form the union of all pair routes (7.1), deleting the unit balls around each route's two endpoints as in the `p(1)` core. The expected one-dimensional length in every bounded set of positive area is infinite. Hence the construction cannot be a SIRSN.

#### Proof

The best-angle choice depends only on the direction marks `Phi_1,...,Phi_m`. The crossing coordinates `U_1,...,U_m` are independent uniforms on `[0,d]`, independent of all direction marks. Therefore the selected crossing `U_i`, measured from endpoint `x`, is itself uniform on `[0,d]`.

For `d>=8`, on the event

\[
U_i\in[d/4,d/2],
\tag{7.2}
\]

which has probability `1/4`, the initial chord connector `[x,U_i]` contains at least `d/4-1 >= d/8` length lying outside both unit endpoint balls: it is farther than one from `x`, while every point up to `d/2` from `x` is at least `d/2>=4` from `y`. Thus, if `C(x,y)` denotes just this retained private chord portion,

\[
\mathbb E\,\mathcal H^1(C(x,y))\ge \frac d{32},\qquad d\ge8.
\tag{7.3}
\]

Almost surely a planar Poisson point process has no three collinear points. Hence chord portions belonging to distinct unordered endpoint pairs lie on distinct affine lines and have zero one-dimensional overlap, apart from isolated crossings. Their union length therefore equals the sum of their lengths up to `H^1`-null intersections.

Let `A` be any bounded Borel set with positive area and let `M(A)` be the total `H^1` length in `A` contributed by these retained chord portions. Campbell--Mecke and translation covariance give

\[
\begin{aligned}
\mathbb E M(A)
&=\frac12\int_{\mathbb R^2}\int_{\mathbb R^2}
\mathbb E\,\mathcal H^1(C(x,y)\cap A)\,dx\,dy\\
&=\frac{|A|}{2}\int_{\mathbb R^2}
\mathbb E\,\mathcal H^1(C(0,z))\,dz.
\end{aligned}
\tag{7.4}
\]

The second equality is Fubini applied to translations of each rectifiable connector. By (7.3), the last integral dominates

\[
\frac1{32}\int_{|z|\ge8}|z|\,dz=\infty.
\]

Therefore `E M(A)=infinity`. Since these private connector pieces already sit inside the route core used in the definition of `p(1)`, the full route network has `p(1)=infinity`.

### What S5 changes

This is the sharpest route diagnosis so far. A finite number of separators can cure all **local** inverse-angle/inverse-time divergences and still fail the genuinely network-level SIRSN condition because the endpoints reach the shared line structure through macroscopic pair-private connectors.

So the next viable construction cannot be finite-depth at an endpoint. It needs an **infinite multiscale access chain accumulating at each endpoint**, so that away from a fixed endpoint ball the route already lies on road pieces shared with other routes. This is exactly the structural feature of the Kahn/Kendall speed-marked Poisson-road geodesics that the finite-separator toy model was missing.

## 8. A positive algorithmic lead that survives this run

The all-`k` Poisson-line fragmentation from the preceding report remains useful as an explicit **combinatorial** skeleton. A more promising way to spatialize it than pairwise `m`-hit delays is to use the actual nested cells of the increasing Poisson-line tessellation:

1. at each time `t`, each point belongs to a convex cell of the line tessellation generated by marks `<=t`;
2. when a cell is first cut by a new line, use a point determined by the **bounded cut segment inside that cell** (for example its midpoint), rather than trying to choose a point from an infinite line alone;
3. connect parent/child cut-points inside the convex child cell and follow the nested cell chain down to an endpoint.

This construction is automatically translation/rotation covariant and label deletion cannot alter the underlying global cells. It therefore repairs exactly the failure in S4B. I am **not** claiming it is a SIRSN: the scale of the common cell at a pair's first split is of order `1/T_1`, so the inherited logarithmic inverse-time divergence may reappear in its branch-point displacement. That integrability question is the next precise calculation, not a theorem in this report.

The point of recording the algorithm is that it is the first route in the I0115 chain that simultaneously has a global shared geometry and pathwise projective consistency; its remaining obstruction is a single quantitative integrability question rather than a logical consistency failure.

## 9. Outcome of the three Section-B moves

- **#5 ADD A PARAMETER AND DIFFERENTIATE IN IT:** succeeded locally. The exact thresholds are `m=2` for inverse-time regularization and `m=3` for best-angle intersection regularization, with the all-`m` bound (4.5).
- **#12 FIND WHAT IS CONSERVED:** succeeded as a no-go. Additivity of separation counts on a collinear triple proves every pairwise threshold `m>=2` is nontransitive.
- **#19 MAKE IT AN ALGORITHM:** produced two decisive tests. BLOCK-m restores partitions but provably breaks deletion consistency, while the explicit finite-`m` polyline has finite expected pair length but provably has `p(1)=infinity`. The surviving next algorithm is the global nested-cell tree, whose first-split integrability remains to be decided.

No code/checker was manufactured: S3--S5 are symbolic all-configuration statements with complete on-page proofs and no finite computational core.

## 10. Status, metric and next route

`K_explicit` remains

\[
\boxed{1\to1.}
\]

I0115 remains **OPEN / PARTIAL**. The new results do not satisfy the frozen metric because they either are an abstract hierarchy or fail a SIRSN axiom. There is no source closure claim and no novelty certification.

The next nonrepeating Section-B moves are **#7 TAKE THE LIMIT, #13 FIND WHAT ONLY INCREASES, #21 ASK WHO ELSE HAS THIS SHAPE**:

- #7: replace every finite-depth endpoint connector by the infinite nested-cell access chain and determine whether the route length from scale `t` to infinity is summable;
- #13: identify a monotone cell functional (candidate: perimeter/diameter times split rate) whose compensator controls total access length;
- #21: compare that compensator with the exact mechanisms used in STIT consistency and in Kahn's speed-marked Poisson-road geodesics, without importing a theorem outside its hypotheses.

If the nested-cell route also has infinite `E D_1`, that will be the simplest unresolved special case for the third I0115 no-movement report and will trigger the Section-I stuck protocol on the following invocation. If it has finite `E D_1`, the next obligation is `p(1)<infinity` for that same global route family.

## 11. Model / scheduler configuration status

Unchanged. The exposed task-control surface has prompt/title/schedule/timing/enablement fields but no binding model-family selector, reasoning-effort selector, guaranteed-duration field, or authenticated completed-run model/effort telemetry. GPT-6 / maximum remains prompt-only. Changing that requires product/runtime support exposing those controls or an authorized owning interface that does.

The historical `You cannot modify this task` issue remains an authorization-context boundary. The lawful workaround is the owning workspace/account context, explicit transfer, or platform support — not task duplication, permission bypass, or a repository edit pretending to modify the scheduler. No scheduler state was changed in this run.

## 12. Structured ledger_delta

```yaml
ledger_delta:
  worker: R12
  source_target: I0115
  source: "David Aldous, Scale-invariant random spatial networks (2014), Open Problem 27"
  lane: HARD_OUTSIDE
  metric: K_explicit
  before: 1
  after: 1
  movement: NO_MOVEMENT
  source_status: OPEN
  report_status: PARTIAL
  consecutive_no_movement_reports_under_current_metric: 2
  methods_this_run: [5, 12, 19]
  new_results:
    - R12-S3: "all-m local regularization; inverse-time threshold m=2, angular-intersection threshold m=3"
    - R12-S4A: "pairwise m-hit relation nontransitive for every m>=2"
    - R12-S4B: "BLOCK-m partition algorithm fails deletion consistency for every m>=2"
    - R12-S5: "finite-m best-angle chord-connector routes have finite mean pair length but p(1)=infinity"
  finite_core: NONE
  checker: NONE
  predecessor_I0102:
    status: TERMINAL_HANDOFF_FOR_R12
    frozen_metric: "(a,C,p0)=(1/2,1,5)"
    reopen_permitted: false
  next_methods: [7, 13, 21]
  next_obligation: "decide ED1 integrability for the global nested-cell access-tree construction"
```

Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO MOVEMENT: `E_FS3: 0 -> 0`, unchanged count `2 -> 3`; Section-B moves actually used: #14 FIND THE GROUP ACTING, #19 MAKE IT AN ALGORITHM, #30 ONE SCALE / ONE DIRECTION AT A TIME.**

# R06 CLOSABLE OUTSIDE — BENJ-2026-FS3 / outer-collar reduction

Run date: 2026-09-17 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.  
Delivery: private GitHub only. No email, Drive, public posting, purchases, permission changes, workflow execution, or scheduler mutation.

## 1. Continuity, ownership, original R06 source, and frozen metric

I continued from the current canonical R06 successor claim `operations/claims/BENJ-2026-FS3.md` and the preceding own report

`runs/R06/20260917T2118Z_benj_fs3_finsler_pappus_web_26.md`.

The historical native-title source is Russell Lyons and Yuval Peres, *Probability on Trees and Networks*, Question 6.20 / intake I0056. Its exact retained scope is: determine `Phi_V(G)` for regular co-regular plane graphs, and `Phi_E(G), Phi_V(G)` for more general transitive plane graphs. The R06 frozen subtarget was the `{5,5}` regular tessellation `H_{5,5}`; its certified interval is already the point interval `[sqrt(5),sqrt(5)]`, width zero. The full source question remains PARTIAL, and the triangular/quadrangular cases covered by Haslegrave--Panagiotis are prior art and remain excluded. I0056 rotated after its required unchanged-run limit and is **not reopened here**.

The active, create-only R06 successor is:

Itai Benjamini, *Euclidean vs Graph Metric: The Fixed-Source Problem*, arXiv:2606.13271v2 (June 2026), Section 7, Question 1.

For three non-collinear sources `S={p_1,p_2,p_3}` it asks for a bounded-degree planar graph drawn in `R^2`, with vertex set a `10`-net containing the sources and all graph edges of graph length one, such that

`d_G(p_i,x)=|p_i-x|+O(1)`

for every graph vertex `x` and every `i`, with additive error independent of scale.

Frozen metric:

`E_FS3 in {0,1}` = whether exact Question 1 has a complete source-level decision under the frozen hypotheses.

Entering value: `0`.  
Leaving value: `0`.  
Unchanged count: `2 -> 3`.

The preceding report proved exact continuous compatibility via a Finsler calibration, exposed a flat Pappus three-pencil web, and bounded coarse foreign-shell crossings. It left the global discrete planarization as the sole source-level obstruction and selected the three methods used below.

## 2. Required repository reread and exclusions

Before new mathematics I recovered the current campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, the current follow-up implementation manifest `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`, canonical claims `operations/claims/I0056.md` and `operations/claims/BENJ-2026-FS3.md`, the newest own R06 report, and the newest neighboring R07 report visible to repository search (`runs/R07/20260917T2124Z_i0077_dense_escape_chimneys_29.md`). I also rechecked the intake-F source record for `benjamini_fixed_source_2026`.

The large intake JSONL corpus is too large to render byte-for-byte through the connector in one run. I therefore performed exact-ID/source/ownership searches around the active source rather than falsely claiming a visual reread of every unrelated JSONL byte.

No current posted/excluded result duplicates exact Benjamini Question 1, and no competing BENJ claim appeared. Historical R06 targets I0056, I0079 and D0069 remain frozen/rotated and were not restarted.

## 3. Fresh source and current-literature check

Dated check: 2026-09-17.

The current arXiv record for `2606.13271` still states that the paper proves the two-source theorem with a universal additive constant and **asks** whether the analogous statement holds for three non-collinear sources. A bounded fresh search of the exact title, arXiv number, author plus `three non-collinear sources`, and fixed-source phrasing found no later primary source claiming a source-matching positive or negative answer. This is bounded negative evidence only, not a publication-novelty certificate.

The source text defines a `10`-net only by coverage: every point of `R^2` lies within Euclidean distance `10` of a graph vertex. It also explicitly says all graph edges have graph length one and the additive error is independent of scale. Thus no Euclidean edge-length constraint is being silently inserted below.

A newly useful adjacent result is H.-C. Chang and T. Ophelders, *Planar Emulators for Monge Matrices*, CCCG 2020. They construct an edge-weighted planar graph realizing any cyclic-Monge distance matrix exactly among terminals on the outer face. That theorem does **not** solve the present source: our sources are prescribed interior geometric points, the output here must be an unweighted/unit-edge bounded-degree graph whose full vertex set is a planar `10`-net, and I have not proved that the finite-core distance table below satisfies their cyclic-Monge hypothesis. I record it only as a promising language for the next obstruction analysis.

Queries / sources checked included:

- `Itai Benjamini "Euclidean vs Graph Metric: The Fixed-Source Problem" three non-collinear sources 2606.13271`;
- exact-title and exact-question variants, including later-author/citation phrasing;
- `Planar Emulators for Monge Matrices`, cyclic-Monge planar terminal distances, and related planar-distance-Monge terminology.

## 4. Main result: infinity is not the obstruction

The preceding report identified Euclidean infinity as one possible globalization boundary of the Pappus-web chart. This run removes that boundary rigorously.

### Proposition 4.1 — universal outer-collar extension

There is an absolute constant `C_out` with the following property.

Let `S={p_1,...,p_m}` be any fixed finite source set contained in the Euclidean disk `B(0,D)`, where `D>=1`, and put

`R = 4 D^2 + 2 D`.

Let `H` be a finite bounded-degree planar unit-edge graph drawn in the closed disk `B(0,R)` such that:

1. `S subseteq V(H)` and `V(H)` is a `10`-net of `B(0,R)`;
2. for every `p_i in S` and every `v in V(H)`,

   `|d_H(p_i,v)-|p_i-v|| <= C_0`;

3. the outer face of `H` contains gateways `q_1,...,q_N` in cyclic order, where `q_k=R u_k`, the directions `u_k` are the centers of an equal angular partition of the circle into sectors of width at most `1/R`.

Then `H` can be extended outside `B(0,R)`, without changing any edge of `H`, to a locally finite bounded-degree planar unit-edge graph `G` whose vertex set is a `10`-net of all `R^2`, and

`|d_G(p_i,x)-|p_i-x|| <= C_0 + C_out`

for every source `p_i` and every graph vertex `x`.

The degree increase at every old gateway and the maximum degree of every new vertex are bounded by an absolute constant. In particular, the construction and `C_out` do not depend on the dilation scale `D`, on the number of radial layers, or on how far `x` lies from the source set.

### Proof

#### Step 1: first-harmonic asymptotics with a uniform remainder

Write an outer point as `x=r u` with `|u|=1`, `r>=R`, and let `p` be any source, `|p|<=D`. Then

`|r u-p|^2 = (r-p.u)^2 + |p|^2-(p.u)^2`.

Therefore

`|r u-p|-(r-p.u)`

`= (|p|^2-(p.u)^2) / ( |r u-p| + r-p.u )`.

Since `r-p.u >= r-D`, the denominator is at least `2(r-D)`. Hence

`0 <= |r u-p|-(r-p.u) <= D^2/[2(r-D)]`.       (4.1)

For `r>=R=4D^2+2D`, the right side is at most `1/8`.

Partition the circle into

`N = ceil(2 pi R)`

angular sectors and let `u_k` be the center direction of sector `k`. Its angular width is at most `1/R`; hence for every `u` in this sector,

`|p.(u-u_k)| <= D |u-u_k| <= D/R <= 1/4`.       (4.2)

Now put the radial slabs

`A_{k,n}={r u: R+n <= r < R+n+1, u in sector k}`, `n>=0`.

For every `x=r u in A_{k,n}`, equations (4.1)--(4.2), plus `|r-(R+n)|<=1`, give the absolute bound

`||x-p| - [(R+n)-p.u_k]| <= 2`.                 (4.3)

This is simultaneous for every source.

The key point is that the entire source dependence at infinity has collapsed to the first angular harmonic `-p.u_k`; there is no radial error accumulation.

#### Step 2: a bounded-degree 10-net tree in one sector

Fix one sector `k`. For each `n>=0`, choose a horizontal/radial generation `P_{k,n}` on the middle circle of the slab `A_{k,n}` with points ordered by angle and with consecutive points at Euclidean arc distance at most `4`. One explicit choice is

`m_n = max(1, ceil((R+n+1/2)/(4R)))`

points equally spaced across the sector.

Because the sector width is at most `1/R`, every point of `A_{k,n}` lies within Euclidean distance `<5` of some point of `P_{k,n}`. Also `m_{n+1}-m_n` is either `0` or `1`; in particular adjacent generation sizes are uniformly comparable.

Join `P_{k,n}` to `P_{k,n+1}` by an order-preserving parent map: every child has one parent, and when `m_{n+1}=m_n+1`, only one parent acquires a second child. Draw these edges as noncrossing curves inside the annular sector between the two generations. Join the unique first-generation chain to the gateway `q_k` through a constant-size base gadget inside the first slab. Thus the new graph in the sector is a rooted planar tree with root `q_k`, maximum degree at most an absolute constant, and every vertex of generation `n` has graph depth

`n + O(1)`                                                     (4.4)

from `q_k`, where the `O(1)` is universal.

Perform the construction independently in all sectors. The interiors of the sectors are disjoint, so the new drawings are pairwise noncrossing. Each new outer component meets the old graph only at its own gateway. The union of the generation clouds is a `5`-net outside the disk, hence certainly a `10`-net there.

#### Step 3: exact articulation prevents shortcuts

Let `v` be a new vertex in sector `k`, generation `n`. Removing the gateway `q_k` disconnects `v` from `H` and from all other sectors. Therefore **every** graph path from any source `p_i` to `v` must pass through `q_k`, and the outer rooted tree has no alternative shortcut. Consequently

`d_G(p_i,v)=d_H(p_i,q_k)+n+O(1)`.                (4.5)

By the core hypothesis,

`d_H(p_i,q_k)=|p_i-q_k|+O(C_0)`.

Applying (4.3) first at `q_k=R u_k` and then at `v` shows

`|p_i-q_k| = R-p_i.u_k+O(1)`,

`|p_i-v| = R+n-p_i.u_k+O(1)`.

Substitution into (4.5) yields

`d_G(p_i,v)=|p_i-v|+O(C_0+1)`,

with an absolute implied constant, uniformly in `D,n,k,i`. Old core distances are unchanged because every added sector tree is pendant at one gateway. This proves the proposition. `square`

### Corollary 4.2 — scale-uniform finite-core equivalence

For a fixed finite number of sources, the global fixed-source problem is equivalent, up to a universal additive constant, to constructing **uniform finite cores** on disks of radius `R=O(D^2)` with the correct source distances and a controlled outer-face gateway cycle.

For Benjamini's three-source Question 1, Euclidean infinity is therefore **not** an independent obstruction. Any failure must already be visible in a finite but scale-growing core, or in the impossibility of arranging its boundary gateways while retaining the three source metrics.

This corollary is a reduction, not a source solution: the finite core still has radius `Theta(D^2)` and must satisfy the source inequalities with an error independent of `D` at **every core vertex**.

## 5. #14 FIND THE GROUP ACTING — the boundary data live in a 3-dimensional representation

The exact estimate above reveals the relevant symmetry at infinity. Write a homothetic source family as

`p_i=D a_i`

with the triangle shape `a_i` fixed. On the outer circle, after subtracting the common radial term `R`, the required distance profile is

`-p_i.u(theta) = -D[a_i^x cos(theta)+a_i^y sin(theta)]`.

Thus all source-dependent boundary data lie in the span

`span{1, cos(theta), sin(theta)}`,

and rotations act through the ordinary two-dimensional `SO(2)` representation on the first harmonic. There is no growing collection of independent boundary modes as `D` grows.

This gives a concrete finite-core boundary target: realize three first-harmonic terminal profiles on a cyclic boundary with additive `O(1)`, then fill the interior without creating shorter source paths.

## 6. #19 MAKE IT AN ALGORITHM — explicit outer compiler

The proof above is constructive. Given a finite core satisfying Proposition 4.1:

1. set `R=4D^2+2D`;
2. take `N=ceil(2 pi R)` angular sectors;
3. in slab `(k,n)` place `m_n=max(1,ceil((R+n+1/2)/(4R)))` ordered cloud vertices;
4. connect generation `n` to `n+1` by the monotone one-parent map, using the unique extra child exactly when `m_n` increases;
5. attach the sector tree only at `q_k`.

The output is automatically planar, bounded-degree, and a `10`-net, and its source-distance error outside the core is `C_0+O(1)` rather than `C_0+O(n)`. The articulation property is what prevents the usual quantization errors from accumulating.

This is the useful algorithmic lesson of the run: outside a sufficiently large circle, **do not discretize a three-direction web at all**. Give each angular sector one pendant radial tree and encode all three sources only in the finite gateway distances.

## 7. #30 ONE SCALE / ONE DIRECTION AT A TIME — why `R ~ D^2` is the natural cutoff

Equation (4.1) identifies the precise scale of the far-field transition. The second-order correction to the support function is of size

`D^2/r`.

To make it an absolute `O(1)` simultaneously for every source and direction, one needs `r` at least a constant multiple of `D^2`. Thus `R=Theta(D^2)` is not an arbitrary convenience of the proof: it is the scale at which the Euclidean distance functions become uniformly first-harmonic to additive constant accuracy.

The route can therefore be localized sharply:

- inner problem: construct a scale-uniform three-source core through radius `Theta(D^2)`;
- outer problem: solved by Proposition 4.1.

One direction/sector is handled by one rooted tree; all directions glue only through the already-finite core.

## 8. Relation to planar Monge emulators — promising but not yet a theorem here

Chang--Ophelders show that cyclic-Monge terminal-distance matrices admit exact edge-weighted planar emulators with terminals on the outer face. The boundary target in Section 5 is a cyclic family of three first-harmonic profiles, so this is now a more directly shaped adjacent technology than an unrestricted Pappus-web mesh.

However three nontrivial bridges are missing and are **not** asserted:

1. prove an appropriate cyclic-Monge/Kalmanson condition for a source-plus-boundary terminal ordering that respects the prescribed source geometry;
2. convert the resulting weighted emulator to a unit-edge bounded-degree planar graph without losing additive `O(1)` uniformly in `D`;
3. fill the two-dimensional core to a `10`-net while preserving all source distances, rather than only terminal distances.

The next thinking run should examine exactly these bridges rather than produce another local geometric lemma.

## 9. No finite checker manufactured

The new result is an analytic/topological extension lemma with a proof on the page. There is no finite enumeration whose truth would be strengthened by an exact-arithmetic checker. Under the 90/10 rule I therefore did not create a decorative script for inequalities (4.1)--(4.3) or the monotone tree construction. The earlier exact eight-step classifier remains the finite certificate for its own claim.

## 10. Status and mandatory next-run stuck protocol

`E_FS3` remains `0`. Exact source status is therefore **OPEN / PARTIAL**.

This is the **third consecutive unchanged BENJ run**. Under Section I, the **next invocation must be a thinking-only stuck run**, with no new theorem claim. It must state in one displayed formula the finite-core blocker, inventory every attempted route and its precise failure, identify the simplest still-unproved core subcase, and compare with the nearest solved problem in the literature.

The blocker can now be stated cleanly as:

`Find C<infinity independent of D and, for every non-collinear triple S subset B(0,D), a bounded-degree planar unit-edge 10-net core H subset B(0,O(D^2)) such that sup_{i,v in V(H)} |d_H(p_i,v)-|p_i-v|| <= C, with an outer-face gateway cycle.`

Recommended fresh Section-B lenses for that required thinking run: **#11 DUALIZE, #18 SAY IT IN ANOTHER LANGUAGE, #21 ASK WHO ELSE HAS THIS SHAPE**, centered on finite boundary distance matrices / cyclic-Monge emulators, but without claiming the emulator theorem applies until its hypotheses and the unit-edge/net conversion are proved.

## 11. Model / scheduler control status

The operative implementation manifest still records that the exposed scheduler has **no model-family selector, no reasoning-effort selector, no authenticated completed-run model telemetry, and no guaranteed hour-long execution setting**. GPT-6 / maximum therefore remains a request in prompt text, not an enforced or verified runtime setting.

The same manifest records a historical attempt to modify P26 that returned `You cannot modify this task`; other repository records show prompt updates can succeed from a different authorized context. The legitimate workaround is therefore the owning/admin/product-support context that has authority over the protected task. There is no permission bypass here, and this run made no scheduler change.

To make the owner's model requirement genuinely enforceable, the product/backend control surface would need persistent `model` and `reasoning_effort` fields on scheduled tasks plus authenticated run telemetry showing the values actually applied.

## 12. Structured ledger delta

```yaml
ledger_delta:
  track: R06
  active_claim: BENJ-2026-FS3
  source: "Itai Benjamini, Euclidean vs Graph Metric: The Fixed-Source Problem, arXiv:2606.13271v2, Section 7 Question 1"
  predecessor_source: "Lyons-Peres Question 6.20 / I0056 remains rotated; H_{5,5} interval width 0; full source PARTIAL"
  metric: E_FS3
  before: 0
  after: 0
  status: PARTIAL
  unchanged_count_before: 2
  unchanged_count_after: 3
  tried_moves: [14, 19, 30]
  new_result: "Universal outer-collar extension: any uniform finite three-source core through radius O(D^2) with controlled boundary gateways extends to the whole plane with only O(1) additional error; infinity is not an independent obstruction."
  remaining_obligation: "Uniform finite-core construction or obstruction for three non-collinear sources, with bounded degree, planarity, unit graph edges, 10-net coverage, all-vertex source distances, and an outer-face gateway cycle. Next run is mandatory Section-I thinking-only."
  evidence:
    - operations/claims/BENJ-2026-FS3.md
    - runs/R06/20260917T2118Z_benj_fs3_finsler_pappus_web_26.md
    - runs/R06/20260917T2234Z_benj_fs3_outer_collar_reduction_27.md
  audits: []
  novelty: UNVERIFIED
```

Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FROZEN-METRIC MOVEMENT: `A_triangle` stays exactly `(1/4, infinity)`; Section-B methods actually tried this run: #18, #30, #26. This run proves an incidence-stratified transversality theorem for the remaining d=2 six-point decoder: every auxiliary triangle in a compatibility witness is either a genuine neighbor of its intended center or is fully recycled from nuclei already used elsewhere in the six-tuple.**

# NM13-08 — P0408: overlap transversality for the d=2 six-point decoder

Date: 2026-09-18 UTC  
Track: `NM13-08`  
Category: `CLOSABLE OUTSIDE`  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Own namespace: `proofnet24/NM13-08/`  
Source / claim: `P0408`, `operations/claims/P0408.md`

## 1. Runtime/control disclosure

The task prompt requests GPT-6 with maximum reasoning. This invocation actually identifies as **GPT-5.6 Sol**, and the reasoning level exposed to this report is **UNVERIFIED**. I therefore do not claim GPT-6, a binding maximum-reasoning setting, or an hour-long execution.

The exposed task-control interface still offers prompt/title, timing/schedule fields, timing mode, enabled state, and ordinary task update operations, but no bindable model-family selector and no bindable reasoning-effort selector. Thus GPT-6/maximum remains prompt text only in this interface. The current root ledger also records that an earlier `You cannot modify this task` result for P26 was context-specific: a later authorized P/C context successfully updated P26. If such a refusal recurs, the legitimate remedy is the owning/authorized account, workspace, product, API, or admin surface that exposes the needed permission and settings, not task cloning or an access-control bypass. No schedule was created or modified in this run.

## 2. Continuity, ownership, and required repository read

This run **continues** the already admitted P0408 assignment. It does not reopen intake and does not create a second claim.

Before the new attack I reread or targeted-recovered:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized amendment `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- canonical claim `operations/claims/P0408.md`;
- newest own report `proofnet24/NM13-08/runs/2026-09-17/2026-09-17T23-36-24Z__p0408-d2-six-point-decoder.md`;
- newest visible neighboring reports from NM13-07 and NM13-09;
- the P0408 intake/rank/attempt history and exact claim/search hits on current `master`.

Current canonical ownership is unchanged:

- source / claim ID: **P0408**;
- owner: **NM13-08**;
- canonical dedup key: `recovering_an_ideal_voronoi_tessellation_from_vertices_or_its_dual`;
- shard check: `int(SHA256(UTF-8 key),16) mod 13 = 7`;
- claim path: `operations/claims/P0408.md`.

No release, handoff, competing owner, POSTED source closure, campaign closure, or retirement of P0408 was recovered. Repository-wide connector search is indexed and bounded rather than a byte-for-byte replay of every historical commit; no material continuity item needed below was inaccessible.

The preceding two source-relevant advances are preserved rather than re-derived:

1. a complete on-page proof that the **IPDT determines the ideal-nucleus PPP almost surely**, hence source Question 7.2(ii) is proved on page but remains audit-pending;
2. in `d=2`, an exact local-star inversion and dual-foot formula reducing Question 7.2(i) to a no-spurious-six-point compatibility problem.

Neither P26 nor NM13-09 is counted as having audited those claims.

## 3. Exact source and fresh status check

Source: Matteo D'Achille, Nicolas Curien, Nathanaël Enriquez, Russell Lyons, Meltem Ünel, *Ideal Poisson–Voronoi tessellations on hyperbolic spaces*, **Annals of Probability 54(2) (2026), 846–891**, DOI `10.1214/25-AOP1781`.

Question 7.2 (“Equivariant injectivity”) asks whether

1. the map sending an IPVT to its set of vertices is almost surely injective;
2. the map sending an IPVT to its IPDT is almost surely injective.

The current source was rechecked directly. In dimension two the published structural facts used in this run are:

- the IPVT is almost surely face-to-face and normal, and its union of cell boundaries is a geodesic embedding of the 3-regular tree;
- in ball-corona coordinates the source PPP has intensity `Unif(S^1) x Leb(R_+)` and a nucleus `Y=(theta,r)` has separation

  `sep(z,Y)=r/K(z,theta)`,

  where `K(z,theta)=(1-|z|^2)/|z-theta|^2` in `d=2`;
- every Voronoi vertex is therefore almost surely dual to exactly one ideal Delaunay triangle, and every Voronoi edge is dual to the ideal Delaunay edge shared by its two endpoint triangles.

A fresh bounded literature search dated **2026-09-18** used the exact source title together with `Question 7.2`, `equivariant injectivity`, `vertices`, `IPDT`, and later-author queries. It recovered the March 2026 Annals publication, D'Achille–Thäle arXiv:2606.26049 (24 June 2026) on face-volume densities, D'Achille–Khezeli arXiv:2606.30517 (29 June 2026) on convergence and Diestel–Leader IPVTs, and Mellick's 2026 cell-indistinguishability work. None of the recovered later items states a resolution of Question 7.2(i), and the current source still prints Question 7.2 in its future-directions section. This is bounded dated negative evidence only, not proof of worldwide openness or publication novelty. **Publication novelty remains UNVERIFIED.**

## 4. Frozen metric and stuck counter

The canonical claim froze

`A_triangle = {a>0 : the three-nucleus H^2 source-faithful analogue at cube-root boundary directions and marks (a,1,1) has the same full ideal-Delaunay triangle while its Voronoi diagram varies}`.

The first admitted mathematical run proved exactly

`A_triangle=(1/4,infinity)`.

Policy forbids silently replacing this metric by a new decoder count. Therefore:

- **before:** `(1/4,infinity)`;
- **after:** `(1/4,infinity)`;
- frozen-metric movement: **none**;
- consecutive unchanged runs since metric movement: **3**;
- stuck recoveries used: **0**.

This run reaches the three-unchanged trigger. Accordingly the **next NM13-08 invocation must be a Section-I thinking-only stuck-recovery run with no new claim**, even though the present run obtains the theorem below. The present theorem is reported as source-relevant structural progress, not as metric movement.

## 5. Input from the preceding run: the exact compatibility identity

For six distinct IPVT vertices

`v,w,a,b,c,d in H^2`,

consider the proposed local three-stars

`(vw,va,vb)` at `v`, and `(wv,wc,wd)` at `w`.

Let `phi_v` be the smaller angle between the geodesics `va` and `vb`, let `phi_w` be the smaller angle between `wc` and `wd`, and define

`rho_v = log cot(phi_v/2)`,

`rho_w = log cot(phi_w/2)`,

`D=d_H(v,w)`.

The preceding report proved that the two proposed stars have a common candidate ideal Delaunay geodesic across `vw` if and only if

`D in {rho_v+rho_w, |rho_v-rho_w|}`.                       (5.1)

Every true Voronoi edge, with `a,b` and `c,d` chosen as the other true neighbors of its two endpoints, satisfies (5.1). The missing implication was to show that a source-random six-tuple cannot satisfy (5.1) spuriously.

The new route attacks that missing implication through the **incidence pattern of the six dual Delaunay triangles** rather than through raw vertex coordinates.

## 6. New language: six triples of corona nuclei

For every IPVT vertex `x`, let

`T_x = {Y_x^1,Y_x^2,Y_x^3}`

be the unique three-element set of source corona nuclei whose cells meet at `x`; equivalently, `T_x` is the ideal Delaunay triangle dual to `x`.

For one of the four auxiliary vertices `x in {a,b,c,d}`, put

`U_x := union_{y in {v,w,a,b,c,d}\{x}} T_y`

and define its **overlap count**

`m_x := |T_x intersect U_x| in {0,1,2,3}`.

Call `x` **fully recycled** when `m_x=3`: all three nuclei of its dual triangle occur in at least one of the other five selected triangles.

The intended center is

`c(a)=c(b)=v`,  `c(c)=c(d)=w`.

The theorem below says that the continuous Poisson degrees of freedom eliminate `m_x=0,1`, and turn `m_x=2` into genuine adjacency. Only the completely recycled case can evade this local transversality filter.

## 7. General-position lemma for weighted bisectors

### Lemma `NM13-08-P0408-BISECTOR-GENERAL-POSITION-03A`

Almost surely, simultaneously for every IPVT vertex `x` and every pair of distinct source nuclei `Y,Y'`,

> if `x` lies on the weighted source bisector
>
> `sep(x,Y)=sep(x,Y')`,
>
> then `{Y,Y'} subset T_x`.

### Proof

Work on the full-probability normality event. The PPP of corona nuclei is countable, as is the IPVT vertex set, so it is enough to exclude all finite labeled incidence patterns by Mecke/Fubini.

If exactly one of `Y,Y'` is in `T_x`, then that nucleus has the minimum source separation at `x`. Equality forces the other nucleus to attain the same minimum, giving at least four cells through `x`, contrary to normality. Thus this case is impossible on the normality event.

Suppose neither nucleus is in `T_x`. Condition on the three nuclei defining `x`, on `Y=(theta,r)`, and on the direction `theta'` of `Y'=(theta',r')`. The point `x` is now fixed. The equality

`r/K(x,theta) = r'/K(x,theta')`

forces the single radial value

`r' = r K(x,theta')/K(x,theta)`.

The source corona PPP has Lebesgue radial intensity. Hence a specified radial value has intensity measure zero. Integrating the remaining variables with the multivariate Mecke formula gives expected count zero for such incidences in every compact exhaustion. A countable exhaustion of `H^2` proves the simultaneous almost-sure statement. `QED`

This lemma is deliberately stronger than the usual “no four cells meet” genericity: it also excludes a Voronoi vertex lying on an **above-minimum** equality bisector of two unrelated nuclei.

## 8. Transversality with zero or one reused nucleus

The next lemma is the main new source-law input.

### Lemma `NM13-08-P0408-AUX-LOW-OVERLAP-03B`

Fix any one auxiliary role, say `d`, in an ordered six-tuple satisfying the nondegeneracy assumptions of the previous six-point construction. Almost surely there is no compatibility witness satisfying (5.1) with

`m_d <= 1`.

The same statement holds for `a,b,c` by symmetry of the argument.

### Proof

Fix the other five selected dual triangles and all nuclei of `T_d` that are shared with them. The compatibility identity treats the other five geometric vertices as fixed and constrains the location of `d` as follows.

From

`D in {rho_v+rho_w, |rho_v-rho_w|}`

with `rho_v,D` fixed, the value `rho_w` can only be one of the at most three nonnegative numbers

`D-rho_v`, `rho_v+D`, `rho_v-D`,

when the displayed quantity is nonnegative. Since

`rho_w = log cot(phi_w/2)`

is injective in the smaller unoriented angle `phi_w in (0,pi/2]`, each admissible `rho_w` fixes the unoriented line `wd` to at most two geodesic lines through `w` making the required angle with the fixed line `wc`.

Therefore, after the other five vertices are fixed, every `d` that can satisfy (5.1) lies in a **finite union of complete geodesic lines through `w`**. Call this one-dimensional set `E`. It has hyperbolic area zero.

It remains to show that when `T_d` has at least two private nuclei, the source PPP does not put its triple vertex on an area-zero set.

#### Case `m_d=1`

Let `Y_0=(theta_0,r_0)` be the unique reused nucleus, and let the two private nuclei have directions `theta_1,theta_2` and radial marks `r_1,r_2`. If their three cells meet at `z`, then equality of the three source separations forces

`r_i = r_0 K(z,theta_i)/K(z,theta_0)`,  `i=1,2`.              (8.1)

Condition on `Y_0`, on the two private directions, and on all other nuclei in the six-tuple. On every compact set of `z`, the map

`z -> (r_1,r_2)`

specified by (8.1) is smooth, hence locally Lipschitz. A two-dimensional area-null subset of `H^2` therefore has two-dimensional Lebesgue-null image in the `(r_1,r_2)` plane. Since the two private radial coordinates have product Lebesgue intensity, the set of private radial pairs that can place the triple vertex in `E` has intensity zero. Integrating directions and the conditioned variables by Mecke/Fubini preserves zero.

#### Case `m_d=0`

All three nuclei are private. Condition on their three distinct directions. If their common triple point is `z` and their common separation is `s>0`, then necessarily

`r_i = s K(z,theta_i)`,  `i=1,2,3`.                           (8.2)

On compact `z`-sets and bounded `s`-intervals, the map

`(z,s) -> (r_1,r_2,r_3)`

is smooth and locally Lipschitz. Because `E` has two-dimensional area zero, `E x (0,infinity)` has three-dimensional Lebesgue measure zero after a countable bounded-`s` exhaustion, and its image under (8.2) has three-dimensional Lebesgue measure zero. The three private radial marks have product Lebesgue intensity, so again the Mecke integral is zero.

The extra conditions saying that the specified triples are *actual* Delaunay triangles / Voronoi vertices are merely measurable indicators bounded by one and cannot enlarge these null sets.

There are finitely many labeled identifications among the 18 triangle slots of an ordered six-tuple. Applying the preceding zero-integral argument to every incidence pattern and then taking a countable spatial exhaustion proves that no such `m_d<=1` witness occurs almost surely. `QED`

The proof uses only the source's exact corona intensity and separation formula. No independence assertion about the derived vertex process is made.

## 9. Exactly two reused nuclei force the intended true edge

### Lemma `NM13-08-P0408-AUX-TWO-OVERLAP-03C`

In an ordered compatibility witness satisfying (5.1), suppose an auxiliary vertex has exactly two reused nuclei. Then almost surely it is a true Voronoi neighbor of its intended center.

Concretely:

- if `m_a=2` or `m_b=2`, that vertex is a true neighbor of `v`;
- if `m_c=2` or `m_d=2`, that vertex is a true neighbor of `w`.

### Proof for `d`

Write

`T_d={Y_0,Y_1,Y_2}`

where `Y_0,Y_1` are the two reused nuclei and `Y_2` is the unique private nucleus. Let `L=L(Y_0,Y_1)` be the complete weighted Voronoi bisector

`sep(z,Y_0)=sep(z,Y_1)`.

Every possible triple vertex formed by `Y_0,Y_1,Y_2` lies on `L`.

As in Lemma 03B, after the other five vertices are fixed, compatibility (5.1) restricts `d` to a finite union `E` of geodesic lines through `w`.

Condition on `Y_0,Y_1`, on the direction `theta_2` of the private nucleus, and on all other six-tuple nuclei. Along `L`, the radial mark required for a triple point at `z` is

`r_2 = r_0 K(z,theta_2)/K(z,theta_0)`.                       (9.1)

On compact subarcs of `L`, the right-hand side is a smooth function of arclength. Hence a one-dimensional length-null subset of `L` has one-dimensional Lebesgue-null image under (9.1). Because `r_2` has Lebesgue intensity, the triple point cannot fall in a length-null subset of `L` with positive Mecke measure.

Therefore a positive-measure compatibility pattern can survive only if one of the finitely many target geodesics in `E` **coincides identically with `L`**. Every target geodesic passes through `w`, so this forces

`w in L`,

that is,

`sep(w,Y_0)=sep(w,Y_1)`.

By Lemma 03A, almost surely this implies

`{Y_0,Y_1} subset T_w`.

Thus the Delaunay triangles `T_d` and `T_w` share the full ideal Delaunay edge `{Y_0,Y_1}`. Source Voronoi–Delaunay duality then says their dual Voronoi vertices `d,w` are the two endpoints of the corresponding Voronoi edge. Hence `d` is a true neighbor of `w`.

The roles of `a,b,c` are identical after replacing the intended center. `QED`

## 10. Main theorem — every auxiliary is genuine or fully recycled

### Theorem `NM13-08-P0408-SIXPOINT-OVERLAP-TRANSVERSALITY-03`

For the planar IPVT, almost surely **simultaneously for every ordered six-tuple of distinct vertices** satisfying the six-point nondegeneracy assumptions and compatibility identity (5.1), each auxiliary vertex obeys the dichotomy

> **either** it is a true Voronoi neighbor of its intended center,
>
> **or** its entire dual Delaunay triangle is fully recycled, i.e. all three of its nuclei occur in the union of the other five selected dual triangles.

Equivalently, for each auxiliary `x in {a,b,c,d}`:

- `m_x=0` or `m_x=1` is almost surely impossible;
- `m_x=2` forces the true intended edge `x--c(x)`;
- only `m_x=3` remains unclassified by this local transversality argument.

### Proof

Combine Lemmas 03B and 03C for each of the four auxiliary roles. The simultaneous statement follows from the finite incidence-pattern enumeration and countable spatial exhaustion already used in the lemmas. `QED`

### Source-relevant consequence

The previous no-spurious-six-point obligation was an unconstrained continuum statement about six vertices. It is now reduced to two sharply described exceptional mechanisms:

1. **fully recycled auxiliary triangles**, where an auxiliary has no private corona nucleus left to supply transversality; and
2. the **central-pair resonance** case in which `a,b` are true neighbors of `v` and `c,d` are true neighbors of `w`, yet the scalar compatibility identity might conceivably hold with `v,w` not adjacent.

All witnesses involving an independently generated or only singly attached auxiliary triangle are eliminated exactly.

This does **not** yet prove Question 7.2(i), because a fully recycled six-triangle incidence pattern or a nonadjacent central-pair resonance has not been ruled out. P0408 therefore remains **OPEN / NM13-08 PARTIAL**.

## 11. Section-B outcomes

### #18 — SAY IT IN ANOTHER LANGUAGE — success

The remaining decoder problem was translated from six raw hyperbolic points into six 3-element subsets of the source corona PPP together with their overlap partition. In that language, “spurious” is not one monolithic event: it stratifies by how many private radial coordinates remain in each dual triangle. The PPP's product-Lebesgue radial intensity then becomes usable directly.

### #30 — ONE SCALE / ONE DIRECTION AT A TIME — success

I localized at a single auxiliary vertex and solved overlap counts `0`, `1`, and `2` completely. Two or more private nuclei give enough continuous dimension to miss the one-dimensional compatibility locus; one private nucleus confines the vertex to a fixed weighted bisector, and survival then forces that bisector through the intended center, which by general position is a genuine shared Delaunay edge.

### #26 — HUNT THE SPORADIC CASE — partial but informative

The only local incidence stratum not killed is `m_x=3`, the **fully recycled** triangle. In addition, even when all four auxiliaries are true intended neighbors, the central pair `v,w` could in principle satisfy the scalar distance identity accidentally while not adjacent. These are now the precise sporadic configurations to analyze; the broad independent-six-point transversality route is exhausted.

No numerical simulation, finite plot, or heuristic is promoted as evidence.

## 12. Why no checker artifact was added

The new claim is an analytic, theorem-sized source-law statement. Its proof is on the page and its core is measure-zero / Mecke transversality, not a finite arithmetic enumeration. Under the 90/10 policy, adding a checker for the already frozen `(1/4,infinity)` metric would be bookkeeping without new evidentiary value. Therefore no checker-only artifact or receipt-only commit is created this run.

No P26 or NM13-09 audit is requested or counted here.

## 13. Exact blocker reached at the stuck trigger

Because the frozen metric has now remained unchanged for three consecutive runs, the next run must use the owner's Section-I thinking-only protocol. The source-level blocker to place in that report is:

\[
\boxed{
\begin{minipage}{0.86\linewidth}
For the planar IPVT, prove that every six-point compatibility witness surviving the overlap-transversality theorem has `v` and `w` joined by the true Voronoi edge and has the source-correct two-star incidence; equivalently, rule out fully recycled auxiliary patterns and nonadjacent central-pair resonance.
\end{minipage}}
\]

In plain notation: after Lemmas 03A–03C, one must still show that no source-random witness can survive solely because all needed nuclei are recycled among the six Delaunay triangles, and that

`d_H(v,w) in {rho_v+rho_w, |rho_v-rho_w|}`

cannot occur for nonadjacent `v,w` when `rho_v,rho_w` come from two chosen genuine incident-edge pairs.

The **next** run should not create a new lemma before completing the five-part stuck report. Prospective new lenses, **not counted as attempted in this run**, are #1 (change category: dual-tree/ideal-triangulation combinatorics), #15 (break the symmetry between recycled and central-resonance patterns), and #25 (double-count the finite six-triangle incidence types / private nuclei).

## 14. Structured ledger delta for P26

```yaml
ledger_delta:
  track: NM13-08
  source_id: P0408
  claim_id: P0408
  canonical_dedup_key: recovering_an_ideal_voronoi_tessellation_from_vertices_or_its_dual
  owner: proofnet24/NM13-08
  category: CLOSABLE_OUTSIDE
  source_status_before: OPEN
  source_status_after: OPEN
  worker_status_before: PARTIAL
  worker_status_after: PARTIAL
  metric_name: A_triangle
  metric_before: "(1/4, infinity)"
  metric_after: "(1/4, infinity)"
  metric_movement: false
  methods_actually_tried: [18, 30, 26]
  new_claims:
    - NM13-08-P0408-BISECTOR-GENERAL-POSITION-03A
    - NM13-08-P0408-AUX-LOW-OVERLAP-03B
    - NM13-08-P0408-AUX-TWO-OVERLAP-03C
    - NM13-08-P0408-SIXPOINT-OVERLAP-TRANSVERSALITY-03
  unchanged_runs_since_metric_movement: 3
  stuck_recoveries_used: 0
  next_protocol: "mandatory Section-I thinking-only stuck-recovery report; no new claim"
  p26_audit: NOT_COUNTED
  nm13_09_audit: NOT_COUNTED
  publication_novelty: UNVERIFIED
  bounded_literature_check_date: 2026-09-18
  next_methods_prospective_not_tried: [1, 15, 25]
```

## 15. Run verdict

**PARTIAL / source OPEN.** The frozen metric does not move. The mathematical advance is a genuine reduction of the d=2 vertex-set injectivity problem: any six-point compatibility witness must be built almost entirely from actual local Delaunay incidence, except for fully recycled nuclei or a remaining central-pair resonance. That is the exact obstruction to analyze in the mandatory next stuck-recovery run.

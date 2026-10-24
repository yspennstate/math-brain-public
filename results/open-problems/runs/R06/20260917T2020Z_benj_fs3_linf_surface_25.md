Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO MOVEMENT on the newly admitted source metric: `E_FS3: 0 -> 0`, unchanged count `0 -> 1`; methods #3 PROVE SOMETHING STRONGER, #8 DISCRETIZE, #27 SWAP THE QUANTIFIERS.**

# R06 CLOSABLE OUTSIDE — BENJ-2026-FS3 / three fixed sources

Date: 2026-09-17 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.

## 1. Continuity and lawful successor admission

I did not reopen either retired R06 target.

- Lyons–Peres Question 6.20 / I0056 retains the frozen regular/co-regular `H_{5,5}` interval `[sqrt(5),sqrt(5)]`, width `0`; the full source question remains PARTIAL. The Haslegrave–Panagiotis triangular/quadrangular cases remain excluded prior art.
- D0069 remains operationally retired after six unchanged frozen-metric runs at `C_5=5/5`; its degree-five theorem package and degree-six partial results are preserved and are not extended in this run.

At run start R06 was `SUCCESSOR_ADMISSION_REQUIRED`. I reread/recovered the campaign `INDEX.md`, `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the NEW-METHODS implementation area, newest own R06 report, current coordinator admission state, current claims, intake ledgers/targeted unmined-source evidence, and the newest relevant neighboring R07 report. The previous coordinator pass had no already-vetted free CLOSABLE row, but a newer PROB20-21 admission-gate report discovered a fresh unclaimed source candidate and deliberately left ownership pending.

That candidate is now claimed create-only by R06:

`operations/claims/BENJ-2026-FS3.md`

initial creation commit `d206e24a4fce96fbebc8e2fb2603ea438ee2de83`; scale-quantifier correction commit `b82f99900bd1db278be4797bb0fbe2ea19a5c6f7`.

No competing claim existed immediately before creation.

## 2. Exact outside source and current-status check

Source: Itai Benjamini, **“Euclidean vs Graph Metric: The Fixed-Source Problem,”** arXiv:2606.13271v2, June 2026, Section 7, Question 1 (Three fixed sources).

The source constructs, for two fixed sources in the Euclidean plane, a bounded-degree planar unit-edge graph on a `10`-net whose graph distances from each source agree with Euclidean distances up to a universal additive constant, and asks whether the analogous statement holds for **three non-collinear sources**. Version 2 also proves a logarithmic obstruction for large ordered source sets in a coordinate-planar setting, while explicitly leaving the fixed three-source question open.

Fresh dated web queries on 2026-09-17 included:

- exact title + `three fixed sources`;
- arXiv `2606.13271` + `three non-collinear sources`;
- author + fixed-source problem + resolution variants.

The current arXiv record still says the analogous three-source statement is asked, and I found no later primary source claiming a source-matching positive or negative resolution. This is bounded negative search evidence only; publication novelty is **UNVERIFIED**.

The frozen metric is

`E_FS3 in {0,1}` = whether R06 has a complete source-level decision of Question 1 under the exact hypotheses.

Entering baseline: `0`. Current value: `0`. A restricted triple shape, sampled finite box, or construction with additive error growing with geometric scale does not move this metric.

## 3. #27 SWAP THE QUANTIFIERS — scale-uniformity is not optional

The first useful result is a scope correction. The `O(1)` cannot be allowed to absorb the entire fixed source separation/scale.

Indeed, suppose a one-source construction at `p_1` obeys

`|d_G(p_1,x)-|p_1-x|| <= C`

for all vertices. For any additional **fixed** vertex/source `p_i` in the same connected graph,

`|d_G(p_i,x)-d_G(p_1,x)| <= d_G(p_i,p_1)`

and

`||p_i-x|-|p_1-x|| <= |p_i-p_1|`.

Therefore

`|d_G(p_i,x)-|p_i-x|| <= C+d_G(p_i,p_1)+|p_i-p_1|`.

If arbitrary dependence on the fixed source configuration were permitted, every finite-source problem would collapse to the one-source case. That is incompatible with the source's explicit scale-independent setup and with its advertising the two-source additive constant as universal. The active claim was therefore corrected so that **scale-uniformity is mandatory**. Whether the formal Question 1 also forces one absolute constant uniform over every triangle shape is retained as a source-wording nuance, but no construction may hide an `O(diam S)` term inside `O(1)`.

This correction matters: it prevents a vacuous “solution” and fixes the actual research quantifier.

## 4. #3 PROVE SOMETHING STRONGER — exact three-landmark `l_infinity` linearization

The source remarks that its two-source confocal-coordinate proof has no analogous **two-coordinate** linearization for three non-collinear sources. There is, however, an exact three-coordinate linearization of all three source distances.

Let

`r_i(x)=|x-p_i|`,

and define the landmark map

`F(x)=(r_1(x),r_2(x),r_3(x)) in R^3`.

For each source `p_i`,

`||F(x)-F(p_i)||_infinity = r_i(x)`.

**Proof.** The `i`-th coordinate difference is exactly `r_i(x)`. For every `j`, reverse triangle inequality gives

`|r_j(x)-|p_i-p_j|| <= |x-p_i|=r_i(x)`.

So the maximum of the three coordinate differences is exactly `r_i(x)`. QED.

This is the finite-landmark form of the classical Kuratowski `l_infinity` embedding, so I do **not** claim the lemma itself as novel. Its value here is that it turns the Benjamini obstruction into a sharply identified planar-discretization problem.

For three non-collinear Euclidean landmarks, `F` is injective: equal distances to `p_1,p_2` leave at most the two mirror points across line `p_1p_2`, and the non-collinear third landmark distinguishes them. Hence

`Sigma := F(R^2) subset R^3`

is a two-dimensional surface homeomorphic to the plane, and each Euclidean segment from `p_i` to `x` maps to an `l_infinity` geodesic from `F(p_i)` to `F(x)`.

Thus the source question can be reframed as:

> Can the two-dimensional distance-triple surface `Sigma` be discretized by one bounded-degree **planar** unit-edge graph so that the three landmark `l_infinity` geodesic systems survive with only uniformly bounded additive loss and the pulled-back vertices form a `10`-net?

This is stronger/more structured than attacking three distance functions separately.

## 5. #8 DISCRETIZE — Gromov-excess coordinates expose the exact allowed steps

Write `D_ij=|p_i-p_j|` and define

`a=(r_2+r_3-D_23)/2`,  
`b=(r_1+r_3-D_13)/2`,  
`c=(r_1+r_2-D_12)/2`.

Also put

`s_1=(D_12+D_13-D_23)/2`,

with cyclic `s_2,s_3`. Triangle inequalities give `a,b,c,s_i >=0`. The inverse linear relations are

`r_1=b+c-a+s_1`,  
`r_2=a+c-b+s_2`,  
`r_3=a+b-c+s_3`.

The source points are axis points:

`p_1 -> (s_1,0,0)`, `p_2 -> (0,s_2,0)`, `p_3 -> (0,0,s_3)`.

For an integer step `(da,db,dc) in {-1,0,1}^3`, the landmark-distance increments are

`dr_1=-da+db+dc`,  
`dr_2= da-db+dc`,  
`dr_3= da+db-dc`.

Exact enumeration of all 26 nonzero steps shows that the condition

`|dr_i|<=1 for i=1,2,3`

leaves exactly eight moves:

`+-e_a, +-e_b, +-e_c, +-(1,1,1)`.

This finite classification was checked with exact integer arithmetic in

`artifacts/R06/20260917T2020Z_benj_fs3_step_vectors_exact.py`

and the executed output is archived at

`artifacts/R06/20260917T2020Z_benj_fs3_step_vectors_exact.out`, ending

`EXACT_STEP_CLASSIFICATION_PASS`.

### Exact source-distance paths in the unrestricted coordinate lattice

This eight-move lattice has no intrinsic metric obstruction. For example, to reach `(a,b,c)` from `p_1=(s_1,0,0)`:

- if `a<=s_1`, use `(s_1-a)` copies of `-e_a`, then `b` copies of `+e_b`, then `c` copies of `+e_c`;
- if `a>s_1`, put `k=a-s_1`. Triangle inequalities imply

`k<=b` because `b-k=(r_1-r_2+D_12)/2>=0`,

and

`k<=c` because `c-k=(r_1-r_3+D_13)/2>=0`.

Use `k` copies of `+(1,1,1)`, then `b-k` copies of `+e_b`, then `c-k` copies of `+e_c`.

Every step in either path raises `r_1` by exactly one, and the path length is exactly

`b+c-a+s_1=r_1`.

Cyclically the same holds from `p_2,p_3`. Since every allowed edge changes each `r_i` by at most one, the unrestricted eight-move coordinate graph has **exact** graph distance `r_i` from each corresponding source whenever the coordinates are integral.

Therefore the three-source difficulty is not simultaneous distance-label feasibility. It is the requirement that one **planar embedded two-dimensional subgraph**, approximating the physical surface `Sigma`, retain enough of these diagonal moves to realize all three source geodesics with only `O(1)` scale-uniform loss.

## 6. The first concrete obstruction: planar crossover, not metric algebra

The most naive discretization takes the arrangement of integer level curves of `r_1,r_2,r_3` in the physical plane. Adjacent cells give a planar graph automatically, but ordinary adjacency changes essentially one distance level at a time. That reproduces an `l_1`-type cost and loses the simultaneous changes that make the `l_infinity` path exact.

At a transverse crossing of two level-curve families, the desired diagonal moves connect opposite sectors. The two possible diagonal pairings form an `X`: in a planar drawing one cannot realize both as independent one-step transitions. Replacing the crossing by a central vertex costs two graph steps. If the wrong pairing is encountered at a positive density of crossings along a source ray, the accumulated defect is linear in scale rather than `O(1)`.

So a successful proof now has a precise combinatorial obligation:

> construct a global planar diagonalization/triangulation of the distance-level arrangement for which every one of the three source-directed geodesic systems incurs only uniformly bounded total crossover defect.

Or, to refute the conjecture, show that some non-collinear shape forces an unbounded crossover defect for at least one source in every bounded-degree planar diagonalization.

This is substantially narrower than the original geometry.

## 7. A promising change-of-category bridge: Schnyder/geodesic embeddings

The exact residual shape has established planar-graph machinery nearby. Stefan Felsner's *Geodesic Embeddings and Planar Graphs* (Order 20, 2003) characterizes 3-connected planar graphs admitting rigid geodesic embeddings and gives a bijection with Schnyder labelings. Felsner–Zickfeld, *Schnyder Woods and Orthogonal Surfaces* (GD 2006 / 2007), develops the correspondence between Schnyder woods, three-coordinate orthogonal surfaces, and planar convex drawings.

This is not yet a solution: their orthogonal surfaces are special combinatorial surfaces, whereas `Sigma=F(R^2)` is a curved Euclidean distance surface, and their geodesic notion does not automatically give the quantitative unit-edge/additive-error bound required here. But the match is unusually close:

- three distinguished coordinate directions;
- one planar graph;
- three source/root geodesic systems;
- a two-dimensional surface embedded in three coordinates;
- the need to choose globally compatible diagonal/crossover resolutions.

The next run should therefore try to **port a weighted Schnyder wood / orthogonal-surface discretization to `Sigma`**, rather than invent another local grid.

## 8. What is and is not proved

Proved on page in this run:

1. source-scale dependence cannot be hidden in `O(1)` without trivializing the problem;
2. the exact three-distance map is an `l_infinity` landmark linearization and is injective for a non-collinear triple;
3. the Gromov-excess change of variables puts the three sources on coordinate axes;
4. among the 26 elementary cube moves, exactly eight preserve all three distance labels by at most one;
5. in the unrestricted eight-move lattice, each source has an exact shortest path of length `r_i` to every integral admissible target.

Not proved:

- existence of a planar discretization of `Sigma` with uniformly bounded crossover loss;
- a source-valid graph for arbitrary three-source configurations;
- a counterexample.

Therefore the honest source status is **OPEN / PARTIAL**, and the frozen metric remains `E_FS3=0`.

## 9. Neighbor/current-fleet read and audit discipline

The newest relevant R07 report was read for continuity; R07 remains on the distinct Burdzy–Scheutzow Problem 7.8 track and has moved to sampled spatial-comb gate families. Its P26 audit activity does not overlap this source. I did not manufacture an audit pass for unrelated new mathematics.

No P26 or second OTHER-track audit is requested yet because BENJ-2026-FS3 is not source-complete.

## 10. Scheduler/model escalation

Still true in the interface actually exposed to this worker: task controls expose prompt/title, schedule/timing and enablement, but **no binding model-family selector, no reasoning-effort selector, no authenticated completed-run model telemetry, and no guaranteed one-hour execution control**. GPT-6/maximum is therefore prompt text only and cannot be certified.

Making it enforceable requires an authorized owner/platform surface or backend support exposing persistent model/reasoning fields and authenticated run metadata. The historical P26 `You cannot modify this task` response is an authorization boundary; the lawful workaround is the owning/admin context or platform support, not duplication or permission bypass. No scheduler change was attempted here.

## 11. Structured ledger_delta

```yaml
ledger_delta:
  worker: R06
  lane: CLOSABLE OUTSIDE
  predecessor_state:
    I0056:
      status: "PARTIAL / RETIRED"
      metric: "width([sqrt(5),sqrt(5)]) = 0"
    D0069:
      status: "PARTIAL / RETIRED-HANDOFF"
      metric: "C_5 = 5/5"
      unchanged_count: 6
  source:
    id: BENJ-2026-FS3
    citation: "Itai Benjamini, Euclidean vs Graph Metric: The Fixed-Source Problem, arXiv:2606.13271v2, Question 1"
    target: "three non-collinear fixed sources"
    ownership: "R06 exclusive canonical claim"
    claim_creation_commit: "d206e24a4fce96fbebc8e2fb2603ea438ee2de83"
    claim_scope_correction_commit: "b82f99900bd1db278be4797bb0fbe2ea19a5c6f7"
  metric:
    name: E_FS3
    before: 0
    after: 0
    unchanged_count: 1
  status: "OPEN / PARTIAL"
  methods: [3, 8, 27]
  progress:
    - "mandatory scale-uniform interpretation isolated"
    - "exact three-landmark l_infinity surface reduction"
    - "exact excess-coordinate eight-step lattice and source geodesics"
    - "planar crossover identified as the residual obstruction"
    - "Schnyder/orthogonal-surface route identified for next attack"
  exact_evidence:
    - "artifacts/R06/20260917T2020Z_benj_fs3_step_vectors_exact.py"
    - "artifacts/R06/20260917T2020Z_benj_fs3_step_vectors_exact.out"
  remaining_obligation: "planar bounded-degree 10-net discretization of the distance-triple surface with scale-uniform O(1) defect for all three roots, or a proof that such a discretization is impossible"
  audit_ids: []
  novelty: UNVERIFIED
  next_methods: [11, 14, 21]
  shared_roots_edited: false
  peer_files_edited: false
  email: false
  drive: false
  public_posting: false
  scheduler_modified: false
```

Next run: **#11 DUALIZE, #14 FIND THE GROUP ACTING, #21 ASK WHO ELSE HAS THIS SHAPE** — formulate the planar crossover choice as a dual orientation/flow problem, quotient by the three-root combinatorics, and test whether weighted Schnyder woods can discretize `Sigma` with bounded accumulated defect.

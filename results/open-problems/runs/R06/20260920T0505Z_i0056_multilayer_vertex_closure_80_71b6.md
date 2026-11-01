Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. FROZEN I0056 METRIC NO MOVEMENT / SOURCE-CLAUSE BOUND MOVEMENT: `H_{5,5}` width `0 -> 0`; for the source-valid tetrapentagonal graph `T=r{4,5}`, the rigorous vertex upper bound improves `113708/133611 -> 116990/147339`, shrinking the certified secondary interval width `0.34293830065971065 -> 0.2859198212533609`; methods #5 ADD A PARAMETER, #8 DISCRETIZE, #26 HUNT THE SPORADIC CASE.**

# R06 / I0056 — an exact non-round multilayer witness for tetrapentagonal outer-vertex isoperimetry

Repository: private `yspennstate/math-open-problems`, branch `master`.  
Worker: R06.  
Outside source: Russell Lyons and Yuval Peres, *Probability on Trees and Networks*, Question 6.20; intake `I0056`.  
Overall source status after this run: **PARTIAL**.

## 1. Exact source and inherited state

The source question retained by the canonical claim is:

> What is `Phi_V(G)` for regular, co-regular plane graphs `G`? What are `Phi_E(G)` and `Phi_V(G)` for more general transitive, plane graphs `G`?

with the original outer-vertex normalization

\[
\Phi_V(G)=\inf_{\varnothing\ne K\subset V(G),\ |K|<\infty}
\frac{|\partial_VK|}{|K|}.
\]

The frozen regular/co-regular R06 subtarget remains

\[
H_{5,5}=\{5,5\},\qquad(d,f)=(5,5),
\]

and its already proved/audited/posted value remains

\[
\boxed{\Phi_V(H_{5,5})=\sqrt5},\qquad [L,U]=[\sqrt5,\sqrt5],\qquad U-L=0.
\]

Hence the fixed metric cannot move below zero. The full source question is still not closed.

The latest useful R06 checkpoint was

`runs/R06/20260920T0322Z_i0056_dual_admissibility_fal_growth_79_a47c.md`.

It proved the all-radius frontier anatomy and the exact shell recurrence for the source-valid mixed-face transitive plane graph

\[
T=r\{4,5\}=M(\{4,5\}),
\]

the 4-regular tetrapentagonal tiling of vertex type `[4,5,4,5]`, and retained

\[
\frac1{\sqrt3+\sqrt5-2}
\le \Phi_V(T)
\le \frac{113708}{133611}.
\tag{1.1}
\]

The lower endpoint is approximately `0.5080994133009662`; the old upper endpoint is approximately `0.8510377139606768`.

Haslegrave--Panagiotis, DOI `10.1002/rsa.20946`, remain excluded prior art. Their paper states that it determines the vertex-isoperimetric constants for the triangular and square hyperbolic lattices, i.e. the regular face/codegree 3 and 4 cases. Nothing below is relabelled from those cases.

## 2. Current literature boundary checked 20 September 2026

Fresh queries included the exact Lyons--Peres question, the Haslegrave--Panagiotis title/DOI, `tetrapentagonal isoperimetric constant`, `[4,5,4,5] isoperimetric hyperbolic`, and later hyperbolic isoperimetry.

The current Haslegrave--Panagiotis article still describes its exact answer as the triangular and square regular hyperbolic cases. D'Achille--Jacquier--Ruszel (arXiv:2504.14080, 2025) treat minimal-perimeter shapes for **regular** `{p,q}` hyperbolic tilings and the edge/perimeter constant; that is not an exact outer-vertex constant for the mixed-face tetrapentagonal graph. I recovered no primary source giving the exact `Phi_V(r{4,5})` or the finite witness below. This is bounded negative evidence only; novelty remains **UNVERIFIED**.

## 3. Idea before archival code and the three moves

Two idea notes were committed before the corresponding archival checkers:

- `artifacts/R06/20260920T0427Z_i0056_frontier_typeB_idea_80_4d21.md`;
- `artifacts/R06/20260920T0442Z_i0056_multilayer_closure_idea_80_71b6.md`.

### #5 — ADD A PARAMETER

For a finite set `K`, introduce

\[
F_r(K)=|\partial_VK|-r|K|.
\]

Rather than asking directly for the optimum ratio, fix `r` and ask whether some finite `K` has `F_r(K)<0`.

### #8 — DISCRETIZE

On the exact Coxeter development of `T`, restrict selected vertices to the radius-17 ball and retain all vertices through radius 18 as possible covered vertices. This is not sampling a lower bound: any explicit finite selected set returned is itself a rigorous upper-bound witness for the infinite graph.

### #26 — HUNT THE SPORADIC CASE

The preceding run proved that large round balls asymptotically get worse than the radius-16 ball. Therefore search specifically for a non-round finite dip rather than extending the BFS radius.

## 4. Vertex boundary as an exact maximum-closure problem

For each candidate graph vertex `v`, introduce a selected state `x_v`. For each vertex `u` that may be selected or adjacent to a selected vertex, introduce a covered state `c_u`. Impose

\[
x_v\le c_v,
\qquad
x_v\le c_u\quad(u\sim v).
\tag{4.1}
\]

For any feasible 0--1 assignment with the covered variables chosen minimally,

\[
\sum_u c_u=|K\cup\partial_VK|,
\qquad
\sum_vx_v=|K|.
\]

Thus

\[
1795\sum_vx_v-1000\sum_uc_u
=795|K|-1000|\partial_VK|.
\tag{4.2}
\]

Maximizing the left side subject to the implications (4.1) is the standard maximum-weight closure problem. It is represented exactly by an integer `s-t` cut:

- source to each selected-state node, capacity `1795`;
- each covered-state node to sink, capacity `1000`;
- every implication in (4.1), capacity `INF`, with `INF` larger than the total positive weight.

The purpose of the cut is only to **find** a finite set. The claimed isoperimetric bound below is then checked independently from the returned selected vertices by exact reconstruction of `K union partial_V K`; it does not require claiming that this finite search solved the infinite optimization.

## 5. Exact finite certificate

The exact arithmetic development uses the same Coxeter model as the preceding R06 runs, over

\[
\mathbb Z[a,b],\qquad a^2=2,\quad b^2=b+1.
\]

It reproduces the graph-distance shells through radius 18:

\[
1,4,10,20,38,70,130,240,446,824,1528,2824,5234,9680,17934,33178,61450,113708,210566.
\]

Hence there are exactly `247319` selectable vertices through radius 17 and `457885` coverage vertices through radius 18. There are exactly `1236595` implication arcs of the form selected vertex -> itself/one of its four neighbours.

At the integer weights `(1795,1000)`, the exact max-flow value is

`443793100`,

while the total positive source weight is

\[
1795\cdot247319=443937605.
\]

The positive closure surplus is therefore

\[
443937605-443793100=144505.
\tag{5.1}
\]

The source side of this cut selects exactly

\[
|K|=147339
\]

vertices and its exact reconstructed covered set has

\[
|K\cup\partial_VK|=264329.
\]

Therefore

\[
|\partial_VK|=264329-147339=116990.
\]

The exact consistency check from (4.2) is

\[
795(147339)-1000(116990)=144505>0.
\]

So, without any floating-point geometry or asymptotic inference,

\[
\boxed{
\Phi_V(T)\le\frac{116990}{147339}
=0.7940192345543271\ldots
}
\tag{5.2}
\]

The witness is visibly non-round. Its exact radial occupancy is

\[
(1,4,10,20,38,70,130,240,446,824,1528,2824,5234,9680,17934,33178,46710,28468).
\tag{5.3}
\]

Thus it contains every vertex through radius 15, then only `46710/61450` vertices of sphere 16 and `28468/113708` vertices of sphere 17.

The selected-index and covered-index SHA-256 fingerprints in deterministic BFS order are respectively

`9421fb6797830c34f3805e8396b8446263d93cd964058adab75d723b37f420bb`

and

`577090beb9217daa49400d85a5743e6dd3ccca9532c68f697f2bbf9406a4814e`.

The exact checker and archived output are:

- `artifacts/R06/20260920T0450Z_i0056_multilayer_vertex_closure_exact_80_71b6.py`;
- `artifacts/R06/20260920T0450Z_i0056_multilayer_vertex_closure_exact_80_71b6.out`.

The archived run ends `ALL_EXACT_CHECKS_PASS`.

## 6. Quantitative movement

The new upper bound strictly improves the previous one because

\[
113708\cdot147339-116990\cdot133611
=1,122,472,122>0.
\]

Combining (5.2) with the inherited rigorous lower bound gives

\[
\boxed{
\frac1{\sqrt3+\sqrt5-2}
\le\Phi_V(r\{4,5\})
\le\frac{116990}{147339}.
}
\tag{6.1}
\]

Numerically,

\[
0.5080994133009662
\le\Phi_V(r\{4,5\})
\le0.7940192345543271.
\]

The rigorous secondary interval width therefore moves

\[
0.34293830065971065
\longrightarrow
\boxed{0.2859198212533609},
\]

a reduction of about `16.626%` in one run.

This does **not** change the frozen H55 metric, which remains zero, and it does **not** close the full source question.

## 7. What failed and what it teaches

A first one-frontier optimization already produced the weaker exact witness

\[
\Phi_V(T)\le\frac{55602}{65845}\approx0.8444376946
\]

by adjoining a favorable subset of sphere 17 to the radius-16 ball. Its exploratory checker is retained in `artifacts/R06/20260920T0431Z_i0056_frontier_typeB_exact_80_4d21.py`.

The multilayer closure formulation then improved this drastically to (5.2). A higher-resolution integer-threshold run indicated that still more finite improvement may exist below `0.794`, but it did not yield a reconstructible source-side cut before the runtime limit. **No stronger bound is claimed from that incomplete computation.**

The key lesson is now rigorous: the round-ball family is not merely asymptotically suboptimal; a concrete exact two-frontier deformation beats it by a large margin. The next route should therefore derive the cut pattern from the already proved finite frontier-state automaton, rather than spend runs increasing a brute-force radius.

## 8. Remaining obligation and next concrete attack

The current gap is

\[
0.2859198212533609.
\]

The strongest next attack is to turn the finite closure pattern into an all-radius transfer rule. Concretely:

1. classify the selected/unselected states on the proved `A,B,C` frontier types over two consecutive shells;
2. derive the finite transition matrix for a repeating non-round boundary profile;
3. compute its Perron ratio exactly, producing an algebraic asymptotic upper bound if the profile propagates;
4. in parallel, revisit the dual weighted-boundary lower inequality with these extremal states to see whether the lower bound can be raised toward the same number.

That route attacks both ends of (6.1) and is qualitatively different from further ball enumeration.

## 9. Model/control truth

The scheduler limitation remains unchanged. The exposed control surface supplies task identity/title, prompt, schedule/timing mode and enabled state, but no binding model-family selector, no reasoning-effort selector, no guaranteed hour-long runtime control, and no authenticated applied-model/effort receipt. Enforcing GPT-6/maximum would require a product/backend/API surface that actually persists and attests those fields.

The historical P26 `You cannot modify this task` event was authorization-context-specific; the current repository ledger records that a later authorized context successfully updated P26. The compliant workaround is therefore the owning/authorized context or a platform-side permission repair, not a permission bypass. No scheduler or permission modification was attempted in this run.

```yaml
ledger_delta:
  worker: R06
  source: "Russell Lyons and Yuval Peres, Probability on Trees and Networks, Question 6.20 / intake I0056"
  full_source_status: PARTIAL
  frozen_target:
    graph: "H_{5,5}={5,5}"
    parameters: "degree=5, face_degree=5"
    normalization: "outer vertex boundary Phi_V"
    metric: "rigorous interval width U-L"
    before: 0
    after: 0
    status: "PROVED/audited/posted subclass; full source still PARTIAL"
  source_clause_progress:
    graph: "T=r{4,5}, 4-regular transitive tetrapentagonal plane graph"
    quantity: "Phi_V(T)"
    lower_before: "1/(sqrt(3)+sqrt(5)-2)"
    lower_after: "1/(sqrt(3)+sqrt(5)-2)"
    upper_before: "113708/133611"
    upper_after: "116990/147339"
    interval_width_before: 0.34293830065971065
    interval_width_after: 0.2859198212533609
    status: "PROVED PARTIAL / exact finite self-check; no new outside audit yet"
  tried_moves: [5, 8, 26]
  remaining_obligation: "derive an all-radius non-round transfer rule and/or raise the lower bound; exact Phi_V(T) remains open"
  evidence:
    idea_1: "artifacts/R06/20260920T0427Z_i0056_frontier_typeB_idea_80_4d21.md"
    idea_2: "artifacts/R06/20260920T0442Z_i0056_multilayer_closure_idea_80_71b6.md"
    checker: "artifacts/R06/20260920T0450Z_i0056_multilayer_vertex_closure_exact_80_71b6.py"
    checker_output: "artifacts/R06/20260920T0450Z_i0056_multilayer_vertex_closure_exact_80_71b6.out"
    checker_verdict: "ALL_EXACT_CHECKS_PASS"
    predecessor: "runs/R06/20260920T0322Z_i0056_dual_admissibility_fal_growth_79_a47c.md"
  audits:
    new_multilayer_bound: "self-check only; independent audit not yet obtained"
    frozen_H55: "existing audited/posted state retained"
```

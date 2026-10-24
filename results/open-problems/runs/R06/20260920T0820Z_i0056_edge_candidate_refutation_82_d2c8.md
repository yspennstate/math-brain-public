Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. FROZEN I0056 METRIC NO MOVEMENT / SOURCE-CLAUSE EDGE MOVEMENT: `H_{5,5}` outer-vertex interval width `0 -> 0`; for the source-valid tetrapentagonal graph `T=r{4,5}`, the rigorous edge upper bound improves `2/sqrt(5) -> 130232/154055`, shrinking the certified edge interval width `0.08929346271191282 -> 0.04022669493746836`; the former sharp-edge candidate `Phi_E(T)=2/sqrt(5)` and its universal disk TURN-CAP are REFUTED, while the full Lyons–Peres Question 6.20 remains PARTIAL; methods #22 READ THE FAILURES, #6 DEFORM TO A SOLVABLE POINT, #9 RANDOMIZE.**

# R06 / I0056 — exact finite counterexample to the tetrapentagonal edge candidate

Repository: private `yspennstate/math-open-problems`, branch `master`.  
Worker: R06.  
Outside source: Russell Lyons and Yuval Peres, *Probability on Trees and Networks*, Question 6.20; intake `I0056`.  
Overall source status after this run: **PARTIAL**.

## 1. Source, ownership, normalization, and continuity

The current Lyons–Peres question is still:

> What is `Phi_V(G)` for regular, co-regular plane graphs `G`? What are `Phi_E(G)` and `Phi_V(G)` for more general transitive, plane graphs `G`?

The fixed R06 normalization is the outer vertex boundary

\[
\Phi_V(G)=\inf_{\varnothing\ne K\subset V(G),\ |K|<\infty}
\frac{|\partial_VK|}{|K|},
\qquad
\partial_VK=N[K]\setminus K.
\]

The frozen regular/co-regular regime remains

\[
H_{5,5}=\{5,5\},\qquad (d,f)=(5,5),
\]

with the already proved, independently audited, and posted value

\[
\boxed{\Phi_V(H_{5,5})=\sqrt5},
\qquad [L,U]=[\sqrt5,\sqrt5],
\qquad U-L=0.
\]

Thus the required fixed metric stays `0 -> 0`. The already-written regular-tessellation paper is listed in root `POSTED.md`; this run does not relabel that result as new.

The still-open source clause used here is the more-general transitive-plane clause, through the 4-regular vertex-transitive tetrapentagonal graph

\[
T=r\{4,5\}=M(\{4,5\}),
\]

with cyclic face type `[4,5,4,5]`.

The newest completed R06 report before the interrupted edge attack was

`runs/R06/20260920T0615Z_i0056_symmetry_quotient_vertex_upper_81_b47e.md`,

which retained

\[
\boxed{
\frac1{\sqrt3+\sqrt5-2}
\le \Phi_V(T)
\le \frac{384566}{484385}
}
\tag{1.1}
\]

and the older rigorous edge interval

\[
\boxed{
\frac4{1+\sqrt3+\sqrt5}
\le \Phi_E(T)
\le \frac2{\sqrt5}.
}
\tag{1.2}
\]

An interrupted later attempt had already written its idea-before-code note at

`artifacts/R06/20260920T0746Z_i0056_edge_candidate_negation_idea_82_d2c8.md`.

I continued that attempt rather than restarting it.

At run start I rechecked `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, `QUEUE.md`, the canonical `I0056` claim, the latest R06 reports, and the newer progress-first owner directive. The large intake JSONL family is not representable row-by-row through one bounded connector response; exact I0056/source/ownership continuity was recovered directly instead of pretending a complete manual rendering. `I0056` remains R06-owned.

## 2. Current source and literature boundary — 20 September 2026

The current Lyons–Peres paperback PDF still prints Question 6.20 in exactly the scope above and annotates Haslegrave–Panagiotis only for the regular codegree `3` and `4` cases. Haslegrave–Panagiotis, DOI `10.1002/rsa.20946`, explicitly state that they establish the vertex-isoperimetric constant for all triangular and square hyperbolic lattices. Those cases remain **KNOWN / EXCLUDED PRIOR ART** and are not used as novelty here.

Fresh bounded searches included the exact Question 6.20 wording, the Haslegrave–Panagiotis DOI/title, `tetrapentagonal isoperimetric constant`, `[4,5,4,5] isoperimetric`, `r{4,5} isoperimetric`, later hyperbolic isoperimetry, and citing/later-author work. I recovered no primary source giving the exact edge or outer-vertex isoperimetric constant of the mixed-face tetrapentagonal graph, nor the finite witness below. This is **bounded negative evidence only**, not a priority certificate.

## 3. The inherited edge candidate and the exact refutation target

Earlier R06 work proved the lower bound in (1.2) by Euler/double counting and regular-tessellation expansion. It also had a ball construction giving the upper bound `2/sqrt(5)` and reduced the conjecture that this upper bound is sharp to the universal quadrangulated-disk inequality

\[
\frac BF\ge\frac2{\sqrt5},
\tag{3.1}
\]

or equivalently

\[
I\le1+\frac B\varphi,
\qquad \varphi=\frac{1+\sqrt5}{2},
\tag{3.2}
\]

and then, using the exact identity

\[
4F+11B+40=10\Delta_4+8\Delta_5,
\tag{3.3}
\]

to the weighted boundary-deficit cap

\[
10\Delta_4+8\Delta_5
\le40+(11+2\sqrt5)B.
\tag{TURN-CAP}
\]

The previous run correctly labeled this as a **candidate**, not a theorem. The present run attacks its negation.

## 4. The three methods

### #22 — READ THE FAILURES, NOT THE SUCCESSES

The earlier global-radial shortcut had already failed. Rather than protect the surviving edge candidate, I treated that failure as evidence that `2/sqrt(5)` itself should be stress-tested. One exact finite set with edge ratio below it is decisive.

### #6 — DEFORM TO A POINT YOU CAN SOLVE

For a rational threshold `r=p/q`, restrict selectable vertices to the exact graph ball `B_R` but charge **all** graph edges leaving the selectable region. Minimize

\[
q|\partial_EK|-p|K|
\tag{4.1}
\]

exactly. This is a finite integer `s-t` cut. A negative value yields an actual finite set of the infinite graph and therefore a rigorous upper bound. Failure at finite radius would not be promoted to a lower bound.

The root-stabilizer symmetry reduction from the preceding R06 run was reused only to reduce the finite cut. The final claim is verified by expanding the selected orbits and recounting all four graph neighbors of every selected vertex in the full exact Coxeter graph, so it does not depend on trusting the quotient optimization as a theorem about the infinite graph.

### #9 — RANDOMIZE

Before the exact cut, I tried random two-shell deformations as a cheap counterexample generator. The best exploratory edge ratio stayed above `1.06`, far from the candidate. I abandoned that route rather than certifying noise. The exact deformation was decisive.

## 5. Exact finite construction

The checker develops `T` in the exact Coxeter model over

\[
\mathbb Z[a,b],\qquad a^2=2,\quad b^2=b+1,
\]

with no floating-point vertex identification. It reconstructs distance spheres through radius `19`:

\[
1,4,10,20,38,70,130,240,446,824,1528,2824,5234,9680,
17934,33178,61450,113708,210566,389692.
\tag{5.1}
\]

The selectable ball through radius `18` has `457885` vertices. Quotienting by the order-four root stabilizer gives `114478` exact orbits.

At

\[
r=\frac{4227}{5000}=0.8454,
\]

the exact integer cut has positive reward surplus

\[
4227|K|-5000|\partial_EK|=30485>0.
\tag{5.2}
\]

After expanding the source-side orbits and directly recounting in the full graph, the returned finite set has

\[
\boxed{|K|=154055},
\qquad
\boxed{|\partial_EK|=130232}.
\tag{5.3}
\]

Therefore

\[
\boxed{
\Phi_E(T)\le\frac{130232}{154055}
=0.8453604232254714\ldots
}.
\tag{5.4}
\]

The comparison with the former candidate is exact. Since both sides are positive,

\[
\frac{130232}{154055}<\frac2{\sqrt5}
\]

is equivalent to

\[
5(130232)^2<4(154055)^2.
\]

The integer margin is

\[
\boxed{
4(154055)^2-5(130232)^2=10129902980>0.
}
\tag{5.5}
\]

Hence

\[
\boxed{
\Phi_E(r\{4,5\})\ne\frac2{\sqrt5};
\quad
\Phi_E(r\{4,5\})<\frac2{\sqrt5}.
}
\tag{5.6}
\]

This **refutes an R06 auxiliary sharp-value candidate**, not the Lyons–Peres question itself.

A useful additional exact fact is that every outside neighbor of this `K` has crossing multiplicity exactly one. Thus

\[
|\partial_VK|=|\partial_EK|=130232.
\tag{5.7}
\]

That does not improve the stronger existing vertex upper bound `384566/484385`; it explains cleanly why this edge witness advances the edge half of the source clause without moving (1.1).

## 6. The universal disk TURN-CAP is also false

The candidate lower bound (3.1) was claimed only after reducing arbitrary finite edge sets to connected hole-filled ones. The new witness therefore settles that reduction in the negative direction as well.

Indeed, decompose the finite `K` from (5.3) into connected components. Since edge boundary and cardinality add over components, some component `C` satisfies

\[
\frac{|\partial_EC|}{|C|}
\le
\frac{130232}{154055}
<\frac2{\sqrt5}.
\]

Fill every finite component of `T\setminus C`. Filling removes crossing edges and adds vertices, so for the resulting connected hole-filled set `S`,

\[
\frac{|\partial_ES|}{|S|}
\le
\frac{|\partial_EC|}{|C|}
<\frac2{\sqrt5}.
\tag{6.1}
\]

The already-proved medial/dual correspondence then turns `S` (after the standard boundary-pinch unzipping if necessary) into a realizable quadrangulated disk with `F=|S|` and `B=|partial_E S|`. Hence (3.1), (3.2), and the equivalent universal TURN-CAP cannot hold for all realizable disks.

So the precise status changes are

\[
\boxed{
\texttt{Phi_E(T)=2/sqrt(5): CONJECTURAL -> REFUTED},
}
\]

and

\[
\boxed{
\texttt{R06-I0056-TURN-CAP: CONJECTURAL -> REFUTED}.
}
\]

The exact identity (3.3) itself remains valid; what fails is the proposed inequality placed on its right-hand side.

## 7. Quantitative movement

The retained rigorous lower bound is unchanged:

\[
L_E=\frac4{1+\sqrt3+\sqrt5}
=0.8051337282880030\ldots .
\]

Combining it with (5.4), the certified edge interval becomes

\[
\boxed{
\frac4{1+\sqrt3+\sqrt5}
\le\Phi_E(r\{4,5\})
\le\frac{130232}{154055}.
}
\tag{7.1}
\]

Its width moves

\[
0.08929346271191282
\longrightarrow
\boxed{0.04022669493746836},
\]

a reduction of about `54.95%` in one run.

The current rigorous vertex interval remains

\[
\boxed{
\frac1{\sqrt3+\sqrt5-2}
\le\Phi_V(r\{4,5\})
\le\frac{384566}{484385}
}
\tag{7.2}
\]

with width `0.28582690563954604`. The frozen requested `H_{5,5}` interval remains width zero.

## 8. Exact checker

Idea-before-code note, already present before this checker:

`artifacts/R06/20260920T0746Z_i0056_edge_candidate_negation_idea_82_d2c8.md`.

Executed exact checker:

`artifacts/R06/20260920T0817Z_i0056_edge_candidate_refutation_exact_82_d2c8.py`.

Archived output:

`artifacts/R06/20260920T0817Z_i0056_edge_candidate_refutation_exact_82_d2c8.out`.

The checker:

1. verifies the Coxeter relations exactly;
2. rebuilds every graph vertex through radius `19` in the exact algebraic ring;
3. reproduces the certified shell sequence;
4. constructs the exact order-four symmetry quotient;
5. solves the integer cut at `4227/5000`;
6. expands the selected orbits back into the full graph;
7. directly recounts every crossing edge and outer boundary vertex;
8. checks (5.2), (5.3), and the exact square comparison (5.5).

The archived output ends

`ALL_EXACT_CHECKS_PASS`.

This is an R06 self-check, not an independent outside-track audit.

## 9. What this teaches and next attack

The important lesson is not merely a better number: the regular-base/round-ball edge candidate was wrong by a visible amount. The source-valid mixed-face graph has

\[
0.8051337282\ldots\le\Phi_E(T)\le0.8453604232\ldots,
\]

so the next run should not invest in proving the dead `2/sqrt(5)` disk cap.

The strongest next attack is to reverse-engineer the **new edge minimizer** using the already-proved all-radius `A/B/C` frontier anatomy and the order-four symmetry quotient. Two concrete goals are:

1. classify the selected/unselected boundary states of the edge minimizer and derive a repeating finite-state contour, which could turn (5.4) into an algebraic asymptotic upper bound below `0.84536`;
2. derive the max-flow/min-cut dual as a periodic fractional edge-packing certificate on the infinite tiling. If the primal contour and dual certificate meet, that would determine `Phi_E(T)` exactly and close the edge half of Question 6.20 for this non-regular transitive graph.

For the vertex half, the existing non-round vertex witness and lower-bound gap remain separate; no equality between the edge and vertex constants is asserted.

## 10. Model / scheduler-control truth

The scheduler/control limitation is still true. The exposed task interface provides task identity/title, prompt, schedule/timing and enabled-state controls but **no binding model-family selector, no binding reasoning-effort selector, no guaranteed hour-long execution field, and no authenticated applied-model/effort receipt**. GPT-6/maximum is therefore a prompt request, not an enforceable setting on this surface.

Making it enforceable requires an owner-authorized product/backend/API surface that actually exposes, persists, and attests model family and reasoning effort. The historical P26 `You cannot modify this task` event was authorization-context-specific; the repository deployment record says a later authorized context successfully updated P26. The compliant workaround is the owning/authorized context or platform-side permission repair, not a bypass. No scheduler or permission mutation was attempted in this run.

```yaml
ledger_delta:
  worker: R06
  actual_model: "GPT-5.6 Sol"
  reasoning_level: UNVERIFIED
  requested_model: GPT-6
  requested_reasoning: maximum
  source: "Russell Lyons and Yuval Peres, Probability on Trees and Networks, Question 6.20 / intake I0056"
  full_source_status:
    before: PARTIAL
    after: PARTIAL

  frozen_target:
    graph: "H_{5,5}={5,5}"
    class: "regular co-regular plane tessellation"
    parameters: "degree=5, face_degree=5"
    normalization: "outer vertex boundary |partial_V K|/|K|"
    metric: "rigorously certified interval width U-L for Phi_V(H_{5,5})"
    before: 0
    after: 0
    interval: "[sqrt(5),sqrt(5)]"
    exact_value: "sqrt(5)"
    unchanged_count: UNKNOWN
    status: "PROVED/audited/posted subclass; full source PARTIAL"

  source_clause_edge_progress:
    graph: "T=r{4,5}, 4-regular vertex-transitive tetrapentagonal plane graph, face type [4,5,4,5]"
    normalization: "edge boundary |partial_E K|/|K|"
    lower_before: "4/(1+sqrt(3)+sqrt(5))"
    lower_after: "4/(1+sqrt(3)+sqrt(5))"
    upper_before: "2/sqrt(5)"
    upper_after: "130232/154055"
    interval_width_before: 0.08929346271191282
    interval_width_after: 0.04022669493746836
    candidate_status_before: "Phi_E(T)=2/sqrt(5) CONJECTURAL"
    candidate_status_after: "REFUTED"
    disk_turn_cap_before: CONJECTURAL
    disk_turn_cap_after: REFUTED
    exact_witness:
      selected_vertices: 154055
      edge_boundary: 130232
      outer_vertex_boundary: 130232
      square_margin_below_2_over_sqrt5: 10129902980
    status: "PROVED PARTIAL / exact finite self-check; no new independent audit"

  source_clause_vertex_progress:
    lower: "1/(sqrt(3)+sqrt(5)-2)"
    upper: "384566/484385"
    interval_width: 0.28582690563954604
    movement: "no movement this run"

  tried_moves: [22, 6, 9]
  failed_route: "random two-shell perturbations; best exploratory edge ratio remained above 1.06"
  remaining_obligation: "determine exact Phi_E(T), preferably via a finite-state non-round contour plus dual certificate; determine Phi_V(T) separately; full Question 6.20 remains PARTIAL"

  evidence:
    predecessor: "runs/R06/20260920T0615Z_i0056_symmetry_quotient_vertex_upper_81_b47e.md"
    idea_before_code: "artifacts/R06/20260920T0746Z_i0056_edge_candidate_negation_idea_82_d2c8.md"
    checker: "artifacts/R06/20260920T0817Z_i0056_edge_candidate_refutation_exact_82_d2c8.py"
    checker_commit: "7ffd4cb72ed42568b5ed090fb49e1e80b1c0733a"
    checker_output: "artifacts/R06/20260920T0817Z_i0056_edge_candidate_refutation_exact_82_d2c8.out"
    output_commit: "5cd6a6fbdd02832a4a8fb8aa91fb34e4eba3f7e3"
    checker_verdict: "ALL_EXACT_CHECKS_PASS"
    excluded_prior_art: "Haslegrave-Panagiotis DOI 10.1002/rsa.20946, triangular/quadrangular regular cases"
  audits:
    new_edge_bound: "R06 self-check only"
    frozen_H55: "existing independent R05/P26 passes retained"
```

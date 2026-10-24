Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. FROZEN METRIC NO MOVEMENT / SOURCE-CLAUSE BOUND MOVEMENT: `H_{5,5}` width `0 -> 0`; for the source-valid mixed-face graph `T=r{4,5}`, the certified vertex upper bound improves `2/sqrt(5) -> 1528/1783`, shrinking its rigorous vertex interval width from `0.38632777769894966` to `0.3488832002716642`; methods #1 CHANGE THE CATEGORY, #2 ATTACK THE NEGATION FIRST, #16 COMPUTE EVERY SMALL CASE.**

# R06 / I0056 — exact Coxeter ball improves the mixed-face outer-vertex bound

Repository: private `yspennstate/math-open-problems`, branch `master`.  
Worker: R06.  
Source: Russell Lyons and Yuval Peres, *Probability on Trees and Networks*, Question 6.20; intake `I0056`.  
Overall source status after this run: **PARTIAL**.

## 1. Source continuity and frozen metric

The exact source question remains

> What is `Phi_V(G)` for regular, co-regular plane graphs `G`? What are `Phi_E(G)` and `Phi_V(G)` for more general transitive, plane graphs `G`?

The outer-vertex normalization is

\[
\Phi_V(G)=\inf_{\varnothing\ne K\subset V(G),\ |K|<\infty}
\frac{|\partial_VK|}{|K|},
\qquad
\partial_VK=\{x\notin K:\exists y\in K,\ x\sim y\}.
\]

The frozen regular/co-regular pair is still

\[
H_{5,5}=\{5,5\},\qquad (d,f)=(5,5),
\]

with the already proved/audited/posted value

\[
\boxed{\Phi_V(H_{5,5})=\sqrt5},\qquad
[L,U]=[\sqrt5,\sqrt5],\qquad U-L=0.
\]

So the task's fixed numerical metric cannot improve below zero. The full source remains PARTIAL because Question 6.20 also asks for `Phi_E` and `Phi_V` on more general transitive plane graphs.

Haslegrave--Panagiotis, DOI `10.1002/rsa.20946`, remain prior art for the triangular and quadrangular regular hyperbolic cases, i.e. codegrees 3 and 4. Nothing in this run relabels those cases.

The newer owner directive `operations/progress_first_2026-09-20/OWNER_DIRECTIVE.md` supersedes repeated targetless gate reports and directs useful mathematics on a precise unresolved implication. I therefore continue the already established source-valid mixed-face branch rather than reopening the solved `H_{5,5}` subclass.

## 2. Current source/literature boundary checked 20 September 2026

The current Lyons--Peres online book still prints Question 6.20 in the full form above and annotates Haslegrave--Panagiotis only for codegrees 3 and 4. The Haslegrave--Panagiotis paper explicitly states that it establishes the vertex isoperimetric constant for all triangular and square hyperbolic lattices and that these are the corresponding cases of the Lyons--Peres question.

Fresh dated queries included:

- `"Question 6.20" "regular, co-regular" plane graphs`;
- `"4,5,4,5" tetrapentagonal isoperimetric Cheeger hyperbolic tiling`;
- `"tetrapentagonal" hyperbolic isoperimetric constant`;
- `"medial graph" "{4,5}" isoperimetric hyperbolic`;
- later/citing searches around Haslegrave--Panagiotis and the edge-homogeneous tessellation literature.

Graves--Pisanski--Watkins, *Growth of Edge-Homogeneous Tessellations*, computes growth data from edge symbols but does not state the mixed-face outer-vertex constant sought here in the material checked. The bounded searches above did not recover a primary source giving the exact `Phi_V` of the tetrapentagonal graph below. This is **bounded negative evidence only**, not a novelty or priority certificate.

## 3. Inherited source-valid mixed-face target

Let

\[
R:=H_{5,4}=\{4,5\}
\]

be the degree-five regular quadrangulation, and let

\[
T:=M(R)=r\{4,5\}
\]

be its medial graph. Then `T` is a 4-regular vertex-transitive plane graph with alternating face type `[4,5,4,5]`. It lies in the **more general transitive plane graph** clause of Question 6.20 and is not co-regular.

The inherited rigorous bounds are

\[
\frac4{1+\sqrt3+\sqrt5}
\le \Phi_E(T)\le \frac2{\sqrt5},
\]

and

\[
\boxed{
\frac1{\sqrt3+\sqrt5-2}
\le \Phi_V(T)\le \frac2{\sqrt5}.
}
\tag{3.1}
\]

The preceding run also refuted the overly strong radial shortcut `Phi_V(T^*) >= phi` and reduced the candidate sharp **edge** value to an exact boundary-turn inequality for realizable quadrangulated disks. That edge obligation remains live; this run deliberately attacks the source's **vertex** quantity by a different method.

## 4. Idea before code and methods #1/#2/#16

Before writing the checker I recorded

`artifacts/R06/20260920T0109Z_i0056_tetrapentagonal_vertex_ball_idea_76_c1d7.md`.

The idea was:

1. **#1 CHANGE THE CATEGORY.** Replace a drawn hyperbolic tiling by the exact Coxeter reflection model `[4,5]` over the number field `Q(sqrt(2),sqrt(5))` and construct the medial graph algebraically.
2. **#2 ATTACK THE NEGATION FIRST.** Treat the inherited vertex upper `2/sqrt(5)` as potentially non-sharp and actively look for one exact finite set with smaller outer-boundary ratio.
3. **#16 COMPUTE EVERY SMALL CASE.** Develop exact graph-distance shells, but promote only a rigorously certified finite ball, not a sampled embedding or floating-point picture.

This succeeds: the radius-nine ball gives a strict new source-valid upper bound.

## 5. Exact Coxeter construction

Put

\[
\phi=\frac{1+\sqrt5}{2}.
\]

Use the standard simple-root reflection representation of the Coxeter group `[4,5]`:

\[
S_1=
\begin{pmatrix}
-1&\sqrt2&0\\0&1&0\\0&0&1
\end{pmatrix},
\qquad
S_2=
\begin{pmatrix}
1&0&0\\\sqrt2&-1&\phi\\0&0&1
\end{pmatrix},
\qquad
S_3=
\begin{pmatrix}
1&0&0\\0&1&0\\0&\phi&-1
\end{pmatrix}.
\tag{5.1}
\]

Their Coxeter Gram matrix is

\[
G=
\begin{pmatrix}
1&-\sqrt2/2&0\\
-\sqrt2/2&1&-(1+\sqrt5)/4\\
0&-(1+\sqrt5)/4&1
\end{pmatrix}.
\tag{5.2}
\]

The exact checker verifies

\[
S_i^2=I,
\qquad
(S_1S_2)^4=(S_2S_3)^5=(S_1S_3)^2=I,
\]

with no smaller positive powers for the order-4 and order-5 products, and verifies `S_i^T G S_i=G`. The leading principal minors are `1` and `1/2`, while

\[
\det G=\frac{1-\sqrt5}{8}<0,
\]

so this is the hyperbolic signature `(2,1)` reflection model.

Take the `{4,5}` vertex

\[
p=\left(\frac{5\sqrt2-\sqrt{10}}8,\ 1,\ \frac{1+\sqrt5}{4}\right)^T,
\tag{5.3}
\]

which is fixed by `S_2,S_3`. If `r=S_2S_3`, then `r^5=I`, and the five neighbors of `p` in `{4,5}` are

\[
r^kS_1p,\qquad 0\le k<5.
\tag{5.4}
\]

Applying the same five moves at every orbit vertex gives the regular quadrangulation `R={4,5}` with its cyclic order. The medial graph `T=M(R)` then has one vertex for each undirected edge of `R`; two such medial vertices are adjacent exactly when the corresponding primal edges are consecutive around a primal vertex.

All arithmetic in the finite development is exact in the dyadic basis

\[
1,\sqrt2,\sqrt5,\sqrt{10}.
\]

No geometric tolerance or floating-point vertex identification is used.

## 6. New theorem: a strict mixed-face vertex upper bound

### Proposition R06-I0056-TETRA-VBALL-01

For the tetrapentagonal transitive plane graph `T=r{4,5}`,

\[
\boxed{
\Phi_V(T)\le\frac{1528}{1783}
<\frac2{\sqrt5}.
}
\tag{6.1}
\]

### Proof

The exact Coxeter development gives the `{4,5}` sphere sizes through radius ten

\[
1,5,15,40,105,275,720,1885,4935,12920,33825,
\]

and, after passing to the medial graph, gives the exact `T` sphere sizes

\[
\boxed{
1,4,10,20,38,70,130,240,446,824,1528
}
\tag{6.2}
\]

for medial radii `0,1,\ldots,10`.

Let `B_9` be the radius-nine graph ball in `T`. Summing (6.2) through radius nine gives

\[
|B_9|
=1+4+10+20+38+70+130+240+446+824
=1783.
\tag{6.3}
\]

For every graph-distance ball, each outside neighbor of `B_9` has distance exactly ten, and every radius-ten vertex has a predecessor at radius nine. The checker additionally verifies that every developed medial vertex of distance at most nine has its full degree four present, so no boundary edge or boundary vertex is lost to truncation. Hence

\[
\partial_VB_9=S_{10},
\qquad
|\partial_VB_9|=1528.
\tag{6.4}
\]

Therefore, directly from the definition of `Phi_V`,

\[
\Phi_V(T)
\le
\frac{|\partial_VB_9|}{|B_9|}
=rac{1528}{1783}.
\]

The strict improvement over the previous upper bound is exact: both quantities are positive, and

\[
\frac{1528}{1783}<\frac2{\sqrt5}
\iff
5\cdot1528^2<4\cdot1783^2.
\]

The integer margin is

\[
4\cdot1783^2-5\cdot1528^2=1,042,436>0.
\]

This proves (6.1). QED.

### Exact finite certificate

The checker is

`artifacts/R06/20260920T0109Z_i0056_tetrapentagonal_vertex_ball_exact_76_c1d7.py`.

It was executed before this report. Its archived output is

`artifacts/R06/20260920T0109Z_i0056_tetrapentagonal_vertex_ball_exact_76_c1d7.out`,

ending with

`ALL_EXACT_CHECKS_PASS`.

This is an R06 **self-check**, not an independent outside audit.

## 7. Certified interval movement on the still-open source clause

Combining (6.1) with the inherited rigorous lower bound gives

\[
\boxed{
\frac1{\sqrt3+\sqrt5-2}
\le
\Phi_V(T)
\le
\frac{1528}{1783}.
}
\tag{7.1}
\]

Numerically,

\[
0.5080994133009662
\le
\Phi_V(T)
\le
0.8569826135726304.
\]

The certified width of this **secondary, source-clause interval** moves from

\[
\frac2{\sqrt5}-\frac1{\sqrt3+\sqrt5-2}
\approx0.38632777769894966
\]

to

\[
\boxed{
\frac{1528}{1783}-\frac1{\sqrt3+\sqrt5-2}
\approx0.3488832002716642.
}
\tag{7.2}
\]

That is a decrease of about `0.03744457742728546`, or `9.69%` of the preceding certified width.

This is real progress on the **more-general transitive-plane-graph** clause. It does **not** move the frozen `H_{5,5}` metric, which remains exactly zero-width, and it does not solve the full Question 6.20.

## 8. What this teaches and what remains

The exact shell sequence shows that the old vertex upper `2/sqrt(5)` was not close enough to be treated as a plausible endpoint merely because it was also the sharp-looking edge-ball upper. The vertex problem sees substantial boundary-vertex collisions that the edge boundary does not.

The previous edge obstruction is still open. For the `(4,5)`-biregular quadrangulated disk `D`, the exact identity

\[
4F+11B+40=10\Delta_4+8\Delta_5
\]

and candidate turn cap

\[
10\Delta_4+8\Delta_5
\le
40+(11+2\sqrt5)B
\]

remain the live route toward `Phi_E(T)=2/sqrt(5)`. This run neither proves nor refutes that edge statement.

For `Phi_V(T)`, the strongest next attack is now different: classify the finite Coxeter cone types of medial-distance spheres and derive an exact finite-state transition matrix. If that gives an algebraic limiting ratio for

\[
\frac{|S_{n+1}|}{|B_n|},
\]

then the graph balls yield a rigorous asymptotic upper bound potentially below `1528/1783`, after which a lower-bound argument should target the same cone-type/turn structure rather than recycle the edge inequality.

Proposed next moves: **#12 FIND WHAT IS CONSERVED, #14 FIND THE GROUP ACTING, #19 MAKE IT AN ALGORITHM.**

## 9. Model / scheduler truth

The model-control limitation is still unchanged. The exposed scheduling surface available to this worker has controls for task identity/title/prompt, recurrence/timing mode, and enabled state, but no binding model-family field, no reasoning-effort field, no guaranteed hour-long execution field, and no authenticated applied-model/effort receipt. Thus `GPT-6 / maximum` remains a prompt preference rather than an enforceable worker-side setting on this interface.

The repository's current deployment record also says the historical P26 `You cannot modify this task` failure was authorization-context-specific and that a later authorized context successfully updated P26. The compliant workaround is therefore the owning/authorized product, admin, or API context (or a platform schema that persists model/effort fields), not a permission bypass. No scheduler or permission change was attempted in this run.

## 10. Structured ledger delta

```yaml
ledger_delta:
  worker: R06
  source: "Russell Lyons and Yuval Peres, Probability on Trees and Networks, Question 6.20 / intake I0056"
  full_source_status: PARTIAL

  frozen_target:
    graph: "H_{5,5}={5,5}"
    class: "regular co-regular plane tessellation"
    parameters: "degree 5, face degree 5"
    normalization: "outer vertex boundary |partial_V K|/|K|"
    metric: "certified interval width U-L for Phi_V(H_{5,5})"
    before: 0
    after: 0
    exact_value: "sqrt(5)"
    status: "PROVED / audit-complete / posted subclass; full source still PARTIAL"

  source_clause_progress:
    graph: "T=M(H_{5,4})=r{4,5}, vertex-transitive tetrapentagonal plane graph"
    quantity: "Phi_V(T)"
    lower_bound_before: "1/(sqrt(3)+sqrt(5)-2)"
    lower_bound_after: "1/(sqrt(3)+sqrt(5)-2)"
    upper_bound_before: "2/sqrt(5)"
    upper_bound_after: "1528/1783"
    interval_width_before: 0.38632777769894966
    interval_width_after: 0.3488832002716642
    new_claim: "R06-I0056-TETRA-VBALL-01"
    claim_status: "PROVED PARTIAL with exact R06 self-check; not independently audited"

  tried_moves:
    - 1
    - 2
    - 16

  evidence:
    idea_before_code: "artifacts/R06/20260920T0109Z_i0056_tetrapentagonal_vertex_ball_idea_76_c1d7.md"
    checker: "artifacts/R06/20260920T0109Z_i0056_tetrapentagonal_vertex_ball_exact_76_c1d7.py"
    checker_output: "artifacts/R06/20260920T0109Z_i0056_tetrapentagonal_vertex_ball_exact_76_c1d7.out"
    checker_verdict: "ALL_EXACT_CHECKS_PASS"
    finite_core: "|B_9|=1783, |partial_V B_9|=1528"

  audits:
    frozen_H55: "existing R05 and P26 passes retained"
    new_tetrapentagonal_ball_bound: "self-check only; no independent audit requested in this progress-first run"

  remaining_obligation: >-
    Determine the exact Phi_V(T), or materially narrow (7.1) again. The strongest
    next route is an exact cone-type transition system for medial graph-distance
    spheres. Separately, the realizable-disk TURN-CAP remains the edge-constant
    obstruction. Neither restricted result closes the full Question 6.20.

  delivery: "report creation/readback pending at write time"
```

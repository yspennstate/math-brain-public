Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. FROZEN I0056 METRIC NO MOVEMENT / SOURCE-CLAUSE BOUND MOVEMENT: `H_{5,5}` width `0 -> 0`; for the source-valid mixed-face graph `T=r{4,5}`, the certified vertex upper bound improves `1528/1783 -> 33178/38983`, shrinking its rigorous secondary interval width `0.3488832002716642 -> 0.3429895229019940`; methods #12 FIND WHAT IS CONSERVED, #14 FIND THE GROUP ACTING, #19 MAKE IT AN ALGORITHM.**

# R06 / I0056 — exact Schreier growth improves the tetrapentagonal vertex bound

Repository: private `yspennstate/math-open-problems`, branch `master`.  
Worker: R06.  
Source: Russell Lyons and Yuval Peres, *Probability on Trees and Networks*, Question 6.20; intake `I0056`.  
Overall source status after this run: **PARTIAL**.

## 1. Exact source and frozen metric

The maintained Lyons–Peres question is still:

> What is `Phi_V(G)` for regular, co-regular plane graphs `G`? What are `Phi_E(G)` and `Phi_V(G)` for more general transitive, plane graphs `G`?

The normalization retained throughout R06 is

\[
\Phi_V(G)=\inf_{\varnothing\ne K\subset V(G),\ |K|<\infty}
\frac{|\partial_V K|}{|K|},
\qquad
\partial_V K=\{x\notin K:\exists y\in K,\ x\sim y\}.
\]

The frozen regular/co-regular target remains

\[
H_{5,5}=\{5,5\},\qquad (d,f)=(5,5),
\]

with the already proved/audited/posted value

\[
\boxed{\Phi_V(H_{5,5})=\sqrt5},\qquad [L,U]=[\sqrt5,\sqrt5],\qquad U-L=0.
\]

Therefore the fixed metric cannot numerically decrease. The full source stays **PARTIAL**, because Question 6.20 also asks for edge and vertex constants in more general transitive plane graphs. The posted regular-tessellation manuscript is an exclusion from duplicate research, not closure of this second clause.

Haslegrave–Panagiotis, DOI `10.1002/rsa.20946`, remain prior art for the codegree-3 and codegree-4 regular hyperbolic cases. Their paper explicitly establishes the vertex-isoperimetric constants for the triangular and square hyperbolic lattices. Nothing below is relabeled from those cases.

## 2. Current literature boundary checked 20 September 2026

Primary/current sources checked this run:

- Lyons–Peres maintained book: `https://rdlyons.pages.iu.edu/prbtree/book_pb.pdf`. Its current Question 6.20 retains both clauses and annotates Haslegrave–Panagiotis for codegrees 3 and 4.
- Haslegrave–Panagiotis, *Site percolation and isoperimetric inequalities for plane graphs*, Random Structures & Algorithms 58 (2021), DOI `10.1002/rsa.20946`.
- *Enumeration and Growth Functions for Uniform Tilings of the Hyperbolic Plane*, Ars Combinatoria 160 (2024), DOI `10.61091/ars-160-14`. This paper defines generations by graph distance, classifies degree-4 uniform types including `[n;m;n;m]`, and develops a face-position/generating-function method. In the checked text it works out all valence-5 families and selected valence-6 families, not an explicit growth function for the degree-4 `[4,5,4,5]` case used below.

Dated search strings also included exact shell fragments, `"[4,5,4,5]" growth function tiling`, `"4.5.4.5" coordination sequence hyperbolic`, and the candidate recurrence polynomial. I did not recover a primary source stating the shell sequence or exact outer-vertex constant below. This is **bounded negative evidence only**, not a novelty or priority certificate.

## 3. Inherited source-valid mixed-face target

Let

\[
R=H_{5,4}=\{4,5\}
\]

be the degree-five regular quadrangulation and let

\[
T=M(R)=r\{4,5\}
\]

be its medial graph. Then `T` is a 4-regular vertex-transitive plane graph with cyclic face type `[4,5,4,5]`. It belongs to the “more general transitive plane graph” clause of Question 6.20 and is not co-regular.

Before this run the best certified R06 vertex interval was

\[
\boxed{
\frac1{\sqrt3+\sqrt5-2}
\le \Phi_V(T)
\le \frac{1528}{1783}.
}
\tag{3.1}
\]

The upper bound came from the exact radius-nine ball in the preceding run.

## 4. Idea before code: methods #12, #14, #19

The idea was written first in

`artifacts/R06/20260920T0118Z_i0056_schreier_ball_idea_77_f3a1.md`.

### #14 — FIND THE GROUP ACTING

The preceding checker developed the primal `{4,5}` tessellation and only then formed the medial graph. A cleaner exact model works directly on edge midpoints.

Use the Coxeter group `[4,5]=<s_1,s_2,s_3>` over

\[
\mathbb Z[a,b],\qquad a^2=2,\quad b^2=b+1,
\]

where `a=sqrt(2)` and `b=phi=(1+sqrt(5))/2`. In simple-root coordinates take

\[
s_1=\begin{pmatrix}-1&a&0\\0&1&0\\0&0&1\end{pmatrix},\quad
s_2=\begin{pmatrix}1&0&0\\a&-1&b\\0&0&1\end{pmatrix},\quad
s_3=\begin{pmatrix}1&0&0\\0&1&0\\0&b&-1\end{pmatrix}.
\]

The checker verifies

\[
s_i^2=1,\qquad (s_1s_2)^4=(s_2s_3)^5=(s_1s_3)^2=1.
\]

Set

\[
r=s_2s_3,
\qquad q=s_1rs_1.
\]

A scaled midpoint of a fixed primal edge is

\[
M=(a,2,b)^T.
\]

It is fixed by `s_1` and `s_3`. The transformations `r,r^{-1}` rotate the fixed edge to its two consecutive edges at one endpoint, while `q,q^{-1}` do the same at the other endpoint. Hence the medial graph is exactly the orbit/Schreier graph generated from `M` by

\[
\boxed{r,\ r^{-1},\ q,\ q^{-1}}.
\tag{4.1}
\]

This eliminates the intermediate primal development and makes all four neighbors of every medial vertex explicit.

### #19 — MAKE IT AN ALGORITHM

Breadth-first search on exact orbit vectors in `Z[a,b]^3` now computes graph-distance generations with no geometric tolerance or floating-point identification. Because (4.1) is the complete degree-four neighbor set, a radius-`N` search determines every sphere through `N` exactly.

### #12 — FIND WHAT IS CONSERVED

The extended exact shells reveal a short integer recurrence after the initial transient. I record it below as a **candidate all-generation invariant**, but do not promote it to a theorem without the missing face-position/cone-type induction.

## 5. Rigorous new bound

### Proposition R06-I0056-TETRA-VBALL-02

For the tetrapentagonal transitive plane graph `T=r{4,5}`,

\[
\boxed{
\Phi_V(T)\le \frac{33178}{38983}=0.8510889362029602\ldots
<\frac{1528}{1783}.
}
\tag{5.1}
\]

### Proof

The exact Schreier BFS gives the sphere sizes

\[
\boxed{
1,4,10,20,38,70,130,240,446,824,1528,2824,5234,9680,17934,33178,61450
}
\tag{5.2}
\]

for radii `0,1,...,16`.

Let `B_14` be the radius-14 graph ball. From (5.2),

\[
|B_{14}|
=\sum_{j=0}^{14}|S_j|
=38983.
\tag{5.3}
\]

In every graph, an outside neighbor of a radius-`14` ball has distance exactly `15`, and every radius-`15` vertex has a predecessor at radius `14`. Since (4.1) gives all four neighbors exactly,

\[
\partial_V B_{14}=S_{15},
\qquad
|\partial_VB_{14}|=33178.
\tag{5.4}
\]

Therefore

\[
\Phi_V(T)
\le
\frac{|\partial_VB_{14}|}{|B_{14}|}
=rac{33178}{38983}.
\]

The improvement over the preceding exact ball is itself exact:

\[
\frac{33178}{38983}<\frac{1528}{1783}
\]

because

\[
1528\cdot38983-33178\cdot1783=409650>0.
\]

This proves (5.1). `QED`

### Exact finite certificate

Executed checker:

`artifacts/R06/20260920T0118Z_i0056_schreier_ball_exact_77_f3a1.py`

Archived output:

`artifacts/R06/20260920T0118Z_i0056_schreier_ball_exact_77_f3a1.out`

The output ends with `ALL_EXACT_CHECKS_PASS`. This is an R06 **self-check**, not an independent audit.

## 6. Certified interval movement on the unresolved source clause

Combining (5.1) with the inherited rigorous lower bound gives

\[
\boxed{
\frac1{\sqrt3+\sqrt5-2}
\le
\Phi_V(r\{4,5\})
\le
\frac{33178}{38983}.
}
\tag{6.1}
\]

Numerically,

\[
0.5080994133009662
\le \Phi_V(r\{4,5\})
\le 0.8510889362029602.
\]

Thus the rigorous **secondary source-clause interval** width moves

\[
0.3488832002716642
\longrightarrow
\boxed{0.3429895229019940}.
\]

The decrease is

\[
0.00589367736967017,
\]

about `1.6893%` of the preceding certified width. The frozen `H_{5,5}` metric remains exactly zero-width, as it must.

## 7. Structural discovery: a candidate exact growth recurrence

The exact spheres (5.2) satisfy, for every tested `7<=n<=16`,

\[
\boxed{
S_n=S_{n-1}+2S_{n-2}-2S_{n-3}+2S_{n-4}+S_{n-5}-S_{n-6}.
}
\tag{7.1}
\]

The checker verifies all ten identities exactly. Equivalently, the candidate characteristic polynomial is

\[
P(\lambda)=
\lambda^6-\lambda^5-2\lambda^4+2\lambda^3-2\lambda^2-\lambda+1.
\tag{7.2}
\]

Its largest positive root is approximately

\[
\lambda_*=1.8511890336360666.
\]

**Status of (7.1): CONJECTURAL as an all-`n` statement.** The finite exact agreement is not a proof that the recurrence continues. If a face-position/cone-type induction proves (7.1), the graph-ball boundary/volume ratio would have the candidate limit `lambda_*-1≈0.8511890336360666`. This is mainly valuable as a structural target: it says the shell process likely closes on finitely many generation types, exactly the kind of mechanism developed in the 2024 uniform-tiling enumeration paper.

I do **not** use (7.1) to certify any uncomputed sphere or any bound in (6.1).

## 8. What moved, what failed, and the next exact obstruction

- **#14 succeeded strongly:** the mixed-face graph has a four-generator exact Schreier model on edge midpoints; this is a substantially simpler representation than developing the primal tessellation first.
- **#19 succeeded:** exact BFS extends the rigorously known shell sequence through radius 16 and yields a new finite-set upper bound.
- **#12 produced a precise structural target:** the order-six recurrence is exact on ten consecutive tested generations, but the missing all-generation induction is the point where finite evidence stops.

The new bound is real source-clause progress but does not determine `Phi_V(T)`, and still less the full Question 6.20. A larger-ball computation alone is now low-value. The next useful step should prove or disprove the finite-state generation mechanism itself.

The nearest literature technique is the 2024 face-position method: classify vertices by arrival/departure/fraternal-edge position, derive a closed recurrence, and solve the corresponding generating function. The missing R06 theorem is therefore concrete:

\[
\textit{prove that the `[4,5,4,5]` graph-distance generations close on finitely many face positions,}
\]

with transition matrix whose scalar elimination yields (7.1), or exhibit the first generation where this candidate closure fails.

Suggested next moves: **#18 SAY IT IN ANOTHER LANGUAGE** (translate the Schreier recurrence into face-position states), **#13 FIND WHAT ONLY INCREASES** (control face closures by distance), and **#30 ONE SCALE/DIRECTION AT A TIME** (prove the transitions separately for square and pentagon sectors).

## 9. Model / scheduler truth

The platform surface available to this worker still does not expose a binding model-family selector, a binding reasoning-effort selector, a guaranteed hour-long execution setting, or authenticated applied-model/effort telemetry. The current repository progress-first directive says the same. Therefore the request for GPT-6/maximum remains prompt text on this surface, while this report truthfully identifies the actual model as GPT-5.6 Sol and the reasoning level as UNVERIFIED.

The historical P26 `You cannot modify this task` error was authorization-context-specific; repository deployment records say a later authorized context succeeded. The compliant remedy is the owning/authorized product, admin, or API context (or a platform schema exposing model/effort controls), not a permission bypass. No scheduler or permission change was attempted.

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
    unchanged_count: UNKNOWN

  source_clause_target:
    graph: "T=r{4,5}=M({4,5})"
    class: "4-regular vertex-transitive plane graph, face type [4,5,4,5]"
    normalization: "outer vertex boundary |partial_V K|/|K|"
    lower_bound: "1/(sqrt(3)+sqrt(5)-2)"
    upper_before: "1528/1783"
    upper_after: "33178/38983"
    interval_width_before: 0.3488832002716642
    interval_width_after: 0.3429895229019940
    status: "PROVED PARTIAL / R06 self-check only"

  tried_moves: [12, 14, 19]
  new_structural_lead:
    statement: "S_n=S_(n-1)+2S_(n-2)-2S_(n-3)+2S_(n-4)+S_(n-5)-S_(n-6)"
    verified_range: "7 <= n <= 16"
    global_status: CONJECTURAL

  remaining_obligation: "prove an all-generation face-position/cone-type recurrence for [4,5,4,5] and then obtain a matching lower bound, or find a counterexample generation/finite set; full Lyons-Peres Q6.20 remains broader"
  evidence:
    idea: "artifacts/R06/20260920T0118Z_i0056_schreier_ball_idea_77_f3a1.md"
    checker: "artifacts/R06/20260920T0118Z_i0056_schreier_ball_exact_77_f3a1.py"
    output: "artifacts/R06/20260920T0118Z_i0056_schreier_ball_exact_77_f3a1.out"
  audits: "none for the new 33178/38983 bound; exact checker is a self-check"
  prior_art_exclusion: "Haslegrave-Panagiotis codegree 3/4 regular cases; not relabeled"
```

Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. FROZEN I0056 METRIC NO MOVEMENT / SOURCE-CLAUSE VERTEX-INTERVAL MOVEMENT: `Phi_V(H_{5,5})` width `0 -> 0`; for the source-valid tetrapentagonal graph `T=r{4,5}`, the rigorous vertex interval width improves `0.1200988393729347496 -> 0.04239362816392151105`; full Lyons–Peres Question 6.20 remains PARTIAL. Descriptive methods #18 SAY IT IN ANOTHER LANGUAGE, #3 PROVE SOMETHING STRONGER, #12 FIND WHAT IS CONSERVED. The I0056 method palette is historically exhausted, so these labels are not falsely represented as never-before-used; they differ from the immediate predecessor's #5/#26/#27.**

# R06 / I0056 — self-improving outer-core bound for the tetrapentagonal vertex constant

Repository: private `yspennstate/math-open-problems`, branch `master`.  
Worker: R06.  
Outside source: Russell Lyons and Yuval Peres, *Probability on Trees and Networks*, Question 6.20; intake `I0056`.  
Overall source status after this run: **PARTIAL**.

## 1. Source, frozen metric, continuity, and prior art

The current online Lyons–Peres edition still asks:

> **Question 6.20.** What is `Phi_V(G)` for regular, co-regular plane graphs `G`? What are `Phi_E(G)` and `Phi_V(G)` for more general transitive, plane graphs `G`?

The frozen R06 regular/co-regular regime remains

\[
H_{5,5}=\{5,5\},\qquad (d,f)=(5,5),
\]

with the original outer-vertex normalization

\[
\Phi_V(G)=\inf_{\varnothing\ne S\subset V(G),\ |S|<\infty}
\frac{|\partial_VS|}{|S|}.
\]

The retained exact result is

\[
\boxed{\Phi_V(H_{5,5})=\sqrt5},\qquad [L,U]=[\sqrt5,\sqrt5],\qquad U-L=0.
\]

That zero-width frozen metric therefore cannot improve numerically. It is already part of the posted regular-tessellation work; this run does not relabel it as new.

The still-open source clause attacked here is the second clause, through the 4-regular vertex-transitive tetrapentagonal graph

\[
T=r\{4,5\}=M(\{4,5\}),
\]

with cyclic face type `[4,5,4,5]`.

At run start I recovered/rechecked the current `INDEX.md`, `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/claims/I0056.md`, the current owner directive and follow-up implementation manifest, the I0056 intake/ownership search, the newest substantive R06 report, and neighboring-track search results. The root ledger is known to lag newer immutable R06 mathematics, so no older `UNMEASURED` row is substituted for the current complete reports.

The immediate mathematical predecessor is

`runs/R06/20260920T0935Z_i0056_threeclosure_vertex_lower_83_4f8c.md`,

which gave

\[
\frac{2}{\sqrt3+\sqrt5-1}
\le \Phi_V(T)
\le \frac{384566}{484385}.
\tag{1.1}
\]

The exact upper witness is from

`runs/R06/20260920T0615Z_i0056_symmetry_quotient_vertex_upper_81_b47e.md`.

Two older inputs are also retained:

\[
h:=\Phi_E(T)\text{ lower bound}
=\frac4{1+\sqrt3+\sqrt5},
\tag{1.2}
\]

proved in `runs/R06/20260916T1922Z_i0056_medial_dual_euler_02.md`, and

\[
q:=\Phi_V(H_{4,5})=\frac2{\sqrt3},
\tag{1.3}
\]

from the regular/co-regular R06 theorem used there. The regular/co-regular dependency has distinct other-track mathematical passes in repository history, including

`R05-AUDIT-R06-I0056-CLOSURE-01-COR-F5-20260916T151529Z`

and the later P26 pass recorded in `runs/R06/20260918T132459Z_i0056_prior_art_interpolation_42.md`. Those audits do **not** audit the new mixed-face theorem below.

Haslegrave–Panagiotis, DOI `10.1002/rsa.20946`, remain excluded prior art: their paper establishes the exact vertex constants for triangular and square hyperbolic lattices, i.e. the regular codegree-3/codegree-4 cases. This run does not claim those cases.

## 2. Current literature check — 20 September 2026

Fresh bounded queries included:

- exact Lyons–Peres Question 6.20 wording;
- `Site percolation and isoperimetric inequalities for plane graphs` / DOI `10.1002/rsa.20946`;
- `tetrapentagonal Cheeger constant`;
- `tetrapentagonal vertex isoperimetric constant`;
- `r{4,5} vertex expansion`;
- `[4,5,4,5] isoperimetric`;
- `edge-homogeneous tessellation isoperimetric constant`;
- later/citing work around uniform hyperbolic tilings.

The current Lyons–Peres online paperback still prints the full source question and explicitly records Haslegrave–Panagiotis only for codegrees 3 and 4. Haslegrave–Panagiotis' abstract likewise says their exact result covers triangular and square hyperbolic lattices.

The bounded mixed-face search recovered Graves–Pisanski–Watkins, *Growth of Edge-Homogeneous Tessellations*, SIAM J. Discrete Math. 23 (2008/09), DOI `10.1137/070707026`, which computes exponential growth/enumeration for edge-homogeneous tessellations. It did **not** yield an exact outer-vertex isoperimetric formula for `r{4,5}` in the material checked. No current primary source was found giving the bound proved below or the exact `Phi_V(r{4,5})`. This is bounded negative evidence only; **novelty/priority remains UNVERIFIED**.

## 3. Ideas before code

Two idea notes were written before the algebra checker:

- `artifacts/R06/20260920T1305Z_i0056_outercore_squarebudget_idea_84_9b71.md` @ `9778efd720d62ad1fe7e947e6389ea1fcdf687c6`;
- `artifacts/R06/20260920T1309Z_i0056_vertex_bootstrap_idea_84_9b71.md` @ `35c3d45563bdc3102e5f025b83284a4936a0b138`.

The first found a stronger plane-core quotient. The second noticed that the already-known vertex lower bound can be fed back into the interior of the core, creating a monotone self-improvement map and a fixed-point lower bound.

## 4. Normalization lemma: from outer boundary to a multiplicity-one core

Write

\[
\rho(S):=\frac{|\partial_VS|}{|S|}.
\]

We first prove a reduction that will be used for every bootstrap level `g>1/2`.

Assume a rigorous global lower bound

\[
\Phi_V(T)\ge g>\frac12.
\tag{4.1}
\]

Starting from a finite nonempty set `S`, repeatedly perform any applicable move:

1. fill a finite component of `T\setminus S`;
2. add a boundary vertex having at least three `S`-neighbors;
3. add a boundary vertex `x` having exactly two `S`-neighbors if one of the other two neighbors of `x` already lies in `partial_V S`;
4. after move 3 is unavailable, if two distinct multiplicity-two boundary vertices share one of their two outward neighbors, add the pair.

Every move does not increase `rho`.

- Filling a hole adds vertices, deletes boundary vertices, and creates no new boundary vertex outside the filled component.
- In move 2, if `x` has `k>=3` selected neighbors, deleting `x` from the boundary and exposing at most `4-k` new vertices changes boundary size by at most `3-k<=0`.
- In move 3, one of the two possible newly exposed vertices is already in the boundary, so the net boundary change is at most zero.
- In move 4, move 3 being unavailable implies the two selected-to-be-added boundary vertices are nonadjacent and all four outward slots were outside the old closed neighborhood. A shared outward vertex means at most three new boundary vertices replace the two old boundary vertices, so `Delta |partial_V|<=1` while `Delta |S|=2`. Since every intermediate finite set still obeys (4.1), its ratio is at least `g>1/2`, and therefore

\[
\frac{b+1}{n+2}\le\frac bn.
\]

The process terminates. Let `E(S)=|partial_E S|`. Hole filling and move 2 strictly decrease `E`; moves 3 and 4 preserve `E` (each newly added nonadjacent multiplicity-two vertex has two old and two new crossing edges). Thus `E` is a nonincreasing nonnegative integer. Between two strict decreases, every move increases `|S|`, while the retained edge inequality (1.2) bounds

\[
|S|\le E(S)/h.
\]

So infinitely many moves are impossible.

Let `K` be a terminal set. Every boundary vertex has one or two `K`-neighbors. Write `B_1,B_2` for the two types and

\[
b_1=|B_1|,\qquad m=|B_2|.
\]

For every `x in B_2`, its two non-`K` neighbors lie outside `N[K]`; distinct `B_2` vertices have disjoint outward-neighbor pairs; and `B_2` is independent. Define

\[
C:=K\cup B_2.
\]

Then every vertex of `partial_V C` has exactly one neighbor in `C`. More explicitly,

\[
|C|=|K|+m=:N,
\qquad
|\partial_E C|=|\partial_V C|=b_1+2m=:E.
\tag{4.2}
\]

Let `a(C)` be the number of selected vertices of internal `C`-degree exactly two. Every swallowed `B_2` vertex is such a vertex, so `a>=m`.

If the starting ratio was below a number `<1`, then the terminal `K` also satisfies `rho(K)<1`, which by (4.2) is equivalent to `E<N`. Consequently

\[
f(t):=\frac{E-t}{N-t}
\]

is decreasing, and

\[
\rho(K)
=\frac{E-m}{N-m}
\ge
\frac{E-a}{N-a}
=:R(C).
\tag{4.3}
\]

Thus a small outer-vertex ratio forces a small auxiliary core quotient `R`.

## 5. Hole filling and leaf pruning do not increase the core quotient

The quantities

\[
P(C):=E(C)-a(C),
\qquad
D(C):=|C|-a(C)
\]

are additive over connected components. A component with `D=0` consists entirely of internal-degree-two vertices; then `E=2|C|` and `P=|C|>0`, so such a component can only increase the global quotient. Hence if `R(C)<r`, some connected component with positive denominator has `R<r`. Fix one such component.

### Fill all finite holes

Suppose the union of finite complement components has `M` vertices and `e` crossing edges from the current component. Because the current outer boundary has crossing multiplicity one, every hole-boundary vertex has exactly one selected neighbor, so

\[
e\le M.
\tag{5.1}
\]

After the holes are filled, every newly added hole vertex has all four graph neighbors selected and therefore is internal degree four; no new degree-two vertex comes from the filled component itself.

Let `t` be the number of old degree-two vertices hit by a hole edge, and let `ell` be the number of old degree-one vertices which receive exactly one hole edge and therefore become degree two. Then

\[
t+\ell\le e,
\qquad
\ell\le M,
\]

and

\[
a'=a-t+\ell,\quad
E'=E-e,\quad
N'=N+M.
\]

Therefore

\[
P'=P-e+t-\ell\le P,
\]

while

\[
D'=D+M+t-\ell\ge D.
\]

Hence `R=P/D` does not increase. The resulting set is connected, induced, hole-free, and its outer boundary still has crossing multiplicity one.

### Peel leaves

Now repeatedly remove an internal-degree-one selected vertex `v`. Its three exterior neighbors are private boundary vertices, so removal preserves connectedness (until the trivial final case), hole-freeness and boundary multiplicity one, and changes `E` by `-2`.

If the unique selected neighbor of `v` has current internal degree 4, 3, or 2, respectively, the pair `(P,D)` changes by

\[
(-2,-1),\qquad(-3,-2),\qquad(-1,0).
\]

While `R<1`, each of these changes does not increase `R`. A would-be denominator-zero terminal degeneracy is an all-degree-two cycle (or the preceding cycle-plus-leaf configuration), whose quotient is at least one, contradicting the maintained `R<1` hypothesis.

Thus every hypothetical counterexample with ratio `<1` reduces to a finite connected induced hole-free set `D` with minimum internal degree at least two, boundary crossing multiplicity one, and no larger core quotient.

## 6. Method #12 / conserved plane budget on the reduced core

For such a reduced core `D`, classify selected vertices as follows:

- `a`: internal degree 2;
- `b`: internal degree 3;
- `o`: internal degree 4 and incident with the unbounded face;
- `i`: internal degree 4 and not incident with the unbounded face.

Then

\[
N=a+b+o+i,
\qquad
E=|\partial_E D|=2a+b.
\tag{6.1}
\]

Every degree-2 or degree-3 selected vertex lies on the unbounded face: otherwise one of its missing graph neighbors would lie in a bounded complement component, contradicting hole-freeness.

Let `F_4,F_5` be the numbers of bounded ambient square and pentagonal faces of the induced plane graph, and let `L` be the length of its unbounded-face boundary **walk**, with bridge sides counted with multiplicity. Hole-freeness and inducedness ensure every bounded face is one ambient square or pentagon.

Euler and (6.1) give

\[
F_4+F_5
=N-E/2+1
=\frac b2+o+i+1.
\tag{6.2}
\]

The face-degree sum is

\[
4F_4+5F_5+L=2e(D)=4N-E.
\]

Combining with (6.2),

\[
\boxed{F_5=E-L-4.}
\tag{6.3}
\]

The unbounded-face walk meets each of the `a+b+o` distinct outer-face selected vertices at least once, so

\[
L\ge a+b+o.
\]

Hence

\[
F_5\le a-o-4,
\]

and therefore

\[
\boxed{
F_4\ge \frac b2+i+2o-a+5.
}
\tag{6.4}
\]

This is the conserved square-face budget driving the improvement.

## 7. Transfer the full-square set to `H_{4,5}`

Because every exterior boundary vertex of `D` has exactly one selected neighbor, a partial ambient square cannot have three selected vertices or two opposite selected vertices: either pattern would give an unselected square vertex two selected neighbors. Thus every partial square has exactly two selected/unselected transitions.

Every crossing edge of `D` lies on exactly one square of the tetrapentagonal tiling. If `Q_4` is the number of partial squares,

\[
2Q_4=E,
\qquad
Q_4=a+\frac b2.
\tag{7.1}
\]

The retained face-transfer lemma identifies square faces with vertices of

\[
H_{4,5}.
\]

A neighbor of a full square which is not full is necessarily partial because the two squares share the medial vertex corresponding to their common base edge. Hence

\[
\partial_V^{H_{4,5}}(\text{full squares})
\subseteq
\{\text{partial squares}\}.
\]

Using the retained exact value `q=2/sqrt(3)`, equations (6.4) and (7.1) imply

\[
qF_4\le Q_4,
\]
so

\[
\boxed{
(1+q)a+\frac{1-q}{2}b-2qo-qi\ge5q.
}
\tag{A}
\]

## 8. Two expansion inequalities for the interior vertices

Let `I` be the set of the `i` interior selected vertices. They have all four graph neighbors in `D`, so every edge/vertex boundary of `I` lies among the selected outer-face vertices of `D`.

An outer-face degree-two selected vertex has both selected incident edges on the unbounded-face walk and therefore cannot be adjacent to `I`. A degree-three outer vertex can have at most one edge into `I`; an outer degree-four vertex can have at most two.

The retained edge lower (1.2) gives

\[
hi\le |\partial_E I|\le b+2o,
\]
that is,

\[
\boxed{b+2o-hi\ge0.}
\tag{B}
\]

If, in addition, a global vertex lower `Phi_V(T)>=g` is already known, then

\[
gi\le |\partial_V I|\le b+o,
\]
so

\[
\boxed{b+o-gi\ge0.}
\tag{C_g}
\]

This is the self-improving input absent from the preceding R06 runs.

## 9. Method #3 / bootstrap theorem

Define

\[
c:=\frac{q+\frac h2(q-1)}{q+1},
\qquad
F(g):=\frac{g+c}{g+1}.
\tag{9.1}
\]

For the present exact `q,h`,

\[
c
=\frac{2\sqrt{15}+6\sqrt3}
 {3\sqrt5+2\sqrt{15}+5\sqrt3+9}
=0.56480138530590267339\ldots .
\tag{9.2}
\]

### Bootstrap theorem

For every rigorous lower bound `g>1/2`,

\[
\boxed{
\Phi_V(T)\ge g
\quad\Longrightarrow\quad
\Phi_V(T)\ge F(g).
}
\tag{R06-I0056-VERTEX-BOOTSTRAP-84}
\]

**Proof.** Suppose a finite set had outer-vertex ratio `<F(g)`. Here `F(g)<1` for the relevant range. Apply Sections 4–5 to obtain a reduced core with

\[
R=\frac{E-a}{N-a}
=\frac{a+b}{b+o+i}
<F(g).
\tag{9.3}
\]

Take inequality (A) with coefficient

\[
\alpha=\frac1{1+q},
\]

inequality (B) with coefficient

\[
\beta=\frac{q-1}{2(q+1)}>0,
\]

and inequality `(C_g)` with coefficient

\[
\gamma
=\frac{1-\frac h2(q-1)}{(g+1)(q+1)}>0.
\]

The last numerator is positive because `1<q<3` and `0<h<1`; in fact the exact checker gives much tighter rational brackets.

A direct coefficient calculation yields

\[
\alpha(A)+\beta(B)+\gamma(C_g):
\]

\[
\boxed{
 a+(1-F(g))b-F(g)(o+i)
 \ge \frac{5q}{1+q}>0.
}
\tag{9.4}
\]

Since `b+o+i>0`, (9.4) is precisely

\[
\frac{a+b}{b+o+i}>F(g),
\]

contradicting (9.3). This proves the bootstrap theorem. `square`

## 10. Iterate the bootstrap to its exact fixed point

A rigorous seed predating the immediate predecessor is

\[
g_0:=\frac1{\sqrt3+\sqrt5-2}
=0.50809941330096615215\ldots>\frac12,
\tag{10.1}
\]

from the earlier edge-to-vertex closure argument in the medial/dual R06 work.

Define

\[
g_{n+1}=F(g_n).
\]

The map has the exact identities

\[
F(g)-g=\frac{c-g^2}{g+1}
\tag{10.2}
\]

and, writing

\[
g_*:=\sqrt c,
\]

\[
F(g)-g_*
=\frac{(1-g_*)(g-g_*)}{g+1}.
\tag{10.3}
\]

The exact rational brackets archived by the checker give

\[
\frac{121}{215}<c<\frac{31}{54},
\]
so

\[
\frac34<g_*<\frac{19}{25}.
\]

Also `g_0<51/100`. Thus `g_0<g_*`. Equations (10.2)–(10.3) show that `g_n` increases monotonically to `g_*` while remaining below it. Applying the bootstrap theorem inductively gives

\[
\Phi_V(T)\ge g_n
\qquad\text{for every }n,
\]

and therefore

\[
\boxed{
\Phi_V(r\{4,5\})
\ge
\sqrt{
\frac{2\sqrt{15}+6\sqrt3}
 {3\sqrt5+2\sqrt{15}+5\sqrt3+9}
}
}
\tag{10.4}
\]

with numerical value

\[
\boxed{
0.751532690776590684825245981810\ldots
}.
\tag{10.5}
\]

This strictly improves the immediate predecessor's lower bound

\[
\frac2{\sqrt3+\sqrt5-1}
=0.673827479567577446\ldots .
\]

## 11. New rigorous interval and quantitative movement

Combine (10.4) with the retained exact finite upper witness:

\[
\boxed{
\sqrt{
\frac{2\sqrt{15}+6\sqrt3}
 {3\sqrt5+2\sqrt{15}+5\sqrt3+9}
}
\le
\Phi_V(r\{4,5\})
\le
\frac{384566}{484385}.
}
\tag{11.1}
\]

Numerically,

\[
0.7515326907765906848\ldots
\le\Phi_V(r\{4,5\})
\le
0.7939263189405121959\ldots .
\]

The certified mixed-face vertex interval width moves

\[
0.120098839372934749598756195172\ldots
\]

to

\[
\boxed{
0.0423936281639215110520004234253\ldots
},
\tag{11.2}
\]

a reduction of about

\[
\boxed{64.7010509133\%}
\]

of the remaining gap from the immediate predecessor.

This is genuine rigorous interval movement for the still-open source-valid mixed-face constant. It does **not** redefine the frozen `H_{5,5}` metric, whose width stays zero.

## 12. Exact self-check

Executed symbolic checker:

`artifacts/R06/20260920T1312Z_i0056_vertex_bootstrap_exact_84_9b71.py`

created at commit

`c1e7b4d6d85c0498031ab46761ec2932d584ff96`.

Archived executed output:

`artifacts/R06/20260920T1312Z_i0056_vertex_bootstrap_exact_84_9b71.out`

created at commit

`cb90c9e24915edea4d888e3e98bedcdd8623505e`

and read back at that exact commit.

The checker verifies symbolically:

- the coefficients in the nonnegative combination of (A), (B), `(C_g)`;
- `F(g)-g=(c-g^2)/(g+1)`;
- the fixed-point identity `F(sqrt(c))=sqrt(c)`;
- exact rational brackets on `q,h,c` via integer-square comparisons;
- `g_0<g_*<384566/484385` without relying on floating-point signs;
- the old/new interval widths and numerical values.

Its output ends

`ALL_EXACT_SYMBOLIC_CHECKS_PASS`.

This is an **R06 self-check**. The theorem-sized combinatorial argument is written in Sections 4–10; the checker is not substituted for that proof.

## 13. Status, audits, and next attack

Status of the full source question remains **PARTIAL**.

What is proved this run is a new rigorous lower bound for one source-valid non-regular transitive plane graph, not the exact constant and not all of Question 6.20. No independent OTHER-track audit has yet been obtained for `R06-I0056-VERTEX-BOOTSTRAP-84`. The older R05/P26 audits concern the regular/co-regular dependency, not this new bootstrap theorem.

The gap for `Phi_V(r{4,5})` is now only about `0.04239`. The most valuable next mathematical attack is not another larger raw ball. It is to characterize equality/near-equality simultaneously in the three core inequalities:

1. the full-square transfer inequality (A);
2. the interior edge inequality (B);
3. the interior vertex inequality `(C_g)`.

At the fixed point the homogeneous relaxation makes all three active. That suggests a finite-state boundary contour with asymptotic proportions close to

\[
a:b:o:i\approx
0.35306359:0.39846910:0.03060236:0.57092854
\]

after normalizing `b+o+i=1`. Proving that this relaxation is unattainable would improve the lower bound again; constructing an asymptotically periodic contour realizing it would instead produce a strong upper candidate near `g_*`. This is the concrete next route.

## 14. Model / scheduler-control truth

The requested GPT-6 / maximum setting is still **not enforceable on the exposed scheduler surface**. The available task controls expose task identity/title, prompt, schedule/timing mode and enabled state, but no binding model-family selector, no reasoning-effort selector, no guaranteed hour-long runtime field, and no authenticated run-level receipt of applied model/effort. Therefore this report truthfully records `GPT-5.6 Sol / UNVERIFIED` rather than inferring GPT-6 from prompt text.

The historical P26 `You cannot modify this task` event was an authorization-context boundary, not a mathematical issue. The current root deployment ledger records that P26 was later successfully updated in another authorized context. A denied task edit therefore requires the owning/authorized product/admin/API context or a platform-side permission/schema fix; there is no compliant worker-side bypass.

```yaml
ledger_delta:
  track: R06
  source: "Russell Lyons and Yuval Peres, Probability on Trees and Networks, Question 6.20; intake I0056"
  frozen_target:
    graph: "H_{5,5}={5,5}"
    graph_class: "regular co-regular plane graph"
    degree_face_pair: [5, 5]
    normalization: "outer vertex boundary |partial_V S|/|S|"
    interval_before: "[sqrt(5), sqrt(5)]"
    interval_after: "[sqrt(5), sqrt(5)]"
    metric_width_before: 0
    metric_width_after: 0
    movement: "none; mathematically zero-width"
    unchanged_count: "historical zero-width streak preserved; not reset or recomputed from scratch"
  source_clause_secondary:
    graph: "T=r{4,5}=M({4,5}), tetrapentagonal [4,5,4,5]"
    quantity: "Phi_V(T)"
    previous_lower: "2/(sqrt(3)+sqrt(5)-1)"
    new_lower: "sqrt((2*sqrt(15)+6*sqrt(3))/(3*sqrt(5)+2*sqrt(15)+5*sqrt(3)+9))"
    upper: "384566/484385"
    interval_width_before: "0.120098839372934749598756195172..."
    interval_width_after: "0.0423936281639215110520004234253..."
    status: "PROVED PARTIAL / source remains PARTIAL"
  tried_moves:
    - "#18 SAY IT IN ANOTHER LANGUAGE: outer-boundary multiplicity -> normalized plane-core quotient; success"
    - "#3 PROVE SOMETHING STRONGER: proved a bootstrap implication Phi>=g => Phi>=F(g); success"
    - "#12 FIND WHAT IS CONSERVED: Euler/unbounded-walk square-face budget drives inequality (A); success"
  method_history_note: "all 30 numbered labels have appeared earlier in I0056 history; this report does not falsely call the labels unused; immediate predecessor triple #5/#26/#27 was not repeated"
  remaining_obligation: "close the 0.0423936 mixed-face vertex gap or determine the exact constant; then obtain current prior-art clearance and two independent audits for any closure claim"
  evidence:
    idea_1: "artifacts/R06/20260920T1305Z_i0056_outercore_squarebudget_idea_84_9b71.md @ 9778efd720d62ad1fe7e947e6389ea1fcdf687c6"
    idea_2: "artifacts/R06/20260920T1309Z_i0056_vertex_bootstrap_idea_84_9b71.md @ 35c3d45563bdc3102e5f025b83284a4936a0b138"
    checker: "artifacts/R06/20260920T1312Z_i0056_vertex_bootstrap_exact_84_9b71.py @ c1e7b4d6d85c0498031ab46761ec2932d584ff96"
    checker_output: "artifacts/R06/20260920T1312Z_i0056_vertex_bootstrap_exact_84_9b71.out @ cb90c9e24915edea4d888e3e98bedcdd8623505e"
    checker_verdict: "ALL_EXACT_SYMBOLIC_CHECKS_PASS"
    upper_witness_report: "runs/R06/20260920T0615Z_i0056_symmetry_quotient_vertex_upper_81_b47e.md"
    edge_lower_report: "runs/R06/20260916T1922Z_i0056_medial_dual_euler_02.md"
  audits:
    new_bootstrap_84: NONE
    regular_dependency_R05: "R05-AUDIT-R06-I0056-CLOSURE-01-COR-F5-20260916T151529Z = PASS_MATH_SCOPE / NOVELTY_UNVERIFIED"
    regular_dependency_P26: "retained P26 PASS recorded in runs/R06/20260918T132459Z_i0056_prior_art_interpolation_42.md"
  prior_art:
    haslegrave_panagiotis: "KNOWN / excluded triangular and quadrangular regular cases; DOI 10.1002/rsa.20946"
    graves_pisanski_watkins: "growth/enumeration only in checked material; DOI 10.1137/070707026"
    exact_tetrapentagonal_constant: "not found in bounded dated searches; novelty remains UNVERIFIED"
```

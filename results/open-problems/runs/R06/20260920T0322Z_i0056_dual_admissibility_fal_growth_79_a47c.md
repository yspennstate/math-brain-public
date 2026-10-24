Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. FROZEN I0056 METRIC NO MOVEMENT / STRUCTURAL OBSTRUCTION CLOSED: `H_{5,5}` width `0 -> 0`; for the source-valid tetrapentagonal graph `T=r{4,5}`, the rigorous interval remains `[1/(sqrt(3)+sqrt(5)-2), 113708/133611]`, but `FAL(4,5,4,5)` moves `CONDITIONAL -> PROVED` and the order-six graph-distance shell recurrence/growth series moves `CONDITIONAL -> PROVED`; methods #21 ASK WHO ELSE HAS THIS SHAPE, #20 FIND WHY THE ALGORITHM FAILS, #23 DO WHAT THE PROPOSER DID NOT EXPECT.**

# R06 / I0056 — dual admissibility proves the all-radius tetrapentagonal frontier anatomy

Repository: private `yspennstate/math-open-problems`, branch `master`.  
Worker: R06.  
Source: Russell Lyons and Yuval Peres, *Probability on Trees and Networks*, Question 6.20; intake `I0056`.  
Overall source status after this run: **PARTIAL**.

## 1. Source, normalization, and fixed metric

The retained source question is still

> What is `Phi_V(G)` for regular, co-regular plane graphs `G`? What are `Phi_E(G)` and `Phi_V(G)` for more general transitive, plane graphs `G`?

with

\[
\Phi_V(G)=\inf_{\varnothing\neq K\subset V(G),\ |K|<\infty}
\frac{|\partial_VK|}{|K|},
\qquad
\partial_VK=\{x\notin K:\exists y\in K,\ x\sim y\}.
\]

The frozen regular/co-regular regime is still

\[
H_{5,5}=\{5,5\},\qquad (d,f)=(5,5),
\]

with the already proved/audited/posted value

\[
\boxed{\Phi_V(H_{5,5})=\sqrt5},\qquad
[L,U]=[\sqrt5,\sqrt5],\qquad U-L=0.
\]

Thus the fixed metric stays `0 -> 0`. This does **not** close the full source question.

Haslegrave–Panagiotis, DOI `10.1002/rsa.20946`, remain excluded prior art. Their paper states that it establishes the vertex-isoperimetric constant for triangular and square hyperbolic lattices, i.e. the regular face/codegree `3` and `4` cases. Those cases are not relabelled here.

## 2. Continuity recovered before research

The immediate predecessor was

`runs/R06/20260920T0220Z_i0056_face_state_reduction_78_6e2b.md`.

It retained the source-valid mixed-face graph

\[
T=r\{4,5\}=M(\{4,5\}),
\]

the 4-regular vertex-transitive tetrapentagonal graph of cyclic face type `[4,5,4,5]`, with rigorous interval

\[
\boxed{
\frac1{\sqrt3+\sqrt5-2}
\le \Phi_V(T)
\le \frac{113708}{133611}.
}
\tag{2.1}
\]

The corresponding secondary interval width is

`0.34293830065971065`.

That run had exact spheres through radius 18 and a complete algebraic derivation of an order-six shell recurrence **conditional** on one all-radius frontier-anatomy lemma `FAL(4,5,4,5)`. It explicitly instructed the next run not to increase the BFS radius blindly, but to prove that structural lemma.

At run start I reread the campaign index/ranking, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, canonical `operations/claims/I0056.md`, the I0056 intake history, `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`, the owner new-method directive, and the predecessor report. `I0056` remains owned by R06. The regular `H_{5,5}` paper is already posted and was not duplicated.

## 3. Fresh literature boundary checked 20 September 2026

The new route came from literature rather than another finite development.

### 3.1 Baues–Peyerimhoff / Klassert–Lenz–Peyerimhoff–Stollmann

Oliver Baues and Norbert Peyerimhoff, *Geodesics in non-positively curved plane tessellations*, Advances in Geometry 6 (2006), 243–263, DOI `10.1515/ADVGEOM.2006.014`, develop the global layered geometry of plane tessellations with nonpositive corner curvature.

Steffen Klassert, Daniel Lenz, Norbert Peyerimhoff and Peter Stollmann, *Elliptic operators on planar graphs: Unique continuation for eigenfunctions and nonpositive curvature*, Proc. Amer. Math. Soc. 134 (2006), 1549–1559, DOI `10.1090/S0002-9939-05-08103-7`, explicitly recalls the pieces needed here:

- a polygon boundary is labelled `a/b`, with `a+` meaning inner degree one;
- admissibility means every `b` boundary vertex is flanked by `a+` vertices;
- in nonpositive corner curvature, the one-neighbourhood of an admissible polygon remains admissible;
- a newly added face meets the previous polygon boundary in a connected edge path of length at most two and contributes a nonempty connected edge path to the new boundary;
- all face-distance balls from a face are admissible polygons;
- the next face sphere has a cyclic enumeration in which two sphere faces intersect iff they are consecutive.

These are not new R06 claims; they are the published global input that was missing from the previous finite-state experiment.

### 3.2 Uniform-tiling growth literature

de Souza–da Silva, *Enumeration and Growth Functions for Uniform Tilings of the Hyperbolic Plane*, Ars Combinatoria 160 (2024), 161–193, DOI `10.61091/ars-160-14`, defines exactly the graph-distance arrival/departure/fraternal language used by R06 and obtains rational generating functions by face start/closure recurrences. The paper explicitly computes all valence-5 families and selected/general valence-6 families; it says the same reasoning applies to other valences. The checked full-text page does not print the `[4,5,4,5]` valence-4 graph-distance rational function derived below. Accordingly, the **method is prior art**; no novelty claim is made for rational-growth machinery itself.

Graves–Pisanski–Watkins, *Growth of Edge-Homogeneous Tessellations*, SIAM J. Discrete Math. 23 (2008), 1–18, DOI `10.1137/070707026`, and Graves–Watkins, *Growth of face-homogeneous tessellations*, Ars Math. Contemp. 14 (2018), study Bilinski/corona growth and include nearby `[4,5,4,5]` face-homogeneous geometry. Their growth metric is not automatically the rooted vertex graph-distance sphere sequence used in Question 6.20.

### 3.3 Search scope

Dated searches included `Question 6.20 Lyons Peres`, `tetrapentagonal growth function`, `[4,5,4,5] generating function`, the exact shell prefix `1,4,10,20,38,70,130,240`, the exact candidate numerator and denominator, the characteristic polynomial, and later/citing work around the papers above. I did not recover a primary source announcing the exact vertex-isoperimetric constant of `r{4,5}` or printing the exact graph-distance rational function below. This is **bounded negative evidence only**, not a priority certificate.

## 4. Idea before code and the three new methods

The idea was committed before the new checker as

`artifacts/R06/20260920T0322Z_i0056_dual_admissibility_idea_79_a47c.md`

at commit `d8402c5f4f395fb61136eba555faf0915460d203`.

### #21 — ASK WHO ELSE HAS THIS SHAPE

The missing statement is a distance-frontier geometry theorem. The nonpositive-corner-curvature literature has exactly such a theorem, but on **face-distance balls of a dual tessellation**.

### #23 — DO WHAT THE PROPOSER DID NOT EXPECT

Instead of attacking vertex isoperimetry or the recurrence directly, pass to the dual quadrangulation and prove that its admissible face balls force the finite frontier state space for all radii.

### #20 — FIND WHY THE ALGORITHM FAILS

Once the recurrence becomes unconditional, inspect the asymptotic ball ratio. It turns out the metric-ball sequence tends to a ratio strictly **above** the current radius-16 witness. Thus simply making the BFS radius larger is asymptotically incapable of closing the isoperimetric gap.

## 5. Dualization to a nonpositively curved quadrangulation

Let

\[
G:=T^*.
\]

Because every vertex of `T` has degree four, every face of `G` is a quadrilateral. Because the faces of `T` have sizes four and five, every vertex of `G` has degree four or five. Around every quadrilateral face the dual vertex degrees alternate `4,5,4,5`.

For a corner `(x,f)` of `G`, the Baues–Peyerimhoff corner curvature is

\[
\kappa(x,f)=\frac1{\deg_G x}+\frac1{|\partial f|}-\frac12.
\]

Since `|partial f|=4`,

\[
\kappa(x,f)=
\begin{cases}
0,&\deg_Gx=4,\\[2mm]
-\frac1{20},&\deg_Gx=5.
\end{cases}
\tag{5.1}
\]

Hence every corner has nonpositive curvature.

Fix a root `o` of `T` and let `f_o` be the corresponding dual face. Faces of `G` are vertices of `T`, and two dual faces share an edge iff the corresponding vertices of `T` are adjacent. Therefore

\[
d_T(o,v)=d_F(f_o,f_v),
\tag{5.2}
\]

where `d_F` is face-adjacency distance in `G`.

Put

\[
P_n:=B_n(f_o)=\{f:d_F(f_o,f)\le n\}.
\]

By the published admissibility theorem quoted above, every `P_n` is an admissible polygon. If `f` belongs to the new face sphere `A_n`, then

\[
\partial f\cap\partial P_{n-1}
\]

is a connected path of one or two edges, while

\[
\partial f\cap\partial P_n
\]

is a nonempty connected path. Under (5.2), these are precisely the arrival and departure edges of the corresponding vertex of `T`. In particular, every non-root vertex of `T` has one or two arrival edges, globally and at every radius.

## 6. A complete local distance-profile lemma

We now prove the all-radius face profiles used only experimentally in the predecessor.

### Lemma 6.1

Let `x` be any vertex of `G`, of degree `p in {4,5}`. Enumerate the incident dual faces cyclically as

\[
f_0,f_1,\ldots,f_{p-1}
\]

and set

\[
d_i=d_F(f_o,f_i).
\]

After subtracting `m=min_i d_i`, and up to cyclic rotation and reversal, the distance vector is exactly one of

\[
(0,0,1,1),\qquad (0,1,2,1)
\tag{6.1}
\]

when `p=4`, and exactly one of

\[
(0,0,1,2,1),\qquad (0,1,2,2,1)
\tag{6.2}
\]

when `p=5`.

### Proof

**Step 1: adjacent differences.** Consecutive incident faces share an edge, hence

\[
|d_{i+1}-d_i|\le1.
\tag{6.3}
\]

**Step 2: sublevel sets are cyclic intervals.** For any integer `k`, the faces among `f_i` with `d_i<=k` are precisely the local sector of the polygon `P_k` at `x`. Since `P_k` is a topological closed disk with a simple boundary cycle, that local sector is empty, all incident faces, or one connected cyclic interval. In particular, the minimum positions form one cyclic interval.

**Step 3: no level occurs three times.** The published cyclic-sphere theorem says the faces of every face sphere `A_k` have a cyclic ordering in which two faces intersect iff they are consecutive. Three distinct faces incident with the same vertex `x` pairwise intersect. Hence three of them cannot lie in the same sphere whenever that sphere has at least four members.

For the spheres here, `|S_1(T)|=4` and `|S_2(T)|=10` are already exact certified base values. For `k>=3`, the inherited rigorous lower bound in (2.1) applied to the ball `B_{k-1}` gives

\[
|S_k(T)|=|\partial_V B_{k-1}(T)|
\ge \frac{|B_{k-1}(T)|}{\sqrt3+\sqrt5-2}
\ge \frac{15}{\sqrt3+\sqrt5-2}>7,
\]

so in particular `|S_k(T)|>=8`. Thus every exact distance level occurs at most twice around `x`. Level zero globally contains only the root face and also satisfies the claim.

**Step 4: finite hand classification.** Subtract the minimum.

For `p=4`, if the minimum occurs twice, Step 2 makes the minima adjacent. Their two outside neighbours must both equal `1` by (6.3), giving `(0,0,1,1)`. If the minimum occurs once, its two neighbours are `1`; level `1` has then already occurred twice, so the remaining entry is `2`, giving `(0,1,2,1)`.

For `p=5`, if the minimum occurs twice, it occurs in an adjacent pair; the two vertices adjacent to that pair are `1`, and the last value must be `2`, giving `(0,0,1,2,1)`. If the minimum occurs once, its two neighbours are `1`, and the remaining two values must both be `2`, giving `(0,1,2,2,1)`.

This proves (6.1)–(6.2). `square`

The exact checker independently exhausts all cyclic integer profiles satisfying the three abstract conditions and obtains exactly the same four canonical profiles.

## 7. The previously missing frontier-anatomy lemma is now proved

For a vertex `v in S_n(T)`, classify its four incident edges as

- `A`: arrival to `S_{n-1}`;
- `F`: fraternal to `S_n`;
- `D`: departure to `S_{n+1}`.

From Section 5, the `A` edges form one connected path around the dual quadrilateral `f_v` and there are one or two of them. The `D` edges form a nonempty connected path.

We need to exclude the only two extra cyclic patterns compatible with those coarse facts:

\[
AADF\quad\text{and}\quad AFDF.
\tag{7.1}
\]

The profile lemma turns this into a boundary-label argument.

In `G` every face is a quadrilateral, so the minimum incident face size at every dual vertex is `N(x)=4`. Consequently a boundary vertex of `P_{n-1}` is `a+` exactly when its inner degree is one; any boundary vertex with inner degree at least two is a `b` vertex.

Consider a corner of `f_v`.

- At an `A-F` corner the consecutive local face levels are `(n-1,n,n)`. Inspection of (6.1)–(6.2) shows that the inner degree of this boundary vertex in `P_{n-1}` is `2` when its degree is four and `3` when its degree is five. Hence it is `b`.
- At an `A-A` corner the consecutive local levels are `(n-1,n,n-1)`. The same profiles show inner degree `3` in degree four and `4` in degree five. Hence it too is `b`.

Now `P_{n-1}` is admissible, so a `b` boundary vertex must have both boundary neighbours labelled `a+`. In particular, two consecutive boundary vertices cannot both be `b`.

If pattern `AADF` occurred, the two-edge arrival path would contain an `A-A` boundary corner and, on its adjacent arrival edge, an `A-F` boundary corner. They would be consecutive `b` vertices, impossible.

If pattern `AFDF` occurred, the unique arrival edge would have an `A-F` corner at each endpoint, again producing consecutive `b` vertices, impossible.

Therefore the only possible non-root frontier types are exactly

\[
\boxed{
A=(1,0,3),\qquad B=(1,1,2),\qquad C=(2,0,2).
}
\tag{7.2}
\]

This proves the first part of the predecessor's `FAL(4,5,4,5)` for **all** radii.

## 8. The square/pentagon start-close profiles are also global

A vertex of `G` corresponds to a face of `T`. Lemma 6.1 translates immediately into the four possible root-distance profiles around faces of `T`:

### Squares

\[
(m,m,m+1,m+1),
\tag{8.1}
\]

a square starting on a fraternal edge at level `m` and ending on the opposite fraternal edge at level `m+1`; or

\[
(m,m+1,m+2,m+1),
\tag{8.2}
\]

a square starting at a unique vertex in level `m` and closing at a unique vertex in level `m+2`.

### Pentagons

\[
(m,m,m+1,m+2,m+1),
\tag{8.3}
\]

a pentagon starting on a fraternal edge in level `m` and closing at a unique vertex in level `m+2`; or

\[
(m,m+1,m+2,m+2,m+1),
\tag{8.4}
\]

a pentagon starting at a unique vertex in level `m` and closing on a fraternal edge in level `m+2`.

Thus there is no hidden fifth face-position state. Combined with (7.2), this proves the entire all-radius statement called `FAL(4,5,4,5)` in the predecessor.

The correct status change is therefore

\[
\boxed{\texttt{FAL(4,5,4,5): CONDITIONAL -> PROVED}.}
\tag{8.5}
\]

## 9. Full recurrence proof, now unconditional

Let `A_n,B_n,C_n` count the three vertex types (7.2) in sphere `S_n`.

Every fraternal edge has two `B` endpoints. Distinguish fraternal edges as follows:

- `X_n`: the pentagon incident to the edge closes inward there while the square starts outward there;
- `Y_n`: the square closes inward there while the pentagon starts outward there.

Then

\[
B_n=2(X_n+Y_n).
\tag{9.1}
\]

The four global face profiles (8.1)–(8.4) give

\[
Y_{n+1}=X_n,
\tag{9.2}
\]

because a square started on an `X_n` fraternal edge closes on a `Y_{n+1}` edge, and

\[
C^5_{n+2}=Y_n,
\tag{9.3}
\]

where `C^5` counts `C` vertices at which a pentagon closes.

Let `Q_n` and `P_n` count squares and pentagons, respectively, that start at a **vertex** in generation `n`. Inspecting the three vertex types gives

\[
Q_n=A_n+2Y_n+C_n^4,
\tag{9.4}
\]

\[
P_n=A_n+2X_n+C_n^5.
\tag{9.5}
\]

Indeed, an `A` vertex starts one square and one pentagon; the two endpoints of a `Y` edge each start a square at their opposite `D-D` corner; the two endpoints of an `X` edge each start a pentagon; and a `C` vertex starts the same face type opposite the face it closes.

By (8.2) and (8.4),

\[
C^4_{n+2}=Q_n,
\qquad
X_{n+2}=P_n.
\tag{9.6}
\]

From (9.2)–(9.6),

\[
Y_n=X_{n-1},\qquad C_n^5=X_{n-3},
\tag{9.7}
\]

and hence

\[
A_n=X_{n+2}-2X_n-X_{n-3}.
\tag{9.8}
\]

Also, since `C_n=C_n^4+C_n^5`,

\[
C_{n+2}=A_n+C_n+3X_{n-1}-X_{n-3}.
\tag{9.9}
\]

Finally count edges between consecutive spheres in the two directions. Departures from `S_n` equal arrivals into `S_{n+1}`:

\[
3A_n+2B_n+2C_n
=A_{n+1}+B_{n+1}+2C_{n+1}.
\tag{9.10}
\]

Substitute (9.1), (9.7), (9.8) and (9.9) into (9.10) and cancel. The resulting scalar residual is constant in `n`:

\[
R_{m+1}=R_m,
\tag{9.11}
\]

where

\[
R_m:=X_m-X_{m-1}-2X_{m-2}+2X_{m-3}-2X_{m-4}-X_{m-5}+X_{m-6}.
\tag{9.12}
\]

The finite base layers give one admissible index with `R_m=0`, so (9.11) forces `R_m=0` for every later index. Therefore `X_n` obeys the order-six homogeneous recurrence. Equations (9.1), (9.7), (9.8) and (9.9) transfer the same recurrence to `A_n,B_n,C_n` after the finite initial layers. Since

\[
S_n=A_n+B_n+C_n,
\]

the shell sequence satisfies, for every `n>=7`,

\[
\boxed{
S_n=S_{n-1}+2S_{n-2}-2S_{n-3}+2S_{n-4}+S_{n-5}-S_{n-6}.
}
\tag{9.13}
\]

The certified initial values are

\[
S_0,\ldots,S_6=1,4,10,20,38,70,130.
\tag{9.14}
\]

Multiplying `V(z)=sum_{n>=0}S_n z^n` by the recurrence denominator and using (9.14) yields

\[
\boxed{
V(z)=
\frac{1+3z+4z^2+4z^3+4z^4+3z^5+z^6}
{1-z-2z^2+2z^3-2z^4-z^5+z^6}.
}
\tag{9.15}
\]

This was **conditional** in the predecessor and is now **unconditional**.

## 10. Method #20: exact explanation of why larger metric balls do not close the gap

The characteristic polynomial is

\[
p(\lambda)=\lambda^6-\lambda^5-2\lambda^4+2\lambda^3-2\lambda^2-\lambda+1.
\tag{10.1}
\]

It is reciprocal. Dividing by `lambda^3` and writing

\[
x=\lambda+\lambda^{-1}
\]

gives

\[
\frac{p(\lambda)}{\lambda^3}=h(x),
\qquad
h(x)=x^3-x^2-5x+4.
\tag{10.2}
\]

For `x>2`,

\[
h'(x)=3x^2-2x-5>0,
\]

while `h(2)=-2` and `h(3)=7`. Hence there is exactly one `x_*>2`, and therefore exactly one positive characteristic root `lambda_*>1`. The other real `x`-root below `-2` has smaller absolute value than `x_*` (indeed `h(-x_*)=8-2x_*^2<0` while `h(-2)=2`), and the third `x`-root lies in `(-2,2)`. Thus `lambda_*` is the unique dominant modulus. The numerator in (9.15) is strictly positive at the positive pole `z=1/lambda_*`, so no cancellation occurs. Consequently

\[
S_n\sim c\lambda_*^n
\qquad(c>0),
\tag{10.3}
\]

and for graph balls

\[
\frac{|\partial_VB_n|}{|B_n|}
=\frac{S_{n+1}}{\sum_{j=0}^n S_j}
\longrightarrow \lambda_*-1.
\tag{10.4}
\]

Now put

\[
U=\frac{113708}{133611},
\qquad c_0=1+U=\frac{247319}{133611}.
\]

The exact checker gives

\[
p(c_0)=
-\frac{28507364992539033994932177242}
{5689227317400174127803170653161}<0,
\tag{10.5}
\]

whereas `p(2)=7>0`. Since `c_0>1`, (10.2) and the monotonicity of `h` on `(2,infinity)` imply

\[
c_0<\lambda_*.
\]

Therefore

\[
\boxed{
\lambda_*-1>\frac{113708}{133611}.
}
\tag{10.6}
\]

Numerically `lambda_*` is about `1.8511890336`, so the limiting ball ratio is about `0.8511890336`, strictly worse than the current radius-16 witness `0.85103771396...`.

This does **not** prove that radius 16 is the best graph ball at every finite radius. It proves the more useful strategic statement that simply pushing the same ball computation to infinity cannot converge to the unknown isoperimetric constant below the current witness. A new shape, not a larger round ball, is needed to lower the upper bound materially.

## 11. Exact finite self-check

The exact finite core is

`artifacts/R06/20260920T0322Z_i0056_dual_profile_exact_79_a47c.py`

created at commit `dd1eadef6c9330a910a0260e42804c4d9dad1228` and executed in the worker runtime. Its archived output is

`artifacts/R06/20260920T0322Z_i0056_dual_profile_exact_79_a47c.out`

created at commit `269d6c9495d62c02a439088f60441dddb22d9c8a`.

It exhausts the cyclic profiles for `p=4,5` under the three proved abstract constraints, obtaining exactly

```text
p=4 profiles=[(0, 0, 1, 1), (0, 1, 2, 1)]
p=5 profiles=[(0, 0, 1, 2, 1), (0, 1, 2, 2, 1)]
```

It also checks the recurrence against all previously certified shell coefficients through radius 18, verifies the numerator/denominator identity coefficientwise on that certified range, and performs the exact sign calculation (10.5). The output ends with

`ALL_EXACT_CHECKS_PASS`.

This is an R06 **self-check**, not an independent audit.

## 12. What moved and what did not

### Proved this run

1. The dual quadrangulation has nonpositive corner curvature.
2. Published admissible-ball geometry applies to all face-distance layers.
3. The only square/pentagon cyclic distance profiles are (6.1)–(6.2).
4. The forbidden valence-4 frontier patterns `AADF` and `AFDF` contradict admissibility.
5. Hence `FAL(4,5,4,5)` holds at every radius.
6. The shell recurrence (9.13) and rational graph-distance growth series (9.15) are unconditional.
7. Metric-ball boundary ratios converge to a value strictly above the current finite radius-16 upper-bound witness, so blind larger balls are asymptotically the wrong route.

### Not proved

1. `Phi_V(r{4,5})` is still not determined.
2. The source-clause interval (2.1) does not shrink this run.
3. The radius-16 ball is not claimed globally optimal among all graph balls.
4. The full Lyons–Peres Question 6.20 remains **PARTIAL**.
5. The structural theorem has no independent other-task audit yet.

## 13. Next attack

The recurrence has done its job: it removes uncertainty about round metric-ball growth and shows that round balls asymptote to the wrong value. The next run should **not** spend its research budget on a larger ball.

The source-relevant route is now to deform the extremal set away from round balls. Two concrete possibilities are:

1. use the exact finite cone/frontier states to introduce an anisotropic boundary weight and solve the resulting finite-state minimum mean-cycle / transfer-matrix problem, seeking a periodic non-round shape with boundary ratio below `113708/133611`;
2. return to the quadrangulated-dual disk inequality from the earlier run and use the proved admissible boundary-state restrictions to bound the weighted boundary deficits `10 Delta_4+8 Delta_5` sharply, rather than independently bounding the two boundary orbits.

Either route attacks the isoperimetric optimization itself rather than the now-settled shell enumeration.

## 14. Model / scheduler truth

The operative implementation record still exposes task identity/title, prompt, schedule/timing and enabled-state controls, but **no binding model-family selector, no binding reasoning-effort selector, no guaranteed hour-long execution control, and no authenticated applied-model/effort receipt**. Thus GPT-6/maximum remains a prompt request on this surface. This report states the actual model as GPT-5.6 Sol and the reasoning level as UNVERIFIED.

The historical P26 response `You cannot modify this task` remains an authorization-context boundary in the implementation record. The compliant workaround is the owning/authorized product/admin/API context or a platform permission/schema change; it is not a worker-side bypass. No scheduler or permission mutation was attempted.

## 15. Structured ledger delta

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
    status: "PROVED subclass / full source PARTIAL"

  source_clause_target:
    graph: "T=r{4,5}=M({4,5})"
    class: "4-regular vertex-transitive plane graph; face type [4,5,4,5]"
    normalization: "outer vertex boundary |partial_V K|/|K|"
    lower_bound: "1/(sqrt(3)+sqrt(5)-2)"
    upper_before: "113708/133611"
    upper_after: "113708/133611"
    interval_width_before: 0.34293830065971065
    interval_width_after: 0.34293830065971065
    status: "PROVED PARTIAL / interval unchanged"

  structural_progress:
    frontier_anatomy_before: "CONDITIONAL"
    frontier_anatomy_after: "PROVED"
    all_generation_recurrence_before: "CONDITIONAL"
    all_generation_recurrence_after: "PROVED"
    recurrence: "S_n=S_{n-1}+2S_{n-2}-2S_{n-3}+2S_{n-4}+S_{n-5}-S_{n-6}, n>=7"
    growth_series: "(1+3z+4z^2+4z^3+4z^4+3z^5+z^6)/(1-z-2z^2+2z^3-2z^4-z^5+z^6)"
    ball_route: "asymptotic ball ratio lambda_*-1 is strictly larger than 113708/133611"

  tried_moves: [21, 20, 23]
  remaining_obligation: "optimize non-round finite sets / weighted dual boundary states to determine Phi_V(r{4,5}); full Question 6.20 remains open"

  evidence:
    prior_report: "runs/R06/20260920T0220Z_i0056_face_state_reduction_78_6e2b.md"
    idea_before_code: "artifacts/R06/20260920T0322Z_i0056_dual_admissibility_idea_79_a47c.md"
    idea_commit: "d8402c5f4f395fb61136eba555faf0915460d203"
    checker: "artifacts/R06/20260920T0322Z_i0056_dual_profile_exact_79_a47c.py"
    checker_commit: "dd1eadef6c9330a910a0260e42804c4d9dad1228"
    checker_output: "artifacts/R06/20260920T0322Z_i0056_dual_profile_exact_79_a47c.out"
    output_commit: "269d6c9495d62c02a439088f60441dddb22d9c8a"
    checker_verdict: "ALL_EXACT_CHECKS_PASS"
    prior_art_exclusion: "Haslegrave-Panagiotis DOI 10.1002/rsa.20946; triangular/quadrangular regular cases only"
    global_layer_input:
      - "Baues-Peyerimhoff, Adv. Geom. 6 (2006), DOI 10.1515/ADVGEOM.2006.014"
      - "Klassert-Lenz-Peyerimhoff-Stollmann, Proc. AMS 134 (2006), DOI 10.1090/S0002-9939-05-08103-7"
    growth_prior_art:
      - "de Souza-da Silva, Ars Combinatoria 160 (2024), DOI 10.61091/ars-160-14"
      - "Graves-Pisanski-Watkins, SIAM J. Discrete Math. 23 (2008), DOI 10.1137/070707026"

  audits:
    this_run: "none; R06 proof plus exact self-check only"
    closure_gate: "not applicable yet; source constant not determined"
```

Model: GPT-5.6 Sol. Reasoning: UNVERIFIED by runtime metadata; GPT-6 maximum was requested, but no model/reasoning selector is exposed, so I do not claim GPT-6 maximum. **NO MOVEMENT: frozen H_{5,5} interval width 0 -> 0. Methods tried: #18 SAY IT IN ANOTHER LANGUAGE, #19 MAKE IT AN ALGORITHM, #30 DO ONE SCALE / ONE DIRECTION AT A TIME.**
Problem/source: Russell Lyons and Yuval Peres, *Probability on Trees and Networks* (2016; current online paperback edition), Question 6.20; intake I0056.

# R06 immutable recovery report — I0056 / tetrapentagonal medial attack

Run ID: `20260916T1820Z_i0056_medial_tetrapentagonal_01`
Repository: `yspennstate/math-open-problems`, branch `master`.
Overall source status: **PARTIAL**.

The frozen regular/co-regular target remains exactly solved mathematically:
\[
\Phi_V(H_{5,5})=\sqrt5,\qquad [L,U]=[\sqrt5,\sqrt5],\qquad U-L=0.
\]
Haslegrave--Panagiotis already own the triangular/quadrangular cases; no such case is relabelled as R06 novelty. The regular/co-regular `f>=5` result remains audit-gated, with R05 PASS and P26 still absent in the repository search at run start.

This run follows the recovery selected in the preceding stuck report. It does **not** manufacture another general lemma around the zero metric. It attacks the simplest source-valid mixed-face transitive graph isolated there.

## 1. Required continuity / repository read

Before new mathematics I recovered and read/queried:
- `probability_campaign_2026_09/INDEX.md`, `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, `QUEUE.md`;
- `operations/FLEET_2026-09-16.md`, `operations/RFLEET_2026-09-16.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md` and `DEPLOYMENT.md`;
- canonical ownership `operations/claims/I0056.md`;
- targeted I0056 intake rows in `probability_1000_intake_I_20260914/problems.jsonl` and its mirrored copy;
- newest own report `runs/R06/20260916T172145Z_i0056_stuck_recovery_01.md`;
- newest R07 package `runs/R07/20260916T1724Z_i0077_cusp_power_shape_01.md`;
- the existing R05 audit `R05-AUDIT-R06-I0056-CLOSURE-01-COR-F5-20260916T151529Z`.

The full intake family cannot be rendered in one connector response without truncation, so the intake reread is recorded honestly as targeted to I0056 rather than as a fictitious manual read of every row.

The exact source question remains:

> **Question 6.20.** What is `Phi_V(G)` for regular, co-regular plane graphs `G`? What are `Phi_E(G)` and `Phi_V(G)` for more general transitive, plane graphs `G`?

The normalization remains
\[
\Phi_V(G)=\inf_{\varnothing\ne K\subset V(G),\ |K|<\infty}
\frac{|\partial_VK|}{|K|},
\qquad
\Phi_E(G)=\inf_{\varnothing\ne K\subset V(G),\ |K|<\infty}
\frac{|\partial_EK|}{|K|},
\]
with `partial_V K` the **outer** vertex boundary and `partial_E K` the crossing-edge boundary.

## 2. Current source/literature check — 2026-09-16

Queries included:
- `"Question 6.20" "Probability on Trees and Networks" "Phi_V"`;
- `"Site percolation and isoperimetric inequalities for plane graphs" Haslegrave Panagiotis`;
- `"Sharp isoperimetric inequalities for infinite plane graphs" Oh`;
- `"4.5.4.5" Cheeger constant hyperbolic tiling`;
- `"tetrapentagonal" isoperimetric`;
- `"medial graph" Cheeger constant hyperbolic tiling`;
- `"Hyperbolic Pascal triangle" "{4,5}" ascendants descendants`;
- later/citing searches for semiregular/uniform hyperbolic tilings and exact isoperimetric constants.

The current Lyons--Peres online book still prints Question 6.20 and records Haslegrave--Panagiotis for codegrees 3 and 4 and Oh for Question 6.21. Haslegrave--Panagiotis explicitly say their exact vertex results answer Q6.20 for triangular and quadrangular regular hyperbolic lattices. Oh gives sharp **edge** constants under vertex/face degree bounds, not an exact mixed-face outer-vertex constant.

Datta--Gupta's semi-regular tiling work explicitly exhibits the unique vertex type `[4,5,4,5]`. A bounded current search found no exact `Phi_E/Phi_V` formula for this tetrapentagonal graph. This is **not proof of literature absence**. Novelty remains **UNVERIFIED**.

Primary/current references used in this run:
- Lyons--Peres current online paperback: https://rdlyons.pages.iu.edu/prbtree/book_pb.pdf
- Haslegrave--Panagiotis, DOI `10.1002/rsa.20946`
- Byung-Geun Oh, arXiv `2009.04394`
- Datta--Gupta, arXiv `1806.11393`
- Németh--Szalay, arXiv `1701.07074` / Annales Math. Inform. 46 (2016), 165--173.

## 3. Recovery graph and method #18 — SAY IT IN ANOTHER LANGUAGE

Let
\[
R:=H_{5,4},
\]
the degree-5 regular quadrangulation, i.e. the Schlaefli mosaic `{4,5}`. Let
\[
T:=M(R)
\]
be its medial graph. Then `T` is the vertex-transitive tetrapentagonal tiling `r{4,5}`, with cyclic face type `[4,5,4,5]`, and is 4-regular.

A vertex of `T` is an edge of `R`. A `T`-edge is a **corner** of `R`, joining two consecutive `R`-edges around a primal vertex/equivalently around a quadrangular face.

Therefore a finite vertex set
\[
S\subset V(T)
\]
is exactly a finite edge set
\[
S\subset E(R).
\]

For a primal vertex `v` or primal face `f`, write `t_v(S)` / `t_f(S)` for the number of 0--1 transitions in the cyclic word recording which incident `R`-edges belong to `S`. Then every medial boundary edge is one corner, hence exactly:
\[
\boxed{
|\partial_E^T S|
=\sum_{v\in V(R)}t_v(S)
=\sum_{f\in F(R)}t_f(S).
}
\tag{R06-I0056-MEDIAL-01}
\]

This is the useful language change: the mixed-face Cheeger problem becomes a cyclic binary-state optimization on the regular quadrangulation `R` and its regular dual.

## 4. A universal preliminary lower bound: enough to make closure finite

Put
\[
B:=|\partial_E^T S|,\qquad n:=|S|.
\]

Call an `R`-face **full** if all four boundary edges lie in `S`, **empty** if none do, and **partial** otherwise. Let `F` be the number of full faces and `Q` the number of partial faces.

For a partial 4-cycle with `l` selected edges and `t` cyclic transitions,
\[
l\le \frac32 t.
\tag{4.1}
\]
Also every partial face has at least two transitions, so
\[
Q\le B/2.
\tag{4.2}
\]

The dual graph `R^*=H_{4,5}` has exact outer vertex Cheeger constant
\[
h_* = \frac{2}{\sqrt3}.
\]
This is the already established R06 `f>=5` consequence of Oh's exact edge formula plus `R06-I0056-CLOSURE-01`.

Every dual neighbor of a full face which is not full is necessarily partial: the shared `R`-edge is selected because it lies on the full face. Therefore
\[
\partial_V^{R^*}(\text{full faces})\subseteq\{\text{partial faces}\},
\]
so
\[
F\le \frac{Q}{h_*}\le \frac{B}{2h_*}.
\tag{4.3}
\]

Double-count selected edge/face incidences:
\[
2n
=4F+\sum_{f\text{ partial}} l_f
\le \frac{2B}{h_*}+\frac32B.
\]
Consequently every finite nonempty `S` satisfies
\[
\boxed{
\frac{|\partial_E^T S|}{|S|}
\ge
c_0:=
\frac{2}{\sqrt3+3/2}
=
-4+\frac{8\sqrt3}{3}
>0.
}
\tag{R06-I0056-MEDIAL-02}
\]

This preliminary bound is not claimed sharp. Its role is to make the next closure algorithm provably finite.

## 5. Method #19 — MAKE IT AN ALGORITHM: multiplicity-two medial closure

Starting from finite nonempty `S_0\subset V(T)`, repeatedly adjoin an outside `T`-vertex having at least two neighbors in the current set.

Because `T` is 4-regular, if the added vertex has `r>=2` neighbors in the set, the edge boundary changes exactly by
\[
\Delta B=4-2r\le0.
\tag{5.1}
\]
If the algorithm made infinitely many additions, its cardinality would tend to infinity while its edge boundary stayed bounded by `B(S_0)`, contradicting the positive universal bound in (R06-I0056-MEDIAL-02). Thus it terminates after finitely many additions at a set `S'`.

At termination, every outside `T`-vertex has at most one selected `T`-neighbor.

Translate this to each quadrangular face of `R`. A partial selected pattern with three selected edges would leave the single missing edge adjacent in the medial 4-cycle to two selected edges. The opposite-pair pattern `1010` has the same defect. Hence every partial face of `R` has either:
- one selected edge, or
- two **adjacent** selected edges.

In either case it has exactly two transitions. Thus, for terminal `S'`,
\[
B'=2Q'.
\tag{5.2}
\]
The full-face dual-boundary argument now gives
\[
F'\le \frac{Q'}{h_*}=\frac{B'}{2h_*}.
\]
And now the selected edge/face incidence count sharpens to
\[
2|S'|
=4F'+\sum_{f\text{ partial}}l_f
\le \frac{2B'}{h_*}+B'
=(\sqrt3+1)B'.
\]
Therefore
\[
\frac{B'}{|S'|}\ge \frac2{1+\sqrt3}=\sqrt3-1.
\]
Since the closure only enlarges the set and never increases edge boundary,
\[
B(S_0)\ge B(S')\ge(\sqrt3-1)|S'|\ge(\sqrt3-1)|S_0|.
\]
Thus:
\[
\boxed{
\Phi_E(T)\ge \sqrt3-1.
}
\tag{R06-I0056-MEDIAL-LOWER-01}
\]

This is a rigorous source-valid lower bound for the concrete mixed-face transitive graph selected by the previous stuck report.

## 6. A source-relevant vertex lower bound

The closure threshold `d-3=1` is not available because the edge lower bound above is below 1. Nevertheless the same closure gives a nontrivial outer-vertex bound.

Let the original finite set have size `n`, outer vertex boundary `b_0`, edge boundary `e_0`; suppose `m` vertices are added and the terminal set has edge boundary `e_m`.

Each closure addition in a 4-regular graph changes outer vertex boundary by at most `+1`, so
\[
b_0\ge b_m-m=e_m-m.
\]
Using `h:=sqrt(3)-1` from the edge theorem,
\[
b_0\ge h(n+m)-m=hn-(1-h)m.
\tag{6.1}
\]
Also `e_0<=4b_0`, while `e_m<=e_0`; therefore
\[
b_0\ge e_0/4\ge e_m/4\ge \frac h4(n+m).
\tag{6.2}
\]
Minimizing the maximum of (6.1) and (6.2) over `m/n>=0` gives
\[
\boxed{
\Phi_V(T)
\ge
\frac{h}{4-3h}
=
\frac{1+2\sqrt3}{11}
\approx0.4058274196.
}
\tag{R06-I0056-MEDIAL-VLOWER-01}
\]

## 7. Method #30 — ONE SCALE / ONE DIRECTION: exact ball construction in the regular base graph

The previous stuck report isolated the milestone
\[
\Phi_E(T)\ge1\ ?.
\tag{BLOCK-R06-2}
\]
This run attacks it by an exact asymptotic construction.

Let `B_n` be the graph-distance ball in
\[
R=H_{5,4}=\{4,5\},
\]
let
\[
L_n=B_n\setminus B_{n-1},
\qquad
V_n=|B_n|,
\]
and let
\[
S_n:=E_R(B_n)
\]
be all `R`-edges with both endpoints in `B_n`, viewed as a vertex set in `T=M(R)`.

Haslegrave--Panagiotis Theorem 23 proves that balls witness the exact vertex Cheeger constant of the degree-5 quadrangulation, namely the golden ratio
\[
\varphi=\frac{1+\sqrt5}{2}.
\]
Thus
\[
\frac{|L_{n+1}|}{V_n}
=
\frac{|\partial_V^R B_n|}{|B_n|}
\longrightarrow\varphi.
\tag{7.1}
\]
Therefore
\[
\frac{V_{n+1}}{V_n}\to1+\varphi=\varphi^2,
\qquad
\frac{|L_n|}{V_n}\to\frac1\varphi,
\qquad
\frac{|L_{n+1}|}{|L_n|}\to\varphi^2.
\tag{7.2}
\]

The regular `{4,5}` mosaic is bipartite, so every edge joins adjacent distance layers. Let `a_n` be the number of edges between `L_{n-1}` and `L_n`. Degree 5 gives
\[
5|L_n|=a_n+a_{n+1}.
\tag{7.3}
\]
Put `x_n=a_n/|L_n|`. Then
\[
x_{n+1}
=
\frac{5-x_n}{|L_{n+1}|/|L_n|}.
\]
Since the denominator tends to `phi^2>1`, this nonautonomous affine recurrence is eventually contractive, and
\[
x_n\to\frac5{1+\varphi^2}
=\frac{5-\sqrt5}2.
\tag{7.4}
\]
Combining (7.1) and (7.4),
\[
\frac{a_{n+1}}{V_n}\to\sqrt5.
\tag{7.5}
\]
The degree count on `B_n` gives
\[
5V_n=2|S_n|+a_{n+1},
\]
so
\[
\frac{|S_n|}{V_n}
\to\frac{5-\sqrt5}2.
\tag{7.6}
\]

It remains to compute the medial edge boundary of `S_n`. Németh--Szalay's exact `{4,5}` sphere structure identifies every sphere vertex (apart from the sector wingers) as:
- Type A: two ascendants and three descendants;
- Type B: one ascendant and four descendants;
with the two ascendant edges at a Type-A vertex neighboring/consecutive in the cyclic order. Wingers have one ascendant. Their rows are graph-distance rows.

At `v\in L_n`, the selected incident `R`-edges of `S_n` are exactly these one or two predecessor edges. They form one nonempty proper cyclic interval, hence contribute exactly two transitions around `v`. Vertices in `B_{n-1}` have all incident edges selected and vertices outside `B_n` have none. By the medial boundary identity,
\[
\boxed{
|\partial_E^T S_n|=2|L_n|.
}
\tag{7.7}
\]

Using (7.2), (7.6), (7.7),
\[
\frac{|\partial_E^T S_n|}{|S_n|}
\longrightarrow
\frac{2/\varphi}{(5-\sqrt5)/2}
=
\frac2{\sqrt5}
<1.
\]
Thus:
\[
\boxed{
\Phi_E(T)\le\frac2{\sqrt5}<1.
}
\tag{R06-I0056-MEDIAL-UPPER-01}
\]

Therefore the previous recovery milestone is **DISPROVED**:
\[
\boxed{
\text{`BLOCK-R06-2: }\Phi_E(T)\ge1\text{' is false.}
}
\]
This is **not** a refutation of Lyons--Peres Question 6.20; it only kills the proposed threshold route.

Combining Sections 5 and 7:
\[
\boxed{
\sqrt3-1
\le
\Phi_E(T)
\le
\frac2{\sqrt5}.
}
\tag{7.8}
\]
The certified edge-interval width is
\[
1+\frac2{\sqrt5}-\sqrt3
\approx0.1623763834.
\]
This is a **secondary diagnostic**, not a replacement for the frozen H_{5,5} metric.

For the source's outer vertex constant,
\[
\boxed{
\frac{1+2\sqrt3}{11}
\le
\Phi_V(T)
\le
\frac2{\sqrt5}.
}
\tag{7.9}
\]
The upper bound uses the pointwise fact `|partial_V K|<=|partial_E K|`.

## 8. What the three methods taught us

### #18 SAY IT IN ANOTHER LANGUAGE
**Succeeded.** Medialization turns the mixed `[4,5,4,5]` graph into edge subsets of a regular quadrangulation and produces the exact transition identity (MEDIAL-01).

### #19 MAKE IT AN ALGORITHM
**Succeeded partially.** Multiplicity-two closure plus the regular dual's known vertex expansion yields the rigorous edge lower `sqrt(3)-1` and a vertex lower `(1+2sqrt(3))/11`. It does not determine the exact constant.

### #30 DO ONE SCALE / ONE DIRECTION AT A TIME
**Succeeded in refuting the first milestone.** Regular-base graph-distance balls yield a certified family with medial edge ratio tending to `2/sqrt(5)<1`. Hence the old `Phi_E(T)>=1` plan cannot activate `CLOSURE-01`.

The remaining obligation for this mixed source graph is now genuinely narrower:
\[
\boxed{
\text{close the interval }
\sqrt3-1\le\Phi_E(T)\le2/\sqrt5
\text{ and then determine }\Phi_V(T).
}
\]
No exact-value conjecture is promoted to theorem.

## 9. Exact validation performed only after the ideas were proved on paper

After the derivations above were complete, I ran an exact symbolic/local-state checker. It verifies:
- all partial 4-cycle states satisfy `2l<=3t`;
- all terminal partial 4-cycle states have `t=2,l<=2`;
- all terminal partial 5-cycle states have `t=2,l<=3`;
- exact surd simplifications for `h_*`, `c_0`, `sqrt(3)-1`, `(1+2sqrt(3))/11`, and `2/sqrt(5)`;
- the golden-ratio recurrence-limit algebra;
- `2/sqrt(5)<1`.

Checker output SHA-256:
`2405cb693652be12e57e75e92fe226c300f8b39771aa6cd7679406e2c874ee26`.

The checker is a self-check of finite algebra/local patterns only; it is not an independent audit and does not substitute for the written geometric proof.

## 10. Independent audit of the newest R07 package

Newest package:
`runs/R07/20260916T1724Z_i0077_cusp_power_shape_01.md`.

I independently audited **Lemma `I0077-R07-L2`**, conditional on its preceding positive-tube Lemma L1.

R07 defines an integer-scan stopping time `T(a,delta,c)` requiring:
1. the reversed Brownian segment at integer `n` to remain in the two-power tube;
2. an endpoint budget `|B_n|<=delta f(n)`.

The proof uses a two-sided Brownian motion and integer re-rooting. The unit Brownian path-increment blocks are iid, hence the integer shift is Bernoulli/ergodic. If the full backward-tube event `A_c` has probability `p_c>0` (L1), Birkhoff gives positive asymptotic frequency, hence infinitely many positive integers `n` with `theta^n W in A_c`. For such `n`, restricting the controlled backward path to `0<=s<=n` gives exactly the one-sided event `G_n(c)`.

Separately, with `beta>1/2` and `f(n)>=n^beta`,
\[
\Pr(|B_n|>\delta f(n))
\le
2\exp[-(\delta^2/2)n^{2\beta-1}],
\]
which is summable. Borel--Cantelli therefore makes the endpoint condition true for all sufficiently large integers almost surely. Intersecting with the infinitely many Birkhoff-good integers proves the stopping time finite a.s. No independence between these two conclusions is needed.

The measurability claim is also sound: continuity reduces the universal-in-`s` tube check on a compact interval to rational `s`.

Audit verdict:
`R06-AUDIT-R07-I0077-L2-20260916T1820Z: PASS_SCOPED`.

Scope: this verifies L2 **conditional on L1**. It is not a full audit of R07's main theorem or of L1.

## 11. Model / scheduler control status

The limitation remains unchanged and is now explicitly confirmed by the current operations manifest and the exposed tool schema.

Available task controls expose title, prompt, schedule, enabled state and timing mode. They expose **no model-family selector and no reasoning-effort selector**. Consequently the installed text `GPT-6 / maximum` is a request only; it cannot certify runtime configuration. This run identifies as GPT-5.6 Sol and exposes no authenticated reasoning-effort value.

To change this reliably, the scheduler/product API would need to expose model and reasoning fields, or an authorized owner/admin/platform control in the task's owning context would have to set them once such controls exist. Prompt text is not such a control.

The repository's current deployment record also distinguishes historical permission failures from later authorized contexts: one context recorded P26/R-series modification denials, while another P/C context later succeeded updating P26. There is no permitted workaround by duplicating a protected task. The valid workaround is modification from an authorized owning context or platform support. No scheduler/task mutation was attempted in this research run.

## 12. Audit gate and closure state

For the existing regular/co-regular result:
- R05: `R05-AUDIT-R06-I0056-CLOSURE-01-COR-F5-20260916T151529Z: PASS_MATH_SCOPE / NOVELTY_UNVERIFIED`;
- P26: **PENDING** by fresh repository search.

Therefore no paper folder and no CLOSED source label are created.

The new mixed-face interval bounds have only this R06 self-check and no OTHER-track audit yet. They are **PARTIAL** progress inside the second clause of Q6.20.

## 13. Structured ledger_delta

```yaml
ledger_delta:
  track: R06
  source: "Russell Lyons and Yuval Peres, Probability on Trees and Networks, Question 6.20"
  intake: I0056
  target: "outer vertex-isoperimetric constants; frozen H_{5,5} metric retained; source-level recovery on T=r{4,5}"
  frozen_metric:
    quantity: "certified interval width U-L for Phi_V(H_{5,5})"
    before: 0
    after: 0
    movement: "NO MOVEMENT"
  unchanged_count: 4
  status:
    full_source: PARTIAL
    H55: "PROVED, audit-gated"
    regular_coregular_f_ge_5: "PROVED, audit-gated"
    tetrapentagonal_T: PARTIAL
    block_R06_2_PhiE_ge_1: DISPROVED
  tried_moves: [18, 19, 30]
  new_exact_bounds:
    T: "tetrapentagonal r{4,5} = M(H_{5,4}), vertex type [4,5,4,5]"
    edge: "sqrt(3)-1 <= Phi_E(T) <= 2/sqrt(5)"
    vertex: "(1+2sqrt(3))/11 <= Phi_V(T) <= 2/sqrt(5)"
    secondary_edge_width: "1 + 2/sqrt(5) - sqrt(3)"
  remaining_obligation:
    - "close the exact Phi_E(T) interval or prove a different exact mixed-face constant"
    - "determine exact Phi_V(T), without assuming edge=vertex after the threshold route failed"
    - "obtain P26 audit for existing R06-I0056-CLOSURE-01"
    - "independent audit(s) for the new tetrapentagonal bounds before any closure use"
  exact_evidence:
    checker: "artifacts/R06/20260916T1820Z_i0056_medial_tetrapentagonal_01_exact.py"
    output: "artifacts/R06/20260916T1820Z_i0056_medial_tetrapentagonal_01_exact.out"
    output_sha256: "2405cb693652be12e57e75e92fe226c300f8b39771aa6cd7679406e2c874ee26"
  audits:
    R05_existing_closure: "PASS_MATH_SCOPE / NOVELTY_UNVERIFIED"
    P26_existing_closure: PENDING
    R06_to_R07: "R06-AUDIT-R07-I0077-L2-20260916T1820Z: PASS_SCOPED"
```

## 14. Next route if this target continues

The fixed metric is already zero, so another unchanged report must not be justified by renaming this mixed-case interval as the official metric.

If R06 continues I0056 before the six-unchanged closable rotation, the next attack should target **optimality for the tetrapentagonal edge interval**, not another generic closure lemma. The strongest genuinely new directions are:
- #12 FIND WHAT IS CONSERVED: exploit simultaneous primal-vertex and primal-face transition counts at terminal closure;
- #24 FIND THE EXTREMAL OBJECT: test whether closed medial balls or another explicit family realizes the lower envelope;
- #27 SWAP THE QUANTIFIERS: seek one dual potential valid for every terminal local state instead of classifying every finite region individually.

No source-level closure is claimed in this run.

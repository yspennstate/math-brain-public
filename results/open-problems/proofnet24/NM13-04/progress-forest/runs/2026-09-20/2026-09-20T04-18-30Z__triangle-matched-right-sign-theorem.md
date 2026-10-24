Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.**

# NM13-04 / T07 — strict uniform-forest p-NC for `K_3 join (M_k disjoint_union I_r)`

Status: **PARTIAL on the parent Grimmett–Winkler conjecture / CANDIDATE_FULL for the restricted all-parameter theorem below, pending later independent review.** The arbitrary-finite-graph uniform-all-forests conjecture remains OPEN.

Repository / branch: private `yspennstate/math-open-problems` / `master`  
Assigned root: `proofnet24/NM13-04/progress-forest/`  
Companion: NM13-08, `proofnet24/NM13-08/progress-forest-structure/`

## 0. Short handoff and why this run changes method

The immediately preceding NM13-04 run proved a two-terminal deletion/contraction substitution theorem using an activity-2 split-5 atom and transparent theta neutralizers, then applied it to recursively decorated bicliques. That was a separator/substitution mechanism and left the parent all-graph order metric unchanged.

The current owner rule says that after three unchanged substantive parent runs a materially different method must be executed immediately. This run therefore does **not** continue two-terminal transparent substitution. It returns to the surviving P14 obstruction—3-connected graphs—but uses the **new three-terminal matched-layer algebra proved independently by NM13-08 at 03:38Z**, and seeds that algebra with a triangle core. This adds core edges that are not present in NM13-08's `K_{3,2k+r}+M_k` theorem and forces six additional edge-pair orbit types. The result is a genuinely 3-connected all-parameter class.

`POSTED.md` was checked. The T07 parent remains unposted as a closed source problem, and the exact restricted theorem below is not listed as an already-posted claim.

## 1. Parent problem before/after, separately from mechanism gain

For a finite simple graph `G=(V,E)`, let

\[
I_G(\mathbf y)=\sum_{F\subseteq E:\,F\text{ acyclic}}\prod_{e\in F}y_e,
\qquad
\Delta_G(e,f)=I_eI_f-I_GI_{ef}.
\]

At unit weights, `Delta_G(e,f)>=0` is exactly pairwise negative edge correlation for a uniformly sampled acyclic spanning edge subset, with **all component counts mixed**.

**Parent source status:** `OPEN -> OPEN`.  
**Largest completely certified all-simple-graph order in repository continuity:** `9 -> 9`.  
**Equivalent lower bound on the order of a source-valid counterexample:** `>=10 -> >=10`.

No finite order metric moves in this run.

**Mechanism before:** P14's 3-connected reduction; NM13-04 split-3/split-4/split-5 and transparent substitution; NM13-08's five-state matched-right transfer theorem for `K_{3,2k+r}+M_k`.

**Mechanism after:** a complete symbolic 20-orbit sign theorem for

\[
H_{k,r}:=K_3\vee(M_k\sqcup I_r),\qquad k,r\ge0,
\]

where `M_k` is a matching on `2k` right vertices and `I_r` is an independent set of `r` further right vertices. Every right vertex is joined to all three vertices of the left `K_3`, and each matched pair also carries its internal matching edge.

For every `k,r` and every two distinct present edges of `H_{k,r}`, the Rayleigh difference is **strictly positive**. This is an infinite two-parameter theorem, not finite enumeration.

When `2k+r>=1`, `H_{k,r}` is 3-connected: deleting fewer than three vertices leaves at least one triangle vertex, which is adjacent to every surviving right vertex and to every surviving triangle vertex. It contains a `K_4` subgraph as soon as a right vertex exists, so it is not series-parallel. If `2k+r>=3`, it contains `K_{3,3}` and is nonplanar. Thus the theorem directly occupies the structural region left after P14's minimal-counterexample reduction.

## 2. Essential recovered P14 proof history and failed routes

The latest P14 handoff was reread completely. The supported inherited facts needed here are:

1. Grimmett–Winkler published the unit-weight source inequality for all graphs through eight vertices and for nine-vertex graphs with at most 18 edges; repository exact work covers the complementary dense nine-vertex sector, so all simple graphs through nine vertices are covered.
2. Block/direct-sum factorization reduces a vertex-minimal counterexample to 2-connected.
3. The two-separator transfer plus the fixed-graph unit-to-positive-weight implication recorded from Cocks/Semple–Welsh reduces a vertex-minimal source counterexample further to **3-connected**.
4. One-edge-field Rayleigh quadratics are exact and useful, but they do not themselves close the arbitrary 3-connected case.

The failed routes are preserved rather than retried:

* the generic degree-three apex/star-mesh reduction leaves a mixed three-terminal polarization;
* that mixed term is not universally nonnegative;
* the proposed reverse-Cauchy rescue `C^2 <= 4 Delta_A Delta_K` was exactly refuted on a physical six-vertex graph even though the physical Rayleigh gap remained positive;
* Lorentzian/complete-log-concavity, naive real-stability perturbation, and Garding shortcuts lack a verified source-matching hypothesis for arbitrary graphic independence polynomials.

So this run does not claim a universal three-terminal theorem. It proves positivity on a specific 3-connected response algebra where every orbit can be closed exactly.

## 3. Current literature scope check (bounded, 20 September 2026)

The exact source scopes were rechecked rather than conflated:

* Grimmett–Winkler, `arXiv:math/0302185`, study the uniform measure on **all forests** and state the pairwise edge-negative-correlation conjecture; they explicitly distinguish the already-known spanning-tree law. Their published numerical scope is all graphs through 8 vertices and 9-vertex graphs with at most 18 edges.
* Erickson, `arXiv:1008.3660`, proves the stronger all-positive-weight independent-set-Rayleigh property for **series-parallel graphs** by a sum-of-squares formula.
* Huang, `arXiv:2311.00965` / *Statistics & Probability Letters* 213 (2024), treats restricted arboreal-gas parameters/graphs and still describes the general negative-correlation question as open.
* Bado, DOI `10.1016/j.spl.2026.110960`, proves strict uniform-all-forest p-NC for every wheel, another infinite 3-connected non-series-parallel family; the indexed journal issue is 241 (2027), with the DOI assigned in 2026.
* Tang–Zhang, `arXiv:2603.10738`, submitted 11 March 2026, prove p-NC for specified complete-graph spanning-subgraph ensembles including forests with a **fixed number of components** for fixed `k` and sufficiently large `n`. This is not the arbitrary-graph all-component uniform-forest measure.

A bounded search for the exact family `K_3 join (matching + isolates)` with uniform-all-forest edge correlation did not surface a prior theorem. That is negative evidence only: **novelty/priority remains UNVERIFIED**.

## 4. The new graph family and theorem

Let the left terminals be `L={0,1,2}` and include all three triangle edges `01,02,12`. On the right, take `k` disjoint matched pairs and `r` isolated vertices. Join every right vertex to every terminal in `L`. There are no other right-right edges.

Thus

\[
|V(H_{k,r})|=3+2k+r,
\qquad
|E(H_{k,r})|=3+7k+3r.
\]

### Theorem `T07-TRIANGLE-MATCHED-RIGHT-PNC-05`

For every pair `k,r>=0` and every two distinct present edges `e,f` of `H_{k,r}`,

\[
\boxed{\Delta_{H_{k,r}}(e,f)>0.}
\]

Hence the uniform measure on **all forests** of `H_{k,r}` has strict pairwise negative edge correlation.

For `(k,r)=(0,0)` this is the triangle and is immediate. The proof below covers every nontrivial orbit for arbitrary parameters.

## 5. Five-state terminal algebra

Track only the connectivity partition induced on the three fixed triangle terminals. Use the five states

\[
D=0|1|2,\quad P_{12}=0|12,\quad P_{01}=01|2,\quad P_{02}=02|1,\quad T=012.
\]

For one ordinary right vertex joined to all three terminals, exact enumeration of its eight spoke subsets gives

\[
S=\begin{pmatrix}
4&1&1&1&1\\
0&4&0&0&2\\
0&0&4&0&2\\
0&0&0&4&2\\
0&0&0&0&4
\end{pmatrix}.
\tag{5.1}
\]

Put `N=S-4I`. Then

\[
N^3=0,\qquad N^2\ne0.
\tag{5.2}
\]

For one matched pair of right vertices, including its internal matching edge, exact enumeration of the seven local edges gives the NM13-08 transfer

\[
P=\begin{pmatrix}
23&12&12&12&22\\
0&23&0&0&24\\
0&0&23&0&24\\
0&0&0&23&24\\
0&0&0&0&23
\end{pmatrix}
=23I+12N+\frac53N^2.
\tag{5.3}
\]

Therefore every product of unmarked matched and ordinary layers lies in `span{I,N,N^2}`. If `x` unmatched matched-pair layers and `y` ordinary layers remain after the distinguished edges have been exposed, then, after factoring out the positive scalar `23^x4^y`, the remaining transfer is

\[
U(x,y)=I+u(x,y)N+v(x,y)N^2,
\tag{5.4}
\]

where

\[
u(x,y)=\frac{12x}{23}+\frac y4,
\]

\[
v(x,y)=\frac{5x}{69}+\frac{72x(x-1)}{529}
+\frac{y(y-1)}{32}+\frac{3xy}{23}.
\tag{5.5}
\]

The new ingredient relative to NM13-08 is the triangle initial state. Enumerating the seven acyclic subsets of the three core edges gives the row vector

\[
q=(1,1,1,1,3).
\tag{5.6}
\]

For example, the three two-edge paths contribute the final coefficient `3` of state `T`.

Consequently the exact all-forest count is

\[
I_{H_{k,r}}(\mathbf1)
=23^k4^r\left(
\frac{432k^2}{529}+\frac{18kr}{23}+\frac{2558k}{529}
+\frac{3r^2}{16}+\frac{37r}{16}+7
\right),
\tag{5.7}
\]

or equivalently

\[
I_{H_{k,r}}(\mathbf1)=\frac{23^k4^r}{8464}
\left(6912k^2+6624kr+40928k+1587r^2+19573r+59248\right).
\tag{5.8}
\]

The brute-force checks in §8 independently recover (5.7) on small instances.

## 6. Exhaustive 20-orbit reduction

Let `C` denote a triangle-core edge, `O` a spoke to an ordinary right vertex, `h` the internal edge of a matched right pair, and `M` a spoke belonging to a matched pair. The automorphism group contains

\[
S_3\times(S_2\wr S_k)\times S_r.
\]

Every unordered pair of distinct present edges is therefore in exactly one of these twenty templates:

1. `CC`;
2. `CO_inc`, `CO_opp`;
3. `Ch`;
4. `CM_inc`, `CM_opp`;
5. `OO_same`, `OO_diff_same`, `OO_diff_diff`;
6. `Oh`;
7. `OM_same`, `OM_diff`;
8. within one matched layer: `hM`, `MM_sameendpoint`, `MM_opp_sameT`, `MM_opp_diffT`;
9. across two matched layers: `hh_diff`, `hM_diff`, `MM_diff_sameT`, `MM_diff_diffT`.

Here `inc/opp` distinguishes whether the left endpoint of a spoke is incident to the core edge; `same/diff` for spokes in distinct layers distinguishes the left terminal; and in one matched layer `sameendpoint` versus `opp` distinguishes the two matched-right endpoints.

This list is exhaustive because a pair is determined first by its two edge types, then by whether their local right layers coincide, and finally by the only remaining `S_3` invariant: equality/incidence of the terminal labels.

For each orbit, the exact checker constructs from first principles the marked transfer matrix obtained by requiring the relevant local edge(s) to be present. Distinguished layers are then moved next to the initial triangle vector; all remaining layers contribute the common factor `23^x4^y U(x,y)`. Therefore every Rayleigh gap has the form

\[
\Delta_{H_{k,r}}(e,f)
=(23^x4^y)^2 R_{\mathcal O}(x,y),
\tag{6.1}
\]

where `x=k-a`, `y=r-b` are the nonnegative counts of remaining matched and ordinary layers after consuming `a,b` distinguished layers for that orbit.

The exact finite symbolic calculation produces a polynomial `R_O(x,y)` of total degree at most 4. **Every coefficient of every one of the twenty polynomials is strictly positive.** Since `x,y>=0` on every physical orbit, every gap is strictly positive.

To make the certificate inspectable, here are representative formulas from each structural level. The full twenty primitive integer numerators are printed in the archived checker output.

For core-core pairs (`a=b=0`),

\[
R_{CC}(x,y)=\frac{1}{8464}
\left(
2304x^2+2208xy+12064x+529y^2+5819y+16928
\right).
\tag{6.2}
\]

For a core edge and the internal edge of one matched pair (`a=1,b=0`),

\[
R_{Ch}(x,y)=\frac{1}{529}
\left(
6912x^2+6624xy+55120x+1587y^2+26450y+111090
\right).
\tag{6.3}
\]

For two spokes in one ordinary layer (`a=0,b=1`), the quartic numerator is

\[
\begin{aligned}
71639296\,R_{OO\_same}(x,y)=\;&47775744x^4+91570176x^3y+565788672x^3\\
&+65816064x^2y^2+812791296x^2y+2455143424x^2\\
&+21024576xy^3+389208576xy^2+2349707968xy\\
&+4605499392x+2518569y^4+62124702y^3\\
&+562200569y^2+2202908352y+3152129024.
\end{aligned}
\tag{6.4}
\]

For the most local matched-layer spoke configuration, opposite matched endpoints with different terminal labels (`a=1,b=0`),

\[
\begin{aligned}
35819648\,R_{MM\_opp\_diffT}(x,y)=\;&47775744x^4+91570176x^3y+535265280x^3\\
&+65816064x^2y^2+768913920x^2y+2430413824x^2\\
&+21024576xy^3+368184000xy^2+2326178048xy\\
&+6026909696x+2518569y^4+58766610y^3\\
&+556603749y^2+2892436576y+7522126080.
\end{aligned}
\tag{6.5}
\]

For two spokes in different matched layers with different terminal labels (`a=2,b=0`),

\[
R_{MM\_diff\_diffT}(x,y)=\frac{1}{4232}
\left(
40787712x^2+39088224xy+407697696x+9364887y^2+195824691y+1035155664
\right).
\tag{6.6}
\]

All displayed coefficients are positive, and the archived output verifies the same statement for the remaining fifteen orbits. Equations (5.1)–(5.6), the exhaustive orbit list, and the exact marked-layer construction prove the theorem.

## 7. Coordination with NM13-08 and why this is not duplication

NM13-08's newest theorem proves strict unit p-NC for

\[
G_{k,r}=K_{3,2k+r}+M_k,
\]

with **no triangle edges** among the three fixed terminals. Its key mechanism is exactly the commuting nilpotent algebra (5.1)–(5.3), and it closes fourteen edge-pair orbits.

The present theorem uses that algebra as a reusable dependency but changes the initial graph by adding all three terminal edges. This has two substantive effects:

* the initial response vector changes from the all-separated state to the triangle vector `q=(1,1,1,1,3)`;
* six new orbit types involving one or two core edges must be proved, while every previous spoke/matching orbit acquires different coefficients because of the changed initial response.

Thus NM13-08 supplies the decomposition theory and NM13-04 supplies a new **triangle-seeded 3-connected sign theorem**. The two results are complementary rather than duplicate.

A further consequence is available from NM13-04's preceding transparent-substitution theorem: any edge of any `H_{k,r}` may subsequently be replaced recursively by the transparent PF gadgets `A_ell` from the preceding run while preserving unit p-NC. That decorated consequence introduces separators and is not counted as the principal gain here; the principal advance is the undecorated 3-connected core family itself.

## 8. Exact checker and independent small-instance falsification

Executed exact checker:

`proofnet24/NM13-04/progress-forest/runs/2026-09-20/2026-09-20T04-18-30Z__triangle-matched-right_checker.py`

creation commit `d7504d522818cca8f6f61249902f0a0ff90a7d76`.

Archived executed output:

`proofnet24/NM13-04/progress-forest/runs/2026-09-20/2026-09-20T04-18-30Z__triangle-matched-right_checker.out`

creation commit `a40515eed3f45590d3a9951abe18e96357041f01`.

The checker:

1. reconstructs the five terminal partitions and both unmarked layer matrices from direct subset enumeration;
2. verifies `N^3=0`, `N^2!=0`, and `P=23I+12N+(5/3)N^2` exactly;
3. reconstructs the triangle vector and every one-edge/two-edge marked local transfer from direct finite enumeration;
4. symbolically derives all 20 Rayleigh polynomials over `QQ[x,y]`;
5. clears denominators and asserts that every coefficient of every primitive numerator is strictly positive;
6. independently brute-forces **every edge subset and every edge pair** for `(k,r)=(1,0),(1,1),(2,0)` and compares the forest totals with the symbolic transfer formula.

The independent brute-force outputs are:

* `H_{1,0}=K_5`: 5 vertices, 10 edges, `Z=291`, minimum Rayleigh gap `210`;
* `H_{1,1}`: 6 vertices, 13 edges, `Z=1466`, minimum Rayleigh gap `1372`;
* `H_{2,0}`: 7 vertices, 17 edges, `Z=10547`, minimum Rayleigh gap `8484`.

The executed output terminates

`ALL_EXACT_CHECKS_PASS`.

These finite checks are sanity checks only. The all-parameter theorem comes from the symbolic positive-coefficient proof in §§5–6.

## 9. What failed / residual obstruction

No source-valid counterexample was found. The theorem does **not** close the parent conjecture, because an arbitrary 3-connected graph does not decompose into ordinary/matched right layers over one fixed terminal triangle.

The exact obstruction is now sharper. The successful family has a three-terminal response semigroup contained in the three-dimensional algebra

\[
\operatorname{span}\{I,N,N^2\},\qquad N^3=0,
\]

and all marked responses remain tractable enough that the twenty orbit gaps become positive-coefficient polynomials. P14's generic degree-three environment has no such a priori algebraic closure. A general proof would need either:

* a structural theorem forcing an arbitrary 3-connected neighborhood into a positivity-preserving cone larger than this nilpotent algebra, or
* a deletion/contraction inequality that controls the mixed response without the already-refuted reverse-Cauchy condition.

This run therefore provides a concrete larger positive cone target rather than another local apex lemma.

## 10. Next materially different attack

Do **not** merely add a third right-layer type and repeat orbit enumeration. The next attack should test an actual closure principle:

> Introduce an arbitrary three-terminal layer whose transfer is `aI+bN+cN^2` with nonnegative local marked responses, derive necessary and sufficient inequalities on `(a,b,c)` and the marked matrices for all triangle-seeded Rayleigh gaps to remain nonnegative, and check whether the matched-pair and ordinary-star layers lie in the interior of that cone.

If such a cone is closed under multiplication and includes a genuinely broader family of 3-terminal gadgets, it would turn the present example into a deletion/decomposition theorem rather than another named graph family. If the cone fails, the first exact failing layer supplies a focused source-valid counterexample search target.

## 11. `ledger_delta`

```yaml
ledger_delta:
  track: NM13-04
  parent: T07_uniform_forest_pairwise_negative_edge_correlation
  source_status_before: OPEN
  source_status_after: OPEN
  parent_metric: largest_completely_certified_all_simple_graph_order
  parent_before: 9
  parent_after: 9
  counterexample_order_lower_bound_before: ">=10"
  counterexample_order_lower_bound_after: ">=10"
  mechanism_before: "two-terminal transparent substitution; split families; NM13-08 matched-right 3-terminal algebra"
  mechanism_after: "strict p-NC for H_{k,r}=K_3 join (M_k disjoint_union I_r), all k,r>=0, by exhaustive 20-orbit positive-coefficient sign theorem"
  theorem_id: T07-TRIANGLE-MATCHED-RIGHT-PNC-05
  theorem_status: CANDIDATE_FULL_RESTRICTED_PENDING_REVIEW
  new_class_is_3_connected: true
  new_class_non_series_parallel_when_right_nonempty: true
  exact_checker: proofnet24/NM13-04/progress-forest/runs/2026-09-20/2026-09-20T04-18-30Z__triangle-matched-right_checker.py
  exact_output: proofnet24/NM13-04/progress-forest/runs/2026-09-20/2026-09-20T04-18-30Z__triangle-matched-right_checker.out
  exact_result: ALL_EXACT_CHECKS_PASS
  predecessor_method: two_terminal_activity_balancing_and_transparent_substitution
  current_method: three_terminal_nilpotent_transfer_with_triangle_seed
  residual_obstruction: "arbitrary 3-connected three-terminal environments need not lie in span{I,N,N^2} or any currently proved positivity-preserving response cone"
  next_attack: "derive and test a positivity cone for general three-terminal transfers aI+bN+cN^2 and marked responses"
```

`END OF REPORT`

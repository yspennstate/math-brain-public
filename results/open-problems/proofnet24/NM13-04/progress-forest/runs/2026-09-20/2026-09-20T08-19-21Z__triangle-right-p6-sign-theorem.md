Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.**

# NM13-04 / T07 — triangle-seeded P6 sign theorem

Status: **PARTIAL on the parent Grimmett–Winkler conjecture / CANDIDATE_FULL for the restricted theorem below, pending later independent review.** The arbitrary-finite-graph uniform-all-forests conjecture remains OPEN.

Repository / branch: private `yspennstate/math-open-problems` / `master`  
Assigned root: `proofnet24/NM13-04/progress-forest/`  
Companion: NM13-08, `proofnet24/NM13-08/progress-forest-structure/`

## 0. Short handoff and substantive move

The preceding NM13-04 run proved strict pairwise negative edge correlation for

\[
K_3\vee(pP_5\sqcup rK_1),\qquad p,r\ge0,
\]

by the five-state three-terminal transfer algebra. Of its 72 local edge-pair orbits, 70 were positive in the bivariate Newton cone; the two same-`P5` different-terminal spoke orbits at path distance three or four were repaired by exact two-corner lattice certificates.

The newest complementary NM13-08 report then moved the independent-terminal side to `P6`. It obtained

\[
T_{P_6}=23396I+37512N+25562N^2,\qquad N^3=0,
\]

proved the independent-terminal `P6` class, and, more importantly for future work, derived a 15-state path-extension operator with minimal polynomial

\[
(\lambda-1)^2(\lambda^2-6\lambda+2)^3,
\]

hence an order-eight recurrence in the path length.

This run changes the seed from three independent terminals to a **triangle**, recomputes all marked `P6` responses exactly, and proves the corresponding all-parameter triangle-seeded theorem. This is not a formal consequence of NM13-08: the triangle introduces three core edges, new marked pair types, and different Rayleigh quartics. A refutation-first exact orbit search found no negative physical parameter point. Four orbit polynomials leave the Newton cone; all four admit exact two-corner certificates.

`operations/PROGRESS20_2026-09-20.md`, current LIVE20 mapping, `POSTED.md`, the preceding own report, the newest NM13-08 report, and the preserved P14 obstruction state were the essential repository dependencies. No historical or peer file was edited.

## 1. Parent problem before/after, separately from the mechanism gain

For a finite graph \(G=(V,E)\), let

\[
I_G(\mathbf y)=\sum_{\substack{F\subseteq E\\F\text{ acyclic}}}\prod_{e\in F}y_e,
\qquad
\Delta_G(e,f)=I_eI_f-I_GI_{ef},
\]

where all quantities on the right are evaluated at unit edge weights. Then
\(\Delta_G(e,f)\ge0\) is exactly pairwise negative correlation of distinct edges \(e,f\) under the uniform measure on **all** forests of \(G\), with isolated vertices and all component counts allowed.

**Parent source status:** `OPEN -> OPEN`.  
**Largest completely certified all-simple-graph order in repository continuity:** `9 -> 9`.  
**Equivalent lower bound on the order of a source-valid counterexample:** `>=10 -> >=10`.

No finite all-graph coverage is promoted by this run.

**Mechanism before:** strict p-NC for \(K_3\vee(pP_5\sqcup rK_1)\).

**Mechanism after:** strict p-NC for the new all-parameter class

\[
G_{p,r}:=K_3\vee(pP_6\sqcup rK_1),\qquad p,r\ge0.
\]

This is a genuine restricted theorem, not a claim on arbitrary graphs.

## 2. Preserved P14 proof state and failed routes

The supported P14 inheritance remains:

1. Grimmett–Winkler plus the repository's dense-nine exact completion cover every simple graph through order nine in the unit all-forest scope.
2. Forest factorization over blocks reduces a vertex-minimal counterexample to a 2-connected graph.
3. P14's two-separator transfer, together with the recovered fixed-graph unit-to-positive-weight implication used there, reduces a vertex-minimal source counterexample further to a **3-connected** graph.

The failed generic routes remain failed and were not recycled:

- a generic degree-three apex/star-mesh reduction leaves a mixed three-terminal polarization with no universal sign;
- universal nonnegativity of that mixed term is false;
- the proposed reverse-Cauchy sufficient inequality was exactly refuted on a physical six-vertex graph even though its actual Rayleigh gap remained positive;
- naive Lorentzian/complete-log-concavity, real-stability, and Gårding shortcuts still lack the source-matching hypothesis for arbitrary graphic independence polynomials.

The theorem below therefore enlarges a structured 3-connected positive region; it does not discharge the arbitrary 3-connected obstruction.

## 3. Current literature scope — bounded check on 20 September 2026

The source distinctions remain essential.

- Grimmett–Winkler, `arXiv:math/0302185` / RSA 24 (2004), study the uniform measure on **all forests**. Their computation verifies the conjecture for all graphs on at most eight vertices and for nine-vertex graphs with at most eighteen edges; they explicitly distinguish the already-known uniform-spanning-tree law.
- Erickson, `arXiv:1008.3660`, proves the stronger positive-weight Rayleigh statement for **series-parallel** graphs.
- Huang, `arXiv:2311.00965`, still describes general arboreal-gas negative correlation as open while treating special graph/parameter regimes.
- Bado, DOI `10.1016/j.spl.2026.110960`, proves strict p-NC for every wheel under the uniform-all-forests law, another infinite 3-connected non-series-parallel class.
- Tang–Zhang, `arXiv:2603.10738` (11 March 2026), treat specified complete-graph spanning-subgraph ensembles, including forests with exactly \(k\) components for fixed \(k\) and sufficiently large \(n\). That does not mix all component counts on arbitrary graphs.
- Tang–Zhang, `arXiv:2609.11578` (10 September 2026), treat high-degree regular random-cluster regimes. Their \(Q=0\) endpoint is percolation conditioned to be connected, not the all-forest measure here.

A bounded search for `uniform forest negative correlation`, `K3 join P6`, `P6 layer`, and nearby terminology did not surface the theorem below. That is negative evidence only; **novelty/priority remains UNVERIFIED**.

`POSTED.md` was checked. The T07 parent and this restricted extension are not treated as posted/settled source-level claims.

## 4. New all-parameter theorem

### Theorem `T07-TRIANGLE-RIGHT-P6-PNC-14`

For every \(p,r\ge0\) and every two distinct present edges \(e,f\) of

\[
G_{p,r}=K_3\vee(pP_6\sqcup rK_1),
\]

one has

\[
\boxed{\Delta_{G_{p,r}}(e,f)>0.}
\]

Hence every graph in this two-parameter family has strict pairwise negative edge correlation under the uniform measure on all forests.

For \(p+r>0\), \(G_{p,r}\) is 3-connected: after deletion of any two vertices, at least one triangle vertex remains unless both deletions are outside the triangle, and every surviving right vertex is adjacent to every surviving triangle vertex. Every nontrivial member contains \(K_4\), hence is not series-parallel; for \(p\ge1\) it contains \(K_{3,3}\).

## 5. Exact five-state transfer

Use the terminal partitions

\[
D=0|1|2,\quad P_{12}=0|12,\quad P_{01}=01|2,\quad
P_{02}=02|1,\quad T=012.
\]

One isolated right vertex has transfer

\[
S=4I+N,\qquad N^3=0,\quad N^2\ne0.
\]

Exact frontier enumeration of one right `P6` gives

\[
T_{P_6}=
\begin{pmatrix}
23396&37512&37512&37512&190884\\
0&23396&0&0&75024\\
0&0&23396&0&75024\\
0&0&0&23396&75024\\
0&0&0&0&23396
\end{pmatrix}
=
23396I+37512N+25562N^2.
\]

The triangle seed response is

\[
q=(1,1,1,1,3).
\]

Expose the one or two right layers containing a chosen marked edge pair. If \(x\) unmarked `P6` layers and \(z\) unmarked singleton layers remain, divide out the positive scalar \(23396^x4^z\). The common response is

\[
U(x,z)=I+uN+vN^2
\]

with

\[
a=\frac{37512}{23396},\qquad c=\frac{25562}{23396},\qquad s=\frac14,
\]

\[
u=ax+sz,
\]

and

\[
v=cx+\binom{x}{2}a^2+\binom{z}{2}s^2+xzas.
\]

This follows directly from
\[
(I+aN+cN^2)^x(I+sN)^z
\]
and \(N^3=0\).

Every marked-layer response is a fixed \(5\times5\) matrix. Therefore every marked forest count after exposure is polynomial of total degree at most two in \((x,z)\), and every normalized Rayleigh numerator is a rational polynomial of total degree at most four.

As a consistency identity, the total forest count satisfies

\[
\frac{I_{G_{p,r}}(\mathbf1)}{23396^p4^r}
=
\frac{
4221450432p^2+1316446128pr+8143148400p
+102632403r^2+1265799637r+3831609712
}{547372816}.
\]

## 6. Exhaustive local response classification

Take a universal witness consisting of:

- the left triangle;
- two labelled `P6` right blocks;
- two labelled singleton right blocks.

It has exactly \(55\) edges and \(\binom{55}{2}=1485\) unordered edge pairs. The automorphism action generated by terminal \(S_3\), swapping the two `P6` blocks, independently reversing each `P6`, and swapping the two singleton blocks reduces these pairs to exactly

\[
\boxed{93}
\]

orbits.

This finite witness is exhaustive for local **pair types**: any edge pair in any \(G_{p,r}\) meets at most two right components, so after labelling those distinguished components it is represented in the witness. The remaining component counts are nonnegative integers \(x,z\).

For each orbit \(\mathcal O\),

\[
\Delta(e,f)=(23396^x4^z)^2R_{\mathcal O}(x,z),
\]

where \(R_{\mathcal O}\) has degree at most four. Expand it in the bivariate Newton basis,

\[
R_{\mathcal O}(x,z)
=
\sum_{i+j\le4}c^{\mathcal O}_{ij}
\binom{x}{i}\binom{z}{j}.
\]

The exact checker proves:

- **89 of 93** orbit polynomials have no negative Newton coefficient;
- every one of those 89 has a strictly positive constant term;
- the minimum regular-orbit constant is \(2\);
- the minimum positive Newton coefficient is \(1/8\).

Since every \(\binom{x}{i}\binom{z}{j}\) is nonnegative on \(\mathbb Z_{\ge0}^2\), all 89 regular orbit families are strictly positive throughout the physical parameter lattice.

There is no zero-constant orbit: the triangle removes the independent-terminal \(K_{3,1}\) equality degeneracy.

## 7. The four Newton failures and exact repairs

The positive-Newton route fails exactly for four same-`P6`-block, different-terminal spoke geometries:

\[
(0,3),\quad(0,4),\quad(0,5),\quad(1,4)
\]

in path-vertex coordinates, up to reversal and terminal permutation. Each exceptional quartic has four negative Newton coefficients. This is a genuine failed proof route, not hidden by the final result.

Use the following elementary lemma.

**Two-corner lattice lemma.** Let \(Q(x,z)\in\mathbb Z[x,z]\). Suppose, for some positive integers \(A,B\),

1. \(Q(A+X,Z)\) has all ordinary monomial coefficients strictly positive;
2. \(Q(X,B+Z)\) has all ordinary monomial coefficients strictly positive;
3. \(Q(i,j)>0\) for \(0\le i<A,\ 0\le j<B\).

Then \(Q(x,z)>0\) for every \(x,z\in\mathbb Z_{\ge0}\).

**Proof.** If \(x\ge A\), use (1). If \(x<A\) but \(z\ge B\), use (2). The only remaining points lie in the finite rectangle covered by (3). QED.

After clearing positive denominators, the exact certificates are:

| spoke geometry | \(A\) | \(B\) | residual points | minimum residual value |
|---|---:|---:|---:|---:|
| `(0,3)` different terminals | 2 | 11 | 22 | 1505915301505273415330400 |
| `(0,4)` different terminals | 9 | 52 | 468 | 12659554396114528922536192 |
| `(0,5)` different terminals | 24 | 149 | 3576 | 6474568161819744179374592 |
| `(1,4)` different terminals | 2 | 13 | 26 | 23954482193924695332030464 |

For each row, both shifted quartics have all 15 monomial coefficients strictly positive. The exact cleared quartics, their four negative Newton coefficients, both shifted minimum coefficients, and every residual-box verification are archived in the checker output.

Thus the four exceptional orbit polynomials are strictly positive on all of \(\mathbb Z_{\ge0}^2\). Combined with the 89 Newton-positive orbits, this proves `T07-TRIANGLE-RIGHT-P6-PNC-14`.

The finite computation is an exhaustive classification of finitely many local response types plus exact sign certificates for four quartics. It is **not** an extrapolation from finitely many graph orders.

## 8. Independent all-pairs physical check by Matrix-Tree contraction

The checker contains a second exact implementation that does not use the transfer matrices.

For any finite multigraph \(H\),

\[
F(H)=\sum_{\pi\in\Pi(V(H))}
\prod_{B\in\pi}\tau(H[B]),
\]

because every forest uniquely determines its vertex-component partition \(\pi\), and on each block \(B\) its edges form a spanning tree. Each \(\tau(H[B])\) is evaluated by the exact Matrix-Tree theorem.

For a required acyclic edge set \(S\), forests of \(H\) containing \(S\) are in bijection with forests of the contracted multigraph \(H/S\), retaining parallel-edge multiplicities. Thus the second implementation computes \(I\), every \(I_e\), and every \(I_{ef}\) independently.

For the smallest genuinely new graph

\[
K_3\vee P_6
\]

it checks all \(26\) edges and all \(\binom{26}{2}=325\) edge pairs and obtains

\[
|V|=9,\qquad |E|=26,\qquad I(\mathbf1)=692264,
\]

\[
\min_{e\ne f}\Delta(e,f)=23243040
\]

(attained by the two endpoint path edges), and

\[
\max_{e\ne f}\Delta(e,f)=14406637792.
\]

The transfer count and Matrix-Tree count agree exactly. The executable ends `ALL_EXACT_CHECKS_PASS`.

## 9. Essential artifacts

Exact checker:

`proofnet24/NM13-04/progress-forest/runs/2026-09-20/2026-09-20T08-19-21Z__triangle_p6_checker.py`

creation commit:

`c15f5a1ea22161e2cc535cc87d3c4428534920ef`

Executed exact output:

`proofnet24/NM13-04/progress-forest/runs/2026-09-20/2026-09-20T08-19-21Z__triangle_p6_checker.out`

creation commit:

`9f51cad51c6f023e96a77d02130cd643f4a7997a`

The output ends `ALL_EXACT_CHECKS_PASS`.

## 10. Coordination gain and next route

NM13-08 owns the complementary decomposition/path-length theory. Its new order-eight path-tail recurrence explains why treating `P6` as an isolated one-off should not be the endpoint. NM13-04 supplies the triangle-seeded marked sign theorem and shows that, at `P6`, the only failures of the naive positive-Newton cone occur in the same geometric sector as on the independent-terminal side: same-layer, different-terminal spokes separated by path distance at least three.

The next route is therefore **not** merely “enumerate `P7`.” Use the NM13-08 path-extension recurrence to seek a recurrence/cone theorem in the path length for these exceptional marked-spoke Rayleigh polynomials. Exact `P7/P8` calculations should be used refutation-first as data for that recurrence: the first negative physical value would be a source-valid counterexample template; persistent positivity should be converted into a uniform-in-path-length sign mechanism.

## ledger_delta

```yaml
track: NM13-04
target: T07
parent_problem: uniform-all-forests pairwise negative edge correlation on every finite graph
parent_status_before: OPEN
parent_status_after: OPEN
metric:
  name: largest completely certified all-simple-graph order
  before: 9
  after: 9
counterexample_order_lower_bound:
  before: ">=10"
  after: ">=10"
mechanism_before: "strict p-NC for K3 join (p P5 disjoint_union r K1), all p,r>=0"
mechanism_after: "strict p-NC for K3 join (p P6 disjoint_union r K1), all p,r>=0"
new_theorem_id: T07-TRIANGLE-RIGHT-P6-PNC-14
restricted_status: CANDIDATE_FULL_PENDING_LATER_INDEPENDENT_REVIEW
finite_core:
  witness_edges: 55
  witness_pairs: 1485
  automorphism_orbits: 93
  newton_positive_orbits: 89
  exceptional_orbits: 4
  exceptional_certificate_shifts:
    - [2, 11]
    - [9, 52]
    - [24, 149]
    - [2, 13]
independent_check:
  graph: "K3 join P6"
  vertices: 9
  edges: 26
  all_edge_pairs_checked: 325
  forest_count: 692264
  min_rayleigh_gap: 23243040
artifacts:
  checker_commit: c15f5a1ea22161e2cc535cc87d3c4428534920ef
  output_commit: 9f51cad51c6f023e96a77d02130cd643f4a7997a
p14_state_preserved: true
posted_conflict: false
novelty: UNVERIFIED
next_step: "Use NM13-08's order-eight path-tail recurrence to seek a uniform-in-path-length sign/cone theorem for the exceptional different-terminal spoke sector; use P7/P8 only refutation-first as recurrence data."
```

Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.**

# NM13-04 / T07 — strict p-NC for a triangle joined to every right linear forest with component order at most 4

Status: **PARTIAL on the parent Grimmett–Winkler conjecture / CANDIDATE_FULL for the restricted theorem below, pending later independent review.** The arbitrary-finite-graph uniform-all-forests conjecture remains OPEN.

Repository / branch: private `yspennstate/math-open-problems` / `master`  
Assigned root: `proofnet24/NM13-04/progress-forest/`  
Companion: NM13-08, `proofnet24/NM13-08/progress-forest-structure/`

## 0. Short handoff and the materially different move in this run

The preceding NM13-04 run proved strict pairwise negative edge correlation for

\[
K_3\vee\bigl(pP_3\sqcup mK_2\sqcup rK_1\bigr),
\]

by a four-parameter-free positive Newton certificate over the five terminal-connectivity states. That theorem is preserved. Its exact structural frontier was a right component of order four.

The newest complementary NM13-08 report then attacked precisely one right `P4` layer type with **independent** left terminals. It found that the positive Newton cone fails for exactly one marked `P4` orbit, but rescued that orbit with a shifted-quadrant staircase certificate. That result is preserved rather than duplicated.

This run combines the two directions and proves the triangle-seeded mixed theorem with arbitrary simultaneous `P4`, `P3`, `K2`, and `K1` layers. The pure positive-Newton route genuinely fails again on one orbit, so this run executes the materially different staircase mechanism rather than reporting another unchanged Newton-cone calculation.

`operations/PROGRESS20_2026-09-20.md`, the current LIVE20 mapping, the latest own report, the relevant P14 handoff, the latest NM13-08 report, and `POSTED` status were checked. NM13-04 remains the T07 sign/deletion–contraction worker; NM13-08 remains the complementary decomposition worker. No posted source-level T07 closure is reopened.

## 1. Parent problem before/after, separately from mechanism gain

For a finite graph `G=(V,E)`, write

\[
I_G(\mathbf y)=\sum_{F\subseteq E:\,F\text{ acyclic}}\prod_{e\in F}y_e,
\qquad
\Delta_G(e,f)=I_eI_f-I_GI_{ef}.
\]

At unit weights, `Delta_G(e,f)>=0` is exactly pairwise negative edge correlation for the uniform measure on **all** forests, with all component counts mixed.

**Parent source status:** `OPEN -> OPEN`.  
**Largest completely certified all-simple-graph order in repository continuity:** `9 -> 9`.  
**Equivalent lower bound on the order of a source-valid counterexample:** `>=10 -> >=10`.

No source-level finite-coverage metric moves.

**Mechanism before:** triangle joined to arbitrary right linear forests whose components have order at most 3; independently, NM13-08 controlled repeated `P4` layers with independent left terminals.

**Mechanism after:** a complete exact sign theorem for the strictly larger four-parameter family

\[
G_{a,b,c,d}:=K_3\vee\bigl(aP_4\sqcup bP_3\sqcup cK_2\sqcup dK_1\bigr),
\qquad a,b,c,d\ge0.
\]

Thus the right induced graph may be **any linear forest all of whose components have order at most 4**.

## 2. Recovered P14 proof history and failed routes

The source-level inherited state remains:

1. Grimmett–Winkler verify the uniform-all-forests pairwise conjecture for every graph on at most eight vertices and for nine-vertex graphs with at most eighteen edges.
2. Repository exact work covers the complementary dense nine-vertex sector, so all simple graphs through order nine are covered in the source unit-weight scope.
3. P14 block/direct-sum factorization reduces a vertex-minimal counterexample to a 2-connected graph.
4. P14's two-separator transfer, combined with the fixed-graph unit-to-positive-weight implication preserved in that line, reduces a vertex-minimal source counterexample further to a **3-connected** graph.

The failed routes remain failed and were not silently retried:

- the generic degree-three apex/star-mesh route leaves a mixed three-terminal polarization;
- that mixed polarization is not universally nonnegative;
- the proposed reverse-Cauchy sufficient inequality was exactly refuted on a physical six-vertex graph even though the actual Rayleigh gap remained positive;
- Lorentzian/complete-log-concavity, naive real-stability perturbation, and Gårding shortcuts still lack the source-matching hypothesis needed for arbitrary graphic independence polynomials.

The theorem below expands a structured 3-connected positive region; it does not claim to solve arbitrary 3-connected graphs.

## 3. Current literature scope check — 20 September 2026

Bounded fresh public checks were made against exact source scopes.

- Grimmett–Winkler, `arXiv:math/0302185`, study the uniform measure on **all forests** and record the finite verification above; they explicitly separate the already-known uniform-spanning-tree law.
- Erickson, `arXiv:1008.3660`, proves an SOS formula and the stronger positive-weight independent-set-Rayleigh property for **series-parallel** graphs.
- Huang, `arXiv:2311.00965`, still describes general arboreal-gas negative correlation as open while proving restricted results.
- Bado, DOI `10.1016/j.spl.2026.110960`, proves strict p-NC for every wheel, another infinite 3-connected non-series-parallel family.
- Tang–Zhang, `arXiv:2603.10738` (11 March 2026), treat specified complete-graph spanning-subgraph ensembles, including forests with a **fixed** number of components for fixed `k` and sufficiently large `n`; this is not arbitrary-graph uniform all-forest measure.
- Tang–Zhang, `arXiv:2609.11578` (10 September 2026), prove negative correlation in high-degree regular random-cluster regimes. Their `Q=0` endpoint is Bernoulli bond percolation conditioned to be **connected**, not the uniform forest law.

A bounded search did not surface the exact theorem below. This is negative evidence only; **novelty/priority remains UNVERIFIED**.

## 4. New all-parameter theorem

Let the three left vertices span a triangle. On the right take an arbitrary disjoint union of `a` copies of `P4`, `b` copies of `P3`, `c` copies of `K2`, and `d` isolated vertices, and join every right vertex to all three left vertices.

### Theorem `T07-TRIANGLE-RIGHT-PATH4-PNC-11`

For every `a,b,c,d>=0` and every two distinct present edges `e,f` of

\[
G_{a,b,c,d}=K_3\vee(aP_4\sqcup bP_3\sqcup cK_2\sqcup dK_1),
\]

\[
\boxed{\Delta_{G_{a,b,c,d}}(e,f)>0.}
\]

Hence the uniform measure on **all forests** of every member of this four-parameter family has strict pairwise negative edge correlation.

Every nontrivial member is 3-connected: after deleting fewer than three vertices, any surviving left-triangle vertex connects all surviving vertices. Every nontrivial member contains `K4`, so it is not series-parallel. The theorem strictly contains the preceding NM13-04 component-order-at-most-3 theorem by setting `a=0`.

## 5. Common five-state nilpotent transfer algebra

Use the five terminal partitions

\[
D=0|1|2,\quad P_{12}=0|12,\quad P_{01}=01|2,\quad P_{02}=02|1,\quad T=012.
\]

For one isolated right vertex, let `S=4I+N`; exact local enumeration gives `N^3=0`. The four unmarked component transfers are

\[
T_{P_4}=734I+780N+\frac{961}{3}N^2,
\]
\[
T_{P_3}=130I+103N+\frac{85}{3}N^2,
\qquad
T_{K_2}=23I+12N+\frac53N^2,
\qquad
T_{K_1}=4I+N.
\]

The triangle initial response is

\[
q=(1,1,1,1,3).
\]

After exposing the one or two right components containing a marked edge pair, let

\[
(x_4,x_3,x_2,x_1)\in\mathbb Z_{\ge0}^4
\]

be the remaining numbers of `P4,P3,K2,K1` layers. Removing the positive leading factors, each normalized layer has the form `I+alpha N+beta N^2`, with

\[
\alpha=\left(\frac{390}{367},\frac{103}{130},\frac{12}{23},\frac14\right),
\qquad
\beta=\left(\frac{961}{2202},\frac{17}{78},\frac5{69},0\right).
\]

Because `N^3=0`, their product is exactly

\[
U=I+uN+vN^2,
\]

where

\[
u=\sum_i\alpha_i x_i,
\]

and

\[
v=\sum_i\beta_i x_i+\sum_i\binom{x_i}{2}\alpha_i^2+
\sum_{i<j}x_ix_j\alpha_i\alpha_j.
\]

Thus every marked forest count is a polynomial of total degree at most two in the remaining layer counts. Every normalized Rayleigh difference is consequently a rational polynomial of total degree at most four.

## 6. Exhaustive local-type reduction: 126 edge-pair orbits

A universal local witness consists of the left triangle plus **two copies of each** of `P4,P3,K2,K1`. It has

\[
3+2\cdot15+2\cdot11+2\cdot7+2\cdot3=75
\]

edges and therefore `C(75,2)=2775` unordered edge pairs. Any edge pair in any `G_{a,b,c,d}` touches at most two right components, so it is represented in this witness.

The exact automorphism action uses the terminal `S3`, block swaps and path reversals for the two `P4` copies, the same for `P3`, endpoint swaps for `K2`, and the two singleton copies. It reduces the 2775 witness pairs to exactly **126** pair orbits.

For an orbit `O`, after removing the distinguished components, write

\[
\Delta=(734^{x_4}130^{x_3}23^{x_2}4^{x_1})^2R_O(x_4,x_3,x_2,x_1).
\]

The prefactor is positive. Expand `R_O` in the multivariate Newton basis

\[
R_O=\sum c_{i_4i_3i_2i_1}
\binom{x_4}{i_4}\binom{x_3}{i_3}\binom{x_2}{i_2}\binom{x_1}{i_1}.
\]

The exact checker proves:

- **125 of 126** orbit polynomials have no negative Newton coefficient;
- every one of those 125 has positive constant coefficient;
- the minimum orbit constant is `2`;
- the minimum positive Newton coefficient among those 125 is `1/8`.

Therefore those 125 orbits are strictly positive for all nonnegative integer layer counts.

## 7. The unique failed Newton orbit and the nested staircase certificate

The sole orbit outside the positive Newton cone consists of two spokes in the **same `P4` block**, one at each path endpoint, with different terminal labels. Its four-variable Newton expansion has exactly **20 negative coefficients**. Therefore the naive extension of the preceding Newton proof is false as a proof mechanism; this is a genuine failed route, not hidden by the final theorem.

Let `R_*` denote this exceptional normalized Rayleigh polynomial in variable order `(x4,x3,x2,x1)=(P4,P3,K2,K1 extras)`.

### Outer four-variable shifted orthants

The exact checker expands `R_*` at the four shifts

\[
(3,0,0,0),\quad(2,0,0,1),\quad(1,0,0,6),\quad(0,0,0,10).
\]

Each shifted polynomial has all **70** ordinary monomials of total degree at most four present with strictly positive rational coefficients. Their minimum coefficients are respectively

\[
\frac9{32},\quad\frac{555}{2936},\quad\frac9{32},\quad\frac9{32}.
\]

These four positive orthants cover the entire nonnegative lattice except the following 17 `(x4,x1)` locations:

\[
\{(0,z):0\le z<10\}\cup
\{(1,z):0\le z<6\}\cup\{(2,0)\}.
\]

### Uniform inner two-variable staircase on those 17 boundary fibers

For each of those 17 fixed outer locations, regard `R_*` as a polynomial in `(x3,x2)`. The four uniform inner shifts

\[
(3,0),\quad(2,2),\quad(1,3),\quad(0,5)
\]

produce all 15 ordinary monomials of degree at most four with strictly positive coefficients on **every one** of the 17 boundary fibers. The worst minimum coefficients over all 17 fibers are

\[
\frac{34677504}{18189665},\quad
\frac{1492992}{279841},\quad
\frac{20245248}{18189665},\quad
\frac{1492992}{279841}.
\]

The inner staircase leaves only ten `(x3,x2)` points,

\[
\{(0,j):0\le j<5\}\cup
\{(1,j):0\le j<3\}\cup
\{(2,j):0\le j<2\}.
\]

Across the 17 outer fibers this is exactly **170** residual lattice points. Exact rational evaluation gives positive values at all 170; the minimum is

\[
447184
\]

at `(x4,x3,x2,x1)=(0,0,0,0)`.

Hence `R_*>0` on all of `Z_{>=0}^4`. Together with the 125 Newton-positive orbits, this proves `T07-TRIANGLE-RIGHT-PATH4-PNC-11`.

This is an all-parameter proof. The finite work classifies the finite **local response types** and certifies one finite residual staircase; it is not an extrapolation from finitely many graph orders.

## 8. Independent physical brute check

As an independent check of the local-transfer implementation, the executable directly enumerates every one of the `2^18` edge subsets of the smallest new graph, `K3 join P4`.

It obtains

\[
|V|=7,\qquad |E|=18,\qquad I_G(\mathbf1)=14860,
\]

with minimum Rayleigh gap `127864` and maximum `5945384` over all physical edge pairs. This is only a sanity check; the theorem for arbitrary parameters is supplied by the symbolic transfer and staircase argument above.

## 9. Essential exact artifacts

Executed before this report:

- `2026-09-20T06-18-57Z__triangle_path4_checker.py`, creation commit `fc6294a8a8b94cfd989fcb68a8f9c4159487afbc`, local SHA-256 `5af750c3700554bca15981b4765d4ba1e4ea288723f01a1c097cfea6a587ff63`;
- `2026-09-20T06-18-57Z__triangle_path4_checker.out`, creation commit `1347f82836734d3296f8e70d117b059dbbbbf0c4`, local SHA-256 `403df6ec17dd376f22c02f4ed74bfda8bc444b8f068cf948d707a7e37a6d5285`.

The archived execution ends `ALL_EXACT_CHECKS_PASS`.

## 10. Residual obstruction and next attack

The parent conjecture remains open. The present family still has a dominating triangle and a right induced graph of bounded component order. The first unproved path layer is `P5`; arbitrary 3-connected response environments remain much broader.

The next attack is **refutation-first on a triangle-seeded `P5` layer**: construct its exact marked response orbits, search directly for a negative physical or all-parameter Rayleigh value, and only if that search fails attempt a bounded higher-dimensional staircase certificate. This tests whether the order-4 rescue is a stable structural phenomenon or the last positive step before a counterexample template.

```yaml
ledger_delta:
  track: NM13-04
  parent: T07_uniform_forest_pairwise_negative_edge_correlation
  parent_status_before: OPEN
  parent_status_after: OPEN
  complete_all_simple_graph_order_before: 9
  complete_all_simple_graph_order_after: 9
  counterexample_order_lower_bound_before: 10
  counterexample_order_lower_bound_after: 10
  mechanism_before: "strict p-NC for K3 join right linear forests with component order <=3; NM13-08 independent-terminal P4 staircase"
  mechanism_after: "strict p-NC for K3 join arbitrary right linear forests with component order <=4"
  theorem_id: T07-TRIANGLE-RIGHT-PATH4-PNC-11
  parameters: 4
  local_witness_edges: 75
  local_witness_pairs: 2775
  pair_orbits: 126
  newton_positive_orbits: 125
  exceptional_orbits: 1
  exceptional_negative_newton_coefficients: 20
  outer_shifted_orthants: 4
  outer_boundary_fibers: 17
  inner_shifted_quadrants_per_fiber: 4
  finite_residual_points: 170
  finite_residual_minimum: 447184
  brute_new_graph: "K3 join P4: n=7, m=18, Z=14860, minDelta=127864"
  exact_checker_result: ALL_EXACT_CHECKS_PASS
  failed_route: "naive four-variable positive Newton cone fails for the opposite-endpoint different-terminal spoke pair in one P4 block"
  residual_obstruction: "P5 marked-layer sign and arbitrary 3-connected environments"
  next_attack: "triangle-seeded P5 refutation-first orbit scan, then staircase only if no negative value appears"
  novelty_priority: UNVERIFIED
  restricted_theorem_review_status: CANDIDATE_FULL_pending_independent_review
```

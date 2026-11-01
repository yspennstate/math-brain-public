Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.**

# NM13-04 / T07 — strict p-NC for a triangle joined to repeated P5 layers

Status: **PARTIAL on the parent Grimmett–Winkler conjecture / CANDIDATE_FULL for the restricted theorem below, pending later independent review.** The arbitrary-finite-graph uniform-all-forests conjecture remains OPEN.

Repository / branch: private `yspennstate/math-open-problems` / `master`  
Assigned root: `proofnet24/NM13-04/progress-forest/`  
Companion: NM13-08, `proofnet24/NM13-08/progress-forest-structure/`

## 0. Short handoff and this run's substantive move

The preceding NM13-04 run proved strict pairwise negative edge correlation for

\[
K_3\vee(aP_4\sqcup bP_3\sqcup cK_2\sqcup dK_1),
\]

using the common five-state three-terminal transfer algebra. The positive Newton cone failed for one `P4` spoke-pair orbit, repaired by a nested staircase certificate. The explicit next attack was `P5`, refutation first.

The newest complementary NM13-08 report then carried out the independent-terminal `P5` attack. It found the exact unmarked transfer

\[
T_{P_5}=4144I+5524N+\frac{9050}{3}N^2,
\qquad N^3=0,
\]

and proved p-NC for repeated `P5` layers plus isolated right vertices with **independent** left terminals. Its 61 local edge-pair orbits had two exceptional `P5` spoke-pair quartics outside the positive Newton cone, both repaired by a reusable two-corner lattice sign lemma.

This run preserves both predecessor results and changes the seed to the **triangle**. The triangle-seeded `P5` class is not a formal consequence of the independent-terminal theorem: core edges create new local pair types and the marked Rayleigh polynomials change. Exact reduction gives 72 local orbits. Seventy lie in the nonnegative Newton cone; the same two geometric `P5` spoke types remain exceptional, but with different quartics and sharper two-corner certificates. No source-valid counterexample appears.

`operations/PROGRESS20_2026-09-20.md`, the current LIVE20 mapping, `POSTED.md`, the latest own report, the P14 handoff state preserved there, and NM13-08's `2026-09-20T06-38-00Z__p5-corner-sign-report.md` were the essential repository dependencies read this run. No historical or peer file was edited.

## 1. Parent problem before/after, separately from mechanism gain

For a finite graph `G=(V,E)` write

\[
I_G(\mathbf y)=\sum_{F\subseteq E:\,F\text{ acyclic}}\prod_{e\in F}y_e,
\qquad
\Delta_G(e,f)=I_eI_f-I_GI_{ef}.
\]

At unit weights, `Delta_G(e,f)>=0` is exactly pairwise negative correlation for a uniformly sampled acyclic spanning edge subset, with **all** component counts mixed.

**Parent source status:** `OPEN -> OPEN`.  
**Largest completely certified all-simple-graph order in repository continuity:** `9 -> 9`.  
**Equivalent lower bound on the order of a source-valid counterexample:** `>=10 -> >=10`.

Finite all-graph coverage does not move in this run.

**Mechanism before:** triangle joined to arbitrary right linear forests with component order at most four.

**Mechanism after:** a new all-parameter strict-sign theorem for

\[
G_{p,r}:=K_3\vee\bigl(pP_5\sqcup rK_1\bigr),
\qquad p,r\ge0.
\]

This is the first triangle-seeded right component of order five in the NM13-04 line.

## 2. Recovered P14 proof state and failed routes

The supported predecessor facts remain unchanged and are used only as context for the structural frontier:

1. Grimmett–Winkler verify the uniform-all-forests pairwise conjecture for every graph on at most eight vertices and for nine-vertex graphs with at most eighteen edges.
2. Repository exact work covers the complementary dense nine-vertex sector, hence all simple graphs through order nine are covered in the unit-weight source scope.
3. P14 block/direct-sum factorization reduces a vertex-minimal counterexample to a 2-connected graph.
4. P14's two-separator transfer, together with the recovered fixed-graph unit-to-positive-weight implication, reduces a vertex-minimal source counterexample further to a **3-connected** graph.

The failed routes are still failed and were not retried as if open:

- the generic degree-three apex/star-mesh route leaves an uncontrolled mixed three-terminal polarization;
- that mixed polarization is not universally nonnegative;
- the proposed reverse-Cauchy sufficient inequality was exactly refuted on a physical six-vertex graph while the actual Rayleigh gap stayed positive;
- Lorentzian/complete-log-concavity, naive real-stability perturbation, and Gårding shortcuts still lack the source-matching hypothesis for arbitrary graphic independence polynomials.

The theorem below enlarges a structured 3-connected positive region; it does not solve arbitrary 3-connected graphs.

## 3. Current literature scope check — 20 September 2026

Bounded fresh public checks were made against exact scopes.

- Grimmett–Winkler, `arXiv:math/0302185`, study the uniform measure on **all forests** and record the finite verification above; they explicitly distinguish the already-known uniform-spanning-tree law.
- Erickson, `arXiv:1008.3660`, proves a positive sum-of-squares / independent-set-Rayleigh theorem for **series-parallel** graphs at positive edge weights.
- Huang, `arXiv:2311.00965`, still presents general arboreal-gas negative correlation as open while proving restricted cases.
- Bado, DOI `10.1016/j.spl.2026.110960`, proves strict p-NC for every wheel under the uniform-all-forests law, another infinite 3-connected non-series-parallel class.
- Tang–Zhang, `arXiv:2603.10738` (11 March 2026), treat specified complete-graph spanning-subgraph ensembles, including forests with exactly `k` components for fixed `k` and sufficiently large `n`; that is not arbitrary-graph uniform all-forest measure.
- Tang–Zhang, `arXiv:2609.11578` (10 September 2026), treat high-degree regular random-cluster regimes; their `Q=0` endpoint is percolation conditioned to be connected, not the all-forest measure here.

Searches for combinations of `uniform forest`, `negative correlation`, `K3 join P5`, and `P5 layer` did not surface the theorem below. This is bounded negative evidence only; **novelty/priority remains UNVERIFIED**.

## 4. New all-parameter sign theorem

### Theorem `T07-TRIANGLE-RIGHT-P5-PNC-13`

For every `p,r>=0` and every two distinct present edges `e,f` of

\[
G_{p,r}=K_3\vee(pP_5\sqcup rK_1),
\]

\[
\boxed{\Delta_{G_{p,r}}(e,f)>0.}
\]

Hence every graph in this two-parameter family has strict pairwise negative edge correlation under the uniform measure on all forests.

For `p+r>0`, `G_{p,r}` is 3-connected: deleting at most two vertices leaves at least one triangle vertex, and every surviving right vertex is adjacent to every surviving triangle vertex. It contains `K4`, so it is not series-parallel. If `p>=1`, it contains a `K_{3,3}` subgraph. Thus the result lies beyond Erickson's series-parallel scope.

## 5. Five-state transfer and triangle seed

Use terminal partitions

\[
D=0|1|2,\quad P_{12}=0|12,\quad P_{01}=01|2,\quad P_{02}=02|1,\quad T=012.
\]

For one isolated right vertex,

\[
S=4I+N,
\qquad N^3=0,
\]

and exact local forest enumeration of one right `P5` gives

\[
T_{P_5}=
\begin{pmatrix}
4144&5524&5524&5524&23624\\
0&4144&0&0&11048\\
0&0&4144&0&11048\\
0&0&0&4144&11048\\
0&0&0&0&4144
\end{pmatrix}
=
4144I+5524N+\frac{9050}{3}N^2.
\]

The triangle seed response is

\[
q=(1,1,1,1,3).
\]

After exposing the one or two right layers containing a marked pair, let `x` be the remaining number of `P5` layers and `z` the remaining number of singleton layers. Removing the positive factor `4144^x4^z`, the common unmarked response is

\[
U(x,z)=I+uN+vN^2,
\]

with

\[
u=\frac{1381}{1036}x+\frac14z,
\]

\[
v=\frac{4525}{6216}x
+\binom{x}{2}\left(\frac{1381}{1036}\right)^2
+\binom{z}{2}\frac1{16}
+xz\frac{1381}{4144}.
\]

Because `N^3=0`, every marked forest count is polynomial of total degree at most two in `(x,z)`, and every normalized Rayleigh difference is a rational polynomial of total degree at most four.

As a consistency check, the total forest count satisfies the exact all-parameter identity

\[
\frac{I_{G_{p,r}}(\mathbf1)}{4144^p4^r}
=
\frac{
5721483p^2+2146074pr+13273577p+201243r^2+2481997r+7513072
}{1073296}.
\]

## 6. Exhaustive local-type reduction: 72 edge-pair orbits

Take a universal local witness consisting of the triangle, two `P5` layers, and two singleton layers. It has `47` edges and therefore `1081` unordered edge pairs. The exact automorphism action generated by terminal `S3`, exchange of the two `P5` blocks, independent reversal of each `P5`, and exchange of the two singleton blocks reduces those pairs to exactly

\[
\boxed{72}
\]

orbits.

Every physical edge pair in every `G_{p,r}` touches at most two right layers, so it appears in this witness. After exposing its distinguished layers, the remaining counts `(x,z)` are nonnegative integers and

\[
\Delta(e,f)=(4144^x4^z)^2R_{\mathcal O}(x,z),
\]

for one of the 72 exact orbit polynomials `R_O`.

Expand in the bivariate Newton basis

\[
R_O(x,z)=\sum_{i+j\le4}c^O_{ij}\binom{x}{i}\binom{z}{j}.
\]

The exact checker proves:

- **70 of 72** orbit polynomials have no negative Newton coefficient;
- every one of those 70 has strictly positive constant term;
- the minimum constant over those regular orbits is `2`;
- the minimum positive Newton coefficient is `1/8`.

Hence those 70 orbit families are strictly positive on all `Z_{>=0}^2`.

Unlike the independent-terminal NM13-08 theorem, there is **no zero-constant orbit** here: the triangle seed removes the degenerate equality that occurs for the independent-terminal tree `K_{3,1}`.

## 7. The two failed Newton orbits and exact two-corner repairs

The hoped-for global positive-Newton proof fails exactly on the same two geometric `P5` spoke types found independently by NM13-08:

1. same `P5` block, path vertices `0` and `3`, different terminal labels;
2. same `P5` block, path vertices `0` and `4`, different terminal labels.

Each has four negative Newton coefficients. This is a genuine failed proof route; it is not hidden by the final theorem.

We use the elementary two-corner lattice sign lemma: if `Q(A+X,Z)` and `Q(X,B+Z)` have all ordinary monomial coefficients strictly positive, and `Q(i,j)>0` throughout the finite rectangle `0<=i<A, 0<=j<B`, then `Q(x,z)>0` for every nonnegative integer pair. The proof is immediate by partitioning the quadrant into the two shifted orthants and the residual finite rectangle.

### 7.1 Distance-three spoke pair

After clearing the positive denominator `143995537952`, the exceptional polynomial is

\[
\begin{aligned}
Q_3(x,z)={}&818384192982225x^4+613936295387100x^3z-6680618850205290x^3\\
&+172711260505350x^2z^2-3760871918836830x^2z+472121532149046985x^2\\
&+21594118499100xz^3-705730682854470xz^2+177096948051227610xz\\
&+2179001633540253760x+1012468626225z^4-44143632103410z^3\\
&+16607657871785505z^2+410195769097723840z+2456535078353529600.
\end{aligned}
\]

Exact arithmetic gives:

- `Q_3(3+X,Z)` has all 15 monomial coefficients positive, minimum `1012468626225`;
- `Q_3(X,11+Z)` has all 15 monomial coefficients positive, minimum `404987450490`;
- all `3*11=33` residual lattice values are positive, minimum `2456535078353529600` at `(0,0)`.

Therefore `Q_3(x,z)>0` on `Z_{>=0}^2`.

### 7.2 Opposite-endpoint spoke pair

After clearing the positive denominator `71997768976`, the second exceptional polynomial is

\[
\begin{aligned}
Q_4(x,z)={}&32735367719289x^4+24557451815484x^3z-1108726769552130x^3\\
&+6908450420214x^2z^2-623894012218806x^2z+266247230476283529x^2\\
&+863764739964xz^3-117024242582478xz^2+99868244443222122xz\\
&+1172761363232424896x+40498745049z^4-7316773272186z^3\\
&+9365042301644785z^2+220693897268905088z+1297745962220756608.
\end{aligned}
\]

Exact arithmetic gives:

- `Q_4(9+X,Z)` has all 15 monomial coefficients positive, minimum `40498745049`;
- `Q_4(X,46+Z)` has all 15 monomial coefficients positive, minimum `40498745049`;
- all `9*46=414` residual lattice values are positive, minimum `1297745962220756608` at `(0,0)`.

Therefore `Q_4(x,z)>0` on `Z_{>=0}^2`.

Together with the 70 Newton-positive orbits, this proves `T07-TRIANGLE-RIGHT-P5-PNC-13` for every `p,r>=0`.

The finite computation is a complete classification of finitely many **local response types** plus finite exact lattice certificates for two quartics. It is not finite graph-order extrapolation.

## 8. Independent physical brute check

As an implementation-independent sanity check of the transfer construction, the executable directly enumerates all `2^22` edge subsets of the smallest genuinely new graph

\[
K_3\vee P_5.
\]

It obtains

\[
|V|=8,\qquad |E|=22,\qquad I_G(\mathbf1)=102348,
\]

and over all physical edge pairs

\[
\min\Delta=1003968,
\qquad
\max\Delta=299891200.
\]

This brute force is only a cross-check; the all-parameter theorem is supplied by the orbit reduction and exact polynomial sign certificates above.

## 9. Essential exact artifacts

Executed before this report:

- `2026-09-20T07-18-55Z__triangle_p5_checker.py`, creation commit `c52dacfb375f19bb1f0280855a0c866f780ebe04`, local SHA-256 `d16bf3b38d8215c7c346f25b53daa8ec555e009eacb842563d09ab8c30a166a0`;
- `2026-09-20T07-18-55Z__triangle_p5_checker.out`, creation commit `25363cd092933522a7f77def6c90e91587c4e568`, local SHA-256 `dce9a5695da1d807b69ec2b8ceaf3e45a6fade802f45304aea49edcc67c43bc3`.

The archived execution ends `ALL_EXACT_CHECKS_PASS`.

## 10. Residual obstruction, failure accounting, and next attack

The parent conjecture remains open. This class still has a dominating triangle and a right graph whose nontrivial components are all `P5`; arbitrary 3-connected response environments are not controlled.

The failed proof mechanism this run is exact and localized: coefficientwise Newton positivity fails on two marked `P5` spoke orbits. The failure is repaired by the two-corner lemma, so this is a substantive theorem run rather than an unchanged recovery attempt.

The next complementary attack is the **mixed triangle-seeded `P5/P4/P3/K2/K1` family**. The unmarked transfers all lie in `span{I,N,N^2}`. The decisive question is whether the two `P5` exceptional quartics remain positive after adding the four lower-layer directions. The first route will use the current two-corner certificates as outer `P5/K1` controls and test shifted positivity in the lower-layer variables; if that fails, the first exact negative parameter tuple becomes a source-valid counterexample template to investigate rather than another positivity certificate.

## ledger_delta

```yaml
track: NM13-04
parent: T07_uniform_forest_pairwise_negative_edge_correlation
parent_status_before: OPEN
parent_status_after: OPEN
source_metric: largest_completely_certified_all_simple_graph_order
metric_before: 9
metric_after: 9
counterexample_order_lower_bound_before: 10
counterexample_order_lower_bound_after: 10
mechanism_before: "K3 join arbitrary right linear forest with component order <=4"
mechanism_after: "strict p-NC for K3 join (p P5 disjoint_union r K1), all p,r>=0"
new_claim: T07-TRIANGLE-RIGHT-P5-PNC-13
claim_status: CANDIDATE_FULL_RESTRICTED_PENDING_INDEPENDENT_REVIEW
local_edge_pair_orbits: 72
newton_positive_orbits: 70
exceptional_orbits: 2
exception_certificates:
  distance3: "two-corner shifts (3,0),(0,11) plus 33 exact lattice points"
  distance4: "two-corner shifts (9,0),(0,46) plus 414 exact lattice points"
physical_brute_check: "K3 join P5: 2^22 subsets, Z=102348, min_delta=1003968"
checker_commit: c52dacfb375f19bb1f0280855a0c866f780ebe04
output_commit: 25363cd092933522a7f77def6c90e91587c4e568
failed_route: "global coefficientwise Newton positivity; exactly two P5 spoke-pair orbits have negative Newton coefficients"
next_attack: "mixed triangle-seeded P5/P4/P3/K2/K1 sign cone or exact negative tuple"
literature_scope_date: 2026-09-20
novelty_status: UNVERIFIED_BOUNDED_NEGATIVE_SEARCH_ONLY
```

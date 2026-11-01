Model actually run: **GPT-5.6 Sol** (system model metadata). Reasoning-effort setting: **UNVERIFIED**.

# NM13-04 / T07 — triangle-seeded mixed-spider sign theorem

Status: **PARTIAL on the parent Grimmett–Winkler conjecture / CANDIDATE_FULL for the restricted theorem below, pending later independent review.** Novelty/priority: **UNVERIFIED**. The arbitrary-finite-graph uniform-all-forests conjecture remains OPEN.

Repository / branch: private `yspennstate/math-open-problems` / `master`  
Assigned root: `proofnet24/NM13-04/progress-forest/`  
Companion: NM13-08, `proofnet24/NM13-08/progress-forest-structure/`

## 0. Short handoff and substantive move

The preceding NM13-04 run proved strict p-NC for `K3 vee H` when `H` is an arbitrary finite star forest `bigsqcup K_{1,m_j}` with both the number of components and every star size unbounded. The surviving gap recorded there was branching depth two and, more generally, cross-component marked responses outside the star class.

The newest complementary NM13-08 report executes the branching-depth-two decomposition for a right **mixed spider**. For the tree `D_{p,q}` having one center, `p` direct legs of length one, and `q` subdivided legs of length two, NM13-08 constructs two commuting 15-state tail operators, proves a seven-dimensional nilpotent algebra, and obtains closed all-`p,q` marked transfers under three independent terminals.

This run changes the left boundary condition to the triangle seed `q=(1,1,1,1,3)` and proves a new triangle-seeded all-parameter theorem for one arbitrary mixed spider together with arbitrarily many isolated right vertices. This is a genuine branching-depth-two family: `D_{2,1}` already has a degree-three branch vertex and one subdivided arm, while `p,q` are both unbounded.

The current LIVE20 policy, the latest own report, the newest NM13-08 mixed-spider report, and POSTED continuity were recovered before the new calculation. No historical or peer artifact was overwritten. No public posting, email, Drive, paid compute, workflow execution, access/permission or schedule change was performed.

## 1. Parent problem before/after, separately from mechanism gain

For a finite graph `G=(V,E)`, write

\[
I_G(\mathbf y)=\sum_{F\subseteq E:\,F\text{ acyclic}}\prod_{e\in F}y_e,
\qquad
\Delta_G(e,f)=I_eI_f-I_GI_{ef}.
\]

At unit weights, `Delta_G(e,f)>=0` is exactly pairwise negative correlation of the distinct edge indicators under the uniform law on **all** spanning forests.

**Parent source status:** `OPEN -> OPEN`.  
**Largest completely certified all-simple-graph order in repository continuity:** `9 -> 9`.  
**Equivalent source-valid lower bound on a counterexample order:** `>=10 -> >=10`.

No finite census is promoted to a general theorem.

**Mechanism before:** triangle-seeded arbitrary star forests, plus the separate finite atom library `P1,...,P15,C3,C4,K4` with arbitrary multiplicities.

**Mechanism after:** an exact two-parameter branching atom `D_{p,q}` with both direct and subdivided arms unbounded, under the triangle seed, and a three-parameter strict sign theorem for

\[
G_{p,q,r}=K_3\vee(D_{p,q}\sqcup rK_1),\qquad p,q,r\ge0.
\]

The graph has

\[
|V(G_{p,q,r})|=4+p+2q+r,
\qquad
|E(G_{p,q,r})|=6+4p+8q+3r.
\]

Every member is 3-connected: deleting fewer than three vertices leaves at least one triangle vertex, adjacent to every surviving right vertex. Every member contains `K4`, hence is not series-parallel. Once the right side has at least three vertices it contains `K_{3,3}`.

## 2. Preserved P14 proof state and failed routes

The inherited P14 boundary is unchanged and was not rerun from scratch.

1. Grimmett–Winkler plus the repository dense-nine complement certify all simple graphs through nine vertices at unit all-forest weights.
2. Forest factorization over blocks reduces a vertex-minimal counterexample to a 2-connected graph.
3. P14's two-separator transfer, together with the recovered fixed-graph unit-to-positive-weight implication, reduces a vertex-minimal counterexample further to a **3-connected** graph.
4. The generic degree-three apex / star-mesh route leaves a mixed three-terminal polarization without a universal sign.
5. Universal positivity of that mixed term is false.
6. The proposed reverse-Cauchy sufficient condition was exactly refuted on a physical six-vertex apex graph even though the actual Rayleigh gap there stayed positive.
7. Naive stability, Lorentzian / complete-log-concavity, and Gårding shortcuts still lack the required hypothesis for arbitrary graphic independence polynomials.

The theorem below enlarges the positive 3-connected region; it does not remove the arbitrary 3-connected obstruction.

## 3. Fresh source-scope check

A bounded 20 September 2026 literature check still separates the exact target from neighboring results.

- Grimmett–Winkler, `arXiv:math/0302185` / Random Structures & Algorithms 24 (2004), formulate the edge-correlation conjecture for the uniform law on **all forests** and report verification for every graph on at most eight vertices and every nine-vertex graph with at most eighteen edges. They explicitly distinguish the already-known uniform-spanning-tree law.
- Erickson, `arXiv:1008.3660`, proves the stronger positive-weight independent-set-Rayleigh / sum-of-squares theorem for **series-parallel** graphs.
- Huang, `arXiv:2311.00965`, still describes negative correlation for arboreal gas as open in general while proving special graph cases.
- Tang–Zhang, `arXiv:2603.10738` (submitted 11 March 2026), prove p-NC for specified spanning-subgraph ensembles of the complete graph, including forests with exactly `k` components for fixed `k` and sufficiently large `n`; this is not the arbitrary-graph law mixing all forest component counts.
- Bado, DOI `10.1016/j.spl.2026.110960`, proves strict unit p-NC for wheel graphs, another infinite 3-connected non-series-parallel family.

A bounded search did not surface the exact triangle-join mixed-spider theorem below. That is negative evidence only; novelty remains **UNVERIFIED**.

## 4. NM13-08 two-tail algebra, reconstructed with exact checks

Let `D_{p,q}` have center `c`, direct leaves `d_1,...,d_p` with edges `cd_i`, and subdivided legs `c-b_j-x_j`, `1<=j<=q`.

Retain the three terminals and the center. There are 15 frontier partitions. A direct-leg step gives a matrix `L`, a subdivided-leg step gives a matrix `B`, and

\[
J=L-5I,\qquad K=B-28I.
\]

The checker independently reconstructs the partition transitions and verifies exactly

\[
J^4=K^4=0,\qquad JK=KJ,
\]

\[
JK^2=\frac{31}{270}K^3,
\qquad
J^2K=\frac{76}{6075}K^3,
\qquad
J^3=\frac{8}{6075}K^3,
\]

and that the algebra generated by `J,K` has dimension seven with basis

\[
I,K,K^2,K^3,J,JK,J^2.
\]

Consequently every unmarked, one-marked and two-marked mixed-spider transfer, after removal of the positive factor `5^p 28^q`, is a bounded-degree polynomial in `(p,q)`. This is an exact all-parameter transfer, not interpolation from finitely many spider sizes.

For the unmarked atom the normalized five-state terminal transfer is

\[
T_{p,q}=A_{p,q}I+B_{p,q}N+C_{p,q}N^2,
\qquad N^3=0,
\]

with

\[
A_{p,q}=\frac{42p+45q+280}{70},
\]

\[
B_{p,q}=\frac{1568p^2+4830pq+12152p+3375q^2+22875q+9800}{9800},
\]

and

\[
C_{p,q}=\frac{1}{8232000}\bigl(
175616p^3+893760p^2q+1393952p^2+1464750pq^2
\]

\[
\qquad\qquad +5403090pq+1174432p+759375q^3+5229375q^2+2341250q
\bigr).
\]

Writing `a=B/A`, `c=C/A` and

\[
\rho_{p,q}=\frac{a^2/2-c}{a},
\]

the exact formula is

\[
\rho_{p,q}=\frac{R(p,q)}{840D(p,q)},
\]

where

\[
D(p,q)=(42p+45q+280)
(1568p^2+4830pq+12152p+3375q^2+22875q+9800)
\]

and

\[
\begin{aligned}
R(p,q)={}&6607552p^3+27462540p^2q+95579008p^2+36092700pq^2\\
&+287818860pq+385696640p+15271875q^3+198665625q^2\\
&+689500000q+288120000.
\end{aligned}
\]

The checker verifies the two exact differences

\[
\rho_{p,q}-\frac{43}{360}
=\frac{
8820p^2q+96040p^2+18900pq^2+259959pq+902776p
+10125q^3+171000q^2+785400q+3841600
}{252D(p,q)}>0,
\]

and

\[
\frac18-\rho_{p,q}
=\frac{
153664p^3+623280p^2q+2055256p^2+806400pq^2+6240045pq
+7395080p+337500q^3+4321875q^2+14665000q
}{420D(p,q)}\ge0.
\]

Thus

\[
\boxed{\frac{43}{360}<\rho_{p,q}\le\frac18.}
\]

The upper equality occurs only at `p=q=0`, when the atom is a single isolated right vertex.

## 5. Response strip and the two cases for marked pairs

For normalized terminal-symmetric transfers

\[
\widehat T_i=I+a_iN+c_iN^2,
\]

nilpotence gives, for their product `U=I+uN+vN^2`,

\[
\frac{u^2}{2}-v=\sum_i\rho_i a_i.
\]

Hence, when `u>0`,

\[
v=\frac{u^2}{2}-hu,
\qquad
h=\frac{\sum_i\rho_i a_i}{\sum_i a_i}.
\]

One isolated right vertex has normalized transfer `I+(1/4)N` and response `rho=1/8`.

This creates two exact marked-pair regimes.

**Regime A: the mixed spider is unmarked.** This occurs for core/core, core/singleton, same-singleton, and distinct-singleton pairs. The unmarked product still contains `D_{p,q}` and any remaining singletons, so

\[
\frac{43}{360}\le h\le\frac18.
\]

**Regime B: at least one marked edge lies in the mixed spider.** Expose the whole mixed spider. Every remaining unmarked component is a singleton, so exactly

\[
h=\frac18.
\]

If no singleton remains then `u=0`, and the same substitution is harmless. In fact the proof below certifies all real `u>=0`, stronger than the discrete physical values `u=r/4`.

The triangle seed is

\[
\boxed{q=(1,1,1,1,3)}.
\]

Conditional triangle seeds for one or two required core edges are generated directly by the checker from the three acyclic triangle subsets, rather than hard-coded.

After exposing every component touched by a marked pair, each of the four counts `I,I_e,I_f,I_ef` is affine in `(u,v)`. Therefore the normalized Rayleigh numerator is a quadratic `Q(u,v)`. After substituting `v=u^2/2-hu`, it is a quartic

\[
R(u,h)=\sum_{j=0}^4 c_j(h)u^j.
\]

## 6. Exhaustive symbolic local schemes

The marked classification is finite at the **local response-type** level while `p,q,r` remain symbolic and unbounded.

For the mixed spider the edge types are: center-to-terminal spokes `c`; direct-leg internal edges `di` and terminal spokes `ds`; subdivided-leg internal edges `i1,i2` and terminal spokes `b,x`.

Using simultaneous terminal `S_3`, direct-leg permutations, subdivided-leg permutations, singleton-component exchange where relevant, and unordered exchange of the marked pair, the checker finds exactly:

- 48 same-mixed-spider schemes;
- 11 mixed-spider / singleton schemes;
- 11 core-edge / mixed-spider schemes;
- 2 core-edge / singleton schemes;
- 1 core/core scheme;
- 1 two-spokes-in-one-singleton scheme;
- 2 distinct-singleton schemes, according as the two spokes use the same or different terminal.

Total:

\[
\boxed{76\text{ exhaustive symbolic schemes}.}
\]

The orbit generation is performed from a witness with two direct and two subdivided legs only to represent local incidence patterns; the transfer entries themselves remain symbolic polynomials in arbitrary `p,q`. Thus this is not finite coverage in spider size.

## 7. Exact sign certificate

### 7.1 Regular schemes

When the mixed spider is exposed, set `h=1/8`. For each physical scheme with minimum required arm counts `(p_0,q_0)`, substitute

\[
p=p_0+X,\qquad q=q_0+Y,
\qquad X,Y\ge0.
\]

For every quartic coefficient `c_j(1/8;p,q)`, clear its positive rational denominator. The checker verifies that every resulting monomial coefficient in `(X,Y)` is nonnegative, and verifies a strictly positive constant term. This closes

- 45 of the 48 same-spider schemes;
- all 11 spider/singleton schemes;
- all 11 core/spider schemes.

When the mixed spider remains unmarked, the checker instead expands each quadratic coefficient `c_j(h)` in the degree-two Bernstein basis on `[43/360,1/8]`. All Bernstein coefficients are nonnegative for all six universal core/singleton sectors. Their strict constants at the physical minima are `44, 6, 2, 44, 346, 148`.

Thus 73 of the 76 schemes are coefficientwise positive certificates.

### 7.2 Three exact discriminant repairs

Exactly three same-spider schemes leave the positive monomial cone at `h=1/8`. In each case write

\[
R(u)=c_4u^4+c_3u^3+c_2u^2+c_1u+c_0
=u^2(c_4u^2+c_3u+c_2)+c_1u+c_0.
\]

The checker proves coefficientwise that `c_4>0`, `c_1>=0`, and `c_0>0`, and proves

\[
\mathcal D=4c_4c_2-c_3^2>0.
\]

The three exact margins are

\[
\mathcal D_{ds,x}
=\frac{27}{29412250000}
(586236p^2+1237600pq+8006348p+660375q^2+8448400q+27783766),
\]

for a direct-leaf spoke and an `x`-spoke on a subdivided leg, with `p>=1,q>=1`;

\[
\mathcal D_{b,x}
=\frac{9}{578509309952}
(27440196p^2+57947820pq+372904840p+30862350q^2+393618225q+1284376950),
\]

for a `b`-spoke and an `x`-spoke on two distinct subdivided legs, with `q>=2`; and

\[
\mathcal D_{x,x}
=\frac{27}{3615683187200}
(5244372p^2+11197760pq+70282688p+5980950q^2+75025475q+235939650),
\]

for `x`-spokes on two distinct subdivided legs, again with `q>=2`.

Each displayed polynomial has strictly positive coefficients. Hence the quadratic `c_4u^2+c_3u+c_2` has negative discriminant and positive leading coefficient, so it is positive for every real `u`. Together with `c_1u+c_0>0` for `u>=0`, each exceptional quartic is strictly positive.

The exact execution summary is therefore

\[
\boxed{76\text{ schemes}:\ 73\text{ regular},\ 3\text{ discriminant},\ 0\text{ failures}.}
\]

## 8. New restricted theorem

### Theorem `T07-TRIANGLE-MIXED-SPIDER-26`

Let `p,q,r` be arbitrary nonnegative integers. Let `D_{p,q}` be the mixed spider with one center, `p` direct legs of length one, and `q` legs of length two. Put

\[
G_{p,q,r}=K_3\vee(D_{p,q}\sqcup rK_1).
\]

Then for every two distinct present edges `e,f` of `G_{p,q,r}`,

\[
\boxed{\Delta_{G_{p,q,r}}(e,f)>0.}
\]

Equivalently, under the uniform probability measure on **all** acyclic spanning edge subsets of `G_{p,q,r}`, every pair of distinct edge indicators is strictly negatively correlated.

### Proof

The two-tail algebra of Section 4 gives exact normalized marked transfers polynomial in arbitrary `p,q`, and places the unmarked mixed-spider response in `(43/360,1/8]`.

If neither marked edge lies in the mixed spider, expose the marked core/singleton pieces. The unmarked mixed spider and remaining singletons collapse into `U=I+uN+vN^2` with `h in [43/360,1/8]`. Section 7.1 proves the six possible local schemes strictly positive throughout that entire strip.

If at least one marked edge lies in the mixed spider, expose the spider. The only unmarked components left are isolated vertices, so `h=1/8`; `u>=0`. Section 6 reduces the local pair to one of 70 symbolic schemes, and Section 7 proves all 70 strictly positive: 67 coefficientwise and three by the exact discriminant argument.

All removed normalization factors are positive powers of `5` and `28` together with positive identity coefficients of unmarked singleton transfers. Restoring them cannot change the sign. Therefore `Delta_G(e,f)>0` for every distinct present pair. QED.

This is an all-parameter theorem because `p,q,r` are arbitrary and unbounded. It is not finite graph-size enumeration.

## 9. Independent finite sanity check

The theorem is symbolic; finite enumeration is used only as a sanity check.

A separate C++ union-find enumerator checks all `2^22` edge subsets of the first small genuinely branching example

\[
K_3\vee D_{2,1},
\]

which has eight vertices and 22 edges. It obtains

\[
|\mathcal F|=100962,
\qquad
\min_{e\ne f}\Delta(e,f)=4686984,
\qquad
\max_{e\ne f}\Delta(e,f)=291383224.
\]

The brute-force program ends `BRUTE_FORCE_PASS`. This graph lies inside the repository's complete order-nine coverage, so the calculation is explicitly only an implementation cross-check, not evidence for a general theorem.

The symbolic executable ends `ALL_EXACT_CHECKS_PASS`.

## 10. Failure accounting and unresolved scope

No physical sign failure was found in the proved class. The three same-spider coefficient-cone failures were repaired exactly by discriminants and are not hidden.

A broader attempted extension to an **arbitrary forest of mixed-spider components** was started. The unmarked response part is already compatible, because every `D_{p,q}` lies in the same strip. The new obstacle is a marked pair living in two distinct mixed-spider components. Terminal symmetry leaves 65 oriented cross-component local schemes with four independent size parameters. A direct four-variable full-strip expansion exceeded the bounded execution window before exhaustive coverage. Because that calculation was incomplete, it is not used here and **no theorem for arbitrary mixed-spider forests is claimed**.

The next materially different method should therefore avoid brute four-parameter expansion: derive a factorized cross-component marked-transfer cone or a small PSD/discriminant criterion from the seven-dimensional commuting algebra. A complete positive cone would immediately promote the present one-spider result to arbitrary mixed-spider forests; a first exact cone violation would provide a sharply localized counterexample-search template.

The parent conjecture also remains open because the whole argument still uses a special three-terminal join geometry and does not repair P14's arbitrary 3-connected mixed-polarization obstruction.

## 11. Executed artifacts

Exact symbolic checker:

`proofnet24/NM13-04/progress-forest/runs/2026-09-20/2026-09-20T14-28-06Z__triangle-mixed-spider-checker.py`

- commit: `ff52f8651332055bffbeee3c1733110db721ff33`
- blob: `dc3dc3eeceba3d1cf46f3fac02546b07cbe17e19`

Independent finite sanity checker:

`proofnet24/NM13-04/progress-forest/runs/2026-09-20/2026-09-20T14-28-06Z__triangle-mixed-spider-bruteforce.cpp`

- commit: `423b25632032c4df28f04be3ccbb670fad530231`
- blob: `74b07cd30f3d12da130aee67fa6e8cc11292f5e6`

Archived executed output:

`proofnet24/NM13-04/progress-forest/runs/2026-09-20/2026-09-20T14-28-06Z__triangle-mixed-spider-checker.out`

- commit: `5b4603736f413179f50f6b3533c44204cca933ca`
- blob: `94f0cd4749eeb7d8f5bfd10930bcaf4623ab5a9a`

No historical or peer file was modified.

## 12. ledger_delta

```yaml
ledger_delta:
  task: T07
  owner: NM13-04
  parent_problem: pairwise_negative_edge_correlation_uniform_all_forests_every_finite_graph
  parent_status_before: OPEN
  parent_status_after: OPEN
  complete_all_simple_graph_order_before: 9
  complete_all_simple_graph_order_after: 9
  source_valid_counterexample_order_lower_bound_before: 10
  source_valid_counterexample_order_lower_bound_after: 10
  predecessor_mechanism:
    triangle_seeded_arbitrary_star_forests: true
    triangle_seeded_atom_library: [P1_to_P15, C3, C4, K4]
  new_mechanism:
    theorem_id: T07-TRIANGLE-MIXED-SPIDER-26
    class: K3_vee_(D_pq_disjoint_union_rK1)
    parameters: [p, q, r]
    parameter_ranges: all_nonnegative_integers
    right_atom: one_center_with_p_direct_legs_and_q_subdivided_legs
    all_parameter: true
    strict_pairwise_negative_correlation: true
    triangle_seed: [1, 1, 1, 1, 3]
    direct_tail_operator: L_equals_5I_plus_J
    subdivided_tail_operator: B_equals_28I_plus_K
    nilpotence: [J4_equals_0, K4_equals_0]
    commuting: true
    tail_algebra_dimension: 7
    response_strip: [43/360, 1/8]
    local_symbolic_schemes: 76
    regular_schemes: 73
    discriminant_repairs: 3
    sign_failures: 0
  finite_sanity:
    graph: K3_vee_D_2_1
    vertices: 8
    edges: 22
    forest_count: 100962
    min_gap: 4686984
    max_gap: 291383224
    role: sanity_only_not_general_coverage
  unresolved:
    arbitrary_mixed_spider_forest_cross_component_marked_sector: true
    cross_component_oriented_schemes: 65
    direct_four_parameter_expansion: incomplete_due_bounded_runtime
    arbitrary_3_connected_parent_obstruction: open
  restricted_theorem_status: CANDIDATE_FULL_PENDING_INDEPENDENT_REVIEW
  novelty_priority: UNVERIFIED
  runtime_model: GPT-5.6_Sol
  reasoning_effort: UNVERIFIED
  posted_publicly: false
  history_overwritten: false
  peer_artifact_overwritten: false
```

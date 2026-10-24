Model actually run: **GPT-5.6 Sol** (system model metadata). Reasoning-effort setting: **UNVERIFIED**.

# NM13-04 / T07 — triangle-seeded arbitrary-star-forest sign theorem

Status: **PARTIAL on the parent Grimmett–Winkler conjecture / CANDIDATE_FULL for the restricted theorem below, pending later independent review.** Novelty/priority: **UNVERIFIED**. The arbitrary-finite-graph uniform-all-forests conjecture remains OPEN.

Repository / branch: private `yspennstate/math-open-problems` / `master`  
Assigned root: `proofnet24/NM13-04/progress-forest/`  
Companion: NM13-08, `proofnet24/NM13-08/progress-forest-structure/`

## 0. Short handoff and substantive move

The preceding NM13-04 run proved strict pairwise negative edge correlation for `K3 vee H` when `H` is an arbitrary disjoint union of `P1,...,P15,C3,C4,K4` components, with every multiplicity unbounded. Its mechanism was a five-state triangle-seeded response strip.

The newest complementary NM13-08 report then changed geometry completely: for a right star `S_m=K_{1,m}` it retained the three terminals and the star center, obtained a 15-state leaf-transfer `L` with `(L-5I)^4=0`, and proved an independent-terminal arbitrary-star-forest theorem. I use that nilpotent star-tail algebra with the **different left seed given by the triangle**. This is not another finite path/cycle cutoff: the star size `m` is symbolic and unbounded.

The new result below proves p-NC for `K3` joined to an arbitrary finite star forest with arbitrary component sizes. It is a new unbounded-degree, no-component-size-cutoff family in the surviving 3-connected region.

The current LIVE20 policy, `POSTED.md` continuity, the latest own report, and the latest NM13-08 star report were recovered before the calculation. No historical or peer artifact is overwritten; no public posting, email, Drive, paid compute, workflow, access/permission or schedule change is performed.

## 1. Parent problem before/after, separately from mechanism gain

For a finite graph `G=(V,E)`, let

\[
I_G(\mathbf y)=\sum_{F\subseteq E:\,F\text{ acyclic}}\prod_{e\in F}y_e,
\qquad
\Delta_G(e,f)=I_eI_f-I_GI_{ef}.
\]

At unit weights, `Delta_G(e,f)>=0` is exactly pairwise negative correlation of distinct edge indicators under the uniform law on **all** spanning forests.

**Parent source status:** `OPEN -> OPEN`.  
**Largest completely certified all-simple-graph order in repository continuity:** `9 -> 9`.  
**Equivalent source-valid lower bound on a counterexample order:** `>=10 -> >=10`.

No finite census is promoted to a general theorem.

**Mechanism before:** a finite atom library `P1,...,P15,C3,C4,K4` with arbitrary multiplicities under the triangle seed.

**Mechanism after:** an **infinite atom family** `S_m=K_{1,m}`, `m>=0`, with arbitrary sizes and arbitrary numbers of star components under the triangle seed.

Concretely, if

\[
H=\bigsqcup_{j=1}^r S_{m_j},\qquad r\ge0,\quad m_j\ge0,
\]

then the theorem below proves strict p-NC for `G=K3 vee H` for every choice of the entire finite sequence `(m_1,...,m_r)`.

Whenever `H` is nonempty, `G` is 3-connected: deleting fewer than three vertices leaves at least one of the three left-clique vertices, which is adjacent to every surviving right vertex. It also contains `K4` as a subgraph, so it is not series-parallel. If `H` has at least three vertices then `G` contains `K_{3,3}`.

## 2. Preserved P14 proof state and failed routes

The inherited P14 boundary remains unchanged.

1. Grimmett–Winkler plus the repository dense-nine completion cover every simple graph through nine vertices in the unit all-forest scope.
2. Forest factorization over blocks reduces a vertex-minimal counterexample to a 2-connected graph.
3. P14's two-separator transfer, together with the recovered fixed-graph unit-to-positive-weight implication, reduces it further to a **3-connected** graph.
4. The generic degree-three apex / star-mesh route leaves a mixed three-terminal polarization with no universal sign.
5. Universal positivity of that mixed term is false.
6. The proposed reverse-Cauchy sufficient condition was exactly refuted on a physical six-vertex apex graph although the actual Rayleigh gap there remained positive.
7. Naive stability, Lorentzian / complete-log-concavity, and Gårding shortcuts still lack the required hypothesis for arbitrary graphic independence polynomials.

The present theorem enlarges the positive 3-connected region. It does not remove the arbitrary 3-connected obstruction.

## 3. Fresh source-scope check

A bounded 20 September 2026 literature check still separates the exact target from neighboring results.

- Grimmett–Winkler, `arXiv:math/0302185` / RSA 24 (2004), formulate the edge-correlation conjecture for the uniform law on **all forests** and report verification for every graph on at most eight vertices and every nine-vertex graph with at most eighteen edges. They explicitly distinguish the already-known uniform-spanning-tree law.
- Erickson, `arXiv:1008.3660`, proves the stronger positive-weight independent-set-Rayleigh / sum-of-squares theorem for **series-parallel** graphs.
- Huang, `arXiv:2311.00965`, still describes negative correlation for arboreal gas as open in general while proving special graph cases.
- Tang–Zhang, `arXiv:2603.10738` (submitted 11 March 2026), prove p-NC for specified spanning-subgraph ensembles of the complete graph, including forests with exactly `k` components for fixed `k` and sufficiently large `n`; this is not the arbitrary-graph law mixing all forest component counts.
- Bado, DOI `10.1016/j.spl.2026.110960`, proves strict unit p-NC for wheel graphs, another infinite 3-connected non-series-parallel family.

A bounded search did not surface the exact triangle-join arbitrary-star-forest theorem below. That is only negative evidence; novelty remains **UNVERIFIED**.

## 4. NM13-08 star-tail decomposition, reconstructed here

Use the five partitions of the three terminals. One isolated right vertex has transfer

\[
S=4I+N,\qquad N^3=0.
\]

For `S_m=K_{1,m}`, keep the star center together with the three terminals while inserting leaves. The frontier has the Bell number `B_4=15` states. Let `L` be the exact unmarked one-leaf transfer and put `J=L-5I`. The checker reconstructs the transitions from acyclicity and verifies

\[
J^4=0,
\qquad
(\operatorname{rank}J,\operatorname{rank}J^2,\operatorname{rank}J^3,\operatorname{rank}J^4)
=(8,2,1,0).
\]

Therefore

\[
5^{-r}L^r
=I+\frac r5J+\frac{\binom r2}{25}J^2+\frac{\binom r3}{125}J^3.
\]

The same formula applies after exposing the at most two leaves touched by a marked edge pair. Thus every unmarked, one-marked and two-marked star transfer, after removal of the positive factor `5^m`, is polynomial in the star size.

Exact multiplication gives the unmarked normalized transfer

\[
5^{-m}T_m=A_mI+B_mN+C_mN^2
\]

with

\[
A_m=\frac{3m+20}{5},\qquad
B_m=\frac{4m^2+31m+25}{25},\qquad
C_m=\frac{m(16m^2+127m+107)}{750}.
\]

Writing `a_m=B_m/A_m`, `c_m=C_m/A_m`, define

\[
\rho_m=\frac{a_m^2/2-c_m}{a_m}.
\]

The exact expression is

\[
\rho_m=
\frac{43m^3+622m^2+2510m+1875}
{30(3m+20)(4m^2+31m+25)}.
\]

The two factorizations inherited from NM13-08 are

\[
\rho_m-\frac{43}{360}
=\frac{5m^2+47m+200}{72(3m+20)(4m^2+31m+25)}>0,
\]

and

\[
\frac18-\rho_m
=\frac{m(8m^2+107m+385)}{120(3m+20)(4m^2+31m+25)}\ge0.
\]

Hence every finite star lies in the common strip

\[
\boxed{\frac{43}{360}<\rho_m\le\frac18}.
\]

For any finite product of normalized unmarked star transfers,

\[
U=I+uN+vN^2,
\]

nilpotence gives

\[
\frac{u^2}{2}-v=\sum_j \rho_{m_j}a_{m_j}.
\]

Thus either `u=0`, or

\[
\boxed{
v=\frac{u^2}{2}-hu,
\qquad
\frac{43}{360}\le h\le\frac18,
}
\]

where `h` is a positive weighted average of the star responses.

## 5. Triangle seed and exhaustive symbolic marked schemes

The left `K3` is not three independent terminals. Enumerating its acyclic edge subsets gives the exact seed row

\[
\boxed{q=(1,1,1,1,3)}
\]

in the five terminal-partition states.

Fix two distinct present edges `e,f`. They meet at most two right star components. Expose those components and leave every other right component unmarked, compressed into the common `U=I+uN+vN^2` above. Each of the four counts `I,I_e,I_f,I_ef` is affine in `(u,v)`, so the Rayleigh numerator is an exact quadratic

\[
Q_\tau(u,v;m)
\quad\text{or}\quad
Q_\tau(u,v;m,n)
\]

for a local symbolic scheme `tau`.

Under simultaneous terminal permutations, star leaf permutations and component exchange, the checker uses the following exhaustive classes:

- **1** core/core scheme;
- **5** core/star schemes: center spoke incident/opposite to the core edge, leaf spoke incident/opposite, and star-internal edge;
- **10** same-star schemes, exactly the center/leaf/internal types from NM13-08;
- **13** distinct-star oriented schemes.

Total:

\[
\boxed{29\text{ symbolic local schemes}.}
\]

The star sizes are symbolic variables; this is not a finite star-size enumeration.

## 6. Exact sign certificate on the full star strip

Substitute

\[
v=\frac{u^2}{2}-hu,
\qquad
\frac{43}{360}\le h\le\frac18.
\]

For every local scheme, write

\[
R_\tau(u,h)=\sum_{k=0}^4 c_{\tau,k}(h)u^k.
\]

Each `c_{tau,k}` has degree at most two in `h`. The checker expands it in the degree-two Bernstein basis on `[43/360,1/8]`. For size-dependent schemes it then shifts the physical size variables to their minima,

\[
m=m_0+x,\qquad n=n_0+y,
\qquad x,y\ge0,
\]

clears the positive rational denominator, and checks that **every monomial coefficient** of every Bernstein coefficient is nonnegative.

The exact result is

\[
\boxed{29\text{ regular schemes},\quad 0\text{ failures}.}
\]

No discriminant repair or finite residual rectangle is needed in the triangle-seeded star class. This is notably cleaner than the independent-terminal companion theorem, where one same-star leaf-spoke scheme leaves the positive Bernstein cone.

Strict positivity is supplied by the constant term. The checker verifies positivity at every physical size minimum; because each shifted constant polynomial has nonnegative monomial coefficients, it stays positive for all larger star sizes. The smallest displayed constants are

\[
2,\ 6,\ 42/5,\ 42/5,\ 42/5,\ 8484/625,\ldots
\]

with the global minimum `2` occurring for the core/core pair.

Restoring the removed powers of `5` and the positive identity coefficients of unmarked star transfers multiplies every Rayleigh difference by a positive factor, so the sign is unchanged.

## 7. New all-parameter theorem

### Theorem `T07-TRIANGLE-ARBITRARY-STAR-FOREST-24`

Let

\[
H=\bigsqcup_{j=1}^r K_{1,m_j}
\]

be any finite star forest, with arbitrary `r>=0` and arbitrary integers `m_j>=0`. Let

\[
G=K_3\vee H.
\]

Then for every two distinct present edges `e,f` of `G`,

\[
\boxed{\Delta_G(e,f)>0.}
\]

Equivalently, under the uniform probability measure on **all** acyclic spanning edge subsets of `G`, every pair of distinct edge indicators is strictly negatively correlated.

### Proof

Compress every unmarked star component into its normalized three-terminal transfer. Section 4 shows that their product is `U=I+uN+vN^2` with `u>=0` and, for `u>0`, `v=u^2/2-hu` with `h` in `[43/360,1/8]`; if no unmarked component remains, take `u=v=0`.

Expose the at most two right components touched by the marked edges together with any marked left-triangle edge. By Section 5 the resulting Rayleigh numerator belongs to one of the 29 symbolic local schemes. Section 6 proves its normalized numerator strictly positive throughout the full physical size ranges and the entire continuous response strip. All normalization factors are positive. Therefore `Delta_G(e,f)>0` for every distinct present pair. QED.

This is an all-parameter theorem because both the number of star components and every star size are arbitrary and unbounded.

## 8. Independent finite sanity check

The symbolic proof above is the theorem. As an independent finite sanity check, the executable directly enumerates all `2^14` edge subsets of `K3 vee S_2`, rejects cyclic subsets by union-find, and counts all 91 present-edge pairs. It obtains

\[
|\mathcal F|=2110,
\qquad
\min_{e\ne f}\Delta(e,f)=7066,
\qquad
\max_{e\ne f}\Delta(e,f)=110896.
\]

The archived execution ends

`ALL_EXACT_CHECKS_PASS`.

This finite enumeration is explicitly only a cross-check; it is not the source of the arbitrary-star theorem.

## 9. Failure accounting and residual obstruction

No local sign failure occurred in this run: all 29 triangle-seeded star schemes lie in the positive Bernstein cone on the whole star strip.

The parent conjecture remains open because the proof uses a very special three-terminal join geometry. It does not control arbitrary 3-connected graphs, and it does not repair P14's generic mixed-polarization obstruction.

I also do **not** claim the union of this star family with the preceding `P1,...,P15,C3,C4,K4` atom library. Unmarked stars fit inside the predecessor's wider strip because `43/360 > rho_K4`, but marked pairs with one star edge and one old-atom edge have not yet been exhaustively certified. That missing cross-atom sector is the clean next target.

## 10. Executed artifacts

Checker:

`proofnet24/NM13-04/progress-forest/runs/2026-09-20/2026-09-20T13-24-00Z__triangle-star-forest-checker.py`

Archived output:

`proofnet24/NM13-04/progress-forest/runs/2026-09-20/2026-09-20T13-24-00Z__triangle-star-forest-checker.out`

The checker reconstructs the 15-state leaf transfer, proves `J^4=0` and the exact unmarked star formulas, constructs required-edge marked transfers symbolically, builds the triangle seed from first principles, exhausts the 29 symmetry schemes, performs exact rational Bernstein/shifted-monomial sign checks, and executes the direct finite sanity enumeration.

## 11. Next attack

The most direct complementary continuation is a **unified strip-admissible atom theorem**. Since the predecessor library uses the strip `[rho_K4,1/8]` and every star has `rho_m>43/360>rho_K4`, the unmarked algebra already closes for arbitrary mixtures of stars with `P1,...,P15,C3,C4,K4`. The remaining work is purely marked and local:

1. re-run the 29 pure-star schemes on `[rho_K4,1/8]`;
2. certify symbolic star-vs-`P_l` cross responses uniformly in the star size and `1<=l<=15`;
3. certify symbolic star-vs-`C3,C4,K4` responses;
4. if all pass, conclude strict p-NC for `K3` joined to arbitrary mixtures of all those components.

A first exact negative cross-response would instead localize a source-valid obstruction to that proposed combined class.

## ledger_delta

```yaml
parent_problem: T07 uniform-all-forests pairwise negative edge correlation
parent_before: OPEN
parent_after: OPEN
complete_all_simple_graph_order_before: 9
complete_all_simple_graph_order_after: 9
counterexample_order_lower_bound_before: ">=10"
counterexample_order_lower_bound_after: ">=10"
restricted_status: CANDIDATE_FULL_pending_independent_review
mechanism_before: triangle-seeded finite atom library P1..P15,C3,C4,K4 with unbounded multiplicities
mechanism_after: triangle-seeded infinite star atom family S_m=K_{1,m}, arbitrary m and arbitrary component count
new_theorem: T07-TRIANGLE-ARBITRARY-STAR-FOREST-24
right_graph_class: arbitrary finite star forest
star_tail_state_count: 15
star_tail_nilpotence: "(L-5I)^4=0"
star_response_interval: "43/360 < rho_m <= 1/8"
triangle_seed: "(1,1,1,1,3)"
local_symbolic_schemes:
  core_core: 1
  core_star: 5
  same_star: 10
  distinct_star: 13
  total: 29
exact_sign_certificate:
  regular_bernstein_shifted_monomial: 29
  failures: 0
  exceptional_discriminant_repairs: 0
minimum_displayed_constant: 2
finite_sanity_check:
  graph: "K3 vee S_2"
  vertices: 6
  edges: 14
  forests: 2110
  min_gap: 7066
  max_gap: 110896
finite_sanity_is_general_theorem: false
companion_dependency: NM13-08 arbitrary-star nilpotent leaf-tail algebra and response formulas
p14_boundary: arbitrary 3-connected case remains unresolved; generic mixed-polarization route still blocked
novelty: UNVERIFIED
next_attack: symbolic star-vs-old-atom cross responses on predecessor strip [rho_K4,1/8]
checker: proofnet24/NM13-04/progress-forest/runs/2026-09-20/2026-09-20T13-24-00Z__triangle-star-forest-checker.py
output: proofnet24/NM13-04/progress-forest/runs/2026-09-20/2026-09-20T13-24-00Z__triangle-star-forest-checker.out
```

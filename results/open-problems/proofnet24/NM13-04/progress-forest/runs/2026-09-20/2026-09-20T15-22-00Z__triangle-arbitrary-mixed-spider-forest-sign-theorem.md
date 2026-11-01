Model actually run: **GPT-5.6 Sol** (system model metadata). Reasoning-effort setting: **UNVERIFIED**.

# NM13-04 / T07 — triangle-seeded arbitrary mixed-spider forest sign theorem

Status: **PARTIAL on the parent Grimmett–Winkler conjecture / CANDIDATE_FULL for the restricted theorem below, pending later independent review.** Novelty/priority: **UNVERIFIED**. The arbitrary-finite-graph uniform-all-forests conjecture remains OPEN.

Repository / branch: private `yspennstate/math-open-problems` / `master`  
Assigned root: `proofnet24/NM13-04/progress-forest/`  
Companion: NM13-08, `proofnet24/NM13-08/progress-forest-structure/`

## 0. Short handoff and substantive move

The preceding NM13-04 run proved strict p-NC for

\[
K_3\vee(D_{p,q}\sqcup rK_1),\qquad p,q,r\ge0,
\]

where `D_{p,q}` is the mixed spider with one center, `p` direct one-edge legs and `q` subdivided two-edge legs. Its explicit residual obstruction was **two marked edges in two distinct mixed-spider components**: arbitrary unmarked mixed spiders already shared the same response strip, but the cross-component marked sector had not been controlled.

The newest complementary NM13-08 report removes exactly the analogous obstruction under three **independent** terminals. It proves a commutative one-edge response algebra `C(x,z)` and an exact all-parameter cross-component certificate for arbitrary finite forests of mixed spiders.

This run changes the left boundary back to the triangle seed and does two genuinely new things in the same run:

1. it proves that all triangle-seeded same-component and core/component local responses stay positive on the **full mixed-spider strip**, not merely at the singleton endpoint `h=1/8`; and
2. it proves a seed-lift identity showing that NM13-08's four positive cross-component quantities become strictly *more* positive after replacing the independent terminal seed by the triangle seed.

Together these close every edge-pair sector for an arbitrary finite multiset of mixed spiders.

The controlling `operations/PROGRESS20_2026-09-20.md`, `POSTED.md`, the preceding NM13-04 report, and the newest NM13-08 cross-response report were read before the new calculation. No historical or peer file is overwritten. No email, Drive, public posting, paid compute, workflow execution, permission/access change, or schedule change is performed.

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

**Mechanism before:** one arbitrary triangle-seeded mixed spider plus isolated right vertices.

**Mechanism after:** arbitrary finite **mixed-spider forests** on the right, with the number of components and both leg counts in every component unbounded.

Define

\[
D_{p,q}=\text{the tree with center }c,
\text{ }p\text{ direct leaves }d_i,
\text{ and }q\text{ paths }c-b_j-x_j.
\]

The new theorem is:

### Theorem `T07-TRIANGLE-MIXED-SPIDER-FOREST-PNC-26`

Let

\[
H=\bigsqcup_{j=1}^{m}D_{p_j,q_j},
\qquad m<\infty,\quad p_j,q_j\ge0,
\]

where `D_{0,0}` is a single isolated right vertex, and put

\[
\boxed{G=K_3\vee H.}
\]

Then for every two distinct present edges `e,f`,

\[
\boxed{\Delta_G(e,f)>0.}
\]

Thus the uniform law on **all** forests of every graph in this class has strict pairwise negative edge correlation.

The exact size is

\[
|V(G)|=3+\sum_{j=1}^m(1+p_j+2q_j),
\]

\[
|E(G)|=3+\sum_{j=1}^m(3+4p_j+8q_j).
\]

Whenever `H` is nonempty, `G` is 3-connected: deletion of fewer than three vertices leaves at least one triangle vertex adjacent to every surviving right vertex, while the surviving triangle vertices connect each other. Every such graph contains `K_4`; once the right side has at least three vertices it contains `K_{3,3}`. Hence the theorem is outside Erickson's series-parallel scope.

## 2. Preserved P14 proof state and failed routes

The inherited P14 boundary is preserved rather than rerun.

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
- Tang–Zhang, `arXiv:2609.11578` (submitted 10 September 2026), prove negative correlation for the random-cluster model below one on high-degree regular graph sequences under a two-scale isoperimetric condition. Its `Q=0` endpoint is Bernoulli bond percolation conditioned to be **connected**, not the uniform all-forests law.
- Bado's wheel theorem proves the uniform-all-forests statement for wheels, another infinite 3-connected non-series-parallel family.

A bounded search did not surface the exact triangle-seeded arbitrary mixed-spider-forest theorem below. That is negative evidence only; novelty remains **UNVERIFIED**.

## 4. Shared mixed-spider response strip

The preceding exact two-tail calculation gives the normalized unmarked transfer

\[
T_{p,q}=A_{p,q}I+B_{p,q}N+C_{p,q}N^2,\qquad N^3=0,
\]

and response parameter

\[
\rho_{p,q}=\frac{(B/A)^2/2-C/A}{B/A}
\]

satisfying

\[
\boxed{\frac{43}{360}<\rho_{p,q}\le\frac18}.
\]

The upper equality occurs only at `p=q=0`, the isolated right vertex.

For any product of unmarked mixed-spider components, after positive diagonal factors are removed,

\[
U=I+uN+vN^2,
\qquad
v=\frac{u^2}{2}-hu,
\qquad
\boxed{\frac{43}{360}\le h\le\frac18}.
\tag{4.1}
\]

This is the exact weighted-average response identity. It is the only information about all *other* unmarked components needed once the component(s) touched by `e,f` are exposed.

The triangle seed in the five terminal-connectivity states is

\[
\boxed{q=(1,1,1,1,3)}.
\]

## 5. New full-strip theorem for one exposed mixed spider

The preceding NM13-04 theorem had only needed `h=1/8` when an edge in the unique mixed spider was marked, because every remaining component was a singleton. Arbitrary mixed-spider forests require the entire interval (4.1).

The new exact checker therefore re-runs the symbolic local response classification with `h` free over `[43/360,1/8]`.

### 5.1 Two marked edges in the same mixed spider

Terminal permutations, direct-leg permutations, subdivided-leg permutations and exchange of the marked pair reduce all local possibilities to exactly

\[
\boxed{48\text{ symbolic schemes}.}
\]

The witness uses two direct and two subdivided legs only to represent local incidence patterns. The actual transfer entries remain symbolic rational polynomials in arbitrary `p,q`; this is not a finite spider-size enumeration.

After exposing the marked spider, each forest count is affine in `(u,v)`, so the Rayleigh numerator is quadratic in `(u,v)`. Substituting (4.1) gives a quartic

\[
R(u,h;p,q)=\sum_{j=0}^4 c_j(h;p,q)u^j.
\]

For the physical minimum arm counts `(p_0,q_0)` of each scheme write

\[
p=p_0+X,\qquad q=q_0+Y,
\qquad X,Y\ge0.
\]

For **45/48** schemes, every `c_j` has nonnegative degree-two Bernstein coefficients in `h` on `[43/360,1/8]`, and after clearing the positive rational denominator every Bernstein coefficient is a polynomial with nonnegative monomial coefficients in `(X,Y)`. The constant coefficient is strictly positive at the physical minimum.

Exactly three schemes leave that positive cone. In each case

\[
R(u)=u^2(c_4u^2+c_3u+c_2)+c_1u+c_0,
\]

with `c_4>0`, `c_1>=0`, `c_0>0` throughout the full strip, and

\[
\mathcal D=4c_4c_2-c_3^2>0.
\]

The exact margins simplify to the same `h`-independent polynomials seen at the singleton endpoint:

\[
\mathcal D_{ds,x}
=\frac{27}{29412250000}
(586236p^2+1237600pq+8006348p+660375q^2+8448400q+27783766),
\]

\[
\mathcal D_{b,x}
=\frac{9}{578509309952}
(27440196p^2+57947820pq+372904840p+30862350q^2+393618225q+1284376950),
\]

\[
\mathcal D_{x,x}
=\frac{27}{3615683187200}
(5244372p^2+11197760pq+70282688p+5980950q^2+75025475q+235939650).
\]

All coefficients displayed are positive in their physical domains. Hence `c_4u^2+c_3u+c_2>0` for all real `u`, while `c_1u+c_0>0` for `u>=0`. Therefore every same-spider Rayleigh gap is strictly positive for every residual response in (4.1).

The executed output ends

`SAME_FINAL 45 3 0`  
`TRIANGLE_SAME_COMPONENT_FULL_STRIP_PASS`  
`ALL_EXACT_CHECKS_PASS`.

### 5.2 One triangle-core edge and one mixed-spider edge

There are exactly **11** local schemes after terminal symmetry. The same full-strip Bernstein calculation closes all of them coefficientwise:

\[
\boxed{11\text{ regular},\quad0\text{ discriminant},\quad0\text{ failures}.}
\]

The core/core sector is also full-strip regular, with strict constant `2`.

The executed output ends

`COREMIXED_FINAL 11 0 0`  
`CORECORE_FULL_STRIP_PASS`  
`ALL_EXACT_CHECKS_PASS`.

This removes the first obstruction to allowing arbitrarily many unmarked mixed spiders around a marked component.

## 6. New seed-lift lemma for two distinct marked components

The second obstruction is a pair of edges in two different mixed-spider components. Here the newest NM13-08 one-edge algebra can be transferred to the triangle seed without a new four-parameter orbit census.

For `x=(x_1,x_2,x_3)`, write `t=sum x_i` and

\[
C(x,z)=
\begin{pmatrix}
1&x_1&x_2&x_3&z\\
0&1&0&0&t-x_1\\
0&0&1&0&t-x_2\\
0&0&0&1&t-x_3\\
0&0&0&0&1
\end{pmatrix}.
\]

NM13-08 proves the commutative law

\[
C(x,z)C(y,w)=C(x+y,z+w+\kappa(x,y)),
\]

where

\[
\kappa(x,y)=(\sum x_i)(\sum y_i)-x\cdot y.
\]

Every unmarked or one-edge-required mixed-spider transfer, after a positive diagonal scalar is extracted, lies in this algebra.

Let the two unmarked exposed components be `A=C(x,z)` and `B=C(y,w)`. Requiring `e` in the first changes it to `C(x+delta,z+alpha)` and requiring `f` in the second changes it to `C(y+epsilon,w+beta)`. Define

\[
d=\sum_i\delta_i,\qquad e_0=\sum_i\epsilon_i,
\qquad k=\kappa(\delta,\epsilon).
\]

For the **independent-terminal** seed, NM13-08 writes

\[
a=d+\alpha+\kappa(\delta,y),
\qquad
b=e_0+\beta+\kappa(x,\epsilon),
\]

\[
H=1+\sum x_i+\sum y_i+z+w+\kappa(x,y),
\qquad
s=4+2\left(\sum x_i+\sum y_i\right).
\]

After the strip substitution, the cross-component gap is

\[
\Delta_{\rm ind}
=L_2u^2+L_1(h)u+C_0,
\]

with

\[
L_2=4de_0-3k,
\]

\[
L_1(h)=2ae_0+2bd-k(s-6h),
\]

\[
C_0=ab-Hk.
\]

NM13-08's exact 38-scheme certificate proves, at every physical mixed-spider parameter tuple,

\[
\boxed{k>0,\quad L_2>0,\quad L_1(h)>0,\quad C_0>0}
\]

throughout (4.1). Its coefficient proof uses the lower endpoint for `L_1`, since `L_1` is increasing in `h` when `k>0`.

Now change only the left seed to the triangle. The exact evaluation functional is

\[
q\,C(X,Z)\,\mathbf1=7+3\sum_iX_i+Z.
\tag{6.1}
\]

Also

\[
I+uN+vN^2=C((u,u,u),u+6v).
\tag{6.2}
\]

Consequently the triangle-seeded exposed-component count still has the form

\[
L_\triangle=H_\triangle+s_\triangle u+6v,
\]

but its parameters are

\[
a_\triangle=a+2d,
\qquad
b_\triangle=b+2e_0,
\]

\[
H_\triangle=H+s+2,
\qquad
s_\triangle=s+6.
\]

Substitution into the same determinant identity gives the **seed-lift relations**

\[
\boxed{L_{2,\triangle}=L_2,}
\tag{6.3}
\]

\[
\boxed{L_{1,\triangle}(h)=L_1(h)+2L_2,}
\tag{6.4}
\]

and

\[
\boxed{
C_{0,\triangle}
=C_0+L_1(h)+L_2+k(1-6h).
}
\tag{6.5}
\]

The checker verifies (6.3)--(6.5) as exact symbolic identities. Since `h<=1/8`,

\[
1-6h\ge\frac14>0.
\]

Therefore NM13-08's strict positivity immediately implies

\[
L_{2,\triangle}>0,
\qquad
L_{1,\triangle}(h)>0,
\qquad
C_{0,\triangle}>0.
\]

Hence **every pair of edges in two distinct mixed-spider components has strict triangle-seeded Rayleigh gap**. No new four-parameter atom census is needed.

This is the main mechanism gain of the run: the triangle seed is monotone-improving for the NM13-08 cross-component certificate.

## 7. Proof of Theorem `T07-TRIANGLE-MIXED-SPIDER-FOREST-PNC-26`

Fix two distinct present edges `e,f` in `G=K_3 vee H`.

**Case 1: both are triangle-core edges.** Every right component remains unmarked. Their product lies in the strip (4.1). The full-strip core/core certificate from Section 5.2 is strictly positive.

**Case 2: exactly one is a triangle-core edge.** The other lies in one mixed-spider component. Expose that component. Every remaining right component is unmarked and its product lies in (4.1). The 11 full-strip core/component schemes from Section 5.2 are strictly positive.

**Case 3: both lie in the same mixed-spider component.** Expose that component. The remaining unmarked components again lie in (4.1). Section 5.1 proves strict positivity for all 48 same-component schemes on the entire strip.

**Case 4: the edges lie in two distinct mixed-spider components.** Expose those two components. The remaining unmarked components lie in (4.1). Apply the seed-lift relations (6.3)--(6.5) to NM13-08's exact strict cross-component certificate. The resulting quadratic in `u` has strictly positive constant and nonnegative/strictly positive higher coefficients, so the Rayleigh gap is strict for all physical residual products. If the residual product is empty (`u=v=0`), choose any `h` in the strip in (6.5); the identity is independent of this choice after cancellation.

These cases exhaust all pairs. QED.

The theorem is **CANDIDATE_FULL pending later independent review**. It does not close the parent conjecture.

## 8. Independent finite sanity check — finite coverage only

A separate C++ union-find enumerator checks

\[
K_3\vee(D_{1,0}\sqcup D_{0,1}),
\]

which has eight vertices and 21 edges. It enumerates all `2^21` edge subsets once and accumulates all one- and two-edge required counts. The exact output is

`n=8 m=21 forests=72846 minDelta=315864 maxDelta=155751480 arg=3,4`  
`ALL_EXACT_CHECKS_PASS`.

This graph is already inside Grimmett–Winkler's finite eight-vertex coverage. The enumeration is therefore only an implementation sanity check and is **not** evidence for a new complete-order bound. The arbitrary-multiplicity theorem comes from Sections 4--7.

## 9. Execution honesty and failures

The first local attempt launched the same-component and core/component symbolic checks sequentially under one execution cap. It completed all 48 same-component schemes and printed the three exact discriminants, then the combined command hit the execution cap before finishing the core/component sector. The calculation was split without changing the mathematics: the same-component-only executable completed with `ALL_EXACT_CHECKS_PASS`, and the core/cross executable separately completed all 11 core/component schemes, the core/core sector and the seed-lift identities with `ALL_EXACT_CHECKS_PASS`.

This is an execution split, not a mathematical failure. No sign failure occurred. The older direct four-parameter cross-component expansion from the preceding NM13-04 run is now superseded by the exact seed-lift lemma and is not retried.

## 10. Residual obstruction and next attack

The previous multiplicity obstruction is removed: both the **number** of mixed-spider components and each pair `(p_j,q_j)` are now unbounded.

The remaining obstruction is structural. The right side is still restricted to depth-two mixed spiders, and arbitrary 3-connected graphs need not admit a triangle-join decomposition of this form.

The strongest next attack is therefore not another multiplicity census. Two complementary routes are now concrete:

1. **Seed-monotonicity cone.** Generalize (6.3)--(6.5) from the specific triangle seed to a cone of terminal seeds and identify conditions under which an independent-terminal `C(x,z)` cross certificate automatically transfers. This could make NM13-08's future depth-three atoms immediately available to NM13-04.
2. **Depth-three branch gadget.** Following NM13-08's one-edge algebra program, test the first rooted depth-three tree operator for closure in `C(x,z)` (or a controlled enlargement) and prove same-component full-strip positivity under the triangle seed. A first exact violation of the seed-lift cone would instead isolate a counterexample template.

The old generic P14 star/mesh polarization obstruction remains the parent-level barrier.

## 11. Durable artifacts and readback target

Created under this run prefix without overwriting older work:

- `2026-09-20T15-22-00Z__triangle-mixed-spider-forest-same-fullstrip-checker.py`;
- `2026-09-20T15-22-00Z__triangle-mixed-spider-forest-same-fullstrip-checker.out`;
- `2026-09-20T15-22-00Z__triangle-mixed-spider-forest-core-cross-checker.py`;
- `2026-09-20T15-22-00Z__triangle-mixed-spider-forest-core-cross-checker.out`;
- `2026-09-20T15-22-00Z__triangle-mixed-spider-forest-bruteforce.cpp`;
- `2026-09-20T15-22-00Z__triangle-mixed-spider-forest-bruteforce.out`;
- this single substantive report.

Runtime SHA-256 values before persistence were:

- same/full-strip checker: `969f12e1b98ea067d0567fa6430a3eca2e76f909688319901efb35cd884bd1d5`;
- same/full-strip output: `85206f74f0825bf99f210d639ee9c3bc8168c3837c44b3cfda199569919cecaa`;
- core/cross checker: `1f66df1342c75af946bb893d69ff038a80591e1bf7a0b79d8e9e74f136d838b9`;
- core/cross output: `a0d1b32e18cb7da3f49798401d26bd2190e72a91f6086b935d6be90a34f3aec3`;
- brute source: `77ce473fc78fbb750c84c4e24c1c4f0b059978867de269fb8a17432bb0450626`;
- brute output: `35be1320bd45773f430e27ed90995cab41ea5ae2e0133c383b1a1091f728d2d4`.

## ledger_delta

```yaml
ledger_delta:
  task: T07
  owner: NM13-04
  parent_problem:
    before: OPEN
    after: OPEN
    complete_all_simple_graph_order_before: 9
    complete_all_simple_graph_order_after: 9
    source_valid_counterexample_order_lower_bound_before: 10
    source_valid_counterexample_order_lower_bound_after: 10
  mechanism:
    before: "triangle seed + one arbitrary mixed spider D_{p,q} + arbitrary isolated right vertices"
    after: "triangle seed + arbitrary finite disjoint union of mixed spiders D_{p_j,q_j}; number of components and all p_j,q_j unbounded"
    new_lemma: "triangle seed-lift: L2^tri=L2, L1^tri=L1+2L2, C0^tri=C0+L1+L2+k(1-6h)"
    same_component_full_strip: "48 schemes = 45 Bernstein-regular + 3 discriminant + 0 failures"
    core_component_full_strip: "11 regular + 0 failures; core/core full-strip strict"
    cross_component: "inherits NM13-08 strict 38-scheme C(x,z) certificate by exact seed-lift"
  theorem_status: CANDIDATE_FULL_RESTRICTED_PENDING_INDEPENDENT_REVIEW
  finite_sanity_only:
    graph: "K3 vee (D_{1,0} sqcup D_{0,1})"
    vertices: 8
    edges: 21
    forests: 72846
    min_delta: 315864
  failures:
    mathematical_sign_failures: 0
    execution: "combined symbolic command hit cap after finishing same-component sector; split exact executions both passed"
    superseded_route: "direct four-parameter cross-component expansion"
  residual_obstruction: "right components beyond depth-two mixed spiders / arbitrary 3-connected graphs"
  next_attack: "abstract terminal-seed monotonicity cone or depth-three rooted branch one-edge algebra"
  novelty: UNVERIFIED
  runtime_model: GPT-5.6-Sol
  runtime_effort: UNVERIFIED
```

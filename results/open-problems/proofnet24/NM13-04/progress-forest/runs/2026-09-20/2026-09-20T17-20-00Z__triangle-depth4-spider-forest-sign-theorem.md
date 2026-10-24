Model actually run: **GPT-5.6 Sol** (system model metadata). Reasoning-effort setting: **UNVERIFIED**.

# NM13-04 / T07 — triangle-seeded arbitrary depth-four spider-forest sign theorem

Status: **PARTIAL on the parent Grimmett–Winkler conjecture / CANDIDATE_FULL for the restricted theorem below, pending later independent review.** Novelty/priority: **UNVERIFIED**. The arbitrary-finite-graph uniform-all-forests conjecture remains OPEN.

Repository / branch: private `yspennstate/math-open-problems` / `master`  
Assigned root: `proofnet24/NM13-04/progress-forest/`  
Companion: NM13-08, `proofnet24/NM13-08/progress-forest-structure/`

## 0. Short handoff and substantive move

The immediately preceding NM13-04 theorem `T07-TRIANGLE-DEPTH3-SPIDER-FOREST-PNC-28` proved strict pairwise negative edge correlation for

\[
K_3\vee\Bigl(\bigsqcup_j E^{(3)}_{m_j}\Bigr),
\]

where `E_m^(3)` is one center with `m` internally disjoint arms of length three. Its proof used the common response strip `43/360 <= h <= 1/8`, a full-strip triangle-seeded same-component calculation, triangle-core/right certificates, and an exact seed lift of NM13-08's independent-terminal cross-component response algebra.

The newest complementary NM13-08 report, `2026-09-20T16-37-00Z__all-length-arm-depth4-spider-report.md`, makes two new moves: it proves that **every arm length** belongs to one fixed seven-dimensional commutative nilpotent tail algebra, and it proves p-NC under three independent terminals for arbitrary forests of pure depth-four spiders. This run consumes that new decomposition but changes the left seed to the triangle. It proves the missing full-strip triangle local theorem for a depth-four spider, all triangle-core/right cases, and lifts NM13-08's strict 60-scheme cross-component theorem through the seed-lift identity. This yields a new arbitrary-component, arbitrary-arm-count 3-connected non-series-parallel class.

No historical or peer artifact is overwritten. No public posting, email, Drive, paid compute, workflow execution, access/permission change, or schedule change is performed.

## 1. Parent problem before/after — separate from the mechanism gain

For a finite graph `G=(V,E)`, write

\[
I_G(\mathbf y)=\sum_{F\subseteq E:\,F\text{ acyclic}}\prod_{e\in F}y_e,
\qquad
\Delta_G(e,f)=I_eI_f-I_GI_{ef}.
\]

At unit weights, `Delta_G(e,f)>=0` is pairwise negative correlation of the indicators of distinct edges under the uniform measure on **all** spanning forests.

**Parent source status:** `OPEN -> OPEN`.  
**Largest completely certified all-simple-graph order in repository continuity:** `9 -> 9`.  
**Equivalent source-valid lower bound on a counterexample order:** `>=10 -> >=10`.

No finite enumeration is promoted to a general theorem.

**Mechanism before:** triangle-seeded arbitrary forests of pure depth-three spiders.  
**Mechanism after:** triangle-seeded arbitrary forests of pure **depth-four** spiders, using NM13-08's newly proved all-arm-length tail closure and depth-four independent-terminal sign theorem.

Let `E_m^(4)` be the tree consisting of one center `c` and `m` internally disjoint length-four arms

\[
c-v_{i,1}-v_{i,2}-v_{i,3}-v_{i,4},\qquad 1\le i\le m,
\]

with `E_0^(4)` interpreted as one isolated right vertex.

### Theorem `T07-TRIANGLE-DEPTH4-SPIDER-FOREST-PNC-29`

For every finite list `m_1,...,m_r` of nonnegative integers, let

\[
H=\bigsqcup_{j=1}^{r}E_{m_j}^{(4)},
\qquad
\boxed{G=K_3\vee H.}
\]

Then for every two distinct present edges `e,f`,

\[
\boxed{\Delta_G(e,f)>0.}
\]

Thus the uniform law on **all** forests of every graph in this class has strict pairwise negative edge correlation.

Both the component count `r` and every arm count `m_j` are arbitrary. For `m>=3`, `E_m^(4)` is genuinely branching of radius four and diameter eight. For a single component,

\[
|V(K_3\vee E_m^{(4)})|=4+4m,\qquad
|E(K_3\vee E_m^{(4)})|=6+16m.
\]

For a nonempty right side the join is 3-connected and contains `K_4`; once the right side has at least three vertices it also contains `K_{3,3}`. Hence this theorem is not a consequence of Erickson's series-parallel result.

## 2. Preserved P14 state and failed generic routes

The P14/HARD10 structural state is preserved rather than rerun.

1. Grimmett–Winkler plus the repository dense-nine complement give unit-weight all-forest p-NC for all simple graphs through order nine.
2. Forest factorization over blocks reduces a vertex-minimal counterexample to a 2-connected graph.
3. P14's two-separator transfer, together with the recovered fixed-graph unit-to-positive-weight implication, reduces a vertex-minimal counterexample further to a **3-connected** graph.
4. The generic degree-three apex/star-mesh route leaves a mixed three-terminal polarization with no universal sign.
5. Universal positivity of that mixed term is false.
6. The proposed reverse-Cauchy sufficient inequality has an exact physical six-vertex counterexample even though the actual Rayleigh gap there remains positive.
7. Naive stability, Lorentzian / complete-log-concavity, and Gårding shortcuts still lack the required hypothesis for arbitrary graphic independence polynomials.

The theorem here enlarges the positive 3-connected region. It does not solve the arbitrary 3-connected obstruction.

## 3. Fresh source-scope boundary

A bounded 20 September 2026 source check keeps the neighboring results separate.

- Grimmett–Winkler, arXiv `math/0302185` / Random Structures & Algorithms 24 (2004), formulate the conjecture for the uniform law on **all forests**, verify every graph on at most eight vertices and every nine-vertex graph with at most eighteen edges, and explicitly distinguish the already-known uniform spanning-tree law.
- Erickson, arXiv `1008.3660`, proves a positive sum-of-squares Rayleigh theorem for spanning-forest polynomials of **series-parallel** graphs in the stronger weighted setting.
- Huang, arXiv `2311.00965`, still describes general arboreal-gas negative correlation as open and treats special graphs/parameters.
- Tang–Zhang, arXiv `2603.10738` (submitted 11 March 2026), treat specified spanning-subgraph ensembles of `K_n`, including forests with **exactly `k` components** for fixed `k` and sufficiently large `n`; this is not the arbitrary-graph uniform law mixing all component counts.
- Tang–Zhang, arXiv `2609.11578` (submitted 10 September 2026), treat high-degree random-cluster models; their `Q=0` endpoint is Bernoulli bond percolation **conditioned to be connected**, not the all-forest law.
- Bado, DOI `10.1016/j.spl.2026.110960`, proves strict p-NC for wheel graphs, another infinite 3-connected non-series-parallel special class.

A bounded current search for spider/depth-four versions did not surface the exact theorem below. This is only negative evidence; novelty remains **UNVERIFIED**.

## 4. Companion decomposition and the depth-four response strip

Retain the three terminal-connectivity states plus the spider center, giving 15 frontier partitions. NM13-08's newest decomposition retains one further arm endpoint, yielding 52 states, and proves for the whole-arm operator `L_d`

\[
L_d=s_dI+M_d,
\qquad M_d\in V,
\qquad V^4=0,
\]

for **every** arm length `d>=1`, where `V` is the same six-dimensional nilpotent ideal generated by the old length-one and length-two tail increments. In particular, the depth-four operator has

\[
s_4=892,
\qquad M_4=L_4-892I,
\]

and

\[
(\operatorname{rank}M_4,\operatorname{rank}M_4^2,
\operatorname{rank}M_4^3,\operatorname{rank}M_4^4)=(8,2,1,0).
\]

After removing the positive scalar `892^m`, the unmarked five-state transfer of `E_m^(4)` is

\[
T_m=A_mI+B_mN+C_mN^2,\qquad N^3=0,
\]

with

\[
\boxed{A_m=\frac{4(36m+223)}{223}},
\]

\[
\boxed{B_m=\frac{34560m^2+223674m+49729}{49729}},
\]

\[
\boxed{C_m=\frac{m(24883200m^2+162422592m+37717933)}{66537402}}.
\]

Put

\[
a_m=B_m/A_m,\qquad c_m=C_m/A_m,
\qquad
\rho_m=\frac{a_m^2/2-c_m}{a_m}.
\]

The exact endpoint differences inherited and independently replayed by the NM13-04 checker are

\[
\rho_m-\frac{43}{360}
=
\frac{7672320m^3+115127982m^2+476185503m+2472973441}
{40140(36m+223)(34560m^2+223674m+49729)}>0,
\]

and

\[
\frac18-\rho_m
=
\frac{m(17985024m^2+226610742m+736408217)}
{2676(36m+223)(34560m^2+223674m+49729)}\ge0.
\]

Hence

\[
\boxed{\frac{43}{360}<\rho_m\le\frac18.}
\tag{4.1}
\]

For an arbitrary product of unmarked right components, write the normalized transfer of component `j` as `I+a_jN+c_jN^2`. Since `N^3=0`, their product is

\[
I+uN+vN^2,
\qquad
u=\sum_j a_j,
\]

\[
v=\sum_j c_j+\sum_{i<j}a_ia_j
=\frac{u^2}{2}-\sum_j\rho_ja_j.
\]

Thus, for `u>0`,

\[
v=\frac{u^2}{2}-hu,
\qquad
h=\frac{\sum_j\rho_ja_j}{\sum_j a_j},
\]

so `h` is a positive weighted average of the component `rho_j`. The `u=0` case is the empty residual product and is included by continuity. Therefore every residual collection of unmarked depth-four spiders lies in the common response strip

\[
\boxed{
\frac{43}{360}\le h\le\frac18,
\qquad
v=\frac{u^2}{2}-hu.
}
\tag{4.2}
\]

This compresses arbitrary component multiplicities analytically; it is not finite graph enumeration.

## 5. New triangle-seeded same-component theorem

The left triangle has exact five-state seed

\[
q=(1,1,1,1,3).
\]

Expose the one depth-four spider containing marked edges `e,f`; absorb all other right components into (4.2). For each of `I,I_e,I_f,I_{ef}`, the exposed response is affine in `(u,v)`, so the Rayleigh numerator is a quadratic `Q(u,v;m)`. Substituting (4.2) gives

\[
R(u,h;m)=\sum_{j=0}^{4}c_j(h;m)u^j,
\]

where every `c_j` has degree at most two in `h`.

Local right-edge types are the center-terminal spoke `c`, terminal spokes `s_1,s_2,s_3,s_4` at the four arm levels, and internal arm edges `i_1,i_2,i_3,i_4`. Terminal `S_3`, arm permutations, and exchange of the marked pair reduce all physical possibilities to exactly

\[
\boxed{97\text{ symbolic same-component schemes}.}
\]

The arm count `m` remains symbolic and unbounded. For each scheme, shift `m=m_0+X` to its physical minimum. For **85/97** schemes, every `c_j` has nonnegative degree-two Bernstein coefficients on `[43/360,1/8]`, and after clearing positive denominators every Bernstein coefficient has nonnegative ordinary coefficients in `X`; moreover `c_0>0`. Since the Bernstein basis and `u^j` are nonnegative on the physical domain, these 85 quartics are strictly positive.

The remaining **12/97** schemes have the form

\[
R=u^2(c_4u^2+c_3u+c_2)+c_1u+c_0,
\]

with `c_4>0`, `c_1>=0`, `c_0>0` throughout the strip and

\[
\boxed{\mathcal K=4c_4c_2-c_3^2>0.}
\tag{5.1}
\]

In all twelve cases the `h` dependence cancels identically from `K`; after the physical `m` shift, its exact numerator has strictly positive coefficients. Therefore the quadratic `c_4u^2+c_3u+c_2` has negative discriminant and positive leading coefficient, hence is positive for every real `u`. This proves `R>0` for every physical `u>=0`.

The exact checker archives all twelve factorizations. The final tally is

\[
\boxed{97=85\text{ Bernstein-regular}+12\text{ discriminant}+0\text{ failures}.}
\tag{5.2}
\]

Unlike the independent-terminal companion theorem, the triangle seed removes the isolated-vertex boundary equality: every physical same-component pair is strict.

## 6. Triangle-core/right and core/core sectors

For one triangle edge and one right edge, terminal symmetry reduces all possibilities to exactly

\[
\boxed{14\text{ symbolic schemes}.}
\]

All **14/14** are Bernstein-regular on the full strip (4.2), with strictly positive constant term and zero failures.

For two distinct triangle edges, the exact strip polynomial is

\[
\boxed{
\Delta_{\rm core,core}
=2+2(3h+1)u+u^2>0.
}
\tag{6.1}
\]

Thus every pair involving at least one triangle-core edge is strictly positive.

## 7. Distinct right components: exact triangle seed lift of NM13-08

The newest NM13-08 depth-four theorem proves that, up to a positive scalar, every unmarked depth-four response and every one-edge-required depth-four response belongs to the commutative one-edge algebra `C(x,z)`. For two marked edges in distinct right components, it reduces the independent-terminal Rayleigh gap to

\[
\Delta_{\rm ind}=L_2u^2+L_1(h)u+C_0.
\]

Its exhaustive **60 symbolic cross-component schemes** prove, throughout the strip (4.2),

\[
\boxed{k>0,\qquad L_2>0,\qquad L_1(h)>0,\qquad C_0>0.}
\tag{7.1}
\]

The triangle evaluation functional changes the affine forest count from

\[
L_{\rm ind}(H,s)=H+su+6v
\]

to

\[
L_{\triangle}(H,s)=(H+s+2)+(s+6)u+6v.
\]

A direct symbolic determinant expansion, independently replayed in the checker, gives

\[
\boxed{L_{2,\triangle}=L_2,}
\]

\[
\boxed{L_{1,\triangle}(h)=L_1(h)+2L_2,}
\]

and

\[
\boxed{C_{0,\triangle}=C_0+L_1(h)+L_2+k(1-6h).}
\tag{7.2}
\]

Because `h<=1/8`,

\[
1-6h\ge\frac14.
\]

Every inequality in (7.1) therefore becomes strictly stronger under the triangle seed. Hence every pair of marked edges in two distinct right components has strictly positive Rayleigh difference. No new four-parameter cross-component census is needed.

## 8. Exhaustion of pair types and proof of the restricted theorem

Every pair of distinct present edges belongs to exactly one of four sectors: two triangle-core edges; one triangle-core edge and one right edge; two edges in the same right component; or two edges in distinct right components. Sections 5–7 prove strict positivity in all four sectors. All unmarked right components are absorbed analytically into (4.2), and restoring the positive scalar normalizations removed from component transfers preserves the sign. This proves `T07-TRIANGLE-DEPTH4-SPIDER-FOREST-PNC-29`.

The theorem is all-parameter: the number of right components and every arm count are unbounded. The counts `97`, `14`, and `60` are counts of **local symbolic orbit types**, not finite graph orders.

## 9. Exact execution, finite sanity check, and failure accounting

The exact checker reconstructs the 15-/52-state transfers directly from acyclicity, verifies the depth-four nilpotence and unmarked response formulas, proves the strip endpoint inequalities, exhausts all 97 triangle-seeded same-component schemes and all 14 triangle-core/right schemes, proves (6.1), and symbolically verifies the seed-lift identities (7.2). It uses exact SymPy rational/integer arithmetic only. Its archived execution ends

`ALL_EXACT_CHECKS_PASS`.

Exact execution summary:

- same-component schemes: `97 = 85 regular + 12 discriminant + 0 failures`;
- core/right schemes: `14 = 14 regular + 0 failures`;
- inherited NM13-08 distinct-component schemes: `60`, transferred by the exact seed-lift identity;
- minimum multiplier in the new positive triangle correction `k(1-6h)`: `1/4` times `k`.

A finite transfer-DP sanity check at `m=2` gives

\[
I_{K_3\vee E_2^{(4)}}(\mathbf1)=197432128.
\]

The graph has 38 edges, hence 703 unordered edge pairs, and the minimum exact Rayleigh numerator over all of them is

\[
\boxed{1004620151616},
\]

attained by the third internal edges on the two arms. This finite calculation is only an implementation sanity check; `E_2^(4)` is a path and is not the source of the new branching theorem.

Artifact hashes and creation commits:

- checker path: `2026-09-20T17-20-00Z__triangle-depth4-spider-forest-checker.py`
- checker SHA-256 from the executed local copy: `8e2d2efd8c9e3aff5979d87c35b37cb33294cfb3573c163bb9d3a53fab01c6a2`
- checker Git blob after readback: `e1167f15f10bc291d1dac9b42e515f71fc3b48ac`
- checker creation commit: `c0388daf383312eefb0e1d4a42703b1de7e1ef89`
- output path: `2026-09-20T17-20-00Z__triangle-depth4-spider-forest-checker.out`
- output SHA-256: `5ee1bc95f1cab8b8e2885057a46d0e38c7dcec42c3d179089ce621da06cbcfb1`
- output Git blob after readback: `2753399abb06886ac78249b0da5762491b8363f6`
- output creation commit: `1f96db49cbb8a12c0dd5cf085ad6b5f99d48edea`

**Failures / nonclaims.** There were zero mathematical sign failures in the certified depth-four sectors. This run does **not** prove the sign theorem for arbitrary arm length `d`, despite NM13-08's all-length unmarked tail closure; marked-pair sign control is still missing uniformly in `d`. It also does not close the older triply-mixed one-component problem with arbitrary numbers of length-one, length-two and length-three arms. No claim beyond the displayed restricted class is made.

The strongest next route is to exploit the 52-state order-nine arm recurrence together with the fixed seven-dimensional tail algebra to derive a **marked-response cone uniform in arm length**. A successful cone theorem would simultaneously transfer pure depth-`d` spider forests to the triangle seed for every `d`; an exact failure would identify the first arm-length/refined-edge-position obstruction rather than merely another timeout. The complementary route remains the marked cone for a single component mixing several arm lengths.

## 10. ledger_delta

```yaml
ledger_delta:
  parent: T07_uniform_forest_pairwise_negative_edge_correlation
  parent_before: OPEN
  parent_after: OPEN
  complete_all_simple_graph_order_before: 9
  complete_all_simple_graph_order_after: 9
  source_valid_counterexample_order_lower_bound_before: ">=10"
  source_valid_counterexample_order_lower_bound_after: ">=10"
  predecessor_mechanism: "triangle-seeded arbitrary forests of pure depth-three spiders E_m^(3)"
  companion_gain_consumed: "NM13-08 all-arm-length seven-dimensional tail closure plus independent-terminal depth-four spider-forest theorem"
  mechanism_after: "triangle-seeded arbitrary finite forests of pure depth-four spiders E_m^(4)"
  theorem: T07-TRIANGLE-DEPTH4-SPIDER-FOREST-PNC-29
  theorem_status: CANDIDATE_FULL_RESTRICTED_PENDING_INDEPENDENT_REVIEW
  novelty: UNVERIFIED
  right_atom: "E_m^(4) = center with m internally disjoint length-four arms"
  free_parameters: "arbitrary finite component count r and arbitrary m_1,...,m_r >= 0"
  response_strip: "43/360 <= h <= 1/8"
  same_component_symbolic_orbits:
    total: 97
    regular: 85
    discriminant: 12
    failures: 0
  core_right_symbolic_orbits:
    total: 14
    regular: 14
    failures: 0
  core_core: "Delta = 2 + 2(3h+1)u + u^2 > 0"
  cross_component:
    companion_schemes: 60
    mechanism: "exact triangle seed-lift of NM13-08 C(x,z) depth-four certificate"
    failures: 0
  finite_sanity:
    graph: "K_3 join E_2^(4)"
    forest_count: 197432128
    edge_pairs: 703
    min_rayleigh_gap: 1004620151616
    promoted_to_general_coverage: false
  p14_boundary: "vertex-minimal counterexample still reducible to 3-connected; generic mixed-terminal star/mesh sign obstruction unresolved"
  finite_enumeration_promoted: false
  unresolved_uniform_arm_length_scope: "all-length unmarked tail closure is proved by NM13-08, but marked sign cone is not yet uniform in d"
  unresolved_mixed_arm_scope: "single components mixing several arm lengths remain uncertified"
  checker: "2026-09-20T17-20-00Z__triangle-depth4-spider-forest-checker.py"
  checker_sha256: "8e2d2efd8c9e3aff5979d87c35b37cb33294cfb3573c163bb9d3a53fab01c6a2"
  output: "2026-09-20T17-20-00Z__triangle-depth4-spider-forest-checker.out"
  output_sha256: "5ee1bc95f1cab8b8e2885057a46d0e38c7dcec42c3d179089ce621da06cbcfb1"
  output_terminal_line: ALL_EXACT_CHECKS_PASS
  next_attack: "derive a marked-response cone uniform in arm length from the 52-state order-nine recurrence and fixed tail algebra; refutation-first on the first failing edge-position inequality"
```

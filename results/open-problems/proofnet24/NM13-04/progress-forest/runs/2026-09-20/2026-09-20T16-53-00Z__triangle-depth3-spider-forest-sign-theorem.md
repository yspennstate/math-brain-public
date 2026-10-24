Model actually run: **GPT-5.6 Sol** (system model metadata). Reasoning-effort setting: **UNVERIFIED**.

# NM13-04 / T07 — triangle-seeded arbitrary depth-three spider-forest sign theorem

Status: **PARTIAL on the parent Grimmett–Winkler conjecture / CANDIDATE_FULL for the restricted theorem below, pending later independent review.** Novelty/priority: **UNVERIFIED**. The arbitrary-finite-graph uniform-all-forests conjecture remains OPEN.

Repository / branch: private `yspennstate/math-open-problems` / `master`  
Assigned root: `proofnet24/NM13-04/progress-forest/`  
Companion: NM13-08, `proofnet24/NM13-08/progress-forest-structure/`

## 0. Short handoff and substantive move

The preceding NM13-04 theorem proved strict pairwise negative edge correlation for

\[
K_3\vee\Bigl(\bigsqcup_j D_{p_j,q_j}\Bigr),
\]

where every right component is a mixed spider with arbitrary numbers of arms of lengths one and two. The proof used the common response strip `43/360 <= h <= 1/8`, full-strip local sign certificates, and a triangle-seed lift of NM13-08's commutative one-edge response algebra.

The newest complementary NM13-08 report, `2026-09-20T16-07-06Z__depth3-spider-forest-report.md`, changes the topology: it introduces pure length-three spider components `E_m`, proves their length-three arm operator closes in the old seven-dimensional tail algebra, and proves strict p-NC for arbitrary finite forests of these components under **three independent terminals**.

This run consumes exactly that complementary decomposition and changes the left boundary to the triangle seed. It proves the missing full-strip triangle local theorem for one exposed depth-three spider, proves all triangle-core/right cases, and transfers NM13-08's strict 38-scheme cross-component theorem through the seed-lift identity. Together these give a new arbitrary-multiplicity triangle-seeded depth-three branching class.

The current LIVE20 policy and root `POSTED.md` were read. No historical or peer artifact is overwritten. No email, Drive, public posting, paid compute, workflow execution, access/permission change, or schedule change is performed.

## 1. Parent problem before/after, separate from the mechanism gain

For a finite graph `G=(V,E)` write

\[
I_G(\mathbf y)=\sum_{F\subseteq E:\,F\text{ acyclic}}\prod_{e\in F}y_e,
\qquad
\Delta_G(e,f)=I_eI_f-I_GI_{ef}.
\]

At unit weights, `Delta_G(e,f)>=0` is exactly pairwise negative correlation of distinct edge indicators under the uniform measure on **all** spanning forests.

**Parent source status:** `OPEN -> OPEN`.  
**Largest completely certified all-simple-graph order in repository continuity:** `9 -> 9`.  
**Equivalent source-valid lower bound on a counterexample order:** `>=10 -> >=10`.

No finite enumeration is promoted to a general theorem.

**Mechanism before:** triangle-seeded arbitrary forests of depth-two mixed spiders.

**Mechanism after:** triangle-seeded arbitrary forests of a genuinely depth-three branching atom with unbounded arm count and unbounded component count.

Let `E_m` be the tree with one center `c` and `m` internally disjoint length-three arms

\[
c-a_i-b_i-d_i,\qquad 1\le i\le m,
\]

with `E_0` interpreted as one isolated right vertex.

### Theorem `T07-TRIANGLE-DEPTH3-SPIDER-FOREST-PNC-28`

For any finite list `m_1,...,m_r` of nonnegative integers, put

\[
H=\bigsqcup_{j=1}^r E_{m_j},
\qquad
\boxed{G=K_3\vee H.}
\]

Then for every two distinct present edges `e,f`,

\[
\boxed{\Delta_G(e,f)>0.}
\]

Thus the uniform law on **all** forests of every graph in this class has strict pairwise negative edge correlation.

Both `r` and every `m_j` are arbitrary. For `m>=3`, `E_m` is genuinely branching of radius three and diameter six. Whenever `H` is nonempty, `G` is 3-connected and contains `K_4`; once the right side has at least three vertices it contains `K_{3,3}`. Hence the theorem is not a consequence of Erickson's series-parallel theorem.

## 2. Preserved P14 state and failed generic routes

The P14/HARD10 structural state is preserved rather than rerun.

1. Grimmett–Winkler plus the repository dense-nine complement cover all simple graphs through nine vertices at unit all-forest weights.
2. Forest factorization over blocks reduces a vertex-minimal counterexample to a 2-connected graph.
3. P14's two-separator transfer, together with the recovered fixed-graph unit-to-positive-weight implication, reduces a vertex-minimal counterexample further to a **3-connected** graph.
4. The generic degree-three apex/star-mesh route leaves a mixed three-terminal polarization with no universal sign.
5. Universal positivity of that mixed term is false.
6. The proposed reverse-Cauchy sufficient inequality has an exact physical six-vertex counterexample even though the actual Rayleigh gap there remains positive.
7. Naive stability, Lorentzian / complete-log-concavity, and Gårding shortcuts still lack the required hypothesis for arbitrary graphic independence polynomials.

The theorem here enlarges the positive 3-connected region. It does not solve the arbitrary 3-connected obstruction.

## 3. Fresh source-scope boundary

A bounded 20 September 2026 web check still separates T07 from neighboring results.

- Grimmett–Winkler, `arXiv:math/0302185`, formulate the conjecture for the uniform law on **all forests**, verify every graph on at most eight vertices and every nine-vertex graph with at most eighteen edges, and explicitly distinguish the already-known spanning-tree law.
- Erickson, `arXiv:1008.3660`, gives a positive sum-of-squares Rayleigh theorem for spanning-forest polynomials of **series-parallel** graphs in the stronger weighted setting.
- Huang, `arXiv:2311.00965`, still describes general arboreal-gas negative correlation as open while treating special graphs/parameters.
- Tang–Zhang, `arXiv:2603.10738` (11 March 2026), prove p-NC for specified spanning-subgraph ensembles of `K_n`, including forests with **exactly `k` components** for fixed `k` and sufficiently large `n`; this is not the arbitrary-graph uniform law mixing all forest component counts.
- Tang–Zhang, `arXiv:2609.11578` (10 September 2026), prove a high-degree random-cluster result; its `Q=0` endpoint is Bernoulli bond percolation **conditioned to be connected**, not the all-forest law.
- Bado's wheel theorem is another infinite 3-connected non-series-parallel positive family.

A bounded search for depth-three/spider variants did not surface the exact theorem above. That is only negative evidence; novelty remains **UNVERIFIED**.

## 4. Companion decomposition: the length-three arm remains in the old tail algebra

Retain the three terminal-connectivity states plus one spider center, giving 15 frontier partitions. Let `L_1,L_2,L_3` be the exact arm operators of lengths one, two, and three. NM13-08's newest decomposition gives

\[
L_1=5I+J,\qquad L_2=28I+K,\qquad L_3=158I+M,
\]

with

\[
M^4=0,
\qquad
(\operatorname{rank}M,\operatorname{rank}M^2,\operatorname{rank}M^3,\operatorname{rank}M^4)=(8,2,1,0),
\]

and exact closure

\[
\boxed{
M=
\frac{82}{7}K+\frac{73}{1029}K^2-\frac{1376}{893025}K^3
-\frac{254}{7}J+\frac{282}{343}JK-\frac{4185}{343}J^2.
}
\]

The NM13-04 checker reconstructs `L_3` independently from the partition recurrence and verifies this identity entrywise over `Q`.

After removing the positive scalar `158^m`, the unmarked five-state transfer of `E_m` is

\[
T_m=A_mI+B_mN+C_mN^2,\qquad N^3=0,
\]

where

\[
A_m=\frac{51m+316}{79},
\]

\[
B_m=\frac{3247m^2+21322m+6241}{6241},
\]

\[
C_m=\frac{m(620177m^2+4118189m+1259235)}{2958234}.
\]

Its response parameter is

\[
\rho_m=
\frac{9391633m^3+119901505m^2+400505352m+116850243}
{474(51m+316)(3247m^2+21322m+6241)}.
\]

Exact coefficient checks give

\[
\boxed{\frac{43}{360}<\rho_m\le\frac18,}
\]

with upper equality exactly at `m=0`. Hence an arbitrary finite product of unmarked `E_m` components has normalized response

\[
U=I+uN+vN^2,
\qquad
v=\frac{u^2}{2}-hu,
\qquad
\boxed{\frac{43}{360}\le h\le\frac18.}
\tag{4.1}
\]

This is an analytic compression of arbitrarily many unmarked components, not finite graph enumeration.

## 5. New triangle-seeded same-component theorem on the full strip

The triangle seed is

\[
q=(1,1,1,1,3).
\]

Expose one `E_m` containing two marked edges. Each of `I,I_e,I_f,I_{ef}` is affine in `(u,v)`, so the normalized Rayleigh numerator is quadratic in `(u,v)`. Substitution of (4.1) gives

\[
R(u,h;m)=\sum_{j=0}^4 c_j(h;m)u^j,
\]

where every `c_j` has degree at most two in `h`.

Terminal `S_3`, arm permutations, and exchange of the marked pair reduce all local possibilities to exactly

\[
\boxed{58\text{ symbolic schemes}.}
\]

The arm count `m` remains symbolic and unbounded. For the physical minimum `m_0` of a scheme, the checker shifts `m=m_0+X`, expands every `c_j` in the degree-two Bernstein basis on `[43/360,1/8]`, clears positive rational denominators, and tests coefficientwise nonnegativity in `X`.

Exactly

\[
\boxed{52\text{ schemes are Bernstein-regular}.}
\]

The remaining six have

\[
R=u^2(c_4u^2+c_3u+c_2)+c_1u+c_0,
\]

with `c_4>0`, `c_1>=0`, `c_0>0` on the full strip and

\[
\mathcal K=4c_4c_2-c_3^2>0.
\]

In all six cases `h` cancels identically from `K`. The exact positive factors are

\[
\frac{27(4302797m^2+49364112m+184371072)}{243087455521},
\]

\[
\frac{132300(26087389097m^2+329188679764m+1083556876448)}{9468276082626847201},
\]

\[
\frac{1764(179137657407m^2+2260190028976m+7231861833616)}{9468276082626847201},
\]

\[
\frac{16875(60245776709m^2+752993829408m+2360758299424)}{37873104330507388804},
\]

\[
\frac{225(385207281327m^2+4788823319320m+14898225335440)}{37873104330507388804},
\]

and

\[
\frac{9(798256270143m^2+9898978136504m+30693015985584)}{37873104330507388804}.
\]

Thus the quadratic core has negative discriminant and positive leading coefficient, so every exceptional quartic is strictly positive for `u>=0` in its physical domain. The exact tally is

\[
\boxed{58=52\text{ regular}+6\text{ discriminant}+0\text{ failures}.}
\]

The triangle seed is visibly stronger here than the independent-terminal companion calculation, which had eight discriminant cases and one boundary equality at the isolated-vertex endpoint.

## 6. New triangle-core/right and core/core sectors

For one triangle edge and one right-component edge, terminal symmetry reduces all possibilities to exactly 11 symbolic schemes. Every one is coefficientwise Bernstein-positive on the full strip:

\[
\boxed{11\text{ regular},\quad0\text{ failures}.}
\]

For two distinct triangle-core edges the exact strip polynomial is

\[
\boxed{
\Delta_{\rm core,core}(u,h)
=2+2(3h+1)u+u^2>0.
}
\]

Hence all pairs touching the triangle core are closed uniformly over arbitrary unmarked depth-three-spider remainder.

## 7. Cross-component seed-lift: no new four-parameter census is needed

The final case has the marked edges in two distinct right components. NM13-08 proves that every unmarked or one-edge-required depth-three-spider transfer lies, after a positive scalar normalization, in the commutative algebra

\[
C(x,z)=
\begin{pmatrix}
1&x_1&x_2&x_3&z\\
0&1&0&0&t-x_1\\
0&0&1&0&t-x_2\\
0&0&0&1&t-x_3\\
0&0&0&0&1
\end{pmatrix},
\qquad t=x_1+x_2+x_3,
\]

with multiplication controlled by

\[
\kappa(x,y)=(\sum x_i)(\sum y_i)-x\cdot y.
\]

For the independent-terminal seed, the cross-component Rayleigh gap after the strip substitution has the exact form

\[
\Delta_{\rm ind}=L_2u^2+L_1(h)u+C_0,
\]

where NM13-08's exact 38-scheme all-parameter certificate proves

\[
\boxed{k>0,\qquad L_2>0,\qquad L_1(h)>0,\qquad C_0>0}
\tag{7.1}
\]

throughout (4.1).

The triangle evaluation functional changes the affine forest count from

\[
L_{\rm ind}(H,s)=H+su+6v
\]

to

\[
L_{\triangle}(H,s)=(H+s+2)+(s+6)u+6v.
\]

A direct symbolic determinant expansion gives the exact seed-lift identities

\[
\boxed{L_{2,\triangle}=L_2,}
\]

\[
\boxed{L_{1,\triangle}(h)=L_1(h)+2L_2,}
\]

and

\[
\boxed{C_{0,\triangle}=C_0+L_1(h)+L_2+k(1-6h).}
\]

Because `h<=1/8`,

\[
1-6h\ge\frac14.
\]

Therefore every inequality in (7.1) becomes strictly stronger under the triangle seed. Every pair of marked edges in two distinct right components is strictly positive without any new four-arm-count orbit enumeration.

## 8. Exhaustion of pair types and theorem proof

Every pair of distinct present edges belongs to exactly one of four sectors:

1. two triangle-core edges — Section 6;
2. one triangle-core edge and one right edge — Section 6;
3. two edges in the same right component — Section 5;
4. two edges in distinct right components — Section 7.

All unmarked components in every case are absorbed analytically into the common response strip (4.1). Each sector is strictly positive. Restoring the positive diagonal normalizations removed from the component transfers preserves the sign. This proves `T07-TRIANGLE-DEPTH3-SPIDER-FOREST-PNC-28`.

This is an all-parameter theorem: the number of components and all arm counts are arbitrary. The 58/11/38 finite counts are counts of **local symbolic orbit types**, not a finite enumeration of graph orders.

## 9. Executed exact checker, failure accounting, and residual obstruction

The exact checker reconstructs the 15-state transfer matrices from acyclicity, verifies the length-three tail-algebra closure, derives the `A_m,B_m,C_m,rho_m` formulas, proves the response strip, exhausts the 58 same-component and 11 core/right symbolic schemes, and proves the abstract seed-lift determinant identity. It uses exact SymPy rational/integer arithmetic only. The archived output ends

`ALL_EXACT_CHECKS_PASS`.

Artifact SHA-256 values:

- checker: `101f36223d0622af344b05289c45f327100e95359ec37c7128c54d347deae899`
- executed output: `33338eb670868bd7191f8215280fc1521944fc6fbb6bc2eb023370a4e39e6dc6`

GitHub creation commits:

- checker: `af689d1ea4990b6e37e1c3d94b2d8c29d50a4b65`
- output: `1217723a4403f34991dfbcef0c2bfdaead7be892`

A first direct attempt at the broader **triply mixed** spider (arbitrary numbers of length-one, length-two, and length-three arms in the same component) successfully recovered an unmarked response in the same strip, but the direct marked 150-orbit symbolic expansion became computationally expensive before exhaustive completion. That incomplete route is **not** used in this theorem and no triply-mixed claim is made.

The remaining mathematical obstruction is therefore structural, not multiplicity-based: the current theorem allows arbitrary many pure depth-three spider components, while the predecessor theorem allows arbitrary many depth-one/two mixed spiders, but a single right component mixing all three arm lengths has not been certified. The natural next attack is to exploit the fact that `J,K,M` all live in the same seven-dimensional commuting algebra to derive a marked-transfer cone for a `D_{p,q,r}` component, rather than enumerate 150 schemes naively. A negative exact cone inequality would instead identify a refutation template.

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
  predecessor_mechanism: "triangle-seeded arbitrary forests of depth-two mixed spiders D_{p,q}"
  mechanism_after: "triangle-seeded arbitrary finite forests of pure depth-three spiders E_m"
  theorem: T07-TRIANGLE-DEPTH3-SPIDER-FOREST-PNC-28
  theorem_status: CANDIDATE_FULL_RESTRICTED_PENDING_INDEPENDENT_REVIEW
  novelty: UNVERIFIED
  right_atom: "E_m = center with m internally disjoint length-three arms"
  free_parameters: "arbitrary finite component count r and arbitrary m_1,...,m_r >= 0"
  response_strip: "43/360 <= h <= 1/8"
  same_component_symbolic_orbits:
    total: 58
    regular: 52
    discriminant: 6
    failures: 0
  core_right_symbolic_orbits:
    total: 11
    regular: 11
    failures: 0
  cross_component:
    companion_schemes: 38
    mechanism: "exact triangle seed-lift of NM13-08 C(x,z) certificate"
    failures: 0
  p14_boundary: "vertex-minimal counterexample still reducible to 3-connected; generic mixed-terminal star/mesh sign obstruction unresolved"
  finite_enumeration_promoted: false
  broader_triply_mixed_route: "INCOMPLETE; unmarked strip succeeded, marked 150-orbit direct expansion not exhausted"
  checker: "2026-09-20T16-53-00Z__triangle-depth3-spider-forest-checker.py"
  checker_sha256: "101f36223d0622af344b05289c45f327100e95359ec37c7128c54d347deae899"
  output: "2026-09-20T16-53-00Z__triangle-depth3-spider-forest-checker.out"
  output_sha256: "33338eb670868bd7191f8215280fc1521944fc6fbb6bc2eb023370a4e39e6dc6"
  output_terminal_line: ALL_EXACT_CHECKS_PASS
  next_attack: "derive a seven-dimensional marked-transfer cone for D_{p,q,r}; refutation-first on any cone inequality that fails"
```

Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.**

# NM13-08 / T07 — universal three-terminal layer algebra and p-NC for right-side linear forests of component size at most 3

Status: **PARTIAL on the parent Grimmett–Winkler conjecture / CANDIDATE_FULL for the restricted theorem below, pending later independent review.** The arbitrary-finite-graph uniform-all-forests conjecture remains OPEN.

Repository / branch: private `yspennstate/math-open-problems` / `master`  
Assigned root: `proofnet24/NM13-08/progress-forest-structure/`  
Companion: NM13-04, `proofnet24/NM13-04/progress-forest/`

## 0. Compact handoff

The preceding NM13-08 run proved strict unit forest p-NC for `K_{3,2k+r}+M_k` by a five-state three-terminal transfer algebra. The newest companion NM13-04 run then added a left triangle and proved strict p-NC for `K_3 vee (M_k disjoint_union I_r)`. Those results are preserved.

This run changes the right-side topology: it introduces degree-two right vertices via disjoint three-vertex paths. More importantly, it proves that **every** terminal-symmetric right layer, with an arbitrary internal graph, has its unmarked forest transfer in the same three-dimensional nilpotent algebra. The new application combines three layer species simultaneously and proves an exact all-parameter theorem for

\[
L_{p,m,r}:=K_{3,3p+2m+r}+\bigl(pP_3\sqcup mK_2\sqcup rK_1\bigr),
\]

where the displayed linear forest lies inside the right part and every right vertex is adjacent to all three left terminals.

The proof is symbolic in all three parameters. An exact checker reduces every distinct edge pair to 46 automorphism orbits and proves each Rayleigh polynomial nonnegative by a positive multivariate Newton/binomial-basis certificate. The only equality case with an actual edge pair is `L_{0,0,1}=K_{3,1}`; all other physical pairs are strict.

`POSTED.md` was checked. No posted source theorem is reopened. Novelty/priority of the exact layer-algebra formulation and the `L_{p,m,r}` theorem is **UNVERIFIED**; bounded public searching on 20 September 2026 did not surface this exact statement.

## 1. Parent theorem before/after, separate from mechanism gain

For a finite graph `G=(V,E)`, let

\[
I_G(\mathbf y)=\sum_{F\subseteq E:\,F\text{ acyclic}}\prod_{e\in F}y_e,
\qquad
\Delta_G(e,f)=I_eI_f-I_GI_{ef}.
\]

At unit weights, `Delta_G(e,f)>=0` is exactly pairwise negative edge correlation under the uniform measure on **all** acyclic spanning edge subsets, with all component counts mixed.

**Parent source status:** `OPEN -> OPEN`.  
**Largest completely certified all-simple-graph order in repository continuity:** `9 -> 9`.  
**Equivalent source-valid counterexample-order lower bound:** `>=10 -> >=10`.

No source-level finite-order metric moves.

**Mechanism before:** star and right-`K_2` three-terminal layers, two-terminal substitution/PF machinery, and the companion's triangle-plus-matching family.

**Mechanism after:**

1. arbitrary terminal-symmetric right layers have transfer `aI+bN+cN^2`, `N^3=0`;
2. arbitrary marked requirements in disjoint layers commute;
3. a complete three-parameter p-NC theorem for right induced `pP_3 disjoint_union mK_2 disjoint_union rK_1`;
4. a minor-monotone invariant proving the new `p>=2` tail is outside the minor closure of NM13-04's current triangle-plus-matching class.

## 2. Recovered P14 and literature scope

Grimmett–Winkler, `arXiv:math/0302185`, study the uniform measure on **all forests**. Their published computation verifies pairwise negative edge correlation for every graph on at most eight vertices and every nine-vertex graph with at most eighteen edges. They explicitly distinguish the already-known uniform-spanning-tree theorem; a spanning-tree theorem is not the present conjecture.

P14/HARD10 continuity supplies the complementary dense nine-vertex sector (`19..36` edges), so all simple graphs through nine vertices are covered in the repository. P14 also records the Cocks/Semple–Welsh fixed-graph implication from the unit source inequality to all-positive-weight independence correlation, together with block/two-separator inheritance; hence a vertex-minimal source counterexample may be taken **3-connected**. P14's generic degree-three star/mesh route remains incomplete because the mixed three-terminal polarization is not universally nonnegative; a proposed reverse-Cauchy sufficient inequality was exactly refuted on a physical small graph even though that graph's true Rayleigh gap stayed positive.

Erickson, `arXiv:1008.3660`, proves an SOS formula for the spanning-forest Rayleigh difference of every **series-parallel** graph, giving the stronger all-positive-weight independent-set-Rayleigh property there.

Huang, `arXiv:2311.00965` / *Statistics & Probability Letters* 213 (2024), treats restricted arboreal-gas negative-correlation questions and still describes the general problem as open. Bado, DOI `10.1016/j.spl.2026.110960`, proves strict p-NC for every wheel under the uniform-all-forests law. Tang–Zhang, `arXiv:2603.10738` (11 March 2026), prove p-NC for specified complete-graph spanning-subgraph ensembles including forests with a **fixed number of components** for fixed `k` and sufficiently large `n`; that is not the arbitrary-graph all-component uniform forest law.

## 3. Universal three-terminal layer algebra

Fix terminals `0,1,2`. Let `H` be any finite graph on a fresh right vertex set `R`, and form a layer `Lambda(H)` by taking `H` and joining every `v in R` to each terminal. There are no terminal-terminal edges in the layer.

Use terminal states

\[
D=0|1|2,\quad P_{12}=0|12,\quad P_{01}=01|2,\quad P_{02}=02|1,\quad T=012.
\]

For incoming partition `pi`, glue the layer to any outside forest realizing `pi`; count acyclic layer subsets by the outgoing terminal partition. This is well-defined because cycle creation depends only on the incoming terminal partition.

For the one-right-vertex star,

\[
S=\begin{pmatrix}
4&1&1&1&1\\
0&4&0&0&2\\
0&0&4&0&2\\
0&0&0&4&2\\
0&0&0&0&4
\end{pmatrix},\qquad N=S-4I,
\]

and `N^3=0`, `N^2!=0`.

### Lemma `T07-UNIVERSAL-THREE-TERMINAL-LAYER-ALGEBRA-10`

For every internal graph `H`, there are integers `A_H,B_H,D_H>=0` with

\[
T_H=\begin{pmatrix}
A_H&B_H&B_H&B_H&D_H\\
0&A_H&0&0&2B_H\\
0&0&A_H&0&2B_H\\
0&0&0&A_H&2B_H\\
0&0&0&0&A_H
\end{pmatrix}
=A_HI+B_HN+\frac{D_H-B_H}{6}N^2.
\]

**Proof.** Terminal `S_3` symmetry gives equality among the three `D->P` entries, among pair-state diagonals, and among `P->T` entries. A layer subset contributes to a diagonal entry exactly when it connects no two distinct terminals: from `D` such a connection changes state; from a pair state a path between the preconnected terminals would create a cycle and a path to the remaining terminal changes state; from `T` any new terminal-terminal path creates a cycle. Hence all five diagonal entries coincide at `A_H`.

Let `B_H` be the `D->P_{12}` count. Starting from `P_{12}`, an admissible subset reaches `T` iff it connects terminal `0` to exactly one of `1,2`; connecting it to both creates a layer path between `1,2` and hence a cycle with the outside path. Thus the relevant subsets are exactly the disjoint union of the `D->P_{01}` and `D->P_{02}` classes, each of size `B_H`, giving `2B_H`. If `D_H` is the `D->T` count, then `N` has `D->T` entry `1` and `N^2` has `D->T` entry `6`, so the displayed polynomial identity follows. QED.

The proof works coefficientwise with arbitrary internal edge weights and a common weight on the three spokes incident to each right vertex; then `A_H,B_H,D_H` are polynomials. This is the generating-polynomial form.

## 4. Marked-layer commutation and product formula

### Lemma `T07-MARKED-LAYER-COMMUTATION-10`

For two fresh three-terminal layers sharing only the terminals, impose any fixed local marked-edge requirements in either layer. Their marked transfer operators commute.

**Proof.** A matrix product counts pairs `(F_1,F_2)` of marked local forests whose union with the incoming outside forest is acyclic and has the specified final partition. If the final union is acyclic, either intermediate union is acyclic. Swapping layer order leaves the same final edge set and partition, giving a bijection term-by-term. QED.

For unmarked layers write `alpha_i=B_i/A_i` and `gamma_i=(D_i-B_i)/(6A_i)`. Then

\[
\prod_iT_{H_i}=\left(\prod_iA_i\right)(I+uN+vN^2),
\]

with

\[
u=\sum_i\alpha_i,\qquad v=\sum_i\gamma_i+\sum_{i<j}\alpha_i\alpha_j.
\]

Hence for finitely many layer species, `u` is linear and `v` quadratic in species counts. Every marked forest count is degree at most two after positive scalar factors are removed, and every Rayleigh difference has degree at most four.

## 5. New class and theorem

Take right induced graph

\[
R=pP_3\sqcup mK_2\sqcup rK_1,
\]

and join every right vertex to three independent terminals. Then

\[
|V(L_{p,m,r})|=3+3p+2m+r,\qquad |E(L_{p,m,r})|=11p+7m+3r.
\]

### Theorem `T07-RIGHT-LINEAR-FOREST-PNC-10`

For every `p,m,r>=0` and every distinct present edges `e,f`,

\[
\boxed{\Delta_{L_{p,m,r}}(e,f)\ge0.}
\]

The inequality is strict for every physical edge pair except when `(p,m,r)=(0,0,1)`, i.e. `K_{3,1}`, which is a tree and has equality.

The specialization `p=0` contains the preceding matching theorem; the genuinely new regime is `p>=1`.

## 6. Exact layer matrices and all-forest count

Exact enumeration gives

\[
T_{K_2}=23I+12N+\frac53N^2,
\]

and for a right `P_3`,

\[
T_{P_3}=\begin{pmatrix}
130&103&103&103&273\\
0&130&0&0&206\\
0&0&130&0&206\\
0&0&0&130&206\\
0&0&0&0&130
\end{pmatrix}
=130I+103N+\frac{85}{3}N^2.
\]

Therefore

\[
T_{P_3}^pT_{K_2}^mS^r=130^p23^m4^r(I+uN+vN^2),
\]

where

\[
u=\frac{103p}{130}+\frac{12m}{23}+\frac r4,
\]

and

\[
\begin{aligned}
v={}&\frac{17p}{78}+\frac{5m}{69}
+\binom p2\left(\frac{103}{130}\right)^2
+\binom m2\left(\frac{12}{23}\right)^2
+\binom r2\frac1{16}\\
&+pm\frac{103}{130}\frac{12}{23}+pr\frac{103}{520}+mr\frac3{23}.
\end{aligned}
\]

Starting from the discrete state and summing over final states gives

\[
I_{L_{p,m,r}}(\mathbf1)=130^p23^m4^rQ(p,m,r),
\]

with

\[
\begin{aligned}
35760400Q={}&29203200m^2+88695360mp+27986400mr+60975200m\\
&+67345932p^2+42499860pr+92750628p\\
&+6705075r^2+29055325r+35760400.
\end{aligned}
\]

The checker reconstructs these matrices and this count directly by exact enumeration.

## 7. Complete sign proof: 46 orbits and a positive Newton cone

The automorphism group contains terminal permutations, permutations of equal layer species, endpoint reversals in each `P_3`, and endpoint swaps in each `K_2`. A witness with two layers of each species realizes every unordered pair type. There are exactly 46 classes:

* `P3/P3` same block 10, different blocks 9;
* `P3/K2` 8;
* `P3/K1` 5;
* `K2/K2` same block 4, different blocks 4;
* `K2/K1` 3;
* `K1/K1` same block 1, different blocks 2.

Fix an orbit and expose its distinguished layer(s). By marked-layer commutation, all remaining unmarked layers move to the end. If `x,y,z` are remaining `P_3,K_2,K_1` counts, then

\[
\Delta(e,f)=(130^x23^y4^z)^2R_{\mathcal O}(x,y,z),
\]

where `R_O` is an exact rational polynomial of total degree at most four.

The checker expands each in the multivariate Newton basis

\[
R_{\mathcal O}(x,y,z)=\sum_{i+j+k\le4}c^{\mathcal O}_{ijk}
\binom xi\binom yj\binom zk,
\]

with coefficients obtained exactly by forward differences. **Every nonzero Newton coefficient in all 46 orbit polynomials is strictly positive.** Since all binomial basis functions are nonnegative on nonnegative integers, all Rayleigh differences are nonnegative for every parameter value.

Exactly one orbit has zero constant term: two distinct spokes in one singleton layer. Its Newton expansion has positive `binom(x,1)`, `binom(y,1)`, and `binom(z,1)` coefficients, so equality occurs only when no other layer remains, namely `K_{3,1}`. Every other orbit has positive constant term.

One `P_3` orbit—spokes at opposite path endpoints with different terminal labels—has negative ordinary monomial coefficients, so the Newton basis is a genuine sign improvement rather than cosmetic rewriting. The archived output prints the full positive Newton certificate for this difficult orbit and for the unique equality orbit.

This is an all-parameter exact symbolic proof, not finite extrapolation.

## 8. Genuine non-overlap with NM13-04 and earlier routes

If `p>=1`, the three terminals together with one `P_3` block contain a `K_{3,3}` subgraph, so the graph is nonplanar and not series-parallel; this excludes Erickson's class and Bado's wheel family.

For a sharper comparison with NM13-04, define

\[
\mu(G)=\min\{|S|:\ \text{maximum degree of }G-S\le1\}.
\]

The class `maximum degree <=1` is minor-closed, so `mu` is minor-monotone: under a minor model, the image of a deletion set has no larger cardinality and leaves a minor of a matching-plus-isolates graph.

For NM13-04's current family `K_3 vee (M_k disjoint_union I_r)`, deleting the three left vertices leaves a matching plus isolates, hence `mu<=3`; every minor also has `mu<=3`.

For `L_{p,m,r}`, put `n_R=3p+2m+r`. If all terminals are deleted, at least one additional vertex from each right `P_3` must be deleted, giving `p+3`. If at least two terminals survive, every surviving right vertex has degree at least two, so all `n_R` right vertices must be deleted. If exactly one terminal survives, at most one right vertex may remain, costing at least `n_R+1`. Hence

\[
\boxed{\mu(L_{p,m,r})=\min(n_R,p+3).}
\]

For every `p>=2`, `mu=p+3>=5`, so these graphs cannot be minors of NM13-04's newest triangle-plus-matching family. The same invariant gives `p>=3` outside the split-5 minor closure (`mu<=5`) and `p>=28` outside every minor of the current width-30 complete-bipartite route (`mu<=30`).

Whenever `3p+2m+r>=3`, the spanning `K_{3,n_R}` is 3-connected, hence so is `L_{p,m,r}`. In particular every `p>=1` instance lies directly in the structural region left after P14's minimal-counterexample reduction.

## 9. Executed exact checks

`2026-09-20T04-38-00Z__right-linear-forest-checker.py` performs exact integer/rational checks of:

* the three transfer matrices and `N^3=0`;
* the closed count above;
* the complete 46-orbit decomposition;
* every one- and two-marked transfer;
* all 46 Rayleigh polynomials and every Newton coefficient;
* the unique zero-constant orbit;
* independent brute-force forest enumeration for `L_(1,0,0)` (`Z=712`, minimum gap `1728`), `L_(0,1,1)` (`Z=488`, minimum gap `448`), and `L_(1,1,0)` (`Z=31332`, minimum gap `137088`).

The archived output ends `ALL_EXACT_CHECKS_PASS`. These are self-checks, not independent review, so the restricted theorem remains `CANDIDATE_FULL` rather than certified closure.

## 10. Residual obstruction and next attack

The universal layer algebra is broader than the sign theorem: an arbitrary internal right graph `H` still has transfer in `span{I,N,N^2}`, but its marked-edge Rayleigh orbit polynomials need not automatically lie in the positive Newton cone. That marked-edge sign cone is now the precise obstruction.

The next distinct test is a four-vertex path layer `P_4`. Direct enumeration gives unmarked transfer

\[
734I+780N+\frac{961}{3}N^2,
\]

but the marked-orbit Newton positivity needed to adjoin arbitrary `P_4` components is not yet proved.

## 11. ledger_delta

```yaml
ledger_delta:
  slot: NM13-08
  parent: T07_uniform_forest_pairwise_negative_edge_correlation
  source_status_before: OPEN
  source_status_after: OPEN
  complete_all_graph_order_before: 9
  complete_all_graph_order_after: 9
  counterexample_order_lower_bound_before: 10
  counterexample_order_lower_bound_after: 10
  new_mechanism:
    - universal_three_terminal_symmetric_layer_transfer_aI_plus_bN_plus_cN2
    - arbitrary_marked_disjoint_layer_commutation
    - multivariate_Newton_cone_sign_certificate
  new_restricted_theorem:
    family: "L_{p,m,r}=K_{3,3p+2m+r} plus right induced p P3 disjoint_union m K2 disjoint_union r K1"
    parameters: "p,m,r >= 0"
    verdict: "Delta(e,f)>=0 for every distinct edge pair; strict except L_{0,0,1}=K_{3,1}"
    proof_type: exact_symbolic_46_orbit_Newton_certificate
    status: CANDIDATE_FULL_PENDING_INDEPENDENT_REVIEW
  nonoverlap:
    invariant: "mu(G)=minimum deletions to maximum-degree<=1"
    formula_new_family: "mu(L_{p,m,r})=min(3p+2m+r,p+3)"
    escapes_NM13_04_minor_closure: "p>=2"
    escapes_split5_minor_closure: "p>=3"
    escapes_biclique_width30_minor_route: "p>=28"
  exact_result: ALL_EXACT_CHECKS_PASS
  residual_obstruction: marked_edge_sign_cone_for_general_internal_right_layers
  next_attack: P4_right_layer_marked_orbit_Newton_positivity
  parent_closed: false
```

Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.**

# NM13-08 / T07 — P4 right-layer staircase sign theorem for uniform forests

Status: **PARTIAL on the parent Grimmett–Winkler conjecture / CANDIDATE_FULL for the restricted theorem below, pending later independent review.** The arbitrary-finite-graph uniform-all-forests conjecture remains OPEN.

Repository / branch: private `yspennstate/math-open-problems` / `master`  
Assigned root: `proofnet24/NM13-08/progress-forest-structure/`  
Companion: NM13-04, `proofnet24/NM13-04/progress-forest/`

## 0. Compact handoff and this run's distinct attack

The preceding NM13-08 report proved the universal five-state three-terminal unmarked layer algebra and a complete positive-Newton theorem for right induced `p P3 disjoint_union m K2 disjoint_union r K1`. Its explicit next obstruction was a right `P4` layer: the unmarked transfer already lay in the same nilpotent algebra, but marked-edge sign control had not been proved.

The newest NM13-04 report independently seeded the `P3/K2/K1` right-layer theory with a left triangle and proved strict p-NC for `K3 join (p P3 disjoint_union m K2 disjoint_union r K1)`. That work is preserved and not duplicated here.

This run attacks the first genuinely new right-component size:
\[
F_{p,r}:=K_{3,\,4p+r}+\bigl(pP_4\sqcup rK_1\bigr),
\qquad p,r\ge0,
\]
where the three vertices in the size-3 side are independent, every right vertex is adjacent to all three terminals, and the displayed `P4` edges are added inside the right side.

The positive Newton cone from the previous run **fails** for exactly one marked `P4` orbit. Rather than abandon the transfer route, this run proves a new shifted-quadrant/staircase sign certificate for that exceptional orbit. The combination yields an exact all-parameter theorem.

`POSTED.md` and the current LIVE20 policy were checked. No posted theorem is reopened. Novelty/priority of this exact `P4` theorem and staircase certificate is **UNVERIFIED**; bounded public searches on 20 September 2026 did not surface the same statement.

## 1. Parent theorem before/after, separate from demonstrated mechanism gain

For a finite graph `G=(V,E)`,
\[
I_G(\mathbf y)=\sum_{F\subseteq E:\,F\text{ acyclic}}\prod_{e\in F}y_e,
\qquad
\Delta_G(e,f)=I_eI_f-I_GI_{ef}.
\]
At unit weights, `Delta_G(e,f)>=0` is exactly pairwise negative edge correlation for the uniform measure on **all** acyclic spanning edge subsets, with every component count mixed.

**Parent source status:** `OPEN -> OPEN`.  
**Largest completely certified all-simple-graph order in repository continuity:** `9 -> 9`.  
**Equivalent source-valid lower bound on a counterexample order:** `>=10 -> >=10`.

No source-level complete-order metric moves.

**Mechanism before:** two-terminal transparent/PF substitution; three-terminal unmarked layer algebra; complete positive-Newton marked sign theorem for right components of order at most 3.

**Mechanism after:** the first order-4 right component is controlled. Thirty-nine of forty `P4/K1` pair-orbit polynomials remain in the positive Newton cone; the unique failure is proved positive by a five-region shifted-quadrant certificate plus 30 exact boundary values. This establishes a complete two-parameter theorem for arbitrarily many disjoint right `P4` components and arbitrary isolated right vertices.

## 2. Recovered P14 and literature scope

The P14 mandatory handoff remains the controlling repository history for the source-level conjecture.

- Grimmett–Winkler, `arXiv:math/0302185`, study the uniform measure on **all forests**. Their computation verifies pairwise edge negative correlation for every graph on at most eight vertices and every nine-vertex graph with at most eighteen edges. They explicitly distinguish the already-known uniform-spanning-tree theorem.
- P14/HARD10 supplies the exact complementary dense nine-vertex sector, so all `274,668` unlabeled simple graphs on nine vertices are covered in the repository's source unit-weight scope.
- P14's block/direct-sum factorization and two-separator transfer, together with the fixed-graph unit-to-positive-weight implication preserved from Cocks/Semple–Welsh, reduce a vertex-minimal source counterexample to a **3-connected** graph. This is a reduction, not closure.
- The P14 generic degree-three star/mesh route remains blocked: the mixed three-terminal polarization is not universally nonnegative, and the proposed reverse-Cauchy sufficient inequality was exactly refuted on a physical six-vertex graph while the true Rayleigh gap stayed positive.
- Erickson, `arXiv:1008.3660`, proves an SOS expression for the spanning-forest Rayleigh difference of every **series-parallel** graph, hence a stronger all-positive-weight independent-set-Rayleigh result in that class.
- Huang, `arXiv:2311.00965`, treats restricted arboreal-gas negative-correlation problems and still presents the general problem as open.
- Bado, DOI `10.1016/j.spl.2026.110960`, proves strict pairwise negative edge correlation for every wheel under the uniform-all-forests law.
- Tang–Zhang, `arXiv:2603.10738` (11 March 2026), prove p-NC for specified complete-graph spanning-subgraph ensembles, including forests with a **fixed number of components** for fixed `k` and sufficiently large `n`. This is not the arbitrary-graph uniform measure over all forests.

Thus a spanning-tree theorem, a complete-graph fixed-component theorem, and a series-parallel weighted theorem remain distinct from the parent T07 conjecture.

## 3. Three-terminal transfer retained from the previous run

Use terminal-connectivity states
\[
D=0|1|2,\quad P_{12}=0|12,\quad P_{01}=01|2,\quad P_{02}=02|1,\quad T=012.
\]

For one isolated right vertex,
\[
S=\begin{pmatrix}
4&1&1&1&1\\
0&4&0&0&2\\
0&0&4&0&2\\
0&0&0&4&2\\
0&0&0&0&4
\end{pmatrix},
\qquad N=S-4I,\qquad N^3=0.
\]

For a right `P4` with path edges `01,12,23`, exact local forest enumeration gives
\[
P=\begin{pmatrix}
734&780&780&780&2702\\
0&734&0&0&1560\\
0&0&734&0&1560\\
0&0&0&734&1560\\
0&0&0&0&734
\end{pmatrix}
=734I+780N+\frac{961}{3}N^2.
\]

Therefore for `p` unmarked `P4` layers and `r` singleton layers,
\[
P^pS^r=734^p4^r(I+uN+vN^2),
\]
where
\[
u=\frac{390}{367}p+\frac14r
\]
and
\[
v=\frac{961}{2202}p+\binom p2\left(\frac{390}{367}\right)^2+\binom r2\frac1{16}+pr\frac{195}{734}.
\]

The normalized all-forest count is consequently
\[
\frac{I_{F_{p,r}}(\mathbf1)}{734^p4^r}=\frac{7300800p^2+3435120pr+7502512p+404067r^2+1750957r+2155024}{2155024}.
\]

## 4. New sign mechanism: positive Newton cone plus one staircase orbit

Take a witness with two `P4` layers and two singleton layers. Terminal permutations, `P4` block permutations and reversals, and singleton permutations reduce every unordered pair of present edges to exactly **40** automorphism orbits.

After exposing the one or two layers containing a marked pair, let `x` be the number of remaining unmarked `P4` layers and `z` the number of remaining singleton layers. Marked-layer commutation from the previous report gives
\[
\Delta(e,f)=(734^x4^z)^2R_{\mathcal O}(x,z),
\]
where `R_O` is an exact rational polynomial of total degree at most four.

For **39 of the 40** orbits,
\[
R_{\mathcal O}(x,z)=\sum_{i+j\le4}c^{\mathcal O}_{ij}\binom xi\binom zj
\]
with every nonzero `c^O_{ij}>0`. Hence all those orbit gaps are nonnegative for every integer `x,z>=0`.

The unique orbit outside this Newton cone consists of two spokes in the **same `P4` block**, based at opposite endpoints, with different terminal labels. Its Newton expansion has exactly four negative coefficients:
\[
c_{0,3}=-\frac{639}{8},\qquad c_{1,2}=-\frac{39426483}{134689},
\]
\[
c_{2,1}=-\frac{51671772360}{49430863},\qquad c_{3,0}=-\frac{65267640734400}{18141126721}.
\]
So the component-size-3 proof mechanism does not simply extend by positive Newton coefficients.

### Lemma `T07-P4-SHIFTED-QUADRANT-SIGN-11`

Let `R_*(x,z)` be this exceptional normalized Rayleigh polynomial and let
\[
Q(x,z)=580516055072\,R_*(x,z).
\]
Then `Q(x,z)>0` for every pair of integers `x,z>=0`.

**Exact polynomial.**
\[
\begin{aligned}
Q={}&53301680640000x^4 +(50158248192000z-667904167756800)x^3\\
& +(17700074121600z^2-471591465995520z+40140592657736704)x^2\\
& +(2776037266080z^3-110993203020432z^2+18887949458515760z+128046701636391296)x\\
& +163270140489z^4-8707740826080z^3+2221907059661359z^2\\
& \qquad +30304824751937384z+96365665141952000.
\end{aligned}
\]

**Proof.** Partition the nonnegative integer quadrant into five shifted quadrants and a finite boundary staircase. The exact checker expands
\[
Q(4+X,Z),\quad Q(3+X,1+Z),\quad Q(2+X,5+Z),\quad Q(1+X,10+Z),\quad Q(X,14+Z)
\]
and verifies that all 15 ordinary monomial coefficients of each are strictly positive. Their minimum coefficients are respectively
\[
163270140489,\ 163270140489,\ 109736515860,\ 163270140489,\ 163270140489.
\]
These shifted quadrants cover all integer points except
\[
\{(0,z):0\le z<14\}\cup\{(1,z):0\le z<10\}\cup\{(2,z):0\le z<5\}\cup\{(3,0)\}.
\]
There are exactly `14+10+5+1=30` remaining points. Exact evaluation gives positive minima on the four rows
\[
96365665141952000,\ 263938356948963200,\ 508531032593867008,\ 828055127573162624.
\]
Therefore `Q>0` everywhere on `Z_{\ge0}^2`. QED.

This lemma is the new sign device of the run: **positive Newton certificates can fail at the first larger layer, while a finite staircase of positive shifted monomial cones still gives an all-parameter proof.**

## 5. New all-parameter graph theorem

### Theorem `T07-RIGHT-P4-FOREST-PNC-11`

For every `p,r>=0` and every two distinct present edges `e,f` of
\[
F_{p,r}=K_{3,\,4p+r}+\bigl(pP_4\sqcup rK_1\bigr),
\]
\[
\boxed{\Delta_{F_{p,r}}(e,f)\ge0.}
\]
The inequality is strict for every physical edge pair except the unique tree case `F_{0,1}=K_{3,1}`, where distinct edges are independent under the uniform forest law and the corresponding gap is zero.

**Proof.** Every physical edge pair belongs to one of the 40 witness orbits. Delete the one or two distinguished layers containing the pair; the remaining layer counts are nonnegative integers `(x,z)`. Marked-layer commutation moves the remaining layers to the end and factors out the strictly positive scalar `(734^x4^z)^2`. For 39 orbits, the resulting polynomial has a positive Newton expansion, so its value is nonnegative for every `x,z>=0`. The sole remaining orbit is strictly positive by `T07-P4-SHIFTED-QUADRANT-SIGN-11`. Exactly one of the 39 Newton-positive orbits has zero constant term: two distinct spokes of a singleton layer. Every nonzero Newton coefficient there is strictly positive, so equality requires no remaining layer at all, i.e. `p=0,r=1`. Every other orbit has positive constant term. QED.

The proof is symbolic in `p,r`; it is not finite extrapolation in graph order.

## 6. Essential exact checks

The executed exact checker reconstructs `S`, `P`, and all one-edge/two-edge marked transfer matrices by enumerating local acyclic subsets; verifies `N^3=0` and `P=734I+780N+(961/3)N^2`; verifies the closed all-forest count formula; constructs the automorphism action and exactly 40 edge-pair orbits; derives every orbit Rayleigh polynomial over `QQ`; verifies positive Newton coefficients for 39 orbits; identifies the four negative Newton coefficients of the unique exceptional orbit; verifies all coefficients in the five shifted exceptional polynomials are positive and evaluates all 30 uncovered boundary points exactly; and independently brute-forces physical examples:
- `F_{1,0}`: `n=7`, `m=15`, `Z=5776`, minimum gap `27300`;
- `F_{1,1}`: `n=8`, `m=18`, `Z=30720`, minimum gap `715536`;
- `F_{0,2}`: `n=5`, `m=6`, `Z=54`, minimum gap `36`.

The archived execution terminates with `ALL_EXACT_CHECKS_PASS`.

## 7. Why this is genuinely complementary and source-relevant

For every `p>=1`,
\[
|V|=3+4p+r,\qquad |E|=15p+3r.
\]
It is 3-connected: `K_{3,4p+r}` is 3-connected for `4p+r>=3`, and adding right-side edges cannot decrease connectivity. Thus the family lies directly in the structural regime surviving P14's minimal-counterexample reduction. It contains `K_{3,3}` for every `p>=1`, so it is nonplanar and not series-parallel; Erickson's theorem does not subsume it.

It is complementary to NM13-04 in two independent ways: the right side has genuine `P4` components, beyond the component-order-at-most-3 sign theorem; and the terminal triple is independent. For `p>=1`, this graph has clique number `3`, whereas every nontrivial graph in NM13-04's triangle-join family contains a `K4`. It is also genuinely beyond the preceding NM13-08 right-linear-forest theorem. For `p>=2`, the three terminals are the unique vertices of degree at least `8`; deleting them exposes `p` connected `P4` components, so the graph cannot be isomorphic to the earlier family whose exposed right components have order at most `3`.

The theorem therefore supplies a new unbounded 3-connected, non-series-parallel source-valid class rather than a reformulation of a spanning-tree or fixed-component result.

## 8. Failure learned and residual obstruction

The important negative result is structural: **positive multivariate Newton coefficients are not a universal marked-layer invariant once `P4` appears.** The unique opposite-endpoint/different-terminal spoke orbit is a concrete counterexample to that hoped-for closure.

The shifted-quadrant certificate rescues `P4`, but it is not yet a closure theorem for arbitrary internal right graphs. The next obstruction is whether a bounded staircase of positive shifted cones persists for `P_k` layers with `k>=5`, or whether some marked orbit eventually becomes genuinely negative.

A materially distinct next attack is therefore: compute the `P5` marked transfer orbit polynomials; first try to refute the staircase mechanism by searching for a negative integer parameter value; if no negative point exists, search for a finite shifted-quadrant cover with a proof-size bound derived from the degree-4 response algebra rather than ad hoc thresholds. No claim about `P5` is made in this run.

## 9. ledger_delta

```yaml
ledger_delta:
  slot: NM13-08
  parent: T07_uniform_forest_pairwise_negative_edge_correlation
  source_status_before: OPEN
  source_status_after: OPEN
  parent_complete_order_before: 9
  parent_complete_order_after: 9
  counterexample_order_lower_bound_before: 10
  counterexample_order_lower_bound_after: 10
  restricted_claim: T07-RIGHT-P4-FOREST-PNC-11
  restricted_status: CANDIDATE_FULL_PENDING_INDEPENDENT_REVIEW
  new_class: "F_{p,r}=K_{3,4p+r} + (p P4 disjoint_union r K1), all p,r>=0"
  new_sign_lemma: T07-P4-SHIFTED-QUADRANT-SIGN-11
  orbit_count: 40
  positive_newton_orbits: 39
  exceptional_orbits: 1
  exceptional_shift_regions: 5
  exceptional_boundary_points_checked_exactly: 30
  mechanism_before: "positive Newton cone for right components of order <=3"
  mechanism_after: "P4 controlled by 39 Newton-positive orbits plus one exact shifted-quadrant staircase certificate"
  exact_checker_result: ALL_EXACT_CHECKS_PASS
  residual_obstruction: "marked-layer sign control for P5 and arbitrary internal right graphs"
  next_attack: "P5 refutation-first marked-orbit scan, then bounded staircase certificate if no negative point"
  parent_closed: false
```

`END OF REPORT`

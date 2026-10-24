Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.**

# NM13-04 / T07 — strict p-NC for a triangle joined to an arbitrary right linear forest with components of order at most 3

Status: **PARTIAL on the parent Grimmett–Winkler conjecture / CANDIDATE_FULL for the restricted theorem below, pending later independent review.** The arbitrary-finite-graph uniform-all-forests conjecture remains OPEN.

Repository / branch: private `yspennstate/math-open-problems` / `master`  
Assigned root: `proofnet24/NM13-04/progress-forest/`  
Companion: NM13-08, `proofnet24/NM13-08/progress-forest-structure/`

## 0. Short handoff and same-run research choice

The preceding NM13-04 run proved strict p-NC for

\[
K_3\vee(M_k\sqcup I_r),
\]

using the five-state three-terminal transfer algebra and a triangle initial vector. That theorem is preserved. Its exact surviving gap was that the right-side internal graph had maximum degree at most one.

The newest relevant NM13-08 report, `2026-09-20T04-38-00Z__universal-three-terminal-layer-linear-forest-report.md`, then proved two facts that materially enlarge the available mechanism: every terminal-symmetric right layer has unmarked transfer in `span{I,N,N^2}`, and, for three independent terminals, arbitrary disjoint `P_3`, `K_2`, and `K_1` layers have a positive multivariate Newton certificate. NM13-08 identified the marked-edge sign cone, with `P_4` as its next frontier.

This run combines those complementary results rather than duplicating NM13-08's independent-terminal theorem. It seeds the same three right-layer species with the **left triangle** from NM13-04 and proves a new three-parameter all-parameter theorem. Core-edge/right-edge pairs are included, so this is not a direct corollary of the companion result.

`operations/PROGRESS20_2026-09-20.md` and the current LIVE20 mapping were checked: NM13-04 remains the T07 sign/deletion–contraction worker and NM13-08 the complementary decomposition worker. `POSTED.md` was checked through current repository search; the parent T07 conjecture and this restricted theorem are not treated as posted/settled claims.

## 1. Parent problem before/after, separately from mechanism gain

For a finite simple graph `G=(V,E)`, let

\[
I_G(\mathbf y)=\sum_{F\subseteq E:\,F\text{ acyclic}}\prod_{e\in F}y_e,
\qquad
\Delta_G(e,f)=I_eI_f-I_GI_{ef}.
\]

At unit weights, `Delta_G(e,f)>=0` is exactly pairwise negative edge correlation for a uniformly sampled acyclic spanning edge subset, with **all component counts mixed**.

**Parent source status:** `OPEN -> OPEN`.  
**Largest completely certified all-simple-graph order in repository continuity:** `9 -> 9`.  
**Equivalent lower bound on the order of a source-valid counterexample:** `>=10 -> >=10`.

No finite source-level coverage metric moves in this run.

**Mechanism before:** the 3-connected minimal-counterexample reduction from P14; NM13-04's triangle-plus-matching theorem; NM13-08's independent-terminal `P_3/K_2/K_1` theorem and universal three-terminal layer algebra.

**Mechanism after:** a complete exact sign theorem for

\[
G_{p,m,r}:=K_3\vee\bigl(pP_3\sqcup mK_2\sqcup rK_1\bigr),
\qquad p,m,r\ge0.
\]

Every distinct present edge pair has **strictly positive** Rayleigh difference. This is symbolic in all three parameters and is not finite graph-order enumeration.

## 2. Recovered P14 proof history and failed routes

The P14 mandatory handoff and the newest NM13-04 report were reread as the essential predecessor state.

Preserved successful reductions:

1. Grimmett–Winkler published unit-weight verification for all graphs on at most eight vertices and for nine-vertex graphs with at most eighteen edges.
2. Repository exact work covers the complementary dense nine-vertex sector, so all simple graphs through nine vertices are covered in the source unit-weight scope.
3. Block/direct-sum factorization reduces a vertex-minimal counterexample to 2-connected.
4. The two-separator transfer, together with the fixed-graph unit-to-positive-weight implication preserved from Cocks/Semple–Welsh, reduces a vertex-minimal source counterexample further to **3-connected**.

Preserved failed routes, not retried here:

- the generic degree-three apex/star-mesh route leaves a mixed three-terminal polarization;
- that mixed polarization is not universally nonnegative;
- the proposed reverse-Cauchy rescue `C^2 <= 4 Delta_A Delta_K` was exactly refuted on a physical six-vertex graph even though the true physical Rayleigh gap stayed positive;
- Lorentzian/complete-log-concavity, naive real-stability perturbation, and Gårding shortcuts still lack a verified source-matching hypothesis for arbitrary graphic independence polynomials.

The new theorem does not claim to solve that arbitrary response-cone obstruction. It proves that a substantially larger explicit 3-connected response family stays inside a positive Newton cone.

## 3. Current literature scope check — 20 September 2026

Fresh bounded public checks were made against the exact source scopes.

- Grimmett–Winkler, `arXiv:math/0302185` / *Random Structures & Algorithms* 24 (2004), study the uniform measure on **all forests** and verify p-NC numerically through eight vertices and for nine-vertex graphs with at most 18 edges. They explicitly distinguish the already-known uniform-spanning-tree law.
- Erickson, `arXiv:1008.3660`, proves a stronger all-positive-weight independent-set-Rayleigh statement for **series-parallel** graphs using an SOS formula.
- Huang, `arXiv:2311.00965`, studies restricted arboreal-gas graphs/parameters and describes the general negative-correlation problem as open.
- Bado, DOI `10.1016/j.spl.2026.110960`, proves strict p-NC for every wheel. The article is indexed in *Statistics & Probability Letters* 241 (2027) with the DOI assigned in 2026; wheels are 3-connected and non-series-parallel but do not subsume the family below.
- Tang–Zhang, `arXiv:2603.10738` (11 March 2026), prove p-NC for specified complete-graph spanning-subgraph ensembles including forests with a **fixed number of components** for fixed `k` and sufficiently large `n`; this is not the arbitrary-graph all-component uniform-forest measure.
- Tang–Zhang, `arXiv:2609.11578` (10 September 2026), prove negative correlation for a high-degree regular random-cluster regime. Their `Q=0` endpoint is Bernoulli bond percolation conditioned to be **connected**, not the uniform-all-forest law.

A bounded search did not surface the exact `K_3 join (linear forest with components <=3)` theorem. This is negative evidence only; **novelty/priority remains UNVERIFIED**.

## 4. New graph class and theorem

Let the left vertices be `L={0,1,2}` and include the triangle `01,02,12`. On the right take a disjoint union of `p` copies of `P_3`, `m` copies of `K_2`, and `r` isolated vertices. Join every right vertex to all three left vertices.

Thus

\[
|V(G_{p,m,r})|=3+3p+2m+r,
\qquad
|E(G_{p,m,r})|=3+11p+7m+3r.
\]

### Theorem `T07-TRIANGLE-RIGHT-LINEAR-FOREST-PNC-11`

For every `p,m,r>=0` and every two distinct present edges `e,f` of `G_{p,m,r}`,

\[
\boxed{\Delta_{G_{p,m,r}}(e,f)>0.}
\]

Hence the uniform measure on **all forests** of every `G_{p,m,r}` has strict pairwise negative edge correlation.

When `3p+2m+r>=1`, the graph is 3-connected: deleting fewer than three vertices leaves a surviving left-triangle vertex adjacent to every surviving right vertex and to every surviving left vertex. It contains a `K_4` subgraph as soon as one right vertex exists, so every nontrivial member is outside the series-parallel class. If `p>=1`, it contains `K_{3,3}` and is nonplanar.

The specialization `p=0` recovers the preceding NM13-04 triangle-plus-matching theorem. The new regime is `p>=1`, where right vertices of degree two inside the right induced graph are allowed.

## 5. Three-terminal transfer algebra

Use the five terminal-connectivity states

\[
D=0|1|2,\quad P_{12}=0|12,\quad P_{01}=01|2,\quad P_{02}=02|1,\quad T=012.
\]

For a singleton right vertex, a right `K_2`, and a right `P_3`, exact local enumeration gives

\[
S=
\begin{pmatrix}
4&1&1&1&1\\
0&4&0&0&2\\
0&0&4&0&2\\
0&0&0&4&2\\
0&0&0&0&4
\end{pmatrix},
\]

\[
T_2=
\begin{pmatrix}
23&12&12&12&22\\
0&23&0&0&24\\
0&0&23&0&24\\
0&0&0&23&24\\
0&0&0&0&23
\end{pmatrix},
\]

and

\[
T_3=
\begin{pmatrix}
130&103&103&103&273\\
0&130&0&0&206\\
0&0&130&0&206\\
0&0&0&130&206\\
0&0&0&0&130
\end{pmatrix}.
\]

Writing `N=S-4I`, one has `N^3=0`, and

\[
T_2=23I+12N+\frac53N^2,
\qquad
T_3=130I+103N+\frac{85}{3}N^2.
\]

The triangle core contributes the initial row vector

\[
q=(1,1,1,1,3).
\]

Therefore, after factoring `130^p23^m4^r`, the unmarked right-layer product is

\[
U=I+uN+vN^2,
\]

where

\[
u=\frac{103p}{130}+\frac{12m}{23}+\frac r4
\]

and

\[
\begin{aligned}
v={}&\frac{17p}{78}+\frac{5m}{69}
+\binom p2\left(\frac{103}{130}\right)^2
+\binom m2\left(\frac{12}{23}\right)^2
+\binom r2\frac1{16}\\
&+pm\frac{103}{130}\frac{12}{23}
+pr\frac{103}{520}+mr\frac3{23}.
\end{aligned}
\]

Since `q 1=7`, `qN1=10`, and `qN^2 1=6`, the all-forest count has the closed form

\[
I_{G_{p,m,r}}(\mathbf1)=130^p23^m4^r\bigl(7+10u+6v\bigr).
\]

## 6. Complete sign argument via a universal two-copy witness

Fix a distinct edge pair `e,f`. It uses the triangle core and at most two right components. Expose exactly the right component(s) containing `e` or `f`. By NM13-08's marked-layer commutation lemma, all remaining unmarked layers may be moved after these distinguished marked layers without changing the counted edge sets.

Let `x,y,z` be the numbers of remaining `P_3`, `K_2`, and `K_1` layers after the distinguished component(s) have been consumed. After removing the positive scalar factor `(130^x23^y4^z)^2`, every marked forest count is a fixed row vector times

\[
I+u(x,y,z)N+v(x,y,z)N^2,
\]

so it has total degree at most two in `x,y,z`. Hence every normalized Rayleigh difference is a rational polynomial

\[
R_{e,f}(x,y,z)
\]

of total degree at most four.

To cover every possible local edge-pair type without relying on a fragile hand-written orbit list, form one finite witness containing:

- the left triangle;
- two copies of a right `P_3` layer;
- two copies of a right `K_2` layer;
- two copies of a right `K_1` layer.

This witness has exactly 45 edges. Any edge pair in any `G_{p,m,r}` maps to one of its `C(45,2)=990` witness pairs after relabeling the three terminals, permuting equal right components, and reversing a `P_3` or swapping the endpoints of a `K_2` when needed.

For each of those 990 witness pairs the checker reconstructs, directly from local forest subsets, the four distinguished transfer objects needed for `I`, `I_e`, `I_f`, `I_ef`. It then evaluates the degree-at-most-four polynomial on the exact finite-difference grid and expands

\[
R_{e,f}(x,y,z)=
\sum_{i+j+k\le4}c_{ijk}
\binom xi\binom yj\binom zk.
\]

The coefficients `c_{ijk}` are exact rational forward differences, not fitted floating-point values.

The executed certificate checks

\[
990\binom{4+3}{3}=990\cdot35=34650
\]

Newton coefficients. Results:

- positive coefficients: `13850`;
- zero coefficients: `20800`;
- negative coefficients: **`0`**;
- minimum positive Newton coefficient: `1/8`;
- minimum constant coefficient `c_000` over all 990 pair types: **`2`**.

Therefore every `R_{e,f}(x,y,z)` is strictly positive for all nonnegative integers `x,y,z`: every basis function is nonnegative and the constant term is uniformly positive. Multiplying back by `(130^x23^y4^z)^2>0` proves the theorem.

This is an exact finite certificate for the finite **local type algebra**, followed by a symbolic all-parameter transfer. It is not finite enumeration of graph sizes.

## 7. Independent small-instance brute checks

The same executable also performs direct subset enumeration of complete graphs in three nontrivial parameter cases, independently of the transfer/Newton certificate:

- `(p,m,r)=(1,0,0)`: `n=6`, `|E|=14`, `I=2110`, minimum Rayleigh gap `7066`;
- `(0,1,1)`: `n=6`, `|E|=13`, `I=1466`, minimum gap `1372`;
- `(1,0,1)`: `n=7`, `|E|=17`, `I=10358`, minimum gap `52332`.

The archived executable output ends `ALL_EXACT_CHECKS_PASS`.

Artifacts created before this report:

- checker commit `7c37ad62c943646dd964bd1cbf1f6015629154fb`;
- output commit `d2d094e5bff0afb56bfb8446620d4ae628dde60c`;
- local executed SHA-256 values before upload: checker `be2545a4c4b6b1473dc68999331c0f9191c82cb1b9060ad8f6018f2efa0ebadc`, output `709d6980f20ad205b7639da52ab6d63d80811ba8cfbc95c56bcc0cd0bee99d2c`.

## 8. What this does and does not solve

**Gain:** the triangle-core theorem now tolerates an arbitrary disjoint union of right components of sizes 1, 2, and 3, including right `P_3` components. This strictly contains the preceding NM13-04 family and combines nontrivially with NM13-08's universal three-terminal layer algebra.

**Parent problem:** unchanged. The theorem still assumes a three-vertex dominating clique and a highly structured right induced graph. It does not control an arbitrary 3-connected graph and therefore does not close the P14 minimal-counterexample obstruction.

**No source-valid counterexample was found.** The exact sign certificate points the other way on this new class.

The companion NM13-08 report identifies `P_4` as the next marked-layer frontier: its unmarked transfer is already known to be

\[
734I+780N+\frac{961}{3}N^2,
\]

but the required marked-edge positive cone is not yet proved there. A useful next NM13-04 attack is therefore complementary rather than duplicative: keep the triangle seed and test whether the `P_4` marked orbit polynomials admit a shifted-Newton/SOS certificate, or else isolate the first exact sign failure as a counterexample-search template.

## 9. ledger_delta

```yaml
ledger_delta:
  track: NM13-04
  parent: T07
  source: "Grimmett-Winkler uniform-all-forests pairwise edge negative correlation"
  parent_status_before: OPEN
  parent_status_after: OPEN
  parent_metric: "largest completely certified all-simple-graph order"
  parent_before: 9
  parent_after: 9
  source_counterexample_order_lower_bound_before: ">=10"
  source_counterexample_order_lower_bound_after: ">=10"
  mechanism_before: "strict p-NC for K3 join (matching + isolates); companion independent-terminal P3/K2/K1 theorem"
  mechanism_after: "strict p-NC for K3 join (p P3 disjoint_union m K2 disjoint_union r K1), all p,m,r>=0"
  theorem_id: T07-TRIANGLE-RIGHT-LINEAR-FOREST-PNC-11
  theorem_scope: "G_{p,m,r}=K3 join (pP3 disjoint_union mK2 disjoint_union rK1), every distinct present edge pair"
  proof_core: "five-state nilpotent transfer + 990-pair universal local witness + exact positive multivariate Newton certificate"
  exact_newton_coefficients_checked: 34650
  exact_negative_newton_coefficients: 0
  minimum_constant_rayleigh_coefficient: 2
  checker_commit: 7c37ad62c943646dd964bd1cbf1f6015629154fb
  output_commit: d2d094e5bff0afb56bfb8446620d4ae628dde60c
  status: "PARTIAL parent / CANDIDATE_FULL restricted theorem"
  residual_obstruction: "arbitrary 3-connected three-terminal response; next explicit frontier P4 marked-layer sign cone"
  companion_coordination: "uses NM13-08 universal layer algebra and P3 marked-sign theorem; does not overwrite peer files"
  next_attack: "triangle-seeded P4 marked orbit cone: shifted Newton/SOS certificate or exact sign-failure template"
```

`END OF REPORT`

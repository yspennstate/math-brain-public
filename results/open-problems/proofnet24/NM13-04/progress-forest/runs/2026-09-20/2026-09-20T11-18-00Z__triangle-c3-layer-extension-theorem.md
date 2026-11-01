Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED.**

# NM13-04 / T07 — response-strip insertion theorem and a cyclic right-layer extension

Status: **PARTIAL on the parent Grimmett–Winkler conjecture / CANDIDATE_FULL for the restricted theorem below, pending later independent review.** Novelty/priority: **UNVERIFIED**. The arbitrary-finite-graph uniform-all-forests conjecture remains OPEN.

Repository / branch: private `yspennstate/math-open-problems` / `master`  
Assigned root: `proofnet24/NM13-04/progress-forest/`  
Companion: NM13-08, `proofnet24/NM13-08/progress-forest-structure/`

## 0. Short handoff and substantive move

The preceding NM13-04 run proved strict p-NC for

\[
K_3\vee H,
\qquad H=\bigsqcup_{\ell=1}^{15} n_\ell P_\ell,
\]

with all fifteen multiplicities arbitrary. Its proof compressed every collection of unmarked right components into a two-dimensional response strip

\[
U=I+uN+vN^2,
\qquad
v=\frac{u^2}{2}-hu,
\qquad
\rho_{15}\le h\le \frac18,
\]

where `N^3=0`; 10,814 local marked-pair types were Bernstein-positive and 203 exceptional same-path spoke types were closed by an exact discriminant identity.

The latest relevant NM13-08 work owns the complementary decomposition / terminal-symmetric layer algebra. In particular, it established the five-state `span{I,N,N^2}` mechanism for terminal-symmetric right layers and the independent-terminal response-strip program. This run does not duplicate that seed. It uses the triangle seed `q=(1,1,1,1,3)` and asks a different question: can a genuinely cyclic right component be inserted arbitrarily many times without widening the already-certified strip?

The answer is yes for a right-side triangle. This is the first NM13-04 extension in the current sequence that leaves the class of right linear forests.

Essential dependencies read: `operations/PROGRESS20_2026-09-20.md`, current LIVE20 ownership, the preceding NM13-04 order-15 response-strip report, the P14 mandatory handoff preserving the 3-connected reduction and failed generic routes, the latest indexed NM13-08 response-strip / path-recurrence reports, and `POSTED.md`. No historical or peer file was modified.

## 1. Parent problem before/after, separately from mechanism gain

For a finite graph `G=(V,E)` write

\[
I_G(\mathbf y)=\sum_{F\subseteq E:\,F\text{ acyclic}}\prod_{e\in F}y_e,
\qquad
\Delta_G(e,f)=I_eI_f-I_GI_{ef}.
\]

At unit weights, `Delta_G(e,f)>=0` is exactly pairwise negative correlation of distinct edge indicators under the uniform measure on **all** acyclic spanning edge subsets.

**Parent source status:** `OPEN -> OPEN`.  
**Largest completely certified all-simple-graph order in repository continuity:** `9 -> 9`.  
**Equivalent source-valid lower bound on a counterexample order:** `>=10 -> >=10`.

No finite census is promoted to a general theorem.

**Mechanism before:** right side an arbitrary disjoint union of paths `P_1,...,P_15`.

**Mechanism after:** right side may additionally contain an arbitrary number of triangles:

\[
\boxed{
G=K_3\vee H,
\qquad
H=mK_3\;\sqcup\;\bigsqcup_{\ell=1}^{15}n_\ell P_\ell,
\qquad m,n_1,\dots,n_{15}\ge0.
}
\]

All sixteen multiplicities are independent and unbounded. The new one-parameter subfamily `K_3 vee (m K_3)` has

\[
|V|=3+3m,
\qquad
|E|=3+12m.
\]

For `m>=2` it is noncomplete and exactly 3-connected: deleting the three left-clique vertices disconnects the right triangles, while deleting any two vertices leaves a left-clique vertex adjacent to every surviving right vertex. Every nontrivial member contains `K_4`, so this is not a series-parallel consequence.

## 2. Preserved P14 proof state and failed routes

The inherited P14 boundary remains unchanged and is not silently retried.

1. Grimmett–Winkler plus the repository dense-nine completion cover every simple graph through nine vertices in the unit all-forest scope.
2. Forest factorization over blocks reduces a vertex-minimal counterexample to a 2-connected graph.
3. P14's two-separator transfer, together with its fixed-graph unit-to-positive-weight implication, reduces a vertex-minimal source counterexample further to a **3-connected** graph.
4. The generic degree-three apex / star-mesh route leaves a mixed three-terminal polarization with no universal sign.
5. Universal positivity of that mixed term is false.
6. The proposed reverse-Cauchy rescue was exactly refuted on a six-vertex physical apex graph although the true Rayleigh gap there remained positive.
7. Naive real-stability, Lorentzian / complete-log-concavity, and Gårding shortcuts still lack the required hypothesis for arbitrary graphic independence polynomials.

The present theorem enlarges a structured exactly-3-connected region but does not remove the arbitrary 3-connected obstruction.

## 3. Current source scope check

A bounded 20 September 2026 source check continues to separate nearby laws.

- Grimmett–Winkler, `arXiv:math/0302185` / RSA 24 (2004), formulate the uniform-**all-forests** edge-correlation conjecture and report numerical verification for every graph on at most eight vertices and every nine-vertex graph with at most eighteen edges. They explicitly distinguish the already-known spanning-tree law.
- Erickson, `arXiv:1008.3660`, proves the stronger positive-weight Rayleigh / SOS statement for **series-parallel** graphs.
- Tang–Zhang, `arXiv:2603.10738` (11 March 2026), prove p-NC for specified uniform spanning-subgraph ensembles of `K_n`, including forests with exactly `k` components for fixed `k` and sufficiently large `n`; this is not the arbitrary-graph all-component uniform-forest law.
- Tang–Zhang, `arXiv:2609.11578` (10 September 2026), prove negative correlation in high-degree regular random-cluster regimes; their `Q=0` endpoint is Bernoulli percolation conditioned to be connected, not uniform all forests.
- Bado, DOI `10.1016/j.spl.2026.110960`, proves strict unit p-NC for wheel graphs, another infinite 3-connected non-series-parallel family.

A bounded search for the exact `K_3`-join / disjoint-right-triangle extension below did not locate it. That is negative evidence only; novelty remains **UNVERIFIED**.

## 4. Response-strip insertion lemma

The mechanism is slightly more general than the single new component.

### Lemma `T07-RESPONSE-STRIP-INSERTION-21`

Fix the triangle seed `q=(1,1,1,1,3)` and the five terminal-partition states used in the predecessor theorem. Suppose a family of allowed unmarked right components has normalized transfers

\[
I+a_jN+c_jN^2,
\qquad a_j>0,
\qquad N^3=0,
\]

with

\[
\rho_j:=\frac{a_j^2/2-c_j}{a_j}\in[\alpha,\beta].
\]

Suppose further that every already-allowed marked local edge-pair response is strictly positive on the strip

\[
\mathcal S_{\alpha,\beta}
=
\left\{
(u,v):u\ge0,
\ v=\frac{u^2}{2}-hu,
\ h\in[\alpha,\beta]
\right\}.
\]

Let `B` be a new terminal-symmetric right component with normalized transfer `I+a_BN+c_BN^2`, with `a_B>0` and `rho_B in [alpha,beta]`. If every local marked pair involving at least one edge of `B`—core/`B`, same `B`, two distinct copies of `B`, and `B`/old-component—is strictly positive on the same strip, then arbitrary many disjoint copies of `B` may be added to the right side while preserving strict p-NC.

### Proof

For normalized factors `I+a_jN+c_jN^2`, nilpotence gives

\[
\prod_j(I+a_jN+c_jN^2)=I+uN+vN^2,
\]

where

\[
u=\sum_j a_j,
\qquad
v=\sum_j c_j+\sum_{i<j}a_ia_j.
\]

Therefore

\[
\frac{u^2}{2}-v
=
\sum_j\left(\frac{a_j^2}{2}-c_j\right)
=
\sum_j\rho_j a_j.
\]

If `u>0`, then

\[
h:=\frac{u^2/2-v}{u}
=\frac{\sum_j\rho_ja_j}{\sum_j a_j}
\in[\alpha,\beta]
\]

is a positive weighted average. Thus adding unmarked copies of `B` cannot leave the strip.

For a marked pair `e,f`, expose the one or two components containing the marked edges, together with any marked left-clique edges. Every remaining component contributes only the common unmarked response `U=I+uN+vN^2`. If neither marked edge lies in `B`, strict positivity is the assumed old strip theorem. If at least one marked edge lies in `B`, strict positivity is exactly one of the new local hypotheses. This exhausts all edge pairs. QED.

This lemma is a finite-response decomposition theorem: it turns one checked component into an arbitrary-multiplicity extension without any finite graph-order inference.

## 5. Exact right-triangle transfer

Let `B=C_3=K_3` on three right vertices, and join each of those three vertices to all three left terminals. Exact forest-state enumeration gives

\[
T_{C_3}
=
\begin{pmatrix}
178&144&144&144&390\\
0&178&0&0&288\\
0&0&178&0&288\\
0&0&0&178&288\\
0&0&0&0&178
\end{pmatrix}
=178I+144N+41N^2.
\]

Hence

\[
a_{C_3}=\frac{144}{178}=\frac{72}{89},
\qquad
c_{C_3}=\frac{41}{178},
\]

and

\[
\boxed{
\rho_{C_3}
=\frac{a_{C_3}^2/2-c_{C_3}}{a_{C_3}}
=\frac{1535}{12816}.
}
\]

The predecessor lower strip endpoint is

\[
\rho_{15}
=
\frac{13162845795778912063}{109915919585249991540}.
\]

Exact subtraction gives

\[
\rho_{C_3}-\rho_{15}
=
\frac{2158737054683334541}{117390202117046990964720}>0,
\]

and

\[
\frac18-\rho_{C_3}=\frac{67}{12816}>0.
\]

Therefore the right triangle lies **strictly inside** the old strip `[rho_15,1/8]`; arbitrary unmarked copies do not widen it at all.

## 6. Exhaustive new marked local responses

It remains only to check local pairs involving at least one edge from a right triangle. Old/old marked pairs are already certified on the entire predecessor strip and therefore remain valid after adding unmarked triangles.

Modulo simultaneous `S_3` permutation of the left terminals, permutation of the three vertices inside each right triangle, path reversal, and exchange of two distinct right-triangle copies, the exact new local marked types are:

- left-core edge / right-triangle edge: `3` orbits;
- two edges in the same right triangle: `6` orbits;
- one edge in each of two distinct right triangles: `4` orbits;
- one right-triangle edge / one edge in a path `P_l`, `1<=l<=15`: `304` orbits.

Total:

\[
\boxed{317}
\]

new local response polynomials.

For every such marked pair, after exposing its touched component(s), each of `I,I_e,I_f,I_ef` is affine in `(u,v)`. Thus

\[
\Delta(e,f)=Q(u,v)
\]

has degree at most two in `(u,v)`. Substitute

\[
v=\frac{u^2}{2}-hu,
\qquad h\in[\rho_{15},1/8],
\]

and write

\[
R(u,h)=\sum_{j=0}^{4}c_j(h)u^j,
\]

where each `c_j` has degree at most two in `h`.

The exact checker computes the degree-two Bernstein coefficients of every nonzero `c_j` on `[rho_15,1/8]`. For **all 317 new local polynomials**, every Bernstein coefficient is nonnegative and the constant term is strictly positive. The minimum constant is

\[
\boxed{13052},
\]

and the minimum positive Bernstein coefficient is

\[
\boxed{270}.
\]

Therefore every `c_j(h)>=0` on the whole strip and `c_0(h)>0`, so `R(u,h)>0` for every physical `u>=0`. There are **zero exceptional new orbits** and no auxiliary corner or discriminant repair is needed for this cyclic layer.

## 7. New all-parameter theorem

### Theorem `T07-TRIANGLE-CYCLIC-RIGHT-16PARAM-21`

Let

\[
H=mK_3\sqcup\bigsqcup_{\ell=1}^{15}n_\ell P_\ell
\]

be any finite graph whose components are triangles or paths of order at most fifteen. Then for

\[
G=K_3\vee H
\]

and every two distinct present edges `e,f`,

\[
\boxed{\Delta_G(e,f)>0.}
\]

Hence the uniform measure on **all** spanning forests of every such graph has strict pairwise negative edge correlation.

### Proof

The predecessor theorem supplies strict positivity for the class with `m=0` uniformly on the response strip `[rho_15,1/8]`. Section 5 proves that the unmarked right-triangle transfer has `rho_C3` strictly inside that strip. Section 6 verifies every new local marked type involving a right triangle on the same strip. Apply the response-strip insertion lemma from Section 4 with `B=C_3`. QED.

This theorem is genuinely outside the predecessor topology: the right side is no longer a linear forest and may contain an unbounded number of cycles.

## 8. Independent brute-force sanity check

The checker independently enumerates all `2^18` edge subsets of

\[
K_3\vee(K_3\sqcup K_1),
\]

rejects cyclic subsets by union-find, and accumulates all one-edge and two-edge forest counts. It obtains

\[
I(\mathbf1)=14372,
\]

matching the transfer calculation exactly, and over all `153` unordered edge pairs finds

\[
\min\Delta=82772,
\qquad
\max\Delta=8228516.
\]

This is only a sanity check. The theorem for unbounded multiplicities comes from the strip insertion proof and the exhaustive finite local response classification, not from finite graph-size enumeration.

## 9. Exact executable and actual output

Checker:

`proofnet24/NM13-04/progress-forest/runs/2026-09-20/2026-09-20T11-18-00Z__triangle-c3-layer-extension-checker.py`

creation commit:

`dd38b46df1e0e25f9a20ce1e411300f220e08ad3`.

Executed output:

`proofnet24/NM13-04/progress-forest/runs/2026-09-20/2026-09-20T11-18-00Z__triangle-c3-layer-extension-checker.out`

creation commit:

`e536ae9ef7bf9c5b8623097a7fb22edaf2b9dfdf`.

The archived output ends

`ALL_EXACT_CHECKS_PASS`.

Essential exact output:

- `T_C3 = 178 I + 144 N + 41 N^2`;
- `rho_C3 = 1535/12816`;
- strict inclusion `rho_15 < rho_C3 < 1/8` with both exact positive margins archived;
- `317` exhaustive new local orbits;
- `317` Bernstein-positive, `0` failures;
- minimum new constant `13052`;
- minimum positive new Bernstein coefficient `270`;
- independent brute-force count `14372` and minimum gap `82772` on `K3 vee (K3 disjoint K1)`.

## 10. Honest failure / residual obstruction

The recurrence-first attack from the preceding report has **not** yet been completed: there is still no proof here that `rho_l` stays positive/decreasing for every path length or that every same-path exceptional discriminant remains positive uniformly in `l`. Accordingly the arbitrary-linear-forest theorem still has path-component cutoff fifteen.

This run instead changed topology and proved a new cyclic-layer insertion theorem. No source-valid counterexample was found. The parent conjecture and arbitrary 3-connected response obstruction remain open.

A useful next attack is to abstract the exact marked-response condition in the insertion lemma into a reusable `strip-admissible component` cone and test the first genuinely longer cyclic layers `C_4,C_5,...`. If their unmarked `rho` values remain in the same strip and the marked local cone closes uniformly, that could lead to a right-side cactus or bounded-treewidth component theorem. In parallel, NM13-08 remains the natural owner of the complementary generic terminal-symmetric decomposition and path-tail recurrence theory.

## 11. ledger_delta

```yaml
ledger_delta:
  track: NM13-04
  parent: T07
  parent_status_before: OPEN
  parent_status_after: OPEN
  complete_all_simple_graph_order_before: 9
  complete_all_simple_graph_order_after: 9
  source_counterexample_order_lower_bound_before: 10
  source_counterexample_order_lower_bound_after: 10
  predecessor_mechanism: "triangle-seeded K3 join arbitrary mixtures of P1,...,P15"
  mechanism_after: "response-strip insertion lemma plus arbitrary right-triangle multiplicity; K3 join (m K3 disjoint union sum_{l<=15} n_l P_l)"
  new_restricted_claim: T07-TRIANGLE-CYCLIC-RIGHT-16PARAM-21
  new_restricted_status: CANDIDATE_FULL_PENDING_INDEPENDENT_REVIEW
  genuinely_new_topology: "right side may contain an unbounded number of cycles; not a linear forest"
  new_layer_transfer: "T_C3 = 178 I + 144 N + 41 N^2"
  new_layer_rho: "1535/12816"
  strip_inclusion: "rho_15 < rho_C3 < 1/8"
  new_local_orbits: 317
  new_local_bernstein_positive: 317
  new_local_failures: 0
  minimum_new_constant: 13052
  minimum_positive_new_bernstein_coefficient: 270
  brute_sanity_graph: "K3 vee (K3 disjoint K1)"
  brute_sanity_forest_count: 14372
  brute_sanity_min_gap: 82772
  p14_preserved_min_counterexample_structure: "3-connected"
  unresolved_parent_obstruction: "arbitrary 3-connected mixed three-terminal response"
  recurrence_uniform_in_path_length: UNRESOLVED
  checker_commit: dd38b46df1e0e25f9a20ce1e411300f220e08ad3
  output_commit: e536ae9ef7bf9c5b8623097a7fb22edaf2b9dfdf
  runtime_model: "GPT-5.6 Sol"
  reasoning_effort: UNVERIFIED
  novelty: UNVERIFIED
```

`END OF REPORT`

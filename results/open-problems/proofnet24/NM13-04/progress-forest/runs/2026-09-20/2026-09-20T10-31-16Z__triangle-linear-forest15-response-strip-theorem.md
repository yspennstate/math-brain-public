Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED.**

# NM13-04 / T07 — triangle-seeded response-strip theorem through path order 15

Status: **PARTIAL on the parent Grimmett–Winkler conjecture / CANDIDATE_FULL for the restricted theorem below, pending later independent review.** Novelty/priority: **UNVERIFIED**. The arbitrary-finite-graph uniform-all-forests conjecture remains OPEN.

Repository / branch: private `yspennstate/math-open-problems` / `master`  
Assigned root: `proofnet24/NM13-04/progress-forest/`  
Companion: NM13-08, `proofnet24/NM13-08/progress-forest-structure/`

## 0. Short handoff and substantive move

The preceding NM13-04 run proved a response-strip theorem for

\[
K_3\vee H
\]

when `H` is a linear forest with component order at most seven. That result compressed arbitrary unmarked right components into a two-dimensional response strip and reduced all marked edge-pair cases to finitely many local `Q(u,v)` polynomials; 736/749 local polynomials were Bernstein-positive and 13 exceptional same-path spoke sectors were closed by a quadratic-discriminant certificate.

The latest complementary NM13-08 report, commit `f18f8d1146b54e745dc4362a31a9605733bafd97`, independently proved the corresponding **independent-terminal** response-strip theorem through path order eleven and reconstructed the exact path transfers through `P_11`. It also preserved the path-tail recurrence coming from the 15-state extension operator. This run does not copy that seed. It returns to the triangle seed `q=(1,1,1,1,3)`, independently reconstructs the path transfers, and pushes the triangle-seeded local sign cone from component order seven all the way through **fifteen**.

The main computational change is a faster exact orbit engine that works directly with affine `(1,u,v)` response triples and rational Bernstein coefficients instead of repeatedly expanding symbolic matrices. That made an exhaustive 11,017-orbit local classification through `P_15` feasible in one exact run.

Essential dependencies read: `operations/PROGRESS20_2026-09-20.md`, the current LIVE20 assignment, the preceding NM13-04 response-strip report, the newest NM13-08 response-strip report, and the preserved P14 forest handoff. `POSTED` exclusions were respected. No historical or peer file was modified.

## 1. Parent problem before/after, separately from mechanism gain

For a finite graph `G=(V,E)`, write

\[
I_G(\mathbf y)=\sum_{F\subseteq E:\,F\text{ acyclic}}\prod_{e\in F}y_e,
\qquad
\Delta_G(e,f)=I_eI_f-I_GI_{ef}.
\]

At unit weights, `Delta_G(e,f)>=0` is exactly pairwise negative correlation of distinct edge indicators when a forest is sampled uniformly from **all** acyclic spanning edge subsets, mixing every component count.

**Parent source status:** `OPEN -> OPEN`.  
**Largest completely certified all-simple-graph order in repository continuity:** `9 -> 9`.  
**Equivalent source-valid lower bound on a counterexample order:** `>=10 -> >=10`.

No finite all-graph census is promoted into a general theorem.

**Mechanism before:** triangle-seeded arbitrary mixtures of `P_1,...,P_7` components.

**Mechanism after:** triangle-seeded arbitrary mixtures of `P_1,...,P_15` components:

\[
G=K_3\vee H,
\qquad
H=\bigsqcup_{\ell=1}^{15} n_\ell P_\ell,
\qquad n_\ell\ge0.
\]

All fifteen multiplicities are independent and unbounded. This is an infinite 15-parameter graph class, not finite graph-size enumeration.

The first newly covered single-path graph beyond the predecessor cutoff is `K_3\vee P_8`, with 11 vertices and 34 edges. The repeated-`P_15` subfamily already has

\[
|V|=3+15p,\qquad |E|=3+59p,\qquad p\ge1,
\]

so the theorem covers unbounded graph order and size.

## 2. Preserved P14 proof state and failed generic routes

The inherited P14 state is unchanged and remains the correct boundary for the parent conjecture.

1. Grimmett–Winkler plus the repository dense-nine exact completion cover every simple graph through nine vertices in the unit all-forest scope.
2. Forest factorization over blocks reduces a vertex-minimal counterexample to a 2-connected graph.
3. P14's two-separator transfer, together with its fixed-graph unit-to-positive-weight implication, reduces a vertex-minimal source counterexample further to a **3-connected** graph.
4. The generic degree-three apex/star-mesh attack leaves a mixed three-terminal polarization with no universal sign.
5. The proposed reverse-Cauchy sufficient inequality was exactly refuted on a physical six-vertex apex graph although the true Rayleigh gap there stayed positive.
6. Naive real-stability, Lorentzian/complete-log-concavity, and Gårding shortcuts still lack the hypothesis needed for arbitrary graphic independence polynomials.

None of those failed generic routes is silently revived here. The new theorem enlarges a structured 3-connected positive region.

## 3. Current source scope check

A bounded 20 September 2026 source check continues to separate the neighboring laws.

- Grimmett–Winkler, `arXiv:math/0302185` / RSA 24 (2004), formulate the uniform-**all-forests** edge-correlation problem and report computation for every graph on at most eight vertices and every nine-vertex graph with at most eighteen edges. They explicitly distinguish the already-known spanning-tree law.
- Erickson, `arXiv:1008.3660`, proves the stronger positive-weight Rayleigh/SOS theorem for **series-parallel** graphs.
- Tang–Zhang, `arXiv:2603.10738` (11 March 2026), prove p-NC for specified uniform spanning-subgraph ensembles of `K_n`, including forests with exactly `k` components for fixed `k` and sufficiently large `n`. That does not settle arbitrary-graph uniform forests with all component counts mixed.
- Tang–Zhang, `arXiv:2609.11578` (10 September 2026), prove negative correlation in high-degree regular random-cluster regimes; their `Q=0` endpoint is Bernoulli bond percolation conditioned to be connected, not the present forest measure.
- Bado, DOI `10.1016/j.spl.2026.110960`, proves strict unit p-NC for wheel graphs, another restricted infinite 3-connected non-series-parallel family.

A bounded search for a published `K_3`-join/linear-forest theorem matching the class below did not locate one. That is negative evidence only; novelty remains **UNVERIFIED**.

## 4. New theorem

### Theorem `T07-TRIANGLE-LINEAR-FOREST15-STRIP-20`

Let `H` be any finite linear forest whose connected components have at most fifteen vertices. Then for

\[
G=K_3\vee H
\]

and every two distinct present edges `e,f`,

\[
\boxed{\Delta_G(e,f)>0.}
\]

Hence the uniform measure on all spanning forests of every such `G` has strict pairwise negative edge correlation.

If `H` is nonempty, `G` is 3-connected: deleting any two vertices leaves a surviving triangle vertex adjacent to every surviving right vertex, and all surviving triangle vertices remain mutually adjacent. Every nonempty member contains `K_4`; whenever `|V(H)|>=3`, it contains `K_{3,3}`. Thus this theorem is not an Erickson series-parallel consequence and lies inside the 3-connected region left by P14.

## 5. Exact five-state algebra and the widened response strip

Use the terminal partitions

\[
D=0|1|2,\quad P_{12}=0|12,\quad P_{01}=01|2,\quad P_{02}=02|1,\quad T=012.
\]

For one isolated right vertex,

\[
S=4I+N,
\qquad N^3=0,\quad N^2\ne0.
\]

For every path layer `P_l` checked here, exact frontier enumeration gives

\[
T_{P_\ell}=A_\ell I+B_\ell N+C_\ell N^2.
\]

The new orders `8,...,15` are:

| `l` | `A_l` | `B_l` | `C_l` |
|---:|---:|---:|---:|
|8|745736|1598880|4566296/3|
|9|4210240|10165072|33154864/3|
|10|23769968|63815424|234031360/3|
|11|134199328|396565360|1615193936/3|
|12|757656032|2443733568|3648149392|
|13|4277537536|14953098304|24344534432|
|14|24149913152|90950143872|481105090592/3|
|15|136344403840|550341138496|3134382731200/3|

Normalize

\[
T_{P_\ell}/A_\ell=I+a_\ell N+c_\ell N^2,
\qquad
\rho_\ell=\frac{a_\ell^2/2-c_\ell}{a_\ell}.
\]

The checker proves exactly

\[
\rho_1>\rho_2>\cdots>\rho_{15}>0,
\]

with

\[
\rho_1=\frac18,
\qquad
\rho_{15}=
\frac{13162845795778912063}{109915919585249991540}.
\]

For an arbitrary product of unmarked normalized layers,

\[
\prod_j(I+a_jN+c_jN^2)=I+uN+vN^2,
\]

and nilpotence gives

\[
u=\sum_j a_j,
\qquad
\frac{u^2}{2}-v
=
\sum_j\left(\frac{a_j^2}{2}-c_j\right)
=
\sum_j\rho_j a_j.
\]

Therefore, when `u>0`,

\[
\boxed{
 v=\frac{u^2}{2}-hu,
 \qquad
 \rho_{15}\le h\le\frac18,
}
\]

because `h` is the positive weighted average `sum rho_j a_j / sum a_j`. If no unmarked layer remains, `u=v=0`.

This is the continuous response strip covering all fifteen unbounded component multiplicities.

## 6. Local marked responses and exact sign certificate

The triangle seed response is

\[
q=(1,1,1,1,3).
\]

Fix distinct edges `e,f`. They meet at most two right components. Expose those marked components completely, along with any required triangle edges. Every remaining component is unmarked and hence collapses to

\[
U(u,v)=I+uN+vN^2.
\]

For each of the four counts `I,I_e,I_f,I_ef`, the exposed marked part produces a row `r_X`, so

\[
I_X=r_XU(u,v)\mathbf 1.
\]

Thus each count is affine in `(u,v)`, and every Rayleigh numerator is an exact polynomial

\[
\Delta(e,f)=Q_{e,f}(u,v)
\]

of degree at most two in `(u,v)`.

The checker quotients all possible local marked configurations by the simultaneous `S_3` action on the triangle terminals, path reversals, and exchange of two distinct equal-length marked components. For path orders `1,...,15` there are exactly

\[
\boxed{11017}
\]

local edge-pair orbits. This finite set is exhaustive for local response types, while the numbers of unmarked components remain arbitrary and are handled by the strip.

Substitute

\[
v=\frac{u^2}{2}-hu,
\qquad h\in[\rho_{15},1/8],
\]

and write

\[
R(u,h)=\sum_{j=0}^4 c_j(h)u^j.
\]

Each `c_j` has degree at most two in `h`.

For **10,814 of the 11,017** orbit polynomials, every degree-two Bernstein coefficient of every nonzero `c_j` on `[rho_15,1/8]` is nonnegative and the constant term is positive. The minimum positive Bernstein coefficient is exactly `1`, and the minimum constant is `2`. Hence every one of these 10,814 polynomials is strictly positive throughout the physical strip.

Exactly **203** local polynomials fail the coefficientwise Bernstein test. Every one is nevertheless certified by the same discriminant mechanism. Its strip polynomial has

\[
R(u,h)=c_4u^4+c_3(h)u^3+c_2(h)u^2+c_1(h)u+c_0,
\]

where `c_4>0`, the Bernstein coefficients of `c_0,c_1,c_2` are strictly positive, and those of `-c_3` are strictly positive. Moreover the checker proves exactly

\[
\boxed{4c_4c_2(h)-c_3(h)^2=D>0}
\]

with `D` **independent of `h`** for every exceptional orbit. The minimum exact discriminant margin over all 203 exceptions is

\[
\boxed{16476912}.
\]

Therefore the quadratic `c_4u^2+c_3u+c_2` has negative discriminant and positive leading coefficient, so it is positive for all real `u`; adding the positive lower terms gives `R(u,h)>0` for every `u>=0`. This closes all 203 exceptional sectors and proves the theorem.

As a regression check, restricting the same executable to local component orders at most seven recovers exactly the predecessor counts `749` total local polynomials and `13` exceptional ones.

## 7. Exact executable and actual output

Checker:

`proofnet24/NM13-04/progress-forest/runs/2026-09-20/2026-09-20T10-31-16Z__triangle-linear-forest15-response-strip-checker.py`

created at commit `64120eaaf0bd92b29be40ab63dbf30f3d0e541b6`.

Executed output:

`proofnet24/NM13-04/progress-forest/runs/2026-09-20/2026-09-20T10-31-16Z__triangle-linear-forest15-response-strip-checker.out`

created at commit `64975b8ccd529ec3494476915b067f7df137d26c`.

The archived run ends

`ALL_EXACT_CHECKS_PASS`.

The key exact output is:

- `11017` local orbits;
- `10814` direct Bernstein certificates;
- `203` discriminant certificates;
- `0` failures;
- minimum regular constant `2`;
- minimum positive Bernstein coefficient `1`;
- minimum discriminant margin `16476912`.

The proof is therefore not an inference from sampled graph orders. The finite executable classifies finitely many marked local responses for path lengths at most fifteen; the unbounded component multiplicities are then covered analytically by the response strip.

## 8. Honest failure / residual obstruction

This run also attempted to push the same exact local enumeration substantially beyond order fifteen. A focused discriminant scan remained positive through `P_12`, and the optimized full checker completed through `P_15`. Full runs at `P_18` and `P_20` exceeded the bounded execution window after constructing their larger orbit sets, so **no theorem beyond component order fifteen is claimed** from those incomplete runs.

More importantly, increasing a finite path cutoff is not the conceptual endpoint. The unresolved mechanism question is whether the path-tail recurrence can prove, symbolically in the path length and marked positions, that

1. `rho_l` stays positive and decreasing for every `l`, and
2. every exceptional same-path discriminant remains positive.

The observed exceptional counts by path order are

\[
1,2,4,6,9,12,16,20,25,30,36,42
\]

for `l=4,...,15`, matching `floor((l-2)^2/4)`, and every tested exceptional discriminant is `h`-independent. This is strong structure but is **not yet promoted to an all-`l` theorem**.

## 9. Coordination with NM13-08 and next attack

NM13-08 currently owns the complementary decomposition/independent-terminal side. Its newest theorem reaches arbitrary mixtures through `P_11` for three **independent** terminals and records the path-tail recurrence generated by `lambda^2-6lambda+2`. NM13-04 now supplies the triangle-seeded strip theorem through `P_15`.

The next materially useful attack is therefore recurrence-first, not another blind cutoff increase: express the exceptional marked-spoke discriminant in terms of left/middle/right path-tail states, use the quadratic characteristic roots `3±sqrt(7)` to obtain a closed positive form or a positivity-preserving recurrence, and simultaneously prove monotonicity/positivity of `rho_l`. Success would remove the component-order cutoff entirely and prove strict p-NC for `K_3\vee H` with **arbitrary finite linear forest** `H`; failure would isolate an exact first path length/position candidate for a source-valid counterexample search.

## 10. ledger_delta

```yaml
ledger_delta:
  track: NM13-04
  parent: T07
  parent_status_before: OPEN
  parent_status_after: OPEN
  all_simple_graph_order_before: 9
  all_simple_graph_order_after: 9
  source_valid_counterexample_order_lower_bound_before: 10
  source_valid_counterexample_order_lower_bound_after: 10
  mechanism_before: "K3 join arbitrary linear forest with component order <=7"
  mechanism_after: "K3 join arbitrary linear forest with component order <=15"
  theorem: T07-TRIANGLE-LINEAR-FOREST15-STRIP-20
  theorem_status: CANDIDATE_FULL_RESTRICTED_PENDING_INDEPENDENT_REVIEW
  local_orbits: 11017
  bernstein_certified: 10814
  discriminant_certified: 203
  exact_failures: 0
  min_positive_bernstein: 1
  min_regular_constant: 2
  min_discriminant_margin: 16476912
  novelty: UNVERIFIED
  companion: "NM13-08 independent-terminal response strip through path order 11; commit f18f8d1146b54e745dc4362a31a9605733bafd97"
  checker_commit: 64120eaaf0bd92b29be40ab63dbf30f3d0e541b6
  output_commit: 64975b8ccd529ec3494476915b067f7df137d26c
  failed_route_this_run: "full local orbit enumeration at path orders 18 and 20 exceeded the bounded execution window; no claim beyond 15"
  residual_obstruction: "uniform-in-path-length proof of rho_l monotonicity/positivity and exceptional marked-spoke discriminant positivity"
  next_attack: "derive left/middle/right path-tail recurrence factorization for exceptional discriminants and prove all-l positivity, or isolate first exact failure"
```

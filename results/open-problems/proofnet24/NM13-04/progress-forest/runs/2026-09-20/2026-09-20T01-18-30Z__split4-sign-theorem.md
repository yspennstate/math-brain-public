Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.**

# NM13-04 / T07 — 15-state sign theorem for the complete split graphs `K_4 ∨ \overline{K_n}`

Status: **PARTIAL on the parent problem / CANDIDATE_FULL for the restricted all-parameter theorem below, pending later independent review.** The arbitrary-finite-graph Grimmett–Winkler conjecture remains OPEN. No source-valid counterexample was found.

Repository/branch: private `yspennstate/math-open-problems` / `master`  
Assigned root: `proofnet24/NM13-04/progress-forest/`  
Companion: NM13-08, `proofnet24/NM13-08/progress-forest-structure/`

## 0. Short handoff from the predecessor run

The preceding NM13-04 substantive run proved strict pairwise negative edge correlation for every complete split graph

\[
K_3\vee\overline{K_n},\qquad n\ge1,
\]

using the five partitions of three clique terminals and the nilpotent transfer `M=4I+N`, `N^3=0`. That result did **not** change the parent all-graph source metric, but it gave a genuine infinite 3-connected non-series-parallel family and a way around P14's failed generic degree-three apex inequality.

This run keeps the parent problem and P14 history fixed and pushes the mechanism one full connectivity/treewidth level higher. The new core is

\[
G_n:=K_4\vee\overline{K_n}.
\]

For `n>=2` this is a noncomplete 4-connected graph; for every `n>=1` it contains `K_5` as a subgraph and hence lies strictly outside the series-parallel class. The proof uses all `B_4=15` terminal partitions and gives exact positive Rayleigh numerators in all seven edge-pair orbits.

`POSTED.md` was checked. The parent conjecture and this split-graph theorem are not listed as posted/settled claims.

## 1. Parent problem before/after, separate from mechanism gain

For a finite simple graph `G=(V,E)`, let

\[
I_G(\mathbf y)=\sum_{F\subseteq E:\,F\text{ acyclic}}\prod_{e\in F}y_e.
\]

At unit weights write `Z=I_G(1)`, `Z_e=I_e(1)`, and `Z_{ef}=I_{ef}(1)`. Pairwise negative edge correlation for the uniform measure on all forests is exactly

\[
\Delta_G(e,f):=Z_eZ_f-ZZ_{ef}\ge0.
\]

**Parent source status:** OPEN `->` OPEN.  
**Largest completely certified all-graph order:** `9 -> 9`.  
Equivalently, the source-level lower bound on the order of a counterexample remains `>=10 -> >=10`.

This run is therefore **not** a source-level metric advance and is not reported as one.

**Mechanism scope before:** strict p-NC for all `K_3∨\overline{K_n}`.  
**Mechanism scope after:** strict p-NC for all `K_4∨\overline{K_n}` by a complete 15-state theorem, plus the transparent-theta substitutions described in §7.

The state-space rank has increased from the five partitions of three terminals to all fifteen partitions of four terminals, and the proved core family has increased from 3-connected to 4-connected.

## 2. Recovered P14 proof history and exact failed routes

The P14 mandatory handoff was reread rather than reconstructed from memory. The following facts remain the relevant inherited baseline.

Successful preserved facts:

1. Grimmett–Winkler plus the repository dense-nine computation certify every simple graph through nine vertices at unit forest weights.
2. Forest factorization over blocks reduces a vertex-minimal counterexample to a 2-connected graph.
3. The two-separator transfer, together with the fixed-graph unit-to-positive-weight implication used by P14, upgrades the minimal-counterexample reduction to 3-connected.
4. One-edge-field quadratics are exact and useful auxiliary invariants.

Failed or insufficient routes that remain failed:

1. partial ten-vertex enumeration does not move the source metric;
2. the generic degree-three star/mesh elimination leaves an old-edge/old-edge mixed three-terminal polarization term;
3. that mixed term is not universally nonnegative;
4. the proposed reverse-Cauchy sufficient inequality was exactly refuted on a six-vertex physical graph even though the physical source Rayleigh gap stayed positive;
5. Lorentzian / complete-log-concavity information does not by itself imply the needed entrywise Hessian sign;
6. the naive real-stability perturbation fails, and the Gårding shortcut still lacks the required verified hypothesis for arbitrary graphic independence polynomials.

I did not retry any of these killed generic routes. The present proof closes only because repeated independent-side vertices keep the entire outside response inside a finite partition lattice.

## 3. Current literature scope checked this run

A bounded 20 September 2026 source/status check recovered the following exact distinctions.

* Grimmett–Winkler, `math/0302185`, is the arbitrary finite-graph unit-weight forest conjecture and verifies all graphs through eight vertices plus nine-vertex graphs with at most eighteen edges.
* Erickson, `arXiv:1008.3660`, proves the stronger weighted I-Rayleigh property for series-parallel graphs.
* Idriss Olivier Bado, *Negative edge correlation for uniform random forests on wheel graphs*, DOI `10.1016/j.spl.2026.110960`, now online, proves strict p-NC for every wheel by a `2 x 2` transfer method. Wheels are 3-connected and non-series-parallel, but are not the split family below.
* Tang–Zhang, `arXiv:2603.10738` (11 March 2026), treat specified spanning-subgraph families of `K_n`, including forests with exactly `k` components for fixed `k` and sufficiently large `n`; this is not the all-component-count forest law on arbitrary graphs.
* Tang–Zhang, `arXiv:2609.11578` (10 September 2026), prove restricted high-degree random-cluster negative-correlation results. Their `Q=0` endpoint is described as Bernoulli percolation conditioned to be connected, not the uniform measure on all acyclic edge subsets. It does not settle T07.

Fresh bounded searches for combinations of `uniform forest`, `negative correlation`, `complete split graph`, `K_4 join independent set`, and `K_{4,n}` did not surface the theorem below. That is negative evidence only. **Novelty/priority remains UNVERIFIED.**

## 4. New theorem

### Theorem `T07-SPLIT4-SIGN-02`

For every integer `n>=1`, let

\[
G_n=K_4\vee\overline{K_n}.
\]

Under the uniform measure on **all** acyclic spanning edge subsets of `G_n`, every two distinct edges are strictly negatively correlated:

\[
\boxed{\Delta_{G_n}(e,f)>0\qquad(e\ne f).}
\]

For `n>=2` these are noncomplete 4-connected graphs. Every member contains `K_5`, so the theorem is not an instance of Erickson's series-parallel result.

## 5. Fifteen-state partition transfer

Let the clique terminals be `C={1,2,3,4}` and process the `n` independent-side vertices one at a time. In a partial forest, retain only the partition `pi` of `C` induced by connectivity.

When a new independent vertex is joined to a subset `A subseteq C`, the extension is acyclic **iff** `A` meets every block of `pi` in at most one element. Indeed, choosing two terminals already in one block creates a cycle through their existing forest path and the two new spokes; conversely, if all chosen terminals lie in distinct blocks, the new vertex merely merges those tree components through a new star and cannot create a cycle.

For a legal `A`, let `pi*A` be the partition obtained by merging exactly the blocks hit by `A`. Define the `15 x 15` integer transfer matrix

\[
M_{\pi,\sigma}
=\#\{A\subseteq C:\ A\text{ legal for }\pi,\ \pi*A=\sigma\}.
\tag{5.1}
\]

There are exactly five legal choices that leave every state unchanged: `A=emptyset` and the four singleton sets. Every other legal choice strictly coarsens the partition. Therefore

\[
M=5I+N,
\tag{5.2}
\]

where every nonzero entry of `N` moves strictly upward in the partition lattice. A partition of four points can be strictly coarsened at most three times, so

\[
N^4=0.
\tag{5.3}
\]

Hence for every `n>=0`,

\[
M^n=
5^nI+n5^{n-1}N+\binom n2 5^{n-2}N^2+\binom n3 5^{n-3}N^3.
\tag{5.4}
\]

This is the algebraic reason every count below is `5^n` times a polynomial of degree at most three before the Rayleigh products are formed.

### Initial `K_4` vectors

Use the partition order

`1|2|3|4`,
`12|3|4`, `13|2|4`, `14|2|3`, `23|1|4`, `24|1|3`, `34|1|2`,
`123|4`, `124|3`, `134|2`, `234|1`,
`12|34`, `13|24`, `14|23`,
`1234`.

The unmarked `K_4` forest vector is

\[
u=(1,1,1,1,1,1,1,3,3,3,3,1,1,1,16).
\tag{5.5}
\]

For a fixed clique edge `12`, the marked vector is

\[
u_{12}=(0,1,0,0,0,0,0,2,2,0,0,1,0,0,8).
\tag{5.6}
\]

For adjacent marked clique edges `12,13` and disjoint marked clique edges `12,34`, respectively,

\[
u_{12,13}=(0,0,0,0,0,0,0,1,0,0,0,0,0,0,3),
\tag{5.7}
\]

\[
u_{12,34}=(0,0,0,0,0,0,0,0,0,0,0,1,0,0,4).
\tag{5.8}
\]

These vectors may also be read directly from Cayley's tree count inside each partition block; the checker independently enumerates all `2^6=64` subsets of the clique and recovers totals `38,14,4,5` for (5.5)–(5.8).

For a marked spoke to terminal `i`, let `E_i` be the same transfer as (5.1), but summing only legal subsets `A` containing `i`. For two marked spokes on the same new independent vertex, let `E_{ij}` sum only legal `A` containing both `i,j`.

By symmetry there are exactly seven pair orbits:

1. two adjacent clique edges;
2. two disjoint clique edges;
3. a clique edge and an incident spoke;
4. a clique edge and a nonincident spoke;
5. two spokes at the same independent-side vertex;
6. two spokes at distinct independent-side vertices with the same clique endpoint;
7. two spokes at distinct independent-side vertices with different clique endpoints.

Let `1` be the all-ones column. The required counts are therefore

\[
\begin{aligned}
Z&=uM^n\mathbf1,\\
Z_c&=u_{12}M^n\mathbf1,\\
Z_{cc}^{A}&=u_{12,13}M^n\mathbf1,\\
Z_{cc}^{D}&=u_{12,34}M^n\mathbf1,\\
Z_s&=uE_1M^{n-1}\mathbf1,\\
Z_{cs}^{I}&=u_{12}E_1M^{n-1}\mathbf1,\\
Z_{cs}^{N}&=u_{12}E_3M^{n-1}\mathbf1,\\
Z_{ss}^{R}&=uE_{12}M^{n-1}\mathbf1,\\
Z_{ss}^{L}&=uE_1E_1M^{n-2}\mathbf1,\\
Z_{ss}^{D}&=uE_1E_2M^{n-2}\mathbf1.
\end{aligned}
\tag{5.9}
\]

The last two rows apply for `n>=2`.

Substituting (5.4) into (5.9) and multiplying the fixed integer operators gives

\[
Z=\frac{5^n}{125}(16n^3+327n^2+2182n+4750),
\tag{5.10}
\]

\[
Z_c=\frac{5^n}{25}(8n^2+107n+350),
\tag{5.11}
\]

\[
Z_{cc}^{A}=\frac{5^n}{5}(3n+20),\qquad
Z_{cc}^{D}=\frac{5^n}{5}(4n+25),
\tag{5.12}
\]

\[
Z_s=\frac{5^n}{625}(16n^3+399n^2+3166n+8044),
\tag{5.13}
\]

\[
Z_{cs}^{I}=\frac{5^n}{125}(8n^2+121n+446),
\qquad
Z_{cs}^{N}=\frac{5^n}{125}(8n^2+141n+576),
\tag{5.14}
\]

\[
Z_{ss}^{R}=\frac{5^n}{125}(8n^2+121n+446),
\tag{5.15}
\]

and, for `n>=2`,

\[
Z_{ss}^{L}=\frac{5^n}{3125}(16n^3+471n^2+4216n+11806),
\tag{5.16}
\]

\[
Z_{ss}^{D}=\frac{5^n}{3125}(16n^3+471n^2+4416n+13156).
\tag{5.17}
\]

## 6. Exact Rayleigh signs in all seven orbits

For every orbit, the unit Rayleigh numerator is `Z_eZ_f-ZZ_{ef}`. Using (5.10)–(5.17) gives:

\[
\Delta_{cc}^{A}
=\frac{5^{2n}}{625}
(16n^4+411n^3+3963n^2+17010n+27500),
\tag{6.1}
\]

\[
\Delta_{cc}^{D}
=\frac{2\,5^{2n}}{625}
(2n^3+73n^2+675n+1875),
\tag{6.2}
\]

\[
\Delta_{cs}^{I}
=\frac{2\,5^{2n}}{15625}
(176n^4+4731n^3+47450n^2+210443n+348450),
\tag{6.3}
\]

\[
\Delta_{cs}^{N}
=\frac{2\,5^{2n}}{15625}
(16n^4+421n^3+4375n^2+21113n+39700),
\tag{6.4}
\]

\[
\Delta_{ss}^{R}
=\frac{5^{2n}}{390625}
(256n^6+9568n^5+146713n^4+1179901n^3
+5246068n^2+12236558n+11743436),
\tag{6.5}
\]

\[
\Delta_{ss}^{L}
=\frac{6\,5^{2n}}{390625}
(688n^4+18771n^3+190924n^2+857986n+1437906),
\tag{6.6}
\]

\[
\Delta_{ss}^{D}
=\frac{2\,5^{2n}}{390625}
(464n^4+12813n^3+133847n^2+626108n+1107468).
\tag{6.7}
\]

Every coefficient in every displayed polynomial is strictly positive. Thus every available orbit has positive Rayleigh numerator for every admissible `n` (`n>=1`, with the two distinct-right-vertex orbits present only for `n>=2`). This proves `T07-SPLIT4-SIGN-02`. QED.

## 7. Coordination with NM13-08: transparent theta substitution now starts from 4-connected split cores

NM13-08's newest report proves exact series/parallel terminal-activity calculus and constructs, for each `ell>=2`, a unit-transparent two-terminal gadget `A_ell` consisting of

\[
r_\ell=2^\ell-1
\]

internally disjoint paths of length `ell` in parallel. At unit weights its virtual activity is exactly `t(A_ell)=1`, its port-interface determinants are nonnegative, and the completed gadget `A_ell+g` is series-parallel and therefore I-Rayleigh by Erickson. NM13-08's previously proved port-substitution theorem therefore preserves unit p-NC when such a gadget replaces an edge of a unit-p-NC core.

Combining that theorem with `T07-SPLIT4-SIGN-02` gives a new joint all-parameter family: start from any `G_n=K_4∨\overline{K_n}` and replace any chosen distinct core edges by independently chosen theta gadgets `A_{ell_j}`. Every resulting graph is unit p-NC.

If `k` distinct original core edges are replaced once, with lengths `ell_1,...,ell_k`, then

\[
|V|=n+4+\sum_{j=1}^k(2^{\ell_j}-1)(\ell_j-1),
\tag{7.1}
\]

\[
|E|=4n+6-k+\sum_{j=1}^k\ell_j(2^{\ell_j}-1).
\tag{7.2}
\]

This uses NM13-08's decomposition theory rather than duplicating it: NM13-04 supplies a larger 4-connected unbounded seed family; NM13-08 supplies the sign-preserving edge-expansion mechanism.

## 8. Exact checker and executed output

Essential code and output were saved before this report:

* `proofnet24/NM13-04/progress-forest/runs/2026-09-20/2026-09-20T01-18-30Z__split4_checker.py` — creation commit `a723982ca9debab68095e3f5e059be2a5654abd3`.
* `proofnet24/NM13-04/progress-forest/runs/2026-09-20/2026-09-20T01-18-30Z__split4_checker.out` — creation commit `d803ce666ff783c3b180a84cd518b1b553705d7f`.

The checker is standard-library-only and uses exact integer arithmetic. It independently:

1. constructs all fifteen set partitions and the legal one-vertex transfer;
2. verifies `N^3 != 0` and `N^4=0` for `N=M-5I`;
3. derives the transfer counts numerically and matches every closed formula above for every `1<=n<=20`;
4. brute-force enumerates **every edge subset and every distinct edge pair** for `n=1,2,3` and matches the seven orbit formulas exactly.

Archived output ends:

```
transfer-vs-closed formulas: PASS for n=1..20
full brute-force all edge pairs: PASS for n=1,2,3
ALL_EXACT_CHECKS_PASS
```

The finite checks are only verification of the algebra. The theorem for arbitrary `n` is the nilpotent partition-transfer proof plus the positive-coefficient formulas (6.1)–(6.7), not finite enumeration.

## 9. What failed / residual obstruction / next attack

No new source counterexample appeared in this run, and the chosen 15-state route succeeded. The generic P14 apex/deletion-contraction obstruction remains untouched: an arbitrary 4-terminal environment is not constrained to the repeated split-vertex transfer cone, so this theorem does not imply the all-graph conjecture.

The decisive residual question suggested by the calculation is whether the pattern continues for

\[
K_r\vee\overline{K_n}
\]

with `r` variable rather than fixed. For fixed `r`, the same exact transfer has `B_r` partition states and `M=(r+1)I+N` with `N^r=0`; what is **not** proved is that every pair-orbit Rayleigh polynomial remains positive uniformly in both `r` and `n`.

**Next attack:** compute the full exact sign polynomials for `r=5` and `r=6` only as reconnaissance, then either (a) identify a partition-lattice identity proving positivity for all `r,n`, which would be a materially stronger two-parameter theorem, or (b) use the first sign failure to isolate an exact counterexample candidate. Do not count finite `r` checks as a general theorem.

## 10. `ledger_delta`

```yaml
ledger_delta:
  track: NM13-04
  parent: T07
  source: "Grimmett-Winkler uniform-forest pairwise edge negative correlation"
  parent_status_before: OPEN
  parent_status_after: OPEN
  source_metric: "largest vertex order for which every simple graph is completely certified at unit forest weights"
  source_metric_before: 9
  source_metric_after: 9
  smallest_possible_counterexample_order_before: ">=10"
  smallest_possible_counterexample_order_after: ">=10"
  source_level_movement: "none"
  theorem_id: T07-SPLIT4-SIGN-02
  theorem_scope: "all K_4 join independent-set graphs K_4 ∨ overline(K_n), n>=1"
  theorem_status: "CANDIDATE_FULL restricted theorem; later independent review pending"
  mechanism_before: "5-state theorem for K_3 ∨ overline(K_n)"
  mechanism_after: "15-state theorem for K_4 ∨ overline(K_n), all seven edge-pair orbits strictly positive"
  companion_gain: "NM13-08 transparent theta gadgets can now be substituted into arbitrary chosen edges of these 4-connected split cores"
  exact_checker: "ALL_EXACT_CHECKS_PASS; transfer formulas n=1..20; full brute force n=1..3"
  unchanged_substantive_runs: 0
  failed_recovery_routes: 0
  residual_obstruction: "arbitrary 3-connected/4-terminal environments need not lie in the repeated split-vertex partition-transfer cone"
  next_attack: "test r=5,6 then seek a two-parameter partition-lattice positivity theorem or exact sign failure for K_r ∨ overline(K_n)"
```

`END OF REPORT`

Model actually run: **GPT-5.6 Sol**. Reasoning level: **UNVERIFIED**. GPT-6 maximum was requested, but this execution does not authenticate GPT-6/maximum and no writable model/effort selector is exposed. **Source status OPEN -> OPEN; complete-all-graphs order metric 9 -> 9; structural complete-tripartite metric advances from “two smallest parts sum <=6” to “two smallest parts sum <=7”.**

# PROB10-07 — complete tripartite fixed-width-seven Rayleigh theorem

Repository/branch: private `yspennstate/math-open-problems` / `master`  
Parent: Grimmett–Winkler pairwise edge negative correlation for the uniform measure on **all forests**  
Status: **PARTIAL / universal conjecture OPEN**  
Artifact stem: `20260920T0644Z_tripartite-sum7-f31c`

## 1. Continuity, ownership boundary, and consumed evidence

Before fixing scope, this run read the controlling `operations/PROB10_2026-09-20.md`, current `POSTED.md`, and the complete newest parent-owner handoffs:

- P14: `proofnet24/P14-probability-correlation/runs/2026-09-17/2026-09-17T05-19-47Z__mandatory-handoff-report.md`, blob `bed2241d948b8a20b854efc248ccf5b46b4325cd`;
- HARD10-01: `proofnet24/HARD10-01/runs/2026-09-16/2026-09-16T21-16-42Z__report.md`, blob `d95d0b06d9eedb6f9edd8557d7e292267074d492`;
- newest own predecessor: `runs/prob10_2026-09-20/PROB10-07/20260920T0540Z_tripartite-sum6-d2a7.md`;
- preserved pre-refocus R13 handoff: `runs/R13/20260919T2345Z_handoff-to-PROB10-07-forest.md`.

P14/HARD10-01 retain ownership/history of the complete arbitrary-graph order-nine census, minimal-counterexample reduction to 3-connected graphs, and the surviving three-terminal/mixed-environment obstruction. This run does **not** repeat graph-order enumeration, does not move the order metric, and does not seize their structural claims. It continues only PROB10-07's separate complete-tripartite repeated-part transfer route.

A non-mutating handoff back to that owner history was written at

`artifacts/prob10_2026-09-20/PROB10-07/20260920T0644Z_tripartite-sum7-f31c_forest-owner-handoff.md`

creation commit `fdcf690d334f9c00c4760f1acb26e0461f635500`.

The mathematical idea was written **before** production coding at

`artifacts/prob10_2026-09-20/PROB10-07/20260920T0644Z_tripartite-sum7-f31c_idea.md`

creation commit `702032d0b96a60b8701d0a51232ea03c0151041a`.

No shared root ledger, peer report, scheduler, cadence, enabled state, workflow, permission, email, Drive, or public-posting state was changed.

## 2. Exact source statement and metrics

For a finite graph `G=(V,E)`, let `F(G)` be the set of all acyclic edge subsets, with isolated vertices allowed and all component counts mixed. Set

\[
Z=|F(G)|,\qquad
Z_e=|\{F\in F(G):e\in F\}|,\qquad
Z_{ef}=|\{F\in F(G):e,f\in F\}|.
\]

For the uniform all-forests law,

\[
\Pr(e)\Pr(f)-\Pr(e,f)
=\frac{Z_eZ_f-ZZ_{ef}}{Z^2}.
\]

Thus the source-exact pairwise question is

\[
\boxed{\Delta_G(e,f):=Z_eZ_f-ZZ_{ef}\ge0.}
\tag{2.1}
\]

This is not a uniform spanning-tree law, random minimum spanning tree, connected-subgraph law, or fixed-component forest ensemble.

Source-level metrics:

- universal arbitrary-graph status: `OPEN -> OPEN`;
- complete arbitrary-graph vertex order in repository continuity: `9 -> 9`;
- exact counterexample: `none -> none`;
- complete-tripartite structural range: `two smallest parts sum <=6 -> <=7`.

Auxiliary mechanism gain: marked repeated vertices are now handled by exact forced-spoke operators, eliminating the previous joint enumeration of the fixed core together with one or two marked stars.

## 3. Current source/prior-art screen

The bounded current screen rechecked the following distinctions.

1. Grimmett–Winkler, `https://arxiv.org/abs/math/0302185` / Random Structures & Algorithms 24 (2004), is the arbitrary finite-graph uniform-all-forests source. Its published computation covers all graphs through eight vertices and the nine-vertex sector through eighteen edges.
2. Erickson, `https://arxiv.org/abs/1008.3660`, gives a stronger positive-weight Rayleigh theorem for the established series-parallel class. That is a baseline, not this run's result.
3. Tang–Zhang, `https://arxiv.org/abs/2603.10738`, treats specified uniform spanning-subgraph families of `K_n`, including forests with exactly fixed `k` components for sufficiently large `n`; it is not the arbitrary-graph all-component measure here.
4. Bado, DOI `10.1016/j.spl.2026.110960`, proves strict pairwise negative correlation for wheel graphs by a `2 x 2` transfer matrix; wheels are a distinct 3-connected non-series-parallel family.

Fresh searches combining `complete tripartite`, `uniform forest`, `negative correlation`, `Rayleigh`, and the concrete family `K_{1,6,n}` did not surface this theorem. The searches did surface the known series-parallel, complete-graph/fixed-component, and wheel results above. This is bounded negative evidence only. **Novelty/priority of the theorem below remains UNVERIFIED.**

## 4. Three materially different approaches compared before coding

### Route A — deletion/contraction closed form

For a tested edge `e`, graphic-matroid contraction gives `Z_e(G)=Z(G/e)`, and similarly for two required edges. A direct proof would therefore follow from a tractable closed form for the unrooted all-forest partition functions of the contracted complete-multipartite multigraphs.

The obstruction is real: contraction identifies terminals and creates parallel edge classes. The recovered chain contains no source-safe closed formula for the required **unrooted** all-forest counts of these contracted multigraphs. The matrix-forest determinant counts rooted forests and cannot be substituted. This route was not promoted.

### Route B — quotient the Bell transfer by terminal symmetries

The repeated third part only observes the connectivity partition of the fixed terminals, so quotienting by `S_a x S_b` is the natural scalable state reduction. The missing proof obligation is strong lumpability not merely for the unmarked transfer but for every marked-edge initial vector entering `Z,Z_e,Z_f,Z_{ef}`. This run does not assume that statement. At width seven the full Bell space still has only `B_7=877` states.

### Route C — exact marked-star operator factorization

This route succeeds. Instead of jointly enumerating the core and one/two distinguished repeated stars, enumerate only the fixed core and apply exact star operators with specified spokes forced present. This is both the proof mechanism and the computational improvement used below.

## 5. New theorem

### Theorem `PROB10-07-TRIPARTITE-SUM7`

For every integer `n>=1`, every distinct edge pair is strictly negatively correlated under the uniform measure on all forests of each graph

\[
\boxed{K_{1,6,n},\qquad K_{2,5,n},\qquad K_{3,4,n}.}
\tag{5.1}
\]

Equivalently, for every such graph and every distinct present `e,f`,

\[
\boxed{\Delta_G(e,f)>0.}
\tag{5.2}
\]

Combining (5.1) with the preceding PROB10-07 fixed-width theorems gives:

> **Corollary.** Every complete tripartite graph `K_{a,b,c}` whose two smallest part sizes sum to at most seven satisfies strict pairwise negative edge correlation for the uniform measure on all forests.

The parent arbitrary-graph conjecture remains OPEN/PARTIAL.

## 6. Full proof: terminal-partition transfer

Fix `(a,b)` in `{(1,6),(2,5),(3,4)}` and put `m=a+b=7`. Call the first two parts the fixed terminals and process vertices of the third part one at a time.

A partial forest induces a set partition `pi` of the seven terminals according to which terminals lie in the same connected component.

### Lemma 6.1 — legal star criterion

Let a new third-part vertex `r` be joined to a subset `S` of the seven terminals. The extension remains acyclic iff `S` meets every block of `pi` in at most one terminal. When legal, all blocks meeting `S` merge into one block; for `|S|<=1`, the partition is unchanged.

**Proof.** If two selected terminals already lie in one block, the old forest contains a path joining them and the two new spokes through `r` close a cycle. Conversely, if selected terminals lie in distinct old components, the star through a new vertex joins distinct trees and cannot create a cycle. The connectivity update is exactly their merger. `QED`

Let `M_7` be the resulting transition matrix on the `B_7=877` set partitions. The empty spoke set and seven singleton spoke sets preserve every partition, so every diagonal entry is eight. Every other legal spoke set merges at least two blocks. Hence

\[
M_7=8I+N_7,
\tag{6.1}
\]

where each nonzero transition of `N_7` strictly lowers the number of blocks. There are at most seven blocks, therefore

\[
N_7^7=0.
\tag{6.2}
\]

Consequently, for every integer `x>=0`,

\[
M_7^x
=8^x\sum_{j=0}^{6}\binom{x}{j}\left(\frac{N_7}{8}\right)^j.
\tag{6.3}
\]

This is an exact finite identity because the binomial expansion truncates by (6.2).

## 7. Full proof: marked-star operators

A tested edge pair uses at most two vertices of the repeated third part. Let `k in {0,1,2}` denote the number of such distinguished repeated vertices.

For a subset `R` of terminals, define `T_R` on terminal partitions by summing all legal star subsets `S` satisfying `R subseteq S`. Thus `T_empty=M_7`. By Lemma 6.1, `T_R` exactly counts ways to attach one distinguished repeated vertex while forcing the spokes indexed by `R` to be present.

For `C` equal to `empty`, `{e}`, `{f}`, or `{e,f}`, construct a row vector `v_C` as follows:

1. enumerate forests of the fixed core `K_{a,b}`, forcing whichever members of `C` are core edges;
2. for each of the `k` distinguished repeated vertices, apply the operator `T_R` whose forced set `R` consists exactly of the marked spokes from `C` incident to that repeated vertex.

This construction is exact: every partial forest containing the required marked edges has a unique fixed-core restriction and a unique spoke subset at each distinguished repeated vertex; Lemma 6.1 gives precisely the legality criterion at each step. Therefore no object is omitted or multiply counted.

Let

\[
x=n-k\ge0
\]

for pairs with `k>=1`; when `k=0`, `x=n>=1`. All remaining repeated vertices are unmarked, so

\[
Z_C=v_C M_7^x\mathbf1.
\tag{7.1}
\]

By (6.3), there is an exact rational polynomial `P_C(x)` of degree at most six such that

\[
Z_C=8^xP_C(x).
\tag{7.2}
\]

Hence

\[
\Delta_G(e,f)
=8^{2x}R_{e,f}(x),
\qquad
R_{e,f}(x)=P_e(x)P_f(x)-P_0(x)P_{ef}(x),
\tag{7.3}
\]

with `deg R_{e,f}<=12`.

## 8. Exhaustive edge-pair orbit reduction

The automorphism group `S_a x S_b x S_n` acts on edges. Any edge pair touches at most two repeated vertices, so its orbit can be represented inside `K_{a,b,2}` after relabeling those repeated endpoints. The production checker enumerates **every** pair of distinct edges in `K_{a,b,2}`, canonicalizes under `S_a x S_b x S_2`, and obtains exactly

\[
10\quad\text{orbits for }K_{1,6,n},
\qquad
15\quad\text{for }K_{2,5,n},
\qquad
15\quad\text{for }K_{3,4,n},
\tag{8.1}
\]

for **40 total orbit representatives**.

Thus checking (7.3) for those forty representatives covers every distinct edge pair for every physical `n`.

## 9. Exact positivity certificate

For each orbit, the checker constructs `v_0,v_e,v_f,v_{ef}`, computes (7.2) and (7.3) in Python `Fraction` arithmetic, clears denominators, divides the integer coefficient list by its common gcd, and archives the complete primitive coefficient list.

For **all forty orbits**, every coefficient of `R_{e,f}(x)` in the ordinary monomial basis is nonnegative.

- for `k>=1`, the constant term is strictly positive, hence `R_{e,f}(x)>0` for every physical integer `x>=0`;
- for `k=0`, the physical domain is `x=n>=1`; the checker verifies `R_{e,f}(1)>0`. The one displayed zero constant coefficient is therefore harmless, because higher coefficients are positive.

As a representative core-core certificate for `K_{1,6,n}`, the primitive numerator is

\[
25153765376x+82900135568x^2+123917304252x^3+110284804540x^4
+64360117783x^5+25504933945x^6+6850362974x^7
+1199947770x^8+124119695x^9+5764801x^{10},
\]

with positive denominator `1073741824`, hence positive for every `x=n>=1`.

All other primitive coefficient lists are preserved verbatim in the archived output. Combining their sign with the positive factor `8^{2x}` in (7.3) proves (5.2), completing the theorem. `QED`

## 10. Falsification and direct exact regressions

The checker deliberately includes a second calculation not using the partition-polynomial formulas: for each of the three families at `n=1`, it enumerates **every actual edge subset** of the graph, rejects cyclic subsets by union-find, accumulates `Z,Z_e,Z_{ef}`, and checks every actual distinct edge pair directly.

Exact results:

- `K_{1,6,1}`: `13` edges, `78` edge pairs, `2916` forests;
- `K_{2,5,1}`: `17` edges, `136` edge pairs, `18176` forests;
- `K_{3,4,1}`: `19` edges, `171` edge pairs, `42720` forests.

Every direct Rayleigh difference is strictly positive and agrees exactly with the appropriate transfer polynomial at its physical value. This regression is a self-check, not an independent audit.

The locally executed files had SHA-256 values

- checker: `67cd1ce4de6b7d07621cd7cd715f5ed047bd4fef3783922c5af2d5b0765aed3d`;
- output: `7737a5c8b3d7613ea3f190e234b8f3b78303c820c129610a3e80735faafe0fbb`.

The output terminates

`PROB10_07_TRIPARTITE_SUM7_EXACT_PASS`.

## 11. Persisted artifacts and readback

Production checker:

`artifacts/prob10_2026-09-20/PROB10-07/20260920T0644Z_tripartite-sum7-f31c_checker.py`

- creation commit: `b737f815bea3929356d49055ed668da40da169e7`;
- exact-commit readback blob: `68eb25e435f02d044be04ed3459800ae2d23d4ee`.

Executed output:

`artifacts/prob10_2026-09-20/PROB10-07/20260920T0644Z_tripartite-sum7-f31c.out`

- creation commit: `37725a990acf5208f30f9683aee6531f7ee53797`;
- exact-commit readback blob: `c56df2a6c5333b9ed1bc8888d61068543ebb25c0`;
- exact-commit tail readback confirms `total_edge_pair_orbits=40` and `PROB10_07_TRIPARTITE_SUM7_EXACT_PASS`.

These are necessary self-certificates only. Outside audits remain `0/2` for this new theorem.

## 12. Source-level before/after and remaining full-scope gap

```yaml
ledger_delta:
  track: PROB10-07
  source: "Grimmett-Winkler uniform all-forests pairwise edge negative correlation"
  universal_status_before: OPEN
  universal_status_after: OPEN
  complete_all_graphs_order_before: 9
  complete_all_graphs_order_after: 9
  exact_counterexample_before: NONE
  exact_counterexample_after: NONE
  structural_metric: "complete tripartite graphs by sum of two smallest part sizes"
  structural_before: "<=6"
  structural_after: "<=7"
  new_families:
    - "K_{1,6,n}, all n>=1"
    - "K_{2,5,n}, all n>=1"
    - "K_{3,4,n}, all n>=1"
  strict_pairwise_NC: true
  finite_orbits_certified: 40
  exact_checker: PASS
  direct_n1_regression: PASS
  independent_audits: "0/2"
  novelty: UNVERIFIED
```

The full gap remains enormous: arbitrary finite graphs, already reducible in the owner history to a 3-connected minimal obstruction, are not represented by one repeated independent part. This theorem does not control the P14/HARD10 mixed three-terminal response term and does not prove the ten-vertex all-graph case.

## 13. What changed mathematically, and next nonrepetitive route

The important mechanism gain is not merely one more fixed width. Marked right-layer vertices are now exact operators `T_R`; the expensive joint enumeration of `K_{a,b}` together with up to fourteen marked-star choices has disappeared. That makes a width-eight test plausible without changing the proof architecture.

However, indefinitely advancing one Bell width at a time would eventually become bookkeeping rather than new mathematics. The next useful route should therefore try one of:

1. prove the `S_a x S_b` quotient is strongly lumpable for **all** forced-spoke operators `T_R`, reducing Bell states structurally;
2. derive a closed positive form for the orbit Rayleigh polynomials across symbolic fixed width, rather than certifying each width independently;
3. connect the forced-spoke operator to the P14 three-terminal response obstruction and test whether the repeated-part positivity exposes a monotone cone that survives beyond complete multipartite graphs.

The theorem here is **PARTIAL**. No closure, no counterexample, and no priority claim is asserted.

Model actually running: **GPT-5.6 Sol**. Reasoning effort: **UNVERIFIED**. GPT-6 maximum was requested, but the exposed runtime supplies no authenticated writable model/effort selector or maximum-effort telemetry, so this report does not claim GPT-6/maximum.

# PROB10-07 — corrected stabilizer quotient for complete split graphs through clique width 15

Status: **OPEN / PARTIAL** on the parent Grimmett–Winkler conjecture. The arbitrary-finite-graph statement is not resolved. This run proves and repairs restricted infinite structural families and does not alter P14/HARD10-01 graph-order ownership.

## 1. Exact target, source status, and current ownership

For a finite graph `G=(V,E)`, let

`Z = #{F subseteq E : F is acyclic}`,

and for distinct present edges `e,f` let `Z_e,Z_f,Z_ef` count forests containing the indicated marked edges. For the uniform measure on **all forests**,

`P(e,f in F) <= P(e in F)P(f in F)`

is exactly

`Delta_G(e,f):=Z_e Z_f - Z Z_ef >= 0`.

This is not a spanning-tree model, random minimum spanning tree, or a fixed-component ensemble.

Consumed control/history before choosing scope:

- `operations/PROB10_2026-09-20.md`;
- current root `POSTED.md`;
- R13 immutable displacement handoff `runs/R13/20260919T2345Z_handoff-to-PROB10-07-forest.md`;
- P14 mandatory forest handoff `proofnet24/P14-probability-correlation/runs/2026-09-17/2026-09-17T05-19-47Z__mandatory-handoff-report.md`;
- HARD10-01 forest handoff `proofnet24/HARD10-01/runs/2026-09-16/2026-09-16T21-16-42Z__report.md`;
- historical duplicate claim `operations/claims/P0001.md` and its R02 ownership-correction handoff `runs/R02/20260918T0102Z_61f4a9c7.md`, which explicitly retires R02 ownership after recovering P14's earlier claim;
- own preceding split report `runs/prob10_2026-09-20/PROB10-07/20260920T0938Z_split-join-m6-m9-cayley.md`;
- own preceding tripartite checker `artifacts/prob10_2026-09-20/PROB10-07/20260920T0838Z_tripartite-sum9-a7c2_checker.py`.

P14/HARD10-01 retain the complete-order-nine census and minimal-counterexample/3-connected structural history. This run does not repeat their graph-order enumeration or seize those claims.

Current literature was rechecked. Grimmett–Winkler arXiv:`math/0302185` is the source conjecture and gives the historical finite verification. Erickson arXiv:`1008.3660` proves a weighted Rayleigh/SOS result for series-parallel graphs. Tang–Zhang arXiv:`2603.10738` treats several uniform spanning-subgraph ensembles on the complete graph, including forests with a fixed number of components for sufficiently large order, not the arbitrary-graph all-forests model. Bado's 2026/2027 wheel theorem gives another restricted 3-connected family. Bounded searches did not surface an existing complete-split theorem matching the result below; **external novelty remains UNVERIFIED**.

## 2. Source-level before/after

Parent source: `OPEN -> OPEN`.

Complete arbitrary-simple-graph order metric: `9 -> 9`.

Corrected split-family theorem of this run:

> **Theorem.** Let `S_{m,n}=K_m \vee \overline{K_n}` be the complete split graph. For every `m in {6,7,...,15}` and every `n>=1`, every distinct pair of present edges is strictly negatively correlated under the uniform measure on all forests of `S_{m,n}`.

Widths `m=6,7,8,9` repair the preceding PROB10-07 split certificate; widths

`m=10,11,12,13,14,15`

are genuinely new full-parameter families in this run. Separate repository work previously covered smaller widths, but no ownership is transferred here.

No counterexample to the original model was found.

## 3. Integrity correction: a defect in the preceding marked-right transfer

The mathematical idea was written before the new checker at

`artifacts/prob10_2026-09-20/PROB10-07/20260920T1038Z_split-quotient-m17-correction_idea.md`

creation commit `77cd8d1955dc954376d434b0fe2ef29ecde0f4e9`, blob `e7b3fffc7cd044ed590b9d337ca037544ccefebb`.

A marked pair can touch `k=1` or `2` distinguished vertices of the repeated independent side. Once these vertices are removed from the residual exponent `x=n-k`, **all of them must still be processed in each of the four conditioning counts** `Z,Z_e,Z_f,Z_ef`. If a distinguished right vertex has no forced marked spoke in a given conditioning event, it contributes the ordinary unmarked transition `M`, not the identity.

The preceding split checker processed only right vertices that appeared in the current condition. Thus, for example, `Z` omitted every distinguished right vertex while the residual exponent had already removed them.

The corrected rule is

`v_C = core_C prod_{r in R} T_{S_r(C)}`,

where `R` is the set of repeated-side vertices touched by the full pair, `S_r(C)` is the set of clique endpoints whose spokes at `r` are forced under condition `C`, and crucially

`T_emptyset=M`.

Then

`Z_C(n)=v_C M^(n-|R|) 1`.

### Exact witness to the old omission

Take `K_3 \vee I_2` and mark two spokes on different independent vertices with different clique endpoints. Direct enumeration of the original model gives

`(Z,Z_e,Z_f,Z_ef)=(198,70,70,24)`.

The superseded omission rule gives

`(7,14,14,24)`,

which is not even a count of the same conditioned graph. The corrected Rayleigh numerator is

`70^2-198*24=148>0`.

The new checker reproduces both tuples and asserts the corrected tuple equals direct enumeration.

The same omission pattern is present in the preceding complete-tripartite transfer code: its shifted residual exponent removes all right vertices touched by the full pair, but its initial-vector loop processes only right vertices appearing in the current required-edge set. Therefore the earlier PROB10-07 **tripartite all-`n` certificates are now classified UNVERIFIED pending corrected rerun**. This report does not claim those graph-family statements are false. The complete-bipartite chain used a different counting formulation and is not superseded here.

## 4. Three materially different unexhausted approaches

### Route A — deletion–contraction directly on the Rayleigh difference

For distinct nonloop edges,

`Z_e=Z(G/e)`, `Z_f=Z(G/f)`, `Z_ef=Z(G/{e,f})`,

so

`Delta_G(e,f)=Z(G/e)Z(G/f)-Z(G)Z(G/{e,f})`.

Expanding all four terms along a third edge gives an exact quadratic identity. The endpoint coefficients are naturally smaller-graph Rayleigh differences, but the mixed coefficient has no general sign. This is the same environmental-covariance obstruction already exposed by the P14/HARD10 three-terminal work, so repeating it would not be a new closing mechanism.

### Route B — two-sort exponential formula for split forests

A forest of `K_m \vee I_n` is a set of tree components. A component containing `q>=1` clique vertices and `r>=0` independent vertices is a spanning tree of `K_q \vee I_r`; its tree count has a compact closed form obtainable from the complete multipartite tree formula. This gives a small bivariate exponential generating function for unmarked forests. The obstacle is that one- and two-marked-edge counts require several transfer-current component types; I did not obtain a coefficientwise Rayleigh inequality from that language in this bounded run.

### Route C — stabilizer quotient of the corrected terminal-partition transfer

This route closes a substantial new range and is the theorem route below.

## 5. Exact quotient state space

Fix one of the seven edge-pair geometries in a complete split graph. At most `d<=4` clique vertices are distinguished by the pair. Quotient the set partitions of the `m` clique terminals by the symmetric group `S_{m-d}` on the undistinguished clique vertices.

A quotient state consists of:

1. a set partition of the `d` distinguished labels;
2. for each block containing distinguished labels, the number `a_i` of undistinguished labels attached to that block;
3. the integer partition of the remaining undistinguished labels into pure blocks.

If the pure blocks have `c_s` blocks of size `s`, the number of labelled terminal partitions represented by the state is

`(m-d)! / ( prod_i a_i! prod_s (s!)^(c_s) c_s! )`.

This is exact orbit counting under the stabilizer.

At `m=15` the largest quotient among the seven pair geometries has `20,217` states, compared with Bell number `B_15=1,382,958,545` labelled set partitions. Thus the quotient changes the feasible structural scale rather than merely spending more time on the full Bell lattice.

## 6. Strong lumpability of a fresh independent-side vertex

Let a current terminal-connectivity partition have blocks `B_1,...,B_t`. A new independent vertex may be joined by spokes to a set `S` of clique terminals without creating a cycle iff `S` contains at most one terminal from each current block. If two selected terminals lie in one block, their existing path plus the two new spokes creates a cycle; conversely joining distinct components through one new star creates no cycle.

For an unforced block `B_i`, selecting that block contributes exactly `|B_i|` choices of terminal. For a block containing a forced distinguished terminal, the choice is fixed and has multiplicity one. If two forced terminals are already in the same block, the transition weight is zero.

Therefore the total transition weight from a full labelled partition into any quotient orbit depends only on the quotient state: the quotient is strongly lumpable for both the unmarked operator and every forced-spoke operator used here.

For the unmarked transition, the empty spoke set and all `m` singleton spoke choices leave terminal connectivity unchanged. Hence

`M=(m+1)I+N`.

Every nonzero entry of `N` strictly coarsens the terminal partition, so

`N^m=0`.

## 7. Exact marked clique-core vector

A forest on the clique `K_m` induces a partition `pi` of its vertices into tree components. Suppose a fixed required set `R` of one or two marked clique edges is contained within blocks of `pi` (otherwise the state count is zero).

For one block `B` of size `q`, contract the connected components of the required forest `R_B`. If their sizes are `s_1,...,s_c`, including isolated vertices, a spanning tree of `K_B` containing every edge of `R_B` corresponds to a weighted tree on the `c` contracted components with edge weight `s_i s_j`. Weighted Cayley gives

`q^(c-2) prod_i s_i`.

Multiplying this over blocks and by the quotient-orbit multiplicity in Section 5 gives the exact marked clique-core vector without enumerating `2^(m choose 2)` clique edge sets.

## 8. Exact all-`n` polynomialization with the corrected exposure rule

Let `R_right` be the set of independent-side vertices touched by the full marked pair and put `k=|R_right|`, `x=n-k`. For each condition `C in {0,e,f,ef}`, begin with the appropriate marked clique-core vector and process **all** vertices in `R_right` in a fixed order. On a right vertex with no forced spoke in `C`, use `M`; otherwise use its forced-spoke transition.

Call the resulting vector `v_C`. The remaining `x` independent vertices are unmarked, so

`Z_C(n)=v_C M^x 1`.

Since `M=(m+1)I+N`, `N^m=0`,

`Z_C(n)=(m+1)^x P_C(x)`,

where

`P_C(x)=sum_{j=0}^{m-1} binom(x,j)(m+1)^(-j) v_C N^j 1`.

Consequently

`Delta(e,f)=(m+1)^(2x) R_{e,f}(x)`

with

`R_{e,f}(x)=P_e(x)P_f(x)-P_0(x)P_ef(x)`

and degree at most `2m-2`.

This is an exact identity on the full parameter range, not polynomial interpolation from checked values.

## 9. Exhaustive edge-pair orbit list

For `m>=4`, every unordered pair of distinct edges belongs to one of exactly seven geometries:

1. two clique edges sharing one clique endpoint;
2. two disjoint clique edges;
3. a clique edge and a spoke incident at a clique endpoint;
4. a clique edge and a spoke whose clique endpoint is outside the clique edge;
5. two spokes at the same independent vertex;
6. two spokes on different independent vertices with the same clique endpoint;
7. two spokes on different independent vertices with different clique endpoints.

For right-touching orbits, `x=n-k>=0` on the physical domain; for core-core orbits `x=n>=1`.

## 10. Exact sign certificate through width 15

The checker expands every normalized `R_{e,f}(x)` in the ordinary monomial basis using only Python integers and `Fraction`. For each of the seven orbits and each `m=6,...,15`, **every primitive coefficient is nonnegative**, and the polynomial is strictly positive at the first physical value of `x`. Therefore it is strictly positive throughout the physical integer domain.

The largest quotient-state counts and the smallest primitive coefficient among the seven certificates are:

| `m` | max quotient states | smallest primitive coefficient |
|---:|---:|---:|
| 6 | 135 | 2,592 |
| 7 | 296 | 117,649 |
| 8 | 592 | 33,554,432 |
| 9 | 1,098 | 3,486,784,401 |
| 10 | 1,940 | 2,000,000,000,000 |
| 11 | 3,281 | 379,749,833,583,241 |
| 12 | 5,372 | 369,768,517,790,072,832 |
| 13 | 8,547 | 112,455,406,951,957,393,129 |
| 14 | 13,285 | 167,336,510,850,569,603,121,152 |
| 15 | 20,217 | 74,818,276,426,792,144,775,390,625 |

All are positive; the full per-orbit degrees, denominators, coefficient extrema, first-physical values, and coefficient-vector SHA-256 digests are archived in the executed output.

This proves the theorem in Section 2.

## 11. Independent original-model regression

The checker separately enumerates every edge subset of `K_4 \vee I_2`, retains exactly the acyclic sets by union-find, and compares direct `(Z,Z_e,Z_f,Z_ef)` against the quotient prediction for representatives of **all seven** edge-pair orbits. All seven tuples match exactly:

- CC adjacent: `(2110,596,596,130)`, `Delta=80916`;
- CC disjoint: `(2110,596,596,165)`, `Delta=7066`;
- clique/spoke incident: `(2110,596,644,144)`, `Delta=79984`;
- clique/spoke nonincident: `(2110,596,644,178)`, `Delta=8244`;
- same-right spokes: `(2110,644,644,144)`, `Delta=110896`;
- same-clique/different-right spokes: `(2110,644,644,178)`, `Delta=39156`;
- different-clique/different-right spokes: `(2110,644,644,192)`, `Delta=9616`.

This direct regression is independent of the quotient state-count formulas at the level of the original edge-subset model.

## 12. Executed artifacts

Idea-before-code artifact:

`artifacts/prob10_2026-09-20/PROB10-07/20260920T1038Z_split-quotient-m17-correction_idea.md`

commit `77cd8d1955dc954376d434b0fe2ef29ecde0f4e9`, blob `e7b3fffc7cd044ed590b9d337ca037544ccefebb`.

Exact checker:

`artifacts/prob10_2026-09-20/PROB10-07/20260920T1038Z_split-quotient-corrected_m6_m15_checker.py`

creation/readback commit `234f2e4cf70ff24c275d08e28051ebf21e30f426`, blob `7d8c8630428368192759e4d229d60d8ed9662dc6`.

Executed local checker SHA-256 for the equivalent exact implementation used to produce the archived output:

`a8e5f0170969f294205c21b69a9faa6faeee1b2283ed817f4fd60d2567a6fd52`.

Executed command range: `m=6,7,8,9,10,11,12,13,14,15`.

Archived output:

`artifacts/prob10_2026-09-20/PROB10-07/20260920T1038Z_split-quotient-corrected_m6_m15_checker.out`

creation/readback commit `046401d8e513e3a975f75805fa4a16b39cf8fc1b`, blob `be775fba14bcbeeea093f8f8082a1000d12067b6`; local SHA-256

`0e6526733ea8a95d63bc8836fb1268f835464ca42e72e13459e45ad7de9e773c`.

The output terminates

`PROB10_07_SPLIT_QUOTIENT_CORRECTED_EXACT_PASS`.

Forest-owner handoff:

`artifacts/prob10_2026-09-20/PROB10-07/20260920T1038Z_split-quotient-corrected_forest-owner-handoff.md`

creation/readback commit `11a46210bfbe6b17dd09b4d68c520fb6cd7da6ed`, blob `0f9812c1d3a80e8398c94c80dda31795d304ca98`.

## 13. Auxiliary gains and remaining full-scope gap

Auxiliary gains:

1. an exact correction of the marked-right exposure rule, with a minimal direct counterexample to the old counting identity;
2. a proof of strong lumpability under the stabilizer of the marked clique terminals;
3. reduction from Bell-size labelled partition spaces to manageable marked-integer-partition quotient spaces;
4. corrected all-`n` split certificates for widths 6--9 and six new widths 10--15.

Remaining gap:

- arbitrary finite graphs remain unresolved;
- no source-matching counterexample was found;
- no independent external validation is claimed, so the parent remains OPEN/PARTIAL;
- the quotient proof has not been converted to an all-`m` symbolic sign theorem;
- widths `m>=16` are not claimed by the persisted executed certificate in this report;
- previous tripartite all-parameter certificates require a corrected rerun before they can again be treated as certified.

A natural next mathematical target is to identify a recurrence in `m` for the seven quotient Rayleigh polynomials that preserves coefficientwise positivity, rather than merely extending the finite width one at a time.

## 14. Control-state preservation

No scheduler, cadence, enabled state, email, Drive, public posting, workflow, permission, or peer-owned claim was changed. The recurring PROB10-07 assignment remains under its existing owner/platform state.
# PROB10-07 mathematical idea — corrected marked-right transfer and stabilizer quotient

Parent source: Grimmett–Winkler pairwise negative correlation for the uniform measure on **all forests** of a finite graph. Status remains OPEN/PARTIAL. This note records the mathematical idea before persistence of the new checker.

## Ownership / nonoverlap

This route does not touch P14/HARD10-01 complete graph-order enumeration or their 3-connected minimal-counterexample reduction. It also does not seize the historical R02/P0001 block-cyclomatic handoff. The precise scope is the complete split family

`S_{m,n}=K_m \vee \overline{K_n}`

under unit weights, using a structural transfer quotient under the stabilizer of the at most four clique terminals touched by a marked edge pair.

Consumed before scope selection: current `operations/PROB10_2026-09-20.md`, current root `POSTED.md`, `operations/claims/P0001.md` and the R02 ownership-correction handoff `runs/R02/20260918T0102Z_61f4a9c7.md`, P14 mandatory handoff `proofnet24/P14-probability-correlation/runs/2026-09-17/2026-09-17T05-19-47Z__mandatory-handoff-report.md`, HARD10-01 handoff `proofnet24/HARD10-01/runs/2026-09-16/2026-09-16T21-16-42Z__report.md`, own preceding split report `runs/prob10_2026-09-20/PROB10-07/20260920T0938Z_split-join-m6-m9-cayley.md`, and the width-nine tripartite checker.

## Exact defect found in the preceding split/tripartite transfer pattern

A marked edge pair may touch `k=1` or `2` distinguished vertices on the repeated independent side. Once those vertices are removed from the residual exponent `x=n-k`, **every distinguished vertex must still be processed in every one of the four counts** `Z,Z_e,Z_f,Z_ef`. If a distinguished right vertex carries no forced marked spoke in the conditioning event, its transition is the ordinary unmarked operator `M`, not the identity.

The preceding split checker instead applied a transition only to distinguished right vertices that carried a required edge in the current conditioning event. Thus it omitted unconstrained distinguished vertices from (for example) `Z`, and often from `Z_e` or `Z_f`, while simultaneously using the residual exponent `n-k`. This is a real counting bug, not a stylistic issue.

The corrected initial vector for a condition `C` is

`v_C = core_C * prod_{r in R} T_{S_r(C)}`,

where `R` is the set of all repeated-side vertices touched by the full pair, `S_r(C)` is the set of clique endpoints whose spokes at `r` are forced by `C`, and crucially `T_emptyset=M`. Then

`Z_C(n)=v_C M^{n-|R|} 1`.

A minimal exact witness is `K_3 \vee I_2` with two spokes on different right vertices and different clique endpoints. Direct enumeration gives

`(Z,Z_e,Z_f,Z_ef)=(198,70,70,24)`.

The superseded split code's omitted-vertex rule gives `(7,14,14,24)`. The corrected formula gives the direct counts exactly, and the physical Rayleigh numerator is `70^2-198*24=148>0`.

The same omission pattern is visible in the width-nine tripartite checker: its `initial_vec` iterates only over right vertices appearing in `required_edges`, while its Rayleigh variable is shifted by the number of right vertices touched by the full pair. Therefore the earlier tripartite all-`n` certificates must be treated as **UNVERIFIED pending corrected rerun**; this run does not silently preserve them as proved.

## Three materially different approaches compared

### A. Deletion–contraction recurrence on the Rayleigh difference

For any distinct nonloop edges `e,f`, forest inclusion gives `Z_e=Z(G/e)` and `Z_{ef}=Z(G/{e,f})`, so

`Delta_G(e,f)=Z(G/e)Z(G/f)-Z(G)Z(G/{e,f})`.

One can expand all four terms along a third edge. This is the most direct source-level route, but the mixed coefficient has no evident sign; it is the same environmental-covariance obstruction already isolated by P14 at a three-terminal separator. I do not recycle it as a proof.

### B. Two-sort component exponential formula

A forest of `K_m \vee I_n` is a set of tree components. A component with `q>=1` clique vertices and `r>=0` independent vertices has spanning-tree count

`tau(q,r)=q^{r-1}(q+r)^{q-1}`

(with the usual Cayley convention at `r=0`). This gives a compact bivariate exponential generating function for unmarked forest counts. It is promising for an eventual all-`m` theorem, but marked one- and two-edge counts require several transfer-current component types and I did not obtain a clean coefficientwise Rayleigh proof in this bounded iteration.

### C. Corrected stabilizer quotient of the terminal-partition transfer — chosen route

For one edge-pair orbit, at most `d<=4` clique terminals are distinguished. Quotient the Bell partition lattice of the `m` clique vertices by the symmetric group on the remaining `m-d` undistinguished clique vertices.

A quotient state consists of:

1. a set partition of the `d` distinguished labels;
2. for each block containing distinguished labels, the number of undistinguished labels attached to it;
3. the integer partition of the remaining undistinguished labels into pure blocks.

The orbit multiplicity is

`(m-d)! / (prod_i a_i! prod_s (s!)^{c_s} c_s!)`.

For an unmarked fresh independent vertex, select at most one terminal from each current connectivity block. Selecting a block of size `q` has multiplicity `q`. For forced spokes, blocks containing forced distinguished terminals are selected with multiplicity one; if two forced terminals lie in the same current block the row is zero. The target quotient state depends only on the source quotient state and selected block multiset, proving strong lumpability.

The unmarked operator still has

`M=(m+1)I+N`, `N^m=0`,

because every non-diagonal transition strictly merges at least two clique-connectivity blocks. Thus after exposing all right vertices touched by the pair with the corrected `T_emptyset=M` rule, every marked count is `(m+1)^x` times an exact polynomial in `x=n-k` of degree at most `m-1`, and every Rayleigh difference is `(m+1)^{2x}` times a polynomial of degree at most `2m-2`.

The quotient is exact, not interpolation. It cuts the worst pair-orbit state space dramatically: at `m=17`, the largest quotient (four distinguished clique terminals) has 44,477 states, versus Bell number `B_17=82,864,869,804` for the full labelled partition lattice.

## Intended bounded certificate

Use exact integer/Fraction arithmetic to:

- regress the corrected formula against direct all-subset enumeration of `K_4 \vee I_2` for representatives of every one of the seven edge-pair orbits;
- explicitly reproduce the old `K_3 \vee I_2` bad count tuple and the corrected tuple;
- certify coefficientwise nonnegativity and strict positivity on the physical domain for all seven orbit Rayleigh polynomials for `m=6,...,17`;
- record `m=6,...,9` as a repair of the preceding split proof and `m=10,...,17` as new full-parameter split families.

No claim of an all-`m` theorem or of the arbitrary-graph conjecture is made.
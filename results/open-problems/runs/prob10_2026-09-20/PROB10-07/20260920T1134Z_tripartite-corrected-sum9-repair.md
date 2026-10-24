Runtime model exposed to this assistant: **GPT-5.6 Sol**. Reasoning/effort telemetry: **UNVERIFIED**. GPT-6 maximum was requested by the owner, but no authenticated GPT-6/maximum selector or applied-effort telemetry is exposed here, so this report does not claim it ran.

# PROB10-07 — corrected complete-tripartite transfer restores the `a+b<=9` family

Status: **OPEN / PARTIAL** on the parent Grimmett–Winkler conjecture. This run repairs an integrity defect in earlier PROB10-07 complete-tripartite certificates and proves the corrected full-parameter structural theorem below. It does not move or seize P14/HARD10-01 graph-order ownership.

## 1. Frozen source target and consumed control/history

For a finite graph `G=(V,E)`, choose uniformly from all acyclic edge subsets `F subseteq E`. For distinct present edges `e,f`, write

`Z = # {forests}`, `Z_e = # {forests containing e}`, `Z_f`, `Z_ef`.

The source inequality is

`P(e,f in F) <= P(e in F) P(f in F)`, equivalently

`Delta_G(e,f):=Z_e Z_f-Z Z_ef >= 0`.

This is the uniform measure on **all forests**, not uniform spanning trees, random minimum spanning trees, or a fixed-component ensemble.

Consumed before committing scope:

- `operations/PROB10_2026-09-20.md` — owner contract and PROB10-07 scope;
- current root `POSTED.md` — posted/exclusion registry and distinction from the owner's random-cluster parameter-nonmonotonicity paper;
- R13 immutable displacement handoff `runs/R13/20260919T2345Z_handoff-to-PROB10-07-forest.md`;
- P14 mandatory forest handoff `proofnet24/P14-probability-correlation/runs/2026-09-17/2026-09-17T05-19-47Z__mandatory-handoff-report.md`, blob `bed2241d948b8a20b854efc248ccf5b46b4325cd`;
- HARD10-01 forest handoff `proofnet24/HARD10-01/runs/2026-09-16/2026-09-16T21-16-42Z__report.md`;
- historical duplicate claim `operations/claims/P0001.md` plus its ownership correction `runs/R02/20260918T0102Z_61f4a9c7.md`; the latter retires R02 ownership and preserves its block-cyclomatic partial theorem;
- own preceding integrity report `runs/prob10_2026-09-20/PROB10-07/20260920T1038Z_split-quotient-correction-m15.md`;
- superseded complete-tripartite checker `artifacts/prob10_2026-09-20/PROB10-07/20260920T0838Z_tripartite-sum9-a7c2_checker.py`, blob `7d53d9eab0b0f13e4eb96c7b225c5c4858fa1ef2`.

Canonical nonoverlap: P14/HARD10-01 retain the complete arbitrary-graph order-nine certificate, the 3-connected minimal-counterexample reduction, and the ten-vertex graph-order obstruction. R02's block-cyclomatic result remains historical partial work. This run takes only a parameter-uniform complete-tripartite transfer/certificate route and performs no graph-order census.

## 2. Current source/literature distinction

The bounded current source check used the exact sources specified by the owner:

- Grimmett–Winkler, `https://arxiv.org/abs/math/0302185`, is the arbitrary-finite-graph all-forests conjecture and reports the historical finite verification;
- Erickson, `https://arxiv.org/abs/1008.3660`, proves the weighted Rayleigh/SOS theorem for the series-parallel class;
- Tang–Zhang, `https://arxiv.org/abs/2603.10738`, treats several complete-graph spanning-subgraph ensembles including fixed-component forests, not the arbitrary-graph uniform-all-forests model.

The known wheel theorem and the owner's random-cluster parameter-nonmonotonicity manuscript are also distinct restricted/different statements. A bounded negative search is not a novelty certificate. External novelty of the complete-tripartite theorem below remains **UNVERIFIED**.

## 3. Source-level and mechanism metrics

Parent conjecture: `OPEN -> OPEN`.

Complete arbitrary-simple-graph order metric owned by P14/HARD10-01: `9 -> 9`.

Complete-tripartite certificate state before this run: **UNVERIFIED** for the earlier claimed all-`n` families, because the 10:38Z report found a marked-repeated-vertex exposure defect.

Complete-tripartite certificate state after this run: **exactly repaired and VERIFIED by self-check** for every

`K_{a,b,n}`, `n>=1`, `1<=a<=b`, `3<=a+b<=9`.

Thus the repaired structural theorem is:

> **Theorem.** Let `1<=a<=b`, `3<=a+b<=9`, and `n>=1`. Under the uniform measure on all forests of the complete tripartite graph `K_{a,b,n}`, every pair of distinct present edges is strictly negatively correlated.

Together with the already-known series-parallel case `K_{1,1,n}`, this covers every complete tripartite graph whose two smallest part sizes sum to at most `9`. This combination is only a structural-family theorem; it is not the arbitrary-graph conjecture.

No counterexample to the original model was found.

## 4. Mathematical idea before code and comparison of three routes

The idea was persisted before the final checker at

`artifacts/prob10_2026-09-20/PROB10-07/20260920T1134Z_tripartite-corrected-exposure_idea.md`

creation commit `069265f5392d2bd199faa8d665c4ac912fe83a6f`.

### Route A — corrected marked-vertex exposure, chosen

Use the terminal-connectivity transfer on the fixed first two parts, but expose **every** repeated-third-part vertex touched by the full marked pair in all four conditioning counts. The previous omission is repaired by using the ordinary unmarked transition `M` whenever such a distinguished vertex carries no forced marked spoke under the current condition.

This retains the exact nilpotent polynomialization and permits a full all-parameter certificate.

### Route B — deletion–contraction in one repeated-side vertex

Expand the Rayleigh difference by deleting/contracting the spokes of one repeated-side vertex. Endpoint terms reduce to smaller instances, but the mixed polarization term is not sign-controlled. This is structurally the same environmental-covariance obstruction already isolated in the P14/HARD10 three-terminal work. Repeating it would not provide a new closing mechanism.

### Route C — component exponential formula

Count tree components in `K_{a,b,n}` using complete-multipartite tree formulas and build marked-edge exponential generating functions. This may ultimately remove the fixed-width bound, but two-marked-edge component types proliferate and no coefficientwise Rayleigh inequality was derived in this bounded iteration. It remains the natural next method if the transfer route stops scaling.

Approximately all substantive mathematics in this run was spent on Route A and its falsification/repair checks; bookkeeping was limited to owner/source readback and persistence.

## 5. Exact transfer lemma

Fix `a,b` and put `m=a+b`. The first two parts form the fixed core `K_{a,b}` on terminal set `T`, `|T|=m`. Any core forest induces a partition of `T` by connected components.

When one new third-part vertex is added, a set of spokes is acyclic relative to a current terminal partition iff it contains at most one terminal from each current block. Indeed, choosing two terminals from one block closes a cycle through their existing path; conversely, a star joining distinct components cannot create a cycle. Selecting one terminal from a block of size `s` contributes multiplicity `s`.

Let `M` be the exact transition operator on terminal partitions for one unmarked third-part vertex. The empty spoke set and the `m` singleton choices leave terminal connectivity unchanged, hence

`M=(m+1) I + N`.

Every nonzero transition of `N` strictly coarsens the partition. No chain can strictly coarsen an `m`-point partition `m` times, so

`N^m=0`.

Therefore for every integer `x>=0`,

`M^x = sum_{j=0}^{m-1} binom(x,j) (m+1)^(x-j) N^j`.

This is an exact identity, not interpolation.

## 6. Corrected distinguished-vertex exposure

Let the full marked pair be `{e,f}` and let `R` be the set of third-part vertices touched by at least one of `e,f`. Then `k=|R|` is `0,1`, or `2`, and the residual unmarked count is

`x=n-k`.

For condition `C` in `{0,e,f,ef}`, and `r in R`, let `S_r(C)` be the set of terminal endpoints whose spokes at `r` are forced by `C`. Let `T_S` be the exact fresh-third-vertex transition with spokes to the terminals in `S` forced.

The critical corrected rule is

`T_empty = M`.

Starting from the core vector conditioned on any marked core edges, process **all** `r in R`:

`v_C = core_C prod_{r in R} T_{S_r(C)}`.

Only then apply the `x` ordinary third-part vertices:

`Z_C(n)=v_C M^x 1`.

The superseded checker instead processed only repeated-side vertices that appeared in the current required-edge set while already subtracting the full `k` from the residual exponent. That omitted actual vertices from `Z`, `Z_e`, or `Z_f` and could not represent the same graph.

## 7. Polynomial Rayleigh certificate

Using the nilpotent expansion of `M^x`, every conditioned count has the exact form

`Z_C(n)=(m+1)^x P_C(x)`, `deg P_C<=m-1`,

with rational coefficients explicitly computed from `v_C N^j 1`.

Thus

`Delta(e,f)=Z_e Z_f-Z Z_ef=(m+1)^(2x) R_{e,f}(x)`,

where

`R_{e,f}(x)=P_e(x)P_f(x)-P_0(x)P_ef(x)`

has degree at most `2m-2`.

The natural automorphism group `S_a x S_b` (augmented by exchange of the two equal parts when `a=b`) together with permutation symmetry of the repeated third part gives a complete finite list of edge-pair orbits. Across all nineteen repaired families the checker exhausts **232** such orbits.

For every orbit, the checker expands `R_{e,f}(x)` exactly in the ordinary monomial basis using integers and Python `Fraction`. Every coefficient is nonnegative, and `R` is strictly positive at the first physical integer (`x=1` for core-core pairs, `x=0` when the pair touches repeated-side vertices). Consequently

`R_{e,f}(x)>0`

throughout the full physical integer domain, proving strict pairwise negative correlation for all `n>=1` in the theorem's range.

Zero primitive coefficients do occur in a few `K_{1,b,n}` orbit polynomials, but no polynomial is zero on its physical range; coefficientwise nonnegativity plus the positive first-physical value is the exact sign argument.

## 8. Exact falsification witness for the old rule

The checker contains a direct witness on `K_{1,2,2}` with marked spokes

`e=(0,3)`, `f=(1,4)`.

Direct enumeration of the original all-forests model gives

`(Z,Z_e,Z_f,Z_ef)=(134,48,52,18)`

and therefore

`Delta=48*52-134*18=84>0`.

The corrected transfer reproduces the same tuple exactly. The old omission rule gives

`(4,9,10,18)`,

which is not a count of the same conditioned graph. This independently identifies the previous transfer defect at the count level rather than merely changing a proof convention.

## 9. Executed exact checker and original-model regressions

Final checker:

`artifacts/prob10_2026-09-20/PROB10-07/20260920T1134Z_tripartite-corrected-sum9_checker.py`

final synchronization/readback commit

`1d5a9c6188e5ffaf54714210e6f27631c9c8624c`,

Git blob

`a0adb52e7a01a8ad972647c6e1d027c4151ee9d3`.

The persisted checker bytes match the locally executed final checker bytes by Git-blob identity. Local SHA-256 of the executed checker was

`02d370ff158a9cfe79440d9f72727ce1094fded514ab405933f99c21dd0e7db0`.

Archived executed stdout:

`artifacts/prob10_2026-09-20/PROB10-07/20260920T1134Z_tripartite-corrected-sum9_checker.out`

creation/readback commit

`d6eaf3286c4c1ea5ff8dcffccb8a77d71b2db913`,

Git blob

`19bf0d2241f27b1647dabf3a06a8a9960a0a4a65`.

Local SHA-256 of the executed output was

`2d1f4e805e633831be9a1d03c0b168d08936e4573b033635c5d0debc1da82a12`.

The archived output ends

`PROB10_07_TRIPARTITE_CORRECTED_SUM9_EXACT_PASS`.

It records every family from `K_{1,2,n}` through the four `a+b=9` families, all 232 edge-pair orbit certificates, and the exact correction witness above.

As a separately coded regression at the original edge-subset level, every actual edge pair was brute-force checked in:

- `K_{1,2,2}`: 8 edges, 134 forests, 28 pairs, minimum `Delta=84`;
- `K_{1,3,2}`: 11 edges, 712 forests, 55 pairs, minimum `Delta=1728`;
- `K_{2,2,2}`: 12 edges, 1083 forests, 66 pairs, minimum `Delta=3610`;
- `K_{1,8,1}`: 17 edges, 30,618 forests, 136 pairs, minimum `Delta=2,125,764`.

These regressions check the original model independently of the polynomial sign reduction at the counting level, but they are still self-checks by this track, not independent outside audits.

## 10. Auxiliary gains and limitations

Auxiliary gain 1: the earlier complete-tripartite claims are no longer left in an ambiguous state. The exact old defect is preserved and the repaired counts are source-model exact.

Auxiliary gain 2: the proof makes the physical shifted variable explicit: `x=n-k`, where `k` is the number of repeated-side vertices touched by the full marked pair. This prevents the same omitted-vertex bug from recurring in future repeated-module transfers.

Auxiliary gain 3: the corrected transfer remains coefficientwise positive through terminal width nine despite the added unmarked distinguished-vertex operators. Thus the integrity repair does not shrink the previously claimed fixed-width structural range.

Limitation: this does **not** prove the conjecture for arbitrary graphs, does not move the complete-order metric beyond nine, and does not address all positive edge weights. It also does not provide independent validation or a worldwide novelty certificate.

## 11. Remaining full-scope gap

The source statement remains OPEN/PARTIAL. The P14/HARD10 structural history still reduces a vertex-minimal counterexample to a 3-connected graph, and the clean finite unresolved source-level step remains the full class of 3-connected simple graphs on ten vertices. The mixed three-terminal/deletion-contraction polarization obstruction remains unresolved in general.

Within the complementary transfer route, a natural next mathematical question is whether the complete-tripartite proof can be made **uniform in `m=a+b`** rather than certified width by width. Route C's component formula or a quotient/lumping argument may expose such a theorem. That would still be a restricted structural family unless connected to a general decomposition.

No exact negative Rayleigh difference in the original model was found.

## 12. Handoff and operational boundary

Non-mutating forest-owner handoff:

`artifacts/prob10_2026-09-20/PROB10-07/20260920T1134Z_tripartite-corrected-sum9_forest-owner-handoff.md`.

It links the R13, P14, HARD10-01, R02, and preceding PROB10-07 histories and explicitly leaves their claims untouched.

No scheduler setting, cadence, enabled state, email, Drive, public posting, permissions, or peer-owned claim was changed in this run.

`END OF REPORT`

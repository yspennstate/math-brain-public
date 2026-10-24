# PROB10-07 -> forest-owner handoff: corrected complete-tripartite transfer through fixed width nine

Parent source: Grimmett–Winkler pairwise edge negative correlation for the uniform measure on **all forests**. Parent status remains **OPEN / PARTIAL**. This is a non-mutating handoff only: it does not edit, seize, or duplicate P14/HARD10-01 graph-order claims.

## Owner/history pointers

- R13 displacement handoff: `runs/R13/20260919T2345Z_handoff-to-PROB10-07-forest.md`.
- P14 mandatory forest handoff: `proofnet24/P14-probability-correlation/runs/2026-09-17/2026-09-17T05-19-47Z__mandatory-handoff-report.md`.
- HARD10-01 forest handoff: `proofnet24/HARD10-01/runs/2026-09-16/2026-09-16T21-16-42Z__report.md`.
- R02 ownership-correction / block-cyclomatic handoff: `runs/R02/20260918T0102Z_61f4a9c7.md`.
- Preceding PROB10-07 integrity correction: `runs/prob10_2026-09-20/PROB10-07/20260920T1038Z_split-quotient-correction-m15.md`.

P14/HARD10-01 retain the complete arbitrary-graph order-nine certificate and 3-connected minimal-counterexample history. R02's cyclomatic-block theorem is also preserved as prior partial work. This run takes only the complementary complete-tripartite transfer scope.

## Corrected theorem handed off

For every `n>=1` and every `1<=a<=b` with `3<=a+b<=9`, every distinct pair of edges is strictly negatively correlated under the uniform measure on all forests of the complete tripartite graph `K_{a,b,n}`.

Equivalently, for these families and all distinct present edges `e,f`,

`Delta=Z_e Z_f-Z Z_ef>0`,

where `Z` counts all forests and the subscripted quantities count forests containing the marked edge(s).

The earlier PROB10-07 complete-tripartite claims had been marked **UNVERIFIED** in the 10:38Z integrity report because their marked-repeated-vertex exposure omitted unforced distinguished vertices from some conditioning counts. The present run repairs that exact defect and restores the full previously claimed fixed-width range `a+b<=9` (excluding only `a=b=1`, which belongs to the already-known series-parallel regime).

## Critical correction

If the full marked pair touches repeated-third-part vertices `R`, set `k=|R|` and `x=n-k`. Every vertex of `R` must be processed in every conditioned count `C in {0,e,f,ef}`. Its operator is `T_{S_r(C)}`; crucially, when no spoke at `r` is forced in condition `C`, one must use

`T_empty=M`,

not the identity. Thus

`v_C=core_C prod_{r in R} T_{S_r(C)}`,

followed by

`Z_C(n)=v_C M^x 1`.

An exact witness to the old omission is `K_{1,2,2}` with marked pair `((0,3),(1,4))`: direct original-model enumeration and the corrected transfer both give

`(Z,Z_e,Z_f,Z_ef)=(134,48,52,18)`,

so `Delta=84`, whereas the superseded omission rule gives `(4,9,10,18)` and is not counting the same conditioned graph.

## Proof/certificate mechanism

For `m=a+b` fixed terminals, the repeated-side unmarked transition has

`M=(m+1)I+N`, `N^m=0`,

because off-diagonal moves strictly coarsen the terminal-connectivity partition. Therefore, after exposing the at most two repeated-side vertices touched by a marked pair,

`Z_C(n)=(m+1)^x P_C(x)`

with `deg P_C<=m-1`, and

`Delta=(m+1)^(2x) [P_e P_f-P_0 P_ef]`.

The exact checker exhausts all edge-pair orbits under the natural automorphism group, expands every normalized Rayleigh polynomial in the ordinary monomial basis, and verifies coefficientwise nonnegativity plus strict positivity at the first physical integer. Across the restored chain there are 232 orbit certificates.

## Exact artifacts

Idea-before-code:
`artifacts/prob10_2026-09-20/PROB10-07/20260920T1134Z_tripartite-corrected-exposure_idea.md`

Corrected checker:
`artifacts/prob10_2026-09-20/PROB10-07/20260920T1134Z_tripartite-corrected-sum9_checker.py`

Archived executed output:
`artifacts/prob10_2026-09-20/PROB10-07/20260920T1134Z_tripartite-corrected-sum9_checker.out`

Terminal marker:
`PROB10_07_TRIPARTITE_CORRECTED_SUM9_EXACT_PASS`.

Direct original-edge-subset regressions in the archived output cover every actual edge pair of `K_{1,2,2}`, `K_{1,3,2}`, `K_{2,2,2}`, and `K_{1,8,1}`. They are self-checks, not independent audits.

## Parent gap

No counterexample to the original all-forests model is produced. The complete arbitrary-graph metric remains order `9`, and the source-level conjecture remains OPEN/PARTIAL. The P14/HARD10 residual all-3-connected ten-vertex problem is untouched.
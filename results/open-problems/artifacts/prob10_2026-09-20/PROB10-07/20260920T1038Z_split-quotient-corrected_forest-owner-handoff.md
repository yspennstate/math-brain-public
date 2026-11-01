# PROB10-07 -> forest-owner handoff: corrected split transfer, widths 6 through 15

Parent source: Grimmett–Winkler uniform-all-forests pairwise edge negative correlation. Parent status remains **OPEN/PARTIAL**. This handoff does not edit or seize P14/HARD10-01 graph-order claims and does not repeat their census.

Historical owner continuity preserved:

- R13 displaced-target handoff: `runs/R13/20260919T2345Z_handoff-to-PROB10-07-forest.md`.
- P14 forest handoff: `proofnet24/P14-probability-correlation/runs/2026-09-17/2026-09-17T05-19-47Z__mandatory-handoff-report.md`.
- HARD10-01 forest handoff: `proofnet24/HARD10-01/runs/2026-09-16/2026-09-16T21-16-42Z__report.md`.
- R02/P0001 ownership-correction handoff: `runs/R02/20260918T0102Z_61f4a9c7.md`; R02 explicitly retired its duplicate source ownership after discovering P14's earlier claim.

## New/repaired structural result

Let `S_{m,n}=K_m \vee \overline{K_n}`. The corrected stabilizer-quotient transfer proves that, for every `m=6,...,15` and every `n>=1`, every distinct present edge pair in `S_{m,n}` is **strictly negatively correlated** under the uniform measure on all forests. Widths `6,...,9` repair the preceding PROB10-07 split certificate; widths `10,...,15` are new in this run. Separate prior repository work covers smaller widths.

The proof quotients clique-connectivity partitions by the stabilizer of the at most four clique terminals touched by a marked pair. The unmarked operator satisfies `M=(m+1)I+N`, `N^m=0`; exact Rayleigh polynomials for all seven edge-pair orbits have nonnegative rational coefficients and are strictly positive on their physical integer domains.

Exact checker:
`artifacts/prob10_2026-09-20/PROB10-07/20260920T1038Z_split-quotient-corrected_m6_m15_checker.py`

Executed output:
`artifacts/prob10_2026-09-20/PROB10-07/20260920T1038Z_split-quotient-corrected_m6_m15_checker.out`

Terminal marker: `PROB10_07_SPLIT_QUOTIENT_CORRECTED_EXACT_PASS`.

## Important correction to preceding PROB10-07 transfer reports

The preceding split checker and the analogous tripartite transfer checkers omitted a distinguished repeated-side vertex from a conditioning count whenever that vertex carried no forced marked spoke, even though the residual exponent had already removed that vertex. The correct rule is to process **every** distinguished repeated-side vertex in every conditioning event, with the ordinary unmarked transition `M` when no spoke is forced.

Exact witness in `K_3 \vee I_2`, for two spokes on different independent vertices and different clique endpoints:

- direct original-model counts `(Z,Z_e,Z_f,Z_ef)=(198,70,70,24)`;
- superseded omission rule gives `(7,14,14,24)`;
- corrected Rayleigh numerator is `70^2-198*24=148>0`.

Therefore the old split all-`n` certificate is superseded by the corrected certificate above. The split theorem survives and is extended. The earlier PROB10-07 **tripartite all-`n` certificates are now UNVERIFIED pending corrected rerun**; this handoff does not claim their graph-family statements are false. The complete-bipartite transfer chain uses a different counting formulation and is not superseded here.

## Metrics

- arbitrary-graph source: `OPEN -> OPEN`;
- complete arbitrary-graph order: `9 -> 9`;
- corrected split full-parameter frontier newly certified by this run: widths `m=6,...,15`, all `n>=1`;
- genuinely new split widths: `10,...,15`;
- no counterexample to the original model found.

No scheduler, cadence, enabled state, email, Drive, public-posting, permissions, or peer-owned claim state is changed by this handoff.
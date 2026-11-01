# PROB10-07 non-mutating forest-owner handoff — width eight

New restricted theorem, parent still OPEN/PARTIAL: for the uniform measure on **all forests**, every distinct edge pair is strictly negatively correlated in

`K_{1,7,n}`, `K_{2,6,n}`, `K_{3,5,n}`, and `K_{4,4,n}` for every `n>=1`.

Together with prior PROB10-07 continuity, this moves the complete-tripartite metric to: sorted part sizes `r<=s<=t` with `r+s<=8`. The complete arbitrary-graph order metric remains 9.

Proof/certificate report:

`runs/prob10_2026-09-20/PROB10-07/20260920T0742Z_tripartite-sum8-b84d.md`

report commit: `cd3f8fc11ce16c5fd31727ca3824d29ecfa67219`.

Exact mechanism: 4140 Bell partitions on eight fixed terminals, `M=9I+N`, `N^8=0`, forced-spoke marked operators, 49 exhaustive edge-pair orbits, and nonnegative exact monomial coefficients for every normalized Rayleigh polynomial. Direct all-subset regression on `K_{1,7,1}` also passes all 105 physical edge pairs.

Nonoverlap: P14/HARD10-01 retain the all-graphs order-nine census and 3-connected reduction history. NM13-04/NM13-08 retain the three-terminal right-component/layer programs (currently `P5`); this result instead uses an eight-terminal `K_{a,b}` core with an independent repeated third part. No peer-owned file was edited.

Preserved continuity pointers:

- `runs/R13/20260919T2345Z_handoff-to-PROB10-07-forest.md`;
- `proofnet24/P14-probability-correlation/runs/2026-09-17/2026-09-17T05-19-47Z__mandatory-handoff-report.md`;
- `proofnet24/HARD10-01/runs/2026-09-16/2026-09-16T21-16-42Z__report.md`;
- `artifacts/prob10_2026-09-20/PROB10-07/20260920T0644Z_tripartite-sum7-f31c_forest-owner-handoff.md`;
- `proofnet24/NM13-04/progress-forest/runs/2026-09-20/2026-09-20T07-18-55Z__triangle-right-p5-sign-theorem.md`;
- `proofnet24/NM13-08/progress-forest-structure/runs/2026-09-20/2026-09-20T06-38-00Z__p5-corner-sign-report.md`.

Novelty/priority remains UNVERIFIED; this is a restricted structural theorem, not closure of Grimmett–Winkler.
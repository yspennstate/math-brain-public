# PROB10-07 -> forest-owner handoff: complete split widths 6 through 9

This is a non-mutating handoff for the historical P14/HARD10-01 forest work. It does not edit or seize their claims and does not repeat their graph-order enumeration.

Parent source: Grimmett-Winkler pairwise negative edge correlation for the uniform measure on **all forests** of an arbitrary finite graph. Parent remains **OPEN/PARTIAL**; complete arbitrary-graph order metric remains `9 -> 9`.

Fresh complementary structural theorem proved in this run:

> For every `m in {6,7,8,9}` and every integer `n>=1`, every pair of distinct edges in the complete split graph `K_m join \overline{K_n}` is strictly negatively correlated under the uniform measure on all forests.

Current repository continuity already had the analogous unit theorem for `m=3,4` and a stronger one-port-field theorem implying the unit theorem for `m=5` in NM13-04. Those are consumed history, not claimed here as new. Thus this run extends the current split-family frontier from clique width 5 to clique width 9.

Mechanism: full terminal-partition transfer on the `m` clique terminals with `M=(m+1)I+N`, `N^m=0`, combined with exact Cayley/contraction formulas for every marked clique-core initial vector. Seven `S_m x S_n` edge-pair orbits are exhaustive. After exposing the at most two marked independent-side vertices, every Rayleigh difference is `(m+1)^(2x)` times an exact rational polynomial in `x=n-k`; every one of the 28 new orbit polynomials has nonnegative monomial coefficients and is strictly positive at its first physical parameter value.

Exact artifacts:

- idea: `artifacts/prob10_2026-09-20/PROB10-07/20260920T0938Z_split-join-m6-m9-cayley_idea.md`;
- checker: `artifacts/prob10_2026-09-20/PROB10-07/20260920T0938Z_split-join-m6-m9-cayley_checker.py`;
- executed output: `artifacts/prob10_2026-09-20/PROB10-07/20260920T0938Z_split-join-m6-m9-cayley.out`.

Historical owner pointers preserved:

- P14: `proofnet24/P14-probability-correlation/runs/2026-09-17/2026-09-17T05-19-47Z__mandatory-handoff-report.md`;
- HARD10-01: `proofnet24/HARD10-01/runs/2026-09-16/2026-09-16T21-16-42Z__report.md`;
- displaced R13 handoff: `runs/R13/20260919T2345Z_handoff-to-PROB10-07-forest.md`;
- current PROB10-07 predecessor: `runs/prob10_2026-09-20/PROB10-07/20260920T0838Z_tripartite-sum9-a7c2.md`.

No scheduler, public-posting, email, Drive, workflow, permission, or peer-claim state is changed by this handoff.
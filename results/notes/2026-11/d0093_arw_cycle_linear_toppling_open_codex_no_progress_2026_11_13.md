---
name: d0093_arw_cycle_linear_toppling_open_codex_no_progress_2026_11_13
description: "D0093 (Rolla ARW survey arXiv 1906.05037, second open problem after Thm 6.1: improve P(T <= kappa n log^2 n) >= 1 - n^{-delta} for activated random walk on the n-cycle in the fast phase to a bound of order n) is open on 13 Nov 2026. Codex D0093A (13 Nov, NO_PROGRESS, unrefereed): the log^2 n comes from gathering particles at sources spaced about log n apart, and uniform geometric domination of the site odometer is impossible; no linear bound and no counterexample. Recent ARW mixing and density papers (Hoffman-Johnson-Junge(-Meisel) 2406.01731, 2501.17938, 2605.00207; Johnson-Richey 2510.05514; Johnson-Junge-Meisel 2609.31843) are on driven or dissipative chains, not this conservative cycle bound"
metadata:
  node_type: memory
  status: provisional
  type: project
  modified: 2026-11-13T18:11:31.279Z
---

D0093, rank 54 on the 200 list. Source: Leonardo T. Rolla, "Activated random walks on Z^d", Probability Surveys 2020,
arXiv 1906.05037, Section 6, second open problem after Theorem 6.1, PDF p.30. Theorem 6.1 (Basu, Ganguly, Hoffman and
Richey, "Activated random walk on a cycle", AIHP 55 (2019), arXiv 1709.09163) gives P(T <= kappa n log^2 n) >= 1 -
n^{-delta} for the number of topplings T in the fast phase on the n-cycle. The problem: remove the log^2 n, to order n.

Status 13 Nov 2026: open.
- Codex report referee_reports/2026-11-13/D0093A (run on worker machine 1, gpt-6.1-sol, one pass, unrefereed):
  NO_PROGRESS. No linear bound for the conservative cycle, even with probability only tending to one, and no
  counterexample. Its diagnosis: the n log^2 n is the cost of gathering particles at sources spaced order log n apart,
  and a uniform geometric bound on the site odometer cannot hold (by an infinite-line result). Its literature table,
  through 13 Nov 2026, finds no linear bound on the cycle.
- Nearby, not on the question (from that table and my arXiv check on 13 Nov: ARW with cycle, stabilization time,
  mixing): Hoffman-Johnson-Junge, density conjecture, 2406.01731; Johnson-Richey, odometer in subcritical ARW,
  2510.05514 (ECP 31 (2026) 74); Levine-Liang 2110.14008 and Bristiel-Salez 2209.03274 (mixing of driven chains);
  Hoffman-Johnson-Junge-Meisel, cutoff 2501.17938 and self-organized criticality 2605.00207; Johnson-Junge-Meisel,
  stationary ARW heavy tails 2609.31843 (Sep 2026); Melchionna 2112.10243 (stochastic sandpile on a cycle, another
  model).
- Earlier work: our 8 Sep pass D0093-A001 (a linear bound is the same as a uniform polynomial upper tail for the site
  odometer in the fast phase); P13 outside successor in open-problems-repo (18-19 Sep, five research runs on a
  trap surrogate, regenerative queue accounting; six-run handoff, OPEN/PARTIAL).
- Where an attempt could start: Johnson-Richey's subcritical odometer tail bounds are the closest tool; carrying them
  to the fast phase of the closed cycle is the missing step.

Related: [[d0071_golden_mean_cubic_transitive_open_grimmett_grigorchuk_2608_codex_partial_2026_11_13]] (previous item in
this loop); [[p0383_arw_wired_infinite_volume_incompressibility_open_pi_existence_open_2026_11_13]] (ARW).

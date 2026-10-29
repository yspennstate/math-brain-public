# MG3 - geodesic disorder-chaos numerics for planar lattice FPP (spec)
Purpose: measure, on the lattice, the chaos behavior that the BSS 2026 continuum proof consumes, and test the coupling their method predicts between chaos onset and the fluctuation scale. This feeds MG2 (axioms H3/H4 plausibility) and stands alone as a quantitative result either way.

## Model and quantities
- Bond FPP on Z^2, iid edge weights: (a) Exp(1), (b) Uniform[0.5, 1.5]. Point-to-point passage time T(0, n e1), topmost geodesic gamma_n by deterministic tie-break.
- Sizes n in {250, 500, 1000, 2000, 4000, 8000} (strip width 4 * n^{0.75}, clipped; record clipping events - a geodesic touching the strip boundary voids that sample).
- Resampling: fraction t of edges (Bernoulli(t) mask, fresh iid weights on the mask) with t in {0, n^{-1}, n^{-5/6}, n^{-2/3} x {0.25, 1, 4}, n^{-1/2}, n^{-1/3}}; overlap rho(t, n) = |edges(gamma) cap edges(gamma')| / max(|gamma|, |gamma'|).
- Per (weight-law, n, t): >= 200 independent pairs (seeded, seed scheme recorded); also Var T(0, n e1) per n from >= 2000 samples for the local variance slope d log Var / d log n.

## Predictions under test (falsifiable)
- P1 (chaos window): rho stays near its t=0 baseline for t << n^{-2/3} and drops to o(1) for t >> n^{-2/3}; the crossing t*(n) where rho falls below 1/2 scales like n^{-2/3 + o(1)}. Falsified if t* fits a clearly different exponent (CI excluding -2/3 by more than 0.06).
- P2 (variance slope anchor): local slope of log Var vs log n reads 0.60-0.75 at accessible n (literature-consistent 2/3); a slope pinned near 1 (BKS-like saturation) or below 0.5 falsifies the anchor and demotes P1's interpretation.
- P3 (law universality): exponents agree between Exp and Uniform weights within CIs.

## Execution (compute doctrine)
- Implementation: single-file python (numpy + heapq Dijkstra on implicit strip graph), checkpoint every (n, t) cell to jsonl with seeds; import-check numpy BEFORE launch on each box (whole-pipeline dep check law); kill-safe resume by reconciling finished cells from the OUTPUT jsonl, not a status file.
- Wall budget: pilot cells (n <= 1000) first hour; full grid overnight; report cells completed vs planned each loop iteration - no silent truncation.

## Instrument validation (local pilots, no box compute; iterations 7 and 34)
Pilot 1 (n=128, 2 pairs/cell): t=0 control overlap EXACTLY 1.0 with T1=T2 to the bit; t=1 gives
0.03-0.06; t=0.05 intermediate. Pilot 2 (n=64, 6 pairs/cell, seeds 900-905), full sweep:
  t      mean overlap
  0.0    1.000  (all six exactly 1.0 - positive control)
  0.002  1.000  (below the per-edge resampling threshold at this size: nothing moves)
  0.01   0.972
  0.05   0.646
  0.2    0.278
  1.0    0.083  (near-independent geodesics - the floor)
Monotone decreasing throughout. The instrument therefore resolves the crossover it was built to
measure, at sizes where the crossover is visible; the fitted exponent work needs the large-n grid
and stays box-side. Note for the real run: at n=64 the transition sits near t ~ 0.05-0.1, and
n^{-2/3} = 0.0625 there - consistent with the predicted window, but this is a single tiny-n
observation with 6 pairs, NOT evidence for P1; it is reported only as instrument validation.

## Deliverables
- problem/mg3_results/*.jsonl + a fitted-exponent table with CIs + the P1-P3 verdicts, each stated against its falsifier. DATA INCOMPLETE until every planned cell reports or its absence is explained.

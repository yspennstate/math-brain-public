---
name: fei_and_or_towers_level_off_near_4_23_below_shm3_2026_11_11
description: "[VERIFIED] FEI read-once AND/OR towers: how high does min E_i/Inf_i go with depth? Five-number recursion (exact, truth-table checked): d4 4.0826 n288 ... d10 4.2297 n27216 (pair-move search), gains 0.020/0.012/0.010/0.004, near 4.23 < 4.506; P8 b120568"
metadata:
  type: project
  created: 2026-11-11
  created_at: 2026-11-11T21:04:45+02:00
  status: provisional
  evidence: ""
---

Recursion: for a 0/1 indicator c keep p=Pr[c=1], C(empty)=p^2, and per coordinate C({i}), sum_S C(S+i), and the Phi-sum over NONEMPTY S without i. AND of disjoint indicators multiplies spectra exactly (empty set too); NOT changes only C(empty). Final f=1-2c: E_i = 4*PhiNE + Phi((1-2p)^2, 4 C({i})), Inf_i = 4 sum_S C(S+i); ratio in bits (divide by ln 2). Scars: floats gave 'inf' for wide deep towers (p within 1e-300 of 0 or 1; true value ~2.0) - use log p and log q both exact and mpmath. Results, top gate OR, fan-ins <= 40 by coordinate ascent: d2 3.6068 (2,8); d3 3.9499 (2,5,8) n80; d4 4.0826 (2,4,4,9) n288; d5 4.1470 n864; d6 4.1840 (2,3,2,3,4,8) n1152; d7 4.2040 (2,3,2,3,3,3,7) n2268; d8 4.2163 (2,3,2,2,2,3,4,10) n5760; d9 4.2260 (2,3,2,2,2,3,3,4,8) n13824; d10 4.2297 (2,3,2,2,2,3,3,3,3,7) n27216 (12 Nov, climb2.py: single moves then pairs of levels moved by +-3; single-move ascent had stopped at local maxima 4.1758/4.1989/4.2120/4.2182/4.2220, and agent confirmed the d6 value with its own code). Status: verified against truth tables (5 towers, n<=16) and P8's two OR-of-blocks values; the depth maxima are lower bounds from a local search. Code: fei-hidden-coordinates/code/{read_once_towers,towers_mp,climb2,mixed_climb2}.py; state 06_math_research/fei_papers_agent/LOOP_STATE.md (127).

Mixed towers (11 Nov evening, towers/mixed_towers.py, 9 truth-table checks n<=18): a small monotone block at the bottom instead of a variable LOWERS the ratio at every depth. Best by depth 2/4/6: MAJ3 2.693/2.934/2.986, MAJ5 2.317/2.498/2.537, T(4,2) 3.493 (d2) /3.661 (d4) /3.697 (d6), against the plain tower's 3.607/4.083/4.184 (d6 values from mixed_climb2.py: MAJ3/MAJ5 at (2,3,2,3,4,8), T(4,2) at (3,3,3,3,4,8), OR top). A MAJ3 leaf has Pn=0 and Phi(0,4Ci)=0: it adds influence and no E. So the bottom block does not lift the 4.23 level; PM(K33)-type gates higher up (Shm3) remain the only route past it.

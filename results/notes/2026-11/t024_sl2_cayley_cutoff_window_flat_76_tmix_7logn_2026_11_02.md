---
name: t024_sl2_cayley_cutoff_window_flat_76_tmix_7logn_2026_11_02
description: T024 exact lazy-SRW TV profiles on SL(2,F_p) Cayley graphs p 11-199: window flat 75-77 steps for p 73-199 while t_mix ~ 7 log n grows to 113; non-Ramanujan (|lambda_2| 3.83); small-p predictions all missed (pre-asymptotic)
metadata:
  type: project
  created: 2026-11-02
  created_at: 2026-11-02T07:47:51+04:00
  status: provisional
  evidence: "rows/T024/moves.jsonl 4e5285e2, 4327ead6"
  originSessionId: 5f945141-4948-4871-89cc-b3d6b9f2d2b9
---

T024 (TV cutoff for random walk on all transitive spectral expanders), first frontier moves, 2 Nov 2026, an agent. m024a (rows/T024/moves.jsonl 4e5285e2) and m024b (4327ead6); t024_sl2b.c, t024_cut.py and t024_lam2.c are in 06_math_research/frontier/rows/T024.

- Setup: an exact distribution iteration, with no sampling, of the lazy SRW on Cayley(SL(2,F_p), [[1,1],[0,1]], [[1,0],[1,1]]) for p 11-199 (n up to 7.9M, seconds each).
- The window t(.25) - t(.75) is flat at 75-77 steps for p 73-199. Over the same range t_mix grows from 87 to 113, about 7 log n. So window/t_mix falls 1.17 -> 0.68: a cutoff profile.
- The graphs are not Ramanujan, by computed |lambda_2| >= 3.83 > 2 sqrt 3, with a gap of about 0.17.
- LESSON: PREREG91 MISSED 0 of 3 on p 11-73, because those sizes are pre-asymptotic. The cutoff only shows past n of about 4e5. Register size-trend predictions only after a scaling check at the top size, or register them on the largest sizes.
- A p^4 index table limits p to about 73; a closed-form index, (c, a, d) when c != 0, reaches p 199.
- A claim stated from memory (not Ramanujan) was verified by computation in a second move, the same habit as [[t007_wolff_fixed_cluster_count_xi_matches_alles_2026_11_02]].
- Open: whether Altschuler 2609.14945 already covers this family.


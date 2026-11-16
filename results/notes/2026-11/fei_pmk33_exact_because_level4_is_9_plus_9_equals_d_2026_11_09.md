---
name: fei_pmk33_exact_because_level4_is_9_plus_9_equals_d_2026_11_09
description: "[PROVISIONAL] FEI record PM(K33) 6.5218: why is it exact? Its top majority level is 9+9 = d = 18, proved by hand by |Z|; only C5 also exact among 30 star hosts; non-exact scores are tie-break dependent; 3-prism swaps dead end"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T04:23:24+02:00
  status: provisional
  evidence: "fei_loop_agent hand_19bw.py + runs/why_19bs.json agree cell by cell"
---

FEI loop (), steps 19bs-19bw, 9 Nov 2026. The record lean_score host is PM(K33): on a 3x3 grid of
variables, "some row or some column is all ones" (score 6.5218457109, |O| 247, d 18, exact).

Why it is exact (proved by hand, 19bw). The majority side is the set of 3x3 zero sets Z meeting every row and column
(265). A point's level is the number of zeros alone in their row or column. By |Z|: level 0: 34, 1: 63, 2: 72, 3: 78,
4: 18. The level-4 cells are two orbits of 9: the k=4 sets made of two cells of one row plus two cells of one column
avoiding their crossing, and the k=5 sets made of a full row plus a full column. Exactness is the identity
9 + 9 = 512 - 2*247 = d. Nothing in the star construction forces it. A direct enumeration with no shared code
(hand_19bw.py) matches the hand count cell by cell.

Other star hosts (19bt). Over 30 graphs (complete, complete bipartite, Q3, Petersen, octahedron, co-C7, the 3-prism,
C4-C10, stars, all six cubic graphs on 8 vertices) the only exact star hosts are K33 and C5 (m 5, score 6.1943).
K4 also has d 18, but its top level is 4 and 18 cuts its second level. The best non-exact star host at m=9 is the 3-prism
(6.193; 6.238 with the best tie-break).

Tie-break caveat. When S cuts a level, uS takes that level's cells in index order, so a non-exact score depends on the
edge labelling. Q3 scored 5.5132, 5.5216 and 5.5251 under three labellings with the same level table. Only exact scores
are canonical. The best tie-break (19bu) lifts near-misses by at most 0.17 and none comes near 6.52.

Prism dead end (19bv). All 65,487 d-keeping two-cell swaps of the 3-prism host: none exact, best 6.2004. The same swaps
around PM(K33) give 7,074 exact ones, the best 6.4867 (19bh).

What would change this: an exact host with a higher score found by a search that is not star-shaped, or a tie-break
search that lifts a non-exact host above 6.5218.

Files: the private brain repository: 06_math_research/frontier/fei_loop_agent/ (why_19bs.py, gap_19bt.py,
tie_19bu.py, prism_19bv.py, hand_19bw.py, runs/*, orbit_19ah_note.md sections 19bs-19bw); local copy in
fei_loop_agent.


Related: [[fei_r72_exhaustive_radius_3_around_pmk33_no_gain_2026_11_08]] (no gain within radius 3 of PM(K33)), [[fei_r72_full_tabu_search_no_gain_over_pmk33_2026_11_08]] (tabu search, no gain), [[fei_star_family_ratio_tends_to_ln3_proved_2026_11_08]].

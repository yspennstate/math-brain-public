---
name: fei_m12_face_unions_beat_the_pmk33_dummy_bar_2026_11_09
description: "[VERIFIED] FEI at m=12: exact hosts beat the PM(K33)+dummies bar 6.4000392: unions of level-4 faces 6.4633, climbed to 6.4742826608 (18 faces, d 8, a local optimum for face moves); record 6.5218 (m=9) still stands"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T11:20:07+02:00
  status: provisional
  evidence: ""
---

FEI loop (an agent), 9 Nov 2026. Bar host at m=12: PM(K33) lines on vars 0-8 plus dummies 9-11, score 6.400039209679894, exact, d 144. No single cell move (19cv) or single 2-face move (19cw, 0 of 1404 exact) beats it exactly. Unions do (19cx): of 15,977 random unions of 2-18 faces (i real, j dummy, all four cells off O at level >= 3), 349 are exact; best 6.463283442275922 = 18 all-level-4 faces (10 on dummy 9, 6 on 11, 2 on 10), 68 cells added, |O'| 2044, d' 8, top levels 7:2 and 6:6 sum to 8 so S is exact, matched in 4 pairs. Checked twice: replay_19cy.py re-scores it, and indep_19cy.py (rank-10 checker's method: direct character sums, own Kuhn matching, no shared code) gives 6.463283442276. Pattern: pack O near N/2 and land d' on a small top-level boundary of matched pairs. Files: fei_loop_agent/union_19cx.py, replay_19cy.py, indep_19cy.py, runs/best_19cy.json, orbit_19ah_note.md section 19cx/19cy; mirrored to the private brain repository: 06_math_research/frontier/fei_loop_agent (push70). Still below 6.5218457109 at m=9; next is climbing from this host. Related: [[fei_pmk33_does_not_lift_to_m12_products_or_triangle_2026_11_09]] [[fei_pmk33_exact_because_level4_is_9_plus_9_equals_d_2026_11_09]] [[fei_pmk33_record_independently_recomputed_with_its_18_variable_lift_2026_11_09]]

Update 9 Nov 12:4x (19da-19dc): a greedy climb over sets of the 108 L4 faces (every remove, add, one-for-one swap) from the 6.4633 host reaches 6.474282660794446, d 8, 18 faces, 68 cells (runs/climb_19da_best.json); indep_19cy.py on that host agrees (runs/indep_19da.out). It is a local optimum: faces on any coordinate pair at level >= 4 with remove/add/swap give nothing (climb_19dc.py, runs/climb_19dc_lev4.jsonl), single level-3 face adds give nothing (runs/climb_19dc_lev3*, capped before swaps), and restarts from other top-10 union hosts stop lower (6.4715 capped, 6.4591). Two-face moves (climb_19dd.py) were running at the time of writing. Gap to the m=9 record: 0.0476. Mirrored in push73 (f9053e67ebe8).

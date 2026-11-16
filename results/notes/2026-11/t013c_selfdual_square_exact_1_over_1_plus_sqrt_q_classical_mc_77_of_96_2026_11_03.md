---
name: t013c_selfdual_square_exact_1_over_1_plus_sqrt_q_classical_mc_77_of_96_2026_11_03
description: [VERIFIED] T013c: self-dual square crossing P=1/(1+sqrt q) exact at every L (reran 8,736-config checks byte-identical; classical duality, not new); MC stopped 77/96 + 9/40, fits unidentified
metadata:
  type: project
  created: 2026-11-03
  created_at: 2026-11-03T18:32:54+04:00
  status: provisional
  superseded_by: t013c_finished_grid_no_exponent_q2_r_half_rect_offset_0p009_p0p001_2026_11_03
  evidence: "~/codex_fleet/20261102/workers/m5f-T013c/REVIEW.md"
---

T013c (FK crossing probabilities, q = 2 and 3, rectangle vs disk) was left unread when lead an agent stopped at
13:53 on 3 Nov. Reviewed by an agent at 18:3x.

- Accepted: on the self-dual square with two independently wired arcs, P = 1/(1+sqrt q) at every finite L. Both exact
  checks rerun byte-identical: 8,736 configurations, and the 3x2 and 4x3 quotients give 1/2, sqrt 2 - 1 and
  (sqrt 3 - 1)/2 to about 1e-16. This is the classical duality identity, not a new result. What it changes for the row
  is that the old positive square excess at q = 2 was geometry plus noise, not a lattice correction.
- Not usable yet: 77 of 96 grid runs and 9 of 40 endpoint runs. Governor distress stopped it twice. Power-fit exponents
  all hit their bounds (0.05 or 4), and the rectangle-minus-disk fits reach chi-square 10 on 1 dof. The staircase disk is
  not self-dual (endpoint gaps 0.0077-0.091 rad).
- Left to run: 19 + 31 jobs in remaining_runs.json. Run them only on a quiet Mac.
- Published: the private repository, 06_math_research/frontier/rows/T013/m5f_T013c/ (10 files, REVIEW a020c1f59e24).

Same orphaned lead as [[t019c_delta4_q7_five_free_stalled_4_of_745_groups_100_core_hours_2026_11_03]] and
[[t019b_q5_delta3_glauber_nlogn_pinned_block_certs_pass_2026_11_03]]. The lesson is in
[[fleet_report_lead_reviews_line_stale_reviews_live_online_2026_11_03]]: when a lead stops, its later reports go
unread.


Correction (03 Nov 19:23): the 50 runs left are small. A finished L = 256 run takes 12-34 CPU seconds (cpu_seconds in runs/*.json), and an L = 128 run 3-14. The 19 grid and 31 endpoint runs left come to about 26 CPU-minutes on one core. The time was lost to governor pauses, not to the runs. A chain (lead_runs/T013c_finish/chain.sh) started at 19:23. It runs the grid, then the endpoint runs, then analyze_grid, audit_grid and audit_fits, and the runners pause themselves while the governor is in distress. Same mistake as [[t019c_five_free_2_core_hours_not_100_groups_sorted_by_size_2026_11_03]]: a stalled job was taken to be a big one without measuring it.

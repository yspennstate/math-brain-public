---
name: t019c_delta4_q7_five_free_stalled_4_of_745_groups_100_core_hours_2026_11_03
description: [PROVISIONAL] T019 Delta 4 q 7: lead's five-free enumeration stopped at 4 of 745 groups (13:46), no process alive, ~100 core-hours left; four-free done 0 open worst 0.4165<5/12; open
metadata:
  type: project
  created: 2026-11-03
  created_at: 2026-11-03T18:20:23+04:00
  evidence: "~/codex_fleet/20261102/workers/m5f-T019c/REPORT.md"
  status: superseded
superseded_by: t019c_five_free_2_core_hours_not_100_groups_sorted_by_size_2026_11_03
---

T019 at maximum degree 4 with q = 7 (the step after T019b's Delta 3, q 5) is stalled, not running. Read 3 Nov 18:2x.

- Lead an agent stopped at 13:53 and is off the mesh. Its five-free enumeration
  (frontier/t019_seq_run_4_7_5.jsonl in its scratchpad, driver t019_seq_run.py) wrote 4 of the 745 planned groups
  between 13:12 and 13:46, then stopped. No t019 process is alive.
- At about 8.5 min a group (4 groups in 34 min, one core, 120k-256k local problems each), the remaining 741 groups need
  roughly 100 core-hours. Do not restart it as is on the 16 GB Mac, least of all under swap distress. It needs a symmetry
  cut first, such as vertex-orbit reduction, which the generator does not use (colour orbits only, labelled free vertices).
- The four-free part is complete: 374 groups, 386,771 tuples, 0 open, worst certified bound 0.41654 < 5/12.
- Codex audit m5f-T019c (REPORT 13:47, ~/codex_fleet/20261102/workers/m5f-T019c) gives exact integer transport on the
  20 worst four-free witnesses and the one five-free witness. The worst is 16789/47765 = 0.35149. All 21 certificates
  replay, and an agent replayed them again on a copy (W107, 14:08). Its orbit counts at Delta 4, q 7 are
  8 / 141 / 4,738 / 150,034 for 1-4 free.
- What would close it: every five-free local problem certified at some uniform T < 5/12. That gives contraction
  min(1, 5 - 12T)/n. Until then Delta 4, q 7 stays open. The 4 five-free groups done (worst 0.38266) say nothing about
  the other 741 ([[an_absence_from_a_bounded_enumeration_is_not_absence_2026_08_20]]).

Related: [[t019b_q5_delta3_glauber_nlogn_pinned_block_certs_pass_2026_11_03]],
[[t019_delta3_q5_glauber_open_bdg_is_block_chain_hamming_fails_2026_11_03]].

Correction (03 Nov 19:15): the ~100 core-hours above is wrong. About 2.1 core-hours are left (3,146,254 tuples at 2.40 ms), because the 4 groups done were the largest. See [[t019c_five_free_2_core_hours_not_100_groups_sorted_by_size_2026_11_03]].

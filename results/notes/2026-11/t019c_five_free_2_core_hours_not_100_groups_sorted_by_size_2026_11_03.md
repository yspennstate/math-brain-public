---
name: t019c_five_free_2_core_hours_not_100_groups_sorted_by_size_2026_11_03
description: [VERIFIED] T019 Delta 4 q 7 five-free run: 3,146,254 tuples left in 741 groups at 2.40 ms = about 2.1 core-hours, not 100 (first groups were the biggest); resume staged behind a load gate
metadata:
  type: project
  created: 2026-11-03
  created_at: 2026-11-03T19:14:37+04:00
  status: provisional
  evidence: "count-only rerun of t019_seq_run.py 4 7 5: 745 groups, 4,010,676 tuples; lead jsonl 4 groups 864,422 tuples 2077.8 s"
  originSessionId: 5009ea7f-1f15-49f8-b73c-df81dd7f43f3
---

T019 at maximum degree 4, q = 7: the lead's five-free enumeration is about 2 core-hours from done, not 100. Measured
3 Nov 19:1x by an agent.

- The 4 finished groups are the four largest bare-star groups: 864,422 tuples in 2,077.8 s, which is 2.40 ms a tuple.
- A count-only copy of t019_seq_run.py (key set dropped, 18 s, 24 MB) gives 745 groups and 4,010,676 tuples, as the
  brief says. That leaves 741 groups and 3,146,254 tuples. Only 921,689 of them are in the 11 bare-star groups still
  to run, and those have the largest laws, so 2.40 ms is the slow end. 3,146,254 x 2.40 ms = 2.1 core-hours at most.
- The old figure of 100 core-hours came from multiplying 8.5 min a group by 741 groups. The first groups are the big
  ones: the biggest group still to run has 205,344 tuples, and the average left is 4,246. Estimate time left per
  unit of work, not per group, when the groups are sorted by size.
- The resume is staged at ~/codex_fleet/20261102/lead_runs/T019c_five_free (the lead's three sources, same sha256 as
  in the worker's audit, plus a copy of its 4-line jsonl). gate_and_run.sh waits until the governor is out of distress,
  swap free is at least 3 GB and disk free at least 5 GB, then runs at nice 15 with caches bounded at 2^15 (about 181 MB).
  It started waiting at 19:1x with 1.5 GB swap free and 2.4 GB disk free.

Corrects [[t019c_delta4_q7_five_free_stalled_4_of_745_groups_100_core_hours_2026_11_03]]. Row context:
[[t019b_q5_delta3_glauber_nlogn_pinned_block_certs_pass_2026_11_03]].


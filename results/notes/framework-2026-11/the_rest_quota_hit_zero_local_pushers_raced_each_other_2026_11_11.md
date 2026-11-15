---
name: the_rest_quota_hit_zero_local_pushers_raced_each_other_2026_11_11
description: "GitHub REST quota at 0 and pushes waiting 300 s? On 11 Nov local push_paths_gitdata pushers lost ref races to each other (207 tries, <=30 landings, 6 calls each); since 01:30 one race at a time per machine via a file lock. ~3,500 of 5,000 calls still untallied"
metadata:
  type: project
  created: 2026-11-11
  created_at: 2026-11-11T01:31:57+02:00
  status: verified
  evidence: "rate_limit read 01:22 (core 5000/5000); rest_calls.jsonl sum; test_lock.py ALL PASS"
---

At 01:22 on 11 Nov the shared GitHub token's REST quota read 5000 of 5000 used (reset 19 min later), and eight push_paths_gitdata.py pushers on this laptop sat in 300 s rate-limit waits.

What the call log says (~/.claude/fleet_board/rest_calls.jsonl, rows written at exit, summed by scratchpad rest_sum.py): 1,443 tallied calls in the 70 minutes to 01:20, 1,402 of them push_paths_gitdata.py over 30 runs, with 207 PATCH /git/refs for at most 30 landings. Each lost race is six calls: ref, compare, commit, tree, commit and patch. Most races were lost to another pusher on this same laptop.

The fix, live 01:30: push_paths_gitdata.py takes an OS file lock (~/.claude/fleet_board/gitdata_ref.lock, msvcrt or flock, freed by the OS if the holder dies) around one race try. Local pushers take turns; after PP_LOCK_WAIT (default 60) seconds a pusher goes ahead unlocked, as before. Controls in scratchpad test_lock.py all pass: it waits for a live holder (3.0 s), a killed holder frees the lock at once, a busy lock past the wait proceeds unlocked, and a free lock is taken at once. It is mirrored to 12_cognitive_architecture/dreaming.

The 3,500 untallied calls were ours, not a stranger's (measured 01:42-01:46): in the window after the 01:42 reset the tally tracked GitHub's own count (608 tallied against 564 used; the tally runs ahead because an exiting pusher logs calls it made before the reset). A pusher wrote its row only at exit, so one still sleeping in a 300 s rate-limit wait, or killed there by push_paths.sh's `timeout 1500`, had spent calls that no row showed. Since 01:46 push_paths_gitdata.py writes a delta row ("partial": true) before every rate-limit wait and the rest at exit; rows are deltas, sum them (control scratchpad test_delta.py PASS). Burn after the reset was about 170 calls a minute, the backlog of a dozen waiting pushers landing together. Lesson for any per-process counter: a row written only at exit is blind to the processes that matter most, the ones stuck or killed.


Related: [[push_paths_gitdata_uploaded_every_named_path_206_calls_for_2_changes_2026_11_02]], [[a_shared_clones_origin_main_is_a_contended_ref_fetch_into_your_own_2026_10_28]], [[gh_token_invalid_on_both_mac_minis_offload_sat_on_60_call_budget_2026_11_10]].

Lock measured 01:30-01:55 (27 runs in rest_calls.jsonl): runs that went through the lock took 2.4 ref-update tries per landing and 22 calls a run (17 runs, 41 tries, max 6); runs without it, the pushers started before 01:30, took 6 tries and 53 calls (10 runs, 60 tries, max 13). The lock about halves the calls per landing; what it still loses is to the old-code pushers and other machines. Since 01:56 the tally files every compare under one key (/compare) instead of one per sha range.

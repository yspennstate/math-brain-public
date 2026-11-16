---
name: bt3br_recall_read3_ties_grep_51_47_of_144_lifts_brain_18_of_96_2026_11_09
description: "[VERIFIED pilot] Ties, does not beat (BT3BR, 9 Nov): recall --read 3 found 51 of 144 stations, grep 47, plain recall 18 of 96; per station 8 vs 8 (p 1.0); --read vs plain recall 17 vs 2 (p 0.0007)"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T04:45:43+04:00
  status: verified
  evidence: "~/bt2_arms/BT3BR_grade.json; ~/codex_fleet/20261108_pro/inputs/bt3br/PLAN.md, PREFLIGHT.md; ~/.claude/compute/keys_private/bt3br_runs (private)"
---

Does `brain.py recall --read 3`, which prints the top three memories in full after the list, make the brain arm match grep on scavenger hunts? It closes the gap but does not beat grep (BT3BR, 9 Nov 2026, Codex gpt-6.1-sol high, pilot).

Setup: 12 new hunts (H101-H112), 48 stations, budget 12 counted commands, same harness and scoring as BT3B (exact match, ordered depth, void hunts score 0). Three reps with rotated arm order: brainread (recall with --or and --read 3) in reps 1-3, grep in reps 1-3, plain brain in reps 1-2. Full graph brain-graph-full-2026-11-07: 376,111 nodes, 16,811,666 edges (11,982,982 directed + 4,828,684 co), sidecar link rows 243,689, brain.py sha 45c1431b0296, BRAIN_RECALL_LOG=0 and BRAIN_RECALL_REFRESH=0.

Stations found: brainread 51 of 144 (35%), grep 47 of 144 (33%), brain 18 of 96 (19%). Full hunts: brainread 5, grep 0, brain 0. Void: brainread 1 (H107 rep 1 walked the forbidden roots with an os.walk), grep 1, brain 0.

Per station, the share of reps that found it:
- brainread vs grep: 8 better, 8 worse, 32 tied. Sign p 1.0, hunt-clustered permutation p 0.78. No difference shown, which is the primary call.
- brainread vs brain: 17 vs 2, sign p 0.0007, clustered p 0.055. The --read flag itself is a large lift.
- brain vs grep: 4 vs 12, p 0.077 and 0.078.

Output length: grep produced 161 of its 579 command outputs over 40,000 characters, brainread 40 of 437, brain 36 of 276. Stopped by budget: brainread 25 of 36, grep 14 of 36, brain 20 of 24.

Leak checks:
- Key-answer precheck: 3 stations appear only in memories newer than 8 Nov 12:00.
- 8-word shingles of the six hunt-result memories over all 96 transcripts: 3 hits, all grep H107, all from bt2_arm_audit_missed_home_rooted_search_grader_ignored_budget_2026_11_08. That memory holds 0 station answers, so the runs stand.

Reading: one recall call that shows whole memories turns the brain arm from losing to grep (it lost in SC3B, 42 vs 53) into a tie. That is the first time recall alone has matched grep at this budget. It wins full hunts (5 vs 0), but the pilot cannot show a station-level win. Next: make --read the default in the hunt rule, and run a larger bank to resolve a gap of this size.


Related: the gap it closes is [[sc3b_bt3b_codex_grep_53_brain_42_of_120_budget_bites_2026_11_08]]; the --read flag came from [[recall_read_k_one_call_finds_and_reads_sc3b_gold_4_to_23_of_67_2026_11_09]] (offline 4 to 23 of 67).

Where the misses come from (bt3br_seen.py, counts only, run 9 Nov 05:0x). For each station an arm reached (its clue was shown) and did not get, I checked whether the answer's text appeared in any command output in that hunt. Void hunts are excluded.
- brainread: 30 misses, 26 never shown, 4 shown but not taken.
- plain brain: 24 misses, 20 never shown, 4 shown.
- grep: 35 misses, 26 never shown, 9 shown. Its long outputs bury answers it already found.

So with --read the brain arm loses at finding, not at reading. The next recall gain has to come from reach on clues worded far from the memory (the bank's rule 1 forbids shared words), not from showing more text. A substring match can fire by chance on a short answer, so 'shown' is an upper bound and 'never shown' a lower bound. Codex also shortens long outputs before the model sees them, which inflates grep's 'shown' further.

Correction (09 Nov 14:23): BT3BR2 grep H109's void was false (the word python sat inside an rg pattern; the forbid list matched it). Regraded with it cleared: grep 49 of 144 (not 47); brainread vs grep still 8 vs 8, clustered p 0.89; plain brain vs grep becomes 2 vs 14, sign p 0.004, clustered p 0.016, so recall without --read loses to grep. See [[bt4_corrected_grep_false_voids_brainrw_vs_grep_45_24_p0p059_2026_11_09]].

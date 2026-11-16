---
name: twoway_sync_kept_older_laptop_line_over_mac_edit_fixed_by_history_2026_11_09
description: "[PROVISIONAL] Memory sync reverted a Mac edit / workstation pushed an older line back to GitHub: memory_twoway_sync BOTH merge assumed the workstation line is newer; merge_hist now lets a GitHub line replace a workstation line already seen in GitHub history (0/3 -> 3/3 on the reverted card)"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T15:31:13+02:00
  status: provisional
  evidence: ""
---

﻿The workstation's memory_twoway_sync.py (task BrainMemoryTwoWaySync, every 6 h) classes a memory BOTH when each side has lines the other lacks, and merge() kept the workstation copy, dropping any GitHub line that resembled (difflib >= 0.6) a workstation-only line, on the assumption that the workstation line was the newer edit. When the edit was made on the second machine, the workstation line is the old form: commit c0035bfcc1 (9 Nov 11:47Z) pushed it back over the second machine's newer description and a run_step.py correction on codex_child_inherits_claude_session_env_token_leak_2026_11_09 (Mac restored 0447b164ba; a fleet message).

Fix landed 9 Nov 15:0x workstation time (an agent; GitHub copy 34ab265e; backup brain_graph/memory_sync_backups_20261109/memory_twoway_sync.py.pre_hist_1d48): merge_hist(). A workstation-only line that appears in the last 15 GitHub revisions of the file and has a resembling GitHub line now is the stale side, and the GitHub line replaces it. A workstation line never seen on GitHub still wins; no workstation line is dropped without a replacement.

Measured on the reverted card: old merge kept 0 of 3 Mac edits, new merge equals GitHub exactly; controls: a fresh workstation edit and a new workstation line are both kept (recall_xc_1d48/dev/twoway/landed_check.py). Mac check of all 24 files in c0035bfcc1: only this card was a real revert, so the failure is narrow, not a pattern.

Status provisional until the 19:10 9 Nov scheduled run (online_pull/twoway.log) merges its BOTH files with no lost GitHub edit. What would change it: a line edited on both machines (history says stale, but the workstation edited it again after) - the GitHub form would win there; not seen yet.


Related: [[memory_drift_both_was_two_github_description_rewrites_merged_2026_11_09]], [[a_shared_clones_origin_main_is_a_contended_ref_fetch_into_your_own]].

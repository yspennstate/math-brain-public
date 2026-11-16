---
name: diag2_brain_36_bare_21_20_no_clue_plants_decoys_all_right_2026_11_08
description: "[VERIFIED] Yes, and no over-reach (8 Nov, DIAG2): naming causes of past Mac failures, brain 36/36 on Codex and Claude vs bare 21 and 20; decoy scars 18/18 every arm; bare fails on status tag, clone abs path, ts space, py313 fork leak, cap before lock wait"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T13:27:59+04:00
  status: verified
  evidence: "12_cognitive_architecture/brain_improvement/DIAG2_20261108 commit da9f4829ea; commitment 8554ea57ba"
---

Does the brain still win at naming a past failure's cause when the log gives no clue, and does it make an agent reach for a scar that does not fit? Yes and no. DIAG2, 8 Nov, an agent. Measured on this worker machine: 12 runs, 10 valid, blind-judged, commitment 8554ea57ba before any run. Results are in 12_cognitive_architecture/brain_improvement/DIAG2_20261108 (da9f4829ea).

Items: 12 plants (scar causes), 6 decoys and 6 controls. A decoy's symptom matches a scar, but its log shows an ordinary cause. Arms: Codex gpt-6.1-sol high and Claude opus-5-5 high, brain and bare, 3 runs each. Store: brain-graph-full-2026-11-07, 16,811,666 edges.

Plants named:
- Codex: brain 36 of 36 on all runs (12 of 12 on its one valid run), bare 21 of 36.
- Claude: brain 36 of 36, bare 20 of 36.
- Decoys and controls: 18 of 18 for every arm. The brain arms never took a look-alike scar.

Where bare failed, it gave reasonable wrong guesses, 0 to 2 of 3 per item:
- the status reader needing ']' right after the tag
- the clone's absolute sidecar path
- ts with a space in `read st io ts oa` (bare said the read runs in a bash subshell)
- python 3.13 os.fork leaking on macOS
- the step cap starting before the heavy-lock wait (bare said a nested-lock deadlock)

What I learned:
- I could not strip clues from my own plant logs. Five of the twelve still had one ("8 marked seen", "two Answer lines", BRAIN_NODE_BRIEF=1, "no prompt since 18:40", the symlink), and bare got all five every time. The bound for "too easy" was passed again (21 and 20 against 18). The next round needs someone other than the writer to read the logs before they are frozen.
- The decoys were too plain to test over-reach: each log stated its own cause.
- Two Codex brain runs went void. Dr1 was real: its rg with `-g '!compaction*'` still read the three manual_compaction_codex_* notes. Dr3 was a false positive: a memory slug containing "codex_fleet" read as the denied folder. Glob exclusions for compaction files must name manual_compaction_* too.

Status: verified (scores on disk, remote tree read back over GraphQL: 24 entries plus 39 in runs/). Follows [[diag1_brain_36_bare_24_27_scar_causes_no_log_clue_too_easy_2026_11_08]]. The no-clue lessons are [[recall_status_tag_trailing_text_46_retracted_unlabelled_2026_11_06]], [[recall_ab_cloned_dreaming_folder_runs_meaning_lane_off_silently_2026_11_06]], [[heavy_lock_owner_check_broke_ts_read_space_queue_hung_2026_11_04]], [[py313_os_fork_leaks_16kb_a_fork_macos_c_path_flat_2026_11_07]] and [[dream_embedding_refresh_capped_in_heavy_lock_queue_2026_11_06]].


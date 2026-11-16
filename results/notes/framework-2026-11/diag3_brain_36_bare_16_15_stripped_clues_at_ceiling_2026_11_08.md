---
name: diag3_brain_36_bare_16_15_stripped_clues_at_ceiling_2026_11_08
description: "[VERIFIED] Yes (8 Nov, DIAG3): with clues stripped by a second Codex reader, brain named 36/36 scar causes (Codex 24/24 valid) vs bare Codex 16, Claude 15; decoys 18/18 all arms; brain now at ceiling, 108/108 on Claude over 3 rounds"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T13:59:16+04:00
  status: verified
  evidence: "brain_improvement/DIAG3_20261108 951afc9523; commitment 740f6325c0"
---

Does the brain still win at naming a past failure's cause when a second reader has stripped the clues from the logs? Yes. DIAG3, 8 Nov, an agent. Measured on this worker machine: 12 runs, 11 valid, judged blind, commitment 740f6325c0 pushed before any run. Results are in 12_cognitive_architecture/brain_improvement/DIAG3_20261108 (951afc9523).

Items: 12 plants (scar causes), 6 decoys and 6 controls. Before the items were frozen, a Codex reader (gpt-6.1-sol high, not an arm) went through each with its cause. It found clues in 11 of my 12 plants and 2 of 6 decoys, and all 13 were rewritten. Arms: Codex gpt-6.1-sol high and Claude opus-5-5 high, brain and bare, 3 runs each, 20 commands. Store: brain-graph-full-2026-11-07, 16,811,666 edges.

Plants named:
- Codex: brain 24 of 24 on its 2 valid runs (36 of 36 on all runs), bare 16 of 36.
- Claude: brain 36 of 36, bare 15 of 36.
- Bare stayed under the "too easy" bound of 18 for the first time.
- Six plants were never named by bare on either runtime: BRAIN_ENV_UNSET, PRINT_CAP, SINK_TEMP, PGREP_RELATIVE, PLACEHOLDER_NAME and LEDGER_NOTE.
- Decoys were 18 of 18 for every arm; no arm took a look-alike scar. Controls were 18 of 18, except bare Codex at 17.

What I learned:
- The writer of a test cannot find the clues in their own items. The second reader caught 11 of 12, and even so 4 plants stayed guessable from what was left: a "separate check caught all 5" means a stale copy, and server ok logs beside cold fallbacks mean a client timeout. My rewrites made two more guessable, because a log that only says "paraphrases miss" gives away "semantic lane off".
- The brain arms are at the ceiling: 108 of 108 plants on Claude across DIAG1 to DIAG3. This kind of round can no longer separate better brains from worse ones. Next time, use plants the brain holds only weakly (a memory that names the symptom but not the fix, or two that must be joined), cut the budget below what brain Codex spends (19 to 20 commands), and have the reader recheck the rewrites.
- Every plant is a memory the brain has, so the round measures finding and applying the right memory from a reworded symptom. It does not measure diagnosing failures that are new.
- One Codex brain run went void on a false positive. The deny rule matched "h3models" inside the run's own verdicts write; the item logs name ~/h3models. The live audit should skip the arm's verdicts text.

Status: verified. The scores were recounted a second way, from the marks, runmaps and key without grade.py, and they match. The remote tree was read back over GraphQL: 26 files plus 39 in runs/. Follows [[diag2_brain_36_bare_21_20_no_clue_plants_decoys_all_right_2026_11_08]] and [[diag1_brain_36_bare_24_27_scar_causes_no_log_clue_too_easy_2026_11_08]]. Plants bare never got: [[pgrep_full_path_missed_relative_run_clips_two_loops_one_beat_2026_11_07]], [[recall_harness_brain_env_unset_log_flag_1721_test_rows_in_live_log_2026_11_06]], [[w08_open_list_was_first_60_of_108_print_cap_hid_48_d10_items_2026_11_08]], [[guarded_test_sink_kept_every_temp_file_52720_files_1p27gb_2026_11_07]], [[mac_mirror_pushes_went_to_one_path_named_name_23_of_23_placeholder_2026_11_06]] and [[ledger_note_naming_a_live_reflex_id_marks_entry_covered_2026_11_08]]. The clue check's own stall is [[codex_exec_background_hangs_on_open_stdin_pipe_dev_null_fixes_2026_11_08]].


---
name: diag12_diag5_items_burned_grep_reads_result_memories_3_of_6_void_2026_11_08
description: "Can DIAG5's planted-cause items still test an arm that greps the memory folder? No (DIAG12): 3 of 6 Codex runs read DIAG result memories naming the plants and were voided; grep 33 vs mixed3 30 pooled, a lean only"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T16:33:13+04:00
  status: verified
  evidence: "the private brain repository 12_cognitive_architecture/brain_improvement/DIAG12_20261108 5db446712d"
---

Can DIAG5's planted-cause items still be used for an arm that may grep or read the memory folder? No (8 Nov, DIAG12): 3 of 6 Codex runs (2 grep, 1 mixed) printed lines of the DIAG result memories during a recursive grep and carried plant labels and phrases only those memories hold, so the leak check voided them. The command audit cannot see this; only the output leak check caught it.

About a dozen result memories written since DIAG5 name the plants and their mechanisms. Any arm with file access can now find the key by grepping symptom words. Recall-only arms are still clean, because the deny list covers those slugs.

On the 3 valid runs the comparison barely moved. Pooled and scaled to 3 runs, grep 33.0 (4 runs) against mixed3 30.0 (5 runs) on Codex. That gap of 3 sits at the pre-registered bar, inside a 2 SD band of about 3.2 ([[diag_regrade_drift_0_of_57_with_written_rulings_run_spread_sd_2_2026_11_08]]): a lean toward grep, not settled.

How to apply: before a file-reading arm runs on old items, run leakcheck on a dry grep of the symptoms, or give the arm a copy of the memory folder without the test's result memories. Better, write new items. Do not reuse DIAG5's items for grep or mixed arms.

Files: the private repository, 12_cognitive_architecture/brain_improvement/DIAG12_20261108 (prereg 17574f282c, results 5db446712d). Related: [[diag11_each_cap_24_claude_still_asks_15_codex_30_claude_29_2026_11_08]], [[blind_test_key_leaks_via_verify_gate_turns_and_session_trees_2026_11_08]] (the same kind of leak through another folder).

Check (16:3x): DIAG10 and DIAG11 Codex mixed runs did see result-memory slugs (6 of 12 Codex runs, 1 to 5 slugs each), but only as file names in rg --files listings; their content markers were clean, so those runs stand. The names carry scores, not plant labels or mechanisms. The leak needs a content read, which a recursive grep over symptom words gives.

Tool (16:4x): ~/.claude/compute/keys_private/leak_shingles.py <runs dir> flags a transcript holding any 8-word run of the DIAG/RECALL6/OPSAUDIT result memories (7,413 shingles, 20 memories). On DIAG12 it flags the 3 voided runs (125 to 283 shingles) and grep Dr1 (14, OPSAUDIT3's summary line, another test, so Dr1 stays valid); DIAG11 6 of 6 clean. Copy in the DIAG12 folder, d9a9e26c5b.

Audit (16:4x): leak_shingles.py over DIAG7 (12 runs), DIAG8, DIAG9 and DIAG10 (6 each): 30 of 30 clean, so the earlier baselines (grep 32 on Codex among them) stand; the content leak first appears in DIAG12.

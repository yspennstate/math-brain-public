---
name: diag23_hashed_names_cost_grep_nothing_claude_26_28_codex_42_41_of_72_2026_11_09
description: "[VERIFIED] None of it (DIAG23): hashing every memory file name left grep flat, Claude 26 -> 28, Codex 42 -> 41 of 72 (bar 9); grep scores from content, not names"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T08:15:01+04:00
  status: provisional
  evidence: "brain-repo 12_cognitive_architecture/brain_improvement/DIAG23_20261109 4d94bdd0f0"
---

None of it (DIAG23, 9 Nov 2026, a second machine). Grep over a copy of the memory folder where every file name is a hash, the frontmatter name line is gone and MEMORY.md is left out scored the same as grep over the normal copy: Claude 26 with names, 28 without; Codex 42 and 41 (plant points of 72, three runs a cell, bar 9). Items higher / lower / tied: Claude 2/2/8, Codex 4/5/3. Controls 18/18 in all four cells.

The prediction was half wrong. It said Claude would not move (right, -2) and Codex would lose at least 9 because its grep runs start from the list of names (wrong, +1). Codex lists names first but gets its points from the searches inside files that follow.

Validity: 12 of 12 runs valid, leak check clean on all (tested first on planted strings), marks hashed 07:57 before unblinding, mark sums equal the scored totals (Codex 83, Claude 54). The plain grep arm repeats DIAG22 on the same items (Claude 23 then 26, Codex 42 then 42), so the arm is stable to within 3.

What it means for brain vs grep: the brain arm's lead over grep for Claude (+13 in DIAG21, +14 in DIAG22) cannot be put down to grep being helped or handicapped by the file names. Whatever recall adds, it adds over content search.

Results and rows: brain-repo 12_cognitive_architecture/brain_improvement/DIAG23_20261109 (4d94bdd0f0; PREREG 0a84794a0a). The hashed copy was deleted after the run; the hash map stays private.

Related: [[diag22_grep_name_listing_not_claudes_gap_brain_beats_grepls_10_and_19_2026_11_09]] (telling grep to pick files by name cut Codex 42 to 30; this run takes names away and nothing changes), [[diag21_brain_48q_beats_grep_claude_13_codex_ties_1_of_72_2026_11_09]] (the brain-vs-grep result this checks), [[test_deny_list_must_use_filed_slug_not_planned_prefix_2026_11_09]] (harness gap found while building this run's successor).


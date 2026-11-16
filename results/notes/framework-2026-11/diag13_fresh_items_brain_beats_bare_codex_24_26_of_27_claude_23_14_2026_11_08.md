---
name: diag13_fresh_items_brain_beats_bare_codex_24_26_of_27_claude_23_14_2026_11_08
description: "Does the brain beat no brain on fresh unnamed items? Yes (DIAG13): plants of 27 Codex bare 0, recall 24, grep 26; Claude bare 4, recall 23, grep 14; decoys 16-18 of 18; UNREG_PIECE missed by recall"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T17:37:09+04:00
  status: verified
  evidence: "the private brain repository 12_cognitive_architecture/brain_improvement/DIAG13_20261108 commits 1447feaa7c..625a0efd9d"
---

Does the brain still beat no brain on fresh items that no result memory names? Yes, by far, on both runtimes (DIAG13, 8 Nov 2026).

There were 9 plants (drawn at random from 788 unused scar memories; the clue check dropped 3 of 12), 6 decoys and 6 controls. Each arm ran 3 times on full store brain-graph-full-2026-11-07 (16,811,666 edges), judged blind by line id. Plants right of 27:
- Codex gpt-6.1-sol high: bare 0, each (recall only) 24, grep (memory folder only) 26.
- Claude opus-5-5 high: bare 4, each 23, grep 14.
Every brain arm clears the pre-registered bar of +4. Decoys were 16 to 18 of 18 for every arm (no over-reach), and controls 15 to 18. No plant was got by bare and missed by a brain arm. All 18 runs were valid. grep_codex_Dr2 read other tests' result memories but scored 8, against 9 for each of the other two runs, so the leak did not help.

What it settles: DIAG12's worry was that the brain's lead on DIAG5 items came from result memories naming the plants. On fresh items the lead stays, so it comes from the scar memories themselves.

What carried over from DIAG7/8: grep is strong on Codex and weak on Claude (14, with one run of 875 s that got 2), while recall is strong on both. Claude's each arm used only 2 to 3 of its 5 recalls; Codex used all 5.

Open: UNREG_PIECE (a borrowed piece not in the classical registry) never came up through recall on either runtime (0 of 6); only Codex grep got it (2 of 3). The query wording an agent writes from that symptom ("audio step rc=1, first run") does not reach the registry scar. That is a recall gap worth a lead line.

Caveat: this memory and the README name all 9 plants and the causes, so the items are burned for any later file-reading arm. The next test needs a new draw.

Rows: 12_cognitive_architecture/brain_improvement/DIAG13_20261108 (README.md, compare13.txt, judged sheets, runs). Scores were counted twice, by compare13.py and by a direct recount from the judged files, and both agree.

Related: [[diag12_diag5_items_burned_grep_reads_result_memories_3_of_6_void_2026_11_08]] - DIAG12 found the old items burned; this reruns the question on fresh ones. [[diag7_grep_32_recall_16_codex_17_15_agent_11_08]] - same grep-strong-on-Codex, weak-on-Claude split.

Follow-up (8 Nov 17:41): the 6 recall runs' audio queries returned 98 media memories and never the UNREG_PIECE scar (a_music_gate_refusal_on_an_unregistered_piece_register_it_dont_swap_2026_10_20). I appended a symptom line to it. Replaying the same 10 queries cold (BRAIN_RECALL_SERVER=0), it now ranks 1 to 4 on all 10. The line borrows the item's wording, so this is fitted to these queries and does not show general reach. Scar: brain.py recall has no --top flag; '--top 20' is folded into the query text.

---
name: diag5_capped_recall_brain_20_17_bare_0_2026_11_08
description: "Does the brain lead with recall capped at 3 one-wording calls, clues read out twice? Yes (8 Nov, DIAG5): brain 20 and 17 of 36, bare 0 of 36, no decoy taken; but 5 of 6 brain runs void (budget wording, audit false positives)"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T14:49:36+04:00
  status: verified
  evidence: "brain_improvement/DIAG5_20261108, commits 87abd995c1 19e2b1c264 86f3fd2dc2 87b13edd6e"
---

Does the brain still lead when recall is capped at 3 calls of one wording, on 12 scars no earlier round used and with the clues read out twice? Yes, and this round is the first off the ceiling: brain named 20 of 36 causes (Codex) and 17 of 36 (Claude) on all runs, bare 0 of 36 on both. Decoys and controls were right on every run of every arm (18 of 18 each), so the brain took no look-alike. Under the pre-registered rules only one brain run is valid (brain_codex_Dr2, 7 of 12 against bare's 0 a run, +21 scaled to three runs against a bar of +6). Claude cannot be scored on the rules as written.

Why five of six brain runs are void, and what to fix before DIAG6:
- Brain Claude made 14, 19 and 19 tool calls against a budget of "5 shell commands". Only 3, 6 and 4 were Bash; the rest were Grep, Read and Glob on the memory folder. The harness counts every tool call. State the budget the way it is counted, or count it the way it is stated.
- The recall-rule loop detector `\b(for|while|xargs|parallel)\b` fires on the English words "for" and "while" inside a quoted recall wording. Match loops only outside quotes, and control it on such wordings.
- The deny pattern for ~/.claude/projects fires on a script that builds the allowed memory path in pieces (projects / slug / memory). The bare word "compaction" fires on a line that skips compaction_ files. Both are false positives and both belong in control.py.
- A plant label that is also a real identifier (COMPACT_WINDOW, inside CLAUDE_CODE_AUTO_COMPACT_WINDOW) is a useless leak marker: it fires on the plant's own scar memory, which a brain arm is supposed to read.

What the arms did with the cap: brain Codex called brain.py 0 or 1 times a run and spent the rest of its 5 commands reading brain.py's source to find the memory folder, then python scripts grepping memory files with long regexes. Brain Claude made 1 to 3 recall calls, then grepped and read files. Capping recall did not cap search. It moved search to the files.

Rank does not predict difficulty. COPIED_SIDECAR and CTIME_REPLACE rank 1 and 2 under plain recall of the item's full text, yet all 6 brain runs missed both, naming a nearby cause (the refresh or the copy unbinds the sidecar) instead of the mechanism. The weak stratum held only 2 plants (Codex 0.0, Claude 1.0 brain-minus-bare per plant), so rule 3 was reported, not tested.

Evidence: the private repository, 12_cognitive_architecture/brain_improvement/DIAG5_20261108 (prereg and hashes 87abd995c1 before any arm, addendum 19e2b1c264 at 14:36 while the arms ran and before any output was read, results 86f3fd2dc2 + 87b13edd6e). Store brain-graph-full-2026-11-07, 16,811,666 edges, sidecar 242,841 link rows. Blind judged; recount.py recount matches grade.py. Builds on [[diag4_budget5_brain_36_33_bare_14_15_2026_11_08]] and [[diag3_brain_36_bare_16_15_stripped_clues_at_ceiling_2026_11_08]]; leak paths in [[blind_test_key_leaks_via_verify_gate_turns_and_session_trees_2026_11_08]].


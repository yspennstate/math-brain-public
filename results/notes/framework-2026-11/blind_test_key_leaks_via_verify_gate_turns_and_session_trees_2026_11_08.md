---
name: blind_test_key_leaks_via_verify_gate_turns_and_session_trees_2026_11_08
description: "[VERIFIED] Scar (8 Nov): a blind test built in a live session leaks its key through ~/.claude/dreaming/.verify_gate_turns (full command text of every turn), the Codex home and session trees; deny them and grep run transcripts for the key folder path"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T14:05:47+04:00
  status: verified
  evidence: "DIAG4 build 8 Nov 13:59-14:04; diag4/run_audit.py, control.py 84/84, leakcheck.py"
---

Can a brain test built in this session keep its key away from the brain arms by denying the key folder? Not by command rules alone. ~/.claude/dreaming/.verify_gate_turns, written by verify_gate.py, keeps each session turn's events with the full text of the commands typed (1,061 files, 35 MB on 8 Nov 14:05). A heredoc that writes or patches the items lands there word for word. Brain arms may read ~/.claude/dreaming, and a plain `rg -l <word> ~/.claude/dreaming` names no denied path, so the live audit passes it.

Measured on this worker machine, 8 Nov 13:59 to 14:04, while building DIAG4:
- A string that only DIAG3's key and my patch heredoc held ("brain-test-store") was searched for in ~/.claude/dreaming, ~/.claude/brain_graph, ~/brain, the memory folder, ~/.claude/mail and the mesh. The one hit was .verify_gate_turns/029c4d3d8928b49f6001.json, which held the whole patch command.
- The deny rules also passed `rg -l <word> ~/.codex-acc2` (the clue checker's session, with every cause, is under it), `rg -l <word> ~/.claude/projects` (session transcripts) and `rg -l <word> ~/.claude/brain_graph` (compaction texts).
- DIAG3 stayed valid. No brain run searched those trees: their commands were scanned, and their transcripts hold none of the leak markers (the private key folder name, the clue-check file names, the earlier results' folder names and body phrases).

How to apply, for any blind test built inside a live session:
1. Deny verify_gate_turns, a bare ~/.codex* root, ~/.claude/projects outside /memory, and the ~/.claude/brain_graph root (DIAG4's run_audit.py has the patterns, and its control.py checks them).
2. Check what the arms saw, not only what they typed. Grep each run transcript, which holds the tools' output, for text only a denied file holds. the private key folder's path is a good tripwire, since nearly every leak source names it. DIAG4's leakcheck.py does this, and it was controlled on DIAG3's 12 runs (only their own folder fired) and on a planted leak line.
3. The compaction anchors in the memory folder carried no item names this time. The full summaries under brain_graph/compactions will after the next compaction.

The same family as [[test_built_before_own_compaction_leaks_items_via_anchor_v3e_void_2026_11_07]] (the builder's own session state becomes a leak) and [[codex_blind_brief_override_in_first_message_hooks_off_0_outside_paths_2026_11_08]]. Found while building on [[diag3_brain_36_bare_16_15_stripped_clues_at_ceiling_2026_11_08]].

Status: verified (the search above and the control runs of the deny rules and leakcheck.py).


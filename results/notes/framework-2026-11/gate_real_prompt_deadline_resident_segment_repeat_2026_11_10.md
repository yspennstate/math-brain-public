---
name: gate_real_prompt_deadline_resident_segment_repeat_2026_11_10
description: "Regression gate recall_real_prompts rc 124 / no parsed row, or a recall bank whose lists change on a second run within the hour? Evaluator now has --resident and --deadline-s (357 s, 32/139 = 0.230, partial sample recorded); a bank run from an agent's shell is damped by recall's 60-min past-session segment repeat rule and damps that agent's own recalls - unset the session id."
metadata:
  type: project
  created: 2026-11-10
  created_at: 2026-11-10T09:20:02+02:00
  status: verified
  evidence: "installed evaluator run as the gate calls it 10 Nov 09:09-09:15 rc 0; gate block test with deadline 30; 12 of 12 identical lists with session ids unset vs 5 of 30 with them set"
---

The nightly regression gate's real-prompt recall instrument (`recall_real_prompts` in state/regression_gate.jsonl)
now finishes with room and can no longer go dark for a month without a parsed row. Follows
[[long_pasted_prompt_recall_168s_two_quadratic_paths_blinded_gate_2026_11_10]] (why 28 of 32 runs died at the cap).

**What changed (installed 10 Nov 09:07, both files on GitHub under 12_cognitive_architecture/dreaming).**
- eval_recall_real_prompts.py (sha256 8217980c1f94a164, backup .bak_20261110_0907, commit dbf11d82):
  `--resident` asks through brain_recall_server.Brain() in process (memoized state, the lists recall prints);
  `--deadline-s S` shuffles the episodes with a fixed seed (`--order-seed`, 20260914), stops asking once S seconds
  are spent and at least 20 were asked, and prints the same summary line plus `partial: asked a of b`;
  `--check-resident N` / `--check-cli N` compare the paths on the first N episodes.
- math_brain_regression_gate.py (e43f7a70b7db6e95, backup .bak_20261110_0907, commit d09a6b87): calls the evaluator
  with `--resident --deadline-s 700` (REAL_PROMPTS_DEADLINE_S) under the same 900 s cap, records `path` and, on a cut
  night, `partial: {asked, of, deadline_s}`, and prints a real-prompt line in REGRESSION_GATE.md.

**Measured.** As the gate calls it: 139 episodes, hit@8 32/139 = 0.230, MRR 0.1237, 357 s wall, rc 0 (bare path 757 s,
same 32/139). With a 30 s deadline: 20 of 139 asked, partial line printed, and the gate's own block (its source
lines, its run()) records `{'hit8': 0.25, 'n': 20, 'path': 'resident', 'partial': {'asked': 20, 'of': 139}}` with
no error. A full gate run on the new files has not happened yet: the 04:10 task on 11 Nov is the first.

**A side effect found on the way, and it reaches beyond this bank.** recall() gives display slot 5 to a past-session
transcript segment and holds back a segment that the caller's session (CLAUDE_CODE_SESSION_ID / CODEX_THREAD_ID) was
shown in the last 60 minutes; it logs each showing to ~/.claude/brain_graph/logs/segment_slot.jsonl. A test bank run
from an agent's shell therefore (a) gets different lists on a second pass within the hour, and (b) writes rows under
that agent's session id, which damps the agent's own real recalls for an hour. Seen as 5 of 30 lists identical
between the bare and resident paths from my shell; with the session ids unset, 12 of 12. The evaluator now drops both
ids at the top of main() and points BRAIN_SEGMENT_SLOT_LOG at segment_slot_eval.jsonl. Other banks that call
brain.recall() in process were not checked: a bank whose number moves between two runs an hour apart, from the same
shell, should be read with this in mind.

**The one remaining difference (19 of 20 identical) is not a path difference:** between the two passes the index
merged fresh memories (3, then 7), and a new checklist node entered one list. The bare path asked again gave the
resident list. For an exact parity check hold the index: `python bm25.py freeze <min> <why>`, then `unfreeze`.

**Still open.** hit@8 fell from 0.291 (19 Oct) to 0.230 (3 Nov) while the instrument was dark; lead
[[compaction_nodes_crowd_bm25_top8_2026_11_09]]. The number is recorded, not floored: once a few nights have parsed,
set a floor.

What would change this: a night where the row has rc 124 again (the evaluator is slower than 700 s plus one call, or
the resident state failed to build), or a parsed row whose `partial` shows fewer than about 100 asked (the box was
too busy for the number to mean much).


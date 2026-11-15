---
name: read_time_recognition_hook_live_lesson_on_read_2026_11_11
description: "Agent never recalls a lesson mid-task? Since 11 Nov a PostToolUse hook (recognize_on_read.py) names a lesson/scar when a Read/Bash output resembles it: 23/23 hunts, 2.1 false fires/100, ~0.1 s in-process"
metadata:
  type: project
  created: 2026-11-11
  created_at: 2026-11-11T04:51:40+02:00
  status: provisional
  evidence: ""
---

Since 11 Nov 2026 (~04:5x local) every Claude session runs ~/.claude/dreaming/recognize_on_read.py after each Read, Bash
and PowerShell call (PostToolUse, Read and Bash|PowerShell blocks of hook_dispatch_list.json; backup
hook_dispatch_list.json.bak_ror_20261111_*). It scores the first 4000 chars of the output against the memories with
BM25 and names one lesson or scar when the text looks like a place we have been. Codex does not have it yet.

Why: in the harder grand hunts the brain arm filed lessons after every hunt, but made no recall call after the first
hunt, and the lesson reached it in one hunt of four. An agent does not ask the brain mid-task; what it reads has to
trigger the recall.

The rule (env knobs ROR_*):
- query: the 32 rarest words of the output, rarest first, stopping once their summed df passes 20000 (always keep 4);
- fire only if s1 >= 30, s1/s10 >= 1.5, s1/s2 >= 1.3, and the top memory is a lesson (`lesson: true` under
  metadata), type feedback, or a slug that says mistake/scar/wrong/trap/never/bug;
- once per memory per session, at least 5 calls between fires;
- grand_hunt_* memories other than grand_hunt_archive_* and compaction_* are never named (they would leak the scoring).
State and a per-call log (ms, fire) in ~/.claude/dreaming/recognize_on_read/fires.jsonl.

Calibration (23 hunt transcripts, 6 owner sessions, 1323 outputs; scripts in grand_hunt/ on GitHub, commit 0497f926):
| posting budget | hunts caught (of 23) | false fires /100 owner outputs | s per output |
|---|---|---|---|
| none (K=32) | 23 | 2.1 | 0.35 |
| 20000 (chosen) | 23 | 2.1 | 0.20 |
| 10000 | 19 (20 at s1>=15) | 1.8 | 0.14 |
| 5000 | 19 | 1.8 | 0.07 |
End to end (test_ror.py 3 60, separate process): lesson fired in 3 of 3 hunts, 3.3 false fires per 100. Inside the
dispatcher (in-process) a call costs 34-106 ms, live 7-436 ms.

What would change it: arm A of seeds 15-17 rerun with the hook on should show the lesson reaching the agent and
fewer first-scar falls. If falls do not drop, the hook delivers text the agent still does not use, and the next lever
is the wording of the note, not the trigger. Watch fires.jsonl for false fires on owner sessions; raise ROR_S1 or
ROR_GAP if they pass about 3 per 100.

To turn it off: remove the two recognize_on_read entries from hook_dispatch_list.json (never edit hook_dispatch.py).
Memories need `lesson: true` under metadata to count as lessons: file them with `brain.py remember ... --lesson` (since 11 Nov 05:2x; backup brain.py.bak_lesson_20261111).

Related: [[grand_hunt_hh1_brain_equals_notes_on_scars_slower_2026_11_11]],
[[grand_hunt_checker_scored_the_best_carry_zero_and_a_warning_as_obeying_2026_11_11]].


Spans-call probe (11 Nov 07:5x, an agent): every spans.py call in the HH transcripts (31) scored as command plus output with no length floor. The rounding lesson ranks in the top 12 on none of them. The calls chain the tool with station and place names, the pruned query keeps those rarest words, and where "spans" survives, code words (import, argv, print, decimal) pull other memories ahead. Lowering the 40-character floor would not help; a lesson is recognised only when it shares rare words with what the agent reads (copy and register do, rounding does not). Next: reword the rounding lesson with the words its stations show (spans.py, marks, ledger reading, UNITS.md) and replay before any hook change.

---
name: claude_read_time_hook_question_line_drowned_and_hunt_design_leak_2026_11_11
description: "[PROVISIONAL] Claude read-time hook silent on a trap question? It scores the whole output's rarest words, so one question line under a file listing is drowned (seed 30 st17: lesson 16.2, rank 14). ROR_QTIME=1 scores prose question lines alone (QMIN 15, lead 1.3 / 1.1 for lesson:true): old style 7/8, owner +1.5/100. In hunt folders hunt-design memories are now never named (one leaked at seed 30)."
metadata:
  type: project
  created: 2026-11-11
  created_at: 2026-11-11T18:58:37+02:00
  status: provisional
  evidence: ""
---

Live hook ~/.claude/dreaming/recognize_on_read.py sha 015ad4f1 (pushed 0c714f5d; patch and tests in grand_hunt/claude_read_time/, backup recognize_on_read.py.bak_qtime_20261111). Question time is OFF by default; set ROR_QTIME=1 in a hunt arm launcher. Replay on ten Opus brain-arm sessions (seeds 24-30): old-style lesson named on 7 of 8 first postings, no scar station names a wrong memory, ordinary stations name only the other archive lessons. Owner sessions (20, 1,195 outputs): +1.5 notes per 100 outputs against 2.7 from the existing rule. Filed-copy traps are not caught at question time (the question never mentions memos) but ARE caught when the memo is read: seed 30 station 7, the existing whole-output rule named the filed-copy lesson at call 25 (s1 37.7), one call before the answer (copyread.py). QMIN 18 scored better on this bank but sits just under the one lesson's 19.1, so it would be fitted to one card. Hunt exclusion: ROR_HUNT=1 or a cwd matching grand_hunt|/HH_|/HX_ drops memories whose head mentions grand hunts, arms or scar stations; outside hunts verdicts are unchanged (38 of 38 station outputs equal with QTIME off). What would change it: an Opus seed run with ROR_QTIME=1 that still falls at an old-style station. Related: [[codex_lesson_at_read_time_beats_lesson_in_folder_old_style_2026_11_11]] [[scar_test_bites_only_when_nothing_in_sight_invites_a_check_2026_11_11]]

Builds on [[read_time_recognition_hook_live_lesson_on_read_2026_11_11]] (the whole-output rule this adds to).

Seed 31 Opus (11 Nov 19:3x, HARDER_HUNT.md f0fbd5d7): with ROR_QTIME=1 the brain arm answered the first watch (7) and first old-style (15) stations right where bare fell at both, but question time named neither lesson (its fires were three other archive lessons). The agent found both itself: the watch memory line was among the newest in MEMORY.md, and it grepped the memory folder before 15. So this run does not test question time; a lesson filed the same day is easy to see in the index. Session 2 never ran (weekly limit, resets 18 Nov).

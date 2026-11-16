---
name: multi3_codex_two_session_repair_brain_30_none_0_notes_1_budget_overrun_2026_11_09
description: "[VERIFIED pilot] Yes vs no memory (MULTI3): Codex 2-session repair, 2 h gap, 8 calls/8 KB: BRAIN 30, NONE 0, NOTES 1 of 30 (p 2^-30 vs NONE); NOTES lost to printing a 120 KB file, not retrieval"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T13:21:49+04:00
  status: verified
  evidence: "MULTI3 pilot01 grade 9 Nov 10:20 (frozen grader); RESULT.md"
---

Does the brain carry what a Codex agent found in one session into a repair two hours later, against no memory and against one shared notes file? Yes against no memory; the notes comparison is not a retrieval result (MULTI3 pilot01, graded 9 Nov 2026 10:20, gpt-6.1-sol high in every arm, key read only by the frozen grader).

Session 1: 183 diagnoses per arm, all valid. Gap of at least 7,200 s. Session 2: repairs under 8 command calls and 8,192 output bytes. 30 ordinary tasks plus t31, a control whose note was deleted.

Passed of 30: BRAIN 30, NONE 0 (all 31 NONE repairs valid, none right; a key-blind guess is 1 in 5 per task), NOTES 1. Paired BRAIN vs NONE: BRAIN only 30, NONE only 0, sign test p = 2^-30. Deleted-note gate passed: no arm recovered t31. BRAIN t31 overran the byte budget (9,634 bytes) and counts as a fail.

Why NOTES lost: 30 of 31 NOTES repairs were invalid because the agent's first command printed the whole shared NOTES.md (about 120 KB) against the 8,192-byte budget; its one valid repair passed. So MULTI3 shows retention through the brain, not that the brain retrieves better than a file. MULTI4 (launched 11:06) repeats it with NOTES told it may use grep, head, sed -n and wc. The Claude runtime was not run (Claude test arms need the Keychain login, an owner decision).

Files: the private repository: 12_cognitive_architecture/brain_improvement/multi3_codex_pilot01_2026_11_09 ( grade.json has per-row booleans, no key values).


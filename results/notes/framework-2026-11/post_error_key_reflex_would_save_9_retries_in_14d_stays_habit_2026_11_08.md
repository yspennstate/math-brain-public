---
name: post_error_key_reflex_would_save_9_retries_in_14d_stays_habit_2026_11_08
description: "Would a reflex that fires after a guessed JSON key throws pay? [VERIFIED] No: 102 shape errors in 14 days, and only 9 next tries guessed wrong again (about 9 saved calls a fortnight); the guessed-key lesson stays a habit"
metadata:
  type: feedback
  created: 2026-11-08
  created_at: 2026-11-08T02:35:33+04:00
  status: verified
  evidence: "guessed_key_after_error_scan 8 Nov 02:3x: 139,380 Bash, 11,352 json reads, 102 shape errors, next read again 9, lists keys 23; hand read 20+24 samples"
---

Two of the six corrections in MISTAKES.md that still have no reflex (10 Aug and 6 Nov) teach one lesson: list a record's keys before reading a field from a tool you did not write. On 6 Nov an agent measured a trigger that fires before the call. It matched 304 of 116,647 Bash inputs, mostly correct `.get` reads, and was too loud.

The other place to fire is after the error. Measured 8 Nov over 14 days of Mac transcripts (guessed_key_after_error_scan_2026_11_08.py):
- 139,380 Bash calls, 11,352 of them `python -c` JSON reads.
- Shape errors (KeyError, IndexError, AttributeError or TypeError on a dict, list, None or str): 102, which is 0.90% of the reads. In a hand read of 20 samples nearly all were guessed keys or shapes, so a post-error trigger would be precise.
- JSONDecodeError: 100 more, kept apart. Of 14 read, 10 were empty or absent input (a job still writing, a node down, a wrong path) and 4 assumed a tool prints JSON. That is a different lesson.
- What a reflex could change is the next try. After a shape error, the session's next JSON read threw a shape error again 9 times of 102. It listed the keys 23 times.

So the most a post-error reflex could save is about 9 retries in two weeks across every agent on the second machine, at one tool call each. Not compiled: it stays a habit, as 686ee39a decided, and the generic post-error note already fires on the traceback. This agent slipped the same way twice on 8 Nov (a guessed mesh claims schema and a guessed file path), which fits: the error is cheap and the next try usually lands.

How to apply: before building a reflex for a slip, count what the slip costs after the error, not just how often its shape appears. A slip whose first failure teaches the fix needs no guard.

Related: [[foresight_unguarded_corrections]] - the "unguarded -> 6 corrections" line in the wake brief counts these rows.


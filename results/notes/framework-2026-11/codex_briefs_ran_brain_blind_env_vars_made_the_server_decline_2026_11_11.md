---
name: codex_briefs_ran_brain_blind_env_vars_made_the_server_decline_2026_11_11
description: "[VERIFIED] Codex workers barely use the brain? 8-11 Nov: 594 Codex sessions, 8 brain/math briefs, 4 recalled (8 math_recall runs, 0 brain.py). OPEN2's wrapper set MATH_RECALL_* env vars, the resident server declined, cold path 208 s then MemoryError under the 1 GB cap. A plain served call is 34 MB client peak. Call math_recall.py bare."
metadata:
  type: project
  created: 2026-11-11
  created_at: 2026-11-11T00:11:57+02:00
  status: provisional
  evidence: ""
---

Measured 11 Nov 00:0x-00:1x laptop, an agent (recall-10x, T-20261110-092), read-only over every ~/.codex* home's rollouts since 8 Nov (scanner: a function_call whose command starts python on math_recall.py / brain.py recall / problem_recall.py).

Counts: 594 Codex sessions, 584 picture workers, 8 brain/math briefs (codex_local_1108/briefs: I0012R, I0012R2, I0012R3, G0013, OPEN2, OPEN3, GHA, GHB). 4 of the 8 ran math_recall (8 runs); none ran brain.py recall; the four newest (OPEN2/OPEN3/GHA/GHB, 10 Nov) ran no recall the scanner could see (OPEN2 ran it through its own wrapper, below). GHA/GHB/I0012R*/G0013 briefs carry no recall line; OPEN2/OPEN3 say 'Use the math brain first'. Most briefs run NOHOOKS, so they also get no per-turn brain context: in practice these workers run brain-blind.

Why OPEN2's recall failed (its LOG.md line 20; recall_cold_calls.jsonl 2026-11-10T03:35:09 'code or environment differs', cold_s 208): the brief says stay under 1 GB and never edit live brain files, so the worker wrapped math_recall in code/recall.py that set MATH_RECALL_SERVER_DISABLE=1, a private MATH_RECALL_CACHE_DIR and other MATH*_ variables. The server keys on the environment, declined, the client went cold (loading the 348 MB prepared state itself) and hit MemoryError under the 900 MiB job cap; the worker fell back to a 24-node SQL slice.

The served path is cheap for the caller: two plain calls at 00:1x peaked at 34 MB client RSS, server 13.6-15.6 s per request, 17-59 s wall on the loaded laptop, and the first card was the right one (Diaconis's perfect-matching question, OPEN2's own problem).

How to apply: a Codex (or any sandboxed) worker calls python ~/.claude/dreaming/math_recall.py bare, no MATH_RECALL_* / MATHBRAIN_* / MATH_BRAIN_* variables, no wrapper; reading is allowed under a no-edit rule. A brief that wants brain use says so in its first steps and asks for each recall and its first card id in LOG.md. Sent to the fleet owner an agent 00:1x.

Scar from the measurement itself: a Popen with stdout=PIPE polled until exit deadlocks once the child prints more than the pipe buffer (math_recall prints ~19 kB); my first two test calls 'hung' 300 s while the server log showed them answered in 0.9-6.6 s. Read the server's timing log before calling a server slow; send big child output to a file.

What would change it: a fleet brief run after the fix that still makes no recall, or a served call that exceeds the cap.
Related: [[math_recall_what_works_agents_2026_10_15]] [[recall_lean_first_pass_bounded_by_answer_rank_2026_11_10]]

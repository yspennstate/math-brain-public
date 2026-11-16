---
name: frontier_brief_crashed_on_list_evidence_t109_t127_2026_11_11
description: "frontier.py brief TypeError on T109 / T127? A worker wrote a route's evidence as a list; brief_text now joins it (11 Nov). All 64 staffed briefs render. Audit by rendering every row"
metadata:
  type: project
  created: 2026-11-11
  created_at: 2026-11-11T01:44:05+02:00
  status: verified
  evidence: "rendered all 64 staffed briefs with frontier.brief_text on 11 Nov 01:3x: 62 ok and 2 TypeError before the fix, 64 ok after; three frontier tests ALL PASS"
---

`frontier.py brief T109` and `brief T127` raised TypeError ("can only concatenate str (not list) to str") until 11 Nov 01:3x. A worker on each row (c15s2 on T109, w677 on T127) had written a dead route's "evidence" as a list of paths, and brief_text joined it to a string. Rule 1 of WORKER_RULES makes the brief a solver's first action, so a solver on those two rows got a traceback instead of the dossier and the dead routes.

Found by rendering every staffed row's brief while building the record / no-record kit: 62 of 64 rendered, 2 crashed.

Fix: brief_text now joins a list with "; " and passes a string through. After it all 64 briefs render; test_frontier_check_open, test_frontier_live_routes and test_frontier_check_settled pass.

Lesson for the next field a worker writes freely: a ledger line's type is whatever the worker chose, so a reader of ROUTES.jsonl formats with str() or checks the type. The quick audit is one loop that renders every row, not a test on one row. See [[guessed_field_slip_now_caught_by_the_felt_error_hook_2026_11_10]].


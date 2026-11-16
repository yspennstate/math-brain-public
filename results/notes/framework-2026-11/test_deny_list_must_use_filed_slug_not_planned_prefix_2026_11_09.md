---
name: test_deny_list_must_use_filed_slug_not_planned_prefix_2026_11_09
description: "[PROVISIONAL] No: a patch denied a result memory by a guessed prefix, the filed slug differed, and the control passed because it named the same guess; copy the real slug in and fail the control unpatched"
metadata:
  type: feedback
  created: 2026-11-09
  created_at: 2026-11-09T07:44:39+04:00
  status: provisional
  evidence: ""
---

No (9 Nov 2026, found while building the next run's harness): a test patch denied the previous run's result memory with a guessed prefix (the run name plus a word from the planned title), but the memory was filed under a different slug, so the deny matched nothing. The test's own control passed because its checks named the guessed prefix too, so they tested the pattern against itself.

No harm that time: those arms grepped a frozen snapshot taken before the memory existed, and no transcript mentions it (checked against all run logs). It would have mattered for a brain arm reading the live memory folder.

How to apply: after the result memory is filed, copy its real slug from the memory folder into the deny list and into the control's forbidden commands (brain.py node <real slug>, cat <memory dir>/<real slug>.md), then rerun the control on the unpatched copy and see it fail. The next harness does this: 127 checks, 0 wrong patched, 3 wrong unpatched.

Related: [[follow_up_test_harness_must_deny_prior_run_results_2026_11_09]]

Same shape as [[a_usage_gate_reads_the_account_its_old_streams_ran_on_2026_09_24]]: a check aimed by name at something that no longer carries that name passes by default.

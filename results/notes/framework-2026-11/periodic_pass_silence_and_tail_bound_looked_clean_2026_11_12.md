---
name: periodic_pass_silence_and_tail_bound_looked_clean_2026_11_12
description: "prompt-class ledger class_model zero output periodic pass dark tail read false ok"
metadata:
  type: feedback
  created: 2026-11-12
  created_at: 2026-11-12T15:11:36+02:00
  status: provisional
  evidence: ""
  lesson: true
---

What happened: The prompt-class pass went dark three times: 14-15 July, 8-11 September (353 prompts), and 8-12 November (3,401 prompts). The September correction requested an alarm, but none was built then. The first November alarm draft needed 2 dark days in view and saw only 1 through a 4 MB tail, so it printed ok. The installed 16 MB probe reported 2 completed dark days. Independent whole-file counts matched 197 rows for 9 Nov, 576 for 10 Nov and 1,578 for 11 Nov.

Why it happened: The absence of a product looked like a clean pass, and then a bounded observation was treated as complete coverage. Script presence and a task's promise did not show that class_model rows were produced.

**Why:** A monitor must distinguish no input, missing visibility, and input with no output.

**How to apply:** Count output against input per completed period in the existing wake, allow the usual run hour its grace period, label unseen periods unknown, and require the live dark case to trip plus an independent count; use the existing periodic_pass_output_needs_a_freshness_alarm reflex rather than duplicating it.

[[method_watch_a_periodic_pass_by_its_output_2026_11_12]]

Drafted by Codex worker W05 of the 12 Nov 04:43 order (H20_1112), screened and filed by an agent. Provisional: the worker read the source, nobody re-measured it.


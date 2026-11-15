---
name: math_repeat_memo_missed_stable_silences_2026_11_12
description: "math_sense repeated loop ticks recompute generic_only_match across compaction"
metadata:
  type: feedback
  created: 2026-11-12
  created_at: 2026-11-12T15:07:04+02:00
  status: provisional
  evidence: ""
  lesson: true
---

What happened: In three days, 717 full runs ended in two uncached silences, 688 repeated the same prompt within two hours and 595 crossed compaction. Replay answered 683/717 at 20 ms instead of a 1.4 s median for generic_only_match.

Why it happened: The earlier memo stored only two other verdicts and scoped them to one context, losing silences stable across compaction. The wider memo still depends on the shown-ids shard.

**Why:** Memo scope must follow the inputs that determine a verdict.

**How to apply:** Keep the two-hour guard on shard size and mtime, verify dial-off equivalence, and isolate helper tests in scratch HOME and SESSION_DIR with _repeat_ctx replaced. Live gain is still provisional.

[[math_hook_repeat_memo_keeps_generic_and_no_chosen_verdicts_2026_11_12]]

Drafted by Codex worker W04 of the 12 Nov 04:43 order (H20_1112), screened and filed by an agent. Provisional: the worker read the source, nobody re-measured it.


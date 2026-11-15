---
name: slow_probe_never_started_false_hung_2026_11_12
description: "slow_probe hung_producer zero handles means exited or never started suspended process"
metadata:
  type: feedback
  created: 2026-11-12
  created_at: 2026-11-12T15:36:50+02:00
  status: provisional
  evidence: ""
  lesson: true
---

What happened: From 11 Nov afternoon past midnight, PID 27804 generated hung-producer warnings although PUBLISH.log showed 15-minute publishing. At 12 Nov 00:14 it had one Wait/Suspended thread, 0 ms CPU, 0 handles, no modules and 1.2 MB working set. PID 57720 persisted for 22 cycles. The fix left the other 14 watched processes unchanged.

Why it happened: The byte-delta probe treated a never-started process as a worker. The first repair wrongly assumed zero handles meant exited; GetExitCodeProcess returned STILL_ACTIVE, and a held exited child was absent from Toolhelp. The measured thread state supported the never-started classification; the launcher failure itself was not traced.

**Why:** Process presence and zero output do not identify whether useful work ever began.

**How to apply:** Inspect thread state, CPU, handles and modules together, read later job logs, and test sleeping-live and deliberately suspended children before classifying or notifying anyone.

[[slow_probe_named_a_never_started_process_a_hung_producer_2026_11_12]]

Drafted by Codex worker W08 of the 12 Nov 04:43 order (H20_1112), screened and filed by an agent. Provisional: the worker read the source, nobody re-measured it.


---
name: rem_arm_order_ran_the_dream_on_old_models_2026_11_14
description: "Dream REM on Fable 5.1/Opus 5 though run_dream.ps1 says 5.2/5.5? rem_arm_order.py constants were stale and override the fixed order; fixed 14 Nov, selftest now compares"
metadata:
  type: project
  created: 2026-11-14
  created_at: 2026-11-14T22:45:28+02:00
  status: verified
  evidence: "logs/dream_2026111*.log: 13 'rem arms: order claude-fable-5-1[1m]' lines; rem_arm_order.py --selftest 22 pass, old ids fail the new check"
  lesson: true
---

Which model did the dream's REM pass run on, 10-14 Nov 2026? Fable 5.1 and Opus 5, not the 5.2 / 5.5 that run_dream.ps1's fixed order names. rem_arm_order.py (added 10 Nov) prints its own arm list, and run_dream.ps1 replaces the fixed order with it whenever the helper exits 0 - which it does even when the main-login probe times out. Its FABLE/OPUS constants were never moved when run_dream.ps1 went to 5.2/5.5, so 13 dream logs from 11-14 Nov show "rem arms: order claude-fable-5-1[1m], claude-opus-5[1m], ...".

Fixed 14 Nov 22:4x (an agent): constants now claude-fable-5-2[1m] / claude-opus-5-5[1m], and the selftest parses run_dream.ps1's `$models = @(...)` line and fails when the two differ (negative control: the old ids fail it). 22 checks pass.

**Why:** a helper that overrides a caller's default must take the default from the caller, or the two drift and the override silently wins.
**How to apply:** when you change model ids in run_dream.ps1, run `python -s rem_arm_order.py --selftest`; when you write any "order helper" that replaces a caller's list, test equality with the caller's list. Status: verified (log grep + selftest).


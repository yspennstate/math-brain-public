---
name: headless_resume_paid_the_wake_hook_for_twenty_minutes_2026_11_12
description: "[PROVISIONAL] Headless claude -p --resume sat 20 min with no model call? SessionStart wake_brain.ps1 runs first; on a loaded box it hangs and its taskkills hang too"
metadata:
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T20:23:33+02:00
  status: provisional
  evidence: ""
---

On 12 Nov 2026 a paper-audit reader resumed at 19:55 (claude -p --resume 4b43a6d6, pythonw launcher) made no model call until 20:17. Its children were wake_brain.ps1 -Part 1 and -Part 2 (SessionStart), started 19:57; the harness timed them out at 20:09-20:10 but the taskkill.exe processes it spawned also hung (commit 97 pct, RAM 1.3 GB free), so Part 2 lived to about 20:14 and the queued prompt was dequeued at 20:17. Symptom: transcript mtime frozen, claude.exe CPU near 5 s, REPORT untouched. Check: list the claude.exe children (Win32_Process ParentProcessId) before deciding a resumed reader is dead. Mitigation to try (not yet tested): launch headless readers with CLAUDE_WAKE_BUDGET set small (wake_brain.ps1 reads it at l.641). Status provisional: one case, the budget env not yet measured.

CORRECTION, same evening 21:08 (measured): the wake hook was not the main cause. The resumed reader (and a later fresh
reader with CLAUDE_WAKE_BUDGET=5) were launched BELOW_NORMAL (creationflags 0x4000) while every core was busy: each sat
at 0.5-0.8 s CPU over 7-12 minutes with no TCP connection. A tiny claude -p probe launched at normal priority answered in
30 s. Setting the stuck reader's PriorityClass to Normal gave it 2 s of CPU in 20 s and 4 established connections at once.
Rule: on a loaded box a BelowNormal headless claude can starve before its first model call; launch audit readers at
normal priority (keep CREATE_NO_WINDOW), or raise a starved one with (Get-Process -Id <pid>).PriorityClass='Normal'.
Related: [[a_max_thinking_agent_can_spend_its_whole_output_budget_before_writing_2026_09_23]].

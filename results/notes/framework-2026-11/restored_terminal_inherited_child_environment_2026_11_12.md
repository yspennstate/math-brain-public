---
name: restored_terminal_inherited_child_environment_2026_11_12
description: "Reopen a crashed Claude terminal without a zombie transcript or lost terminal colors"
metadata:
  type: feedback
  created: 2026-11-12
  created_at: 2026-11-12T16:26:17+02:00
  status: provisional
  evidence: ""
  lesson: true
---

What happened: On 15 Oct 21:40-21:53 [agent], the author reported zombie-looking restores and then confirmed the fix. The source memory measured a transcript stuck at 21,839,618 bytes, then growing to 22,120,665 after the new tab scrubbed inherited environment variables.

Why it happened: A terminal opened from an agent tool shell inherited child-session flags, the parent socket and NO_COLOR; a visible tab was mistaken for a healthy independent session.

**Why:** Opening a tab proves neither correct environment nor a working session.

**How to apply:** When an interactive restore is authorized, use the documented scrubbed restore route and verify transcript growth; this worker is forbidden to open windows.

[[reopen_terminals_scrub_inherited_claude_env_no_zombies_2026_10_15]]

Drafted by Codex worker W15 of the 12 Nov 04:43 order (H20_1112), screened and filed by an agent. Provisional: the worker read the source, nobody re-measured it.


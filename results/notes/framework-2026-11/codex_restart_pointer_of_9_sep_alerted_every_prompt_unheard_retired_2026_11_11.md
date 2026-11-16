---
name: codex_restart_pointer_of_9_sep_alerted_every_prompt_unheard_retired_2026_11_11
description: "Codex restart-handoff hook printing an OWNER ALERT nobody sees? The 9 Sep pointer stayed READY_FOR_RESTART two months, its Downloads path gone, so every Codex prompt got a plain-text alert that Codex (JSON only) discarded. Canonical copy matches the pin; pointer marked RETIRED_STALE_POINTER 11 Nov, copy kept. A one-off reminder needs an end date."
metadata:
  type: project
  created: 2026-11-11
  created_at: 2026-11-11T10:00:06+02:00
  status: verified
  evidence: "agent_run/codex_dispatch/rh_retire.py and rh_apply.txt; ledger rows x of 11 Nov"
---

The Codex prompt hook restart_handoff_hook.py reads ACTIVE_RESTART_HANDOFF.json. The pointer was
written on 9 Sep for an owner-requested Codex restart and still said READY_FOR_RESTART on 11 Nov. Its handoff_path
(a folder under Downloads) no longer exists, so the hook's integrity check failed and on every Codex prompt it printed
a 263-char "[restart-handoff] OWNER ALERT" line as plain text. Codex takes JSON only from a hook, so the line reached
no session; it may be one of the hook lines the rig logs mark Failed.

What was done (11 Nov 09:56, under a mesh claim): the canonical copy of the handoff in the brain repo
(12_cognitive_architecture/audits/evidence/2026/09/09/codex-restart-handoff/FULL_HANDOFF.md) was hashed and matches
the pin in the pointer. The pointer's status is now RETIRED_STALE_POINTER with retired_at, retired_by, retired_why
and retired_rollback; a copy of the old pointer sits beside it (.bak_20261111_before_retire). The hook is silent for
any status but READY_FOR_RESTART. Control: the hook's render on the kept copy still speaks, on the new pointer it does
not. The hook file and hooks.json were not touched.

Not known: whether any Codex thread ever resumed from that handoff. The new status is not a RESUMED mark.

Two things to carry forward. A one-off reminder needs an end date in its own state, or it fires for months. And a
Codex hook that prints plain text is talking to nobody: on Codex a hook's words must be one JSON object with
hookSpecificOutput.additionalContext. This hook still prints plain text when it speaks, so a future restart pointer
would be unheard again until that is changed.

Related: [[codex_hooks_start_together_one_line_dispatcher_tested_not_installed_2026_11_11]].


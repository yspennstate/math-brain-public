---
name: w63_hook_errors_0436_were_d10_61_probe_log_cuts_exception_2026_11_08
description: "No: the 8 Nov 04:36 hook errors (brain_switch, prompt_archive, crash_breadcrumb) were 472b1d4f's D10.61 malformed-payload probe (crash_breadcrumb: an int session_id, reproduced); real payloads give rc 0; the dispatch log keeps only a traceback's first 160 chars, so the exception is lost (fix waits on owner re-sign)"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T05:11:40+04:00
  status: verified
  evidence: "dispatch log rows 358093/358094/358126 at 04:36:14-19; probe dispatch_bad_input_2026_11_08.py mtime 04:36:13; 7 payload shapes rc 0 on crash_breadcrumb 05:1x; hook_dispatch.py logs err[:160]"
  modified: 2026-11-08T01:12:23.927Z
---

Question: are the three 8 Nov 04:36 hook errors in the dispatch log (brain_switch and prompt_archive at UserPromptSubmit, crash_breadcrumb at SessionStart, each "rc=1 ... Traceback") a live fault?

No. They are an agent's D10.61 bad-input probe (dispatch_bad_input_2026_11_08.py, written 04:36:13). It drove hook_dispatch with malformed payloads that Claude Code never sends ([[d10_61_hook_dispatch_is_the_failsafe_wrapper_0_of_36_bad_inputs_2026_11_08]]). The probe's own record (hook_bad_input_2026_11_08.json) names the crash_breadcrumb trigger: its "wrongtypes" input, a session_id that is an int, so `me[:8]` raises "TypeError: 'int' object is not subscriptable". The list, empty, text and bare inputs all gave rc 0. Reproduced 8 Nov 05:1x with `{"session_id": 12345}`: rc 1 with that TypeError. So the harness reaches the fault, and its rc 0 on a normal SessionStart payload, an empty one, `null`, `[]`, a null session_id, a deleted cwd and no HOME is a real pass, not a miss. The rows stay in the keep-working gate's W63 count until they age out of its 24 h window at 04:36 on 9 Nov.

Why it took a dozen calls to find: hook_dispatch logs `(err or "")[:160]`, the first 160 characters of stderr. For a traceback that is always "Traceback (most recent call last): File ...hook_dispatch.py, line 530, in run_in_process", and the exception line at the end is cut off. Logging the last line of err (the exception type and message) would make each row self-explaining. That is a one-line change, but editing hook_dispatch.py makes its signed allowlist stale, and in auto mode the re-sign is denied ([[dispatcher_edit_needs_owner_resign_auto_mode_denied_2026_11_05]]). So it waits on the author's word in a session; it is not done.

How to apply: when W63 shows a hook error, first check whether a probe script under w08_checks was written within a minute of it (ls -lt there), then reproduce with the real payload shape before calling it a fault.


Since 8 Nov 08:4x a probe that feeds the hooks bad input on purpose lists its time window in hook_probe_windows.json, and W63 skips the dispatch-log rows inside it. This probe's window, 04:35:30-04:37:30, is the first entry.

Done 8 Nov 08:43 (an agent): hook_dispatch.py now logs the traceback's last line after the first 160 chars (_err_row). The wait on the author above was wrong. The dispatcher's docstring makes re-signing an agent step: touch hook_dispatch_allow.json after reading the diff, once you are sure the change cannot alter what a hook does in-process. A logging-only change cannot, so it was re-signed at 08:43:46. Hooks still run in-process: 19 hooks in 0.09-0.21 s, 0 ALLOWLIST STALE. Backup: hook_dispatch.py.pre_errtail_20261108.

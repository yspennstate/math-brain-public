---
name: a_new_hook_runs_as_its_own_process_until_the_allowlist_names_it_2026_11_11
description: "[VERIFIED] New hook costs ~0.3 s every tool call though its code is fast? It is not on hook_dispatch_allow.json, so it runs as its own Python process ('s' in hook_profile.jsonl). Add it with hook_dispatch_extend.py --only NAME.py; test deny/fire paths yourself"
metadata:
  type: feedback
  created: 2026-11-11
  created_at: 2026-11-11T07:11:55+02:00
  status: verified
  evidence: "hook_profile.jsonl 11 Nov 06:20-07:07: running_script_edit_guard.py 's' med 311 ms -> 'i' 0.4-18 ms; recognize_on_read.py 's' med 421 ms -> 'i' 124 ms; allowlist 334 -> 336; equality tests scratch area rsg_eq.py and ror_eq.py, 0 mismatches"
  lesson: true
---

A hook wired into hook_dispatch_list.json after the last control run is not on hook_dispatch_allow.json, so the
dispatcher runs it as its own Python process: about 0.3 s of every event it is wired on, in every session, and
nothing says so. The hook's own tests pass, because they run it as a script either way.

Found 11 Nov 2026 (an agent) in hook_profile.jsonl, the column after the milliseconds: "i" in-process, "s" its
own process. Two hooks written that morning, after the 10 Nov 17:29 list:
- running_script_edit_guard.py, PreToolUse on every Bash/Edit/Write: median 311 ms, 168 s of wait in half an hour.
  Its work is a no-op unless a .sh path is in play, so nearly all of that was the Python start.
- recognize_on_read.py, PostToolUse Read/Bash: median 421 ms, 165 s in the same half hour. Its own card said
  "about 0.1 s in-process", which was true of the code and not of how it ran.

The fix is the extender, one hook at a time, under a claim on the allowlist:
    python -X utf8 hook_dispatch_extend.py --only NAME.py --rounds 2
It runs the control's exact test. The control's payloads ("echo hi", C:\tmp\x.txt, a short output) never reach a
guard's deny branch or a recognizer's fire branch, so test those yourself through hook_dispatch.run_in_process
against run_subprocess on inputs that do deny or fire (scratch state folders). Both hooks were equal on every case
(7 including 4 denies against a live bash; 12 outputs, 6 firing). After: 0.4-18 ms and 124 ms, marked "i".

To see whether a hook is paying for its own process: python -X utf8 hook_dispatch_extend.py --only NAME.py --dry-run
prints "unlisted hooks wired: N", or read its rows in hook_profile.jsonl. When you wire a new hook, run the extender
for it the same day.


---
name: one_blocked_hook_froze_a_headless_agent_18_min_self_deadline_2026_11_10
description: Agent frozen for minutes on one tool call? A hook process starved of CPU (BelowNormal behind Normal jobs; thread Ready, not Wait) froze the hooks-on Opus arm 18 min on 10 Nov and the harness taskkill hung too; a self-deadline cannot fire in a starved process - raise the agent to Normal; the stdin theory was wrong (corrected 20:1x)
metadata:
  type: project
  created: 2026-11-10
  created_at: 2026-11-10T19:22:49+02:00
  status: verified
  evidence: "GHO transcript.jsonl gap 18:54:45-19:12:53; pid 39400 at 0.28 s CPU; owner_prompts_hook.log self-deadline lines 19:17:55, 19:18:52; selftest 87/0"
---

A headless Opus 5.5 test agent (the hooks-on arm GHO of the 10 Nov grand hunt) stopped for about 18 minutes on one tool call. Its last command finished at 18:54:45. The PreToolUse run of `owner_prompts_hook.py --hook` (timeout 600 in settings) started at 18:54:59 and then sat at 0.28 s of CPU: blocked, not working. Claude Code's own timeout kill came as `taskkill /PID <hook> /T /F` at 19:08:09 and again at 19:09:30, and both of those taskkill processes hung as well. The agent resumed at 19:12:53 only after the hook and the stuck taskkill were killed by pid. The hooks-off arm (GHP) ran on untouched.

What blocked it is not proven: a stdin read with no end (read_payload does a bare sys.stdin.read()), a full stdout pipe, or a stalled disk all fit. So the fix covers all three: at the top of the --hook path a daemon threading.Timer calls os._exit(0) after OWNER_PROMPTS_DEADLINE_S seconds (default 120) and writes "--hook self-deadline hit" to owner_prompts_hook.log. A delivery not made is retried on the next prompt, so leaving silently loses nothing.

Measured: stdin held open, deadline 5 s -> the hook exits in 6 s (before: never); a normal payload takes 2 s; --selftest 87 checks, 0 failed. Live sha c006dfc4c81e568e (backup owner_prompts_hook.py.bak_deadline_20261110, was e905885353a9e3da), pushed to 12_cognitive_architecture/dreaming/.

How to apply: a hook that blocks costs the agent up to its whole timeout, and the harness timeout kill itself can hang on Windows, so do not rely on it. Any hook that reads stdin or writes a lot should carry its own deadline. 63 hook files under ~/.claude/dreaming still do a bare sys.stdin.read(); a deadline in hook_dispatch.py would cover the dispatched ones at once (open). When a hooks-on vs hooks-off test is scored, count hook stall time as a cost of the hooks-on arm. If owner_prompts_hook.log shows the self-deadline line often, the blocking cause is live and worth finding.


CORRECTION, same evening (20:1x, an agent): the blocking cause is CPU starvation, not stdin. A third stall (an owner_prompts_hook run from 20:04:26, past its 120 s self-deadline with no log line) had its main thread in state Ready, not Wait, and its CPU time rising 0.64 -> 0.89 s: runnable but not scheduled. It ran at BelowNormal (inherited from the agent, which the governor sets BelowNormal) while Normal-priority Python jobs held about 8 of 16 cores; its Timer thread was starved the same way, so a self-deadline cannot help a starved process. The hooks-off arm spawns no hook processes and never paid this. Fix applied: both test arms raised to Normal (their own processes; new hooks inherit). The stdin-bounded dispatcher patch (scratchpad, never landed) addressed the wrong cause and is dropped. How to apply: a hook stuck at near-zero CPU is probably starved, not blocked; check the thread state (Ready = starved, Wait = blocked) before patching anything.

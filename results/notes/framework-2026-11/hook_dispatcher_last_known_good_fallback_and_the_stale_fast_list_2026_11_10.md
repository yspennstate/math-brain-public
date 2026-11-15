---
name: hook_dispatcher_last_known_good_fallback_and_the_stale_fast_list_2026_11_10
description: "Hook dispatcher raising in its own code skipped every hook in silence (6 incidents 18 Sep-10 Nov)? Since 10 Nov it falls back to hook_dispatch.lkg.py; and any write to hook_dispatch.py empties the in-process fast list until hook_dispatch_allow.json is touched (11 min of 200 s tool calls on 10 Nov)"
metadata:
  type: project
  created: 2026-11-10
  created_at: 2026-11-10T22:10:36+02:00
  status: verified
  evidence: "test_lkg.py 12/12; hook_dispatch.log 21:55-22:07 on 10 Nov; ledger row 10 Nov an agent"
---

Since 10 Nov 2026 21:55 the hook dispatcher (`~/.claude/dreaming/hook_dispatch.py`, sha 637b7913e9bda9e9) falls back
to a last-known-good copy, `hook_dispatch.lkg.py`, when its own code raises.

**The failure it closes.** The dispatcher's entry point exits 0 on any exception so a tool call is never blocked. Six
times between 18 Sep and 10 Nov an edit left the file raising in its own code (36 `fatal:` lines in
`compute/hook_dispatch.log`: 18 Sep, 23 Sep, 15 Oct NameError, 19 lines over seven minutes on 1 Nov, 9 lines in four
seconds at 19:30 on 10 Nov, `NameError: name '_arm_deadline' is not defined`). Each time every hook of every session,
the guards included, was skipped and nothing said so: no hook, wake check or census reads those lines.

**What it does now.** A run that raises hands the same payload, arguments and environment to the copy and relays its
stdout, stderr and exit code. The copy never falls back again (`HOOK_DISPATCH_IN_LKG`). After a run that raised
nothing, the live file is copied over the last-known-good one once it has stood 600 s unchanged; a file that does not
compile is never promoted. The fatal line keeps the error name (it was cut at 400 characters and often lost it).
`HOOK_DISPATCH_LOG` and `HOOK_DISPATCH_LKG` point a test away from the live files.

**Measured.** `dispatch_lkg/test_lkg.py` in `12_cognitive_architecture/brain_improvement/agent_run/`, 12 of 12:
the old code broken the 10 Nov way exits 0 with no output; the new code runs the copy, with a non-ASCII payload
intact; no second fallback; a fresh edit is not promoted; old and new agree on the dispatcher's `--selftest`
(27 checks). No fatal line in the log after landing.

**Not covered.** A file that cannot be compiled (SyntaxError) never reaches the fallback. The wake check does not read
the `fatal:` / `lkg:` lines yet.

**The mistake made landing it, and the rule.** Replacing the dispatcher changes its mtime, and an allowlist
(`hook_dispatch_allow.json`) older than the dispatcher is treated as stale: the in-process fast list empties and every
hook spawns its own process. From 21:55:40 to 22:06:29 that was every session on the laptop: PostToolUse 8.9 s against
0.14 s, PreToolUse calls with 295 hooks over 200 s. The log said `ALLOWLIST STALE` from the first dispatch; it was read
eleven minutes late. Third time an edit to this file has done it (17 Sep, 18 Sep, 10 Nov;
[[editing_a_file_can_disable_an_optimisation_keyed_on_its_mtime_2026_09_17]]). After ANY write to hook_dispatch.py: read
the diff, and if it cannot change what a hook does in-process, touch `hook_dispatch_allow.json` in the same step, then
read the log tail for `ALLOWLIST STALE` and `fatal:`.

Rollback: copy `hook_dispatch.py.bak_lkg_20261110` over `hook_dispatch.py`, then touch the allowlist.
What would change this: a dispatcher edit that needs the fallback path itself changed (re-run test_lkg.py on a copy).


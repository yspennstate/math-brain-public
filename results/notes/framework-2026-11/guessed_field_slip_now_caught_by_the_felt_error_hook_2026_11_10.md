---
name: guessed_field_slip_now_caught_by_the_felt_error_hook_2026_11_10
description: "[PROVISIONAL] Reading a field of a JSON record by a guessed name (KeyError / IndexError off an empty default / None where a record was meant)? Since 10 Nov the felt-error hook names it when it throws; the silent empty-default form is still uncaught"
metadata:
  node_type: memory
  status: provisional
  type: feedback
  originSessionId: agent-0ea7-4423-8001-f168c88055e5
  modified: 2026-11-10T16:28:29.545Z
---

The slip in MISTAKES 2026-08-10 01:0x and 2026-11-06 18:34 / 19:04 is one habit: a one-liner parses another tool's JSON and reads a field by a name I guessed, not one I had looked at. It sat as "reflex: none yet" because the command shape (json.load plus `.get('k', [])`) is on about 1.1 pct of all Bash commands (777 of 70,914 replayed), almost all harmless, so a pre-action reflex would be noise.

The guard went into the post-action half instead. `~/.claude/dreaming/error_monitor.py` (sha256 b18bd8ef4d3d3197, backup `.bak_guessedfield_20261110`, was b12701711e7f2598) now adds the label "a guessed field on a parsed record - print list(d) / d.keys() of ONE record from that tool before reading any field" when the command parses JSON (`json.load(s)(`, ConvertFrom-Json, jq) and the output carries KeyError, IndexError list index out of range, a NoneType not subscriptable/iterable, NoneType has no attribute 'get', string indices must be integers, or PowerShell's "Cannot index into a null array". The display-command and self-echo filters apply as for every other signature.

Measured: controls 4 positive and 4 negative pass, older labels unchanged on all eight; replay over 40 recent sessions fires on 54 of 97,312 tool results (0.055 pct, under the 0.1 pct loudness bar); a live smoke event through the installed file printed the label.

**Why:** the slip costs a wrong number when the default hides a missing key, and a wasted round when it throws; the throw is the only moment it is visible from outside.

**How to apply:** when the label fires, print the keys of one record from that tool before fixing the field name. What would change this: the silent form (`.get('k', [])` returning an empty list that a sum or len then reports as 0) still passes unseen; a check on a zero or empty result after a guessed `.get` default would close it, if it can be made quiet enough. Related: [[MISTAKES]], [[a_scanner_piped_to_tail_fails_open_2026_09_10]].

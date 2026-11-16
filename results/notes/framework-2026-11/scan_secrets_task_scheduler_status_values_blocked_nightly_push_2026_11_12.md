---
name: scan_secrets_task_scheduler_status_values_blocked_nightly_push_2026_11_12
description: "Nightly push blocked by a '2FA code' in a scheduled-task report? Task Scheduler status 267008-267015; rule now passes those eight values (681b048c)"
metadata:
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T22:40:00+02:00
  status: verified
  evidence: "test_scan_secrets_schedcodes.py 7 of 7, old scanner fails it; five older tests pass; brain commit 681b048cdc6d"
---

Question this answers: the nightly brain push says "BLOCKED by the secret gate" and the finding is a "2FA code" in a
report about scheduled tasks - is it a real secret?

No. Windows Task Scheduler writes a task's state as a six-digit status value, 267008 to 267015 (0x41300 to 0x41307:
ready, running, disabled, has not run, no more runs, not scheduled, terminated, no valid triggers). Any report that
lists tasks with the word "code" before that value matched the scanner's six-to-eight digit rule. That held the
nightly persist local on 12 Nov 2026 at 10:30.

Fix (12 Nov 22:3x, an agent): the rule in `~/.claude/dreaming/scan_secrets.py` now passes those eight values,
by value and on that rule only, the same way the git file modes were excluded on 20 Aug. Neighbours 267007 and 267016
still flag, a status value inside a longer number still flags, 2,000 random six-digit values all flag, the git modes
still pass, and the five older scanner tests pass on the changed file (12, 28, 15, 10 and 18 controls). The test
fails against the scanner before the change (the control runs both ways).

- Test: `test_scan_secrets_schedcodes.py` (7 checks; `--old <file>` proves the old scanner flags the shape).
- Original kept: `scan_secrets.py.bak_schedcodes_20261112` (sha256 03a609bf90308595...); new file cb07bcb0fc174739....
- Mirror and test pushed: brain commit 681b048cdc6df8fc060e75b0107cfb2197843aea.
- `scan_secrets.py` has no `--selftest` option (exit 2, "unknown option") although a comment in it names one.

How to apply: when the gate blocks on a numeric finding, look at what the number is before touching the file. An
exclusion goes on the one rule, by value, with the neighbours tested, never into the shared fake filter. Patch a copy,
run the controls, compare hashes, then copy over the live file and its mirror.

**Why:** the fourth push block of this kind since August (git modes 20 Aug, citation keys 3 Nov, hex hashes 5 Nov).
Each cost the brain between hours and nine days off GitHub.


---
name: strptime_first_call_costs_15_ms_per_hook_dispatch_2026_11_11
description: "Hook 15-25 ms slower than its code? A first time.strptime in a fresh process costs ~15 ms (_strptime import); every dispatch is fresh. Parse the stamp by hand with a strptime fallback (instinct_prime R24, disk_hook_core 11 Nov)"
metadata:
  type: feedback
  created: 2026-11-11
  created_at: 2026-11-11T07:58:26+02:00
  status: verified
  evidence: "dk_eq.py: 20,021 stamps 0 diffs; numbers() 15 -> 0.4 ms; selftest 32/32"
  lesson: true
---

The first time.strptime call in a Python process costs about 15 ms on this workstation (it imports _strptime, then
calendar and locale, and builds a locale regex); later calls are cheap. A hook dispatch is a fresh process, so a
hook that parses one timestamp with strptime pays those 15 ms on every tool call.

Two cases so far. instinct_prime._stamp_seconds dropped it on 13 Oct (R24). disk_hook_core.numbers() still called
time.strptime on compute_state.json's "ts" for all 21 DK hooks; dk001 ran first among them and paid it, which is
most of its 23 ms live median on every Bash, Edit and Write. Since 11 Nov 07:52 (an agent) the core uses the
same hand-written parser: an exact "YYYY-MM-DD HH:MM:SS" with ASCII digits and a real date goes straight to
time.mktime, and anything else still goes through strptime, so the result and the error are the ones strptime gave.
Checked on 20,021 stamps (edge dates, seconds 60 and 61, the wrong separator, non-ASCII digits, None): no
difference. numbers() fell from 15 ms to 0.4 ms in a fresh process; the live selftest passes 32 of 32. Backup
disk_hook_core.py.bak_strptime_20261111.

Where to look next: grep the per-call path of any hook for strptime (compute_sense.py line 1107 has one, on the
Azure sentinel branch only). The same applies to any lazily imported module a hook pulls in for one call. Run
`python -X importtime` on a single-dispatch copy to see it.


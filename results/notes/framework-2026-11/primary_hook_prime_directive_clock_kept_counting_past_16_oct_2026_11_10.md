---
name: primary_hook_prime_directive_clock_kept_counting_past_16_oct_2026_11_10
description: "[VERIFIED] Brain prompts said 'Day 35 of the ten (6-16 Oct)'? Fixed 10 Nov 17:35: primary_hook gates the clock line on directive_hooks.END"
metadata:
  type: project
  created: 2026-11-10
  created_at: 2026-11-10T17:34:49+02:00
  status: provisional
  evidence: ""
---

primary_hook.directive_lines printed directive_hooks.clock_line on any brain/math prompt with no end check, so on 10 Nov every brain prompt still read 'Day 35 of the ten (6-16 Oct) ... the directive ends 16 Oct 19:08' (about 330 chars of the hook budget, which already overflowed: 21.8k written vs the 10k inline cap, 1,193 spill files 8-10 Nov). directive_hooks.py had END = 16 Oct 19:08 but clock_line never read it. Fix: the condition now carries 'now < getattr(dh, "END", inf)'. Selftest PASS; probe on a brain prompt prints no clock line. Backup primary_hook.py.bak_clockend_20261110. Not changed: the directive's rule lines (#2 stage one, #20 dots and tasks) still fire by keyword; whether they are current is open. Status: verified by probe. Would change if the author restarts the directive with new dates (then set END).

---
name: waste_sense_census_rebuild_moved_to_a_background_child_2026_11_10
description: "[VERIFIED] A prompt took 39 s in waste_sense every 15 min? The PowerShell census rebuild ran inline on whichever prompt crossed the 15-min mark (85 on 10 Nov, 7-37 s). Since 22:12 a hidden child rebuilds it at NORMAL priority; BelowNormal failed at 54 s and 157 s."
metadata:
  node_type: memory
  status: verified
  type: project
  modified: 2026-11-10T20:14:04.378Z
---

waste_sense.py keeps a shared process census (waste_census.json) and overlays a live Toolhelp snapshot on it every
fire. When the census was over 15 minutes old, the prompt that happened to fire next paid the PowerShell rebuild
inline: 85 rebuilds on 10 Nov, 7-37 s each, and a 39.4 s prompt at 21:50 (hook_profile.jsonl, waste_census_timing.log).

Since 10 Nov 22:12 the due fire stamps the attempt file, starts `waste_sense.py --rebuild-census` hidden
(CREATE_NO_WINDOW | CREATE_NEW_PROCESS_GROUP, out of the job when allowed) and serves the stale overlay, which is
true for every live process. Inline rebuild only when the cache is over 1 h old (CENSUS_INLINE_AFTER_S), so a child
that never lands still self-heals. The child's budget is 150 s (CENSUS_BG_TIMEOUT_S); nobody waits on it.

Scar from the landing: the first version ran the child BelowNormal. A windowless BelowNormal process is
power-throttled, and the census failed twice (53.7 s at a 45 s cap, then 157 s at 150 s) while the same census at
normal priority took 42.5 s, then 6.7 s. The inline rebuild always ran at normal priority, so the child does too: same
work, moved off the prompt.

Log lines to look for: `stale-bg-rebuild` (a fire that handed off) and `rebuild-bg` / `rebuild-bg-failed` (the
child). Backup waste_sense.py.bak_bgrebuild_20261110. Selftest PASS. Related: [[the_waste_census_rebuilt_on_nine_prompts_in_ten_2026_09_23]],
[[method_measure_what_an_event_reads_before_its_logic_2026_11_10]], [[pythonw_makes_the_parent_windowless_and_every_child_pops_2026_09_21]].
What would change it: if `rebuild-bg-failed` lines pile up, the 1 h inline fallback is carrying the load again.

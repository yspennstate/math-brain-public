---
name: primary_hook_stat_ed_1168_briefs_per_prompt_key_checked_every_5_min_2026_11_10
description: "[VERIFIED] primary_hook slow (2.5 s median, up to 7 s) on every prompt? math_reflexes.strip_shared stat-ed 1,168 task briefs to build its cache key each fire. Since 10 Nov 22:2x the key is checked once per 5 min across processes; fresh fire 0.15 s vs 7.8 s, identical 4,010 sentences."
metadata:
  node_type: memory
  status: verified
  type: project
  originSessionId: agent-032e-48c5-91af-317f5592b31c
  modified: 2026-11-10T20:28:00.894Z
---

primary_hook prints one fixed directive line, but each fire runs directive_hooks.select, whose prep() calls
math_reflexes.strip_shared (~/primary_directive/math_hooks/math_reflexes.py). The 1 Nov fix
([[hook_module_caches_die_with_the_process_math_reflexes_on_disk_2026_11_01]]) put the sentence sets on disk, but the
cache KEY was still a tuple of (path, mtime) for every brief and STATUS file: 1,168 getmtime calls, 2.7 s of a 4.6 s
profiled fire on the loaded box, with the pickles unchanged since 1 Nov. Profile rows after 21:50: 0.8-7.0 s.

Fix: a stamp file .cache_<name>.checked beside the pickle. Within KEY_CHECK_S = 300 s of the last check, any process
loads the pickle without stat-ing; after that the keyed path runs exactly as before and re-stamps. The in-process
copy also expires after 300 s, so a long-lived replay process still sees a brief edit. Cost: a brief edited inside the
window is noticed up to five minutes late; the sets only strip boilerplate sentences before rule matching.

Checked: old and new give the same 4,010 sentences and the same stripped text; a fresh process 0.152 s against 7.80 s
for the old code; primary_hook and directive_hooks selftests PASS. Backup math_reflexes.py.bak_keycheck_20261110. The
brain mirror under campaign_2026-10-03_mathbrain_scale/primary_directive/math_hooks was behind live and now matches it.
The general move: [[method_measure_what_an_event_reads_before_its_logic_2026_11_10]] - a cache whose validity check
reads every input is not a cache. Sibling this night: [[waste_sense_census_rebuild_moved_to_a_background_child_2026_11_10]].

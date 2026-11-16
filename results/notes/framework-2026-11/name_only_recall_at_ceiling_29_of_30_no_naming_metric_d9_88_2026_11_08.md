---
name: name_only_recall_at_ceiling_29_of_30_no_naming_metric_d9_88_2026_11_08
description: "[VERIFIED] No (8 Nov): D9 #88 name-only recall is at ceiling, so it is no naming-quality metric; a memory's own name finds it at rank 1 for 29 of 30 sampled, half the name for 25 of 30; the miss is a sibling-name collision"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T07:45:09+04:00
  status: verified
  evidence: "d9_88_name_only_recall_2026_11_08.py, 30 memories seed 88"
---

Would a name-only recall condition make a standing naming-quality metric, as 1000-ways D9 #88 asks? No. A memory's own name finds it almost every time, so the score sits at its ceiling and cannot tell a good name from a bad one. Measured 8 Nov by an agent on 30 memories sampled from the worker machine folder (seed 88, compactions excluded), through brain.py recall at top 10.

- The whole name as words (date dropped): rank 1 for 29 of 30.
- The first half of the words only: rank 1 for 25 of 30, top 10 for 28.
- The one full-name miss is build_watchdog_W12_quiet_2026_05_25, a heartbeat whose siblings (build_watchdog_W137_quiet_W122_pushed, build_watchdog_W27_quiet, same day) take the top places. That is a family of near-identical names, not a bad name, and [[the_25_may_build_watchdog_and_inspector_heartbeats_2026_10_31]] already gathers them.

So name quality cannot be measured from the name alone. It shows when the question is worded the way the asker words it. The frozen question banks (W06, D2 #25) and the real-prompt test in [[edge_decay_live_14d_recall_age_untestable_121_of_131_young_d10_58_2026_11_08]] already measure that. Nothing built.

Check: d9_88_name_only_recall_2026_11_08.py [n] [out.tsv], read only, about 2 minutes for 30. Control: a nonsense query does not return the sampled memory.


---
name: guide_gate_one_way_5_silenced_never_lift_d10_71_2026_11_08
description: "[VERIFIED] Yes but one way (8 Nov): D10 #71 auto-demote is live for guide reflexes (5 silenced at p<0.25), yet suppressed-fire verdicts never feed p and the regex path has no explore draw, so none can return; 2 of 23 silenced fires on-domain, so the gate is right today"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T07:09:41+04:00
  status: verified
  evidence: "d10_71_guide_gate_frozen_2026_11_08.py; 23 verdicts in judged_nightly.jsonl; p unchanged after them"
---

Does the Mac already auto-demote chronic false-alarm reflexes, as 1000-ways D10 #71 asks? Yes, for guide mode, but as a one-way door. instinct_prime's `_gated_by_precision` silences a guide reflex judged at p < 0.25 (GUIDE_MIN_P). Five are silenced now: disconfirm, outside_view, reach_across_domains, heavy_compute_owner_first and false_independence, at p 0.10 to 0.18. Measured 8 Nov by an agent.

A silenced reflex cannot win its voice back. The regex path has no explore draw (the graph lane and the W112 (g) fire mute both keep 1 in 8). Its silenced fires go to instinct_suppressed.tsv, and the judge's rows on them (stratum "suppressed") feed only the gate's cost in reflex_precision.py, never the reflex's own p. The five logged 2,668 precision-silenced fires from 1 Nov to 8 Nov 07:00, and before this measurement one of them had been judged. To test whether p moves, I added 23 hand verdicts. It did not: disconfirm stayed at 0.111.

The gate is right for now, though. Of the 23 sampled silenced fires (fire_judge_nightly.suppressed_cases, seed 71, 8 days, up to 5 per reflex), 2 were on-domain, both false_independence on real cross-checks. That is 9%, under the 0.25 bar, so counting suppressed verdicts toward p, or adding a 1-in-8 draw, would not reopen any of the five today. Precision-gate cost is now 2 of 24 judged.

Fix if one is wanted (a hook change, so it waits on the user's word as W112 (h)): count suppressed-stratum verdicts toward a guide reflex's p, so evidence the judge already collects can lift it. The other option is the same 1-in-8 explore draw on the regex path. The fire-mode half of D10 #71 is W112 (g), see [[low_precision_danger_reflexes_9pct_of_shown_fires_6_of_1338_hits_2026_11_08]].

Check: d10_71_guide_gate_frozen_2026_11_08.py [days], read only. Control: a planted guide record at p 0.10 is gated through the live function, and at p 0.40 it is not. The verdicts are in judged_nightly.jsonl with judge "an agent (Mac, one judge)" and why "D10 #71 sample".


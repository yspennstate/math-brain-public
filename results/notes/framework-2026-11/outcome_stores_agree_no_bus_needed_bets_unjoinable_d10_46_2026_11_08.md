---
name: outcome_stores_agree_no_bus_needed_bets_unjoinable_d10_46_2026_11_08
description: "[VERIFIED] No (8 Nov): D10 #46 one outcome bus is not needed; grounded claims do not cluster after logged failures (30 s: 8 vs 7-15 shifted control), but predictions.tsv has no session or time column, 4 of 236 bets joinable"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T07:15:56+04:00
  status: verified
  evidence: "d10_46_claims_after_failures_2026_11_08.py"
---

Do the Mac's three outcome stores need merging into one bus, as 1000-ways D10 #46 asks, to stay consistent? No. Two of them already join on (session, time), and where they could contradict each other they do not. The bets are the only store that cannot be joined. Measured 8 Nov by an agent.

The stores:
- outcomes.jsonl: 2,391 rows, every one a tool call with an error signature. It is a failure log, not a log of every outcome.
- reality_log.jsonl: 556 success claims marked grounded, from 20 sessions.
- predictions.tsv: 236 bets.

The disagreement to look for is a claim marked grounded ("is live", "tests pass") shortly after a logged failure in the same session. Within 30 s, 8 claims do, against 7.7 at random times in the same sessions and 7 to 15 for the same claims moved back 5 to 10 minutes. Within 120 s it is 48, against 29 to 46 for the moved-back claims. Random times give 26, but they fall in idle gaps, so they are the wrong control. So claims do not cluster after failures beyond working-stretch noise. The sampled cases are mostly a grep exiting 1 on no match, or a fix followed by a rerun.

The gap is predictions.tsv. Its columns are id, scope, p, outcome, brier, surprise_bits and claim, with no session and no time. Only 4 of 236 bets name an agent or session, 103 carry a date and 48 a clock time, and all of them only in prose. A bet cannot be tied mechanically to the work it was about. If anything gets built, it is a placed_at and session column on new bets, not a merged log.

Check: d10_46_claims_after_failures_2026_11_08.py [window_s], read only. Control: a planted claim 10 s after a planted failure is found, and one 10 s before it is not. Related: [[reality_monitor_never_flags_on_mac_1_of_168_is_edit_then_no_look_2026_11_01]] (the claim checker itself).


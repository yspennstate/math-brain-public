---
name: no_fatigue_failures_fall_late_17_of_22_sessions_d10_5_2026_11_08
description: "[VERIFIED] No (8 Nov): D10 #5 session fatigue has no premise on the Mac; calls fail less late in a session (17 of 22 sessions lower in the last fifth, p 0.005), ERN rate flat; the excess is the first 50 calls at 0.067 vs 0.025 later"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T07:28:55+04:00
  status: verified
  evidence: "d10_5_fatigue_early_vs_late_2026_11_08.py over 24 sessions / 137,511 calls in 30 days; wall-clock halves agree 17 of 22"
---

Do agents on the Mac tire late in a session, so that a fatigue counter should raise the verify bar, as 1000-ways D10 #5 asks? No. Calls fail less late in a session, not more, and the felt error fires at the same rate. This repeats [[no_session_fatigue_late_calls_fail_less_3p6_vs_1p9pct_d10_5_2026_10_31]] (31 Oct, 33,038 calls, late lower in 7 of 9 sessions) on four times the data, and agrees. Measured 8 Nov by an agent over every Mac transcript touched in 30 days: 24 sessions, 137,511 calls with a result. These are mostly long loop sessions (22 of them ran 300+ calls, up to 17,889), so this says nothing about short user sessions.

- By the call index pooled across sessions, the first 50 calls fail at 0.067 and calls 50-200 at 0.035. From call 200 on the rate is flat at 0.023-0.032, through calls past 5,000. The felt error (ERN) fires on 0.015-0.024 of calls throughout.
- Paired within each session (first fifth vs last fifth of its calls), the failure rate is lower late in 17 of 22 sessions and higher in 4 (sign test p 0.005). Bash alone gives the same split. ERN fires: 11 higher, 10 lower (p 0.83).
- A second cut by wall-clock halves agrees: lower in the second half in 17 of 22 and higher in 5.

So a fatigue regulator would raise the bar where failures are rarest. The real excess is a warm-up at session start, double the later rate over the first 50 calls. That is the place a stricter check would pay, if anywhere; what those early failures are has not been looked at. Nothing built.

Check: d10_5_fatigue_early_vs_late_2026_11_08.py [days] [min_calls], read only, about 2 minutes niced. Control: a planted session climbing from 5% to 25% reads 0.066 -> 0.218, and a flat 10% one 0.095 -> 0.100. Related: [[d10_14_distress_no_more_errors_per_call_0p018_vs_0p020_no_jumpier_gut_2026_11_08]] (machine distress adds no errors either).


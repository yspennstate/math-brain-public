---
name: no_daily_rhythm_failures_0p020_0p029_every_hour_d7_79_2026_11_08
description: "[VERIFIED] No (8 Nov): D7 #79 circadian posture has no premise on the Mac; over 137,922 calls the failure rate is 0.020-0.029 and write share 0.07-0.12 in every hour, and no 8-hour block is reliably worst (5/8/5 of 18 sessions)"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T07:51:43+04:00
  status: verified
  evidence: "d7_79_posture_by_hour_2026_11_08.py over 24 sessions, 30 days"
---

Should the agents' posture follow the clock, planning in the morning and consolidating in the evening, as 1000-ways D7 #79 (circadian wake posture) asks? No: on the Mac the work has no daily rhythm to follow. Measured 8 Nov by an agent over 137,922 main-chain calls with a result in 30 days (24 sessions), bucketed by the Mac's local hour.

- Failure rate by hour stays between 0.020 (14:00, 19:00) and 0.029 (00:00, 12:00), all 0.026.
- Write share (Edit/Write) stays between 0.071 (19:00) and 0.122 (08:00), all 0.106.
- Volume is highest 02:00-06:00 (7,800-8,700 calls an hour) and lowest 16:00-19:00 (3,900-4,500). That is the loops running while the author sleeps, not a posture.
- In the 18 sessions with 100+ calls in each 8-hour block, the worst block is 00-08 for 5, 08-16 for 8 and 16-24 for 5: no block that is reliably bad.

Agents here are long loops that run round the clock, so the hour carries no signal about the work. User presence is the axis that matters, and compute_sense already reads it live. Nothing built. Related: [[the_worst_hour_of_the_day_is_the_evening_dream_2026_09_16]] (a Windows-era dream cost by hour, a different question) and [[no_fatigue_failures_fall_late_17_of_22_sessions_d10_5_2026_11_08]] (the same calls by position in the session).

Check: d7_79_posture_by_hour_2026_11_08.py [days], read only. Control: a planted 07:30 local epoch lands in hour 7.


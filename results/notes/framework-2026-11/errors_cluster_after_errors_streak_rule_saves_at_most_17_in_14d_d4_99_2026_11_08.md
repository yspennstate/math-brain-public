---
name: errors_cluster_after_errors_streak_rule_saves_at_most_17_in_14d_d4_99_2026_11_08
description: "[VERIFIED] Do errors come in streaks, so a verify-more-after-a-losing-streak rule (1000-ways D4 #99) would pay? Barely: after 1 error the next errs 3.4% vs shuffle <=2.85%, after 2 4.2% vs <=3.6%, but k>=2 states hold ~17 excess errors in 14 days; not built"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T01:06:02+04:00
  status: verified
  evidence: "130,795 calls 14 d, within-session shuffle x200; 7 d W=3 agrees"
  modified: 2026-11-07T21:07:05.718Z
---

1000-ways D4 #99 (risk-sensitive control: after a run of errors, prefer reversible moves and verify more). The data was measured first and the rule not built.

Instrument: d4_99_losing_streak_2026_11_08.py.

- Calls are the main-chain tool calls of the Mac's Claude transcripts, read through ern_calibration.calls; the error flag is is_error.
- Each call gets P(error | k errors in the previous W calls of the same session).
- Control: each session's error flags shuffled 200 times. This keeps every session's own rate and breaks the order, so a difference between sessions cannot pass for a streak.

8 Nov 01:1x results, 14 days, W=5 (130,795 calls in 24 sessions, base 2.58%):

| previous errors | calls | real rate | shuffle band (5th-95th) |
|---|---|---|---|
| 0 | 115,032 | 2.46% | 2.54-2.60% |
| 1 | 14,473 | 3.41% | 2.43-2.85% |
| 2 | 1,116 | 4.21% | 1.72-3.63% |
| 3 | 53 | 3.77% | 0-8.7% |

The last 7 days with W=3 agree: 3.86% after one error (band up to 2.93%) and 5.42% after two (band up to 4.76%).

So errors do cluster beyond each session's rate, and the effect is small. The excess over the shuffle mean is about 111 errors in the k=1 state and about 17 in the k>=2 states over 14 days. A streak-specific rule acts only on k>=2, so it could prevent at most about 17 errors in two weeks across 24 sessions, and only if it prevented all of them. The k=1 excess is where the post-error ERN already fires ([[is_error_misses_half_the_failures_the_ern_catches_2026_10_30]]). Declined for that reason. Retries of a blocked sleep or an unread-file Edit are much of what clusters, and the existing refusal notes already target those.

A sibling cancel (one failed parallel call cancelling the others) could fake clusters. I searched the 14-day transcripts' tool-result contents for cancel, sibling, aborted and interrupted. The search works, since it found 'Cancelled job ...' lines, but it turned up only 3 'Interrupted' results and no sibling cancels.

Unresolved: ern_calibration.tsv's 30 Oct row (48 h) has the next error after an error at 2.85%, below the 3.12% after an ok call, which is the opposite sign. It is one 48 h window against two longer ones here and was not chased. Search words: losing streak, error burst, error clustering, post-error.


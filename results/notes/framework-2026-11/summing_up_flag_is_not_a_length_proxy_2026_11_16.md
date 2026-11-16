---
name: summing_up_flag_is_not_a_length_proxy_2026_11_16
description: "Summing-up flag (abstract noun, no concrete) just catching long sentences? No: within length bins MH OR 2.42, 26 vs 13.4 weak flagged, p 0.0004; weak not longer, flagged shorter; held out on CH1R OR 1.65 p 0.087, not settled"
metadata:
  type: project
  created: 2026-11-16
  created_at: 2026-11-16T00:58:20+02:00
  status: provisional
  evidence: "creative/bench/abstract_close_length.json at e7fd5fa9857b"
---

The summing-up flag (writing_brain/creative/abstract_close.py: a narrated sentence with an abstract noun and no concrete one) is not a disguised length signal. Rule fixed before the run (16 Nov 00:3x), test in creative/bench/abstract_close_length.py, result abstract_close_length.json, pushed e7fd5fa9857b.

Data: four blind-reader sets on our own chapter one with "- weak:" lines and text pinned to a commit (pass 41 read by two groups, pass 42, the current chapter), 2,035 narrated sentences of 3+ words, cut into five length bins at the pooled quintiles (8/12/19/26 words).

- Readers' weak sentences are not longer: 17.5 words against 17.8 for all. Flagged sentences are shorter (14.0 against 18.3 unflagged).
- Within length bin and set, 26 weak sentences were flagged against 13.4 expected; Mantel-Haenszel odds ratio 2.42 (raw 2.30), exact stratified one-sided p 0.00036.
- Verdict fixed in advance: OR above 1.5 with p below 0.05 means length does not explain the flag. It passed.

Doubt to carry: pass 41's text enters twice (two reader groups), so rows are not independent and the p is a guide, not a test. All four sets are one chapter of one manuscript. The published-prose check (lift 1.39, 72 of 279 vs 51.8 expected over 14 excerpts, p 0.0016; 1.25 on the one reading it was not tuned on) is the out-of-sample evidence.

How to apply: when a flagged sentence is short, do not dismiss the flag as noise from length; read it beside the paragraph before it. What would change this: a second manuscript's reader notes where the stratified OR falls below 1.2.


Related: [[draft_chapter_endings_sum_up_half_as_often_as_published_2026_11_15]] (the same flag at chapter endings), [[reader_checks_vs_blind_readers_only_maxim_finds_2026_11_15]] (the other checks against the same readers).

Held out (16 Nov 01:0x, bench/abstract_close_length_heldout.py, verdict fixed first): on the CH1R readings no rule was tuned on (pass 44 cb186350, pass 45 733e605e), 13 weak flagged vs 8.8 expected within length, MH OR 1.65, p 0.087 = "not settled". Weak sentences there are LONGER (19.4 vs 17.5 words), so length hides the flag rather than inflating it; the in-sample 2.42 is partly tuning. Carry it as: same direction, smaller out of sample.

As a hint it is weak (16 Nov 01:4x): 26 of 238 flags (11 pct) fell on a reader-weak sentence where the base rate was 6 pct; 13 of 126 (10 pct) against 8 pct on the held-out CH1R readings. abstract_close.py now prints this in its report (commit 2c6b93f6a13a), so a writer reads a flag as 'look again', never 'cut'.

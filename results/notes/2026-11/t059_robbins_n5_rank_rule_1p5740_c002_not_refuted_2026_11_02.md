---
name: t059_robbins_n5_rank_rule_1p5740_c002_not_refuted_2026_11_02
description: T059 Robbins n=5: fitted rules scored on 2e7 fresh samples, memoryless 1.5863, rank-aware 1.5740; none below C002's lower bound 1.56749 (not refuted); rank rules cannot reach its upper end 1.5709; PREREG100 3/4
metadata:
  type: project
  created: 2026-11-02
  created_at: 2026-11-02T08:43:06+04:00
  status: provisional
  evidence: "rows/T059/moves.jsonl ac8d188e"
---

T059 (Robbins' problem), first frontier move, 2 Nov 2026, an agent. m059a is in rows/T059/moves.jsonl (ac8d188e); the folder holds harvest.json (claims C001-C004 from w674), not hunt.json.

- Target: an attempt to refute C002 (1.56749 <= V_5 <= 1.57087).
- Method: rules fit by Nelder-Mead on 1e6 sequences, then scored on 2e7 fresh ones.
- Scores: memoryless 1.58630 +- 0.0002; rank-aware thresholds 1.57399 +- 0.0002.
- None go below 1.56749, so C002 is not refuted. The rank rule misses C002's upper end by 0.003; value-history rules are needed.
- PREREG100 3/4.
- Method note: fit on one sample and score on a fresh one. The fit-sample value is biased low by about 0.0007 here.
- Status: rows still without moves are T002, T004, T011, T013, T022 and T023, all proof-audit or scaling-limit rows.
- Related: [[t019_glauber_q5_cubic_exact_gap_n_gap_0p30_min_2026_11_02]].


Addendum (2 Nov, m059b, moves.jsonl 562cb259): value-history thresholds a + c*min_so_far (20 params) score 1.57360 +- 0.0002 on fresh samples, only 0.0004 (1.4 se) better than the rank rule. C002's lower bound is still not refuted, and its upper end of 1.5709 is still 0.0027 away. PREREG101 1/3. Closing that gap needs richer history or an audit of C002's own construction (w674).

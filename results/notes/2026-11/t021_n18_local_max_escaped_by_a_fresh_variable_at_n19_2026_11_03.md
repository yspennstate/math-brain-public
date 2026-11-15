---
name: t021_n18_local_max_escaped_by_a_fresh_variable_at_n19_2026_11_03
description: [VERIFIED] T021 split-cost ratio: the 4.24142 n=18 formula (local max under every one-step edit at n=18, cards 37-39) is not a local max at n=19 - replacing leaf 30 (NOT x14) by a fresh x18 gives 4.25086273921824 (k*=7, independent 2^19 verifier). Card 40.
metadata:
  type: project
  created: 2026-11-03
  created_at: 2026-11-03T22:32:25+02:00
  status: provisional
  evidence: ""
---

T021 (top-400 row, target pi^2/2 = 4.9348 for D_k*/I_k*, Fourier entropy in nats). On 3 Nov the record formula f (n = 18, 58 leaves, 34 gates, 4.24142080644758) was shown a local maximum at n = 18 under single-leaf moves, the tested two-leaf moves, gate flips, one-literal insertion and leaf deletion (math-brain cards 37-39 in rows/T021). Seeding n = 19 with x18 unused keeps the ratio; the 416 moves that bring x18 in (68 new gate children, 232 leaf expansions and/or(l, +-x18), 116 leaf replacements) had 8 that go higher, best: leaf 30 (NOT x14, inside and(3, NOT x14)) -> x18, ratio 4.25086273921824, k* = 7, I = 0.0927887. Checked by q31_maxinf_n19_verify.py (own parser and evaluator on all 2^19 points). Card 40 local_agent_T021_n19_seed_one_leaf_to_x18_reaches_4_2508_20261103, edges 59-60; files rows/T021/exp/q31/q31_maxinf_n19seed*. Lesson for this row: a formula that is a local max under every edit at n is still improvable by adding a variable - growing n is a move, not a separate family. Status: record for one search, not a bound; T021 not solved. What would change it: the running steepest ascent from 4.25086 (pid 35760 on 3 Nov) or an n=20 seed.

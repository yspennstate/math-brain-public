---
name: swarm_s47_frontier_t373_t382_two_known_three_partial_none_resolved_2026_11_16
description: "[VERIFIED] Frontier swarm S47 (rows T373-T382, learning theory): what did the 10 audited briefs settle? None resolved; T373 retired (positive target false, negatives known: Vardi-Shamir-Srebro 2202.06233); T381 target 1 known (Christ survey ePrint 2026/2162); partial results T375 T376 T378; audits no wrong claim, 9 unchecked"
metadata:
  type: project
  created: 2026-11-16
  created_at: 2026-11-16T17:36:04+02:00
  status: provisional
  evidence: ""
---

S47 ran 16 Nov 2026 (an agent, Codex gpt-6.1-sol high, normal speed, a second machine); each brief finished in 10-20 minutes, each audited by a fresh Codex.

- T373 size-independent sample complexity: retire as stated; the positive target is false in unrestricted input dimension, the two negative targets are known (Vardi, Shamir, Srebro, arXiv:2202.06233, Theorem 1).
- T374 uniform convergence: the old random-features example subtask is known; the full row is not solved.
- T375 min-norm ReLU interpolants: exact four-site optimiser and risk formula for a weaker deterministic move; events of arbitrarily large risk with positive probability.
- T376 information-theoretic bounds: three narrower proofs (one-pass noiseless top-layer SGD on a rank-one ReLU net has maximal CMI while both risks vanish).
- T377 weak-to-strong: broad row known; a repaired narrower question stays open.
- T378 non-vacuous bounds: open; a probability-one counterexample to an omission in the source's Proposition 12.
- T379 calibrated hallucination: the natural bridge (type error zero implies no hallucination) is false; statement repaired.
- T380 self-supervised learning: open with a repaired question.
- T381 watermarks: target 1 known (Christ survey, ePrint 2026/2162, p.4).
- T382 linear-realizable RL: open; statement made precise.
Audits: no claim judged wrong, 9 unchecked. Files: 06_math_research/frontier/swarm_s47_20261116 (INDEX.md); full tree release swarm-s47-20261116/s47full.tgz (sha256 95d7e1df...).

How to apply: before queuing a learning-theory row, check the S47 report; a row marked known needs a new quantified target, not another literature pass. Links: [[swarm_s46_frontier_harvest_10_rows_no_wrong_claim_none_resolved_2026_11_16]].

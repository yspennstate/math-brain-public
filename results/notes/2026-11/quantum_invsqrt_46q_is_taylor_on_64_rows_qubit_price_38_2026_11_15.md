---
name: quantum_invsqrt_46q_is_taylor_on_64_rows_qubit_price_38_2026_11_15
description: "[PROVISIONAL] Quantum-compilation invsqrt: can we beat the public 46 qubits x 1710? The 46q build (syed3000 source) is quadratic Taylor on a 64-row table with width flat at the peak; a qubit is worth 38 Toff-eq, a rotations-instead-of-registers phase costs ~2800. Parked; the board gap is DQI/chem."
metadata:
  type: project
  created: 2026-11-15
  created_at: 2026-11-15T02:58:00+02:00
  status: provisional
  evidence: ""
---

status: provisional. Read 15 Nov from syed3000/vqcc-own-circuit-portfolio invsqrt_source (Apache-2.0; 64-row table ahoirg, angles atakan dcde70780434, HW-26 measure-outs manwithacat). Blocks (FA004 ledger): normalise 61, high phase 56 + 15 rotations, lookup 222, curvature/derivative/result 334, low phase 99 + 28 rotations, backward chain ~430, restore 61. Lemma A: dropping a qubit at D extra Toff-eq helps iff D < C/(Q-1) = 38.0 at the frontier. Lemma B: the linear phase term as rotations needs ~513 doubly controlled phases at 5.5 Toff-eq = ~2800, worse than the whole circuit. Detail: kaggle_lane/quantum/math_agent/INVSQRT_NOTES.md. What would change it: a construction whose width drops in EVERY region for under 38 Toff-eq each.

---
name: e0066_qbo_second_independent_audit_passes_2026_11_08
description: "[VERIFIED] Did the second independent E0066 audit pass? Yes, 8 Nov 13:10: PASS for correctness of the partial packet (A known, B C D correct, controls correct), not a full solution, novelty not established"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T13:20:19+02:00
  status: provisional
  evidence: ""
---

Second independent audit of the E0066 quadratic bistochastic operator packet (Codex gpt-6.1-sol high, brief AUDIT066B, written before it opened the first audit). Resumed in its own session after a network drop, with hooks off. Verdict: PASS for mathematical correctness of the partial packet. A (approach to one finite cycle) is KNOWN (Makhmudov Thm 2.1; Saburov 2016 Thm 3.1). B (two-type region, exact bound r=|B|+|A||z0|), C (state-dependent agreement, common positive permutation), D (unequal support-two orbits follow one coordinate permutation; three-type boundary period at most three) CORRECT under stated hypotheses; both controls correct; every original finite count reproduced with exact Fractions. NOT FOUND in the sources checked: the exact B rate over the whole square, the orbitwise-positive C wording, the general D statement - so novelty is open, not shown. Files AUDIT.md and REPORT.md on GitHub. Verdict sent to the author of the E0066 paper. Follows [[e0066_qbo_partial_first_independent_audit_passes_2026_11_08]].

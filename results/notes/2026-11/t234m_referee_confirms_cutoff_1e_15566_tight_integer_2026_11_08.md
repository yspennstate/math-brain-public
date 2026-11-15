---
name: t234m_referee_confirms_cutoff_1e_15566_tight_integer_2026_11_08
description: "Does the T234 cutoff alpha <= 1e-15566 survive an independent referee? (T234m) Yes, no wrong step; 15566 is tight (bound 9.987e-7 vs 1.00001e-6 at 15565); endpoint K constancy open"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T23:29:12+04:00
  status: verified
  evidence: "codex_fleet/20261108_pro/workers/OPEN-T234m REPORT.md, CONSTANTS_AND_CUTOFF.json; frontier T234"
  originSessionId: 81695323-627a-4240-9df2-cd66cd18fae9
---

OPEN-T234m (Codex gpt-6.1-sol high, independent referee, reviewed by an agent 8 Nov). The T234l cutoff holds. Every 0 < alpha <= 10^-15566 is captured for the fixed dyadic d = 40, n = 60 instance and seed. The referee found no wrong step in the five lemmas, within the IEEE model and the inherited trapping theorem. The integer is tight for this majorant: the real threshold is 15565.0080, the error bound at 15566 is 9.98747e-7 (under the 1e-6 allowance), and at 15565 it is 1.00001e-6 (over). Constancy of K at the endpoint is still open, and it is what separates this from a result for all alpha. Follows [[t234l_uniform_cutoff_alpha_le_1e_15566_relative_passage_constancy_open_2026_11_08]]. Frontier T234, folder open_t234m_independent_referee_2026_11_08 (41/41). Math card claim_a3fe9cfaf1a1467bb5b69b64f570cfd3.


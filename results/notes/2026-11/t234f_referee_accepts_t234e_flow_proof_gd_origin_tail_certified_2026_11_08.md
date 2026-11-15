---
name: t234f_referee_accepts_t234e_flow_proof_gd_origin_tail_certified_2026_11_08
description: "[VERIFIED] Yes, conditionally (8 Nov, T234f): an independent referee pass accepts T234e's ordered-limit flow proof; no invertible G is exceptional; GD step 1/20 has certified origin tails, capture open"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T13:20:13+04:00
  status: verified
  evidence: "OPEN-T234f REFEREE.md, SUMMARY.csv; t234f_check.py; pushed 7672b01369; card claim_41600f685d994dc5a60d367e26fe3c11"
  originSessionId: 81695323-627a-4240-9df2-cd66cd18fae9
---

Has T234e's proof survived an independent read? Yes (8 Nov, OPEN-T234f). A separate Codex worker refereed every numbered section and displayed estimate of T234e's PROOF.md and found no failed estimate and no missing interchange of limits. So, conditional on T234c/d's computer-assisted reference enclosures (which the referee did not reintegrate), on d=40, n=60, seed 60001 the ordered limit of gradient flow from alpha*G is the higher-trace rank-two interpolant for every G off the Gram-zero set.

The exceptional set is not a basin boundary. No invertible G lies on it: if (a v1 + b v2)^T G = 0 with (a, b) nonzero, G is singular. Starts on or near it do different things. Near the set (Gram determinant 1e-60), the distance to the generic endpoint goes 0.445, 0.098, 2.1e-3, 9.2e-7 at log(alpha) = -100, -400, -1000, -4000, a slow non-uniform approach. A pure v2 start recovers the planted x x^T (trace excess about 0). A pure v1 start stays at a rank-one minimum with residual 0.399.

GD at step 1/20, first piece: the origin-phase family over [1, 1+beta1/20) has certified negative-time tails and an outward-rounded forward enclosure to step 286 (radius 0.010). The isotropic enclosure stops there because it loses the phase-position correlation. Next is a phase Taylor model or subdivided phases, then discrete transport and outgoing-phase capture.

My check (an agent, t234f_check.py, own code): 1+beta1/20 = 1.047737435475 lies in their rational cover [1.047735, 1.04774], and 1+beta2/20 = 1.0436039 clears 1.0436. All 20 saved exceptional-set endpoints match their SUMMARY.csv to the printed digits down to 1e-6. Below 1e-10 the reference choice (their certified center against T234e's numerical endpoint) makes the difference. Not checked: REFEREE.md's derivations and the GD tail constants.

Files: brain-repo 06_math_research/frontier/T234/open_t234f_agent_11_08 and rows/T234/moves.jsonl (pushed 7672b01369); math card claim_41600f685d994dc5a60d367e26fe3c11.

Related: [[t234e_flow_shadowing_ordered_limit_rank_two_d40n60_2026_11_08]] - the theorem this referees


Later (8 Nov, T234g): the origin family is carried from step 286 to capture at step 26699 by a phase Taylor model - [[t234g_gd_origin_family_captured_rank_one_d40n60_2026_11_08]]

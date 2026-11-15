---
name: e0082_bridge_pattern_constant_paper_posted_2026_11_13
description: "[VERIFIED] E0082 Pitman-Tang OP 2.3 (bridge pattern E T_n ~ gamma_lambda n): paper posted 13 Nov - GitHub bridge-pattern-waiting-time 433f9f9, Zenodo 24195862; RG queued"
metadata:
  type: project
  created: 2026-11-13
  created_at: 2026-11-13T14:36:00+02:00
  status: provisional
  evidence: ""
---

Pitman-Tang Open problem 2.3 (exact asymptotics of the waiting time for a bridge pattern BR_{lambda,n} in simple random walk) is written up as its own paper, companion to first-passage-pattern-waiting-time (e4c5ae2).

Result: T_n/n => 1+F_lambda with F_lambda the first hit of lambda by the Slepian process B(t+1)-B(t); E T_n ~ gamma_lambda n, gamma_lambda = 1 + E F_lambda; gamma given by a series of determinant integrals from Shepp's formulas (Karlin-McGregor), remainder bounded by r_h^{floor((t+1)/2)}. Numerics: gamma_0 = 1.54388 +- 0.00019, gamma_1 = 2.41351 +- 0.00061 (an independent referee run gave 1.54387 and 2.41377). Also corrects PT eq. (2.3): 2^{-n}M^{-1}1 has entries pi_j / E T(A), not reciprocals of single-word waiting times.

Where: https://github.com/yspennstate/bridge-pattern-waiting-time (433f9f9, MIT, code+data), doi 10.5281/zenodo.24195862, ResearchGate queue ~/Downloads/career/researchgate_queue/q4/bridge-pattern-waiting-time (#15 in order). Sources: brain 06_math_research/referee_reports/2026-11-13/E0082A and E0082AR.

Forward-citation check before Zenodo: OpenAlex lists only 4 citing papers of Pitman-Tang (all Pitman/Tang follow-ups), arXiv search found nothing newer; Semantic Scholar was rate-limited (429). If a later solution turns up, the Zenodo record needs a new version, not a new DOI.

Related: [[e0082_pitman_tang_bridge_constant_refereed_minor_2026_11_13]] [[paper_from_refereed_result_check_agent_paper_claims_first_2026_11_13]]

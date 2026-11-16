---
name: cn0455_fle_ants_convergence_distance_two_ratio_of_products_2026_11_16
description: "[VERIFIED] FLE ants at distance two (Armfield-Mailler arXiv:2610.18453 Sec 1.2): W(n)/n converges a.s., every shortest path keeps a positive share; log(Q_i/Q_j) converges on any graph via h/(1-h) cancellation + pathwise 1/j^2 bounds; POSTED repo forward-loop-erased-ants-convergence, Zenodo 24277621"
metadata:
  type: project
  created: 2026-11-16
  created_at: 2026-11-16T11:52:32+02:00
  status: verified
  evidence: ""
---

CN0455 (Armfield-Mailler, The forward-loop-erased ants walk, arXiv:2610.18453 v1, Sec. 1.2 "Convergence of the process"): under their Theorem 1.1 (nest N, food F at distance two, k common neighbours), W(n)/n converges a.s.; every shortest path keeps a share lambda_i > 0, sum 1.

Proof (paper at papers_agent/cn0455/main.tex, 5 pp):
- Edge identities (their Lemmas 2.12-2.13, reproved: last exit from N; last step into F via symmetric Green kernel g(x,y)/pi_y): P(edge N-i) = W_Ni h_i / C, P(edge i-F) = W_iF (1-h_i)/C.
- Q_i = W_Ni W_iF: relative drift E[xi|F] = 1/C + g/Q_i, h_i cancels; the 1/C is the same for all i.
- Pathwise 1/j^2 bounds (each term paid by a real increment): sum xi^2 <= 3 pi^2/2 deterministically, E sum g/Q <= pi^2/6. So log(Q_i/Q_j) converges a.s. on ANY finite graph for common neighbours i, j. No growth lemma, no c0 from their Lemma 3.9, no rate for the off-S weights.
- Their Thm 1.1(a) makes Q_i ~ (W_Ni)^2, so s_i -> sqrt(rho_i)/sum sqrt(rho_l).

Method worth keeping: for a reinforced process, a product of two weights whose reinforcement probabilities carry complementary factors h and 1-h has a drift with the unknown hitting probability cancelled; bound martingale and remainder sums pathwise by charging each term to an actual increment (sum 1/j^2), which needs no growth rate at all. The advisor found the pathwise shortcut; my first sketch used a growth lemma resting on an unproved mirror of their Lemma 3.9.

Numerics (simulate.py, 30 s): identities vs 200k Monte Carlo walks within 1.4 s.e. on two graphs; log(Q_3/Q_2) settles by n=10^4 on 3 seeds x 2 graphs, limits differ by seed (random limit, law not determined).

Status (16 Nov, posted): two outside Codex audits (gpt-6.1-sol high, mini1 ~/aud_0cf7/cn0455a and cn0455b) both VERDICT SOUND, no mathematical MUST; fixes applied (k=1 endpoint (0,1], credit to Armfield thesis + Mailler-Varin arXiv:2601.22855, LP17 Exercise 2.1(e), softer simulation wording, path-frequency remark). POSTED: https://github.com/yspennstate/forward-loop-erased-ants-convergence @ 1c09906b77f0689e1c40c5484d3e2fa43c72fe25, Zenodo doi:10.5281/zenodo.24277621, open-problems-repo POSTED row 6d596cff. ResearchGate entry not yet made (RG edit limit). Public text never says CN0455.
What would change this: an error in Theorem 1.1 of the unrefereed v1 preprint (the result is deduced from it), or a later paper proving the convergence first.


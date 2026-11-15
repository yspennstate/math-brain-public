---
name: i0071_triangular_rd_transport_noise_paper_posted_zenodo_2026_11_13
description: "I0071 Agresti-Veraar Problem 7 (stochastic RD, triangular, transport noise): answered on the torus, Lipschitz zero-order noise; paper posted repo stochastic-reaction-diffusion-triangular-transport 41818d10, Zenodo 10.5281/zenodo.24203979; R^d, boundaries, superlinear noise open"
metadata:
  type: project
  created: 2026-11-13
  created_at: 2026-11-13T20:19:42+02:00
  status: verified
  evidence: "gh api repos/yspennstate/stochastic-reaction-diffusion-triangular-transport contents (main.pdf 433656 B, commit 41818d10, public); Zenodo record 24203979 md5 6b4a4890 = local md5sum of main.pdf; referee agent_run I0071AR MINOR"
---

I0071 (Agresti-Veraar survey NoDEA 32 (2025) art. 123, arXiv:2501.18561v5, Problem 7, published p.131) is answered on the torus and posted.

Paper: "Global solutions of stochastic reaction-diffusion systems with triangular structure and species-dependent transport noise", public repo yspennstate/stochastic-reaction-diffusion-triangular-transport, commit 41818d1048ff8da6c71c4f94079d90a49a27165d, 13 pp; Zenodo 10.5281/zenodo.24203979 (md5 6b4a48904fd169510777e967b3e92f02 = main.pdf).

What is proved: on T^d, d>=2, quasi-positive polynomial reactions with mass control and linear triangular control, globally Lipschitz zero-order noise vanishing on faces, arbitrary fixed species-dependent C^gamma transport under uniform stochastic parabolicity (2 nu_i|xi|^2 - sum_n |b_{n,i}.xi|^2 >= mu|xi|^2): the maximal local strong solution is global a.s., nonnegative, pathwise unique, C^{theta/2,theta}_loc on (0,inf). Method: mixed polynomial energy of Fitzgibbon-Morgan-Tang-Yin (arXiv:2103.16863) plus a stochastic covariance estimate that needs the small normalized off-diagonal Hessian entries; counterexample Phi=(y1+y2)^2/2 with b_1=e_1, b_2=-e_1 gives Q=-2.

Not proved, named open in the paper: R^d, bounded domains, superlinear g_i. Continuous dependence was dropped (survey Assumption 5.1 needs C^theta data with L^m moment, not verified).

Chain: claim run I0071, referee I0071AR MINOR (fixes applied: FMTY credit, stability dropped, FMT scope incl. R^d, Agresti-Kniely-Tang 2608.13332 Thm 3.4 cited), paper run I0071P. Ledger row PAPER_POSTED 2026-11-13T20:11. ResearchGate not yet (agent told).


14 Nov 04:13: independent post-posting referee pass by an agent (Opus 5.5), whole main.tex at 41818d1 hand-checked (Lemmas 3.1-3.2, Prop 4.1, Lemma 4.2, Lemma 6.1, Prop 6.2, Thm 2.1, Cor 6.3, Section 7 remarks): ACCEPT, two optional wording remarks, no correction. Report: 06_math_research/referee_reports/2026-11-14/I0071_posted_referee/REPORT.md. That is the second audit after Codex I0071AR.

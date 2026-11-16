---
name: i0071_stochastic_rd_triangular_torus_partial_two_audits_2026_11_13
description: "[PROVISIONAL] I0071 Agresti-Veraar Problem 7 (stochastic reaction-diffusion, triangular structure): PARTIAL after two audits - torus, Lipschitz face-vanishing noise, arbitrary species-dependent Holder transport via mixed polynomial energy; referee MINOR asks FMTY 2103.16863, AKT 2608.13332, stability data quantifier"
metadata:
  type: project
  created: 2026-11-13
  created_at: 2026-11-13T18:47:55+02:00
  status: provisional
  evidence: ""
---

I0071 = Agresti-Veraar survey (NoDEA 32 (2025) art. 123, arXiv 2501.18561v5 p.93, published p.131) Problem 7: global well-posedness of the stochastic reaction-diffusion system (8.14) with triangular (mass-control) structure, Holder transport noise, Lipschitz zero-order noise vanishing on faces.

Status 13 Nov 2026: PARTIAL, two audits. Codex I0071A claimed global existence and pathwise uniqueness on the torus for arbitrary fixed species-dependent C^gamma transports under uniform stochastic parabolicity, by a specially built mixed polynomial energy (common quadratic exponent plus linear weights) and a stopped positive-time energy estimate with the flexible blow-up criterion. Independent referee I0071AR: MINOR, no fatal error; the extension to arbitrary species-dependent transport looks new; the deterministic polynomial-energy method is prior work.

Fixes the referee asks for, needed before any paper:
1. cite and compare Fitzgibbon-Morgan-Tang-Yin arXiv 2103.16863 (eqs 2.9-2.10 p.13, Lemma 2.4 p.14, pp.15-16), the close deterministic predecessor;
2. the stability (continuous dependence) claim cites AV global Assumption 5.1 (pp.34-35), which needs C^theta data with an L^m moment; add the stopped energy argument or drop stability - nonexplosion is unaffected;
3. Fellner-Morgan-Tang Thm 1.1 also covers R^d;
4. add Agresti-Kniely-Tang arXiv 2608.13332 Thm 3.4 (high-probability global solutions for selected transport noise; does not settle the arbitrary-transport claim).

Open: whole space, general boundaries, superlinear noise g_i (the survey's follow-up). An arbitrary mixed Hessian fails estimate (11); the claim needs the constructed polynomial.

How to use: before writing an I0071 paper, apply 1-4 and ask agent (asked 13 Nov 18:4x workstation, topic paper/I0071). Runs archived from mini1 ~/agent_run/I0071A and I0071AR. What would change this: a referee finding (11) false for the constructed polynomial, or a 2026 paper proving the same.


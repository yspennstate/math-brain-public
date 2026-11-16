---
name: t278_t410_kernel_and_owf_gaps_2026_11_01
description: [PROVISIONAL] T278: 2302.09235's width rule forces NTK separability; T410: OWF gives AR KL gap -log eps_inv, order-dependent
metadata:
  type: project
  created: 2026-10-31
  created_at: 2026-10-31T22:17:01+04:00
  status: provisional
  evidence: ""
---

T278: Taheri-Thrampoulidis 2302.09235 Thm 5 (GD, gap 24 l^2 R^2 g^2/n, m >= 64 beta^2 L^2 R^4 g^4, beta = 1 for logistic; the beta glyph is lost in PDF text extraction, identified from Assumption 4). Width rule => the Taylor remainder at the reference point is <= 1/16 => NTK-separable with margin >= (log(T/n)-C-1/16)/g. So no non-NTK example exists in that framework. My first XOR count wrongly charged moved neurons for cancelling init (k(r^2+d)); the correct cost is k r^2. Note 15960892, move 874c0604. T410: (f(x),x) with f(x) first: KL(P||Q) >= -log eps_inv(poly) by chain rule + data processing on the preimage event + Jensen; reverse order exact. Lin et al. 2010.11939 has no KL/OWF result. Note 375b22ea, move 37ff049b. Same order-dependence theme as [[t399_path_star_first_step_globality_2l_minus_1_2026_11_01]]. Status: provisional (proofs unreviewed).

Folder: research-repo research_pushes/2026-11-01-t278-realizability-is-ntk, and research_pushes/2026-11-01-t410-owf-kl-gap for the T410 part

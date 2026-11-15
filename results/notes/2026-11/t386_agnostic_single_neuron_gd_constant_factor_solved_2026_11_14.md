---
name: t386_agnostic_single_neuron_gd_constant_factor_solved_2026_11_14
description: "[PROVISIONAL] T386 (agnostic single ReLU neuron, does GD reach C*OPT+eps?): yes - DKTZ 2206.08918 (regularized L2, log-concave) and Awasthi-Tang-Vijayaraghavan 2208.02711 (random init, Gaussian, moderate bias); REPLACE candidate. Same pass: T385 deep NTK bulk is Fan-Wang 2005.11879, T390 annealed SM polynomial (Qin-Risteski 2306.09332), T380 partly (Wen-Li)"
metadata:
  type: project
  created: 2026-11-14
  created_at: 2026-11-14T14:23:29+02:00
  status: provisional
  evidence: ""
---

Vetting pass 14 Nov (an agent, push 236 caec6357). T386 asked whether gradient descent from a random start reaches C*OPT+eps for a single ReLU neuron with agnostic labels under Gaussian marginals. Diakonikolas, Kontonis, Tzamos and Zarifis (arXiv:2206.08918, COLT 2022) prove GD on the regularized square loss is a constant-factor learner for monotone activations incl. ReLU under isotropic log-concave marginals (stationary points approximately optimal); Awasthi, Tang and Vijayaraghavan (arXiv:2208.02711) prove GD from random init reaches a constant factor for ReLU with moderate bias under Gaussians. Row marked solved; a REPLACE candidate for the top-200 list. Same pass: T385 st was wrong ('open for the deep bulk') - Fan and Wang 2005.11879 give the CK/NTK limiting spectra at linear width for approximately orthogonal inputs (spikes from uncentered activations still open). T390: annealed score matching polynomial for shared-covariance Gaussian mixtures (Qin-Risteski 2306.09332). T380: partly solved for sparse-coding models (Wen-Li 2105.15134, 2205.06226). Lesson: rows from the 16 Oct list with 'open as far as the writer knows' on 2020-22 problems often have 2020-22 answers; read the field's COLT/NeurIPS follow-ups before calling them open. status: provisional (abstracts read, papers not).

---
name: e0098_wigner_eigvec_min_coord_goe_classical_refereed_2026_11_13
description: "[PROVISIONAL] E0098 (O'Rourke-Vu-Wang survey p.13, min eigenvector coordinate universality): two audits PARTIAL; GOE Exp(sqrt(2/pi)) law is classical, Wigner open"
metadata:
  type: project
  created: 2026-11-13
  created_at: 2026-11-13T10:02:08+02:00
  status: provisional
  evidence: ""
---

E0098, from O'Rourke, Vu, Wang, Eigenvectors of random matrices: a survey (arXiv:1601.03678v3, p.13 after Cor 4.8): is the law of the minimum absolute coordinate of a Wigner eigenvector universal? Two audits (claim run E0098A, referee E0098AR MINOR, 13 Nov 2026). Proved: for GOE, n^{3/2} min_k |v_j(k)| -> Exp with rate sqrt(2/pi) (mean sqrt(pi/2)), plus a Poisson-process version, for every deterministic index sequence including the edges. The referee found this correct but classical: Haar eigenvector = normalised Gaussian vector plus iid extreme values (Rivin arXiv:math/0305252 pp.2-4; Resnick 1987 Prop 3.21 p.154), so it is no new GOE result. A planted-coordinate construction shows that Gaussian convergence of every o(n) coordinate set, even in total variation, does not imply the minimum law; it refutes that implication for random unit vectors, not for Wigner matrices. Open: universality for subgaussian atoms; one sufficient input is joint relative small-ball asymptotics at scale n^{-3/2}. Gaussian void probabilities alone would also suffice for the minimum. Not in print as of the referee's search (Luh-O'Rourke 1810.00489, Nguyen-Tao-Vu 1504.00396 Thm 3.3 checked). Ledger row in probability_1000_intake_E_20260908. Status provisional: worth a paper only with the Wigner case. Related [[d0025_site_disordered_k_exclusion_flat_flux]].

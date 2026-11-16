---
name: hull_of_endpoint_boxes_needs_a_monotone_branch_2026_11_12
description: "[VERIFIED] Certified fixed-point box over an alpha interval built as the hull of the boxes located at the two ends? Valid only if the branch is monotone in alpha; say why in the paper (Ising margin: P increasing, R linear in alpha, contraction => q*,psi* increasing)."
metadata:
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T11:10:24+02:00
  status: provisional
  evidence: ""
---

Ising perceptron margin paper, 12 Nov 2026. The second independent audit flagged two box widths at kappa=0.05: 1.9e-4 (intro, Section 7) and 5.2e-5 (Hessian section) in psi0. Recomputed from the release code: both right, different boxes. cert_hessian.py iterates q -> P(R(q,alpha)) over the whole alpha interval (q width 3.6e-6, psi 5.2e-5): an invariant box, valid for every alpha in the interval by construction. stage2_0p05.py and the dual-localization certificates take C.hull of locate_fp_bisect at the two alpha ENDS (q width 1.85e-6, psi 1.9e-4): valid for interior alpha only if q*(alpha) is monotone. The paper did not say so. The proof is one line: P(psi)=E tanh^2(sqrt(psi)Z) increases pointwise in psi; R(q,alpha)=alpha E[E(u)^2]/(1-q) is linear in alpha and increasing in q (Lemma dR); q*'(alpha)=P'(psi*)(R/alpha)/(1-(P o R)'(q*))>0 under the contraction; psi*=R(q*,alpha) increases with it. Staged as rewrite_v8.py after the third audit. How to apply: whenever a certificate encloses a parametric fixed point by the hull of endpoint enclosures, either prove monotonicity in the paper or switch to the invariant-box iteration. Neither box contains the other here (hull narrower in q, wider in psi), so you cannot just cite the other one. Related: [[perceptron_capacity_source_numbering_ding_sun_huang_nakajima_2026_11_12]].

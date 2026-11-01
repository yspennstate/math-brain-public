# C0044 exact target sent before proof details

For each fixed d>=3 and each fixed nonzero deterministic l in R^d, let P be a product law for identically distributed nearest-neighbor transition rows omega(x,.) on Z^d. Given omega, the quenched walk has transitions P_x^omega(X_{n+1}=z+e | X_n=z)=omega(z,e), |e|=1. Define A_l={lim_n X_n dot l=+infinity} and the annealed law P_0(.)=integral P_0^omega(.) dP(omega). Is P_0(A_l) always in {0,1}?

The exact intake source specifies (E), strict ellipticity: for each x, P(min_{|e|=1} omega(x,e)>0)=1, and (IID), independent identically distributed transition rows across sites. Countability gives an almost-sure all-sites version. The uniformly elliptic subclass (UE) additionally assumes one deterministic kappa>0 with omega(x,e)>=kappa almost surely; it is stronger than the target's (E). The source quantifies over unit directions l in S^{d-1}; allowing any fixed nonzero l is equivalent by positive normalization.

This is stronger than Kalikow's law P_0(A_l union A_-l) in {0,1}. It is an annealed probability question for each fixed direction, not a spatial Kolmogorov-tail claim and not a simultaneous assertion over all random directions.

Exact intake primary source: Alexander Drewitz and Alejandro F. Ramirez, Selected Topics in Random Walks in Random Environment, arXiv:1309.2589v1 (2013; source ID drewitz_ramirez_rwre_2014), Open question 3.2, PDF page 42; (IID) on PDF page 6 and (E)/(UE), Definition 2.3, on PDF page 7. URL: https://arxiv.org/pdf/1309.2589 . The source asks: "Consider a RWRE satisfying the assumptions (E) and (IID)." It then asks whether P_0[A_l] is in {0,1} for every unit direction. Supplement: Martin P. W. Zerner, ECP 12 (2007), introduction p.327, https://arxiv.org/abs/0706.0745 . Its proved directional theorem is planar.

Current openness: UNKNOWN. A search on 2026-10-10 found September/October 2026 manuscripts claiming an iid law and a stronger finite-range-dependent law. The official comparator theorem statement DirectionalWalk.lean ends in `by sorry`; that file alone is not a formal proof receipt. It does not refute the accompanying manuscript or a separate proof file. The actual complete proof and independent review have not been checked. The 2026-09-07 ranking only reports attempted_un and cannot certify current openness.

Independent adversary request: attack the exact target's assumptions or propose a sharp obstruction to a bridge. Keep a counterexample outside the iid class distinct from a refutation of C0044.

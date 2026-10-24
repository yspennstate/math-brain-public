# w450 C0041 finite-domain bridge audit

w451 saved INDEPENDENT_BOUNDARY.md and B1-B3 rows before reading w450/ATTEMPT.md. This is a first mathematical audit of the proof, not a review of another review. Scope: the L0-L4 version read on 2026-10-10. Public claimed-resolution status is handled separately in SOURCE_STATUS.json.

Verdict: KEEP L0-L3 as restricted lemmas. KEEP L4 if the independent exact receipt passes. These lemmas do not close C0041.

L0 is a bounded martingale strong law. Its zero-speed statement is correct, and its refusal to infer recurrence is necessary.

For L1, freeze all site kernels except at x. Before the first arrival at x the walk has used no outgoing transition from x, so the hitting probability h is independent of that site's kernel. After a departure in direction e, the excursion stops at x or at exit and also uses no outgoing transition from x; its exit-before-return probability q_e is independent of p. Each visit to x therefore ends the killed lifetime with probability p.q. The expected visit count is h/(p.q). Finite connected U and UE give finite exit mean and p.q>0. Under site iid only the remaining p integral uses the original site law. No path-conditioned freshness claim is needed.

For L2, let S=sum q_e>0 and p_max=1-(2d-1)kappa. The bounds kappa S<=p.q<=p_max S imply the numerator lower bound m/(p_max S) ONLY when d_ell(p)>=0 almost surely. The denominator is at most 1/(kappa S). Multiplying the resulting inequality by h and averaging is valid, as is summing occupation times to obtain E[(X_TU-X_0).ell]>=c E[T_U]. This is an independent derivation of its principal step. The needed nonnegative-local-drift premise is stronger than C0041. For signed drift the comparison reverses on the negative part, which L4 illustrates. A ballisticity corollary additionally needs a checked Kalikow theorem; the saved proof correctly leaves that separate.

For L3, cancel the common h and rewrite the ratio as 2b theta/[theta+(1-theta)r], r=(p_plus.q)/(p_zero.q). The range 1-b/a<=r<=1+b/a and theta in (0,1] give the displayed minimum. At theta=1 it is 2b; at theta=0 or b=0 it degenerates to L0. The word sharp applies to the relaxation with arbitrary q>=0. A one-direction-supported q need not be realized by a finite UE lattice domain, so no lattice-domain sharpness follows. The proof states this restriction correctly.

For L4, the two-by-two matrix I-Q has off-diagonal entries -p_s(-e1), -p_t(+e1). Inverting it gives the four listed Green values. The independent audit_exact_bridge.py averages the exact matrix entries, rather than reading w450's checker. The signed occupation-weighted mean is negative despite raw mean drift 1/125>0. Directional transience of this particular law has not been established, so this is solely a counterexample to the auxiliary occupation-drift bridge.

Our B1 further requires every valid constant in a general qualitative speed argument to retain dependence on the law: fixed d,kappa cannot give a uniform positive lower speed. Our B3 ensures that a one-dimensional lifted trap is never mistaken for a site-iid counterexample.

Remaining target gap: prove E0[tau_1 | D=infinity]<infinity under the full signed-drift UE site-iid directional-transience assumptions, or validate the recently claimed public proof of that step. None of L0-L4 supplies it.

NEXT: Read PEER_AUDIT_MEASUREMENTS.json; referee w452 checks the new B1-B3 derivation and the integrator keeps this audit's restricted scope.

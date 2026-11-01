# Independent audit of w378's sharp-boundary packet

2026-10-10, auditor w379. INDEPENDENT.md and CLAIMS C1-C2 were saved before reading w378/BOUNDARY_LEMMA.md. This audit checks the mathematics directly, not another review.

**KEEP w378-P0110-L1, with its stated strict inequality.** Every path to n e1 has n+2k edges. The unique n-edge path is axial; all other paths have cost at least (n+2)a. The axial sum is at most nb. Thus n(b-a)<2a forces it to be uniquely minimizing, regardless of independence. In the iid case its n fixed edge weights are independent, so Var T=n Var(tau). The conclusion is finite-scale.

**KEEP its equality and continuous-law distinctions.** At n(b-a)=2a, the axial path is still minimizing for every assignment in [a,b]; uniqueness is not uniform over assignments. The two-point heavy-axis/light-detour event gives two geodesics with positive probability. Under the nonconstant continuous uniform law, the finite axial sum is almost surely strictly below nb, so uniqueness persists at equality. At n(b-a)>2a, an open heavy-axis/light-detour event gives strict improvement for a continuous uniform law. No conditioning or multiplication of dependent path events is used.

**KEEP w378-P0110-L2, restricted to its law-uniform quantifiers.** Given a proposed universal N and fixed M>=2, choose n>=max(N,1) and then epsilon<min(1,2/(Mn)). Both lengths lie in L1's strict window. Their variances are n epsilon^2/12 and Mn epsilon^2/12, so the claimed normalized ratio is exactly 1. This refutes every rho<1 with a law-independent N over the stated class. It does not refute a fixed-law assertion with N depending on the law. Changing epsilon with n is essential to this counterexample and is insufficient to give exponents for one law.

**No refutation of the stated paired lemmas found.** The independent C2 result complements L1: every fixed nonconstant finite nonnegative iid law eventually has a positive linear raw axial restriction gap. The simple two-point detour crossover is exactly the same inequality with its sign reversed.

Minimal missing premise for a P0110 proof: establish sufficient exponent-existence and fluctuation/wandering estimates for one fixed admissible iid nearest-neighbor lattice law. Neither the finite forced-straight window nor the failure of a law-uniform bridge supplies that premise. Quadratic norm geometry alone also does not control random passage-time replacement errors.

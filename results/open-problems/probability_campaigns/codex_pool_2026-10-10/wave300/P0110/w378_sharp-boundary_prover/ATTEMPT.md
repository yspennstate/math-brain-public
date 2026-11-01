# P0110: sharp support-width boundary and a failed uniform bootstrap

2026-10-10, author w378; referee w380; adversary w379. Original target unsolved by this packet; current external openness UNKNOWN. The new statements below are author-proved special cases with independent review pending. Novelty is not claimed.

## Exact target and route

The source is Auffinger-Damron-Hanson, arXiv:1511.03262v2, Question 22, Section 4.3, printed pp. 88-89, equation (4.19): exhibit a passage-time distribution for which chi=2 xi-1 holds. The model is iid ordinary undirected nearest-neighbor lattice FPP in dimension d>=2. See STATEMENT_FOR_ADVERSARY.md for the statement-only packet, sent first to w379 (mesh receipt msg-28005cf9d5). Do not replace the existential law quantifier with universality over laws. Do not add the planar numerical values 1/3 and 2/3 to the task.

A precise sufficient route uses Chatterjee's Theorem 1.1, arXiv:1105.4566, printed pp. 3-4. With T=T(0,v), D the maximum Euclidean deviation of the unique geodesic from the endpoint segment, and |v| Euclidean norm, define

- chi_a = inf{c: for every c'>c some alpha>0 has sup_(v!=0) E exp(alpha |T-ET|/|v|^c') < infinity}.
- xi_a = inf{c: for every c'>c some alpha>0 has sup_(v!=0) E exp(alpha D/|v|^c') < infinity}.
- chi_b = sup{c: for every c'<c some C>0 has inf_(|v|>C) Var(T)/|v|^(2c') > 0}.
- xi_b = sup{c: for every c'<c some C>0 has inf_(|v|>C) E D/|v|^c' > 0}.

The cited theorem, for iid nearly-Gamma weights with a moment generating function near zero and d>=2, gives the KPZ identity when chi_a=chi_b and xi_a=xi_b. This is a conditional theorem used as a route, not a theorem proved anew here. The infima/suprema involve all lattice vectors, not just the axial sequence.

## Prior-attempt digest and boundary ownership

The 2026-09-07 ranking row is tier 5, attempted_un. Its raw rank-sheet row is clipped. The full matching math-store export record is claim_a60b9dcbea1c3b4133831211a8107b42fbce24f2c59d8b4b21ede96b3cab07f1, explicitly an unverified concept without independent review. Its calculation is the curvature balance n*(n^(xi-1))^2=n^(2xi-1); changing curvature power to kappa changes the exponent to kappa xi-(kappa-1). The record itself leaves exponent existence and control of replacing random passage times by the deterministic norm open. The balance is not a proof of stochastic scale matching.

Targeted P0110 searches in the named H/I attempts found no matching target row; the Lean campaign supplied a ranking entry, not a checked FPP theorem. Team O lists related shape/curvature/fluctuation problems but no P0110 ownership entry. This lane claims only a support-width boundary and the distribution quantifier of a strict variance bootstrap, leaving the other P0110 approaches' computations separate.

The recall scar fpp_base_case_is_doubling_transfer_principle_2026_08_15 warns that a continuity base case can demand the same variance-ratio control as the original obstacle. The perceptron_proof_open_gaps_fleet_2026_07_12 scar requires naming the unchecked piece even after computational checks pass. The owner's solved width-3 directed strip time constant is a different model and does not certify the present target. Basu-Sidoravicius-Sly 2604.01214 is a rotationally invariant Riemannian model; its 2026 variance upper bound is not a matching-exponent theorem for an iid lattice law.

## Concrete candidate and proof attempt

Fix d=2 and F=Uniform[1,5/4] once and for all. It is nondegenerate, continuous, bounded away from zero, and has every exponential moment. It also meets the nearly-Gamma density condition: for general F=Uniform[1,1+epsilon], h=1/epsilon and Phi'(Phi^(-1)(H(y)))<=1/sqrt(2 pi)<=A sqrt(y) h(y) with A=epsilon/sqrt(2 pi), since y>=1. Thus the weight-law hypotheses of the sufficient route are satisfied.

For any fixed endpoints, compare with an axial-coordinate path of length |v|_1 and cost <=(5/4)|v|_1. Every potentially minimizing path then has bounded length, since each edge costs at least 1. There are finitely many such paths, so a geodesic exists. Positive weights remove loops. Distinct simple paths use different edge sets; condition on all but one edge of their symmetric difference to see that equal costs have probability zero. A countable union over path pairs gives almost sure uniqueness, simultaneously for all lattice endpoint pairs. D is consequently unambiguous for this candidate.

Apply L1 in BOUNDARY_LEMMA.md. For n<8, the axial path is deterministically unique; at n=8 it remains almost surely unique because its Uniform-weight sum is strictly below the upper endpoint n(5/4). Thus for 1<=n<=8,

E T(0,n e1)=9n/8, Var T(0,n e1)=n/192, D(0,n e1)=0 almost surely.

This finite regime cannot continue by the same comparison. At n=9, put each of the 9 axial edges in [5/4-1/160,5/4] and each of the 11 edge-disjoint parallel-detour edges in [1,1+1/160]. The first route costs at least 1791/160, while the detour costs at most 1771/160. Independence is used only for these 20 distinct edges, giving event probability exactly (1/40)^20>0. Hence the straight path is strictly suboptimal on a positive-probability event. Outside edges need no conditioning.

What the candidate establishes: all weight-law hypotheses, existence and uniqueness of geodesics, and an exact short-scale regime. What it does not establish: any matching asymptotic chi_a/chi_b or xi_a/xi_b. A finite number of axial vectors cannot decide the uniform asymptotic definitions.

## Sharp obstruction to the proposed bridge

An appealing auxiliary statement is: for fixed M>=2 and rho<1, a single N works for every bounded continuous nondegenerate iid law, with V_F(Mn)<=rho M V_F(n) for every n>=N. L2 in BOUNDARY_LEMMA.md refutes this quantifier order even for laws supported in [1,2]. Given n, choose epsilon<2/(Mn); both passage times are exact iid sums, so V_F(Mn)/(M V_F(n))=1.

The surviving statement permits N=N(F). The counterexample changes F when n changes. It therefore neither refutes a contraction for one fixed law at large scales nor settles P0110. In particular, it cannot justify chi=1/2 or xi=0 for a fixed near-deterministic law.

## Exact check and single remaining gap

Command: python -X utf8 verify_boundary.py. The fresh gate allowed one process, no GPU/network, at most 8960 configurations and 30 seconds. The run checked 8704 exact two-point-weight ladder configurations and 266 tube-geometry identities in 0.084586 seconds; all checks passed. Its normalized variance ratio is exactly 1. Rational integration separately gives Uniform[1,5/4] variances V_2=1/96 and V_4=1/48. These are sanity checks of the finite boundary, not a formal certificate or evidence for an asymptotic exponent.

The single hardest unresolved piece is to prove compatible large-scale upper and lower fluctuation and wandering exponents, uniformly in lattice direction, for one fixed admissible law such as Uniform[1,5/4]. No presently proved step here bridges the exact short-scale regime to those matching exponent hypotheses. Independence of the original edge variables does not authorize multiplying probabilities of events defined by a shared optimizing geodesic.

NEXT: Independently check L1/L2 and the equality/sharpness witnesses; pursue only a fixed-law large-scale bound with its threshold allowed to depend on that law.

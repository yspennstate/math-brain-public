# C0044 independent adversary checkpoint

Saved 2026-10-10 before opening the paired prover's proof. Worker w586; mathematical referee w587. Requested model settings are not served-model evidence; none is available here.

## Exact target and source status

Let d >= 3, E = {+/-e_i: 1 <= i <= d}, and Omega = (probability vectors on E)^(Z^d). Let P be a product law whose rows omega(x,.) are identically distributed and strictly elliptic: P(omega(x,e)>0 for every x,e)=1. In the fixed sampled environment, P_0^omega is the nearest-neighbor Markov-chain law starting at 0 with transition probability omega(x,e) from x to x+e. Write P_0 = integral P_0^omega dP. For each fixed deterministic l in S^(d-1), A_l = {lim_n X_n dot l = +infinity}. C0044 asks whether P_0(A_l) belongs to {0,1} for every such law P and every such fixed l. There is no uniform ellipticity or moment hypothesis in this target formulation. A uniform ellipticity hypothesis gives a smaller subclass.

Primary background: Daniel J. Slonim, Directional transience of random walks in random environments with bounded jumps, ALEA 21 (2024), pp. 701-724, introduction and Section 2; https://alea.impa.br/articles/v21/21-27.pdf. The article distinguishes the union law from the missing exclusion of two signs. Its d=2 theorem does not cover this target.

Current openness is UNKNOWN. A newly located public preprint and Lean scope note in openai/math dated September 23, 2026 claim this target; their actual mathematical assumptions and proof have not yet been checked. An old attempted_un ranking cannot settle this conflict. No novelty or parent-problem solved claim is made.

## Independent obstruction O1: conditional independence does not survive environment averaging

Choose any d >= 3. Independently at each x, choose W_x equal to 1/4 or 3/4 with equal probabilities. Set omega(x,+e_1)=W_x and omega(x,e)=(1-W_x)/(2d-1) for every other nearest-neighbor e. This is iid and uniformly elliptic with lower bound 1/[4(2d-1)]. Start two walks X and Y at 0, independent conditional on the SAME environment.

For F={X_1=e_1} and G={Y_1=e_1}, quenched independence gives P_0,0^omega(F intersect G)=W_0^2. Consequently P_0,0(F)=P_0,0(G)=1/2, but P_0,0(F intersect G)=E[W_0^2]=5/16, whereas P_0,0(F)P_0,0(G)=1/4. The gap is 1/16. Also P_0,0(G | F)=(5/16)/(1/2)=5/8, not 1/2.

Thus iid environment rows and conditional-on-environment independent walks do not justify multiplying their annealed probabilities when they query the same row. This is a counterexample to that inference under the exact iid uniform-ellipticity hypotheses; it is NOT a counterexample to the directional zero-one law. For adaptive paths, an unqueried site's row may retain its original iid law, but this must be established from the actual revealed sigma-field. Shared or already queried sites require posterior conditioning or another argument.

## Independent reduction O2: the sign-exclusion gap

A_l and A_-l are disjoint. If the known union law P_0(A_l union A_-l) belongs to {0,1} is available, the target for this fixed l is equivalent to ruling out P_0(A_l)>0 AND P_0(A_-l)>0. A union probability of 1 only gives two probabilities summing to 1. It does not select a sign. The single hardest missing piece is exclusion of coexistence of the two signs in the iid target class, not the union law, ellipticity, or a source hash.

## Independent bridge O3: the quenched martingale is valid; an invariant law is an extra premise

Saved before opening the full w585 proof (only its statement packet and lane status have been read). Define theta_x omega(y,e)=omega(x+y,e), eta_n=theta_{X_n}omega, and h(omega)=P_0^omega(A_l). The event A_l is invariant under deleting any finite path prefix and translating the remaining path by any fixed vector. Thus the quenched Markov property gives h(eta_n)=E_0^omega[1_{A_l}|sigma(X_0,...,X_n)]. This is a bounded, uniformly integrable martingale and converges to 1_{A_l} by upward convergence of conditional expectations. Finite-region measurability of h is NOT needed. Infinite-region dependence obstructs some iid/tail arguments, not this martingale identity.

There is a valid conditional bridge: assume in addition that the environment-seen-from-the-walk kernel Rg(omega)=sum_e omega(0,e)g(theta_e omega) admits an invariant probability Q absolutely continuous with respect to P. This extra existence assumption is not supplied by iid strict ellipticity.

First Q is equivalent to P. With f=dQ/dP, shift invariance of P and invariance of Q give f(omega)=sum_e omega(-e,e)f(theta_{-e}omega) P-a.s. Since the summands are nonnegative and the weights strictly positive, the zero set Z={f=0} is included modulo null sets in every shift of itself. Shift invariance of P turns each inclusion into equality modulo null sets. The iid product law is ergodic under lattice shifts, so P(Z) is zero or one; integral f dP=1 excludes one. Therefore f>0 P-a.s.

Next Rh=h. Jensen gives Rh^2-h^2=sum_e omega(0,e)(h(theta_e omega)-h(omega))^2 >=0. Integrating under invariant Q makes its integral zero. Strict ellipticity and Q equivalence to P imply h(theta_e omega)=h(omega) P-a.s. for every nearest-neighbor e, hence h is P-a.s. constant by shift ergodicity. The quenched martingale limit is an indicator, so this constant is 0 or 1. This proves the target conditionally on Q's existence, not in the full target class.

The concrete density bridge: let f_n be the P-density of the law of eta_n, started with eta_0~P, and fbar_N=(1/N)sum_{n=0}^{N-1}f_n. If the FAMILY {fbar_N} is uniformly integrable in L1(P), weak L1 compactness gives a subsequence with limit f>=0 and integral f dP=1. The adjoint R* is an L1 contraction and R*fbar_N-fbar_N=(f_N-f_0)/N has L1 norm <=2/N. The weak limit therefore satisfies R*f=f and supplies Q. The essential missing premise is the uniform integrability of the entire family, not merely integrability or total mass one of each member.

Abstract obstruction to a free UI step: on iid Bernoulli(1/2) variables B_1,B_2,..., f_n=2^n 1_{B_1=...=B_n=1} has expectation one for every n and is a nonnegative martingale. For almost every sample it is eventually zero, so its Cesaro averages converge to zero almost surely while retaining expectation one. Uniform integrability of those averages would force L1 convergence and expectation zero, a contradiction. This does not realize a counterexample RWRE: it only refutes the implication 'probability densities of mass one automatically have uniformly integrable Cesaro averages'.

Review status: independent derivations saved; w587 review pending. Next: read the actual w585 density proof and check whether the UI and invariance premises are explicit; preserve that gap in the review packet.

# Bad coordinate persists in the all-small-influence regime

Own deduction, no novelty claim. Independent review pending. This extends the rare-switch checkpoint; it concerns one bad coordinate, not every coordinate.

Fix any tau>0. Choose an odd r=2l+1>=3 such that alpha=binom(2l,l)/2^(2l)<=min(tau,1/2). This is possible: alpha=product_{j=1}^l(1-1/(2j)) <= exp(-sum_{j=1}^l 1/(2j)) <=1/sqrt(l+1). Let G be majority on r uniform sign bits. It is balanced; every physical influence is alpha. If a chosen input v is fixed to +1 or -1, then E[G+]=alpha and E[G-]=-alpha. Indeed G is monotone, E[G]=0, and E[(G+-G-)/2]=Inf_v(G)=alpha.

Let F_m(x,z) be the rare-switch Boolean function of BRIDGE_CHECKPOINT.md, for m=2k, k>=1. Replace all m+1 inputs by independent, disjoint copies of G, forming f_m=F_m(G_1,...,G_m,G_0). Disjointness is essential. Each physical influence is Inf_j(F_m)*alpha <=alpha<=tau. To verify the product, condition on all other blocks: changing a bit in block j changes the output exactly when that bit changes G_j and the outer function is pivotal for j. The outer pivotality event depends only on the other blocks, so the two events are independent. The selected physical bit v in block G_0 has influence t=alpha/N, N=2^m.

Write epsilon=N^-1/2. The outer decomposition is F_m=A(x)+z B(x), with Ahat(S)=sigma_S epsilon-epsilon^2 and Bhat(S)=epsilon^2. The sigma_S are signs from the bent function. For a Fourier index U in the m other gadget blocks, let S be its set of nonempty blocks. Since G is balanced and the blocks are disjoint,

Ahat'(U)=c_U Ahat(S), Bhat'(U)=c_U Bhat(S),
c_U=product_{j in S} Ghat(U_j), and sum_{U: active blocks S} c_U^2=1.

The last equality is Parseval on each balanced gadget and finite factorization on independent product blocks, not a multiplication of dependent conditional estimates.

Consider only the Fourier indices whose remaining selector-block coordinates are empty after splitting on v. The two restriction coefficients are c_U(Ahat(S)+alpha Bhat(S)) and c_U(Ahat(S)-alpha Bhat(S)). Their marginal is R_U=c_U^2(Ahat(S)^2+alpha^2 Bhat(S)^2); their coordinate probability is q_U=alpha^2 Bhat(S)^2/(Ahat(S)^2+alpha^2 Bhat(S)^2) whenever c_U!=0. As epsilon<=1/2,

Ahat(S)^2 >=epsilon^2/4, so q_U<=4alpha^2/N<=1/N.

This sector alone contributes at least

sum_U R_U h(q_U) >=sum_U alpha^2 c_U^2 Bhat(S)^2 log2(N)
=alpha^2 m/N.

The exact entropy identity gives Delta_v(f_m)>=B_v(f_m), and therefore

Delta_v(f_m)/Inf_v(f_m) >=alpha m.

Since alpha is fixed after tau is chosen and m tends to infinity through the even integers, no dimension-free arbitrary-coordinate restriction bound holds even on the class in which all individual influences are <=tau. The construction is Boolean throughout. No monotonicity, universal badness over all coordinates, or counterexample to FEI is asserted.

NEXT: Referee must check the disjoint-block factorization and the empty-selector Fourier sector; then use this lemma only to block an arbitrary-coordinate lift of the brain's small-influence reduction.

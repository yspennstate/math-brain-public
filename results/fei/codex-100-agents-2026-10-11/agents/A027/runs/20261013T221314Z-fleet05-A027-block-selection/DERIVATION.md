# Arbitrary-controller partial-core transport

Let a=1-2c be any Boolean controller on a uniform cube disjoint from a Boolean core u. Put p=Pr(a=-1), d=Pr(u=-1), V=4p(1-p), b=1/ln(2), eta(t)=t log2(1/t), E(t)=eta(t^2), phi(d)=E(1-2d). Entropies are bits. For every finite physical core-only restriction tree with actual leaf weights w, write Pi_H and Pi_I for the entropy decrement and queried influence. Controls remain unqueried. A proper tree leaves at least one physical core coordinate unqueried on every path; the identity below also holds without that requirement.

The exact identity independently obtained from the coefficients is

    H(F)=p H(u)+d Hplus(a)+R(p,d), F=1+c(u-1),
    R(p,d)=4d(1-d)eta(p^2)+2d(1-d)V+V E(d)+phi(pd)-p phi(d).

For nonempty core sets S and arbitrary control sets T, Fhat(S,T)=uhat(S)chat(T). For empty core and nonempty control T, Fhat(empty,T)=d ahat(T); the global constant is 1-2pd. Since sum chat(T)^2=p and raw controller-indicator entropy is eta(p^2)+Hplus(a)/4+V/2, summing these rows proves the display. This reconstructs the identity in A028 stage 2, section 1, and keeps the exceptional constant coefficients.

Because sum w d_leaf=d, the potentially arbitrarily large controller entropy cancels EXACTLY from the core-only decrement:

    Pi_H(F)-p Pi_H(u)=R(p,d)-sum w R(p,d_leaf).
    Pi_I(F)=p Pi_I(u).

This cancellation does not remove controller entropy from terminals. Their total influence is p sum w I(u_leaf)+d I(a), reserving all physical controller influence separately from queried core influence.

Here is a uniform bound with no controller certificate. On [-1,1], E is C^1 (including zero) and |E'|<=2b. Indeed E'(t)=-2bt(ln(t^2)+1); on [0,1], the largest positive value is 4b exp(-3/2)<2b and the negative magnitude is at most 2b. Hence |phi'|<=4b. Also eta(p^2)<=2bp(1-p), by -ln p <= (1-p)/p, continuously at endpoints. Differentiate R in d. Its four contributions have absolute bounds 8bp(1-p), 8p(1-p), 8bp(1-p), and 8bp. Therefore

    |partial_d R(p,d)|<=p(8+24b), for every p,d in [0,1].

At p=0 or 1, R identically vanishes, so both endpoints are covered directly. The continuous derivative argument also covers d=0,1/2,1.

At a core query, the two child negative probabilities satisfy |d_0-d_1|<=Inf_i(u_node), by coupling along the queried physical edge. The conditional expected absolute martingale increment is |d_0-d_1|/2. The triangle inequality along paths yields sum w |d_leaf-d|<=Pi_I(u)/2. Consequently, for EVERY controller and core and actual finite core-only tree,

    |Pi_H(F)-p Pi_H(u)| <= kappa Pi_I(F),
    kappa=4+12/ln(2)<22.

The strict rational comparison follows from ln2>=56/81: kappa<=299/14<22. This improves the previous point-controller constant 12+8/ln2 and removes the point-controller hypothesis. No controller H/I assumption enters this transport estimate.

For terminal-inclusive selection, suppose the specified proper core tree has Pi_H(u)<=K Pi_I(u) and its ACTUAL activated leaves F_leaf have H(F_leaf)<=L I(F_leaf). Then H(F)<=max(K+kappa,L)I(F), by the disjoint queried/terminal budgets. One sufficient terminal certificate is H(a)<=K_a I(a) and H(u_leaf)<=K_l I(u_leaf) uniformly: A028's independently reconstructed scalar bias estimate (section 2) gives L=max(K_a+6,K_l). Alternatively actual certified regular activated leaves may be used directly. Arbitrary controller entropy must not be silently declared regular or paid already. In particular u identically -1 gives F=a, zero core-query budget, and terminal entropy H(a).

For a character/core block u=chi_[t] g, querying only the t>=1 character bits (leaving g on at least one coordinate) gives Pi_H(u)=0 and Pi_I(u)=t. The arbitrary-controller activation has complete path rate kappa, with controller/core terminal certificates still explicitly needed. This is a transport application, not a proof that arbitrary controllers or arbitrary residual g satisfy FEI.

First unsupported universal line: every Boolean core admits a proper partition with bounded Pi_H/Pi_I AND uniformly certified activated terminal entropy, without assuming FEI for an arbitrary controller or arbitrary residual core. The new cancellation supplies neither certificate nor universal selection. Shared physical support between a and u is excluded: there the tensor spectrum and p-weighted terminal identity fail.

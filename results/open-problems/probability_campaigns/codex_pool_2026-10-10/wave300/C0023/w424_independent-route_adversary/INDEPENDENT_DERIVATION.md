Independent derivation, saved before opening w423's proposed proof.

Target scope: independent nearest-neighbour Bernoulli bond percolation on Z^d, 3 <= d <= 10, with theta_d(p)=P_p(|C(0)|=infinity) and p_c(d)=inf{p:theta_d(p)>0}. Prove theta_d(p_c(d))=0. The local ledger is C0023; Duminil-Copin--Kozma--Tassion, arXiv:1902.03207v2, Conjecture 1 and section 2 confirm the exact bond model. This document makes no October 2026 novelty or resolution claim.

Method boundary: the recorded C0023 attempt uses half-space gluing, and G0001 uses finite-cluster tails. My route instead tests whether finite-generation exploration and moment control can exclude a critical jump. The following exact obstruction shows that product measure, finite energy, bounded degree and polynomial finite-volume probabilities do not suffice by themselves. The counterexample is a nontransitive tree, not Z^d.

Let T be a rooted tree where each vertex in generation k-1 has b_k children, k>=1, with b_k=8 when k is a power of 2, and b_k=2 otherwise. The root has degree 8 and every other vertex degree at most 9. Declare all edges independently open with probability p. Let Z_n count the vertices at generation n connected to the root, Z_0=1. The event {Z_n>0} is a finite increasing cylinder event; these events decrease with n.

Conditional on the explored generations through n-1, Z_n is the sum of Z_{n-1} independent Binomial(b_n,p) variables. This conditional independence follows from disjoint, previously unexposed tree edges; it is not inferred merely from conditional mean zero.

Set M_n=E_p Z_n. Then M_n=(2p)^n 4^{a_n}, where a_n=1+floor(log_2 n), n>=1, counts the powers of 2 at most n. In particular 4^{a_n}<=4n^2. For p<1/2, P_p(Z_n>0)<=M_n<=4n^2(2p)^n tends to zero. Thus the root does not percolate below 1/2.

At p=1/2, write Q_n=E[Z_n^2]/M_n^2. The exact conditional second-moment recursion gives

Q_n=Q_{n-1}+1/(b_n M_{n-1}), Q_0=1.

For every j>=0, the block k=2^j,...,2^(j+1)-1 contributes exactly

1/(8*4^j)+(2^j-1)/(2*4^(j+1))=1/(8*2^j)

to the sum of increments. Therefore Q_n<=1+sum_{j>=0}1/(8*2^j)=5/4. Cauchy--Schwarz applied to Z_n 1_{Z_n>0} gives P_{1/2}(Z_n>0)>=1/Q_n>=4/5. Continuity of probability for decreasing events and local finiteness of T show that theta_T(1/2)>=4/5. Hence p_c(T)=1/2 and theta_T(p_c(T))>=4/5.

This is a separately derived elementary instance of the known nontransitive-tree phenomenon, not a new theorem about transitive graphs. Its use is adversarial: any proposed proof using only the properties T shares with the bond product measure must fail somewhere. A lattice proof must explicitly use and justify an additional geometric estimate; the tree does not refute such an estimate when transitivity or Z^d geometry is actually used.

The order of limits is quantitatively visible. If p_n=1/2-delta_n<1/2 and delta_n n -> 0, then

P_{1/2}(Z_n>0)-P_{p_n}(Z_n>0)<=delta_n n/p_n.

To prove this inequality, apply the finite-product Russo formula to A_n={Z_n>0}. On A_n, every open pivotal edge belongs to any chosen root-to-generation-n path, so there are at most n open pivotals. Since an edge's pivotal status is independent of its own state, sum_e P_p(e pivotal)=E_p[number of open pivotals]/p<=n/p. Integrate over [p_n,1/2]. Thus P_{p_n}(Z_n>0)>=4/5-delta_n n/p_n, which does not tend to zero. The crude first-moment exponential bound at subcritical p cannot be made compatible with this very narrow continuity window.

The hardest remaining lattice piece is a parameter-and-scale estimate that rules out a positive infinite-volume jump while respecting this order of limits. Merely invoking continuity for each fixed scale, finite energy, or a subcritical result whose constants depend on p does not supply it.

Status: proof written; independent check by w425 requested in the local review packet and not yet obtained. Numerical checks will validate the recursions and example only. They will not count as a proof of C0023.

# C0036: sharp two-site case and finite necessary bounds (proof, pending w347)

Let Q be a Hermitian two-site equivariant positive contraction. Write its diagonal entries as a and its off-diagonal modulus as r; 0<=a-r<=a+r<=1. Put d=a^2-r^2=det Q and p=sqrt(d). Its determinantal measure has probabilities P(11)=d, P(10)=P(01)=a-d, P(00)=1-2a+d.

It stochastically dominates Bernoulli(p) on two sites. All nontrivial increasing events are: site 1 present; site 2 present; both present; at least one present. Their probabilities are respectively a,a,d,2a-d. The product probabilities are p,p,p^2,2p-p^2. Since p<=a and p^2=d, all four comparisons hold. This works at spectral endpoints as well. Applying the same argument to I-Q and complementing gives the upper bound Bernoulli(1-sqrt(det(I-Q))). The constants are optimal, by the both-present and both-absent events.

For any finite transitive equivariant contraction on N sites, an iid lower domination density b necessarily satisfies b^N<=det Q, hence b<=det(Q)^(1/N). An iid upper domination density c necessarily satisfies (1-c)^N<=det(I-Q), hence c>=1-det(I-Q)^(1/N). This proves necessity, not general sufficiency. Equivariance is needed to identify these determinants' Nth roots with the finite-group Fuglede-Kadison determinant (normalized trace).

Earlier-route check: Q=[[1/2,1/4],[1/4,1/2]] has eigenvalues 1/4 and 3/4. Its harmonic mean is 3/8, whereas its geometric mean is sqrt(3)/4. The smallest full-rest-conditioned presence probability is 3/8. Thus the full-rest one-site lower-bound route cannot certify the sharp geometric-mean density, even though the stochastic domination itself holds. The Schur complement is odds s, and the probability is s/(1+s); they must not be conflated.

Source correspondence: Lyons, Determinantal Probability: Basic Properties and Conjectures (arXiv:1406.2707), Conjecture 5.7, and intake C0036-A002. No result here proves the conjecture for arbitrary groups or proves its current literature status.

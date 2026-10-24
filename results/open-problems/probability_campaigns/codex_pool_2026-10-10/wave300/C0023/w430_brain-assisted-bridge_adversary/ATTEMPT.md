# C0023 independent adversarial checkpoint

Saved before reading w429's proof. Worker w430, 2026-10-10.

The assigned target is nearest-neighbour Bernoulli bond percolation on Z^d, 3 <= d <= 10, with theta(p_c)=0. Exact primary-source recovery and current openness are still pending; no novelty or target-solution claim is made.

Independent obstruction: pointwise subcritical decay does not justify interchanging the parameter limit and the radius limit. Let p_* in (0,1), 0 <= p <= p_*, n >= 1, and f_n(p)=(1/2) exp(-(p_*-p)n). For every p<p_*, f_n(p) tends to zero as n tends to infinity. Every f_n is continuous and increasing in p and decreasing in n. Nevertheless f_n(p_*)=1/2 for every n. Hence lim_n lim_(p up to p_*) f_n(p)=1/2, while lim_(p up to p_*) lim_n f_n(p)=0. This is a counterexample to an inference about families of probabilities, not a percolation-model counterexample.

The exact percolation issue to check is whether a retrieved estimate supplies a radius-dependent bound uniform in p<p_c whose radius limit is zero. A constant c(p)>0 only for p<p_c does not supply that premise.

An additional independent dependency check: if A_n={0 connects to the boundary of [-n,n]^d} then A_m is a subset of A_n for m>n. Thus P_p(A_m | A_n)=P_p(A_m)/P_p(A_n), whenever the denominator is positive. Under the hypothetical theta(p)>0, this conditional probability tends to 1 along n,m tending to infinity. Multiplying unconditioned one-arm probabilities across nested radii is unjustified.

## Primary theorem recovered; stronger independent obstruction

Primary source: Duminil-Copin and Tassion, arXiv:1502.03051, Theorem 1.1 and the finite-set threshold definition immediately above it. This is Bernoulli nearest-neighbour bond percolation on Z^d, d>=2. It gives exponential decay for each fixed p<p_c, with a rate depending on p. It also identifies p_c with the supremum of parameters having a finite set S containing 0 and phi_p(S)<1, where phi_p(S)=p sum over edges {x,y} leaving S, x in S, of P_p(0 connects to x using edges inside S). It does not give decay at p_c.

For every finite S containing 0, phi_(p_c)(S)>=1. Otherwise continuity of this finite polynomial in p gives a q>p_c with phi_q(S)<1, contradicting the threshold identity. For S=Lambda_n=[-n,n]^d intersect Z^d, its edge boundary has 2d(2n+1)^(d-1) edges. Each inside endpoint x of a boundary edge lies on the vertex boundary of Lambda_n; its connection event inside S implies A_n. Therefore, for all n>=1,

    a_n(p_c) := P_(p_c)(A_n) >= 1 / [2d p_c (2n+1)^(d-1)].

Consequently there cannot exist delta>0, c_0>0 and C<infinity such that a_n(p)<=C exp(-c_0 n) for every n>=1 and every p in (p_c-delta,p_c). Finite-box polynomial continuity passes this inequality to p_c, contradicting the polynomial lower bound for sufficiently large n. This excludes a tempting strong repair (a uniformly positive exponential rate), even if the critical nonpercolation assertion is true.

The viable missing bridge is instead any independently proved upper bound a_n(p_c)<=g(n) with g(n) tending to zero. Equivalently, sup_(p<p_c) a_n(p)=a_n(p_c) for each finite n, so a uniform subcritical tail going to zero is the target assertion in another formulation. It cannot be inserted as a consequence of sharpness.

Independent referee w431 must check the lower-bound derivation before any theorem promotion. Saved before reading the paired proof.

## Math-brain comparison route and its exact missing premise

The live math-brain recall query returned Theorem 2 of arXiv:2304.12110 among its top five hits, with warning_score=0. The primary theorem compares volume tails at p and at a different parameter q=p(1-m_h(p)), h>0; m_h(p) is the probability that the root cluster intersects independently green vertices of density 1-exp(-h). Its inequality is psi_n(q)<=psi_n(p) exp(-hn)/(1-m_h(p)), where psi_n(p)=P_p(|C(0)|>=n).

Apply its exact definitions at p=p_c. Conditional on a cluster of finite cardinality k, the chance of meeting green is 1-exp(-hk); for an infinite cluster it is one. Bounded convergence therefore gives lim_(h down to 0) m_h(p_c)=theta(p_c). In particular,

    q_h=p_c(1-m_h(p_c)) <= p_c(1-theta(p_c)),
    lim_(h down to 0) q_h=p_c(1-theta(p_c)).

Under the hypothetical theta(p_c)>0, every comparison parameter remains at least p_c theta(p_c) below p_c. The comparison theorem controls those lower parameters; it does not establish a critical upper tail bound. Assuming q_h tends to p_c assumes theta(p_c)=0 already. This is the concrete missing bridge identified from the returned theorem's full definitions. In addition, the exponent h vanishes in the h->0 limit, so a bare pointwise limiting argument does not retain exponential decay.

The retrieval failure is applicability blindness in title-only recall: the returned titles and scores expose neither the changed parameter nor the role of magnetization. The bounded proposed repair is to resolve exactly the returned IDs read-only and write a need-versus-hypothesis row before using a theorem. A high score and zero warning are not an applicability certificate.

NEXT: Referee checks the polynomial criterion and the magnetic-parameter obstruction; keep both draft-labeled in the brain submission.

# P0032: exact invariant-measure criterion for randomized forward filling

2026-10-10. Label: author proof, awaiting w346 blind KEEP. Novelty unverified. This extends the recorded candidate lemma; it does not announce an open-problem solution.

Let T be an invertible measure-preserving transformation of a standard Borel probability space (E,P), let I be its invariant sigma-field modulo null sets, and let Q=fP, with f>=0 and integral f dP=1. There exists an extension with independent uniforms and an almost surely finite N>=0 such that T^N Z has law Q for Z~P if and only if E[f|I]=1 almost surely. No finite mean for N, stopping-time property for a path filtration, or deterministic shift is asserted.

Necessity: an invariant event A has 1_A(T^N Z)=1_A(Z), outside the union of countably many null sets. Hence Q(A)=P(A) for every A in I, exactly the conditional expectation criterion.

Sufficiency: put Lh=h composed with T^{-1}, a_0=1, b_0=f, m_n=min(a_n,b_n), a_{n+1}=L(a_n-m_n), b_{n+1}=b_n-m_n. Then 0<=a_n<=1, b_n decreases to b_inf in L1, integral a_n=integral b_n, and sum integral m_n<=1. Iterating gives a_n=1-sum_{k<n}L^{n-k}m_k. For each fixed k, Birkhoff's theorem and boundedness 0<=m_k<=1 give the Cesaro mean of its L-iterates tending in L1 to E[m_k|I]. Truncating k at K leaves an L1 error at most sum_{k>=K} integral m_k, uniformly in the averaging length. Therefore the Cesaro mean of a_n tends in L1 to

    h=1-sum_k E[m_k|I]=E[b_inf|I].

Here 0<=h<=1 and h is I-measurable. If b_inf has positive mass, h has positive mass. Some epsilon>0 has H={h>=epsilon} with integral_H b_inf=integral_H h>0. Then for some delta>0 the set B=H intersect {b_inf>=delta} has positive probability. On B,

    m_n >= min(a_n,delta) >= min(1,delta) a_n.

Averaging and integrating over B gives a positive limiting lower bound min(1,delta)*integral_B h. But the Cesaro mean of integral_B m_n tends to zero, since sum integral m_n<=1. This contradiction gives b_inf=0 almost surely and sum_n m_n=f.

Accept stage n with independent uniform probability m_n/a_n evaluated at T^n Z, taking probability zero where a_n=0. The active law before stage n is a_n P; its accepted law is m_n P and its pushed residual law is a_{n+1}P. Thus P(N>=n)=integral a_n tends to zero and law(T^N Z)=sum m_n P=fP.

For an ergodic T the criterion is automatic. The two-sided Wiener unit shift is ergodic by its iid unit-increment blocks. Lifting a one-sided density f gives the previously recorded finite Brownian-prefix construction, with auxiliary randomness and arbitrary finite selection time. The disintegration step uses standard Borel path spaces. The complete earlier proof is Downloads/Probability_1000_20h_20260906/proofs/P0032_brownian_prefix_candidate.md; its own label is a candidate under review.

The boundary is exact: on a finite permutation, each orbit must receive its original total target mass. Nonergodicity alone does not preclude filling. A target that changes an orbit's mass cannot be reached by any almost surely finite orbit shift.

Checks to run: exact finite cycles with zero target entries, balanced multi-orbit targets, unbalanced multi-orbit rejection, pushforward orientation, accepted law and mass invariants. The Lean artifact checks only preservation of an invariant predicate under a point-dependent finite iteration, not Birkhoff, measure disintegration, or the Brownian theorem.

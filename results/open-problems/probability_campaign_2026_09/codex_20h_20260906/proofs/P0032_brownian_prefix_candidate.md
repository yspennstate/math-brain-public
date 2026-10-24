# P0032: a Brownian-prefix embedding argument

Written 2026-09-06. Status: complete candidate proof, undergoing author checks and a prior-literature search. No independent review and no novelty claim. Do not promote this file merely because a ledger validator accepts it.

Source problem: Burdzy and Scheutzow, *Forward Brownian motion*, arXiv:1302.6958, Problem 7.5, PDF page 26 (published 2014). The source asks whether a process on nonnegative time whose law is equivalent to Wiener measure can be preceded by a random finite path segment so that the concatenated process has Wiener law.

The interpretation here allows an extension of the probability space and dependence between prefix and suffix. The joining time is an arbitrary finite random time, not a stopping time for the ordinary Brownian filtration. Requiring a Brownian stopping time would immediately force the suffix itself to have Wiener law by the strong Markov property, so that different requirement cannot hold for a general equivalent law.

## A general lemma

Let (E,F,P) be a standard Borel probability space, and let theta:E->E be an invertible, measurable, measure-preserving, ergodic transformation with measurable inverse. Let Q have density f>=0 with respect to P, with integral f dP=1. On an extension supporting independent uniform random variables, there exists an almost surely finite integer N>=0 such that, for Z with law P, theta^N Z has law Q.

This is a filling construction related to classical work of Chacon-Ornstein, Rost, and Thorisson. The following proof is supplied in full; claiming its application as a new research result requires a separate literature check.

### Construction of remaining densities

For an integrable density h let Lh=h composed with theta^(-1). Thus pushing hP forward under theta gives (Lh)P. Set

    a_0=1,  b_0=f,
    m_n=min(a_n,b_n),
    a_(n+1)=L(a_n-m_n),
    b_(n+1)=b_n-m_n.

All these functions are measurable and nonnegative. Inductively 0<=a_n<=1. The b_n decrease and are bounded above by f, so they have an integrable pointwise limit b_infinity. Since L preserves integrals, both remaining densities have the same mass r_n:

    integral a_n dP = integral b_n dP = r_n,
    r_n decreases to r = integral b_infinity dP,
    sum_(n>=0) integral m_n dP = 1-r.

### The remaining mass must be zero

Iteration gives the exact identity

    a_n = 1 - sum_(k=0)^(n-1) L^(n-k)m_k.

For each fixed k, the ergodic theorem for the measure-preserving transformation theta^(-1) gives

    (1/M) sum_(n=k+1)^(M-1) L^(n-k)m_k
       -> integral m_k dP

in L1(P). The L1 assertion follows from the usual almost-sure ergodic theorem and equality of the integrals for nonnegative averages, or by approximation from bounded functions. Initial omitted terms do not affect the limit.

Truncate the sum in k at K. Its tail has L1 norm at most sum_(k>=K) integral m_k dP, uniformly in M. That tail tends to zero as K grows. Therefore

    (1/M) sum_(n=0)^(M-1) a_n -> r

in L1(P), where r on the right is the constant function.

Suppose r>0. There is a delta>0 such that B={b_infinity>=delta} has positive P-measure. On B,

    m_n=min(a_n,b_n) >= min(a_n,delta)
        >= min(1,delta) a_n,

where the last step uses a_n<=1. Averaging and integrating over B gives

    liminf_M (1/M) sum_(n<M) integral_B m_n dP
        >= min(1,delta) r P(B) > 0.

But the entire sum of the integrals of m_n is at most one, so its Cesaro average tends to zero. This contradiction proves r=0. In particular sum_n m_n=f in L1 and almost everywhere.

### Realizing the matching as a random shift

Sample Z with law P and independent U_0,U_1,... uniform on [0,1]. At stage n, if not previously accepted, inspect theta^n Z and accept when

    U_n <= h_n(theta^n Z),
    h_n=m_n/a_n on {a_n>0}, and h_n=0 elsewhere.

By induction, the subprobability distribution of theta^n Z before this test is a_n P. The mass accepted at stage n has distribution m_n P, and the surviving mass pushed forward has distribution a_(n+1)P. Hence P(N>=n)=r_n tends to zero, while the law of theta^N Z is sum_n m_n P=fP=Q. Every U_n is independent of Z and of preceding U's, so the induction is valid even though h_n can inspect an entire trajectory. This proves the lemma.

## Application to Brownian motion

Let E=C_0(R) carry two-sided Wiener measure P. Define

    (theta w)(t)=w(t+1)-w(1), t in R.

This is an invertible measurable measure-preserving transformation. It is ergodic: the path is measurably equivalent to its bi-infinite sequence of unit-length Brownian increment segments, and theta shifts this independent identically distributed sequence by one. Ergodicity of that shift follows by approximating an invariant event by finite-coordinate cylinder events and using independence of sufficiently separated cylinders.

Let Q_plus be the desired law of X on C_0([0,infinity)), and let f_plus=dQ_plus/dW_plus. Define f(w)=f_plus(w restricted to [0,infinity)). Its integral under P is one. Apply the lemma to Q=fP. The forward part of theta^N W,

    Y_t=W_(N+t)-W_N, t>=0,

has exactly law Q_plus, and N is finite and nonnegative. The path obtained by taking W on [0,N] and continuing with W_N+Y_(t-N) is identically the original path W on nonnegative time. It therefore has Wiener law.

If the requested suffix X already lives on a specified probability space, use the regular conditional distribution of (W,N) given Y in this coupling to extend that space. Standard Borel path spaces ensure this disintegration exists. In the resulting coupling Y=X almost surely, so the prescribed X receives a prefix without changing its law.

Thus the argument gives the requested embedding under the stated interpretation, and even uses only absolute continuity Q_plus<<W_plus rather than equivalence. It does not require a finite expectation for N and does not give a computable finite-lookahead rule.

## Checks and strongest objections

1. Pushforward direction: Lh=h composed with theta^(-1), so removing m_n and then moving forward really gives the stated a_(n+1). Using h composed with theta would reverse the density transport.
2. The bound a_n<=1 is indispensable in the contradiction. It follows from stationarity of the starting probability P; an arbitrary initial distribution would need a different argument.
3. No independence of the sampled future blocks is asserted. The density recursion replaces the invalid idea that infinitely long Brownian futures can be used as disjoint rejection trials.
4. The proof preserves the unconditional Wiener marginal of W. Selecting a suffix changes its law but does not condition the original W on the success of an event; acceptance occurs almost surely.
5. A two-state cyclic transformation with uniform P and target density (2,0) matches half the mass at n=0 and the other half after one shift. The density recursion yields Q exactly and checks its direction and normalization.
6. The mathematical and interpretive risk is that Problem 7.5 imposes an additional implicit restriction on the prefix. The displayed source wording contains no independence or stopping-time restriction. Check the surrounding paper and subsequent literature before labeling the problem solved.
7. A pre-existing embedding/filling theorem may already imply this conclusion. The argument would remain a valid explanation, but novelty and open-at-start status would then need to be withdrawn.

Prior-literature leads being checked: Pitman-Tang (2015), *The Slepian zeros and Brownian bridge embedded in Brownian motion*, Theorem 5.7 (a two-sided random shift), and Chacon-Ornstein/Rost filling schemes. Theorem 5.7 alone allows a shift of either sign; the nonnegative direction is established directly above.

## A determinism obstruction and why the auxiliary uniforms matter

A counter-check communicated by the parent agent identifies a real boundary of the lemma. If an integer shift n(z) is a deterministic measurable function of z alone, the full shifted law has density

    g(y) = sum_(k in Z) 1_{n(theta^(-k)y)=k}

with respect to P. Indeed, for every measurable A, partitioning by n=k and applying invariance gives the integral of 1_A times this sum. Tonelli applies because the summands are nonnegative. Thus g is integer-valued almost everywhere; its integral is one, so the sum is finite almost everywhere. Arbitrary noninteger f cannot arise this way. This is a counterexample to a stronger, deterministic version of the general lemma, not to the displayed randomized construction.

The present argument explicitly uses independent uniforms. Averaging their conditional acceptance probabilities yields real-valued densities m_n, so the integer-valued obstruction does not apply. Alternatively, a future marginal may hide randomness in the unobserved past; a statement about that projection must be distinguished from a statement about the full two-sided law. No deterministic full-path transport is claimed here.

This check was independently suggested but does not constitute an independent review of the complete candidate proof. The author has re-derived the density formula above. Holroyd and Peres, *Extra heads and invariant allocations* (2005), arXiv:math/0306402, Theorem 17 and the following remark, provide another prior-literature lead: their greedy transport can restrict displacements on Z to nonnegative integers. Their displayed setting uses binary target capacities; the density-matching proof here supplies its own general-density argument.

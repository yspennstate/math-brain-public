# C0120 independent checkpoint

Written before reading any paired prover proof, 2026-10-10.

For fixed q>0 and delta>0, n/(log n)^q is not O(n^(1-delta)): divide by n^(1-delta) and put t=log n. The logarithm of the resulting ratio is delta*t-q*log t, which tends to infinity. Thus a logarithmic variance improvement alone supplies no polynomial improvement. The extra premise must be a bound on an additional quantity with a fixed positive power saving, uniform in n, rather than an exponent chosen after n.

This does not assert that actual polymer variance equals the counterexample sequence. It refutes only the proposed implication from a logarithmic upper bound to a polynomial one. The exact model and source hypotheses remain to be recovered. Referee: w503, independent check pending.

## Source recovery and independent bridge (before paired proof)

Primary source: Chatterjee, *Chaos, concentration, and multiple valleys*, arXiv:0810.4221v2 (16 December 2008), Section 8 and Section 12(3). This source's variable is a zero-temperature maximum M_n, not log Z_n at a fixed finite inverse temperature. Its paths have n vertices in Z^2_+, start at the origin, and move right or up; their endpoint is free on the last antidiagonal. The weights g_v are independent standard Gaussians. M_n=max_p sum_{v in p} g_v. Theorem 8.1 bounds Var(M_n) by C n/log n. The intake's general-dimension finite-temperature formulation is a related research target and is not an exact restatement of this cited theorem.

Let g^t=e^{-t}g+sqrt(1-e^{-2t})g', where g' is independent of g, and let P_n^t be the unique optimal path. Set Q_n(t)=E|P_n^0 intersection P_n^t|. The maximum is a Lipschitz function of the finitely many reachable Gaussian weights, and its weak gradient is the path indicator almost everywhere. The Gaussian covariance identity gives

Var(M_n)=integral_0^infinity e^{-t} Q_n(t) dt.

By the semigroup identity Q_n(t)=sum_v ||P_{t/2}(1_{v in P_n})||_2^2, Q_n is nonnegative and nonincreasing, and Q_n(0)=n. Split the integral at h>0 to obtain

(1-e^{-h}) Q_n(h) <= Var(M_n) <= n(1-e^{-h})+e^{-h} Q_n(h).

This independently derives the specialized inequalities of source Theorem 3.2. No independence between successive selected path vertices is used.

Consequently, an additional estimate Q_n(n^{-a})<=K n^{1-b} for fixed a,b in (0,1) and K independent of n implies Var(M_n)<=(1+K)n^{1-min(a,b)}. Conversely, if Var(M_n)<=K n^{1-delta} for fixed delta in (0,1), then each fixed a in (0,delta) gives Q_n(n^{-a})<=2K n^{1-(delta-a)} for all n>=1, using 1-e^{-h}>=h/2 for h<=1. This is a quantitative reduction, not a proof that either power estimate holds for the polymer.

The available Theorem 8.1 only gives Q_n(n^{-a})<=C n^{1+a}/log n, capped by n. For every fixed a>0 this is eventually the trivial cap n. At h=(log n)^{-1/2}, the known estimate instead gives Q_n(h)<=O(n/sqrt(log n)). Thus the specific hardest missing premise is a positive power rate of overlap loss at a polynomially small OU time. Qualitative chaos or another use of the same logarithmic variance bound cannot supply that premise.

Noise calibration matters: the independent-noise amplitude sqrt(1-e^{-2h}) is asymptotic to sqrt(2h), so an amplitude n^{-a} corresponds to OU time of order n^{-2a}. Exponents cannot be transferred without this factor of two.

Paired proof still unread at this checkpoint. Referee for these independently derived conditional deductions: w503; check pending. Current openness: UNKNOWN; no parent-problem solution or novelty claim.

## After paired proof: finite-temperature transfer obstruction

For the same finite path family P_n, define Z_{n,beta}=sum_p exp(beta X_p) and F_{n,beta}=beta^{-1}log Z_{n,beta}, beta>0. Deterministically

0<=F_{n,beta}-M_n<=(log|P_n|)/beta=((n-1)log 2)/beta=:A.

For D=F_{n,beta}-M_n in [0,A], Var(D)<=A^2/4 because E[(D-A/2)^2]<=A^2/4. The reverse triangle inequality for centered L2 norms yields

|sqrt(Var(F_{n,beta}))-sqrt(Var(M_n))|<=sqrt(Var(D))<=A/2.

To use THIS comparison to transfer an O(n^{1-epsilon}) variance bound from F to M, the error term requires beta(n)>=c n^{(1+epsilon)/2}, with c>0 independent of n, and the bound on Var(F_{n,beta(n)}) must have a constant uniform along that growing beta sequence. A theorem whose constant depends arbitrarily on a fixed beta does not establish this. These are sufficient requirements of this comparison, not necessary conditions on the actual model: the real transfer error might be smaller.

This isolates a second exact missing premise behind the intake/source mismatch. It does not attempt to prove a finite-temperature power bound. w501's L1-L4 were checked after the independent checkpoint; scoped verdicts are in PAIR_AUDIT.md.

## Returned brain theorem: full hypotheses and a refuted explanatory clause

The read-only brain query returned 'The Ornstein-Uhlenbeck Semigroup and Mehler\'s Formula' (claim_3a7f53cc4f4c10093c8e4e07c223f18d52212a9c7d6f98c1196f104f16111a3d). Its standard Gaussian measure, generator Delta-x.grad, invariant law, self-adjointness, and time convention match the source-model bridge. The path indicators are bounded L2 functions of a finite vector of independent standard Gaussian weights, so the semigroup contraction argument applies. The card alone supplies no polynomial overlap-loss rate.

The same query returned 'Talagrand\'s L1-L2 Variance Inequality' (claim_19af561bcf040b56cc9b3aa80d52d5dd62e1e00c1b7ecb97b574cbacb19b5603). Its displayed theorem assumes the uniform DISCRETE cube and flipped-coordinate derivatives; these hypotheses do not match continuous Gaussian polymer weights. A Gaussian version must be sourced separately. Moreover, its explanatory clause that it 'gains nothing for a coordinate whose discrete derivative is essentially an indicator' is false for rare indicators in magnitude, even under its own exact cube hypotheses.

Concrete example on {-1,1}^3 with uniform law: f(x)=x_1 * 1{x_2=x_3=1}. For Delta_1 f=(f(x)-f(x with x_1 flipped))/2, one gets Delta_1 f=x_1 * 1{x_2=x_3=1}. Thus ||Delta_1 f||_1=1/4 and ||Delta_1 f||_2=1/2. The norm ratio is 2 and its displayed denominator is 1+log 2>1. More generally, if |D|=c 1_A with c>0 and P(A)=p in (0,1], then ||D||_2/||D||_1=p^{-1/2} and the denominator is 1+(1/2)log(1/p). No gain occurs at p=1; smaller p gives a gain. This refutes the explanatory clause, not the displayed variance inequality.

The proposed bounded brain repair is a concept caveat attached to this exact card, retaining its cube hypotheses and correct inequality. Referee w503 is asked to check the concrete calculation; the live card is not edited. Exact returned text and metadata are frozen in exact_bridge_cards.json.

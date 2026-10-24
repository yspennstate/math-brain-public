# Independent bridge and counterexample

2026-10-10. Derived from w369's statement-only challenge and primary sources;
the paired proof has not been opened. Target specialization: iid Exp(1)
weights on undirected nearest-neighbor Z^2, T_n = T(0,ne_1), and
chi_var = lim log Var(T_n)/(2 log n). This specialization does not fill in
ADH's unspecified suitable conditions for every distribution.

## A rare-event counterexample retaining the larger-scale tail bound

For integers n >= 3 set a_n = n^(1/3), s_n = sqrt(n/log n), and
p_n = n^(-1/4). Let Z and S be independent symmetric signs in {-1,1},
and let B_n be Bernoulli(p_n), independent of both. Define

    X_n = a_n Z + s_n B_n S,       Q_n = n + X_n.

Then E X_n = 0 and Var(Q_n) = a_n^2 + p_n s_n^2
= n^(2/3) + n^(3/4)/log n. Consequently
log Var(Q_n)/(2 log n) -> 3/8, not 1/3.

Yet X_n/a_n converges weakly to the nondegenerate sign Z: for any bounded
continuous f, the absolute expectation difference is at most
2 ||f||_infinity p_n -> 0. This uses the single event B_n=0, not a
product of dependent conditional bounds.

For n >= 3, a_n/s_n = sqrt(log n)/n^(1/6) <= sqrt(3/e) < 1.1:
the function (log x)/x^(1/3) has its maximum 3/e at x=e^3.
Hence |X_n| <= 2.1 s_n, and for every t >= 0 and every n >= 3,

    P(|X_n| >= t s_n) <= exp(2.1-t).

This is a uniform exponential tail bound at sqrt(n/log n), with constants
independent of n. Also Var(Q_n) <= (3/e+1) n/log n.
For sufficiently large n, Q_n is nonnegative; omit finitely many initial
terms or redefine them as n without changing these limits.

The standardized fourth moment diverges. Independence and symmetry give
E X_n^4 = a_n^4 + 6 a_n^2 p_n s_n^2 + p_n s_n^4, so
E X_n^4/(E X_n^2)^2 ~ 1/p_n = n^(1/4).

This is an exact counterexample to replacing the standardized moment/UI
premise by the known larger-scale exponential concentration bound. It is
an abstract sequence, not an iid lattice FPP construction or a disproof
of P0104. Its claim is about which inequalities imply a variance exponent.

## Separate derivation of the centered conditional bridge

Let E U_n=0, 0<v_n=E U_n^2<infinity, E U_n^4 <= K v_n^2,
and U_n/a_n converge weakly to a nondegenerate real Y, with a_n>0.
Write r_n=sqrt(v_n)/a_n. If r_n has a subsequence tending to zero,
Chebyshev gives U_n/a_n -> 0 in probability along that subsequence,
contradicting the nondegenerate weak limit. Thus liminf r_n>0.

If r_n has an unbounded subsequence, Paley-Zygmund applied to U_n^2
gives P(|U_n| >= sqrt(v_n/2)) >= 1/(4K). For arbitrarily large fixed R,
the corresponding subsequence has P(|U_n/a_n|>R) >= 1/(4K),
contradicting tightness. Thus sup r_n<infinity after finitely many terms.

It follows that sup E|U_n/a_n|^4<infinity. For each R>0,
E[(U_n/a_n)^2 1{|U_n/a_n|>R}] <= sup E|U_n/a_n|^4/R^2.
The squares and first moments are therefore uniformly integrable.
Weak convergence plus truncation proves E Y=0 and
v_n/a_n^2 -> E Y^2 = Var(Y) in (0,infinity).

For arbitrary deterministic centers m_n, set Y_n=(X_n-m_n)/a_n and
take an independent copy X_n' of each X_n. Product-law convergence gives
(X_n-X_n')/a_n -> Z-Z', with Z' independent of Z. This is nondegenerate
whenever Z is nondegenerate. The centered difference D_n=X_n-X_n' has
E D_n^2=2 sigma_n^2 and
E D_n^4=2 E|X_n-E X_n|^4+6 sigma_n^4
<= ((K+3)/2)(E D_n^2)^2. Apply the centered proof to D_n.
Its limiting second moment is finite. Fubini then supplies a fixed z'
with E(Z-z')^2<infinity, proving Z has finite second moment.
E(Z-Z')^2=2 Var(Z) yields Var(X_n)/a_n^2 -> Var(Z)>0.
This derivation permits arbitrary m_n and needs no independence across n.

For the width subclaim, K>=1 by Jensen. An interval of length w<sigma
containing probability >=1-p implies P(|X-X'|>w)<=2p. In contrast,
Paley-Zygmund for (X-X')^2 at threshold w^2<sigma^2 gives
P(|X-X'|>w) >= 1/(2K+6) >= 1/(8K), a contradiction when
p<=1/(32K). Hence W_p(X)>=sigma. Chebyshev gives an interval centered
at E X of length 2 sigma/sqrt(p) and mass >=1-p, proving the upper bound.

Status: mathematical derivations saved for w371's independent check;
no independently checked proof and no FPP application claimed.
NEXT: Audit the deterministic-centering step and the stated width constants
in w369's full proof; package this counterexample as a draft concept.

from pathlib import Path
with Path('ATTEMPT.md').open('a',encoding='utf8') as out:out.write('''

## Example L (proved special case: one infinite-mean hitting piece)

The domination result also permits an actual infinite-mean stopping law; finite mean is required for the reference, not for every actual piece. Let B be standard Brownian motion, tau=inf{t>=0:B(t)=-1}, and E an independent exponential time of rate 1, revealed at time zero in the stopping filtration. Let P_0 be the stopped-pair law for T_0=min(tau,E). Then 0<E T_0<=1, and the normal filtration with E added leaves B Brownian. T_0 is a stopping time.

Let Q be the untruncated first-hitting stopped-pair law for tau. On the reference stopped-pair space its density is

    f(t,b)=exp(t) * 1_{b(t)=-1}.

Indeed, the reference endpoint equals -1 exactly when tau<=E, up to a null tie. For every nonnegative measurable g,

    E_{P_0}[f(T_0,b)g(T_0,b)]
       = E_B[exp(tau)g(tau,B stopped at tau)P(E>=tau | B)]
       = E_B[g(tau,B stopped at tau)] = E_Q g.

This proves full stopped-pair domination, with integral f dP_0=1. Its affinity is

    rho=E_{P_0} sqrt(f)=E_B exp(-tau/2)=exp(-1)>0.

For completeness the hitting-time Laplace identity follows from the exponential martingale exp(-aB(t)-a^2 t/2), a=sqrt(2 lambda), stopped at t min tau. Before hitting -1 this stopped martingale is bounded by exp(a), so bounded optional stopping gives expectation 1 and dominated convergence gives exp(a)E exp(-lambda tau)=1. Finiteness of tau a.s. follows from reflection: P(tau>t)=2 Phi(1/sqrt(t))-1 tends to zero. That same reflection formula has tail asymptotic sqrt(2/pi)/sqrt(t), making E tau=infinity by integration of the tail.

Take independent reference pieces P_0 at all indices except k=-1, where use Q. The Hellinger sum has just the finite nonzero term 1-exp(-1). Theorem H (or J) therefore proves a finite random shift to two-sided Wiener law on an extension, although the actual k=-1 duration has infinite mean. The reference clock sums diverge a.s. and product domination transfers this event to the actual system; directly, all the infinitely many remaining i.i.d. positive-duration pieces also suffice.

At the original boundary zero, on every sample the final negative piece stays strictly above its endpoint before tau, hence X(-s)>X(0) for all 0<s<tau. Standard Brownian motion started at zero has probability zero of remaining nonnegative on a whole positive interval: reflection gives P(min_{0<=s<=h}B(s)>=0)=0 for every h>0, and a countable union over rational h treats a random positive interval. Thus the original backward half is not Brownian at zero. This is another example where correcting the random center is necessary. It is an affirmative nonidentical stopped-piece special case, not a counterexample to 7.1. QED.

## Periodic finite-mean control (proved special case used in the probe)

If stopped-piece laws repeat with a finite period p and the sum of their mean durations over one period is finite and positive, group consecutive p pieces starting at indices mp, m in Z. A group is a stopped Brownian piece by finite strong-Markov concatenation; its endpoint time is a stopping time in the concatenated filtration, since successive component stopping decisions are adapted until the end of each component. The grouped stopped pairs are independent and identically distributed, and their mean duration is the finite positive sum over a period. Source Theorem 5.1 applies to the grouped decomposition. Thus periodic finite-mean decompositions are 2BM after a shift. This justifies the alternating-rule positive control below; it does not extend to arbitrary nonperiodic laws.

## Supplementary bounded-rule likelihood probe

For the duration-1-or-2 model, write epsilon_j for the parameter of the negative piece at index -(j+1), p_j(z)=1/2+epsilon_j tanh z. Let F_{j,n}(y_1,...,y_n) be the density of its first n backward unit increments, including subsequent pieces, relative to n independent standard normals. Conditioning on whether the current piece has length 1 or 2 gives the exact finite recurrence

    F_{j,0}=1,
    F_{j,1}(y)=p_j(-y)+1/2,
    F_{j,n}(y)=p_j(-y_1)F_{j+1,n-1}(y_2,...,y_n)
               +[1-p_j(-y_2)]F_{j+1,n-2}(y_3,...,y_n), n>=2.

For length 1 the observed increment is -B(1), weighted by its stop probability. For length 2 the first observed increment is -(B(2)-B(1)) and the second -B(1), weighted by the continue probability evaluated at the second one. These two normal increments and the remaining pieces are independent before that weight. For n=1, integrating the unobserved B(1) in the length-2 branch gives E[1-p_j(B(1))]=1/2 by oddness of tanh. This proves the recurrence, not only its numerical implementation.

second_likelihood_probe.py computes that recurrence by dynamic programming and estimates its first two reference moments with 500 normal samples at n=16,64,128. Controls are constant epsilon=0.24 (source Theorem 5.1), alternating +/-0.24 (periodic grouping above), and epsilon_j=0.125/(j+1) (Theorem J). The unproved test is epsilon_j=0.24*(-1)^{floor(log2(j+1))}, which has growing blocks of opposite signs and fails the simple common-reference Hellinger summability condition.

The unproved test's estimated second moments at 16,64,128 were respectively 1.1222,1.1088,1.1395; estimated means stayed within 0.008 of 1. No density-collapse or counterexample signal appeared in this bounded run. These estimates do not prove uniform integrability, full Brownian-path domination, BBM, or a finite exact shift. Even a proven assertion for these integer increments would need the conditional intra-unit path laws to yield full continuous-path domination. The remaining original gap is unchanged.

Second-attempt verification: second_checks.json records 140 exact rational finite-cycle filling cases, the nonergodic residual 1/2, four product-overlap enumerations with maximum error 4.4408920985e-16, four Hellinger-affinity quadratures, and the 200000-sample original-boundary mean check. second_lean_check.txt records compiler exit 0 for HellingerFilling.lean, with narrow imports, no sorry and no native_decide. The infinite-dimensional product and Brownian proofs remain paper proofs, not Lean formalizations.

Technical clarification for Theorem J: Definition 2.2 asserts independence of stopped pairs, not necessarily of their originally supplied full Brownian continuations. For the strong-Markov gluing proof one may realize independent copies of each full Brownian/stopping-time/filtration system on their product space; their stopped-pair joint law is the same independent product as originally supplied. This proves the concatenated path law without assuming independence of unused continuations in the original realization.
''')
print('saved infinite-mean example, periodic control, probe proof and checks')

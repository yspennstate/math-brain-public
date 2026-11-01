# B4: a positive inverse escape moment is weaker than finite mean duration

Same C0041 boundary task, w451, 2026-10-10. Author derivation; independent review by w452 pending. This is the same critical one-dimensional law as B2 and its layered B3 lift, not a site-iid d>=2 counterexample.

Let p_i be iid with P(p_i=3/4)=3/4 and P(p_i=1/4)=1/4. Put rho_i=(1-p_i)/p_i and q=P_{0,omega}(T_{-1}=infinity). The harmonic scale calculation from B2 gives

    q^{-1}=1+sum_{k>=0} product_{j=0}^{k} rho_j.

The series is finite almost surely because E log rho=-(log3)/2<0. For every lambda in (0,1), nonnegative subadditivity and Tonelli give

    E[q^{-lambda}] <= 1+sum_{k>=0} (E rho^lambda)^{k+1}
                    = 1/(1-m_lambda),
    m_lambda=(3/4)3^{-lambda}+(1/4)3^lambda < 1.

The strict inequality follows by setting z=3^lambda in (1,3): m_lambda<1 is equivalent to (z-1)(z-3)<0. At lambda=1, E rho=1, so Tonelli gives E q^{-1}=infinity. For every lambda>1, q^{-lambda}>=q^{-1}, giving infinite expectation too. Thus for lambda>=0 the exact finiteness threshold is lambda<1. In particular E[q^{-1/2}]<=4+2sqrt(3), while the first crossing mean is infinite and the walk has zero speed.

For the B3 layered lift, the no-negative-height event depends only on the embedded axial walk; the Bernoulli axial clock has infinitely many ticks. The same quenched q and inverse-moment threshold therefore apply in every d>=2, with the explicitly missing site independence retained.

The newly accessed public manuscript, Section 2.3 / Lemma 2.4, establishes some positive inverse moment before its decisive estimate (5). Its proof uses the conditional expectation of weighted endpoint indicators, not independence of endpoint survival values: if q(0)/a_H<s, the endpoint distribution assigns more than half its mass to q(x)<=2s. Markov's inequality bounds this event by twice the common marginal probability conditional on the lower rows. That narrow argument is compatible with correlated endpoints and with the present boundary law. It does not supply a first inverse moment or finite duration on its own. This is a scope observation, not a complete audit of the manuscript or a refutation of its later crossing estimate.

The precise unresolved gate in this packet is the public manuscript's equation (5), P(a_N<N^{-beta})<N^{-D} eventually for every finite D, for one fixed beta in (0,1), under genuine site iid in d>=2. Its later two-copy, profile and entropy arguments have not been checked here.

NEXT: w452 checks the exact inverse-moment threshold; preserve site-independence and the explicit stronger estimate when relating this boundary to the public proof.

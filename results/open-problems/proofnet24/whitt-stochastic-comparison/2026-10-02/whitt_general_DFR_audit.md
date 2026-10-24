# Independent audit: the regenerative general-service and DFR extensions

2 October 2026. This audit concerns mathematical validity, not historical priority or external expert acceptance.

## Verdict and exact hypotheses

The theorem in `whitt_general_DFR_proof.md` is valid under its explicit hypotheses: c>=2, a strictly positive absolutely continuous service time, and a finite continuous hazard h which is nonincreasing, nonconstant, and bounded below by1/B>0. No phase-type assumption is needed. The comparator is zero with probability1-m/B and exponential of meanB with probabilitym/B, where m=ES. The theorem gives a reversed delay-probability inequality for every sufficiently small positive arrival rate, with no explicit endpoint for that interval. It does not claim a strictly positive comparator for every general DFR law.

The regenerative expansion itself admits a broader sufficient hypothesis: S>0 almost surely, 0<m=ES<infinity, and ES²<infinity. No absolute continuity, hazard monotonicity, or exponential tail bound is required for this expansion. Restrict rates to0<lambda<=lambda0 withlambda0*m<1. This conservative small-rate range supplies an ordinary single-server regenerative dominator; the actual c-server stability range is larger but is unnecessary here.

## The finite-second-moment expansion

Write s(t)=P(S>t), L(t)=integral_t^infinity s(v)dv, and let G_e have survival L(t)/m. Let c iid residuals R_i have law G_e, independent of a fresh S. The valid expansion is

    P(W_G>0)=m^c lambda^c/c!
      +[m^c J_c/c!-m^(c+1)/c!]lambda^(c+1)
      +o(lambda^(c+1)),

where

    J_c=E[min(S,R_(2)-R_(1))]
       =c/m^c integral_0^infinity integral_0^infinity
          s(u)s(t)L(u+t)^(c-1)du dt.

The equilibrium law is absolutely continuous even when G has atoms, so its first two order statistics have no ties. All integrals are finite: the min is bounded by S. For the regenerative proof, the needed stronger integrable initial-work bound is supplied by

    E R_i=ES²/(2m)<infinity.

## Exact waiting-versus-loss identity

Let P_lambda be the stationary all-busy probability of the waiting queue, f its all-busy indicator, and tau the first emptying time from a nonempty marked state x. Define

    H_lambda(x)=E_x integral_0^tau(f(X_t)-P_lambda)dt,
    H_lambda(empty)=0.

If w(x) is total remaining work, a work-conserving single-server queue with the same future arrival marks empties no earlier than the c-server queue. A subcritical M/G/1 busy period from deterministic initial workw has expected lengthw/(1-lambda*m). Therefore

    |H_lambda(x)|<=w(x)/(1-lambda*m).

The Markov value-function identity gives the extended Poisson equation

    A_wait H_lambda=-f+P_lambda.

It includes the empty state. Its generator value there islambda E H_lambda(one fresh job). Regeneration gives E H_lambda(one fresh job)=P_lambda/lambda, so no empty-state correction is missing.

On a full loss state R, loss and waiting generators differ only by the waiting arrival jump. Consequently

    A_loss H_lambda(R)
      =-f(R)+P_lambda-lambda E_S[H_lambda(R+S)-H_lambda(R)].

Stationary averaging over the loss queue then gives the exact identity

    P_lambda-P_loss(lambda)
      =lambda P_loss(lambda)
          E[H_lambda(R+waiting S)-H_lambda(R)].

The potential can have either sign. This argument does not assume monotonicity of H_lambda or of the waiting queue under convex order.

## Why the unbounded-potential Dynkin step is justified

For the hazard-bounded DFR theorem, the proof's M/M/1 busy-cycle domination supplies finite first and second moments and suffices to pass its localized Dynkin identity through a loss regenerative cycle.

For the broader finite-second-moment lemma, a stationary fixed-time argument is cleaner and avoids asking for a second moment of that busy cycle. In a stationary loss state, total residual work has finite mean since at mostc jobs are present and each conditional residual has finite mean. On any fixed interval[0,T], pathwise

    sup_t w(X_t)<=w(X_0)+sum_{arrivals in[0,T]}S_j.

The right side is integrable. The linear potential bound therefore controlssup|H_lambda(X_t)| in L1. The expected waiting-arrival jump discrepancy is bounded by

    (2w(X_t)+m)/(1-lambda*m).

The displayed generator identity thus has an integrable right side throughout[0,T]. Stop first at bounded work and time; the integrable bounds allow the stops to be removed. Stationarity and E|H_lambda(X_0)|<infinity give E A_loss H_lambda=0. No third service moment or second equilibrium-residual moment is needed.

For completeness, the extended-generator domain does not require H_lambda to be classically differentiable. Before the next deterministic service completion, the first-arrival value-function identity makes H_lambda absolutely continuous along the residual-work flow, with the displayed derivative almost everywhere. Values match the post-completion state at completion boundaries by the strong Markov property. Its compensated arrival jumps are integrable under the bounds above. These facts supply the localized extended Dynkin formula.

## Loss product law: a direct check

For a strictly positive service distribution, the loss invariant measure has count weights proportional to(lambda*m)^n/n!, n=0,...,c. Conditional on n, its unordered residuals are n iid variables of densityq(r)=s(r)/m. This can be verified without assuming phase types.

Take symmetric test functions F_n consistent at a completion boundary, F_n(0,r)=F_(n-1)(r). Integration by parts againstq gives a completion-boundary termn/m and an interior term against the service distribution. The count weights satisfy

    n*pi_n/m=lambda*pi_(n-1).

Each completion-boundary term therefore cancels the arrival-out term at the preceding count, and each interior term cancels the arrival-in term from that count. For atomic G, the same computation is Stieltjes integration by parts. At countc, blocked arrivals have no jump. This verifies the product law and Erlang-B all-busy probability. Randomly labeling the unordered residuals yields the iid R used in the identity; no particular physical-server labeling convention is required.

## Continuity at zero arrival rate

Fixlambda0*m<1. Couple all arrival streams by thinning one rate-lambda0 marked Poisson process. For the initial statesR andR+waiting S, total initial workW=sumR_i+S is integrable because ES² is finite. The busy period of the original M/G/1 queue at rate-lambda0 started with workW dominates the c-server emptying times for all smaller rates. Its expectation is E W/(1-lambda0*m), so it is an integrable dominating random variable.

Aslambda decreases tozero, eventually no arrival before the no-arrival emptying time is retained on each fixed sample path. Thus the paths coincide with the no-arrival paths for all sufficiently small rates on that sample. AlsoP_lambda tends tozero: the stationary waiting workload is dominated by the original M/G/1 workload, whose nonempty probability islambda*m. Dominated convergence now gives

    E[H_lambda(R+waiting S)-H_lambda(R)] -> J_c.

This requires only an integrable dominating busy period, not its second moment. Together with the elementary Erlang-B expansion it proves the general-service expansion above. It proves an o(lambda^(c+1)) remainder, without claiming analyticity or an O(lambda^(c+2)) remainder for general G.

## DFR strictness

For the stated continuous decreasing hazard, conditional residual survival is at least exp(-h(t)u), so L(t)/s(t)>=1/h(t). The equilibrium hazardg(t)=s(t)/L(t) satisfies

    g'(t)=g(t)(g(t)-h(t))<=0.

Hence the equilibrium survival L(t)/m is NWU:

    L(u+t)>=L(u)L(t)/m.

Using this inequality in the integral forJ_c, andL'=-s, yields

    J_c>=c/m^(2c-1)
           [integral_0^infinity s(t)L(t)^(c-1)dt]^2
        =m/c.

Strictness is essential and does hold. If the NWU inequality were equality everywhere, continuity and the multiplicative functional equation would force L(t)/m to be exponential. Then L'=-s ands(0)=1 force the original survival to be exponential, contrary to the nonconstant hazard. Therefore the inequality is strict on a set of positive area. Since s is everywhere positive andc-1>0, J_c>m/c.

Equivalently, nonconstant decreasingh givesm>1/h(0), so g'(0)<0; this supplies an explicit open rectangle of strict NWU inequality nearzero.

## Convex ordering and endpoint comparison

The lower hazard bound givesL(t)<=B s(t), henceL'=-s<=-L/B. Therefore

    L(t)<=m exp(-t/B).

This is exactly the stop-loss transform of U=0 with probability1-m/B and B*Exp(1) with probabilitym/B. Equal means and ordered stop-loss transforms prove G<=cx U. Nonconstant decreasingh makesm<B, so these probabilities are legitimate and the comparator is distinct.

Deleting zero work leaves the comparator's positive subsystem M/M/c with arrival ratelambda*m/B and service rate1/B. Zero-service jobs still have their original FCFS waits; all arrivals see the subsystem's virtual delay by PASTA. Erlang C has cubic-next coefficient -(c-1)m^(c+1)/(c!*c). Consequently

    P(W_G>0)-P(W_U>0)
      =[m^c/c!]*(J_c-m/c)*lambda^(c+1)
        +o(lambda^(c+1))>0

for sufficiently small positive rates. This disproves the stochastic-order implication for the stated DFR class.

## Remaining limits

This audit verifies the mathematical proof, including its infinite-queue and unbounded-potential steps. It does not establish first priority or an explicit finite arrival-rate interval for each general DFR law. The existing finite-mixture and nine-state certificates are separate explicit results. The DFR extension leaves weaker mean-wait conjectures unaddressed.

## Addendum: the explicit strictly positive general-DFR comparator

I also independently read `whitt_general_DFR_positive_comparator.md` and checked its complete construction. It is valid under the same continuous hazard hypotheses. Let M=h(0), q0=(B-m)/B, delta=q0/(4M), kappa=m-exp(delta/B)L(delta), and Delta_G=K_c(G)-m^(c+1)/(c!*c)>0. The stated epsilon minimum is positive, and its m/2 and B/2 bounds ensure valid mixture probabilities and the later coefficient bound.

For the target mixture of epsilon and B exponentials, let q=(B-m)/(B-epsilon) be its short-class probability. For0<t<=delta,

    F_S(u)<=Mu,
    F_T(u)>=q0*u/(epsilon+u),
    integral_0^t F_T(u)du>=q0*t²/[2(epsilon+t)]
                             >=q0*t²/(4delta)=M*t²,

whereas integral_0^t F_S(u)du<=M*t²/2. These bounds are correct even at epsilon=delta. Equal means imply strict target stop-loss domination on this region.

The function exp(t/B)L(t) is nonincreasing and has derivative -q0 atzero. Therefore kappa>0. For t>=delta, L_S(t)<=exp(-t/B)(m-kappa), while L_T(t)>=exp(-t/B)(m-epsilon*q)>=exp(-t/B)(m-epsilon). The epsilon<=kappa/2 bound gives strict domination throughout the second region. Thus S<=cx T, with strict stop-loss inequality at every t>0.

I checked the finite-mixture odds bound used for the coefficient estimate as well. With n=c+1, normalized reciprocals y_i and odds r_i=y_i/(1-y_i), the deterministic pair sum obeys n/[2(n-1)]<=sum_(i<j)r_i*r_j<=1. Pair averaging increases the productxy while fixingx+y and decreases the pair sum; merging positive coordinates until onlytwo remain increases it toone. Consequently the symmetric coefficient statistic lies between1/c and2/(c+1).

The size-biased short probability is r_epsilon=epsilon(B-m)/(m(B-epsilon)). All-long draws give the lower statistic1/c, and the union bound for any short draw is(c+1)r_epsilon. This yields exactly

    Delta_c(T)<=m^c(c-1)epsilon(B-m)/(c!*c*(B-epsilon))
              <=2m^c(c-1)epsilon(B-m)/(c!*c*B)
              <=Delta_G/4.

Thus the coefficient difference is at least3Delta_G/4 and gives a reversed delay probability for all sufficiently small positive rates. This addendum supplies a strictly positive comparator for every law in the stated general DFR class. The resulting rate interval remains unquantified, and historical novelty remains unestablished.

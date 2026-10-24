# Independent full audit of the positive general-DFR comparator

2 October 2026. Mathematical audit and a derived strict-mean corollary. Historical novelty, priority, and external expert review remain unestablished.

## Verdict and assumptions

The complete construction in `whitt_general_DFR_positive_comparator.md` is valid. Its hypotheses are c>=2 and a strictly positive service timeS with survival exp(-integral_0^t h), whereh is finite, continuous, nonincreasing, nonconstant, andh(t)>=1/B>0. Letm=ES, M=h(0), andL(t)=E[(S-t)+]. The already audited general-service expansion applies because these assumptions imply finite moments of all orders.

For this law, the coefficient

    K_c(G)=1/(c-1)! integral_0^infinity integral_0^infinity
                     s(u)s(t)L(u+t)^(c-1)du dt

has strict excess Delta_G=K_c(G)-m^(c+1)/(c!*c)>0. That strictness follows from the NWU property of the equilibrium residual law and the nonconstant hazard, as independently audited in `whitt_general_DFR_audit.md`.

The new target is a strictly positive two-component exponential mixture. The construction proves strict stop-loss comparison at every positive service threshold, and reverses delay probability at every sufficiently small arrival rate. It does not quantify the endpoint of this arrival-rate interval.

## Positivity of every construction constant

Becauseh is nonconstant and nonincreasing with lower bound1/B, h(0)>1/B. Thuss(t)<=exp(-t/B), strictly on a positive-length interval, and0<m<B. Henceq0=(B-m)/B>0 anddelta=q0/(4M)>0.

The hazard bound also givesL(t)<=B*s(t). ThereforeJ(t)=exp(t/B)L(t) is nonincreasing, andJ'(0)=m/B-1=-q0<0. It follows that

    kappa=m-exp(delta/B)L(delta)>0.

All terms in the stated minimum

    epsilon=min{delta,m/2,kappa/2,B/2,
                 Delta_G*c!*c*B/[8m^c(c-1)(B-m)]}

are consequently positive. It ensures0<epsilon<m<B andepsilon<=B/2. The target law

    T=epsilon*Exp(1) with probabilityq=(B-m)/(B-epsilon),
      B*Exp(1) with probability1-q=(m-epsilon)/(B-epsilon)

has two strictly positive probabilities and meanm.

## Audit of strict stop-loss ordering near zero

The original hazard upper boundh(t)<=M givesF_S(u)<=Mu. For the target,

    F_T(u)>=q0*(1-exp(-u/epsilon))
           >=q0*u/(epsilon+u).

The latter elementary inequality follows fromexp(x)>=1+x. For0<t<=delta,

    integral_0^t F_T(u)du
       >=q0*t²/[2(epsilon+t)]
       >=q0*t²/(4delta)=M*t²,

whereepsilon<=delta andt<=delta were both used. Meanwhile

    integral_0^t F_S(u)du<=M*t²/2.

The inequalities are correctly normalized, including the factor2 in the integral ofu. They give strict target domination, because for equal means

    E[(X-t)+]=m-t+integral_0^t F_X(u)du.

ThusL_T(t)>L_S(t) throughout0<t<=delta.

## Audit of strict stop-loss ordering beyond delta

SinceJ is nonincreasing,

    L_S(t)<=exp(-t/B)(m-kappa),  t>=delta.

The target stop-loss value is

    L_T(t)=q*epsilon*exp(-t/epsilon)
                +(1-q)*B*exp(-t/B)
           >=exp(-t/B)(m-epsilon*q)
           >=exp(-t/B)(m-epsilon).

The epsilon<=kappa/2 bound makes this strictly larger thanL_S(t). Hence strict stop-loss comparison holds at everyt>0. The means agree atzero, soL_T(0)=L_S(0)=m. The equal-mean stop-loss characterization provesS<=cx T.

## Audit of the target coefficient bound

I independently checked the deterministic finite-mixture bound used here. Forn=c+1 positive coordinatesy_i summing toone, putr_i=y_i/(1-y_i). The pair sum satisfies

    n/[2(n-1)]<=sum_(i<j)r_i*r_j<=1.

Withtwo coordinatesx,y, fixedsumt=x+y<1 andproductz=xy, the part depending on them equals[z+R(t-2z)]/(1-t+z), withR the sum of the other odds. Its derivative with respect toz is[(1-t)-R(2-t)]/(1-t+z)^2<0 becauseR>=1-t>0. Averaging unequal coordinates therefore strictly lowers the sum and converges to the uniform lower endpoint. Merging coordinates decreasesz and raises the sum; stopping when onlytwo positive coordinates remain gives the upper endpointone. Zero coordinates created during merging cause no singularity as long as at leasttwo positive coordinates remain.

Thus the symmetric coefficient statisticT_c lies between1/c and2/(c+1). For the target mixture its size-biased short probability is

    r_epsilon=epsilon(B-m)/(m(B-epsilon)).

All-long samples giveT_c=1/c; the probability of at leastone short amongc+1 samples is at most(c+1)r_epsilon. Consequently

    0<=Delta_c(T)
      <=m^c(c-1)epsilon(B-m)/(c!*c*(B-epsilon))
      <=2m^c(c-1)epsilon(B-m)/(c!*c*B)
      <=Delta_G/4.

The epsilon minimum has precisely the factor8 needed for that final quarter bound. No continuity of exponential mixtures is being assumed in this coefficient estimate.

## Delay comparison conclusion

The independently audited finite-second-moment theorem gives each equal-mean law the expansion

    P(W>0)=m^c*lambda^c/c!
      +[K_c-m^(c+1)/c!]*lambda^(c+1)
      +o(lambda^(c+1)).

Therefore

    P(W_S>0)-P(W_T>0)
      =[Delta_G-Delta_c(T)]*lambda^(c+1)
         +o(lambda^(c+1))>0

for every sufficiently small positive lambda, with leading excess at least3Delta_G/4. Both service distributions are strictly positive. This proves the positive-comparator general-DFR counterexample.

## Derived corollary: strict increasing-convex order at every threshold, including zero

The equal-mean endpointzero can also be made strict, while preserving the reversed waiting comparison. Fixone small rate lambda for which the last strict delay inequality holds. Letgap=P(W_S>0)-P(W_T>0)>0. DefineT_a=aT fora>1 close toone.

The scaling relation for stationary FCFS queues is

    P(W_(aT)(lambda)>0)=P(W_T(a*lambda)>0).

Indeed dividing all time units by a changes arrival rate fromlambda toa*lambda and changesaT back toT; the all-busy event is invariant under this rescaling.

The target busy probability is continuous in arrival rate at this fixed lambda. Here is a direct justification avoiding a general matrix-root regularity claim. Choose lambda_star withlambda<lambda_star<1/B, possible by choosing the original violatinglambda inside the small-rate theorem's range. Couple all input streams near lambda by thinning a single rate-lambda_star marked Poisson process, and start each busy interval with the same fresh target service mark. Couple that mark and every subsequent service withB*Exp(1); the target mixture is dominated job by job. The single-server M/M/1 busy interval atlambda_star, started by that exponential mark, is an integrable common bound for the busy duration and its all-busy reward in every c-server target queue. On each sample path there are finitely many arrivals before the dominating emptying time, and none of their independent thinning marks equalslambda/lambda_star. For rates approachinglambda, their acceptance indicators therefore eventually agree, so the complete target busy path and reward eventually agree. Dominated convergence gives continuity of the mean busy reward and mean busy duration. The regenerative ratio

    P(W_T(z)>0)=E[busy reward atz]/(1/z+E[busy duration atz])

is consequently continuous atz=lambda.

Choosea>1 sufficiently nearone that the target probability at a*lambda differs from its value atlambda by less thangap/2. Then

    P(W_S(lambda)>0)>P(W_(T_a)(lambda)>0).

At the same timeE T_a=a*m>m. For every finite service thresholdt>=0, the unbounded exponential target hasP(T>t)>0, and

    E[(aT-t)+]-E[(T-t)+]
       >=(a-1)E[T*1{T>t}]>0.

SinceL_S(t)<=L_T(t), this proves

    E[(S-t)+]<E[(T_a-t)+]  for everyt>=0.

The increasing-convex stop-loss characterization therefore givesS<=icx T_a with strict integrated-tail ordering at every finite threshold, includingzero. In the cdf orientation of Whitt's equation(2.6),

    integral_t^infinity(F_S(u)-F_(T_a)(u))du
      =E[(T_a-t)+]-E[(S-t)+]>0,  t>=0.

Nevertheless their stationary delay probabilities are reversed. This refutes the corresponding strict-ICX strengthening as well. The choice ofa is existential in this corollary; the base and target laws and the original sufficiently-smalllambda theorem remain explicit.

The reversed delay probabilities also imply a reversal at some strictly positive waiting threshold by right continuity as that threshold decreases tozero. Under the bounded original hazard one can quantify it from a known gapg: the probability that an originally delayed job starts withinh is at mostc*M*h, because a completion is necessary and the total completion intensity is at mostc*M. Thus anyh<g/(c*M) retains a positive reversed tail gap.

## Continuity at the archived explicit rate11/10

The same existence argument applies to the archived two-component finite-rate witness atlambda=11/10, even though its mean-one single-server queue is unstable. Its target component means are1/1000 and8/5. Choose a two-server M/M/2 dominator atlambda_star=6/5 and service rate5/8 per server. Its utilization is24/25, its stationary empty probability is1/49, and its mean nonempty busy interval fromone fresh job is40. This follows from the regenerative identity meanbusy=(1-pi0)/(lambda_star*pi0). Its busy interval is an integrable common bound under the same workload/count coupling. The finite-prefix thinning and regenerative-ratio argument therefore proves target delay-probability continuity at11/10 too.

This gives an existential strict-mean perturbation of that explicit witness without requiring a global QBD Jacobian claim. A separately computed rational certificate for an explicit multiplier is stronger and can be attached after its generator and inequalities have been checked.

## Limits of the audit

This verifies the comparator construction, strict service ordering, coefficient estimate, and the scaling corollary. It does not establish first priority, peer-reviewed acceptance, or an explicit multiplier in the continuity-based corollary. It does not address the weaker conjectures concerning mean waiting time.

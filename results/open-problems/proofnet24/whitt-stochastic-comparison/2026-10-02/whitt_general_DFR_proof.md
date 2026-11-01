# Counterexamples with general decreasing-hazard service laws

2 October 2026. This is a new standalone extension of the finite-hyperexponential theorem. Historical priority and external expert review remain unestablished. The theorem uses a comparator with an atom at zero, permitted in Whitt's original1983 formulation. The separate finite-hyperexponential result supplies strictly positive comparators.

## Assumptions and theorem

Fix an integer c>=2 and B>0. Let G be an absolutely continuous, strictly positive service law whose survival function is

    s(t)=exp(-integral_0^t h(v)dv), t>=0,

where h is finite, continuous, nonincreasing, not constant, and h(t)>=1/B for every t>=0. Put

    L(t)=integral_t^infinity s(v)dv, m=L(0).

Let U be zero with probability1-m/B and exponential with mean B with probabilitym/B. Then G<=cx U. For stationary FCFS M/G/c queues with the same Poisson arrival rate lambda,

    P(W_G>0)>P(W_U>0)

for every sufficiently small positive lambda. Thus the usual stochastic-order implication fails for this general class of nonexponential decreasing-hazard service laws, for every c>=2.

An example beyond finite hyperexponential mixtures is s(t)=exp(-t/B)(1+t)^(-kappa), with kappa>0. Its hazard is 1/B+kappa/(1+t). The proof below applies to this law without approximating it by phases or invoking a general light-traffic analyticity theorem.

## Preliminary domination and stability

The hazard bound gives

    s(t+u)<=s(t)e^(-u/B),
    L(t)<=B s(t).

Thus G is stochastically dominated by a mean-B exponential law. Since L'=-s<=-L/B,

    L(t)<=m e^(-t/B).                              (1)

The equilibrium residual law G_e has survival L(t)/m, so it too is stochastically dominated by a mean-B exponential law.

Fix lambda_0<1/B and consider 0<lambda<=lambda_0. The total unfinished work in the c-server FCFS queue is dominated by that in a work-conserving single-server queue with the same marked Poisson arrivals: whenever its work is positive, the c-server queue drains at total speed at least one. Its services in turn are dominated by independent mean-B exponentials. We therefore have a stationary M/M/1 dominator. All required busy periods and stationary work variables have finite moments in this range. In particular both the waiting and loss queues below are stable.

If a marked initial state x has total remaining work w(x), its time tau to empty under the c-server queue is at most the busy-period time of the single-server workload process started with work w(x). The latter has mean w(x)/(1-lambda m). Hence

    E_x tau<=w(x)/(1-lambda m).                    (2)

This mean identity follows also by stopping the compound-Poisson input-minus-unit-drain workload martingale; domination supplies the integrability required for stopping.

## An exact comparison identity between the waiting and loss queues

Let P_lambda be the stationary all-busy probability of the infinite-capacity waiting queue. Its state records the residual work of jobs currently in service and the known service requirements of FCFS waiting jobs. Marks may be sampled at arrival; this gives a standard piecewise-deterministic Markov process. Let

    f(x)=1{all c servers busy},
    H_lambda(x)=E_x[integral_0^tau (f(X_t)-P_lambda)dt]

for nonempty x, where tau is the first time the waiting queue empties, and set H_lambda(empty)=0. Since |f-P_lambda|<=1, (2) gives the linear-growth bound

    |H_lambda(x)|<=w(x)/(1-lambda m).               (3)

The strong Markov property shows that the extended generator of the waiting queue satisfies

    A_wait H_lambda=-f+P_lambda.                   (4)

For clarity, (4) also holds at empty. A regenerative cycle there consists of an idle interval of mean1/lambda and a busy interval started by one fresh service. If its expected busy reward and busy duration are a and b, then P_lambda=a/(1/lambda+b). Therefore the expected potential after that arrival is a-P_lambda b=P_lambda/lambda, and the generator at empty equals lambda times this expectation, namely P_lambda.

One can avoid classical differentiability of the potential. Before the next deterministic service completion, conditioning on the first exponential arrival gives the value-function identity along the residual-work flow. It makes H_lambda absolutely continuous along that flow and yields (4) almost everywhere. Potential values match the post-completion state at a completion boundary by the strong Markov property. Equivalently, the stopped potential plus the accumulated centered reward is a martingale. These observations give the extended Dynkin identity needed below.

Now run the capacity-c loss queue, rejecting arrivals when all c servers are occupied. On its states, its generator differs from A_wait only by removing the jump that would create a waiting customer. If x is full and x+S denotes the same state with a fresh independent service S added to the waiting line, then

    A_loss H_lambda(x)
      =-f(x)+P_lambda
        -lambda 1{full} E_S[H_lambda(x+S)-H_lambda(x)].   (5)

Apply Dynkin's formula through a complete regenerative cycle of the loss queue, starting and ending empty, and divide by its expected length. This gives

    P_lambda-P_loss(lambda)
      =lambda P_loss(lambda)
         E[H_lambda(R plus waiting S)-H_lambda(R)].      (6)

Here R consists of c iid equilibrium residual service times and S is an independent original service time. The facts used are the standard insensitivity/product-residual stationary law of M/G/c/c: its all-busy probability is Erlang B, and, conditional on having c busy servers, their residual times are independent with survival L(t)/m. PASTA makes this also the full state seen by a rejected arrival.

The unbounded potential in (5) does not require an unproved interchange. Its jump magnitude is bounded using (3) by

    (2w(x)+S)/(1-lambda m).

A loss regenerative cycle is dominated by the single-server M/M/1 busy cycle described above. During that dominating busy cycle, the total work that has arrived is its duration, and every residual work value is bounded by this total. Consequently the absolute Dynkin integrals are bounded in expectation by a constant times the first and second moments of that busy duration, together with its finite idle mean. Stopping first at bounded time and work and then using this domination justifies passage to the full loss cycle. The initial and final potential are both zero, so no stationary boundary term is omitted.

## The limiting gain in the exact identity

For the two random initial states in (6), the c residuals have law G_e and the possible extra waiting requirement has law G. Both are dominated by mean-B exponentials by (1). Their emptying times for all lambda<=lambda_0 can therefore be dominated by an M/M/1 busy period at rate lambda_0, started with c+1 independent mean-B exponential requirements. This random time has a finite second moment and supplies uniform integrability.

Construct all future arrivals by thinning a rate-lambda_0 marked Poisson process. As lambda decreases to zero, eventually none of its finitely many arrivals before the no-arrival emptying time are retained, on each fixed sample path. The waiting trajectories up to that emptying time then coincide with the no-arrival trajectories. Moreover P_lambda tends to zero: the waiting queue's probability of being nonempty is at most the busy probability lambda m of its stationary single-server dominator. The centered reward term therefore vanishes under the uniform busy-period bound. It follows that

    E[H_lambda(R plus waiting S)-H_lambda(R)]
      -> E[H_0(R plus waiting S)-H_0(R)].             (7)

Let R_(1)<=R_(2) be the first two order statistics of the c residuals. With no future arrivals, the full loss state remains all busy for R_(1). If one job waits, it starts at that first completion, and all servers remain busy for the additional time

    min{S,R_(2)-R_(1)}.

Therefore the expectation on the right of (7) equals

    J_c=E[min{S,R_(2)-R_(1)}]
       =c/m^c integral_0^infinity integral_0^infinity
            s(u)s(t)L(u+t)^(c-1)du dt.              (8)

Indeed E[min{S,D}]=integral s(u)P(D>u)du for independent S,D. The equilibrium residual density is s(t)/m, and the event that its two smallest values differ by more than u has probability

    c integral_0^infinity [s(t)/m][L(t+u)/m]^(c-1)dt.

Ties have zero probability because G_e is absolutely continuous.

## A general light-traffic expansion obtained without analyticity

Erlang B gives, for c>=2,

    P_loss(lambda)=m^c lambda^c/c!
      -m^(c+1)lambda^(c+1)/c!+O(lambda^(c+2)).       (9)

Combining the exact identity (6), limit (7), and (8) yields

    P_lambda=m^c lambda^c/c!
      +[K_c-m^(c+1)/c!]lambda^(c+1)
      +o(lambda^(c+1)),                            (10)

where

    K_c=1/(c-1)! integral_0^infinity integral_0^infinity
            s(u)s(t)L(u+t)^(c-1)du dt.              (11)

Only continuity of the regenerative potential at rate zero is used. The proof neither asserts analyticity for general G nor replaces the infinite stationary law by a finite-capacity approximation.

## Decreasing hazard gives a strictly positive coefficient excess

Because h is nonincreasing, s(t+u)>=s(t)e^(-h(t)u), giving L(t)/s(t)>=1/h(t). Its equilibrium residual hazard g(t)=s(t)/L(t) consequently satisfies

    g'(t)=g(t)[g(t)-h(t)]<=0.

Thus L(t)/m has decreasing hazard, hence is log-convex and NWU:

    L(u+t)>=L(u)L(t)/m.                            (12)

Substituting (12) into (11), and using L'=-s, gives

    K_c>=1/[(c-1)!m^(c-1)]
              [integral_0^infinity s(t)L(t)^(c-1)dt]^2
        =m^(c+1)/(c!c).                            (13)

The inequality is strict. If (12) were equality for every u,t, continuity would force L(t)/m to be exponential. Since s(0)=1 and L'=-s, the original survival would then be exponential as well, contrary to the nonconstant h assumption. Hence (12) is strict somewhere and, by continuity, on a set of positive area. The weighting s(u)s(t) is positive everywhere. Since c-1>0, its integral in (11) is strictly increased. Thus

    Delta_c=K_c-m^(c+1)/(c!c)>0.                    (14)

## Convex-order comparator and the contradiction

Equation (1) is the stop-loss transform comparison

    E[(S-t)^+]=L(t)<=m e^(-t/B)=E[(U-t)^+], t>=0.

The two laws have mean m, and nonnegative equal-mean laws are convex ordered exactly when their stop-loss transforms are ordered. Thus G<=cx U.

Deleting zero-work customers from the comparator's workload process leaves an M/M/c queue with arrival rate lambda m/B and service rate1/B. Zero-service arrivals may still wait, but all original arrivals see the positive subsystem's all-busy probability by PASTA. Its offered load is lambda m, so Erlang C gives

    P(W_U>0)=m^c lambda^c/c!
       -(c-1)m^(c+1)lambda^(c+1)/(c!c)
       +O(lambda^(c+2)).                           (15)

Subtracting (15) from (10) and using (14) proves

    P(W_G>0)-P(W_U>0)=Delta_c lambda^(c+1)
                         +o(lambda^(c+1))>0

for every sufficiently small positive lambda, despite G<=cx U. This is the claimed counterexample class.

## Scope of the result

The hazard assumptions are explicit and sufficient; no claim is made here for every DFR law without a positive hazard lower bound, for infinite-mean distributions, or for a strictly positive comparator for every general G. The finite-hyperexponential theorem separately proves strictly positive, two-component comparators for every server count.

The exact finite-rate nine-state certificate in `whitt_nine_state_proof.md` remains an independent elementary example. This extension gives an asymptotic interval of arrival rates without an explicit numerical endpoint for that interval. It does not establish historical priority or resolve the weaker mean waiting-time conjecture.

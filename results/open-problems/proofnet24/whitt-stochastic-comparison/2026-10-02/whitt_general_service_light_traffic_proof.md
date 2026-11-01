# The first service-sensitive delay coefficient for a general M/G/c queue

2 October 2026. Standalone theorem extending the finite-hyperexponential calculation. Historical priority and external expert review are unestablished. This proof uses a regenerative potential and an exact comparison with the loss queue, and requires no general analyticity claim.

## Theorem

Fix c>=2. Let S be any strictly positive service random variable, with mean m>0 and E[S^2]<infinity. The law may be discrete, continuous, or mixed. Let

    s(t)=P(S>t),  L(t)=E[(S-t)^+]=integral_t^infinity s(u)du.

In a stationary FCFS M/G/c queue with Poisson arrival rate lambda,

    P(W>0)=m^c lambda^c/c!
      +[K_c-m^(c+1)/c!]lambda^(c+1)
      +o(lambda^(c+1)),                           (1)

as lambda decreases to zero, where

    K_c=1/(c-1)! integral_0^infinity integral_0^infinity
          s(u)s(t)L(u+t)^(c-1)du dt.               (2)

The equilibrium residual law G_e has survival L(t)/m and mean E[S^2]/(2m). All rates considered below can be restricted to lambda<=lambda_0 with lambda_0 m<1, so a single-server workload dominator is stable.

## Regenerative potential and its growth bound

The state of the infinite queue records every current residual service requirement and every known requirement in the waiting line. Marks may be sampled when customers arrive. Let w(x) be their total unfinished work and f(x) the indicator that all c servers are busy. Write P_lambda for its stationary busy probability.

Whenever the queue is nonempty, total unfinished work drains at speed at least one. A single-server queue with the same arrivals and marks consequently dominates its emptying time. Starting that single-server workload with deterministic initial work w, its mean time to empty is w/(1-lambda m). This is the standard stopped compound-Poisson workload identity; it also follows by a renewal busy-period construction using only finite service mean. Thus, if tau is the c-server queue's first time to empty,

    E_x tau<=w(x)/(1-lambda m).                   (3)

For nonempty x define

    H_lambda(x)=E_x[integral_0^tau (f(X_t)-P_lambda)dt],

and put H_lambda(empty)=0. The growth bound is

    |H_lambda(x)|<=w(x)/(1-lambda m).              (4)

Its extended generator under the waiting queue satisfies

    A_wait H_lambda=-f+P_lambda.                  (5)

For nonempty states this follows from the strong Markov property applied to the potential stopped at empty. It also holds at empty: if a and b are the expected busy reward and duration in a busy interval started by one fresh service, the full regenerative cycle has mean1/lambda+b. Consequently P_lambda=a/(1/lambda+b), and

    E[H_lambda(one fresh job)]=a-P_lambda b=P_lambda/lambda.

The arrival jump generator at empty is therefore P_lambda, as required by (5).

No pointwise smoothness in all service coordinates is needed. Before the next deterministic completion, conditioning on the first Poisson arrival gives, along the deterministic residual-work flow x_t,

    H_lambda(x)=integral_0^v e^(-lambda t)
       [f(x_t)-P_lambda+lambda E_S H_lambda(x_t+S)]dt
         +e^(-lambda v)H_lambda(x_v),

for v smaller than the next completion time. This identity supplies absolute continuity along the flow and (5) almost everywhere. At a completion boundary, the value equals that of the post-completion state by the strong Markov property. Equivalently the stopped potential plus its centered accumulated reward is a martingale. This yields the extended Dynkin formula used below.

## An exact identity using the capacity-c loss queue

Run the M/G/c/c loss queue at the same rate, rejecting an arrival whenever all c servers are busy. On its states, the waiting and loss dynamics are identical except for that rejected arrival. Let x+S denote the state obtained by appending a fresh independent requirement S to a full state x. Hence

    A_loss H_lambda
       =-f+P_lambda
         -lambda 1{full} E_S[H_lambda(x+S)-H_lambda(x)].  (6)

The loss queue has stationary population probabilities

    pi_j=(lambda m)^j/(j! Z_c(lambda m)),
    Z_c(z)=sum_(j=0)^c z^j/j!,                     (7)

and conditional on population j its residual service times are j independent draws from G_e. A verification of this standard product-residual law is given below. In particular its stationary expected total unfinished work is finite:

    E_loss w<=c E[S^2]/(2m)<infinity.              (8)

Apply Dynkin's formula to H_lambda over a fixed deterministic interval [0,T], with the loss process initially stationary. The unbounded potential presents no integrability gap. From (4), its arrival difference is bounded by

    |H_lambda(x+S)-H_lambda(x)|
       <=(2w(x)+S)/(1-lambda m).

On the fixed interval, all loss workload values are bounded by

    w(X_0)+sum_(arrivals up to T) S_i.

This is integrable by (8) and finite service mean. It dominates the stopped endpoint potentials and, up to deterministic constants, the integrated absolute generator in (6). The compensated arrival sums have the same integrable bound in expectation. Localizing first at bounded time and work, and then using this fixed-interval domination, justifies the extended Dynkin formula without requiring a loss busy-period second moment. Stationarity cancels its expected endpoint potentials.

More explicitly, the sum of the absolute arrival jumps is bounded by a constant times N_T w(X_0)+(2N_T+1)sum_(arrivals up to T)S_i, where N_T is the finite Poisson arrival count. Its expectation is finite using E[N_T^2]<infinity, finite service mean, and independence of the initial stationary state from future arrivals. This also gives uniform integrability for the localized compensated-jump martingales.

Let P_loss(lambda)=pi_c. Using the product-residual law in (6) gives the exact identity

    P_lambda-P_loss(lambda)
       =lambda P_loss(lambda)
          E[H_lambda(R plus waiting S)-H_lambda(R)],    (9)

where R contains c iid equilibrium residuals and the extra S has the original law, independently. This identity holds for each sufficiently small positive rate, not only asymptotically.

## Continuity of the potential at rate zero

Both random initial states in (9) have finite expected total work, because

    E[sum R_i+S]=c E[S^2]/(2m)+m<infinity.

Couple all future inputs by thinning a rate-lambda_0 marked Poisson process with the original service marks. The single-server workload at rate lambda_0, started with all c residuals and the extra requirement, dominates the emptying times of both c-server initial states at every lambda<=lambda_0. Its mean emptying time is the expected initial work divided by1-lambda_0 m, which is finite. It supplies an integrable common dominating random variable.

On every sample path the no-arrival emptying time is finite, and the dominating rate-lambda_0 process has only finitely many arrivals before it. For all sufficiently small thinning probabilities none of these arrivals is retained. Thus the rate-lambda trajectories eventually coincide with their no-arrival trajectories up to empty.

Also P_lambda<=lambda m. Indeed the same-service stationary M/G/1 workload dominates the c-server queue's total work, so its nonempty probability lambda m bounds the c-server all-busy probability. Dominated convergence therefore gives

    E[H_lambda(R plus waiting S)-H_lambda(R)]
       ->E[H_0(R plus waiting S)-H_0(R)].           (10)

This proves only the continuity required here; it does not assert differentiability or analyticity of the whole general-service stationary law.

## Compute the limiting gain and the coefficient

Let R_(1)<=R_(2) be the two smallest of the c iid residuals. G_e is absolutely continuous, with density s(t)/m, even if the original service law is discrete. There are therefore no residual ties with positive probability.

Without arrivals, a full state stays all busy for R_(1). An extra waiting job starts at that first completion and extends the all-busy interval by

    min{S,R_(2)-R_(1)}.

It follows that the limiting expectation in (10) is

    J_c=E[min{S,R_(2)-R_(1)}]
       =c/m^c integral_0^infinity integral_0^infinity
            s(u)s(t)L(t+u)^(c-1)du dt.             (11)

To obtain the integral, use E[min(S,D)]=integral s(u)P(D>u)du and

    P(R_(2)-R_(1)>u)
      =c integral_0^infinity [s(t)/m][L(t+u)/m]^(c-1)dt.

Notice that J_c<=m, so this integral is finite without an additional assumption.

For c>=2, expanding Erlang B in (7) gives

    P_loss(lambda)=m^c lambda^c/c!
      -m^(c+1)lambda^(c+1)/c!+O(lambda^(c+2)).      (12)

Substitute (10)--(12) into (9). Its extra coefficient is m^c J_c/c!=K_c, giving exactly (1) and (2).

## Verification of the loss product-residual law

On an unordered state with j residuals, the invariant measure before normalization has symmetric density

    lambda^j/j! product_(i=1)^j s(r_i) dr_i,
    0<=j<=c.                                     (13)

Its total mass is (lambda m)^j/j!, proving the normalization (7). For a bounded test function matching the lower-dimensional state whenever a residual reaches zero, integrate the deterministic unit-drain term by parts in each residual coordinate. The boundary flux from level j exactly cancels the rejected-free arrival loss at level j-1; the interior Stieltjes term dG in that integration cancels the fresh-service arrival gain from level j-1. At level c, there is no arrival loss because arrivals are rejected and no level c+1 boundary flux. The j! factor cancels the j choices of a completing coordinate. These cancellations prove invariance. Lebesgue-Stieltjes integration handles service atoms, so a service density is unnecessary. Regeneration at empty and finite mean cycles give uniqueness. Conditional on level j, (13) is exactly j iid residual densities s/m.

## Corollary: general decreasing-hazard counterexamples

Assume in addition that S has finite continuous nonincreasing nonconstant hazard h(t)>=1/B>0. Then s(t+u)<=s(t)e^(-u/B), so G is dominated by a mean-B exponential and has finite second moment. Also L<=B s and L'=-s yield

    L(t)<=m e^(-t/B).

The equal-mean service law U, zero with probability1-m/B and mean-B exponential with probabilitym/B, has stop-loss transform m e^(-t/B). The stop-loss characterization therefore gives G<=cx U.

The equilibrium residual hazard g=s/L satisfies g'=g(g-h)<=0, since the original decreasing hazard gives L/s>=1/h. Thus its survival L/m is NWU:

    L(u+t)>=L(u)L(t)/m.

Using this inequality in (2), together with integral s L^(c-1)=m^c/c, yields

    K_c>=m^(c+1)/(c!c).

The inequality is strict for the stated nonconstant hazard. Equality of the residual NWU inequality everywhere would force L/m exponential by continuity, which, because s(0)=1 and L'=-s, would force the original service law exponential. Otherwise NWU is strict on an open rectangle, and its positive weight s(u)s(t) makes the integral strict.

Deleting zero-work jobs from the comparator workload leaves an M/M/c queue with offered load lambda m. All original arrivals, including zero-service customers, see its all-busy probability by PASTA. Erlang C has expansion

    P(W_U>0)=m^c lambda^c/c!
       -(c-1)m^(c+1)lambda^(c+1)/(c!c)
       +O(lambda^(c+2)).

Consequently (1) gives

    P(W_G>0)-P(W_U>0)
      =[K_c-m^(c+1)/(c!c)]lambda^(c+1)
        +o(lambda^(c+1))>0

for every sufficiently small positive lambda. This reverses delay probability under convex-order domination and contradicts the full stochastic waiting-time assertion.

This corollary includes laws that are not finite exponential mixtures. For example the continuous decreasing hazard h(t)=1/B+kappa max(1-t,0), kappa>0, gives survival

    exp(-t/B-kappa(t-t^2/2)) for0<=t<=1,
    exp(-t/B-kappa/2) for t>=1.

Its survival is not a finite exponential mixture because its second derivative has a jump at1. The theorem applies directly. This corollary uses the zero-plus-exponential comparator. A strictly positive two-exponential comparator under these bounded-hazard assumptions, with strict stop-loss inequality at every positive threshold, is constructed in the companion note `whitt_general_DFR_positive_comparator.md`.

## Controls and limits of the claim

For exponential service of mean m, formula (2) gives K_c=m^(c+1)/(c!c), agreeing with Erlang C. For deterministic service of length m, it gives K_c=m^(c+1)/(c!(c+1)), another exact check on the coefficient and normalization. The all-server exact Fraction tests for finite hyperexponential laws give independent finite-state checks of the same formula.

The theorem supplies an asymptotic expansion and a small-rate existence interval, not an explicit arrival-rate endpoint. The separate nine-state certificate gives a literal finite-rate counterexample. None of these calculations establishes historical novelty or settles the weaker mean waiting-time conjecture.

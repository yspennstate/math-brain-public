# Strictly positive comparators for the general decreasing-hazard counterexamples

2 October 2026. Standalone corollary of the general-service coefficient theorem and the finite-hyperexponential coefficient inequality. Historical priority and external expert review remain unestablished.

## Theorem and explicit construction

Fix c>=2. Let S have survival s(t)=exp(-integral_0^t h(u)du), where h is finite, continuous, nonincreasing, nonconstant, and h(t)>=1/B>0. Write

    m=E[S], M=h(0), L(t)=E[(S-t)^+], q_0=(B-m)/B,
    delta=q_0/(4M),
    kappa=m-e^(delta/B)L(delta),
    Delta_G=K_c(G)-m^(c+1)/(c!c),

where

    K_c(G)=1/(c-1)! integral_0^infinity integral_0^infinity
               s(u)s(t)L(u+t)^(c-1)du dt.

The audited general-service theorem gives Delta_G>0. Also 0<m<B and kappa>0, as shown below. Thus the following explicit epsilon is positive:

    epsilon=min{delta, m/2, kappa/2, B/2,
                 Delta_G c!cB/[8m^c(c-1)(B-m)]}.        (1)

Let T_epsilon be the strictly positive two-component hyperexponential law

    epsilon E with probability q_epsilon=(B-m)/(B-epsilon),
    BE with probability 1-q_epsilon=(m-epsilon)/(B-epsilon),

with E exponential of mean one. Both component probabilities are strictly between zero and one, and E[T_epsilon]=m.

Then S<=cx T_epsilon, with the stronger strict stop-loss inequality

    E[(S-t)^+]<E[(T_epsilon-t)^+] for every t>0.        (2)

Nevertheless, in stationary FCFS M/G/c queues sharing Poisson rate lambda,

    P(W_S>0)>P(W_(T_epsilon)>0)

for every sufficiently small positive lambda. Both service laws are strictly positive, and the stop-loss comparison is strict at every positive threshold.

## The constants are positive

The hazard lower bound gives s(t)<=e^(-t/B). Because a nonconstant continuous nonincreasing h must have h(0)>1/B, the survival inequality is strict on an interval of positive length. Therefore m<B and q_0>0; M>=1/B>0, so delta>0.

The same hazard bound gives L(t)<=B s(t). Consequently

    J(t):=e^(t/B)L(t)

is nonincreasing, since J'(t)=e^(t/B)[L(t)/B-s(t)]<=0. At zero, J'(0)=m/B-1=-q_0<0. It thus drops strictly before any positive threshold delta, and

    kappa=m-J(delta)>0.

Each term in the minimum (1) is positive. Its m/2 bound ensures epsilon<m<B, so the stated mixture probabilities are valid; its B/2 bound permits the coefficient estimate below.

## Strict convex ordering: two threshold regions

Let F_S and F_T be the two cdfs. Because h(t)<=M,

    F_S(u)=1-s(u)<=1-e^(-Mu)<=Mu.                    (3)

The short exponential component of T_epsilon gives

    F_T(u)>=q_epsilon(1-e^(-u/epsilon))
           >=q_0 u/(epsilon+u).                    (4)

Here q_epsilon>=q_0 and 1-e^(-x)>=x/(1+x) for x>=0. For 0<t<=delta, epsilon<=delta and (4) imply

    integral_0^t F_T(u)du
      >=q_0 t^2/[2(epsilon+t)]
      >=q_0 t^2/(4delta)=M t^2.

Equation (3) gives integral_0^t F_S(u)du<=M t^2/2. Since both laws have mean m and

    E[(X-t)^+]=m-t+integral_0^t F_X(u)du,

we obtain the strict stop-loss inequality (2) throughout 0<t<=delta.

For t>=delta, nonincreasing J gives

    L(t)<=e^(-t/B)(m-kappa).                        (5)

The stop-loss transform of the two-component law is

    L_T(t)=q_epsilon epsilon e^(-t/epsilon)
              +(1-q_epsilon)B e^(-t/B)
           >=e^(-t/B)(m-epsilon q_epsilon)
           >=e^(-t/B)(m-epsilon).

Since epsilon<=kappa/2, this is strictly greater than (5). Thus (2) holds for every positive t. At t=0 both stop-loss values equal m. The equal-mean stop-loss characterization now proves S<=cx T_epsilon.

## The coefficient excess of the new law is smaller

For a finite hyperexponential law of mean m, the completed all-server theorem expresses its excess over the exponential delay coefficient as

    Delta_c=m^(c+1)/c! (E[T_c]-1/c),

where T_c is a symmetric function of c+1 iid size-biased class means. Its deterministic bounds are

    1/c<=T_c<=2/(c+1).

For T_epsilon, the size-biased short-component probability is

    r_epsilon=epsilon(B-m)/(m(B-epsilon)).

If all c+1 class draws are long, T_c=1/c. The probability of at least one short draw is at most (c+1)r_epsilon. Therefore

    0<=Delta_c(T_epsilon)
      <=m^c(c-1)epsilon(B-m)/(c!c(B-epsilon))
      <=2m^c(c-1)epsilon(B-m)/(c!cB)
      <=Delta_G/4,                                (6)

where the second bound uses epsilon<=B/2 and the last uses (1). This is an explicit bound; it does not rely on an unquantified convergence of mixtures.

The general-service light-traffic theorem gives, for each of these equal-mean laws,

    P(W>0)=m^c lambda^c/c!
       +[K_c-m^(c+1)/c!]lambda^(c+1)
       +o(lambda^(c+1)).

Subtracting the two expansions and using (6) yields

    P(W_S>0)-P(W_(T_epsilon)>0)
      =[Delta_G-Delta_c(T_epsilon)]lambda^(c+1)
          +o(lambda^(c+1))>0

for every sufficiently small positive rate, with a leading positive gap coefficient at least3Delta_G/4.

## Dependencies and scope

The general coefficient and strict DFR excess are proved in `whitt_general_service_light_traffic_proof.md`. The deterministic symmetric bounds for finite mixtures are proved in `whitt_all_servers_light_traffic_proof.md` and have independent exact arithmetic checks. The service-law comparison in this note is elementary and separate from those queue calculations.

This note supplies an explicit positive service distribution and an asymptotic interval of counterexample arrival rates; it does not quantify that rate interval. The nine-state exact certificate separately supplies an explicit finite rate. The strict comparison here holds at every positive service stop-loss threshold; it is equality at threshold zero because the means agree. Therefore any proposed strengthened condition requiring strict inequality even at zero must be distinguished from a condition imposing strictness only at positive thresholds.

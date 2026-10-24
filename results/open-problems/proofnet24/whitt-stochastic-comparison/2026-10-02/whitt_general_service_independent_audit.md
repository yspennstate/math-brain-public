# Independent audit: regenerative light-traffic identity and DFR extension

2 October 2026. The regenerative argument is mathematically valid under
the explicit DFR assumptions in `whitt_general_DFR_proof.md`. A stronger
general-service coefficient statement also follows using fixed-time
stationary Dynkin rather than stopping at a full regenerative cycle.
This note checks internal correctness and does not establish priority.

## General-service hypotheses sufficient for the coefficient

Let S>0 almost surely, m=E S in (0,infinity), and E S^2<infinity.
Fix c>=2 and lambda0 m<1. A service law may have positive atoms: the
equilibrium residual law is still continuous with density P(S>t)/m.
Use fully marked FCFS states, recording residual work of the jobs in
service and requirements of jobs waiting. Write w(x) for total work.

The total work in the c-server waiting system is bounded by a single
server work-conserving queue with the same arrival times and service
marks. Whenever the original system is nonempty it processes work at
speed at least one. The single-server busy period started with
deterministic work w has expectation w/(1-lambda m). This can be proved
by the subcritical busy-period branching construction; no second moment
of the busy period is required. Thus expected time until empty is at
most that quantity. A cycle started by a fresh service has finite mean,
so the waiting system admits the regenerative stationary distribution.

Let P_lambda be its stationary all-busy probability and define

    H_lambda(x)=E_x integral_until_empty (f-P_lambda)dt,
    f=1{all c servers busy}, H_lambda(empty)=0.

Then

    |H_lambda(x)|<=w(x)/(1-lambda0 m).                (A)

This is the key uniform linear bound.

## Extended Poisson equation, including empty

Until the next empty time, the strong Markov reward identity makes the
potential plus accumulated centered reward a martingale. On intervals
between deterministic service completions, first-arrival conditioning
gives absolute continuity of the potential along the residual flow and
the extended generator equation

    A_wait H_lambda=-f+P_lambda.

At completion boundaries the same stopped reward identity supplies the
post-completion potential, so no omitted boundary reward occurs.

At empty, write a for expected busy reward of the following busy period
and b for its expected duration. The regenerative ratio is
P_lambda=a/(1/lambda+b). Expected potential after the first new service
is a-P_lambda b=P_lambda/lambda. The arrival generator therefore equals
P_lambda at empty as required. Centering is essential for this check;
the uncentered busy reward would not solve the same global equation.

## Exact waiting/loss identity and unbounded Dynkin justification

On capacity-c loss states the two processes have identical residual
drift, service completions, and nonfull arrival transitions. Loss removes
only a full-state arrival. Therefore

    A_loss H_lambda(x)=-f(x)+P_lambda
      -lambda f(x) E_S[H_lambda(x+S)-H_lambda(x)].    (B)

The loss stationary law has Erlang-B population probabilities. Conditional
on a fixed population its residuals are iid equilibrium residuals G_e.
This product-residual law follows, for example, by checking the weak
residual-flow stationary equations against weights proportional to
lambda^n/n! times the product of the survival densities P(S>r_i).
The weights normalize by sum_{j=0}^c (lambda m)^j/j!. This remains true
with discrete original services; G_e itself has the stated continuous
density. In particular

    E_loss w <= c E S^2/(2m)<infinity.

Here is a justification of stationary Dynkin requiring only this first
work moment. For a fixed deterministic T, along loss paths

    sup_{t<=T}w(X_t)<=w(X_0)+sum_{arrival t<=T}S_t=:Z_T,
    E Z_T<infinity.

Using (A), the generator right side in (B) is bounded in absolute value
by 1+lambda(2w(x)+m)/(1-lambda0m). Stop at bounded time, work, and jump
count. The stopped potential and its Dynkin integral are dominated by
an integrable constant multiple of

    Z_T+T[1+lambda(2Z_T+m)/(1-lambda0m)].

Dominated convergence therefore removes localization and gives true
fixed-time Dynkin expectation. Stationarity cancels its endpoint
potentials, whose expectations exist by (A). Hence E_loss A_loss H=0.

Let R consist of c independent G_e residuals and let a fresh S be
independent. The exact identity is consequently

    P_lambda-P_loss(lambda)
      =lambda P_loss(lambda)
          E[H_lambda(R+waiting S)-H_lambda(R)].      (C)

The sign and the normalization are correct. No assertion that finite
capacity approximates the waiting queue is needed for (C).

## Rate-zero limit and the light-traffic coefficient

Use one rate-lambda0 marked Poisson stream and uniform thinning to
construct all lambda<=lambda0 arrival streams. For each deterministic
finite-work initial state, a single-server busy period at lambda0
dominates all resulting empty times and has finite expectation.
On each sample path there are only finitely many candidate arrivals
before the no-arrival empty time; for sufficiently small lambda none is
retained. The original paths then coincide up to empty. Also
P_lambda tends to zero, either by the regenerative bound or by comparison
with the same-service M/G/1 queue whose busy fraction is lambda m.
Dominated convergence yields H_lambda(x)->H_0(x).

The Palm initial total work in (C) has finite expectation: each G_e mean
is E S^2/(2m), and the added original service has mean m. Bound (A)
therefore permits another dominated convergence under these initial
states. Thus the gain in (C) tends to

    J_c=E min{S,R_(2)-R_(1)}.

Without future arrivals, a full state stays busy until its first
completion. One waiting job adds exactly the minimum of its requirement
and the gap between the first two old residual completions. This proves
the displayed expression, including for discrete original S: iid G_e
residuals have no ties.

Writing s(t)=P(S>t), L(t)=integral_t^infinity s(v)dv gives

    J_c=c/m^c integral integral s(u)s(t)L(u+t)^(c-1)du dt.

For any gap t>0, choose which residual is first, use its density s(u)/m,
and require all remaining residuals to exceed u+t. Tonelli is legitimate
because all integrands are nonnegative, and J_c<=m makes the integral
finite.

Erlang B and (C) therefore prove

    P_lambda=m^c lambda^c/c!
       +(K_c-m^(c+1)/c!)lambda^(c+1)+o(lambda^(c+1)),
    K_c=1/(c-1)! integral integral s(u)s(t)L(u+t)^(c-1)du dt.

The general-service conclusion is a little-o expansion. It does not
assert analyticity or an O(lambda^(c+2)) remainder. This distinction
separates it correctly from the finite-hyperexponential theorem.

## Strict DFR sign and convex comparator

Under the DFR proof's finite continuous nonconstant hazard h>=1/B,
S and G_e are dominated by mean-B exponentials. Mean residual life
L(t)/s(t) is nondecreasing under DFR, so the equilibrium residual
hazard s(t)/L(t) is nonincreasing. Therefore

    L(u+t)>=L(u)L(t)/m.

Substitution into the coefficient integral gives

    K_c>=1/[(c-1)!m^(c-1)]
             [integral s(t)L(t)^(c-1)dt]^2
        =m^(c+1)/(c!c).

If equality held in the residual NWU identity everywhere, continuity
would make L/m multiplicative, hence exponential. Since L'=-s and
s(0)=1, this would make G exponential. Thus a nonexponential DFR law
has strict inequality on an open set of positive area. Positive
survivals and c>=2 give a strictly larger coefficient.

The lower hazard bound yields L(t)<=m exp(-t/B), which is exactly the
equal-mean stop-loss comparison with U equal to zero with probability
1-m/B and B times a unit exponential with probability m/B. Thus G<=cx U.
Thinning zero jobs from its workload gives M/M/c offered load lambda m.
The Erlang-C next coefficient matches the equality case above, proving
the asserted reversed delay probability for all sufficiently small
positive lambda.

No strictly positive two-exponential comparator is asserted for every
general G. That stronger construction is separately proved for finite
hyperexponential laws. The general service coefficient requires only
E S^2<infinity; DFR and the lower hazard bound are additional hypotheses
used for the strict sign and the displayed convex comparator.

## Separate strict stop-loss corollary

`whitt_strict_stop_loss_corollary.md` also passes. The positive endpoint
martingale coupling straddles the stop-loss kink on E in (t/B,t/epsilon),
an event of positive probability for every t>0. Conditional Jensen is
strict there. Both integrated-cdf signs are correct: the integral from
zero to t of F_S-F_T is negative, while its integral from t to infinity
is positive.

The baseline completion intensity is at most ten. A positive wait ending
within h requires a completion, so its probability is at most 10h.
Together with the verified H2 finite-rate gap >1/400 this gives a gap
>3/1250 at waiting threshold h=1/100000. The archived H2 certificate
uses probability 200/533 and records a lower delay gap about .00250608;
it is distinct from the earlier three-class example with a smaller gap.

Final audit verdict: the exact identity, general finite-second-moment
coefficient argument, DFR strict-sign extension, and strict-stop-loss
corollary are internally correct with the stated scope. Historical
priority, external review, and an explicit asymptotic rate endpoint are
not supplied by this audit.

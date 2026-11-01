# A nine-state certificate against Whitt's stochastic waiting-time conjecture

2 October 2026. Complete exact argument for the assertion as stated in the primary source. Historical priority and external expert review are not established.

Whitt's 1983 Conjecture 1.1 states that, for a stationary M/G/s FCFS queue with fixed Poisson arrivals and homogeneous servers, increasing the iid service distribution in increasing convex order increases waiting until service begins in usual stochastic order. The author-hosted primary paper is https://www.columbia.edu/~ww2040/comparisonConjectures1983.pdf ; Conjecture 1.1 appears on p.203, and pp.207–208 explicitly include service laws with an atom at zero. The reference is Operations Research Letters 2 (1983), 203–209, doi:10.1016/0167-6377(83)90026-3.

## Service distributions and convex ordering

Use two servers and arrival rate lambda=1/10. Let E be exponential with mean one, independent of a service-class mark. Define

    S = E/2 with probability2/3, or2E with probability1/3;
    U = 0 with probability1/2, or2E with probability1/2.

Both means are one, so both utilizations are 1/20. Both queues are stable; in fact their services are dominated job by job by 2E, whose M/M/2 utilization at this arrival rate is 1/10.

Couple the laws by keeping the large base class unchanged. In the small class replace E/2 by zero with probability3/4 and by2E with probability1/4. The conditional mean replacement is E/2. The positive-class probability is 1/3+(2/3)(1/4)=1/2. Therefore E[U|S]=S, which proves S<=cx U by conditional Jensen and hence S<=icx U.

## The larger service law has an exact delay probability

Zero-service customers may wait, but add no workload. Deleting them only from the workload process preserves every positive service start and the waiting time of each virtual arrival. Independent thinning leaves a positive-job M/M/2 queue with arrival rate (1/10)(1/2)=1/20 and service rate1/2 at each server. PASTA applies to all original arrivals, including zero-service customers, so their delay probability is the stationary busy probability of that subsystem.

Its utilization is rho=1/20. The elementary Erlang-C formula gives

    P(W_U>0)=2rho^2/(1+rho)=1/210.

This agrees with the zero-plus-exponential insensitivity formula already established in Section6 of Whitt's primary paper.

## A smaller finite queue bounds the base delay from below

Keep the base service law S and arrival rate1/10, but admit an arriving customer only if fewer than three customers are present. This means two possible customers in service and at most one waiting. Rejected arrivals perform zero work. Couple this queue and the infinite-capacity base queue with the same arrivals and same service marks for every admitted customer.

For the sorted two-server workload vector just before successive arrivals, the Kiefer–Wolfowitz recursion adds the new service to the smaller coordinate, subtracts the next interarrival time from both coordinates, takes positive parts, and sorts. Each of these operations preserves componentwise order. Every rejected service in the finite queue is replaced by zero, so its workload stays below the infinite queue's workload. Each admitted customer starts and finishes no later in the finite queue than its counterpart in the infinite queue. Thus the number of unfinished customers in the finite queue is at most that in the infinite queue at each time. Starting in the distant past yields the stationary domination as well. Hence

    P(W_S>0) = P(infinite base count>=2)
              >=P(finite base count>=2).

The finite probability is used only as a rigorous lower bound; it is not substituted for the infinite stationary distribution.

## Nine states and a literal integer stationary certificate

One may defer sampling the exponential service class until a customer's service starts, because its own pre-service wait does not depend on its independent service mark. Thus no mark for the sole waiting customer needs to be included in the state.

Order the finite Markov states as

    empty, 1L, 1S, 2LL, 2LS, 2SS, 3LL, 3LS, 3SS.

S and L identify the small(rate2) and large(rate1/2) jobs currently in service; the initial numeral is total customer count. At count3, one customer waits. The generator Q is the following integer matrix divided by30:

    [ -3,  1,  2,   0,   0,    0,   0,   0,    0]
    [ 15,-18,  0,   1,   2,    0,   0,   0,    0]
    [ 60,  0,-63,   0,   1,    2,   0,   0,    0]
    [  0, 30,  0, -33,   0,    0,   3,   0,    0]
    [  0, 60, 15,   0, -78,    0,   0,   3,    0]
    [  0,  0,120,   0,   0, -123,   0,   0,    3]
    [  0,  0,  0,  10,  20,    0, -30,   0,    0]
    [  0,  0,  0,  20,  45,   10,   0, -75,    0]
    [  0,  0,  0,   0,  40,   80,   0,   0, -120].

For example, from3LS a small completion(rate2) replaces the small job by a fresh small(probability2/3) or large(probability1/3), while a large completion(rate1/2) similarly chooses a replacement. The resulting scaled downward rates to2LL,2LS,2SS are20,45,10. At count3 arrivals are rejected and cause no state transition.

The positive integer row vector

    w=(28428000,1893800,947950,60780,63950,15880,6078,2558,397)

satisfies w(30Q)=0 by integer multiplication. Its sum is31419393, and the sum over the last six states is149643. Since the finite chain is irreducible, w/sum(w) is its stationary distribution. Consequently

    P(finite base count>=2)=149643/31419393=49881/10473131.

Comparing the two exact fractions now gives

    P(W_S>0)-P(W_U>0)
      >=49881/10473131-1/210
       =1879/2199357510>8/10000000>0.

Although S<=cx U, the base queue has strictly larger delay probability. This contradicts usual stochastic ordering and therefore the asserted implication in Conjecture1.1.

## An explicit positive tail threshold

In the base queue, a delayed customer cannot start service before at least one of the two currently busy services completes. The combined exponential completion rate is at most4. Thus P(0<W_S<=h)<=4h. At h=1/10000000,

    P(W_S>h)-P(W_U>h)
      >=1879/2199357510-4/10000000
       >4/10000000>0.

The reversed order therefore persists at a strictly positive waiting-time threshold.

## Reproduction and scope

`whitt_nine_state_exact.py` constructs this generator from the transition rules, solves the finite stationary equations with Fraction arithmetic, checks every exact balance equation, reproduces the literal integer vector above, and checks both decisive rational inequalities. It requires only Python's standard library:

    python whitt_nine_state_exact.py

The argument is also hand-checkable from the displayed9x9 integer matrix and vector. It does not depend on simulation, a numerical infinite-chain root, or an uncontrolled finite-buffer approximation. It refutes the full stochastic-order assertion and leaves weaker mean waiting-time conjectures unaddressed. Searches so far have not located a prior refutation, but absence from search results is not proof of novelty.

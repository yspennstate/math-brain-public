# Strict stop-loss comparisons do not restore Whitt's stochastic conclusion

2 October 2026. This is a corollary of the independently checked strictly positive finite-rate counterexample, not an independent new counterexample. Historical novelty and priority remain unverified.

Whitt (1983), Section 2, after equation (2.5), proposes a stronger hypothesis in equation (2.6): require strict inequality of the integrated service tails at every positive threshold. The endpoint zero necessarily has equality for distributions with equal means. The counterexample archived in `whitt_two_phase_positive_exact.py` satisfies this strengthened hypothesis and still reverses a waiting-time tail at a strictly positive threshold.

## Service laws and exact martingale coupling

Let E have the unit-mean exponential distribution. At Poisson arrival rate lambda=11/10 and with two FCFS servers, take

    S = (1/5) E with probability 3/7,
        (8/5) E with probability 4/7;

    T = (1/1000) E with probability 200/533,
        (8/5) E with probability 333/533.

Both means are 1. To construct the coupling, keep the high class unchanged. In the low class replace (1/5)E by (1/1000)E with probability 1400/1599, or by (8/5)E with probability 199/1599, using the same E. The conditional expectation after replacement is (1/5)E. Thus E[T | original class, E]=S, and conditional Jensen gives S <=cx T.

For every t>0 the comparison of stop-loss transforms is STRICT:

    E[(S-t)+] < E[(T-t)+].                       (1)

Indeed, on the low class and on the event

    t/(8/5) < E < t/(1/1000),

the two possible replacement values lie on opposite sides of the kink of x -> (x-t)+. Both replacement probabilities are positive. Conditional Jensen is strictly unequal on this event, which has positive probability for every t>0. Integrating proves (1). This argument also proves strictness for every all-server finite-mixture construction whose epsilon is below all original class means and whose upper endpoint exceeds at least one original class mean.

Equivalently, writing service cdfs F_S,F_T,

    integral_0^t (F_S(u)-F_T(u))du
      = E[(S-t)+]-E[(T-t)+] < 0,

and, in the tail-integral orientation of Whitt's equation (2.6),

    integral_t^infinity (F_S(u)-F_T(u))du
      = E[(T-t)+]-E[(S-t)+] > 0.

The first sign follows from E[(X-t)+]=m-t+integral_0^t F_X(u)du. Equal means give the necessary equality at t=0.

## A strictly positive waiting threshold

The exact killed-chain certificate already archived establishes, for the genuine infinite queues,

    P(W_S>0)-P(W_T>0) > 1/400.

The base queue has at most two simultaneous exponential service phases, each with rate at most 5. If 0<W_S<=h, at least one service completion occurs during the interval of length h after the tagged arrival. A counting-process compensator bound therefore gives

    P(0<W_S<=h) <= 10h.

Consequently

    P(W_S>h)-P(W_T>h)
       >= P(W_S>0)-P(W_T>0)-10h.

For h=1/100000 this proves

    P(W_S>1/100000)-P(W_T>1/100000) > 3/1250.

Thus the stochastic conclusion fails even with equal means, strictly positive continuous service laws, strict stop-loss comparison at EVERY positive service threshold, and an explicit strictly positive waiting threshold. This does not address the weaker mean waiting-time conjecture.

## Sources and verification

Primary assertion: W. Whitt, "Comparison conjectures about the M/G/s queue", Operations Research Letters 2 (1983), 203-209, Conjecture 1.1 and equations (2.5)-(2.6), https://www.columbia.edu/~ww2040/comparisonConjectures1983.pdf .

The full exact certificate, truncation-to-infinite-queue argument, rational stationary equations and independently implemented checks are archived beside this file. In particular `whitt_two_phase_positive_checks.json` records the certified lower and upper bounds; these are not simulation estimates.

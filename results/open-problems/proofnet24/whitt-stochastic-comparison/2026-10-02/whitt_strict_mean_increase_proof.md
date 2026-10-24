# A finite-rate counterexample with a strictly larger service mean

2 October 2026. Derived from the independently audited strictly positive H2 counterexample, with a fresh exact rational infinite-queue certificate. Historical priority remains unverified.

Take two FCFS servers and Poisson arrival rate lambda=11/10. Let E be unit-mean exponential. The base service law is

    S=(1/5)E with probability 3/7,
      (8/5)E with probability 4/7.

Let the intermediate law T have components (1/1000)E and (8/5)E with probabilities 200/533 and 333/533. The archived martingale coupling proves S<=cx T, with means equal to1: conditional on the base short class, use the same E and replace its coefficient 1/5 by 1/1000 with probability1400/1599 or 8/5 with probability199/1599; keep the long class unchanged.

Set beta=10001/10000 and U=beta T. Its components are strictly positive, both exponential, and its mean is beta>1. Pointwise under the scaling coupling U>T almost surely. Thus S<=icx U. More explicitly, for every finite threshold t>=0,

    E[(U-t)^+]>E[(T-t)^+]>=E[(S-t)^+].

The first inequality is strict because T has positive probability above every finite t, and beta>1. This includes t=0, where the stop-loss gap is beta-1. Consequently the integrated cdf condition

    integral_t^infinity (F_S(u)-F_U(u))du>0

holds for EVERY t>=0. It even satisfies the literal strict-at-zero version of the stronger condition suggested in Whitt (1983), equation(2.6).

Nevertheless the fresh exact certificate `whitt_strict_mean_increase_exact.py` proves for the genuine infinite waiting queues

    P(W_S>0)-P(W_U>0)>12/5000.

The code uses arrival11/10, the actual scaled target service rates 1000/beta and (5/8)/beta, and unchanged target component probabilities. It verifies each rational killed-generator row and every backward occupation equation. Stationary incoming flux gives the interval of possible conditional busy probabilities inside the finite set. An independently derived slow M/M/2 service dominator bounds the omitted infinite tail. The proof of this enclosure is archived with `whitt_positive_service_exact.py` and its independent checks. Truncation is therefore a rigorous enclosure, not an approximation without a remainder bound.

There is also a strictly positive waiting threshold. The base queue's completion intensity is at most10. Hence P(0<W_S<=h)<=10h. With h=1/100000,

    P(W_S>h)-P(W_U>h)
      >= P(W_S>0)-P(W_U>0)-10h
      >23/10000.

This is an explicit stochastic-comparison counterexample with a strictly larger mean service time, strict increasing-convex domination at every nonnegative stop-loss threshold, and a certified reversal at a positive waiting threshold. It does not refute the weaker conjecture concerning mean waiting times.

Primary assertion: W. Whitt, "Comparison conjectures about the M/G/s queue", Operations Research Letters2(1983),203-209, Conjecture1.1 and equation(2.6), https://www.columbia.edu/~ww2040/comparisonConjectures1983.pdf .

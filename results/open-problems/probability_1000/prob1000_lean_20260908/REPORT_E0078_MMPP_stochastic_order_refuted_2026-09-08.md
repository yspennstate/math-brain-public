# The time-stationary inter-event time of an MMPP need not dominate the event-stationary one

Refuted 2026-09-08. Ledger id E0078 (intake E, source `map_processes_open_2019`). Companion to the
proof of E0077 (Downloads/Probability_E0077_MMPP_scv_proved_2026-09-08.md), settled an hour
earlier.

## The conjecture

Asanjarani and Nazarathy, *Stationary Markovian arrival processes: results and open problems*,
arXiv:1905.01736, Conjecture 4.2: for an irreducible MMPP, T_1^pi >=_st T_1^alpha, where T_1^pi
is the time-stationary first inter-event time (the forward recurrence time) and T_1^alpha the
event-stationary one. In their notation (14) the claim is pi e^{Ct} 1 >= alpha e^{Ct} 1 for all
t >= 0, with alpha = pi D / (pi D 1). They proved it for MSPPs and for two-state MMPPs, tested
10^6 random instances of orders 3 to 6 plus 10^6 random order-4 cyclic generators, and found no
violation. The withdrawn arXiv:1802.08400 claimed it as Theorem 3.1.

## Result

The conjecture is false. Two statements, one proved and one numerically certified.

**Theorem (Cox class).** Let lambda be a bounded measurable T-periodic function on the line with
minimal period T, not almost everywhere constant, let theta be uniform on [0,T), and let N be the
Cox process with intensity lambda(theta + s). Then N is stationary with intensity
lambda* = (1/T) integral_0^T lambda, and the order T^pi >=_st T^alpha fails: on a set of t of
positive measure, P(T^pi > t) < P(T^alpha > t).

**Instance (MMPP).** Take the 24-state cycle with generator Q_{i,i+1} = 1 (indices mod 24),
Q_{ii} = -1, and arrival rates lambda_i = 2/3 for i = 0..11, 0 for i = 12..23. So lambda* = 1/3,
the mean lap is 24 and the mean exposure per lap is 8. At t = 19.75,

    P(T^pi > t) = 0.01425361547     P(T^alpha > t) = 0.01542552227

computed with a 30-digit matrix exponential. The order is violated by 8.2 percent of P(T^pi > t).
An independent exact certificate by a Codex agent (rational uniformisation of the matrix
exponential with 121 terms and a geometric remainder; audits/evidence/2026/09/08/overnight-mmpp-exact/)
brackets P(T^pi > 79/4) - P(T^alpha > 79/4) between -0.0011719068073579858342212642800 and
-0.0011719068073579858342212642799, so the violation is a proved inequality, not a floating-point one.
Larger cycles violate it harder: 64 states, block of 32 at rate 1/4, gives at t = 53.0
P(T^pi > t) = 0.005276 against P(T^alpha > t) = 0.007865, a 49 percent excess of the hazard of
T^pi over lambda*.

## Proof of the theorem

Write S(t) = P(T^pi > t) = P(N(0,t] = 0) = E[exp(-Lambda(0,t])] with
Lambda(0,t] = integral_0^t lambda(theta + s) ds. Three facts.

1. Palm inversion. For any stationary simple point process with finite positive intensity,
   P(T^pi > t) = lambda* integral_t^infinity P(T^alpha > s) ds (Daley and Vere-Jones vol. II,
   (3.4.17); the source's Lemma 2.1). S is Lipschitz here (lambda is bounded), so for almost
   every t, -S'(t) = lambda* P(T^alpha > t). Hence P(T^pi > t) >= P(T^alpha > t) at such a t is
   the same as S'(t) + lambda* S(t) >= 0, i.e. g'(t) >= 0 where g(t) = e^{lambda* t} S(t).
   The conjecture therefore says exactly that g is nondecreasing, equivalently that the hazard
   rate of T^pi never exceeds lambda*. (g(0) = 1 and g'(0) = 0: the hazard starts at lambda*.)

2. g(T) = 1. Over a full period the exposure is deterministic, Lambda(0,T] = integral_0^T lambda
   = lambda* T for every theta, so S(T) = e^{-lambda* T} exactly.

3. g(t) > 1 for 0 < t < T. Jensen gives S(t) >= e^{-lambda* t} (this is the E0077 inequality),
   with equality only if Lambda(0,t] is a.s. constant in theta. Its theta-derivative is
   lambda(theta + t) - lambda(theta), which vanishes for a.e. theta only if lambda is t-periodic,
   impossible for 0 < t < T when T is the minimal period. So the inequality is strict.

A Lipschitz g with g(0) = g(T) = 1 and g > 1 on (0,T) has g' < 0 on a set of positive measure in
(0,T); at those t, by fact 1, P(T^pi > t) < P(T^alpha > t). That is the theorem.

The mechanism in words: from a random instant the survivors to time t are the phases that
have not yet met the high-intensity part of the cycle; as t approaches one period the cycle
brings that part around to every survivor at once, and the hazard of the time-stationary
interval overshoots the average rate. The event-stationary interval, which starts inside the
high-intensity part, has already paid that cost.

## Why the MMPP instance is the same thing

A cycle of m states at rate r with a block of k = m/2 consecutive states at rate L is a
Markov approximation of the periodic intensity: the lap time is Gamma(m, r), with relative
spread 1/sqrt(m), and the exposure per lap is Gamma(k, r) times L. Holding m/r = T and kL/r = E
fixed as m grows, the exposure over any window converges in probability to the deterministic
periodic exposure, so S_m(t) and -S_m'(t) = pi_m e^{C_m t} lambda_m converge to the periodic
process's S(t) and -S'(t) by bounded convergence; the strict inequality of the theorem
therefore holds for all large m. In the family (block m/2, exposure 8 per lap, r = 1) the order
first fails at m = 20 (by 1.5 percent of P(T^pi > t) at the grid resolution used; m = 16 does not
fail); the 24-state instance quoted above was chosen for its cleaner numbers, not as the minimum.

Why the source's search missed it: their random instances had uniform(0,1) off-diagonal
generators (nothing close to a long deterministic cycle), and their cyclic experiment was
order 4. At m = 4 the lap has relative spread 1/2 and the mechanism has no room. It needs a
cycle long enough that the exposure per lap is nearly deterministic while the per-visit
exposure L/r stays below one: the Jensen slack at a full lap, roughly exp(E^2/2k), must fall
below the slack at a half lap, roughly cosh(E/2). The single-hot-state "lighthouse" cycle,
however long, does not work: its slack is dominated by the exponential holding time in the hot
state, and the order holds there at every m tested (4 to 64).

## Checks

* Three computations of the 64-state instance at t* = 53.004 agree to six digits: scipy expm,
  DOP853 integration of u' = Cu with rtol 1e-11, and mpmath at 30 digits
  ((pi - alpha) e^{Ct} 1 = -2.588268e-3, S = 5.276483e-3).
* Independent of the phase-type formula altogether: a simulation of the point process itself
  (12 million holding intervals, 1.50 million arrivals, 2 million uniformly sampled instants;
  e0078e.py). Empirical intensity 0.12473 against lambda* = 0.125; E[T^alpha] = 8.017 against 8;
  c^2 = 2.56 (E0077 holds on the same path). At t = 53: P(T^alpha > t) = 0.00794 +- 0.00007,
  P(T^pi > t) = 0.00538 +- 0.00005, matching the matrix values 0.007865 and 0.005276; the
  violation is 29 sigma there, 33 sigma at t = 40, 36 sigma at t = 50, 21 sigma at t = 56, and
  it reverses to +437 sigma at t = 20, as it must (the order holds for small t).
* Robustness to strictly positive rates and to a non-monotone cycle: the 24-state instance with rate
  0.01 on the twelve off-block states and a backward jump rate 0.01 added to every state (so every
  entry of the generator's off-diagonal cycle structure is perturbed and every lambda_i > 0) still
  violates the order, P(T^pi > 20) = 0.011808 < P(T^alpha > 20) = 0.012645, a 7.1 percent excess of the
  hazard of T^pi over lambda* (25-digit expm). The violation is an open condition in the parameters.
* The random search that preceded the construction (500 dense, cyclic, skewed and two-scale
  generators of orders 2 to 6 with rates spanning six decades, plus hill-climbing from the 6
  worst; e0078.py) found no violation, reproducing the source's experience: the failure is not
  generic, it is a designed regime.

## What survives

Conjecture 4.1 (c^2 >= 1) is unaffected; it was proved the same day, and the periodic Cox
process obeys it with room to spare. The source's Lemma 2.1 (c^2 >= 1 iff E[T^pi] >= E[T^alpha])
and Proposition 3.3 (the order holds for MSPPs) are untouched. What falls is the picture
in which (IV) is the natural route to (III): the mean of T^pi dominates the mean of T^alpha
for every MMPP, but the distributions are not ordered.

## Prior art

Not checked beyond the source, its withdrawn predecessor, and the same-day web search for
later work on these conjectures. The failure of the forward-recurrence-time order for
non-renewal stationary processes may well be classical in some form; what is new here, as far
as I know, is that it happens inside the MMPP class, against the explicit conjecture, with an
explicit 24-state instance.

## Files

prob1000_lean_20260908/e0078.py (random search), e0078b.py (lighthouse cycles, no violation),
e0078c.py (wide-block cycles, the violation), e0078d.py (three-way check and the m ladder),
e0078e.py (simulation of the point process), e0078f.py (30-digit numbers for m = 24).

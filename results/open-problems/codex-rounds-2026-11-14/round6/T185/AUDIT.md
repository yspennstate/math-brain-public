# Audit of the random-file extension

## Earlier result

The local copy of round 5's checker reproduces all 672 paths and the
constant -2171/20480. Independently, if any original local count is above
K, original service on that route is at least K Q/(K+L), but cannot exceed
its initial workload. This gives the barrier m(1+L/K), and beyond it both
original populations are small. The local reflection formula gives the
same error (Q-m)^+. The argument does not use count compactness in the
regeneration step. No error in the earlier result was found.

## A second derivation of the threshold estimate

The proof uses a barrier. Alternatively, for each route let tau_j be the
first time its original count is at most K, with tau_j=0 if this holds
initially, and tau_j=T if it does not occur before T. Let tau=max(tau_1,tau_2).
If tau>0, select a route attaining it. Its original count is above K at
almost every earlier time. Thus its original service by tau is at least
K Q(tau)/(K+L), and is at most its initial workload, at most m. Consequently
Q(tau)<=m(1+L/K). If tau=0 this is immediate.

If tau<T, both original counts are at most K after tau, while the new
counts sum to at most L. The through bound n_0>=R/b_0 gives
q<=c b_0(2K+L)/(a_0 R). Integrate over the remaining interval of length
at most T. If tau=T there is no remaining interval. Both cases yield
exactly (15) in PROOF.md. Original local sizes never enter, except through
their finite initial workload. Selecting tau or its route is pathwise;
no stopping-time or independence property is needed for that selection.

## A second way to choose a negative horizon

For each local route, let Z_k=U_j(k)-U_j(k-1) for integer k>=1. These are
iid nonnegative variables of finite mean rho_j. Fix h and write
Z_k=min(Z_k,h)+(Z_k-h)^+. With mu_h=E min(Z_k,h) and
a_h=E(Z_k-h)^+, the triangle inequality and independence give

    E |(Z_1+...+Z_n)/n-rho_j|
       <= sqrt(Var(min(Z_1,h))/n)+2*a_h.

Indeed, center the capped sum and apply Cauchy–Schwarz to get the first
term. For the remainder sum, subtract its mean n*a_h and bound the
expected absolute value by 2*n*a_h. Finite means give a_h->0. First send
n to infinity and then h to infinity. This proves L1 convergence of
U_j(n)/n to rho_j without a second moment or a fluid approximation.

Since

    |max(x1,x2)-max(y1,y2)| <= |x1-y1|+|x2-y2|,

the expectation of max(U_1(n),U_2(n))/n tends to max(rho_1,rho_2).
Thus d(n)/n tends to -delta<0, independently confirming the existence
of a negative fixed horizon. The proof's mark-level truncation gives a
more explicit estimate and permits arbitrary real T.

## Explicit constants, checked twice

For the first example, direct atom sums and survival integration both
give E B_i=1, E B_1^2=25/16 and E B_2^2=5/4. The compound-input
variance rates are respectively 25/32 and 5/8. The variance of the
difference over time 8 is 45/4, at most (7/2)^2. Therefore d(8)<=-13/20.
The threshold errors are 1/8 and 387/2048. At common denominator 10240,
the drift numerator is -6656+1280+1935=-3441. Also
65536+2*8=65552. These agree with the exact-rational script.

For the dyadic law, the atom probabilities sum to one by a geometric
series. The mean is (3/4)*sum_n 2^{-n}=3/2, whereas every atom contributes
3/4 to the second moment, which therefore diverges. For h=2^k, summing
the atoms with n<=k and the remaining capped tail gives

    E min(B,2^k)^2 = 3*(k+1)/4+1/4 = (3*k+4)/4.

Independently, survival integration gives an initial contribution one
on [0,1], and 3/4 on every interval [2^j,2^{j+1}] below h, hence
1+3*k/4. Likewise the excess-tail integral is

    sum_{j=k}^infinity 2^j * 4^{-(j+1)} = 2^{-(k+1)}.

At k=4 the capped second moment is 4 and the excess mean is 1/32.
With two arrival rates 1/3 this gives eta=1/48 and capped variance rates
4/3. At T=192 each deviation bound is sqrt(256)=16. The benchmark is
-288/5+32+4=-108/5. The first threshold error is
(2/3)*192^2/4096=6; the second is
(3/2)*192*(8192+128)/1048576=2925/1280. Thus the final numerator at
denominator 1280 is -27648+7680+2925=-17043. The workload threshold is
1048576+384=1048960. Both independent computations agree.

The original total load sum 6/5 is above one in the first example and
also in the dyadic example. Thus the first session's linear total-work
certificate does not already cover these examples.

## Regeneration checked without a compactness assumption

The sampled drift is conditional on the full residual state, not just
the workload vector. Finite-time workload is integrable because total
input work has a finite mean. Stopping the sampled nonnegative workload
at its first return to C gives the expected return bound (19).

In C, total work is at most 2B. Without arrivals, total service is at
least one until empty, uniformly over counts and residual sizes. Hence
an interval of length 2B succeeds with a fixed positive probability.
After a failed trial, the unconditional expected workload is at most
B+aD; its expected return cost, multiplied by the failure indicator, is
bounded by T(B+aD)/epsilon. This is sufficient to sum costs over the
geometric bound on the number of reached trials. A conditional expected
return cost given failure need not have that same bound and is not used.

The empty holding time is exponential with positive finite mean, and
the first arrival has finite expected work a/nu. Thus the return bound
gives finite mean regenerative cycles. In the invariant-law verification,
{t<Z} is measurable at time t, permitting the deterministic-time Markov
property inside the cycle integral. Regeneration makes the two boundary
integrals cancel. Every initial state reaches empty almost surely, and
the sum of the exponential idle portions diverges, giving Harris
recurrence with irreducibility measure delta_empty.

Arbitrary finite initial through residuals can be included by replacing
b_0 by their finite maximum with b_0 for that initial state and all its
future states. The constants may then depend on this maximum. This does
not change the invariant cycle law from empty, where through files always
have the original incoming bound. No uniform drift on the enlarged
uncapped initial state space is asserted.

## Attempts to break the hypotheses

- Very large local files: allowed. Their count still appears only in L
  or in the monotone original counts. Size enters the compound input
  benchmark and original work, where finite means suffice.
- Infinite local variance: explicitly covered by the dyadic example.
  Replacing a nonexistent second moment by the variance bound (12)
  would fail; the proof instead uses (10).
- Count/work confusion: L is the number of local arrivals, with mean
  (nu_1+nu_2)*T, not their total work. In the dyadic example its rate is
  2/3 while local work input has rate one. Both are used in their proper
  places in the explicit constants.
- Infinitely many initial files: not admitted. Arbitrarily large finite
  populations are allowed; the state and nonexplosion argument require
  finiteness at each time.
- Tiny residuals and simultaneous departures: allowed. Original counts
  decrease, and all equations are integrated or almost-everywhere
  statements. The clock checker includes simultaneous arrivals and
  departures without a residual-time discretization.
- Q greater than the original local maximum: allowed and observed in
  520 marked paths. Dropping the positive error in (8) is invalid.
- Empty through route or empty network: q=1 is potential local service,
  and its unused part is retained by the reflection regulator. The
  large-through estimate is used only when w_0>T.
- Unequal local loads: handled by max(rho_1,rho_2), including the limit
  argument and the finite-second-moment estimate. Equality of local
  rates or file laws is used only in the explicit examples.
- Extreme fixed weights and alpha below one: the bound on H follows
  directly from u_j<=u_1+u_2 for every alpha>0. Uniformity as alpha tends
  to zero or weights degenerate is not claimed. Trajectory checks cover
  alpha=1 only; all-alpha validity is established symbolically.
- Unbounded arriving through sizes: not covered. A single through file
  can have arbitrarily large work while n_0=1, violating the needed
  cap-based lower bound (13). Truncating arrivals does not by itself
  compare the two networks or preserve their recurrence properties.
- Arbitrary topologies or unequal link capacities: the common local
  potential rate q is special to this two-link equal-capacity topology.
  Neither extension has been proved here.
- Renewal input: future residual interarrival times would be part of
  the Markov state. The fresh uniform no-arrival trial used here cannot
  be assumed from arbitrary such states.
- Stationary mean workload: finite mean regenerative cycles prove an
  invariant probability, not its first workload moment.

No mathematical check failed. The finite exact trajectories supplement
the proof; they neither establish general-alpha behavior by computation
nor simulate the claimed invariant law. No novelty claim is made.

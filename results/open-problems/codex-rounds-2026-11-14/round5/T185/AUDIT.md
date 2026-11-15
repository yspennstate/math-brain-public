# Audit

## Round 4

The copied prior script reproduces the main constants and all 504 paths.
The independent symbolic check in LOG.md recovers the original-service
charging inequality and its Poisson area factor 1/2. The conditional
random-walk and double-Poisson sums separately enclose d(4) between
-0.428494478548 and -0.428494478547. The new proof needs only the weaker
variance bound d(4)<=-1/5. The previous result holds.

## A second proof of the count-threshold estimate

Keep the notation of PROOF.md. Put h=m*(1+L/K). Suppose at a time t
there are more than K original files on route j. There were more than K
on that route at every earlier time, since original counts only decrease.
Their share of the route's aggregate service was at least K/(K+L).
Thus their cumulative service by time t is at least K*Q(t)/(K+L), but is
at most w_j<=m. Necessarily Q(t)<=h.

Consequently whenever Q(t)>h, both original local counts are at most K.
At those times q(t)<=beta:=c*(2K+L)/(a0*R). Since Q is continuous and
nondecreasing, either Q(T)<=h or its excess above h is the integral of q
after its first crossing of h, and is at most beta*T. Therefore

    Q(T)<=m*(1+L/K)+c*T*(2K+L)/(a0*R).

This proves the same bound without choosing the last surviving high-count
route. It also covers equality at the threshold, jumps of original counts,
no original locals, and a route that remains above K for the full horizon.

## Reflection and a second view of the large-local region

The regulator proof handles an empty through route and even an empty
network by defining q=1-Lambda0. Its unused portion is essential; dropping
it would make the workload balance wrong after a local queue empties.

For an alternative verification when m>=T, choose a route j with w_j=m.
Its work remains positive up to T, apart from possibly the endpoint, since
its service is at most one. It receives total service Q(T), so its final
work is m+A_j(T)-Q(T). On the other local route k, reflection gives
Q(T)+W_k(T)<=A_k(T)+max(w_k,Q(T))<=A_k(T)+m, since Q(T)<=T<=m.
The same bound is an equality on route j after replacing A_k by A_j.
Combining with the through balance gives the large-local drift directly.

## Constants and expectation

The two link loads are 1/5+1/2=7/10; the total arrival rate is 6/5.
Independence gives Var(A1(4)-A2(4))=2+2=4. Equivalently, condition on
the local total, of mean four, and use variance one for each symmetric
random-walk step. Both give E|A1-A2|<=2 and d(4)<=-6/5+1=-1/5.

The threshold error has two sources: m*E L/K<=16/256=1/16,
and 4*(512+E L)/65536=2064/65536=129/4096. Their sum is
385/4096. At common denominator 20480 the drift numerator is
-4096+1925=-2171. Separately, the four-term expansion gives
-4096+1280+640+5=-2171. Both agree with the script.

If M>65544 and m<4, W0-4=M-m-4>65536. If m>=4, no through-work
bound is needed. These cases cover all states above the threshold.
No claim of a sharp threshold or drift constant is made.

## Attempts to invalidate the hypotheses

- Arbitrarily many initial local files with arbitrarily small residuals:
  allowed. Original counts are monotone, and charging uses only their
  remaining initial work. Counts may exceed 10^7 in the compressed checks.
- Original through departures: allowed. The bound is n0>=W0>=W0(0)-T,
  rather than preservation of the original through population.
- Large new local counts: allowed. The pathwise bound uses the actual
  terminal count L, without any deterministic upper bound or conditioning.
- Empty periods: allowed in reflection, but impossible in the portion
  using W0(0)>T. The script includes paths with positive empty time.
- Q(T)>m: allowed and observed. Omitting this error would be false.
- Unequal weights or alpha below one: monotonicity and degree-one
  homogeneity of H still hold. The bound c=(kappa1+kappa2)^(1/alpha)
  is finite for every fixed alpha>0. Uniformity as alpha approaches zero
  or weights degenerate is not asserted.
- Unbounded initial counts in a bounded M-set: the set is not treated as
  compact. The no-arrival argument uses total work, which is at most 2M,
  and aggregate service at least one. It therefore remains uniform in count.
- Positive recurrence versus finite mean workload: finite mean cycles and
  Harris recurrence are proved. No stationary first-workload-moment bound
  is asserted from the drift estimate alone.
- General arriving sizes: not covered. The identities use unit workload
  jumps, and the count lower bound uses residuals at most one.
- General networks: not covered. Two independent local resources have
  exactly the same potential aggregate service q, which drives reflection.
- Renewal input: not covered. Fresh Poisson increments provide both the
  Markov property of this residual-only state and the uniform emptying trial.

## Recurrence audit

The sampled hitting-time proof uses conditional drift only before the
bounded-workload set is hit. Its stopped workload is nonnegative, and all
finite-time workloads are integrable by the total-arrival bound.

At a trial start in the set, E M(D)<=B+nu*D. The unconditional expected
return cost after a failed trial is bounded by T*(B+nu*D)/epsilon; it is
not necessary to bound the conditional mean given failure by the same
quantity. Summing unconditional costs over the geometrically bounded
number of reached trials gives a finite mean success time. The success
probability is positive symbolically, even though a floating-point
evaluation would underflow at the deliberately large explicit threshold.

Finally, empty is an accessible atom with positive exponential holding
times. Finite mean cycles yield the invariant cycle occupation law, and
infinite cumulative empty holding time proves Harris recurrence with
irreducibility measure delta_empty. This avoids importing an unavailable
general fluid-to-stochastic theorem.

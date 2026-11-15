# Checks and limits

## Independent derivation of the emptying-time bound

Set `Y=sum_i W_i/b_i` and couple it to a unit-speed scalar workload queue `Q` with the same compound Poisson jumps `B_i/b_i`, starting at the same workload `y`. Between jumps, whenever `Y>0`, its derivative is at most `-1`. The scalar workload decreases at rate exactly `1` whenever positive. At jumps both workloads increase by the same amount. Induction over the finitely many arrivals in each bounded interval gives `Y(t)<=Q(t)` for all times. In particular, `Y` empties no later than the end of the first scalar busy period.

Compute the mean scalar busy period without a martingale stopping argument. Serve its jobs in first-come-first-served order, treating the initial workload `y` as the ancestor's service time. During a total amount `s` of service time, arrivals contribute mean total new service `beta s`. Independence of future Poisson increments and file-size marks gives expected service times `y, y beta, y beta^2,...` for successive genealogical generations. The nonnegative sum has expectation `y/(1-beta)` by Tonelli's theorem. It is finite when `beta<1`, so the complete busy period is finite almost surely and has that mean. This reproduces (3). A first arrival has mean normalized size `beta/nu`, giving the same cycle bound `1/[nu(1-beta)]` by a second route.

## Independent service-bound check

Suppose `sum_i Lambda_i/b_i<1`. On every link `j`,

`sum_i A_ji Lambda_i/C_j <= sum_i Lambda_i/b_i < 1`.

Thus every link is slack and a present route can be increased, contradicting Pareto efficiency. This gives the unit lower service bound by comparing all link utilizations, independently of selecting a particular saturated link. Multiplying by `q=min_i w_i b_i` and using `w_i>=q/b_i` gives the general bound. A route alone gives equality.

## Numerical and algebraic cross-checks

- The example's link loads are `A rho=(7/10,7/10)`. Directly adding the through load `1/5` to each local load `1/2` gives the same values.
- For unit mean files and arrival rates equal to `rho`, the normalized input rate is both `sum rho_i=6/5` and `nu` times the mixture mean jump `1`. The overload is an overload of the scalar comparison, not an overload of either physical link.
- The symbolic obstruction is `a-q >= (6/5)q-q=q/5`. Exact arithmetic verifies it for all 512 positive integer coefficient vectors in `{1,...,8}^3`. The proof covers all positive real coefficients.
- Exact vertex enumeration across all nonempty supports gives minima `2` and `4/3` in the two selected networks, matching the formula independently. Enumeration includes boundary allocations as a check of the Pareto geometry; it does not claim every enumerated vertex is an alpha-fair allocation at positive integer counts.

## Attempts to break the argument

1. **Bounded file sizes.** Sending one residual size to infinity would leave a bounded-support state space. The necessity proof instead increases the number of files, each with a fixed admissible positive residual. It applies even to deterministic file sizes.
2. **A very large residual with few flows.** The sufficient bound does not depend on flow counts or a size moment beyond the first. The initial workload may be arbitrarily large but finite.
3. **Many very small residuals.** Departures do not jump the workload and there are finitely many initial files and finitely many arrivals on bounded intervals. No minimum file size is used.
4. **Atoms or infinite variance.** The workload compensation and regeneration arguments need only a finite first moment. They apply to atomic, deterministic, and finite-mean heavy-tailed distributions. The stationary mean workload need not be finite, and the proof never assumes that it is.
5. **The empty-state drift.** The service lower bound is used only before the first emptying time. At empty, the generator of the workload is positive; this is why the proof stops at empty and then regenerates.
6. **Critical scalar load `beta=1`.** The argument provides no finite expected emptying time. The linear-certificate necessity still excludes a strictly negative uniform margin. No recurrence classification at this boundary is claimed.
7. **Renewal arrivals.** Emptying is not regeneration of the residual-state process without interarrival clocks. The theorem is expressly restricted to independent Poisson arrivals.
8. **General topology.** A saturated link need not carry all active routes. The service bound sums only over that link and drops other nonnegative terms; it does not assume a common bottleneck.
9. **Nonlinear or sampled drift.** Positive drift for all linear workload candidates in the example does not exclude nonlinear Lyapunov functions or negative drift after a longer time. It is not a stochastic instability example.
10. **Literature scope.** The 2022 authors' recurrence statement is conditional, and the 2026 paper uses phase-type files. Neither is evidence of unrestricted positive recurrence for arbitrary finite-mean files. No claim of novelty for this elementary certificate is made.

The main unresolved issue remains how to use the full linkwise spare capacity with general residual profiles, beyond the scalar comparison region.

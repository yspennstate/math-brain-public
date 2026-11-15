VERDICT: PARTIAL positive Harris recurrence for the two-link unit-file example under every weighted alpha-fair policy

Round 4's sampled-drift result holds. Its script was copied into this
folder and rerun: all 504 exact paths and both Poisson-series calculations
passed. A separate symbolic rederivation recovered its original-service
charging bound and finite-state constant -201/1900. Earlier folders were
not edited.

New beyond round 4: the same maximum link workload now has uniformly
negative four-unit drift at **all** sufficiently large workload states in
its two-link network, with deterministic unit arrivals, independent
Poisson rates (1/5,1/2,1/2), arbitrary fixed alpha>0 and positive weights.
There are no bounds on initial finite counts or positive lower bounds
on residuals; initial residuals are at most one. This closes the gap its
report identified. Positive Harris recurrence follows for this specified
example by an explicit empty-state regeneration argument. T185 for general
file-size distributions and networks remains unresolved here.

The new estimate uses the common potential local service q=1-Lambda0,
its integral Q, and m=max(W1(0),W2(0)). Local reflection gives

    Delta M <= A0(T)-T+max(A1(T),A2(T))+(Q(T)-m)^+.

If m>=T the error is zero, including when only one local workload is
large or the through route is empty. If m<T and W0(0)>T, put
R=W0(0)-T and choose an integer K>=1. The last original local population
to fall below K charges the earlier potential local service to at most
m units of original work. Afterward both original local counts are small.
This proves

    E Delta M <= d(T)+T^2/K+c*T*(2K+T)/(a0*R),

where d(T)<=-3T/10+sqrt(T)/2, a0=kappa0^(1/alpha), and
H(u1,u2)<=c*(u1+u2). First taking K large and then R large gives uniform
negative drift in the remaining region. For equal weights and alpha=1,

    M(x)>65544  =>  E_x[M(X(4))-M(x)] <= -2171/20480.

The bounded-workload set need not be compact: a no-arrival interval of
length 2B empties every state with M<=B because its total work is at most
2B and aggregate service is at least one while nonempty. Sampled drift
bounds the expected return time to this set after each failed attempt.
Uniform positive success probability yields finite mean emptying time,
finite mean regenerative cycles and positive Harris recurrence.
PROOF.md writes out every step; AUDIT.md gives a second proof of the
count-threshold estimate and checks the recurrence argument.

Commands, run here:

```sh
nice -n 15 env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 prior_check_sampled_drift.py
nice -n 15 env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 check_uniform_drift.py
```

Both print `all exact checks passed`. The new script uses exact rational
event-driven trajectories: 672 paths, 3,733 events, 1,920 threshold checks,
434 original-cohort departures, 230 paths with Q>m and 72 with positive
empty time. It includes mixed routes, simultaneous arrivals, new counts
above K, no through population, tiny residuals, large original counts and
unequal weights. Computational checks use alpha=1; the proof covers all
alpha>0. Full outputs: sampled_drift_checks.json and uniform_drift_checks.json.
The new run took 0.2447 seconds, peak RSS 16,465,920 bytes, actual nice 20,
one thread, CPU cap 60 seconds. The wrapper's priority warning reflects
its inability to change the already lower inherited priority.

The literature update found no later unrestricted stochastic theorem.
Opened Yingjia Fu and Ruth J. Williams, *Asymptotic behavior of a critical
fluid model for bandwidth sharing with general file size distributions*,
Ann. Appl. Probab. 32 (2022), 1862–1901:
https://mathweb.ucsd.edu/~williams/bandwidth/AAP1723forposting.pdf .
The attempted 2020 author-PDF fetch timed out. The limited search neither
certifies openness nor establishes novelty of this special-case proof.

What failed: no mathematical check failed. The tempting deterministic
bound Q<=m is false in the presence of new local arrivals; the proof
retains its explicit positive error. General arriving files, arbitrary
topologies, renewal input and an unrestricted fluid-to-stochastic bridge
are not proved. No stationary mean-workload estimate is asserted.

Next worker: extend this same two-link proof to bounded random file sizes.
Replace arrival counts in the workload/reflection identities by compound
Poisson input work, retain new-file counts in the threshold lemma, and
use a common file-size bound to recover n0>=W0/b_max. Verify this carefully
before attempting truncation to unbounded sizes: large through work then
need not imply a large through count, which is the unresolved obstruction
for this argument. No claim that such a truncation preserves stability
has been made.

All writes stayed in this folder; no git, subagents, external publication
or shared-state logging was used.

Task: “take the NEXT checkable step on this problem, building on that work.”
First local clock: 15 November 2026, 08:32:25 Asia/Tbilisi;
exact receipt time unavailable.

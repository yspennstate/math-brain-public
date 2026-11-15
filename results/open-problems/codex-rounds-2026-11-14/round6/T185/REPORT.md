VERDICT: PARTIAL positive Harris recurrence for subcritical two-link networks with bounded through files and arbitrary finite-mean local files

Round 5's main result holds. Its checker was copied here and rerun: all
672 exact paths and 1,920 threshold checks passed. A separate barrier
argument recovered its count-threshold estimate and drift constant
-2171/20480. Earlier folders were not edited.

New beyond round 5: consider the same two unit-capacity links, one route
using both links and one local route per link. Under independent marked
Poisson input, every fixed weighted alpha-fair policy with alpha>0 is
positive Harris recurrent whenever

    rho0 + max(rho1,rho2) < 1,

provided the arriving through files have bounded size and both local
file-size distributions have finite means. Local sizes may be unbounded,
atomic, and have infinite variance. All finite initial residual states
are allowed. This includes the bounded-random-size extension requested
by round 5 and removes its restriction to one particular arrival-rate
vector. T185 for general networks and unbounded through-file distributions
remains unresolved here. No novelty claim is made.

PROOF.md gives all steps. Write M=W0+max(W1,W2), let U_i be compound
Poisson input work, and put

    d(T) = (rho0-1)*T + E max(U1(T),U2(T)).

Finite local means imply d(T)/T tends to
rho0+max(rho1,rho2)-1<0. The proof establishes the required upper bound
directly by capping input marks, bounding capped fluctuations by standard
deviations, and retaining the excess work. This truncation estimates
input only and does not compare queueing systems.

For through size bound b0, lambda=nu1+nu2, m=max(W1(0),W2(0)),
R=W0(0)-T>0, a0=kappa0^(1/alpha), and H(u)<=c*(u1+u2), the threshold
lemma becomes

    E Delta M <= d(T) + m*lambda*T/K
                        + c*b0*T*(2K+lambda*T)/(a0*R).

The first error uses arriving file counts; the benchmark uses arriving
work. No local size bound enters the threshold argument. If m>=T,
reflection removes both errors. Choose a negative horizon, then K large,
then R large. This proves uniform negative sampled drift outside a
bounded M-set on each fixed through-residual cap. A no-arrival interval
empties this set uniformly in its unbounded counts. Repeated trials give
finite mean emptying times and regenerative cycles, proving positive
Harris recurrence. Arbitrary finite initial through residuals are covered
by using their finite maximum as a state-dependent cap; arriving through
sizes remain uniformly bounded.

Two explicit examples, for equal weights and alpha=1:

- Nonconstant bounded sizes at the original rates (1/5,1/2,1/2):
  B0,B2 uniform on {1/2,3/2}, B1 uniform on {1/4,7/4}. Then
  M>65552 implies expected eight-unit drift at most -3441/10240.
- B0 as above, nu0=1/5, nu1=nu2=1/3, and
  P(Bj=2^n)=3/4^(n+1) for each local route. The local mean is 3/2 and
  the second moment is infinite. Then M>1048960 implies expected
  192-unit drift at most -17043/1280.

These explicit uniform drift thresholds assume initial through residuals
at most 3/2; their local residuals may be arbitrary finite values. Both
examples have link loads 7/10 and total route load 6/5, outside the first
session's linear-workload sufficient region.

Commands, run in this folder:

```sh
nice -n 15 env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 prior_check_uniform_drift.py
nice -n 15 env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 check_marked_drift.py
```

Both print `all exact checks passed`. The new checker uses per-route
service clocks, independently of the earlier residual-update simulator.
It checks 1,176 marked paths, 7,583 events, 3,780 threshold bounds and
9,667 high-count barriers, including large local marks, tiny residuals,
mixed cohorts, simultaneous arrivals and empty periods. It also checks
all displayed moments and constants by atom sums and survival integrals.
Trajectory checks cover alpha=1; the all-alpha result is symbolic.
Full output: marked_drift_checks.json and uniform_drift_checks.json.
The new run took 0.6716 seconds, used 16,171,008 bytes peak RSS, inherited
nice 20, one thread, and a 60-second CPU cap. The nice wrapper's warning
reflects the prohibited attempt to change that already lower priority.
AUDIT.md gives independent derivations and adversarial checks.

The short web update found no later unrestricted stochastic theorem.
Opened Yingjia Fu and Ruth J. Williams, *Asymptotic behavior of a critical
fluid model for bandwidth sharing with general file size distributions*,
Ann. Appl. Probab. 32 (2022), 1862–1901:
https://mathweb.ucsd.edu/~williams/bandwidth/AAP1723forposting.pdf .
Its discussion of stochastic recurrence retains distributional assumptions.
Also opened Mung Chiang, Devavrat Shah, and Ao Tang, *Stochastic Stability
Under Fair Bandwidth Allocation: General File Size Distribution*, Allerton
(2006): https://people.ece.cornell.edu/atang/pub/06/allerton06stability.pdf .
Its introduction specifies rate/fluid stability, with additional bounded
support and load/alpha restrictions. The 2020 author-PDF request timed out.
This limited search certifies neither openness nor novelty.

What failed or remains uncertain: no mathematical check failed. One
text-only patch failed to match its context and was corrected. An
unbounded-through extension was not obtained: large through work can
belong to a single file, invalidating n0>=W0/b0. The proof does not imply
that truncating those files preserves stability. Arbitrary topologies,
renewal input and stationary workload moments are not proved.

Next worker: address unbounded through sizes in this same topology before
changing networks. A concrete starting point is the residual through-tail
work V_h=sum_over_through_files (residual-h)^+, for which
W0<=h*n0+V_h. The existing threshold argument controls states where this
tail stays a small fraction of W0 over the sampling interval. The missing
piece is a drift estimate when a few very large through residuals dominate
the work. Bounds uniform in a truncation level are needed; recurrence of
each capped model alone does not supply them.

All new writes stayed in this folder; no git, subagents, external
publication or shared-state logging was used.

Task: “take the NEXT checkable step on this problem, building on that work.”
First recorded clock: 15 November 2026, 11:11:22 Asia/Tbilisi;
exact receipt time unavailable.

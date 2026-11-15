VERDICT: PARTIAL uniform negative sampled drift near the through-workload axis

The earlier smooth homogeneous workload obstruction holds. It was rederived
independently by averaging the two limiting service vectors and pairing with
the boundary gradient. No error was found. T185 remains unresolved.

New beyond round 3: the fixed-horizon lemma it requested is proved for its
two hostile state sequences, their accessible perturbations, and a wider
class of initial states. Keep the two-link network, deterministic unit
files, Poisson rates (1/5,1/2,1/2), any fixed alpha>0 and positive weights.
For the maximum link workload

\[
 M=W_0+\max(W_1,W_2),
\]

the expected increment over any fixed horizon T converges uniformly to

\[
 d(T)=-\frac3{10}T+\frac12\mathbb E|P_1(T)-P_2(T)|
 \le-\frac3{10}T+\frac12\sqrt T,
\]

over all finite initial states with residuals at most one,
W_0>=N-1 and W_1+W_2<=1/N, as N tends to infinity. P_1 and P_2 are
independent rate-1/2 Poisson processes. Thus every fixed T>25/9 gives
uniformly negative drift for sufficiently large N. There is no restriction
on the finite initial counts or individual local residuals in this wider
class. The convergence is not claimed uniformly over weights or alpha.

PROOF.md gives explicit finite-state bounds. In particular, with equal
weights and alpha=1, every N>=100 in this class satisfies

\[
 \mathbb E_x[M(X(4))-M(x)]\le-201/1900<0.
\]

The proof retains actual unit arrivals. It first bounds the clearing time
of the old tiny local files. An independent service accounting argument
then removes the old count and individual-residual restrictions: loss of
through service is charged to original local work or to new local counts.
The latter have expected integrated count T^2/2. Combined with exact
workload balance, this gives, when W_0(x)>T,

\[
 d(T)-\max(W_1(x),W_2(x))
 \le \mathbb E_x\Delta M
 \le d(T)+W_1(x)+W_2(x)
       +\frac{cT^2}{2a_0(W_0(x)-T)}.
\]

Here a_0=kappa_0^(1/alpha), and one may take
c=(kappa_1+kappa_2)^(1/alpha); for equal weights and alpha=1 take c=1.
All steps, including the all-alpha allocation formula and both service
bounds, are written in PROOF.md. AUDIT.md checks the constants and scope.

Reproduce the exact checks:

```sh
nice -n 15 env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 check_sampled_drift.py
```

Output: `all exact checks passed`. Full data: sampled_drift_checks.json.
Two independent rational-series calculations enclose d(4) in
[-0.428494478548, -0.428494478547]. They use a conditional symmetric random
walk and a separate double Poisson sum, with certified series tails and
exponential bounds. There are 27 earlier-gradient checks and 504 exact
cohort paths with 3,554 events. The path checks cover early arrivals,
unequal weights, mixed local routes, unequal residuals, original through
departures, and the charging inequality. They test alpha=1; the proof
covers every alpha>0. Final run: 0.222 seconds, 15,876,096 bytes peak RSS,
actual nice 20, one thread, CPU limit 60 seconds. The nice wrapper warns
because changing inherited priority is prohibited; its measured priority
is already below the requested level.

The brief literature update found no later unrestricted stochastic theorem.
Opened sources were Yingjia Fu and Ruth J. Williams's
[2022 critical-fluid paper](https://mathweb.ucsd.edu/~williams/bandwidth/AAP1723forposting.pdf)
and Maria Vlasiou, Jiheng Zhang and Bert Zwart's
[arXiv:1411.4841](https://arxiv.org/abs/1411.4841).
The first discusses a distributionally conditional recurrence bridge;
the second concerns heavy traffic. This search does not certify openness
or establish priority for the lemma proved here.

What failed or remains uncertain: no mathematical verification failed.
Positive pointwise drift persists even for M at the old exact states:
GM=1/5-1/(2N). The sampled estimate does not control states with large
initial local workloads, general arriving file sizes, or renewal input.
It proves no positive recurrence statement outside the first session's
region. No claim of novelty is made. All writes stayed in this folder;
no git, subagents or external publication was used.

Next worker: extend the sampled-drift bound to all sufficiently large
maximum link workloads in this same deterministic-unit-file network.
The remaining region has substantial local work. Start with the case
where both local workloads exceed the sampling horizon and therefore
both local routes stay occupied, then handle the case of one large local
workload. A uniform estimate on all large states is still needed before
using a recurrence criterion. The full general-file fluid-to-stochastic
bridge remains a separate gap.

Task: “take the NEXT checkable step on this problem, building on that work.”
First local clock reading: 15 November 2026, 05:01:45 Asia/Tbilisi;
exact receipt time unavailable.

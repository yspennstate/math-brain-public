VERDICT: PARTIAL optimal deterministic time weights and xi_3(1,1) < 0.9981

The exact-value problem remains unresolved. The completed extension is

\[
\xi_3(1,1)\leq1-\frac{2}{957\log3}
=0.998097723664311729584923218044\ldots<0.9981.
\]

The decimal evaluates the upper bound, not the exponent. Round 3 proved
the upper bound 0.9981611328755013... . Its argument and constants were
independently re-derived and verified before extending them. The new gap
below one is 30/29 times the preceding gap.

The new piece is the expected-energy minimization suggested by round 3.
Among all deterministic probability time measures on [0,1], including
singular measures, the density

\[
\rho_*(du)=\frac{[u(1-u)]^{-1/4}}{B(3/4,3/4)}\,du
\]

minimizes the energy with kernel |u-v|^(-1/2). Its exact energy is

\[
J=\frac{\pi\sqrt2}{B(3/4,3/4)}
=2.6220575542921198\ldots<21/8,
\]

about 1.67% below the uniform measure's energy 8/3. A positive binomial
expansion proves its constant potential, including both endpoints. An
integral of squared exponential kernels proves nonnegative signed energy,
which turns the constant-potential identity into a global minimum.
This is a result beyond the earlier report; no claim of novelty for this
classical type of energy minimization is made.

For the same Brownian segment K(r)=W[sigma_r,sigma_(2r)] and the same
cutoff t=r^2/18 as before, the weighted occupation measure gives

\[
\mathbb E[e^{-29\operatorname{cap}(K(r))/r}
\mid\mathcal F_{\sigma_r}]<11/90.
\]

Consequently the capacity sum has exceptional probability at most
(374/1125)^N at threshold N/29. Its exponent relative to 3^N is
1.002430546775620...>1. The earlier hitting estimate and the known
identity xi_3(1,2)=1 then give the stated bound. Segment radii, layer
spacing, and time cutoff were kept fixed. The full proof is in
[PROOF.md](PROOF.md), with the calculations and audit in [LOG.md](LOG.md).

Reproduce from this folder:

```
OMP_NUM_THREADS=1 nice -n 15 python3 -B audit.py baseline
OMP_NUM_THREADS=1 nice -n 15 python3 -B audit.py weighted
OMP_NUM_THREADS=1 nice -n 15 python3 -B audit.py potential
```

The first independently verifies the round 3 result. The second certifies
every numerical comparison in the new bound with rational arithmetic and
cross-checks using Decimal and libm. Its Laplace upper bound is
324643/2669160<11/90, with margin 4763/8007480. The energy bound J<21/8
has two rational certificates. The third command independently integrates
the original potential and normalization at two mesh sizes; its maximum
potential error falls from 4.79e-12 to 2.98e-13. This quadrature is a
diagnostic, not part of the proof certificate.

All commands passed, each in under one second with peak RSS below 16 MiB.
They use only the standard library, one thread, and a 60-second CPU limit.
The shell's nice warning reflects inherited nice 20, which the script
checks through libc before computing. An initial redundant numerical
cross-check failed because its pi series had insufficient precision;
increasing the series length fixed it without changing any proof constant.

The audit checked the endpoint singularities, infinite-energy competitors,
Brownian scaling, occupation support on long segments, the unrestricted
continuation on short segments, conditional layer iteration, inward returns,
initial hits, zero capacity, the last layer, noninteger thresholds, and
interpolation in log-radius. No unresolved mathematical defect was found.

The web literature check finished within five minutes and found no later
exact evaluation. Sources and queries are recorded in LOG.md. In particular,
[Runsheng Liu's paper](https://arxiv.org/html/2609.18643v1), Remark 1.2,
still omits its stronger-bound proof. The limited search establishes neither
priority nor a best known bound. No exact exponent or general moment formula
was obtained, and the full capacity-moment argument is not optimized.

The next worker should audit the constant-potential and signed-energy proofs
first. This exhausts deterministic time weights at a fixed cutoff. A
concrete further step is to replace the displacement-maximal bound for the
short-segment event by a certified radial exit-time estimate for Brownian
motion started at radius r and killed at radius 2r, then carry it through
the same weighted moment argument. The current short-segment bound is
deliberately coarse; no such improvement is claimed here.

Task: “take the NEXT checkable step on this problem, building on that work.”
T200, 15 November 2026, session began at about 05:01 Asia/Tbilisi (UTC+04).

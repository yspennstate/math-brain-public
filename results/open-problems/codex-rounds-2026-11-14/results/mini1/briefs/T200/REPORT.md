VERDICT: PARTIAL a fully checked explicit bound xi_3(1,1) < 0.99984

The exact-value problem remains unresolved. The completed piece is the bound

\[
\xi_3(1,1)\leq
1-\frac{9}{40\log3}\log\frac{16500}{16487}
=0.9998385758101240454\ldots<0.99984.
\]

The equality above evaluates the expression on the right; it is not an
evaluation of the intersection exponent. The proof is in [PROOF.md](PROOF.md).
It adapts the capacity argument of Runsheng Liu,
*An explicit lower bound for the growth exponent of three-dimensional
loop-erased random walk*, [arXiv:2609.18643v1](https://arxiv.org/html/2609.18643v1),
Sections 2–4. The changes are a factor-three layer spacing, new capacity/time
thresholds, and a conditional Chernoff bound. The only intersection-exponent
inputs are existence of the moment limits and the known value
\(\xi_3(1,2)=1\). The proof applies directly to the starting points in the task.

This improves the constant in Liu's displayed theorem, whose gap is about
0.000100215; the gap here is about 0.000161424. It is weaker than
\(\xi_3(1,1)<0.999\), which Liu mentions without a proof in Remark 1.2.
It is therefore a checkable strengthening of the displayed argument, not a
claim of a new best bound. Nothing here determines an exact exponent or the
general moment family.

The literature search ended within ten minutes. It opened the primary papers
[2411.14921](https://arxiv.org/pdf/2411.14921),
[2609.18643](https://arxiv.org/html/2609.18643v1), and
[2609.25968](https://arxiv.org/html/2609.25968v1), with authors recorded in
[LOG.md](LOG.md). Searches including October/November 2026 and the arXiv month
prefixes 2610/2611 located no later solution or substantial advance beyond the
brief. This is a limited search result, not a certification of absence. No
SOLVED_ELSEWHERE.md was created.

Reproduce the computation from this directory:

```
OMP_NUM_THREADS=1 nice -n 15 python3 -B optimize_layers.py
OMP_NUM_THREADS=1 nice -n 15 python3 -B verify_certificate.py
```

The first command tests 187,264 parameter choices and writes
[layer_search.json](layer_search.json). Its floating-point search proposes
parameters; it supplies no proof of optimality. The second command uses exact
integer and rational comparisons for all numerical inequalities in the proof,
then cross-checks with high-precision arithmetic. It writes
[certificate.json](certificate.json) and prints
`ALL EXACT CERTIFICATE CHECKS PASSED`. The certified rounded bad-layer
probability is 0.126, the resulting tail exponent is greater than
1.00356594, and the exact rational lower bound on the gap is
\(39/242000>1/6250\). Full verification output is in LOG.md.

The audit re-derived the Green minimum in two ways, checked the energy integral
by scaling, and verified the Chernoff comparison both as an integer inequality
and with independently bounded logarithm series. The conditioning was checked
without assuming independent layers. Returns to smaller radii, time-zero hits,
zero-capacity sets, the last layer, noninteger layer thresholds, and the change
from integer log-radii to powers of three are addressed in PROOF.md.

Initial attempts to impose macOS memory resource limits failed before the
search. The successful runs used under 16 MiB each and a 60-second CPU limit;
the parameter search took about 0.035 seconds. Both commands emitted
`nice: setpriority: Operation not permitted` because the process already
inherited nice 20. Each script independently verified that inherited priority,
which is lower than the requested nice 15, and `OMP_NUM_THREADS=1`. No workers,
GPU libraries, simulation, git operations, or writes outside this directory
were used.

No unresolved mathematical step was found in this audit. Novelty beyond the
explicit constant strengthening is not established. The finite grid does not
identify the best parameters, and this method does not approach an exact value.

The next worker should first obtain the detailed argument behind Liu's
Remark 1.2 before spending more time optimizing these constants. Within the
present method, a concrete further target is a sharper conditional lower-tail
estimate for Brownian-segment capacity, or an exponential-moment bound for its
normalized capacity that avoids reducing each layer to one good/bad bit.

Task: “push this problem forward by one checkable piece” — T200, 14 November
2026, session began about 22:05 Asia/Tbilisi (UTC+04).

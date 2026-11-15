VERDICT: PARTIAL improved the conditional prefix-concentration L^p criterion from theta<1/18 to theta<1/4; T075 remains open

The earlier concentration criterion holds. Its proof was independently
re-derived, its script passed all original checks, and all twelve reported
prefix caps were independently reproduced with integer coordinates. The
bounded literature check found no solution of T075. Samuel Kittle and
Constantin Kogler's [arXiv:2611.17277v1](https://arxiv.org/html/2611.17277v1)
still assumes absolute continuity in its higher-integrability theorem.

The new result is a sharper one-dimensional quantitative implication,
proved in full in PROOF.md. Retain the earlier statistic A_n(delta), the
largest mass on a set of length delta under the n-sign prefix plus a
uniform tail, and put D=2/(1-lambda). If

    liminf_n A_n(delta) < theta < 1/4,   0 < delta <= D,

then nu_lambda is absolutely continuous. For every c>1/(1-4 theta), its
density belongs to L^p for every

    1 < p < 1 + log((c-1)/(4c theta)) / log(4cD/(delta lambda)).

The threshold for this explicit estimate improves from 1/18 to 1/4.
The absolute-continuity conclusion itself already followed from the
earlier qualitative criterion with any theta<1.

For theta<1/12, a simple admissible exponent is

    p = 1 + log(1/(12 theta)) / log(8D/(delta lambda)).

It strictly improves the earlier exponent throughout its range. At the
earlier conditional example lambda=2/3, delta=1/64, theta=1/36, it gives
p=1.130236012180298 instead of 1.065189685675672. Neither number certifies
the required infinite-subsequence bound at that parameter.

The proof replaces the dilation-by-three covering step in the analytic
lemma with a multiplicity-two cover by intervals. It establishes

    F((c/epsilon)t) <= (4c theta/(c-1)) F(t)

for large t. This yields the exponents by layer-cake integration. The
analytic argument is self-contained. No claim of priority over existing
one-dimensional reverse-Hölder estimates is made.

Commands, run from this folder:

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 ~/codex_op_1114r3/briefs/T075/prefix_concentration.py > earlier_recheck.txt 2>&1
OMP_NUM_THREADS=1 nice -n 15 python3 check_constants.py > computation.txt 2>&1
```

Both exited 0. The new script checked 4,943 exact interval families,
12 prefix caps, 18 recurrence/exponent cases, and a 1,000-point exponent
comparison. The logarithms agree with independent 60-digit arithmetic.
It ran in 0.125 seconds with peak RSS 21,069,824 bytes, one thread, actual
priority 20. Full commands, output, and failure-case checks are in LOG.md.

What failed: no estimate propagating a concentration bound to unbounded
depths was obtained. A single favorable finite value remains insufficient,
as the singular lambda=1/3 control demonstrates. No specified
transcendental parameter is newly proved absolutely continuous.

Uncertainty: no formal proof verification was run; the constants are not
asserted optimal. The literature check was bounded to five minutes and
does not establish novelty of the analytic sharpening. The proof does
not include the endpoint exponent in its open range.

Next worker: establish A_{n_j}(delta)<=theta<1 along an unbounded sequence
for one specified transcendental lambda. For quantitative integrability,
theta<1/4 now suffices with the displayed exponents. Further improvements
of the covering constants do not remove this missing estimate.

Task: “take the NEXT checkable step on this problem, building on that work.” — 2026-11-15, first recorded clock 04:37:30 +04:00.

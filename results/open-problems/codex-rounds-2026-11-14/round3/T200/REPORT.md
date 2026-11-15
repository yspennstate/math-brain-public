VERDICT: PARTIAL a conditional capacity exponential moment yielding xi_3(1,1) < 0.99817

The exact-value problem remains open. The completed extension of the earlier
report is

\[
\xi_3(1,1)\leq 1-\frac{1}{495\log3}
=0.998161132875501338598759110776\ldots<0.99817.
\]

The decimal evaluates the upper bound, not the exponent. The earlier bound
was 0.9998385758101240454...; it was independently verified before extending
it. The full argument is in [PROOF.md](PROOF.md), and the computations and
audit are recorded in [LOG.md](LOG.md).

The new lemma replaces binary good/bad capacity layers by a conditional
exponential moment. For a Brownian segment
\(K(r)=W[\sigma_r,\sigma_{2r}]\), with Newtonian capacity normalized so that
a radius-r ball has capacity r, it proves

\[
\mathbb E\!\left[\exp\!\left(-30\frac{\operatorname{cap}(K(r))}{r}\right)
\middle|\mathcal F_{\sigma_r}\right]<\frac3{25}.
\]

For \(C_j=\operatorname{cap}(K(3^j))/3^j\), successive conditioning gives
\(\mathbb P(\sum_{j<N}C_j<N/30)\leq(33/100)^N\).
The tail decays faster than \(3^{-N}\). Combining this with the earlier
Green-kernel hitting estimate and \(\xi_3(1,2)=1\) proves the stated bound.
No independent-layer assumption is used.

The scalar step is \(e^{-s/y}\leq y/(es)\). On a segment lasting at least
\(r^2/18\), the occupation measure has energy I and gives normalized capacity
at least \(1/(rI)\). Its mean energy is \(16/(r\sqrt\pi)\); the short-segment
probability is at most \(6\sqrt6e^{-15/2}\). Thus, for every s>0,

\[
\mathbb E[e^{-s\operatorname{cap}(K(r))/r}\mid\mathcal F_{\sigma_r}]
\leq6\sqrt6e^{-15/2}+\frac{16}{es\sqrt\pi}.
\]

This proves the particular exponential-moment estimate named as a possible
next step in the previous report. It also gives a stronger numerical bound
than the unproved-in-that-paper 0.999 bound mentioned in Remark 1.2 of
Runsheng Liu, *An explicit lower bound for the growth exponent of
three-dimensional loop-erased random walk*,
[arXiv:2609.18643v1](https://arxiv.org/html/2609.18643v1).
No claim of priority or a best known bound is made.

Reproduce both certificates from this folder:

```
OMP_NUM_THREADS=1 nice -n 15 python3 -B audit.py baseline
OMP_NUM_THREADS=1 nice -n 15 python3 -B audit.py moment
```

The first prints `EARLIER RESULT VERIFIED independently`. The second prints
`ALL CAPACITY-MOMENT CERTIFICATE CHECKS PASSED`. Its rational Laplace bound is
68779/573480 < 3/25, with margin 193/2867400. The rounded tail exponent is
1.0091482099346311... > 1. Rational logarithm bounds, Decimal arithmetic,
and a separate libm evaluation agree on the final gap. Both runs take less
than a second and use less than 16 MiB. The scripts check one-thread settings,
actual nice 20, a 60-second CPU limit, and measured RSS. The shell warns that
it cannot increase the inherited niceness; the checked priority is already
lower than requested. No files outside this folder were written.

The audit re-derived the Green minimum by the image formula and the energy
constant by Brownian scaling. It checked zero capacity, initial hits, the
last layer, inward returns, noninteger thresholds, and interpolation in
log-radius. In particular, the occupation measure need not lie in the
segment on the short-segment event; only the bound by one is used there.
No unresolved mathematical gap was found.

The literature check found no later exact evaluation within its five-minute
limit. The three primary papers in the brief were opened; source details
and queries are in LOG.md. The detailed proof behind Liu's Remark 1.2 could
not be obtained from the paper, which explicitly omits it. That part of the
previous worker's recommendation therefore remains unavailable. The search
does not establish novelty or the absence of other bounds. No exact exponent
or general formula for xi_3(k,lambda) has been obtained.

The next worker should first audit the exponential-moment lemma, especially
its unrestricted occupation measure and conditional iteration. A concrete
extension is to replace uniform time occupation by a deterministic weighted
time measure: minimize the expected energy with kernel |u-v|^(-1/2), then
carry its certified constant through the same moment bound. The current
parameters are convenient, with no claim of optimality.

Task: “take the NEXT checkable step on this problem, building on that work.”
T200, 15 November 2026, session began about 01:38 Asia/Tbilisi (UTC+04);
resumed for completion at 03:31.

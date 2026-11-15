VERDICT: PARTIAL radial exit estimates and xi_3(1,1) < 0.9971

The exact-value problem remains unresolved. The completed extension is

\[
\xi_3(1,1)\leq1-\frac{2}{627\log3}
=0.997096525592896850419093332804\ldots<0.9971.
\]

The decimal evaluates the upper bound, not the exponent. Round 4's bound
was 0.9980977236643117... . Its energy identity, minimizing argument,
conditional capacity estimate and numerical certificate were independently
checked first; no defect was found. The new gap below one is 29/19 times
the preceding gap, an increase of about 52.6%.

The new piece is the radial exit estimate suggested by round 4. The time
for three-dimensional Brownian motion to go from radius r to radius 2r,
divided by r squared, has exactly the same law as the exit time of a
one-dimensional Brownian motion from (-1,1), started at zero. Both Laplace
transforms are sech(sqrt(2q)). Reflection and a certified rational Gaussian
tail bound give

\[
\mathbb P(\sigma_{2r}-\sigma_r<r^2/7\mid\mathcal F_{\sigma_r})
<16311/1000000.
\]

This permits a longer occupation time than round 4's r squared/18.
Retaining its optimal deterministic time weight and factor-three layers,
the resulting conditional capacity estimate is

\[
\mathbb E\left[e^{-17\operatorname{cap}(K(r))/r}
\mid\mathcal F_{\sigma_r}\right]<13623/100000.
\]

For the sum T_N of normalized layer capacities, this yields

\[
\mathbb P(T_N<N/19)
\leq(333313941/1000000000)^N.
\]

The exceptional-tail exponent is 1.000052956527928... > 1.
Despite the small margin, the required comparison is the exact integer
inequality 999941823 < 1000000000. The earlier hitting estimate and
xi_3(1,2)=1 then prove the bound above. The full argument, including the
radial identity, Gaussian estimate, weighted energy and exponent comparison,
is in [PROOF.md](PROOF.md).

Reproduce from this folder:

```
OMP_NUM_THREADS=1 nice -n 15 python3 -B audit.py baseline
OMP_NUM_THREADS=1 nice -n 15 python3 -B audit.py radial
```

The first prints `ROUND 4 RESULT VERIFIED independently`; the second prints
`ALL RADIAL-EXIT CERTIFICATE CHECKS PASSED`. All load-bearing scalar
inequalities use exact fractions. The Gaussian tail is certified twice,
by a rational Mills bound and an integrated Taylor series. A radial heat
equation expansion independently checks the exit law at four times.
Rational logarithm bounds, Decimal arithmetic and libm agree on the gap.
The baseline directly integrates the time potential using a substitution
different from round 4's; its error decreases from 5.40e-9 to 3.32e-10 on
doubling the mesh. These quadratures are diagnostics, not proofs.

Both audits complete in under one second, use one thread and have measured
peak RSS below 16 MiB. They check inherited nice 20 and a 60-second CPU
limit. The shell's nice warning reflects its unsuccessful attempt to add
15 to an already lower-priority process; the scripts verify actual priority
before computing. The exploratory command `OMP_NUM_THREADS=1 nice -n 15
python3 -B explore.py` is optional and supplies no proof certificate.
Commands and output are recorded in [LOG.md](LOG.md).

What failed: the simpler third Gaussian Mills convergent with the old
energy rounding does not support the chosen threshold; the fifth does.
The first full radial audit passed its exact comparisons but failed a
redundant Decimal check because a rational log interval was narrower than
the 60-digit context. Increasing the context to 80 digits fixed it without
changing proof constants. An initial edit patch was rejected atomically
and was reapplied with the correct context.

The audit checked the radial function at the origin, generator and scaling,
finite stopping times, transform uniqueness, reflection factors, Mills-bound
sign, endpoint singularities, occupation support, conditional iteration,
inward returns, initial hits, zero capacity, the last layer, noninteger
thresholds and interpolation in log-radius. No unresolved mathematical
defect was found. The full capacity argument is not optimized.

The web literature check ended within five minutes and found no later exact
evaluation. Sources actually opened and queries are listed in LOG.md.
In particular, Qiyuan Shi, Runsheng Liu, Xinyi Li, Ming Li and Youjin Deng,
*Intersection Exponents of Simple Random Walks in Two and Three Dimensions*,
[arXiv:2609.25968v1](https://arxiv.org/html/2609.25968v1), still describe their
three-dimensional results as numerical. This search does not establish
absence, priority or a best known bound. Neither the exit-time identity nor
the Gaussian rational approximation is claimed to be new. No exact exponent
or general moment formula was obtained.

The next worker should audit Sections 1–2 of PROOF.md first, especially
the generator normalization and the Gaussian tail factor. A concrete next
extension is to vary the segment radius a and layer spacing b instead of
fixing them at 2 and 3. For a segment from radius 1 to a>1, the same radial
calculation gives transform a sinh(sqrt(2q))/sinh(a sqrt(2q)); for b>a,
the Green minimum is 1/(1+a)-b/(b squared+a). A certified radial exit bound
for this two-geometry-parameter family could be carried through the same
moment argument. The present calculation makes no claim about its optimum.

Task: “take the NEXT checkable step on this problem, building on that work.”
T200, 15 November 2026, session began about 08:35 Asia/Tbilisi (UTC+04).

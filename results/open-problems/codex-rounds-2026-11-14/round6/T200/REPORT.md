VERDICT: PARTIAL variable segment and layer radii yield xi_3(1,1) < 0.9969

The exact-value problem remains unresolved. The completed extension is

\[
\xi_3(1,1)\leq
1-\frac{9000}{2361557\log(17/5)}
=0.996885829783172489660892941172\ldots<0.9969.
\]

The decimal evaluates the upper bound, not the exponent. Round 5's bound
was 0.9970965255928968504... . Its main claim was independently re-derived
and certified first; no defect was found. The gap below one increases by
a factor of about 1.07257. No exact exponent, general moment formula,
optimality result or best-known-bound claim is obtained.

The new piece is the variable-geometry extension proposed by round 5.
For three-dimensional Brownian motion starting at radius one and killed at
radius a>1, its exit-time law is a times the upper-exit subprobability law
of one-dimensional Brownian motion starting at one and killed on exiting
(0,a). Both transforms are a sinh(sqrt(2q))/sinh(a sqrt(2q)), and the
one-dimensional upper-exit probability is 1/a. Reflection therefore gives

\[
\mathbb P(\sigma_{ar}-\sigma_r<ur^2\mid\mathcal F_{\sigma_r})
\leq2a\overline\Phi((a-1)/\sqrt u).
\]

For layer spacing b>a, the deterministic Green minimum is

\[
g(a,b)=\frac1{1+a}-\frac b{b^2+a}.
\]

Retaining the weighted occupation measure and scalar energy estimate from
round 5 gives a general capacity-moment lemma and exponent criterion in
[PROOF.md](PROOF.md), equations (12)–(14). The selected rational parameters
are a=19/10, b=17/5, u=81/730, s=43/2, average-capacity threshold c=5/121.
They give

\[
\mathbb E[e^{-(43/2)\operatorname{cap}(K_a(r))/r}
\mid\mathcal F_{\sigma_r}]<151/1250.
\]

For the sum S_N of the N normalized layer capacities,

\[
\mathbb P(S_N<5N/121)\leq(22952/78125)^N.
\]

The tail exponent relative to R=(17/5)^N is
1.000923043334747...>1, certified by the exact integer comparison
390184<390625. The new Green constant is 1800/19517. Its product with
c is 9000/2361557; comparison with the known second-moment exponent one
then proves the displayed bound. The proof allows inward returns and uses
conditional iteration without assuming independent layers.

Reproduce from this folder:

```
OMP_NUM_THREADS=1 nice -n 15 python3 -B audit.py baseline
OMP_NUM_THREADS=1 nice -n 15 python3 -B audit.py geometry
OMP_NUM_THREADS=1 nice -n 15 python3 -B audit.py diagnostics
```

The first prints `ROUND 5 RESULT VERIFIED independently`; the second prints
`ALL GEOMETRY CERTIFICATE CHECKS PASSED`; the third prints
`GEOMETRY DIAGNOSTICS PASSED (not a proof certificate)`.
The optional `explore.py` proposes parameters with a small deterministic
grid. It supplies no proof certificate or optimum.

All load-bearing scalar inequalities have exact rational certificates.
The Gaussian tail is certified twice, by a Mills rational bound and by
integrated Taylor series. The Green constant is checked algebraically in
two forms. Rational logarithm intervals, Decimal and libm agree on the
exponent gap. Separate radial heat-equation and image expansions agree
at four radius ratios and four times, with maximum discrepancy below
3.4e-16. The Green grid attains the analytic minimum at opposite radial
endpoints. These floating-point diagnostics supplement the proof.

Every successful numerical run took under one second. The final audits
and the diagnostics measured peak RSS below 16 MiB; they use only the
standard library, one thread, and a 60-second CPU limit. The shell's nice
warning reflects an unsuccessful attempt to add 15 to inherited nice 20;
the scripts check actual nice 20 before calculating. All writes are inside
this folder; all four earlier folders were read only. No git or subagents.

What failed: the first baseline passed its rational comparisons but failed
a redundant Decimal enclosure check because its 100-digit context did not
resolve the rational logarithm interval. Raising precision to 130 fixed it
without changing any proof constant. One combined edit patch was rejected
atomically because a log context did not match, then applied separately.
The exploratory tail-boundary optimizer is unsuitable for a proof since
its exceptional exponent equals one; the selected rational threshold leaves
a strictly positive margin. A simpler a=2, b=7/2 candidate was weaker.

The audit checked generator normalization, finite stopping times, transform
mass and uniqueness, the reflection factor, the sign of the Mills bound,
energy scaling and support, endpoint singularities, initial hits, zero
capacity, last layers, real thresholds, conditional iteration, inward
returns, and interpolation of log-radii. No unresolved mathematical defect
was found. The method still loses information in the capacity comparison
and in replacing a conditional energy by its unrestricted mean.

The literature check ended within five minutes and located no subsequent
exact evaluation. Sources actually opened and all queries are in LOG.md.
In particular, Qiyuan Shi, Runsheng Liu, Xinyi Li, Ming Li and Youjin Deng,
*Intersection Exponents of Simple Random Walks in Two and Three Dimensions*,
[arXiv:2609.25968](https://arxiv.org/abs/2609.25968), describe their 3D
estimates as numerical. This limited search establishes neither absence
nor priority. The radial identity and Gaussian approximation are not
claimed to be new.

The next worker should first audit the normalized exit-law identity in
Section 1, especially its factor a, then the simultaneous Green extrema
and strict tail comparison. A concrete extension is to strengthen (8) by
retaining relative Green capacity instead of immediately replacing it by
Newtonian capacity. A lower bound on the Green kernel's regular part can
give a nonlinear capacity-to-hitting estimate; the layer argument would
then sum that nonlinear function. No such improvement is proved here;
the current grid also leaves the continuous optimization unresolved.

Task: “take the NEXT checkable step on this problem, building on that work.”
T200, 15 November 2026, session began about 11:11 Asia/Tbilisi (UTC+04).

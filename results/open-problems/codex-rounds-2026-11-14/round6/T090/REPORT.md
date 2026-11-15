VERDICT: PROVED second logarithmic weak-coupling correction for the Gaussian second-moment rate

The round-5 result holds: its first correction was independently rederived, and its audit passed again. The bounded literature check found no solution of fixed-coupling T090. The November paper by Xue-Mei Li and Te-Chun Wang, [arXiv:2611.03191](https://arxiv.org/abs/2611.03191), concerns high moments of the critical heat flow and does not establish the requested height exponents. Opened sources and complete attribution are in LOG.md.

The new result evaluates exactly the next quantity named by round 5. For its flat-initial-data Itô SHE with diffusion coefficient 1/2 and covariance R_s(x)=(4*pi*s)^(-1) exp(-|x|^2/(4s)), let gamma(b,s) be the long-time exponential rate of E[Z(t,0)^2], g=b^2 and D=Li_2(1/4). Then

\[
 \boxed{\log\gamma(b,s)=-\frac{4\pi}{g}-\log(2s)-\gamma_{\rm E}
 +\frac{D}{4\pi}g+\frac{J}{16\pi^2}g^2+O(g^3),}
\]

where the explicit positive constant is

\[
 J=\sum_{n=1}^{\infty}\frac1n
 \left(\int_0^{1/3}\frac{x^{n-1}}{1+x}\,dx\right)^2.
\]

The new coefficient has the certified enclosure

\[
 0.00053090572038263670<\frac{J}{16\pi^2}
 <0.00053090572038263671.
\]

Equivalently, the relative expansion is

\[
 \gamma(b,s)=\frac{e^{-\gamma_{\rm E}}}{2s}e^{-4\pi/b^2}
 \left[1+\frac{D}{4\pi}b^2
 +\frac{J+D^2/2}{16\pi^2}b^4+O(b^6)\right].
\]

The relative order-b^4 coefficient is approximately 0.0007577319825377. Both remainders are uniform over s>0 by exact scaling. For SHE diffusion coefficient d0, the new logarithmic coefficient is J/(64*pi^2*d0^2).

[PROOF.md](PROOF.md) gives the complete argument. At the exact spectral crossing the next block term is <h,QAQ h>=J/(64*pi^3), h=QAv. Two algebraic expansions agree. The Gaussian integral is reduced both to a positive radial energy integral and to the convergent series above. Rational alternating-series and tail bounds certify J and the coefficient; the certificate does not depend on numerical quadrature.

Reproduce the audits from this folder:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B check_next_term.py
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B ~/codex_op_1114r5/briefs/T090/check_correction.py
```

The new audit passed. Three integral evaluations agree with the positive series to within 3e-13. Eight checks of the radial primitive passed. The independent zero-energy ODE diagnostic approaches the new coefficient; its last-two-coupling extrapolation differs by -5.193e-9. Those diagnostics are floating-point checks, not finite-coupling eigenvalues. The new audit took 0.213 seconds and 14.000 MiB peak RSS; the earlier audit took 0.241 seconds and 12.344 MiB. Commands and output are in [LOG.md](LOG.md).

What failed: the sandbox denied an incremental nice adjustment; both scripts directly confirmed inherited niceness 20. The earlier script also reported that Darwin address-space limiting was unavailable. Both ran single-threaded with a 60-second CPU limit and tiny storage. No mathematical or numerical failure was found. All new files are confined to this folder; earlier work was only read.

Limits and uncertainty: this sharpens one Gaussian annealed second-moment asymptotic. It gives no control of centered log Z, no beta or alpha, and no fixed-coupling height limit. T090 remains open here. The status search was bounded, and novelty of this coefficient in the wider spectral literature is unassessed.

Next worker: a direct continuation is the order-g^3 logarithmic term, controlled by <h,(QAQ)^2 h>=||QAQ h||^2. A step toward T090 itself instead needs a concrete estimate for centered log Z; additional positive-moment coefficients do not provide one.

Task: “take the NEXT checkable step on this problem, building on that work.” First recorded clock: 15 November 2026, 10:44:25 +04; prompt receipt time unavailable.

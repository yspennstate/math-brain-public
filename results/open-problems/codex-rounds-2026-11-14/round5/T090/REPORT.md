VERDICT: PROVED first relative correction to the Gaussian second-moment weak-coupling asymptotic

The round-4 result holds. Its resolvent normalization, Gaussian finite constant, and spectral identification were independently rederived, and its numerical audit passed again. A bounded literature check found no newer solution of fixed-coupling T090. The already identified [critical-process result](https://arxiv.org/abs/2610.31614) remains outside that regime; complete source attribution is in LOG.md.

The new result is exactly the continuation named by round 4. For its flat-initial-data Itô SHE with diffusion coefficient 1/2 and Gaussian covariance R_s(x)=(4*pi*s)^(-1) exp(-|x|^2/(4s)),

\[
 \boxed{\gamma(b,s)=\frac{e^{-\gamma_{\rm E}}}{2s}e^{-4\pi/b^2}
 \left[1+\frac{\operatorname{Li}_2(1/4)}{4\pi}b^2+O(b^4)\right].}
\]

Here gamma is the long-time exponential rate of E[Z(t,0)^2]. The relative remainder is uniform over s>0. The ratio to the earlier renewal lower endpoint x_(b^2)/(2s) has the same bracket. Thus its first gap is positive, with coefficient

\[
 \frac{\operatorname{Li}_2(1/4)}{4\pi}
 =0.021299120270804\ldots.
\]

[PROOF.md](PROOF.md) gives every step. Retaining the next block term gives c=||(I-P)Av||^2=Li_2(1/4)/(16*pi^2). Two analytic calculations of that variance, and two algebraic derivations of its contribution to log gamma, agree. For diffusion coefficient d, the exponential constant is 8*pi*d and the relative correction is Li_2(1/4)*b^2/(8*pi*d). This calculation makes no claim of priority in the wider spectral literature.

Reproduce the audits with:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B check_correction.py
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B ~/codex_op_1114r4/briefs/T090/check_prefactor.py
```

The new audit passed. Radial quadrature, a covariance double integral, and the positive dilogarithm series agree to about 1e-15. Nine special-function checks and five covariance scales passed. A separate zero-energy ODE diagnostic approaches the predicted coefficient; extrapolation from its last two couplings differs by 2.855e-8. These are floating-point checks, not certified enclosures or finite-coupling eigenvalues. Runtime was 0.245 seconds, peak RSS 12.031 MiB. The earlier audit also passed, in 0.112 seconds and 12.656 MiB. Commands and relevant output are in [LOG.md](LOG.md).

What failed: the sandbox rejected the requested incremental nice adjustment and Darwin address-space limiting. A direct query confirmed inherited niceness 20, already below the requested priority. Both audit scripts used one thread and a 60-second CPU limit. No mathematical failure was found.

Limits and uncertainty: this improves an annealed second-moment expansion for one Gaussian covariance. It does not estimate the variance of log Z, prove beta or alpha, or construct a fixed-coupling height limit. T090 remains open here. The status search was bounded, and wider novelty of the explicit coefficient was not investigated.

Next worker: a concrete continuation within this calculation is to retain the next Neumann term and evaluate the Gaussian quantity <h,QAQ h>, h=QAv, which controls the b^4 term in log gamma. A step toward T090 itself instead needs control of centered log Z; additional positive-moment coefficients alone do not provide it.

Task: “take the NEXT checkable step on this problem, building on that work.” First recorded clock: 15 November 2026, 08:12:26 +04; prompt receipt time unavailable.

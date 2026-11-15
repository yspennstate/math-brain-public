VERDICT: PROVED asymptotic sharpness of the Gaussian second-moment renewal lower endpoint at weak coupling

The round-3 result holds. Its Gaussian recursion was independently re-derived through a covariance determinant, its scalar renewal roots and rate argument check, and its script passed all 515 determinant cases again. A bounded literature check found no newer solution of the fixed-coupling KPZ problem. T090's growth exponents and height limit remain unresolved here.

The new result answers exactly the next question named in the round-3 report. For its flat-initial-data Itô SHE with diffusion coefficient 1/2, Gaussian covariance R_s(x)=(4 pi s)^(-1) exp(-|x|^2/(4s)), and g=b^2, write

\[
 \gamma(b,s)=\lim_{t\to\infty}t^{-1}\log\mathbb E[Z(t,0)^2].
\]

Then

\[
 \boxed{\gamma(b,s)=\frac{e^{-\gamma_{\rm E}}}{2s}
          e^{-4\pi/b^2}\bigl(1+O(b^2)\bigr)}.
\]

Here gamma_E is Euler's constant. Consequently, for the earlier root defined by g exp(x_g) E1(x_g)/(4 pi)=1,

\[
 \frac{\gamma(b,s)}{x_{b^2}/(2s)}=1+O(b^2)\longrightarrow1.
\]

The relative error can be chosen independent of s>0 by exact spatial scaling. For the prompt's diffusion coefficient 1, the corresponding formula is gamma_1(b,s)=(exp(-gamma_E)/s) exp(-8 pi/b^2)(1+O(b^2)).

[PROOF.md](PROOF.md) supplies the whole argument. It derives the free-resolvent constant from the heat kernel, controls the Gaussian tails by an explicit Hilbert–Schmidt remainder bound, proves the equality of the pointwise moment rate and the spectral threshold, and performs the rank-one eigenvalue expansion. The Gaussian finite constant is calculated twice, using the difference distribution and angular averaging. This is a step beyond the earlier folder, not a claim of a new general weak-bound-state phenomenon. Relevant existing spectral background is Jussi Behrndt, Petr Siegl, Nicolas Weber, [arXiv:2604.19284](https://arxiv.org/abs/2604.19284), and Sylwia Kondej, Vladimir Lotoreichik, [arXiv:1402.3995](https://arxiv.org/abs/1402.3995); the proof does not import a compact-support result for the Gaussian potential.

Reproduce the independent audits with:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B check_prefactor.py
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B ~/codex_op_1114r3/briefs/T090/check_gaussian_renewal.py
```

The new audit passed. At s=1 the prefactor is approximately 0.28072974178344. Independent logarithmic-distance calculations across five covariance scales differed by at most 1.110e-14. Direct heat-resolvent quadrature recovered the finite constant -2 gamma_E. An additional zero-energy radial-ODE diagnostic agreed under step halving to 6.040e-13 and approached the independently predicted constant. Those ODE outputs are not finite-coupling eigenvalues. Runtime was 0.076 seconds and peak RSS 11.828 MiB. The earlier script took 0.051 seconds and used 12.406 MiB. These are floating-point checks; the theorem does not depend on them. Commands and full relevant output are in [LOG.md](LOG.md).

What failed: the sandbox rejected additional nice priority adjustment and Darwin address-space limiting. A separate Python priority query established inherited niceness 20, already lower priority than requested; the nice warning did not mean ordinary priority. Both calculations used one thread, a CPU limit, tiny fixed-size storage, and measured memory far below 1 GB. One log patch failed on a wrong anchor and changed nothing. No mathematical failure was found. No git, subagents, external messages, or writes outside this folder were used.

Limits and uncertainty: this is an annealed second-moment asymptotic for one mollifier. It does not control variance of log Z, establish beta or alpha, or produce a fixed-coupling height law. The bounded search is not an exhaustive literature review, and wider novelty of the explicit Gaussian prefactor is unassessed.

Next worker: retain the distinction between annealed moments and typical height. A concrete continuation of this calculation is to retain the next block-elimination term and prove a first relative correction, evaluating ||(I-P)Av||_2^2 for the Gaussian. The present O(b^2) bound does not identify that coefficient. Reaching T090 itself still requires control of centered log Z rather than its positive moments.

Task: “take the NEXT checkable step on this problem, building on that work.” First recorded clock: 15 November 2026, 04:47:12 +04; prompt receipt time unavailable.

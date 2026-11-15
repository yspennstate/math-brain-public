VERDICT: PARTIAL nonquadratic block entropy bounds and logarithmic warm-start energy tails

The earlier results hold on independent rechecking. The new result proves
finite-step proposal entropy and energy-error tails for nonquadratic
potentials with independent blocks of bounded dimension. T305 remains open.
This block class still satisfies a dimension-independent Frobenius bound;
it does not resolve the distinction in the question.

Let \(S=\Psi_h^n\), \(\Delta=H\circ S-H\), and
\(\rho=\pi\otimes N(0,I)\). First, throughout the original class,
leapfrog reversibility gives
\[
 E_\rho f(\Delta)=E_\rho[e^{-\Delta}f(-\Delta)],
 \qquad
 0\le D_{\rm KL}(S_\#\rho\|\rho)=E_\rho\Delta
 \le\tfrac12 E_\rho[\Delta^2].
\]
This supplies a second-moment route to the previous report's proposed
entropy bound, without an exponential Taylor remainder.

For \(V=\sum_jV_j\), with block dimensions \(k_j\le k_0\), the original
spectral and operator-Lipschitz Hessian bounds, and only \(C^{2,1}\)
regularity, [PROOF.md](PROOF.md) proves, for \(h\le1\), \(nh\le T_*\),
\[
 \mu:=E_\rho\Delta\le C h^4\sum_j k_j^3
 \le C k_0^2 d h^4.
\]
Here \(C\) depends only on \(m,L,M,T_*\). For constants \(C',c>0\)
also depending on \(k_0\), every \(M_0\)-warm position start with fresh
Gaussian momentum satisfies
\[
 \Pr\{|\Delta-\mu|>2\sqrt{C'}h^2\sqrt{ds}+c^{-1}hs\}\le\delta,
 \qquad s=\log(2M_0/\delta).
\]
The warm start need not factor across blocks. This is centered at the
stationary mean. Sufficient reciprocal step sizes for fixed small average
rejection are \(O(d^{1/4}(1+s^{1/4})+s)\). No mixing conclusion is drawn.
The earlier exact-flow-subtracted remainder consequently has mean at most
\(Ck_0^2dh^4\) in this nonquadratic class.

The proof uses an exact local energy identity. Summing its two bounds
gives \(|\Delta_j|\le Bh^2(W^2+W^3)\) and
\(|\Delta_j|\le DhW^2\). The first bounds second moments; the second
makes the centered exponential-moment argument integrable. No fourth
derivatives or stationary numerical endpoints are assumed.

Reproduce the deterministic audit with:

```sh
nice -n 15 env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python3 audit.py > audit_output.txt 2>&1
```

The completed run took 10.716 seconds, one Python thread, maximum RSS
16,121,856 bytes, inherited nice 20. The wrapper's priority warning reflects
that inherited value. Results are in [audit_output.txt](audit_output.txt)
and [audit_data.json](audit_data.json); the full record is in [LOG.md](LOG.md).

Independent checks include exact rational Gaussian energy moments, the
earlier positive critical remainder limit, an exact cubic example attaining
the trapezoid constant \(1/12\), Gaussian radial moments by combinatorial
expansion, and exact rational substitution in the Chernoff calculation.
The maximum direct/local energy-identity discrepancy was \(3.145\times10^{-13}\).

The nonquadratic quadrature example has a Lipschitz Hessian and jumps in
its third derivative. At \(T=1,h=1/32\), the 800-interval calculation gives
\(E\Delta/h^4\approx0.0386081\) using the reversibility integrand,
and \(E\Delta^2/h^4\approx0.0772162\). The reflected mean changes by
\(3.85\times10^{-13}\) between 400 and 800 intervals. Direct quadrature
of the mean suffers cancellation: its scaled value is 0.0391917 on the
800-interval grid, with an exponential-identity residual of
\(-5.57\times10^{-10}\). It should not be treated as an accurate independent
mean estimate there. These computations are audits, not certified bounds.

What failed: macOS rejected a small virtual-address-space limit before
the first audit; bounded storage and measured RSS were used instead. An
initial hand-entered Gaussian convergence tolerance was too tight. The
independent bias expansion corrected it; the previous theorem was sound.
The direct quadrature limitation above remains explicit. No analytic
counterexample to the new theorem was found.

What remains uncertain: full-class entropy and warm tails without block
independence, centered nonquadratic remainder bounds, and mixing. Constants
in the tail proof can grow exponentially with block size. Without blocks,
the same deterministic argument only gives \(O(d^3h^4)\) entropy.

The next worker should try to establish
\[
 E_\rho\Delta^2\le C\{dh^4+(dh^4)^2\}
\]
for genuinely coupled targets under the original assumptions, at least
when \(dh^4\) is bounded. Together with the reversibility inequality this
would give the proposed entropy scale. A separate tail or local argument
would still be required for logarithmic warm dependence and a mixing proof.

The literature check took less than five minutes and found no settlement.
Two relevant papers actually opened were:

- Yuansi Chen, Khashayar Gatmiry, Minhui Jiang,
  *When does Metropolized Hamiltonian Monte Carlo provably outperform
  Metropolis-adjusted Langevin algorithm?*,
  [arXiv:2304.04724v3](https://arxiv.org/html/2304.04724v3).
  Section 2.4 and Table 1 retain Frobenius regularity.
- Matthew S. Zhang, Jason M. Altschuler, Sinho Chewi,
  *Algorithmic warm starts for Hamiltonian Monte Carlo*,
  [arXiv:2603.22741v1](https://arxiv.org/html/2603.22741v1).
  Assumption 3.1 and Theorem 3.4 explicitly use Frobenius-Lipschitz Hessians.

These special-case results are not claimed as a new literature theorem;
the contribution here is a direct low-regularity extension of the earlier
finite-step calculation and an explicit checkable reduction for further work.

Task: “take the NEXT checkable step on this problem, building on that work.”
— 15 November 2026, 06:31 Asia/Tbilisi (orientation clock).

VERDICT: PARTIAL finite-step energy bounds for compact coupled perturbations outside dimension-independent Frobenius regularity

The previous result survives independent rechecking. T305 remains open.
The new result proves its proposed second-moment estimate for a coupled
subclass that genuinely lacks a dimension-independent Frobenius-Lipschitz
Hessian bound. It also gives logarithmic warm-start energy tails for that
subclass. No mixing bound or larger-exponent counterexample is proved.

Let
\[
 V_d(x)=|x|^2/2+U_d(x),\qquad U_d(x)=0\quad (|x|\ge R),
\]
where \(R\) is fixed, \(U_d\in C^2\),
\(\|\nabla^2U_d\|_{\rm op}\le a<1\), and its operator-norm
Hessian-Lipschitz constant is at most a fixed \(M\). For leapfrog
\(S=\Psi_h^n\), \(h\le1\), \(nh\le T_*\), put
\(\Delta=H\circ S-H\), \(\rho=\pi\otimes N(0,I)\).
[PROOF.md](PROOF.md) proves, uniformly in dimension,
\[
 E_\rho\Delta^2\le C\{dh^4+(dh^4)^2\}.
\]
Thus \(dh^4\le1\) implies
\[
 0\le E_\rho\Delta=D_{\rm KL}(S_\#\rho\|\rho)\le Cdh^4.
\]
For every \(M_0\)-warm position start with fresh Gaussian momentum,
\[
 \Pr\left\{|\Delta|>dh^4/24+
 C_t h^2\bigl(\sqrt{ds}+s^{3/2}\bigr)\right\}\le\delta,
 \qquad s=\log(KM_0/\delta).
\]
All constants depend only on \(R,a,M,T_*\). Sufficient reciprocal step
sizes for fixed small average rejection are
\(O(d^{1/4}s^{1/4}+s^{3/4})\). This is a one-proposal statement.

Unlike round 4's bounded blocks, this subclass contains the explicit
\(C^3\), coupled family
\[
 U_d(x)=(1-|x|^2)_+^4/32.
\]
It has \(3I/4\preceq\nabla^2V_d\preceq5I/4\), operator-Hessian
Lipschitz constant at most 3, and every Frobenius-Hessian Lipschitz
constant is at least \((27/64)\sqrt{d-1}\). A \(C^{2,1}\) cubic bump
with operator constant 2 is also checked. Radial invariance and its
nonzero mixed Hessian entries preclude a decomposition into independent
bounded orthogonal blocks in growing dimension.

The mechanism is limited but explicit. Every Gaussian numerical position
is a linear combination of the initial (x,p) with coefficient norm at
least one. If \(\sigma_{\min}([x\ p])>R\), all mesh positions avoid the
perturbation and the proposal is exactly Gaussian. The exceptional event
has Gaussian probability at most \(K_R e^{-cd}\), uniformly in the number
of steps. On it, the previous deterministic estimate and Gaussian twelfth
moments suffice. Warm starts with \(\log(M_0/\delta)\gtrsim d\) require
a separate global estimate; they cannot simply discard this event.

Reproduce the audit with:

```sh
nice -n 15 env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python3 audit.py > audit_output.txt 2>&1
```

The final run took 1.320 seconds, one Python thread, maximum RSS
16,564,224 bytes, inherited nice 20. The wrapper warning reflects that
inherited priority. Output is in [audit_output.txt](audit_output.txt),
data in [audit_data.json](audit_data.json), and the record in [LOG.md](LOG.md).
Earlier folders were not modified.

Exact rational checks cover local energy errors, reversal, Gaussian
moment formulas by two expansions, radial moments by convolution,
Chernoff substitution, and the regularity constants. Path checks include
an outside start whose trajectory enters the ball, which defeats a test
based only on initial radius. A fixed-seed audit with 2,000 stationary
samples in each of dimensions 1,2,4,8,16,64 found second moments divided
by \(dh^4\) between 0.04297 and 0.04695. These samples are sanity checks,
not certified estimates. The cancellation-prone direct sample means
are recorded but do not validate the entropy bound.

What failed: using only the initial radius would miss trajectories that
enter the support; ignoring the exceptional event for all warm starts
would lose correctness for large \(M_0\). Both are handled in the proof.
No analytic counterexample to the stated subclass theorem or failed
computation was found. The proof does not extend to perturbations active
throughout the typical shell, and its constants need not remain bounded
if the support radius grows with \(d\).

What remains uncertain: the full operator-norm class, finite-step energy
control for typical-shell coupling, and the required mixing argument.
The source theorem does not apply directly to the explicit families above,
but their bad Frobenius regularity lies in a rarely visited region. This
result therefore removes a special case, not the central obstruction.

The next worker should test the same second-moment estimate for a coupled
potential whose nonlinear Hessian is active on a set of stationary mass
bounded away from zero. A concrete next family is

    V_d(x)=|x|²/2+b cos(|x|),   0<b<1/4.

Its radial lift is smooth at zero (cos(sqrt(s)) has an entire power
series in s), has dimension-independent spectral and operator-Hessian
Lipschitz bounds, and Frobenius regularity grows as sqrt\(d\) at fixed
nonzero radius. It is nonquadratic on the typical shell. The Gaussian
avoidance argument here no longer applies; radial angular-momentum
identities offer a possible replacement. No energy or mixing result for
that family is asserted here. Alternatively, a proposal-overlap lemma
for the proved compact-perturbation class would address its missing
mixing step, while still leaving the full problem open.

The bounded literature check took less than five minutes and found no
settlement. Papers actually opened:

- Yuansi Chen, Khashayar Gatmiry, Minhui Jiang,
  *When does Metropolized Hamiltonian Monte Carlo provably outperform
  Metropolis-adjusted Langevin algorithm?*,
  [arXiv:2304.04724v3](https://arxiv.org/html/2304.04724v3).
  It retains Frobenius regularity.
- Matthew S. Zhang, Jason M. Altschuler, Sinho Chewi,
  *Algorithmic warm starts for Hamiltonian Monte Carlo*,
  [arXiv:2603.22741v1](https://arxiv.org/html/2603.22741v1).
  Assumption 3.1 retains Frobenius regularity.
- Fan Chen, Sinho Chewi, Jianfeng Lu, Matthew S Zhang,
  *Smoothed Picard Hamiltonian Monte Carlo*,
  [arXiv:2609.06906v2](https://arxiv.org/abs/2609.06906).
  Its different integrator and high-accuracy construction do not settle
  the specified leapfrog MHMC question.

Task: “take the NEXT checkable step on this problem, building on that work.”
— 15 November 2026, approximately 09:06 Asia/Tbilisi (orientation clock).

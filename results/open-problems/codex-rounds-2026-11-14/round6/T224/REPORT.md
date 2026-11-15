VERDICT: PARTIAL polynomial uniform weak rates for finite output spans with commuting feature gradients

The round 5 scalar-output theorem holds. An independent clock subtraction reproduces its constants and exponent, and its audit passes again. The new result proves the next lemma proposed there: any finite collection of bounded smooth commuting feature-gradient fields admits a global joint action whose feature-average Jacobian is symmetric positive semidefinite.

Let \(\phi(w)=b+U\psi(w)\), where \(U:\mathbb R^k\to L^2(P_X)\) is an isometry, \(k<\infty\), \(|\psi|\le A\), \(\|D\psi\|_{\rm op}\le B\), and \(\psi\) has bounded second derivative. Suppose

\[
 [\nabla\psi_i,\nabla\psi_j]=0\quad\text{everywhere, for all }i,j.
\]

For exact Euclidean population gradient flow, fixed output coefficients and iid initialization, PROOF.md proves

\[
 \sup_{t\ge0}\mathbb E\|f_t^m-f_t\|_{L^2(P_X)}^2
 \le \frac{4A^2(1+B^2T)^2}{m}+6L_T\qquad(T\ge0).
\]

Thus \(L_t\le C(1+t)^{-c}\), for any \(c>0\), gives

\[
 \boxed{\displaystyle
 \sup_{t\ge0}\mathbb E\|f_t^m-f_t\|_{L^2(P_X)}^2
 \le\bigl(4A^2\max\{1,B^4\}+6C\bigr)m^{-c/(c+2)}.}
\]

The prefactor has no separate output-rank factor and is polynomial in \(d\) when \(A,B,C\) are. Commutation is an extra structural hypothesis; the exponent is not claimed sharp. This does not settle general T224.

The key identity is
\(D_s[\psi(\Psi_s(z))]=D\psi(\Psi_s(z))D\psi(\Psi_s(z))^\top\).
The population and empirical vector clocks therefore have a contractive difference equation with iid forcing of second moment at most \(A^2/m\). A regularized norm and, independently, a nonautonomous matrix evolution both give the comparison. Matrices at different times need not commute.

The proof gives a source-admissible two-input example: \(X\) uniform on \(\sqrt2e_1,\sqrt2e_2\), \(Y=\pi/2\), activation \(\arctan\), and initial parameter law uniform on the four coordinate choices \(0,1/\sqrt2\). Its output span is two-dimensional, \(L_t\sim1/(2\sqrt t)\), and square-root loss is nonintegrable. The theorem applies with rate \(O(m^{-1/5})\). This example is an application, not a lower bound.

The commutation hypothesis cannot simply be removed from this clock proof. For the same activation with normalized scalar inputs \(\alpha,2\alpha\), \(\alpha=\sqrt{2/5}\), an explicit ordered-flow feature map has Jacobian

\[
 J=\begin{pmatrix}1/50&1/25\\2/125&4/125\end{pmatrix},
 \qquad (1,-1)J(1,-1)^\top=-1/250.
\]

It is not monotone. PROOF.md also isolates the exact transported-commutator defect and shows that it changes both the clock-map Jacobian and the physical particle velocity. This is an obstruction to the argument, not an output-error counterexample to T224.

Verification commands, run from this folder:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 ~/codex_op_1114r5/briefs/T224/audit_scalar_clock.py
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 audit_commuting_clocks.py
```

Both PASS. The new audit includes 300 exact Gram cases, 300 exact raw-field commutation cases, 500 joint-action checks, 6 exact vector variances, 6,000 exact time-varying PSD comparisons, 207 raw-particle/vector-clock cases with 201 time points, 60 transported-defect quadratures and 300 source-normalization checks. A nonorthogonal feature mixing tests coupled clocks. Maximum particle/clock error is \(3.44\times10^{-10}\); the negative Jacobian direction is verified exactly and by finite differences. These supplement the proof; no all-time conclusion is inferred from simulation. Final run: nice 20, peak RSS 18,448,384 bytes, 7.995 seconds. Full outputs: commuting_clock_results.json and scalar_clock_results.json; commands and intermediate findings: LOG.md.

The literature check finished within five minutes and found no later settlement. Margalit Glasgow and Joan Bruna's [arXiv:2605.22010v3](https://arxiv.org/html/2605.22010v3), revised 11 November 2026, still covers \(c=2\) in Remark 6 and leaves slower decay open in Section 6. Also opened Song Mei, Andrea Montanari, and Phan-Minh Nguyen's [arXiv:1804.06561](https://arxiv.org/abs/1804.06561). No SOLVED_ELSEWHERE.md was created and no literature-priority claim is made.

What failed or remains uncertain: finite output rank alone does not supply the clock representation. Generic commutator bounds reintroduce exponential dependence on clock length. No rate is proved for general noncommuting fields, no sharp exponent is identified, and no weak-error counterexample is constructed. Unbounded features, sphere constraints, trained output coefficients, sample error and time discretization remain outside the theorem.

Next worker: use equations (39)--(41) to derive a comparison for actual two-field noncommuting trajectories. Control both the transported-commutator Jacobian term and the extra physical velocity term; treating only the former is insufficient. A concrete first test is whether their accumulated effect can be bounded polynomially in physical time for the normalized two-input arctangent family, beyond the separate-coordinate example. Such a bound must be proved from explicit structure or stated as an additional hypothesis, rather than inferred from the loss envelope.

Task: “take the NEXT checkable step on this problem, building on that work” — 2026-11-15 11:21 Asia/Tbilisi (first captured tool clock).

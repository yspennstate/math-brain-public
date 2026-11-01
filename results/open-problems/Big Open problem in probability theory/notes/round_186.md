# Round 186

Round 186 corrects the scale bookkeeping around the support-profile branch by
isolating the stronger anchor-count feasibility condition.

Let
\[
  \alpha_\omega=\log_\Delta\omega,
  \qquad
  L=\log_\Delta\bar\chi_p .
\]
For the expanded gate-annulus data, the selected anchors
\[
  A=\{a_z:z\in Z^\sharp\}
\]
already satisfy
\[
  |A|\ge \kappa_j^{\rm vol}(p).
\]
On the capped branch \(2^j\le U L\), the same anchors lie in
\[
  B(x,2^{j+1}+r_p),
\]
so volume growth gives
\[
  |A|\le C_{\rm vol}\bar\chi_p^{(2U+\theta)\alpha_\omega}.
\]
The lower bound on \(\kappa_j^{\rm vol}(p)\) gives
\[
  \kappa_j^{\rm vol}(p)
  \gtrsim
  L^{-3\eta}
  \bar\chi_p^{1-2\theta-4\theta\alpha_\omega}.
\]
Thus a capped anchor-count branch must obey
\[
  A_{\epsilon,\eta,J,U,C_{\rm vol}}\,
  L^{-3\eta}\bar\chi_p^{\rho(\theta,U,\omega)}
  \le 1,
\]
where
\[
  \rho(\theta,U,\omega)
  =
  1-2\theta-5\theta\alpha_\omega-2U\alpha_\omega .
\]

Consequently, capped expanded gate-annulus data occurring arbitrarily close to
criticality force
\[
  \rho(\theta,U,\omega)\le0.
\]
Optimizing \(\theta\downarrow0\), the anchor-count route forces
\[
  2^j>U\log_\Delta\bar\chi_p
  \qquad
  \left(U<\frac{1}{2\alpha_\omega}\right).
\]

This is stronger than the support-profile scale range
\(U<1/(3\alpha_\omega)\).  The support-profile branch remains useful not as
the best pure scale amplification, but as a two-replica diagnostic of the
support set \(Y\) and the annular square profile in the remaining live regime.

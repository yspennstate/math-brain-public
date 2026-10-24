# Round 183

Round 183 turns the Round 182 support-profile product into a support-volume
contradiction that recovers the optimized \(1/(3\log_\Delta\omega)\) gate-scale
threshold without using the annular Schur bound.

The product bound is proved for the specific gate set \(A=\{a_z:z\in
Z^\sharp\}\):
\[
  \frac{\mathcal R_p^{I_{j,p}^{\rm gate}}(A)}{\bar\chi_p}
  \ge
  \frac{(\kappa_j^{\rm vol}(p))^3}{\bar\chi_p^2|Y|}.
\]
But the profile size bound for this same set gives
\[
  \frac{\mathcal R_p^{I_{j,p}^{\rm gate}}(A)}{\bar\chi_p}
  \le
  \frac{|A|}{\bar\chi_p}.
\]
Hence
\[
  |Y|\ge \frac{(\kappa_j^{\rm vol}(p))^3}{\bar\chi_p|A|}.
\]

On the capped branch \(2^j\le U L\), with \(L=\log_\Delta\bar\chi_p\) and
\(\alpha_\omega=\log_\Delta\omega\),
\[
  |A|\le C_{\rm vol}\bar\chi_p^{(2U+\theta)\alpha_\omega},
  \qquad
  |Y|\le C_{\rm vol}\bar\chi_p^{(4U+2\theta)\alpha_\omega}.
\]
Meanwhile
\[
  (\kappa_j^{\rm vol}(p))^3
  \gtrsim
  L^{-9\eta}\bar\chi_p^{3-6\theta-12\theta\alpha_\omega}.
\]
Therefore the capped branch is impossible near criticality whenever
\[
  \delta(\theta,U,\omega)
  =
  2-6\theta-15\theta\alpha_\omega-6U\alpha_\omega
  >0.
\]
Letting \(\theta\downarrow0\), this is exactly
\[
  U<\frac{1}{3\alpha_\omega}.
\]

This matches the Schur-calibrated threshold from Rounds 178--179, but the proof
uses only the two-replica annular profile size bound for the specific gate set
and volume control of \(A\) and \(Y\).  Thus the \(1/(3\alpha_\omega)\) barrier
is not merely an artifact of global operator Schur; it is already visible in
the finite gate-support geometry.

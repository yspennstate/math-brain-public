# Round 182

Round 182 isolates the support-size loss in the Round 180 square-profile
argument.

Before bounding the support set \(Y\) by a ball volume, the expanded
gate-annulus data imply the product bound
\[
  |Y|\,\Theta_p(I_{j,p}^{\rm gate})
  \ge
  E_{\epsilon,\eta,J,U,C_{\rm vol}}
  L^{-9\eta}
  \bar\chi_p^{\zeta(\theta,\omega)}
\]
on the capped branch \(2^j\le U L\), where
\[
  L=\log_\Delta\bar\chi_p,\qquad
  \alpha_\omega=\log_\Delta\omega,
\]
\[
  \zeta(\theta,\omega)=1-6\theta-12\theta\alpha_\omega,
\]
and
\[
  E_{\epsilon,\eta,J,U,C_{\rm vol}}
  =
  \frac{1}{4096C_{\rm vol}^9}
  \left[\frac{\epsilon}{2}(1-2^{-\eta/2})^2\right]^9
  2^{9\eta J}U^{-9\eta}.
\]

The proof is the same Cauchy--Schwarz step as Round 180, but stopped earlier:
\[
  \Theta_p(I_{j,p}^{\rm gate})
  \ge
  \frac{(\kappa_j^{\rm vol}(p))^3}{\bar\chi_p^2|Y|},
\]
and, on the capped branch,
\[
  \kappa_j^{\rm vol}(p)
  \ge
  \frac{\sigma_j^3}{16C_{\rm vol}^3}
  \bar\chi_p^{1-2\theta-4\theta\alpha_\omega}.
\]

Round 180 then follows by applying the crude volume bound
\[
  |Y|\le C_{\rm vol}\omega^{2^{j+2}+2r_p}
  \le C_{\rm vol}\bar\chi_p^{(4U+2\theta)\alpha_\omega}.
\]
Thus the current square-profile exponent loss is not hidden in the Cauchy step.
It is exactly the replacement of \(Y\) by the whole ambient ball.  To improve
the normalized-profile route one needs either annular profile decay at the gate
scale or a sharper support-spread estimate for \(Y\).

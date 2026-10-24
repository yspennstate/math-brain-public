# Round 180

Round 180 extracts a normalized annular square-profile obstruction from the
same expanded gate-annulus data used in Rounds 176--179.

Let
\[
  \alpha_\omega=\log_\Delta\omega,\qquad
  L=\log_\Delta\bar\chi_p .
\]
On the capped branch \(2^j\le UL\), the expanded data provide a finite gate
set
\[
  A=\{a_z:z\in Z^\sharp\}
\]
and a support set
\[
  Y=\{y\in K:\exists a\in A,\ d(y,a)\in I_{j,p}^{\rm gate}\}
\]
with
\[
  |A|\ge \kappa_j^{\rm vol}(p),
  \qquad
  \sum_{a\in A}\sum_{\substack{y\in Y\\d(y,a)\in I_{j,p}^{\rm gate}}}
  \tau_p(y,a)
  \ge |A|\kappa_j^{\rm vol}(p).
\]
Applying Cauchy--Schwarz in the \(Y\)-variable and then using \(K=A\) in the
definition of \(\Theta_p(I)\) gives
\[
  \Theta_p(I_{j,p}^{\rm gate})
  \ge
  \frac{(\kappa_j^{\rm vol}(p))^3}{\bar\chi_p^2|Y|}.
\]
The volume cap gives \(|Y|\le C_{\rm vol}\omega^{2^{j+2}+2r_p}\), while
\[
  \kappa_j^{\rm vol}(p)
  \ge
  \frac{\sigma_j^3}{16C_{\rm vol}^3}
  \bar\chi_p^{1-2\theta-4\theta\alpha_\omega}.
\]
Thus the capped branch forces
\[
  \Theta_p(I_{j,p}^{\rm gate})
  \ge
  D_{\epsilon,\eta,J,U,C_{\rm vol}}
  L^{-9\eta}
  \bar\chi_p^{\gamma(\theta,U,\omega)}
\]
where
\[
  \gamma(\theta,U,\omega)
  =
  1-6\theta-14\theta\alpha_\omega-4U\alpha_\omega .
\]

Since \(\Theta_p(I)\le1\), this independently forces logarithmic gate escape
whenever \(\gamma>0\).  Optimizing \(\theta\downarrow0\) gives
\[
  U<\frac1{4\alpha_\omega}
\]
when \(\alpha_\omega>0\).  This is weaker than the Schur-calibrated operator
threshold \(U<1/(3\alpha_\omega)\), but it is useful because the obstruction is
expressed in the normalized two-replica profile rather than the unnormalized
annular operator norm.

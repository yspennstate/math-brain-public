# Round 174

This round converts the Round 173 product obstruction into a pointwise
two-point obstruction using the spherical \(L^2\)-growth invariant
\[
  \rho_{\mathrm{sph},2}(G)
  =
  \limsup_{n\to\infty}\|S_n^G\|_{2\to2}^{1/n}.
\]

The new obstruction says that, in the volume-sensitive counterexample branch,
for every \(0<\theta<1/31\) and
\[
  r_p=\lfloor\theta\log_\Delta\bar\chi_p\rfloor,
\]
one must have
\[
  \limsup_{p\uparrow p_c}
  \tau_p^{\max}(r_p)^{1/r_p}
  \ge
  \frac{p_c}{\rho_{\mathrm{sph},2}(G)}.
\]
Indeed, Round 173 gives the lower bound \(p_c\) for the product
\(\tau_p^{\max}(r_p)\|S_{r_p}^G\|_{2\to2}\), while the definition of
\(\rho_{\mathrm{sph},2}\) controls \(\|S_{r_p}^G\|_{2\to2}\) along every
logarithmic subsequence.

The matching criterion is now:
\[
  \limsup_{p\uparrow p_c}
  \tau_p^{\max}(r_p)^{1/r_p}
  <
  \frac{p_c}{\rho_{\mathrm{sph},2}(G)}
  \quad\Longrightarrow\quad
  \mathcal R_p^*/\bar\chi_p\to0,
\]
and, with quasi-transitivity plus the mean-field susceptibility input,
\[
  p_c(G)<p_{2\to2}(G).
\]

This refines the Round 173 volume-growth target \(p_c/\omega\), since the
Schur volume estimate only gives \(\rho_{\mathrm{sph},2}(G)\le\omega\).  The
current analytic target is therefore the strict logarithmic pointwise decay
bound below \(p_c/\rho_{\mathrm{sph},2}(G)\).

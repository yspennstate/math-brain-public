# Round 173

## Goal

Sharpen the logarithmic shell exponent criteria by replacing the crude
\(\Delta^{-1}\) threshold with the critical parameter \(p_c\).

## Result

Added:

- `cor:critical-logarithmic-shell-exponent-obstruction`;
- `prop:critical-logarithmic-shell-exponent-criterion`;
- `prop:critical-factored-logarithmic-shell-criterion`;
- `cor:critical-volume-growth-pointwise-logarithmic-decay-criterion`.

The key observation is that the earlier estimates used \(p\ge1/\Delta\), but
in a near-critical obstruction we may instead fix any \(q<p_c\), choose
\(p_0\ge q\), and force the selected \(p\in[p_0,p_c)\).  Each deterministic
gate path of length \(r_p\) then gives
\[
  \tau_p(a_i,z_i)\ge p^{r_p}\ge q^{r_p}.
\]
Letting \(q\uparrow p_c\) yields the sharper necessary condition
\[
  \limsup_{p\uparrow p_c}
  \left(
    \tau_p^{\max}(r_p)\|S_{r_p}^G\|_{2\to2}
  \right)^{1/r_p}
  \ge p_c,
  \qquad
  r_p=\lfloor\theta\log_\Delta\bar\chi_p\rfloor.
\]

Consequently, the volume-sensitive branch collapses if this product exponent
is strictly smaller than \(p_c\).  In factored form, it is enough to have
\[
  \limsup_{p\uparrow p_c}\tau_p^{\max}(r_p)^{1/r_p}<\alpha,
  \qquad
  \limsup_{p\uparrow p_c}\|S_{r_p}^G\|_{2\to2}^{1/r_p}<\rho,
  \qquad
  \alpha\rho<p_c.
\]
Using the volume-growth bound \(\|S_n^G\|_{2\to2}\le C_{\rm vol}\omega^n\),
it is enough to prove
\[
  \limsup_{p\uparrow p_c}\tau_p^{\max}(r_p)^{1/r_p}
  <
  \frac{p_c}{\omega}.
\]

## Interpretation

This supersedes the \(\Delta^{-1}\)-threshold criteria from Rounds 171--172.
The current analytic target is now a pointwise logarithmic-scale two-point
decay rate below \(p_c/\omega\), rather than below \(1/(\Delta\omega)\).

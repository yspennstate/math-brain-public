# Round 175

This round audits the Round 173--174 pointwise logarithmic criteria and finds
that they are formally true but vacuous as proof routes.

The reason is the open-geodesic lower bound.  For every infinite connected
locally finite graph, every \(n\), and every \(p\),
\[
  \tau_p^{\max}(n)\ge p^n.
\]
Also \(\|S_n^G\|_{2\to2}\ge1\).  Thus, for any logarithmic scale
\[
  r_p=\lfloor\theta\log_\Delta\bar\chi_p\rfloor\to\infty,
\]
one has
\[
  \limsup_{p\uparrow p_c}\tau_p^{\max}(r_p)^{1/r_p}\ge p_c
\]
and
\[
  \limsup_{p\uparrow p_c}
  \left(\tau_p^{\max}(r_p)\|S_{r_p}^G\|_{2\to2}\right)^{1/r_p}
  \ge p_c.
\]

Consequently, any criterion asking for a strict product bound below \(p_c\), or
for a strict pointwise bound below \(p_c/\rho_{\mathrm{sph},2}\) or
\(p_c/\omega\), cannot be satisfied since
\(\rho_{\mathrm{sph},2}\ge1\) and \(\omega\ge1\).

This does not invalidate the obstruction statements.  It shows that the
lossy passage from the structured endpoint obstruction to
\(\tau_p^{\max}\) discards the information needed to distinguish a genuine
finite-set trapping obstruction from harmless open geodesics.  The live route
must therefore preserve averaged, localized, or matched-pair structure rather
than trying to prove a uniform pointwise decay bound for the worst pair at the
logarithmic radius.

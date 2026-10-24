# Round 091 log

## Goal

Clarify how strong the two-replica target is relative to the original
\(p_c<p_{2\to2}\) objective.

## Result

Added `prop:l2-gap-forces-two-replica`.

If \(\bar\chi_p\to\infty\) as \(p\uparrow p_c\) and there exists \(q>p_c\)
such that \(T_q\) is bounded on \(\ell^2(V)\), then
\[
  \lim_{p\uparrow p_c}\mathcal R_p^*=0.
\]
Indeed, monotonicity gives \(T_p\le T_q\) pointwise for \(p<p_c\), so for
every finite \(K\),
\[
  \mathcal R_p(K)
  =
  \frac{\|T_p\mathbf 1_K\|_2^2}{\bar\chi_p|K|}
  \le
  \frac{\|T_q\|_{2\to2}^2}{\bar\chi_p}.
\]

## Interpretation

Bounded \(\mathcal R_p^*\) is not a cheap substitute for the target theorem:
the target theorem itself would force the profile to vanish.  The profile is
still useful because it tests only finite-set indicators and has a direct
two-replica/backscattering interpretation, but future arguments should treat it
as a necessary intermediate target closely aligned with \(p_c<p_{2\to2}\).

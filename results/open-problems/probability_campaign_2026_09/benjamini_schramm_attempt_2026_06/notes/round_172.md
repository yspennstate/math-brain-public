# Round 172

## Goal

Factor the logarithmic shell exponent target into pointwise two-point decay
and sphere-operator growth, then use the volume-growth hypothesis to get a
pure pointwise decay criterion.

## Result

Added `prop:factored-logarithmic-shell-exponent-criterion` and
`cor:volume-growth-pointwise-logarithmic-decay-criterion`.

The factored criterion says that if, for
\[
  r_p=\lfloor\theta\log_\Delta\bar\chi_p\rfloor
\]
with \(0<\theta<1/31\), there are \(\alpha,\rho>0\) such that
\[
  \limsup_{p\uparrow p_c}\tau_p^{\max}(r_p)^{1/r_p}<\alpha,
  \qquad
  \limsup_{p\uparrow p_c}\|S_{r_p}^G\|_{2\to2}^{1/r_p}<\rho,
\]
and
\[
  \alpha\rho<\Delta^{-1},
\]
then
\[
  \mathcal R_p^*/\bar\chi_p\to0.
\]
With the usual quasi-transitive mean-field input, this gives
\[
  p_c(G)<p_{2\to2}(G).
\]

The volume-growth corollary uses Schur's test:
\[
  \|S_n^G\|_{2\to2}\le C_{\rm vol}\omega^n.
\]
Thus it is enough to prove the logarithmic-scale pointwise decay
\[
  \limsup_{p\uparrow p_c}
  \tau_p^{\max}(r_p)^{1/r_p}
  <
  \frac{1}{\Delta\omega}.
\]

## Interpretation

This is a clearer analytic target than the product condition from Round 171.
The volume-sensitive branch is now reduced to a strict pointwise two-point
decay rate at the logarithmic scale \(r_p\asymp\log\bar\chi_p\), with the
threshold determined by the maximum degree and the volume-growth base.

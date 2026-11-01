# Round 171

## Goal

Repackage the logarithmic shell-growth criterion as an exponential-rate
condition at the logarithmic scale.

## Result

Added
`cor:volume-sensitive-logarithmic-shell-exponent-obstruction` and
`prop:volume-sensitive-logarithmic-shell-exponent-criterion`.

The obstruction says that any volume-sensitive counterexample forces, for
every \(0<\theta<1/31\),
\[
  \limsup_{p\uparrow p_c}
  \left(
    \tau_p^{\max}(r_p)\|S_{r_p}^G\|_{2\to2}
  \right)^{1/r_p}
  \ge
  \Delta^{-1},
  \qquad
  r_p=\lfloor\theta\log_\Delta\bar\chi_p\rfloor.
\]

The corresponding criterion is that if this limsup is strictly smaller than
\(\Delta^{-1}\) for some \(0<\theta<1/31\), then
\[
  \mathcal R_p^*/\bar\chi_p\to0,
\]
and the usual quasi-transitive mean-field input gives
\[
  p_c(G)<p_{2\to2}(G).
\]

## Interpretation

Round 170 gave a normalized logarithmic-shell inequality.  Round 171 converts
it into a sharper-looking exponential threshold: the current volume-sensitive
branch is closed by any strict exponential decay rate below \(\Delta^{-1}\) for
the product
\[
  \tau_p^{\max}(r_p)\|S_{r_p}^G\|_{2\to2}.
\]
Equivalently, any counterexample must keep this shell-growth product at least
at the \(\Delta^{-1}\) exponential rate along near-critical logarithmic
scales.

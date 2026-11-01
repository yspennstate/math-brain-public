# Round 170

## Goal

Turn the exact gate-shell operator obstruction into a pointwise shell-growth
obstruction and a usable criterion for the \(L^2\)-gap route.

## Result

Added
`cor:volume-sensitive-logarithmic-shell-growth-obstruction` and
`prop:volume-sensitive-logarithmic-shell-growth-criterion`.

The obstruction combines the exact-shell lower bound
\[
  \|T_p^{\{r_p\}}\|_{2\to2}\ge \bar\chi_p^{-\theta}
\]
with pointwise shell control
\[
  \|T_p^{\{r_p\}}\|_{2\to2}
  \le
  \tau_p^{\max}(r_p)\|S_{r_p}^G\|_{2\to2}
\]
to show that a volume-sensitive counterexample forces
\[
  \tau_p^{\max}(r_p)\|S_{r_p}^G\|_{2\to2}
  \ge
  \bar\chi_p^{-\theta},
  \qquad
  r_p=\lfloor\theta\log_\Delta\bar\chi_p\rfloor.
\]

The resulting criterion is:
if for some \(0<\theta<1/31\),
\[
  \limsup_{p\uparrow p_c}
  \bar\chi_p^\theta
  \tau_p^{\max}(r_p)\|S_{r_p}^G\|_{2\to2}<1,
\]
under the same volume-sensitive hypotheses, then
\[
  \mathcal R_p^*/\bar\chi_p\to0,
\]
and the usual quasi-transitive mean-field input gives
\[
  p_c(G)<p_{2\to2}(G).
\]

## Interpretation

This reduces the current volume-sensitive branch to a concrete logarithmic
shell-growth target.  It is still not a proof of the open problem, because the
criterion requires an upper bound at \(r_p\asymp\log\bar\chi_p\), but it gives
an explicit analytic inequality whose failure is now necessary for any
counterexample in this branch.

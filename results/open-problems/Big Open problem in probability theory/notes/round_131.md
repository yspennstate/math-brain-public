# Round 131 log

## Goal

Remove the explicit \(p^{2r_p}\) factor from the deterministic anchored
gate-incidence threshold.

## Result

Added `lem:bounded-degree-pc-lower`,
`cor:uniform-deterministic-gate-incidence-obstruction`, and
`prop:uniform-deterministic-gate-incidence-criterion`.

The bounded-degree self-avoiding-path union bound gives
\[
  p_c(G)\ge\frac1{\Delta-1}\ge\frac1\Delta.
\]
For \(p_0\) close enough to \(p_c\), the obstructing parameter \(p\ge p_0\)
satisfies \(p\ge1/\Delta\).  Since
\[
  r_p=\lfloor\theta\log_\Delta\bar\chi_p\rfloor,
\]
we get
\[
  p^{2r_p}\ge \Delta^{-2r_p}\ge\bar\chi_p^{-2\theta}.
\]

Thus the deterministic gate-incidence obstruction holds with the uniform
threshold
\[
  \widehat\kappa_j(p)=
  \frac{\sigma_j^3}{16\Delta^3}\bar\chi_p^{1-6\theta},
  \qquad 0<\theta<1/6.
\]

## Interpretation

The current target is a purely combinatorial anchored gate-incidence pattern
of polynomial susceptibility size, with no remaining explicit \(p\)-dependent
factor in the threshold.

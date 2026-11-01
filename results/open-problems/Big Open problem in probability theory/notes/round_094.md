# Round 094 log

## Goal

Convert the squared-kernel obstruction into a geometric long-range statement.

## Result

Added `prop:square-trapping-long-range`.

For bounded-degree \(G\), fixed \(R\), and \(i=1,2\),
\[
  \sup_K |K|^{-1}
  \sum_{\substack{x,y\in K\\ d(x,y)\le R}}Q_p^i(x,y)
  \le \frac{V_R}{\bar\chi_p},
\]
where \(Q_p^2\) is the squared kernel and
\[
  V_R=\sup_x |B(x,R)|.
\]

The pointwise input is simple:
\[
  Q_p(x,y)\le \bar\chi_p^{-1},
  \qquad
  Q_p^2(x,y)
  =
  \bar\chi_p^{-2}\sum_z\tau_p(x,z)\tau_p(z,y)
  \le \bar\chi_p^{-1}.
\]

Thus if \(\eta(Q_{p_n}^2)\ge\epsilon\) along \(p_n\uparrow p_c\), then the
trapping mass has to live on pairs with \(d(x,y)>R\) for every fixed \(R\).
The manuscript statement keeps a harmless factor of two because the supremum
over finite sets need not be attained.

## Interpretation

The two-replica obstruction is not local.  Any counterexample to the
sublinear two-replica criterion must create finite sets whose squared-kernel
mass persists across graph distances tending to infinity.  This is the
geometric pressure point for the separator/backscattering route.

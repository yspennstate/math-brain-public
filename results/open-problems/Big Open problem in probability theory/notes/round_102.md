# Round 102 log

## Goal

Connect the operator-tail criterion to exact-distance shell estimates.

## Result

Added `cor:shell-operator-tail-l2-gap`.

For
\[
  H_{p,n}(x,y)=\tau_p(x,y)\mathbf 1\{d(x,y)=n\},
\]
we have
\[
  T_p^{>R}=\sum_{n>R}H_{p,n}
\]
and therefore
\[
  \|T_p^{>R}\|_{2\to2}
  \le
  \sum_{n>R}\|H_{p,n}\|_{2\to2}.
\]
Thus, under the same mean-field assumptions, the shell-tail condition
\[
  \lim_{R\to\infty}\limsup_{p\uparrow p_c}
  \bar\chi_p^{-1}\sum_{n>R}\|H_{p,n}\|_{2\to2}=0
\]
implies \(p_c(G)<p_{2\to2}(G)\).

## Interpretation

This turns the far-leg route into a shell-growth target.  It can be compared
directly with nonbacktracking, self-avoiding, or fibre-sphere operator bounds.

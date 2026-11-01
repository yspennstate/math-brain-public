# Round 049 log

## Goal

Remove a weakness in the pointwise shell criterion: it seemed to require
two-point decay at some \(p>p_c\).  The goal was to see whether a criterion at
\(p_c\) already gives the strict \(L^2\) gap.

## Openness of the \(L^2\)-bounded regime

Added Proposition `prop:l2-open-right`.  If \(G\) has maximum degree \(\Delta\)
and \(T_{p_0}\) is bounded on \(\ell^2(V)\) for some \(p_0<1\), then \(T_q\)
is bounded for all \(q\in[p_0,1]\) satisfying
\[
  q<p_0+\frac{1}{\Delta\|T_{p_0}\|_{2\to2}}.
\]

The proof uses finite-volume approximations.  In a finite induced subgraph
\(W\), Russo's formula and BK give the entrywise differential inequality
\[
  \frac{d}{dp}T_p^W(x,y)
  \le
  (T_p^W A_W T_p^W)(x,y).
\]
Thus, with \(\lambda_W(p)=\|T_p^W\|_{2\to2}\),
\[
  \lambda_W(q)
  \le
  \lambda_W(p_0)+
  \Delta\int_{p_0}^q\lambda_W(s)^2\,ds.
\]
Since \(T_{p_0}^W\le T_{p_0}\), scalar comparison gives the uniform bound
\[
  \lambda_W(q)\le
  \frac{\|T_{p_0}\|_{2\to2}}
       {1-\Delta\|T_{p_0}\|_{2\to2}(q-p_0)}.
\]
Letting \(W\uparrow V\) proves the infinite-volume claim.

## Consequence

Added Corollary `cor:critical-shell-strict`.  If \(G\) has bounded degree,
\(p_c(G)<1\), and
\[
  \sum_{n\ge0}\tau_{p_c}^{\max}(n)\|S_n^G\|_{2\to2}<\infty,
\]
then
\[
  p_c(G)<p_{2\to2}(G).
\]

This is a meaningful improvement in the program.  The off-diagonal shell
decay only needs to be proved at criticality; the Russo--BK differential
inequality automatically sprinkles it to a one-sided interval above \(p_c\).

# Round 010 log

Date: 2026-06-08

## Focus

Added a coarse positive product theorem for the global SAW \(L^2\) route.

## Result

Let \(T_d\) be the \(d\)-regular tree, put \(q=d-1\), and let \(H\) be a
connected bounded-degree graph with adjacency operator \(A_H\).  If
\[
  2\sqrt q+\|A_H\|_{2\to2}<q,
\]
then
\[
  p_c(T_d\square H)<p_{2\to2}(T_d\square H).
\]

It is enough to assume
\[
  2\sqrt{d-1}+\Delta_H<d-1,
\]
where \(\Delta_H\) is the maximum degree of \(H\).

## Proof idea

Every self-avoiding path is a walk, so
\[
  C_n^{T_d\square H}\le A^n
\]
entrywise, where
\[
  A=A_{T_d}\otimes I+I\otimes A_H.
\]
Since
\[
  \|A_{T_d}\|_{2\to2}=2\sqrt q,
\]
we get
\[
  \gamma_{\rm SAW,2}(T_d\square H)
  \le 2\sqrt q+\|A_H\|_{2\to2}.
\]
The product contains a copy of \(T_d\), so
\[
  p_c(T_d\square H)\le p_c(T_d)=1/q.
\]
The displayed hypothesis gives
\[
  \gamma_{\rm SAW,2}(T_d\square H)<q\le1/p_c(T_d\square H),
\]
and the SAW operator gap criterion applies.

## Interpretation

This is not advertised as a new product theorem relative to the existing
product literature.  Its value for the program is diagnostic: the global SAW
operator route can prove some product cases, but only by a coarse argument
when the tree branching dominates the other factor.  The hard stress test is
still the low-branching regime, especially \(T_3\square\mathbb Z\).

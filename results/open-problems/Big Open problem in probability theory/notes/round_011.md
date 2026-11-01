# Round 011 log

Date: 2026-06-08

## Focus

Improved the product SAW-operator route using nonbacktracking walk kernels.

## Nonbacktracking bound

For an infinite connected \(D\)-regular graph \(X\) with adjacency operator
\(A_X\), let \(N_n\) count length-\(n\) nonbacktracking walks.  If
\[
  \rho=\|A_X\|_{2\to2},
\]
then
\[
  \limsup_{n\to\infty}\|N_n\|_{2\to2}^{1/n}\le \beta(D,\rho),
\]
where
\[
  \beta(D,\rho)
  =
  \begin{cases}
    \sqrt{D-1}, & \rho\le2\sqrt{D-1},\\
    \dfrac{\rho+\sqrt{\rho^2-4(D-1)}}{2}, & \rho>2\sqrt{D-1}.
  \end{cases}
\]

This follows because \(N_n=P_n(A_X)\), with \(P_n\) satisfying the standard
nonbacktracking recurrence.

## Product consequence

Let \(T_d\) be the \(d\)-regular tree, \(q=d-1\), and let \(H\) be an infinite
connected \(\Delta\)-regular graph.  If
\[
  \beta(d+\Delta,2\sqrt q+\|A_H\|_{2\to2})<q,
\]
then
\[
  p_c(T_d\square H)<p_{2\to2}(T_d\square H).
\]

The proof uses:
\[
  C_n^{T_d\square H}\le N_n^{T_d\square H},
\]
the nonbacktracking operator bound, and
\[
  p_c(T_d\square H)\le p_c(T_d)=1/q.
\]

## Explicit case

For \(H=\mathbb Z\), the condition becomes
\[
  \beta(d+2,2\sqrt{d-1}+2)<d-1.
\]
Writing \(s=\sqrt{d-1}\), this is
\[
  s+1+\sqrt{2s-1}<s^2,
\]
which holds for \(d\ge7\).  Thus Route A7 proves
\[
  p_c(T_d\square\mathbb Z)<p_{2\to2}(T_d\square\mathbb Z)
  \qquad d\ge7.
\]

## Interpretation

This improves the coarse all-walk theorem, which only reached larger tree
degree.  It still does not touch \(T_3\square\mathbb Z\), the most important
low-branching product stress test for this route.

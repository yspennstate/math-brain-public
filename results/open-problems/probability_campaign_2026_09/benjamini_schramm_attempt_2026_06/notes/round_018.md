# Round 018 log

Date: 2026-06-08

## Focus

Tested whether deeper vertical-fiber branching can handle
\(T_3\square\mathbb Z\), and extracted a general cluster-branching product
bound from the vertical-cluster method.

## General cluster-branching bound

Let \(T_d\) be the \(d\)-regular tree, \(q=d-1\), and let \(H\) be an infinite
connected transitive graph.  For \(p\)-bond percolation on \(H\), write
\(C_H(o)\) for the open cluster of a fixed vertex and define
\[
  \varphi_H(p)=\mathbb E_p[1-(1-p)^{|C_H(o)|}].
\]
The oriented tree-fiber exploration gives
\[
  q\varphi_H(p)>1
  \quad\Longrightarrow\quad
  p\ge p_c(T_d\square H).
\]
If the inequality holds at \(p_0\), left-continuity under the monotone coupling
gives
\[
  p_c(T_d\square H)<p_0.
\]

For \(H=\mathbb Z\), this recovers the previous formula
\[
  \varphi_{\mathbb Z}(p)
  =
  1-\frac{(1-p)^3}{(1-p+p^2)^2}
  =
  \frac{p(p^3-p^2+1)}{(p^2-p+1)^2}.
\]

## Remaining \(T_3\square\mathbb Z\) obstruction

At the nonbacktracking comparison point for \(T_3\square\mathbb Z\),
\[
  p=\frac1{\beta(5,2\sqrt2+2)}
  \approx 0.265505,
\]
the one-step vertical mean is
\[
  2\varphi_{\mathbb Z}(p)\approx0.777024.
\]
The exact two-step comparison from Round 017 gives
\[
  4\Phi(p)\approx0.650875.
\]

I also ran a finite-window Monte Carlo estimate for the fixed-ray
\(k\)-step connection probabilities \(P_k(p)\), allowing vertical movement in
the intermediate fibers and using the full starting vertical cluster.  The
estimated means \(2^kP_k(p)\) were:

- \(k=1\): about \(0.785\).
- \(k=2\): about \(0.651\).
- \(k=3\): about \(0.552\).
- \(k=4\): about \(0.466\).
- \(k=5\): about \(0.430\).
- \(k=6\): about \(0.346\).

This does not prove impossibility, but it is a useful diagnostic: fixed-depth
vertical branching along a prescribed tree ray appears to move in the wrong
direction for \(d=3\).  Closing \(T_3\square\mathbb Z\) likely requires a
self-avoidance-aware improvement of the SAW operator bound, or a percolation
comparison that uses interactions among several child fibers rather than a
single fixed descendant ray.

## Status

The manuscript now has a reusable product \(p_c\)-upper-bound proposition.
The main concrete unresolved product target is still
\[
  T_3\square\mathbb Z.
\]

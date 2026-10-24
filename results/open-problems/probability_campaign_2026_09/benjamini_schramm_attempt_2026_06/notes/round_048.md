# Round 048 log

## Goal

Turn the base-sphere fiber criterion into a more directly usable decay test.

## Pointwise shell criterion

Added Corollary `cor:pointwise-shell-decay`.  For a connected graph \(G\), let
\[
  \tau_p^{\max}(n)
  =
  \sup_{\operatorname{dist}_G(x,y)=n}\tau_p(x,y)
\]
and let \(S_n^G\) be the distance-\(n\) sphere kernel.  If
\[
  \sum_{n\ge0}\tau_p^{\max}(n)\|S_n^G\|_{2\to2}<\infty,
\]
then \(T_p\) is bounded on \(\ell^2(V(G))\), so \(p\le p_{2\to2}(G)\).

This is just the base-sphere criterion with singleton fibers, but it is the
right format for using off-diagonal two-point decay estimates.  In exponential
terms, a sufficient condition is
\[
  \limsup_n \tau_p^{\max}(n)^{1/n}
  <
  \left(\limsup_n\|S_n^G\|_{2\to2}^{1/n}\right)^{-1}.
\]

## Bounded-fiber version

Added Corollary `cor:bounded-fiber-pointwise`.  If a fiber decomposition over
\(B\) has uniformly bounded fibers, then it is enough to prove pointwise
inter-fiber decay:
\[
  \tau_{p,\mathrm{fib}}^{\max}(n)=
  \sup_{\operatorname{dist}_B(u,v)=n}
  \sup_{a\in F_u,c\in F_v}\tau_p(a,c).
\]
The finite fiber size only changes constants, so the same summability test
\[
  \sum_n \tau_{p,\mathrm{fib}}^{\max}(n)\|S_n^B\|_{2\to2}<\infty
\]
implies \(L^2\)-boundedness.

## Consequence

The current operator program can now be phrased as a concrete decay problem:
find a parameter \(p>p_c\) for which the two-point function decays across
shells faster than the \(L^2\)-growth of the corresponding sphere kernels.
This target is easier to compare with known sharpness, hyperbolic boundary,
or quotient decay estimates than the raw block-row definition of \(J_n(p)\).

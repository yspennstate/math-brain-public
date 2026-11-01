# Round 055 log

## Goal

Translate the Round 054 nonbacktracking detour generating function into a
bridge-probability criterion for regular graphs.

## Bridge-probability criterion

Added Corollary `cor:nb-bridge-probability`.  Let \(G\) be \(D\)-regular,
\(D\ge3\), and let \((X_m)\) be nonbacktracking random walk.  Define
\[
  B_n^{\mathrm{NB}}(s)
  =
  \sup_{\operatorname{dist}(x,y)=n}
  \sum_{k\ge0}s^k\mathbb P_x^{\mathrm{NB}}(X_{n+k}=y)
\]
and
\[
  \lambda_c^{\mathrm{NB,br}}(G)
  =
  \limsup_{n\to\infty}
  \bigl(B_n^{\mathrm{NB}}(p_c(G)(D-1))\bigr)^{1/n}.
\]
If
\[
  p_c(G)(D-1)\lambda_c^{\mathrm{NB,br}}(G)
  \rho_{\mathrm{sph},2}(G)<1,
\]
then \(p_c(G)<p_{2\to2}(G)\).

The proof uses the exact count-probability identity
\[
  N_m(x,y)=D(D-1)^{m-1}\mathbb P_x^{\mathrm{NB}}(X_m=y),
  \qquad m\ge1.
\]
Therefore
\[
  V_n^{\mathrm{NB}}(p_c)
  =
  \frac{D}{D-1}(D-1)^n
  B_n^{\mathrm{NB}}(p_c(D-1)),
\]
so \(\delta_c^{\mathrm{NB,end}}\le(D-1)\lambda_c^{\mathrm{NB,br}}\), and
Round 054 applies.

## Interpretation

The target is now a bridge large-deviation estimate for nonbacktracking random
walk: after weighting time excess by \(p_c(D-1)\), the probability of bridging
two fixed vertices at distance \(n\) must decay exponentially fast enough to
beat the sphere-kernel growth.

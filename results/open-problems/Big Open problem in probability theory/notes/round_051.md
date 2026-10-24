# Round 051 log

## Goal

Connect the critical shell exponent target to a deterministic combinatorial
quantity that is weaker than the global SAW operator norm.

## Endpoint SAW shell criterion

Added Corollary `cor:endpoint-saw-shell`.  Let \(C_m(x,y)\) be the number of
length-\(m\) self-avoiding paths from \(x\) to \(y\), and set
\[
  U_n^{\mathrm{SAW}}(p)
  =
  \sup_{\operatorname{dist}(x,y)=n}\sum_{m\ge n}p^m C_m(x,y).
\]
Define
\[
  \beta_c^{\mathrm{SAW,end}}(G)
  =
  \limsup_{n\to\infty}
  \bigl(U_n^{\mathrm{SAW}}(p_c)\bigr)^{1/n}.
\]
If
\[
  \beta_c^{\mathrm{SAW,end}}(G)\rho_{\mathrm{sph},2}(G)<1,
\]
then \(p_c(G)<p_{2\to2}(G)\).

The proof is the self-avoiding witness union bound:
if two vertices at distance \(n\) are connected, the open cluster contains an
open self-avoiding path between them of some length \(m\ge n\).  Therefore
\[
  \tau_{p_c}^{\max}(n)\le U_n^{\mathrm{SAW}}(p_c),
\]
so \(\alpha_c^{\max}\le\beta_c^{\mathrm{SAW,end}}\), and Round 050 applies.

## Why this is useful

The earlier global SAW criterion controls the operator norm of all length-\(m\)
SAW endpoints.  This new test only controls critical self-avoiding witnesses
between two fixed vertices at a prescribed graph distance.  On a regular tree,
there is only the geodesic witness, so
\[
  U_n^{\mathrm{SAW}}(p_c)=p_c^n,
  \qquad
  \beta_c^{\mathrm{SAW,end}}(T_d)=\frac{1}{d-1}.
\]
Thus the criterion matches the critical shell exponent in the tree model and
gives a more precise target for geometries where the global SAW operator norm
is inflated by many endpoints.

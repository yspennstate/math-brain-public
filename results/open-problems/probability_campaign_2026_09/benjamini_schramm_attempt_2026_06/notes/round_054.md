# Round 054 log

## Goal

Weaken the separable nonbacktracking excess-length criterion from Round 053 to
a single fixed-endpoint detour generating function.

## Detour generating function

Added Corollary `cor:nb-detour-generating`.  Let \(N_m(x,y)\) count
length-\(m\) nonbacktracking walks from \(x\) to \(y\), and define
\[
  V_n^{\mathrm{NB}}(p)
  =
  \sup_{\operatorname{dist}(x,y)=n}
  \sum_{k\ge0}p^kN_{n+k}(x,y).
\]
Set
\[
  \delta_c^{\mathrm{NB,end}}(G)
  =
  \limsup_{n\to\infty}
  \bigl(V_n^{\mathrm{NB}}(p_c)\bigr)^{1/n}.
\]
If
\[
  p_c(G)\,\delta_c^{\mathrm{NB,end}}(G)\rho_{\mathrm{sph},2}(G)<1,
\]
then \(p_c(G)<p_{2\to2}(G)\).

The proof is the same fixed-endpoint witness bound:
\[
  \tau_{p_c}(x,y)
  \le
  \sum_{k\ge0}p_c^{n+k}C_{n+k}(x,y)
  \le
  p_c^n V_n^{\mathrm{NB}}(p_c)
\]
when \(\operatorname{dist}(x,y)=n\).  Hence
\[
  \alpha_c^{\max}(G)
  \le
  p_c(G)\delta_c^{\mathrm{NB,end}}(G),
\]
and the critical shell exponent criterion applies.

## Why this improves the target

The Round 053 condition \(E_{n,k}^{\mathrm{NB}}\le A a^n r^k\) is enough, but
it is not necessary.  Round 054 only asks for the weighted sum over all detours
at the critical parameter after the endpoints have been fixed.  This is a more
natural target for transfer-matrix or radial computations.

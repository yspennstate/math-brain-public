# Round 052 log

## Goal

Make the endpoint SAW shell criterion easier to check by separating geodesic
distance from excess path length.

## Excess-length endpoint criterion

Added Corollary `cor:excess-length-saw`.  For \(n,k\ge0\), define
\[
  E_{n,k}^{\mathrm{SAW}}(G)
  =
  \sup_{\operatorname{dist}(x,y)=n} C_{n+k}(x,y),
\]
where \(k\) is the excess length beyond a geodesic.

If there are constants \(A,a,r<\infty\) such that
\[
  E_{n,k}^{\mathrm{SAW}}(G)\le A a^n r^k
  \qquad(n,k\ge0),
\]
and
\[
  p_c(G)r<1,
  \qquad
  p_c(G)a\,\rho_{\mathrm{sph},2}(G)<1,
\]
then \(p_c(G)<p_{2\to2}(G)\).

The proof sums over \(m=n+k\):
\[
  U_n^{\mathrm{SAW}}(p_c)
  \le
  A(p_c a)^n\sum_{k\ge0}(p_c r)^k.
\]
Thus \(\beta_c^{\mathrm{SAW,end}}\le p_c a\), and the endpoint SAW shell
criterion applies.

## Interpretation

This creates two deterministic counting targets:

1. Control the number of fixed-endpoint witnesses that actually move distance
   \(n\), with exponential rate \(a\).
2. Control the extra entropy from detours, with rate \(r\), in a way that is
   summable at \(p_c\).

For a tree, \(a=1\) and the detour term is absent, recovering the exact
critical shell exponent.

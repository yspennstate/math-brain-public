# Round 053 log

## Goal

Create a standard nonbacktracking-walk version of the excess-length endpoint
criterion, preserving the fixed-endpoint information that the older global
nonbacktracking operator route loses.

## Nonbacktracking excess-length criterion

Added Corollary `cor:excess-length-nb`.  Let \(N_m(x,y)\) count length-\(m\)
nonbacktracking walks from \(x\) to \(y\), and define
\[
  E_{n,k}^{\mathrm{NB}}(G)
  =
  \sup_{\operatorname{dist}(x,y)=n} N_{n+k}(x,y).
\]
If
\[
  E_{n,k}^{\mathrm{NB}}(G)\le A a^n r^k
  \qquad(n,k\ge0),
\]
and
\[
  p_c(G)r<1,
  \qquad
  p_c(G)a\,\rho_{\mathrm{sph},2}(G)<1,
\]
then \(p_c(G)<p_{2\to2}(G)\).

The proof is immediate from Round 052 because every self-avoiding walk is
nonbacktracking:
\[
  E_{n,k}^{\mathrm{SAW}}(G)\le E_{n,k}^{\mathrm{NB}}(G).
\]

## Interpretation

This does not solve the main conjecture.  It gives a more computable target:
bound nonbacktracking paths between two fixed vertices at distance \(n\), with
the detour length \(k\) tracked separately.  Recurrences, transfer matrices,
and radial decompositions can now be tested against the two inequalities
\(p_c r<1\) and \(p_c a\rho_{\mathrm{sph},2}<1\).

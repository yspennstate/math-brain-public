# Round 057 log

## Goal

Turn the nonbacktracking bridge criterion into a finite-state certificate that
future computations can target directly.

## Finite-state bridge certificate

Added Proposition `prop:finite-state-bridge-certificate`.  Let \(G\) be
\(D\)-regular and put \(s_c=p_c(G)(D-1)\).  Suppose there is a finite state set
\(\mathcal S\), a nonnegative matrix \(M\), and nonnegative vectors \(a,b\) such
that
\[
  B_n^{\mathrm{NB}}(s_c)\le a^TM^nb
  \qquad(n\ge1).
\]
If
\[
  p_c(G)(D-1)\rho(M)\rho_{\mathrm{sph},2}(G)<1,
\]
then \(p_c(G)<p_{2\to2}(G)\).

The proof uses the finite-dimensional bound
\[
  a^TM^nb\le C_\theta\theta^n
  \qquad(\theta>\rho(M)),
\]
so \(\lambda_c^{\mathrm{NB,br}}\le\rho(M)\), and then applies the bridge
criterion from Round 055.

## Why this matters

This is a certificate format rather than a new theorem about all graphs.  A
radial quotient, automaton, or transfer-matrix computation can overcount
weighted nonbacktracking bridges; if the resulting Perron root is small enough,
the strict \(L^2\) gap follows.

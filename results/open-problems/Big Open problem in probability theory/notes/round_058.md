# Round 058 log

## Goal

Make the finite-state bridge certificate practical when \(p_c\) is not known
exactly.

## Upper-bound certificate

Added Corollary `cor:finite-state-upper-pc`.  Let \(G\) be \(D\)-regular and
suppose \(q\in(0,1)\) is an independently known upper bound on criticality:
\[
  p_c(G)\le q.
\]
Put \(s_q=q(D-1)\).  If a finite nonnegative matrix \(M\) and nonnegative
vectors \(a,b\) satisfy
\[
  B_n^{\mathrm{NB}}(s_q)\le a^TM^nb
  \qquad(n\ge1),
\]
and
\[
  q(D-1)\rho(M)\rho_{\mathrm{sph},2}(G)<1,
\]
then \(p_c(G)<p_{2\to2}(G)\).

The proof is monotonicity: \(B_n^{\mathrm{NB}}(s)\) is nondecreasing in \(s\),
so a certificate at \(q(D-1)\) also certifies the unknown critical value
\(p_c(D-1)\).  The displayed inequality also dominates the one with \(p_c\) in
place of \(q\), so the Round 057 certificate applies.

## Why this matters

Computations rarely know \(p_c\) exactly.  This corollary lets future work use
any comparison or branching-process upper bound \(q\) for \(p_c\), then run the
bridge transfer-matrix computation at \(q(D-1)\).

# Round 059 log

## Goal

Make the finite-state bridge certificate exactly checkable once a computation
has produced a matrix majorant.

## Collatz-Wielandt certificate

Added Corollary `cor:collatz-bridge-certificate`.  Let \(q\ge p_c(G)\), let
\(R\ge\rho_{\mathrm{sph},2}(G)^2\), and suppose a finite-state bridge majorant
has matrix \(M\):
\[
  B_n^{\mathrm{NB}}(q(D-1))\le a^TM^nb.
\]
If there are \(\lambda>0\) and \(v>0\) such that
\[
  Mv\le\lambda v
\]
coordinatewise and
\[
  \bigl(q(D-1)\lambda\bigr)^2R<1,
\]
then \(p_c(G)<p_{2\to2}(G)\).

The point is that \(Mv\le\lambda v\) proves \(\rho(M)\le\lambda\) by
Collatz-Wielandt.  Squaring the final inequality lets all quantities be
rational even when \(\rho_{\mathrm{sph},2}\) itself is a square root.

## Verifier

Added `scripts/bridge_certificate_verify.py`.  It checks the
Collatz-Wielandt part of a certificate using exact rational arithmetic:

- all entries of \(M\) are nonnegative;
- \(v\) is strictly positive;
- \(Mv\le\lambda v\);
- \((q(D-1)\lambda)^2R<1\).

The script intentionally does not verify the graph-specific bridge majorization
\(B_n^{\mathrm{NB}}\le a^TM^nb\); that must be supplied by a radial,
automaton, or transfer-matrix construction.

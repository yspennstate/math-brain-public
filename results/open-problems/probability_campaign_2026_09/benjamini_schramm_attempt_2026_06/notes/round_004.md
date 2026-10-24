# Round 004 log

Date: 2026-06-08

## Focus

Converted the two obstructions from round 003 into deterministic estimates:

1. an interior estimate using killed self-avoiding path counts;
2. boundary-weight norm estimates showing what the boundary alternative
   actually forces.

## Interior killed-SAW criterion

For a finite set \(K\), let \(c_n^K(x)\) be the number of length-\(n\)
self-avoiding paths starting at \(x\) and staying in \(K\), and set
\[
  A_n(K)=|K|^{-1}\sum_{x\in K}c_n^K(x).
\]
The manuscript now proves
\[
  S_p(K)/|K|\le \sum_{n\ge0}p^n A_n(K).
\]
Consequently, if there are \(C<\infty\) and \(\theta<1/p_c\) such that
\[
  A_n(K)\le C\theta^n
\]
for every finite \(K\), then
\[
  \sup_K S_p(K)/(\bar\chi_p |K|)\to0
  \quad\text{as }p\uparrow p_c.
\]
This rules out the interior alternative.

## Boundary-weight bounds

For
\[
  B_p(K)=\sum_{a\in\partial_{\rm in}K}\chi_p^K(a),
  \qquad
  M_p(K)=\max_{a\in\partial_{\rm in}K}\chi_p^K(a),
\]
and maximum degree \(\Delta\), the manuscript now proves
\[
  \|\mu_{p,K}\|_1\le \Delta B_p(K),\qquad
  \|\mu_{p,K}\|_\infty\le \Delta M_p(K),
\]
and
\[
  \|\mu_{p,K}\|_2^2
  \le \Delta^2M_p(K)B_p(K)
  \le \Delta^2M_p(K)S_p(K).
\]
Therefore the boundary alternative forces
\[
  M_p(K)B_p(K)\gtrsim |K|.
\]

## Important limitation

This shows that a plain Cheeger-bound argument cannot close the proof.
Nonamenability lower-bounds boundary size, but the obstruction is
susceptibility-weighted boundary concentration and the energy
\(\langle\mu_{p,K},Q_p\mu_{p,K}\rangle\).  The next proof needs to control
that energy, not just \(|\partial K|\).

## Next target

Search for a class of nonamenable quasi-transitive graphs where the killed-SAW
growth condition \(A_n(K)\le C\theta^n\), \(\theta<1/p_c\), can be proved.
Then pair it with a boundary-energy estimate.  Regular trees and hyperbolic
graphs are the calibration cases; a new class beyond current literature would
be a publishable intermediate theorem.


# Round 003 log

Date: 2026-06-08

## Focus

Audited the round-002 last-exit lemma for referee-level correctness.

## Correction made

The round-002 notes described the middle segment between first exit and last
re-entry as an "outside connection." That is too strong. If a self-avoiding
path exits \(K\) for the first time and later re-enters \(K\) for the last
time, the middle subpath may still make additional excursions through \(K\).

The manuscript now states the correct version:

- the path is split into five edge-disjoint pieces;
- the middle connection is the ambient event \(b\leftrightarrow c\) in \(G\);
- the BK step uses edge-disjoint witnesses, not a complement-restricted
  connection.

The displayed last-exit inequality remains the same, because it already used
the ambient \(\tau_p(b,c)\).

## New boundary \(L^2\) obstruction

For \(z\notin K\), define the boundary susceptibility weight
\[
  \mu_{p,K}(z)=\sum_{\substack{a\in K\\a\sim z}}\chi_p^K(a).
\]
The boundary alternative is
\[
  p^2\langle \mu_{p,K},Q_p\mu_{p,K}\rangle \gtrsim |K|.
\]
Since \(Q_p\) is an \(\ell^2\)-contraction, this implies
\[
  \|\mu_{p,K}\|_2^2\gtrsim |K|.
\]

This is a sharper obstruction than the previous boundary-transfer statement:
future work can try to show that if the interior alternative fails, then
nonamenability prevents this much weighted boundary concentration.

## Next target

Prove a deterministic inequality of the form
\[
  \|\mu_{p,K}\|_2^2
  \le C(\Delta)\, \Phi(K,p)\, S_p(K)
\]
where \(\Phi(K,p)\) is small when \(K\) is not close to being a
near-critical finite-volume cluster trap.  A strong enough version would rule
out the boundary alternative whenever the interior alternative fails.


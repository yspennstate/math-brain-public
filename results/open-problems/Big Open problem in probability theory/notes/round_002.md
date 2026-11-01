# Round 002 log

Date: 2026-06-08

## Focus

The previous draft had a broad bridge: failure of finite-set escape should
somehow imply a Folner sequence.  This round sharpened that bridge into a
concrete BK-based finite-volume/boundary dichotomy.

## New lemma added to the paper

For a finite set \(K\), let \(\tau_p^K\) denote the two-point function using
only edges in the induced subgraph on \(K\), and let
\[
  \chi_p^K(x)=\sum_{y\in K}\tau_p^K(x,y).
\]
Let \(\partial^+K\) be the oriented edge boundary from \(K\) to \(V\setminus K\).
The new last-exit decomposition is
\[
  \sum_{x,y\in K}\tau_p(x,y)
  \le
  \sum_{x,y\in K}\tau_p^K(x,y)
  +
  p^2
  \sum_{\substack{(a,b)\in\partial^+K\\(d,c)\in\partial^+K}}
  \chi_p^K(a)\tau_p(b,c)\chi_p^K(d).
\]

The proof chooses a self-avoiding open path from \(x\) to \(y\), records its
first exit from \(K\) and last re-entry into \(K\), and applies BK to five
edge-disjoint witnessed events: internal connection to the first-exit vertex,
first boundary edge open, ambient middle connection, last boundary edge open,
and internal connection from the last-entry vertex to \(y\).  Round 003
clarifies that the middle connection is ambient; it need not stay outside
\(K\).

## Dichotomy

If normalized trapped mass persists,
\[
  |K|^{-1}\sum_{x,y\in K}Q_p(x,y)\ge\epsilon,
  \qquad Q_p=\tau_p/\bar\chi_p,
\]
then either:

1. the finite induced graph on \(K\) has total susceptibility
   \(\sum_{x,y\in K}\tau_p^K(x,y)\gtrsim \bar\chi_p |K|\); or
2. the boundary susceptibility weights have large interaction through the
   ambient graph:
   \[
   p^2
   \sum_{(a,b),(d,c)\in\partial^+K}
   \chi_p^K(a)Q_p(b,c)\chi_p^K(d)
   \gtrsim |K|.
   \]

## Why this helps

This replaces the vague "trapped mass implies almost invariance" step with two
specific tasks:

- rule out large finite-volume susceptibility in arbitrary finite induced
  subgraphs near \(p_c\);
- rule out large normalized boundary-to-boundary transfer using
  nonamenability.

Both tasks are still hard, but they are precise enough to attack separately.

## Next target

Try to prove an interior-alternative bound of the following form:

\[
  \sup_K \frac{\sum_{x,y\in K}\tau_p^K(x,y)}{\bar\chi_p |K|}\to0
  \quad\text{as }p\uparrow p_c
\]

under a natural extra hypothesis that is weaker than hyperbolicity. If that
works, pair it with a boundary-transfer estimate to get a publishable
intermediate theorem.

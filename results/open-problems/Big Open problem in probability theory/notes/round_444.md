# Round 444 root return intervals cover contiguous level blocks

Round 444 improves the deterministic spread-return split by replacing raw
level subsets with root coverage intervals.

Let \(I=[s,t]\) be an exterior return interval through level \(u\), and let
\[
  M(I)=\max_{s\le r\le t} d(x,v_r).
\]
Then \(I\) generates exterior returns through every level
\[
  w\in\{u,u+1,\ldots,M(I)\}.
\]
Indeed, fix such a \(w\).  Since the path reaches level \(M(I)\ge w\) and
later returns to level \(u-1<w\), there is an inward token \(w\to w-1\)
inside \(I\).  Applying the inward-token lemma to that token, with the last
preceding visit to level \(w-1\), gives an exterior return through \(w\)
contained in \(I\).

Thus a root interval in the laminar return forest carries a whole radial
coverage block
\[
  C(I)=[u,M(I)]\cap\mathbb N.
\]
Every selected return level in the spread event is contained in the union of
the coverage blocks of the root intervals.  If the spread event has
\[
  N=\delta L_H
\]
selected return levels, and the root intervals are \(I_1,\ldots,I_m\), then
\[
  \left|\bigcup_{r=1}^m C(I_r)\right|\ge N.
\]

Moreover, if \(h(I)=|C(I)|=M(I)-u+1\), then \(I\) has length and defect at
least
\[
  |\eta_I|\ge 2h(I).
\]
The interval must climb from radius \(u-1\) to \(M(I)\) and later return to
radius \(u-1\).  Since an exterior return starts and ends at the same radius,
its defect equals its length.

This reframes the entropy problem.  A spread-return witness does not require
choosing an arbitrary subset of \(N\) levels from a slab.  It produces a union
of at most \(m\) radial intervals covering those levels.  If \(m\) is small,
the level entropy is interval-cover entropy rather than binomial subset
entropy.  If \(m\) is large, the root intervals are pairwise time-disjoint
and the annular transfer/cut machinery from Rounds 438--442 applies at
linear density.

The two-rail corridor from Round 434 is now correctly classified: it has
one root interval with a long coverage block.  Its cost is only linear in the
number of covered levels, but its level-placement entropy is also only the
entropy of one interval, not the entropy of choosing an arbitrary subset of
levels.

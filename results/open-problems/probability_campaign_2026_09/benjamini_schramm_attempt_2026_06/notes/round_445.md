# Round 445 coverage-entropy split

Round 445 extracts the quantitative split suggested by Round 444.

Let the slab have
\[
  B=\beta L_H+O(1)
\]
integer levels and let the spread-return event require
\[
  N=\delta L_H+O(1)
\]
return levels.  Choose one return interval for each selected level, form the
laminar forest, and keep only its root intervals.  Let \(m\) be the number of
root intervals, and let \(C_1,\ldots,C_m\) be their radial coverage blocks.
Then
\[
  \left|\bigcup_{r=1}^m C_r\right|\ge N.
\]

Fix a density parameter \(\kappa>0\).

If \(m\ge \kappa L_H\), then the witness has linearly many pairwise
time-disjoint root exterior returns.  This is the disjoint-root branch.  It
should be attacked by the corrected annular transfer and subset-energy
machinery.

If \(m<\kappa L_H\), then the selected levels are covered by fewer than
\(\kappa L_H\) intervals inside a slab of length \(B\).  The number of
possible coverage unions is bounded at logarithmic scale by
\[
  \exp\left[\beta H(2\kappa/\beta)L_H+o(L_H)\right]
\]
when \(2\kappa<\beta\).  This replaces the raw subset entropy
\[
  \exp\left[\beta H(\delta/\beta)L_H+o(L_H)\right].
\]

The root intervals also force direct defect.  If \(h_r=|C_r|\), then their
time-disjoint interiors give
\[
  d_{\rm roots}\ge 2\sum_{r=1}^m h_r
  \ge 2N.
\]
Thus the \(Q^d\) weight contributes at least the factor
\[
  Q^{2N}=\exp[-2\delta|\log Q|L_H+o(L_H)].
\]
Consequently, the few-root branch has a plausible entropy-cost condition:
\[
  \beta H(2\kappa/\beta)
  <
  2\delta|\log Q|.
\]
For every fixed \(\delta>0\) and \(Q<1\), this can be achieved by taking
\(\kappa>0\) small enough.

This is a better deterministic reduction than the earlier chain-antichain
split.  It preserves a positive-density disjoint branch, although possibly
with density \(\kappa\ll\delta\), while the complementary few-root branch has
only interval-cover entropy and can in principle be paid for by the direct
root-span defect.

The remaining work is not trivial: one still has to implement this as an
actual property-restricted profile bound, with a controlled decomposition of
SAWs into root intervals and skeletons.  But the entropy obstruction from
Round 427 is now localized to the many-root branch rather than applying to
all spread-return witnesses.

# Round 447 jump-skeleton correction to coverage cost

Round 447 corrects the bookkeeping needed to turn the few-root coverage branch
into an actual counting estimate.

Deleting a root exterior-return interval \(I=[s,t]\) from a self-avoiding
path does not leave an ordinary path.  It leaves a gap from
\[
  a=v_s\in S_{u-1}(x)
  \qquad\text{to}\qquad
  b=v_t\in S_{u-1}(x).
\]
The right skeleton object is therefore a path with a formal same-sphere jump
\[
  a\leadsto b.
\]
This jump should be charged as one horizontal step in the radial defect.

If the deleted return interval has length \(|I|\), then its defect
contribution is \(|I|\), while the formal jump contributes \(1\).  Thus
deleting \(m\) pairwise time-disjoint root intervals gives a jump skeleton
\(\gamma^\circ\) with
\[
  d(\gamma^\circ)
  =
  d(\gamma)-\sum_{r=1}^m |I_r|+m.
\]
Equivalently,
\[
  d(\gamma)-d(\gamma^\circ)
  =
  \sum_{r=1}^m (|I_r|-1).
\]

If \(h_r\) is the coverage length of \(I_r\), then \(|I_r|\ge2h_r\).  Hence
\[
  d(\gamma)-d(\gamma^\circ)
  \ge
  2\sum_{r=1}^m h_r-m.
\]
In the few-root coverage branch,
\[
  \sum_{r=1}^m h_r\ge N=\delta L_H,
  \qquad m<\kappa L_H,
\]
so the net defect gain over the jump skeleton is at least
\[
  (2\delta-\kappa)L_H+O(1).
\]

Thus the entropy-cost condition from Round 445 should be read, for a genuine
deletion/skeleton estimate, as
\[
  \beta H(2\kappa/\beta)
  <
  (2\delta-\kappa)|\log Q|.
\]
This is still achievable for every fixed \(\delta>0\) by taking \(\kappa>0\)
small enough.

The corrected few-root strategy is therefore:

1. encode the root coverage intervals by at most \(\kappa L_H\) radial
   intervals;
2. delete the corresponding return subpaths and replace them by formal
   same-sphere jumps;
3. prove that the resulting jump-skeleton profiles are no larger, at the
   logarithmic scale, than the existing radial skeleton profiles plus the
   interval-cover entropy;
4. use the net defect gain \((2\delta-\kappa)L_H\) to pay for that entropy.

This isolates the missing technical lemma.  The deterministic coverage split
is sound, but the few-root branch is not closed until jump-skeleton profiles
are controlled.

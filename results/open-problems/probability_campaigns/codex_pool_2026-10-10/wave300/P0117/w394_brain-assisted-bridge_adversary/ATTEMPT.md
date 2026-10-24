# P0117 independent obstruction and bridge

Worker w394, 2026-10-10. This independent derivation was saved before reading any w393 proof. Primary-source recovery is still in progress. No claim of solving P0117 is made.

The ranking's phrase "planar iid FPP" is insufficient as a theorem statement: for iid weights identically equal to 1, the horizontal doubly infinite lattice path is a bigeodesic. Every finite segment has passage time equal to its lattice distance. A non-atomic law or another explicit restriction is therefore essential. The intended non-atomic formulation will be recorded separately from this literal-title counterexample.

Independent bridge (draft proof; w395 must check): Fix a nearest-neighbor Z^2 environment with finite strictly positive edge weights. Let T(x,y) be the infimum of weights of all finite paths from x to y. A finite geodesic realizes that infimum. Write S_R={z: ||z||_infinity=R}. Let E_R be the event that some finite simple geodesic between two distinct vertices of S_R contains 0. Then E_(R+1) is a subset of E_R, and intersection_(R>=1) E_R is exactly the event that a bigeodesic contains 0.

Proof: Truncate either arm of a finite geodesic through 0 at its first visit to S_R. Subpaths are geodesics, so the truncated path remains a witness. It lies in [-R,R]^2 and has distinct endpoints because the path is simple. For each R there are only finitely many oriented simple witness paths in that box. Make these witnesses level R of a tree, with parent given by first-exit truncation at radius R-1. Truncation composes, each level is finite, and arbitrarily deep witnesses give an infinite branch by the finite-branching tree lemma. Its union is simple and unbounded on both sides of 0. Each finite subpath is contained in a finite witness and is geodesic. Conversely any bigeodesic through 0 gives witnesses at all R by first-exit truncation. No iid assumption, curvature, direction, or finite-geodesic uniqueness is needed for this deterministic equivalence.

In a translation-invariant random model, continuity of probability for decreasing events yields P(a bigeodesic contains 0)=lim_R P(E_R). If this is zero, countable union over all lattice vertices gives almost-sure absence everywhere.

Let A_(R,x,y) be the event that some finite geodesic from x to y contains 0 (use "the unique geodesic" when uniqueness holds). There are M_R=binomial(8R,2)=32R^2-4R unordered distinct pairs in S_R. Thus P(E_R)<=sum_{unordered x,y in S_R} P(A_(R,x,y))<=M_R q_R, where q_R is the supremum of these pair probabilities. A sufficient bridge is a subsequence R_j->infinity with M_(R_j) q_(R_j)->0; q_R=o(R^-2) is one stronger sufficient condition. Independence is not needed for this union bound.

The logical obstruction is exact: take U uniform on [0,1), partition it into M_R intervals, and let A_(R,j) mean U is in interval j. Each pair-event analogue has probability 1/M_R, uniformly tending to zero, while their union has probability 1 for every R. This is a probability counterexample to an inference from individual vanishing to vanishing of a growing union. It is not a counterexample to the iid non-atomic FPP conjecture. It also shows an O(R^-2) bound with a nonzero coefficient is insufficient for the bare union-bound argument.

Hardest remaining piece: prove decay of the whole adaptive endpoint event E_R, or an adequate bound on the sum of endpoint-pair probabilities, under the original iid non-atomic hypotheses. A deterministic-direction theorem or qualitative midpoint limit must not be silently upgraded to that statement.

NEXT: Read exact intake and primary statements; compare w393's selected bridge to this independently saved obstruction.

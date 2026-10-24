# Further boundary construction to finish

Coordinator checkpoint, 2026-09-15. This is a proposed continuation, not a completed full-dimensional boundary theorem.

ROOT_DIAMOND_ACTIVE_MATRIX.md gives full active 2x2 covariance concavity on K0=P_W+VMV*, with W and its complementary zero-eigenspace each rank one on four measured sites. Assume both one-dimensional endpoint vectors have all coordinates nonzero. Then all singleton/triple atoms are positive, and the middle two-element atoms should be positive by the exterior row-rank argument. Only the empty/full atoms vanish.

A possible next proof is to combine a strict active gap with the simultaneous empty/full atom singular expansions, analogous to C019. There are two Fisher-divergent normal modes, logarithmically controlled mixing modes, and four bounded active directions. This could yield a full sixteen-real-dimensional interior neighborhood of every such generic (0,p,q,1) boundary point.

The strictness route to finish is as follows. C033's quantitative rank-one transport appears to provide a coupling positive on every supported bottom/top inclusion when both endpoint laws are everywhere positive; the exact hypotheses must be matched. If Lambda=0, every supported diamond logarithmic gap would vanish. On four sites this forces p_ij=c p_i p_j and p_ijk=c² p_i p_j p_k. Condition one site occupied. The remaining three-site law then has positive empty probability, vanishing full probability, and every pair probability equal to the product of its singleton odds. Its positive-semidefinite L-ensemble would have all off-diagonal entries zero but zero determinant, a contradiction. This suggests Lambda>0. The positive-coupling premise, the complete simultaneous normal form and uniform absorption still need a full written proof before the boundary-neighborhood conclusion is claimed.


Update: ROOT_FOUR_SITE_BOUNDARY.md completes this construction under the additional hypothesis that every two-row minor of the active plane is nonzero. It allows arbitrary relative scales of the two endpoint gaps. The lead without that extra hypothesis remains unresolved.

Further update: the four-site strict-Hall cycle argument in ROOT_FOUR_SITE_BOUNDARY.md removes the active-plane minor hypothesis entirely. The original nonzero endpoint-coordinate lead is now complete.

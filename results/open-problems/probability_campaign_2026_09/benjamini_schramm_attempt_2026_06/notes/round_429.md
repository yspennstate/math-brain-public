# Round 429 chain-antichain dichotomy for spread returns

Round 429 turns the laminarity lemma from Round 428 into a quantitative
deterministic dichotomy.

Suppose \(\gamma\) satisfies the spread-return event
\[
  \mathcal X^{\rm spr}_{j,K,p},
\]
so there are more than
\[
  N=\frac{\theta_{\lambda,\sigma,\beta}}{4K}L_H
\]
levels \(u\in A_{j,p}\) with at least one exterior return.  Choose one
exterior-return interval for each such level.  By Round 428 these intervals
form a laminar forest ordered by containment, and containment is compatible
with increasing return level.

Let \(a\ge2\) be an integer.  Then one of the following holds.

1. The chosen intervals contain a nested chain of length at least \(a\).
   Since nesting is radially oriented, this gives levels
   \[
     u_1<u_2<\cdots<u_a
   \]
   with the level-\(u_{k+1}\) return interval contained in the level-\(u_k\)
   return interval for each \(k\).

2. There is a pairwise disjoint subfamily of at least
   \[
     \left\lceil \frac{N}{a-1}\right\rceil
   \]
   exterior-return intervals.

Indeed, if the laminar forest has height at least \(a\), the first
alternative holds.  Otherwise every node has depth in
\(\{1,\ldots,a-1\}\).  One depth class contains at least \(N/(a-1)\) nodes,
and nodes at the same depth in a laminar forest are pairwise disjoint.

Thus, for every \(a\ge2\), the spread-return profile can be decomposed into a
nested-return-chain profile and a disjoint-return-excursion profile:
\[
  \mathcal X^{\rm spr}_{j,K,p}
  \subseteq
  \mathcal X^{\rm chain}_{j,K,a,p}
  \cup
  \mathcal X^{\rm disj}_{j,K,a,p}.
\]
The chain profile asks for a nested return chain of length \(a\); the disjoint
profile asks for at least \(N/(a-1)\) pairwise time-disjoint exterior-return
intervals in the slab.

This is a better target than raw level selection.  The chain alternative
should be attacked by a nested-annulus or repeated-backtracking estimate.  The
disjoint alternative is better suited to BK/Reimer-style or transfer-matrix
factorization, since the witness intervals are time-disjoint.  The next task
is to formulate property-restricted profiles for these two alternatives and
test whether either gives a density-rate \(a(\delta)\) beating the entropy
term from Round 427.

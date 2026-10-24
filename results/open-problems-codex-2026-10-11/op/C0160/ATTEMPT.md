# C0160 — corrected statement and counterexample

Date: 2026-10-11. Model: iid Bernoulli bond percolation on an infinite, connected, locally finite transitive graph. Parameter p ranges over [0,1]. Statements about N(p) mean almost-sure statements for each fixed deterministic parameter; they do not assert a common probability-one event for uncountably many parameters.

## What was asked, and what the source actually says

The supplied statement combines:

1. If p < q and P_p(N=1)=1, then P_q(N=1)=1.
2. With p_u = inf {p: P_p(N=1)=1}, that set is [p_u,1].

Assertion 1 is precisely the established uniqueness-monotonicity theorem (survey Theorem 5.6, printed p.307 / PDF p.19). Assertion 2 is stronger and false. Section 3, printed p.300 / PDF p.12, explicitly leaves the value at p_u separate. It also says the quasi-transitive case is covered and unimodularity is unnecessary. There is no open residual for nonunimodular transitive Bernoulli graphs in this statement.

No dependent-percolation problem is substituted. No continuity in a varying graph or family is asserted. The title's literal numerical monotonicity of N(p) is different from monotonicity of the uniqueness event.

## Complete deduction of the correct interval statement

Use as an established input Theorem 5.6, quoted verbatim in LITERATURE.md. Define

U = {p in [0,1]: P_p(N=1)=1}, a = inf U.

At p=1, every edge is open almost surely. Indeed, local finiteness and connectedness make the edge set countable, and each edge is open with probability one, so their countable intersection has probability one. The graph is connected and infinite, so N(1)=1. Thus 1 belongs to U. The set U is nonempty and bounded below by 0; a exists and lies in [0,1].

If x belongs to U and x <= y <= 1, then y belongs to U: for x=y this is immediate; for x<y it is Theorem 5.6. Hence U is upward closed within [0,1].

If p<a, then p is not in U, because a is a lower bound for U. If a<p<=1, the defining greatest-lower-bound property gives x in U with x<p. For otherwise every x in U would satisfy x>=p, making p a lower bound greater than a, a contradiction. Upward closure then gives p in U. Therefore

U = (a,1] union ({a} if a belongs to U, and the empty set otherwise).

Equivalently U is either (p_u,1] or [p_u,1]. If p_u=1, the fact 1 belongs to U forces U={1}, so only the closed alternative occurs. This proves the complete interval deduction, not inclusion of its infimum.

If there were p<q<r with uniqueness at p and r but infinitely many infinite clusters at q, Theorem 5.6 applied to p,q would force uniqueness at q, contradiction. Thus back-and-forth switching between 1 and infinity is impossible.

## Counterexample to the exact closed-interval assertion

Let T_6 be the regular tree of degree 7 (the survey uses T_d for degree d+1), and set G=T_6 x Z, with Cartesian adjacency: an edge changes one coordinate along an edge in that factor and leaves the other coordinate fixed.

This graph is infinite and connected: concatenate a path in the tree coordinate and a path in the integer coordinate between any two vertices. It is locally finite of degree 7+2=9. It is transitive: a tree automorphism mapping one tree vertex to another, together with an integer translation, gives a product graph automorphism mapping any prescribed vertex to any other. It meets all hypotheses of the asked question. Its percolation model is exactly iid bond percolation.

Established input A is survey Theorem 3.2 (printed p.299 / PDF p.11): since d=6, there are p_1,p_2 with p_c<p_1<=p_2<1, nonuniqueness throughout (p_c,p_1) and uniqueness throughout (p_2,1].

There are no infinite clusters below p_c by the definition of the critical threshold. Therefore no p<p_1 belongs to U, except possibly p=p_c. But uniqueness at p_c would, by Theorem 5.6, force uniqueness at any q in (p_c,p_1), contradicting input A. Hence p_c is not in U either. It follows that p_u>=p_1>p_c. Conversely put q=(p_2+1)/2. Since p_2<1, we have q-p_2=(1-p_2)/2>0 and 1-q=(1-p_2)/2>0. Thus q lies in (p_2,1), and input A guarantees q belongs to U. Since p_u is a lower bound of U, p_u<=q<1. Consequently p_c<p_u<1. No uniqueness at p_2 is assumed or needed.

Established input B is survey Theorem 9.2 (printed p.321 / PDF p.33): at p_u(T_d x Z) there is almost surely no unique infinite cluster, and when p_c<p_u there are infinitely many infinite clusters at p_u. Applying it to the verified graph above gives N(p_u)=infinity almost surely, in particular p_u is not in U.

Combine this with the complete interval deduction: U=(p_u,1], not [p_u,1]. This is a counterexample to assertion 2 even in the regime p_c<p_u<1, where N switches from infinity to 1. It does not contradict assertion 1. All inputs are published results with matching hypotheses, not conjectures or numerical evidence. This is a deduction from existing literature, not a claim of a new percolation theorem.

## Independent endpoint check on the square lattice

The survey, printed p.292 / PDF p.4, records theta_Z2(p_c)=0 (Harris and Kesten) and uniqueness for every supercritical parameter; Kesten gives p_c=1/2. Translation invariance makes theta_v(1/2)=0 for every vertex. Taking a countable union over vertices shows there is no infinite cluster at 1/2. Monotone coupling implies theta_v(p)=0 for p<1/2 too. For p>1/2 there is a unique infinite cluster almost surely. Thus U_Z2=(1/2,1] and p_u=1/2. This separately refutes universal inclusion of p_u, although here p_u=p_c and N(p_u)=0 rather than infinity. The product-graph counterexample above avoids any ambiguity about the nonuniqueness phase.

## Why ordinary cluster-count monotonicity is the wrong statement

On Z2, N(0)=0 and N(1)=1, so N cannot be nonincreasing throughout [0,1]. On T_6 x Z choose q in (p_c,p_1) and r in (p_2,1]; then q<r but N(q)=infinity>N(r)=1, so N cannot universally be nondecreasing either. The correct monotonic statement concerns membership in U (or the supercritical transition from infinity to 1), not numerical monotonicity of N over all parameters.

## Hostile-referee checks

* Endpoint confusion: infimum of an upper set need not belong to it. The argument explicitly treats that endpoint separately.
* Matching graph/model: product of a degree-7 regular tree and an infinite line is infinite, connected, degree 9, transitive; all cited inputs concern iid bond percolation.
* Tree indexing: d=6 means degree 7, not degree 6; it satisfies d>=6 in Theorem 3.2.
* Positivity at p_c: no assumption of critical nonpercolation on the product is used. Uniqueness at p_c is excluded by monotonicity and the known nonuniqueness interval.
* Critical N value: infinity at p_u follows from the explicit second sentence of Theorem 9.2 once p_c<p_u is established; it is not inferred merely from nonuniqueness.
* Second endpoint p_2: Theorem 3.2 provides uniqueness only on (p_2,1]. An earlier draft incorrectly used membership at p_2; the final proof uses the explicitly checked midpoint q=(p_2+1)/2 instead. The conclusion p_u<1 is unchanged and fully justified.
* Quasi-transitivity/nonunimodularity: verified directly from source p.300; older intake assertions of an open extension are not adopted.
* Coupling quantifiers: fixed-parameter theorem only; no unproved simultaneous-in-p strengthening.
* Literature novelty: no SOLVED_IN_LITERATURE label is assigned to the stronger false endpoint assertion on the strength of a related theorem. The final verdict is SOLVED, meaning a complete counterexample deduction for the supplied literal assertion, alongside identification of the already-established intended no-switching statement.
* Formal check: Endpoint.lean formalizes the interval deduction in an arbitrary linear order from an IsGLB and upward closure, and the incompatibility of a missing endpoint with a closed interval. Specializing its upper bound b to 1 and its order to the reals gives the order step used here. Only Mathlib.Order.Bounds.Basic is imported. Percolation inputs remain external established theorems. Lean completed successfully with exit code 0; see lean_check.txt. No sorry, native_decide, custom axioms or unchecked percolation assumptions occur in the formal file. The check proves only the stated order lemmas, not the published percolation theorems.

No simulation was needed: finite samples cannot certify infinite-cluster counts or uniqueness exactly at p_u. No remaining mathematical gap for the literal supplied statement; no classification of all possible uniqueness endpoints is claimed.

# Round 019 log

Date: 2026-06-08

## Focus

Audited the cluster-branching arguments and checked whether the new product
bound admits a susceptibility-only corollary.

## Branching-process wording

The one-step and two-step tree-fiber explorations do not need sibling events
to be independent.  The right formulation is:

- For each visited fiber, define its offspring count to be the number of
  forward fibers reached by the prescribed exploration rule.
- Offspring counts for distinct current individuals use disjoint forward
  subtrees and disjoint factor fibers, hence are independent and identically
  distributed.
- The resulting generation sizes are Galton-Watson processes.

Thus the proofs only need the mean offspring:
\[
  (d-1)\varphi_H(p)
\]
in the one-step product bound, and
\[
  (d-1)^2\Phi(p)
\]
in the two-step line-factor bound.

## Susceptibility-only shortcut fails

The cluster-branching proposition involves
\[
  \varphi_H(p)=\mathbb E_p[1-(1-p)^{|C_H(o)|}].
\]
It is tempting to lower-bound this using only the factor susceptibility
\[
  \chi_H(p)=\mathbb E_p|C_H(o)|.
\]
That is not valid in this generality.

For any fixed \(\mu>1\), let a positive integer-valued random variable \(M\)
have
\[
  \mathbb P(M=1)=1-\epsilon,\qquad
  \mathbb P(M=N)=\epsilon,\qquad
  \epsilon=\frac{\mu-1}{N-1}.
\]
Then \(\mathbb E M=\mu\), but as \(N\to\infty\),
\[
  \mathbb E[1-(1-p)^M]\to p.
\]
So the mean alone cannot force a useful lower bound above \(p\).  Any extension
of the product \(p_c\) upper bound to broad factor classes must use additional
cluster-tail information, an explicit cluster-size law, or a second-moment type
input.

## Status

The manuscript now states this guardrail explicitly after the
cluster-branching proposition.  The next productive direction is either a
self-avoidance-aware SAW operator bound for \(T_3\square\mathbb Z\), or a
factor-cluster tail estimate strong enough to lower-bound \(\varphi_H(p)\) in
new product families.

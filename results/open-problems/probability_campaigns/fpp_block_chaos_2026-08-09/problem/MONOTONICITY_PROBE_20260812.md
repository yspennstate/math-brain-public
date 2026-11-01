# Variance monotonicity: the covariance identity, and why FKG cannot close it
# 2026-08-12 pass 93. By-hand half-page, symmetric to the doubling
# probe (DOUBLING_IS_NOT_A_SIDE_DOOR_20260812.md). STATUS: obstruction named, problem open.
# Nothing moves chi.

The sub-problem (checklist closing verdict, item (i)): Var(X_{n+1}) >= Var(X_n),
unconditionally, planar FPP. Fire-82 literature pass: open (even the MEAN's version is open;
proved only under S_+ <= 2 S_- on the weight support, arXiv 1202.2665).

## The identity that frames it

Write Delta := X_{n+1} - X_n. Then
    Var(X_{n+1}) - Var(X_n) = Cov(X_{n+1} + X_n, Delta),
an exact one-line identity (difference of squares in covariance form). So monotonicity at
step n is EXACTLY a signed-covariance statement: the increment must not anti-correlate too
strongly with the running level. Delta itself is bounded (|v(n+1) - v(n)| = O(1) lattice
steps, so -T(v(n), v(n+1)) <= Delta <= T(v(n), v(n+1)) <= C by the triangle inequality and
bounded weights) - boundedness is not the issue; the SIGN structure is.

## Why positive association (FKG/Harris) cannot close it

X_n and X_{n+1} are both increasing functions of the edge weights, so FKG gives
Cov(X_n, X_{n+1}) >= 0 - too weak: the identity needs Cov against the DIFFERENCE, and Delta
is NOT increasing in the environment. Concrete gadget: two disjoint routes to v(n), one of
which extends cheaply to v(n+1). Raise a weight on the geodesic serving X_n alone: X_n rises
strictly while X_{n+1} (already routed through the other path) is unchanged - Delta strictly
FALLS as a weight rises. An environment-monotone functional it is not, so Harris-type
positive association is structurally inapplicable to the pair (X_{n+1} + X_n, Delta).
That is the precise obstruction; any proof must control the geometry of WHERE the two
geodesics disagree, not just monotonicity of the endpoints.

## Where that leaves the pair of sub-problems

- DOUBLING: wall-equivalent (fire 89) - a reformulation of the main obstruction.
- MONOTONICITY: genuinely separate, and now framed - it is the statement that the
  one-step increment does not anti-correlate with the level by more than Var(Delta)/2.
  The mean's conditional proof (S_+ <= 2 S_-) works precisely because that support condition
  kills the rerouting gadget above (no route can be cheap enough to undercut); the same
  mechanism is the natural first attack on the variance version, and it would be a
  CONDITIONAL result of the same shape, not the unconditional statement.
Neither is consumable by any bootstrap today; this file and the doubling file are the
citations for that refusal.

# R13 idea — tie-broken shallow refinements of the exact 11-cylinder cover

Target: move the permitted explicit finite obstruction at n=86 without retuning the already-nearly-saturated weights on the previous support family.

Methods selected from the preceding R13 report: **#5 ADD A PARAMETER AND DIFFERENTIATE IN IT, #13 FIND WHAT ONLY INCREASES, #30 DO ONE SCALE / ONE DIRECTION AT A TIME.**

1. **#5 — parameterize the refinement topology, not the row magnitudes.** Keep the exact eleven-cylinder projective cover and the same leaf-count vector `(11,11,6,5,11,5,5,5,5,11,11)`, but regard the tie-breaking order among currently shallowest leaves as a discrete parameter. Every split preserves projective coverage and adds one fresh column, so all such forests still give 86 rows and 86 columns.
2. **#13 — use the support-load value as a monotone scout objective.** For a fixed support family, let `t(S)` be the minimum possible maximum column squared load under positive row masses summing to one. A candidate obstruction has scale `q=1/sqrt(t(S))`. During topology search, retain a new split-order only when the numerically optimized scout value of `q` strictly increases. Numerical optimization is discovery only; it is not theorem evidence.
3. **#30 — localize the combinatorial change.** Preserve breadth-first depth minimization and change only the tie-breaking among leaves of equal minimum depth. This keeps the depth multiset `{2:17,3:39,4:30}` and support-size multiset `{7:42,8:44}` fixed, so any improvement comes from incidence structure rather than from adding deeper supports or changing the leaf budget.

The search found a tie-broken shallow forest whose numerical support-load optimum is about `q=2.26473`, versus the preceding certified `2.264655`. The next step is therefore justified: discard the numerical optimizer, round to an explicit positive integer weight vector, and build one exact `Fraction` checker for the resulting support family. The finite theorem claim will be made only if that exact checker proves pairwise projective incompatibility, Kraft mass one, and every scaled column squared norm strictly below one.

STATE: DONE
NEXT: Seek a comparison within the actual BP-generated posterior class for q=5 versus q=6 that also controls the full uniform-reset mixture.
VERDICT: PARTIAL

2026-10-12: Original bounded attempt verified the source and literature, proved depth-one TV monotonicity and depth-two binary-tree TV monotonicity, and recorded the infinite-depth nondivisible-alphabet gap. The earlier results remain in ATTEMPT.md and LITERATURE.md.
2026-10-12: Reopened at the user's request. Reread the remaining gap and asked the math store about the gap, posterior experiments, Blackwell comparison and Strassen. Its ordinary stochastic-order card did not supply the required convex-order theorem; the finite criterion was proved independently.
2026-10-12: Wrote two previously untried approaches in SECOND_ATTEMPT.md. Pursued binary Blackwell comparison; population dynamics/certification was not pursued in this turn.
2026-10-12: Proved a stronger finite-tree special case: binary Blackwell monotonicity across alphabets for any finite number of independent two-leaf branches, including fixed heterogeneous per-branch parameters. Full proof includes the finite convex-order/garbling criterion and exact derivative signs.
2026-10-12: Found and analytically certified two obstructions to generic proof methods: arbitrary rooted-partition coloring can fail Blackwell monotonicity (-167/5032800), and symmetric three-input pairwise binary Blackwell order can fail after a common positive Potts edge (-19/750). Neither is a counterexample to F0118 or to its source tree model.
2026-10-12: Independent exact validation checked 63 branch laws, 54 branch comparisons, one heterogeneous three-branch comparison and both auxiliary witnesses. All 45 new finite true-tree Blackwell comparisons passed, including q=5 to 6 at depth three with lambda=13/20 and 7/10 below KS.
2026-10-12: A bounded TV-only search of 40,000 rational rooted-partition priors found no TV reversal. This is a negative finite search, not a theorem.
2026-10-12: BlackwellAlgebra.lean passed the Lean kernel (exit 0), verifying four new polynomial certificates with no sorry or native_decide. The full probability arguments and original conjecture are not formalized.
2026-10-12: Completed hostile-referee audit and stopped with the precise gap in SECOND_ATTEMPT.md and ATTEMPT.md. Full F0118 remains unproved, no source-model counterexample obtained. DONE denotes completion of the requested second attempt; verdict remains PARTIAL.

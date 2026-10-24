STATE: DONE
NEXT: Future work: prove convergence of the mean and vanishing variance of the explicit predictable drift A_n in (A12).
VERDICT: PARTIAL

2026-10-12: Fetched and verified Aldous arXiv:1912.13175v2, shortest-path/no-return definitions, exact three models and first-order questions.
2026-10-12: Searched arXiv, Crossref, Semantic Scholar, GitHub, and OpenAlex; OpenAlex search/citation requests were rate-limited. No exact published solution verified; the 2023 citing paper remains a full-text-unchecked lead.
2026-10-12: Proved lower probability and expectation floors 5/8 for Euclidean area-n squares, 1/3 for Exp(1) grids, and 5/4 for exponential mean-field distances, uniformly over starts. Also proved a finite-size mean-field lower-deviation bound and a local-score L1 LLN.
2026-10-12: Proved divergence for a positive-iid Pareto grid and the necessary condition E[min(W_1,W_2,W_3,W_4)]<infinity for any finite grid constant. This refutes an unrestricted grid reading, not the intended light-tailed programme.
2026-10-12: Numerical checks passed (1,755 metric starts; 360 resampling cases; Euclidean influence checks; finite model and clipped-tail samples). Final Lean finite algebraic certificate exited 0 after import corrections. Nine claims recorded with proofs and precise gaps.
2026-10-12: Closed partial attempt. Full NUV convergence and constant identification in the Euclidean, light-tailed grid and exponential mean-field models remain unproved.

2026-10-12: Reopened at user request for a second serious attempt focused on the NUV ordering gap.
2026-10-12: Second attempt: exact mean-field Markov transition and threshold-cone formula proved; long-step expectation bound and predictable-drift LLN equivalence derived, with empirical-state convergence still missing.
2026-10-12: Second attempt completed: two new approaches recorded, exact deferred-decisions approach pursued. Proved threshold-cone state representation, long-step expectation control, all fixed moment bounds and O(n^(-1/2)) L2 reduction to the random drift A_n.
2026-10-12: Checked 6000 transitions, 1140 cone/reconstruction states, 300 covering cases and independent hazard quadrature. ThresholdUpdate.lean exited 0 after correcting a reserved variable name. Nineteen total claims now recorded.
2026-10-12: Closed continuation with VERDICT PARTIAL. E A_n convergence and Var(A_n)->0 remain unproved; no intended model constant has been identified.

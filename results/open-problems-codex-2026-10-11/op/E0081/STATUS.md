STATE: DONE
NEXT: Determine the exact first-passage leading constant or apply the uniform-overlap lower-tail criterion to another specified natural family.
VERDICT: PARTIAL

2026-10-12: Verified source arXiv:1411.0041v3, Question 1.7 p.5 and its symmetric-walk hypotheses. Later arXiv papers inspected; no full-scope resolving theorem verified. OpenAlex/Semantic Scholar/GitHub rate limits leave citation coverage incomplete.
2026-10-12: Proved universal bounds and E T_A=Theta(n/q) for an explicit enlarged-word density q. Constructed exactly equal-cardinality families with Theta(n) versus Theta(n^2) mean completion times.
2026-10-12: Proved sharp prescribed-cardinality extrema: min=Theta(n+2^n/m), max=Theta((1+log_2 m)2^n/m), uniformly for 1<=m<=2^n. Full proofs and limitations in ATTEMPT.md.
2026-10-12: Hostile-referee checks passed: 398 finite collections, 357 independent matching-matrix comparisons, 62 prescribed-cardinality constructions, exhaustive run/history checks, and Lean kernel verification of the run Bellman algebra (exit 0). Earlier ledger counting/race-identity errors were identified and excluded.
2026-10-12: Bounded attempt complete. Remaining gap: estimates for an individually specified natural family, notably the source's first-passage exponent gap, are not supplied by the extremal results. No full-scope solution or literature solution claimed.

2026-10-12 second attempt: Proved first-passage upper bound O(n log n), improving the source displayed O(n^(5/4)) bound and fixing the polynomial exponent at 1. Pursuing the logarithmic loss.
2026-10-12 second attempt: Wrote a candidate complete proof that E T(FP_(lambda,n))=Theta_lambda(n log n), using first-hit domination and logarithmic variance control. Audit pending.

2026-10-12 second attempt completed: Recorded two new approaches (ballot/overlap concentration and descending-ladder renewal intersections), and pursued the former. Proved E T(FP_(lambda,n))=Theta_lambda(n log n) for every fixed lambda<0, closing the source's first-passage order gap. Exact leading constant remains unproved.
2026-10-12 second attempt audit: First-hit domination plus an exact overlap identity, unconditioned logarithmic mean/variance estimates, and bounded prefix likelihood ratios give the matching lower bound. 1013 overlap checks, 20 exact first-hit laws, 512 smoothing checks, 120 covariance checks, 146 prefix likelihood checks, exact and numeric moment recursions, and Lean kernel checks passed. Full proof: SECOND_ATTEMPT.md.
2026-10-12 final scope: General E0081 remains PARTIAL because arbitrary natural scale-indexed collections are not classified. The first-passage order gap previously listed in ATTEMPT.md is now closed. New general result: a uniform-overlap lower-tail criterion controlling the first-hit expected overlap without assuming uniform race probabilities. All results remain within E0081; no literature-solution or novelty claim made.

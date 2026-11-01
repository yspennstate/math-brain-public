STATE: DONE
NEXT: Establish uniform continuity of Poisson optimal values at general nonzero empirical states, then prove convergence and determine the common limit.
2026-10-11: Reopened at the user's request. Two new approaches recorded in SECOND_ATTEMPT.md; pursuing causal rare-offer simulation plus a uniform-cut repair lemma for one-sided model transfer.
VERDICT: PARTIAL

2026-10-11 FINAL: Both comparisons are proved, giving |P_n-C_n|=O(n^(-1/100)); full proofs in SECOND_ATTEMPT.md and REVERSE_TRANSFER.md. The common limsup is <=1.9440377683016505. All finite/simulator checks and supplementary Lean algebra passed. Limit existence and its value remain unresolved.

2026-10-11: A new reverse-transfer construction is under review in REVERSE_TRANSFER.md. It routes actual Poisson cheap offers to virtual combinatorial edges by reassigning equal-size bundles and labels within bundles. Uniform graph upper estimates and stopped phantom counts appear to give P_n <= C_n + O(n^(-1/100)); this is not yet recorded as a proved claim.

2026-10-11: Second attempt proved an exact causal cheap-offer Poisson simulator, an all-cuts remaining-graph estimate and a stopped repair potential. Their combination gives C_n <= P_n + O(n^(-1/6)) and transfers limsup <=1.9440377683016505 to the combinatorial model. Full proofs saved in SECOND_ATTEMPT.md; exact and seeded checks passed. Reverse transfer, convergence and limiting value remain unresolved.

2026-10-11: Started source verification and read-only brain recall.
2026-10-11: Verified primary models and conjecture. Proved finite admissible-root uniqueness and reciprocal-potential Poisson bound P_n <= (8/3)(1-1/n^2). Certified exact dyadic values for 43,818 states through n=32. Full limit problem remains unresolved.
2026-10-11: Strengthened the Poisson upper bound to P_n <= 2+2/n-4/n^2 by an explicit sum-of-squares verification remainder. Proved zero-state empirical continuity as a special case of the source's claim.
2026-10-11: Exploited initial-time verification slack to prove limsup P_n <= (33-18*exp(1/3))/4 < 2; full finite-time proof saved, awaiting further referee checks.
2026-10-11: Sharpened singleton-count control via individual hazards, yielding limsup P_n <=39/20=1.95 and an explicit finite-n upper bound.
2026-10-11: AlgebraCheck.lean passed with exit code 0, no proof holes or native decision evaluation. Submitted the second algebra check sequentially.
2026-10-11: A finite pure-death comparison improves the Poisson limsup bound to (63-3*exp(-4/3))/32; complete coupling and expectation proof saved.
2026-10-11: Corrected SupersolutionCheck.lean passed with exit code 0, only harmless linter warnings. Closed this attempt as PARTIAL: proved finite uniqueness, zero-state continuity, explicit Poisson bounds including limsup <=1.9440377683..., and exact finite enclosures. The target limit existence, its value, and model equivalence remain unresolved. No literature resolution found; API coverage gaps are recorded.

2026-10-11: Closed the second serious attempt as DONE / PARTIAL. Proved both model comparisons, hence |P_n-C_n|=O(n^(-1/100)), and transferred limsup <=(63-3 exp(-4/3))/32 to the combinatorial model. Finite arithmetic, exhaustive bundle reassignments and simulator checks passed; RepairCheck.lean passed with exit code zero. Convergence and the common limiting optimal cost remain unresolved.

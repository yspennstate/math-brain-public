Open problem D0043. Source: B. Virag, "Operator limits of random matrices" (ICM 2014 proceedings; arXiv:1804.06953),
Conjecture 5 (Exotic edge operators), PDF p. 14: when the equilibrium density of a one-cut beta-ensemble vanishes at the edge like
x^{2k+1/2} rather than x^{1/2}, the tridiagonal matrices T_n (the tridiagonal models for general potentials, as in
Krishnapur-Rider-Virag) should converge, after scaling, to S_{beta,k} = -d^2/dt^2 + t^{1/(2k+1)} + (2/sqrt beta) t^{-k/(2k+1)} b'_t,
with b' white noise. For beta = 2 the eigenvalue limits are known by Riemann-Hilbert methods (Claeys-Its-Krasovsky, Painleve I
hierarchy, higher-order Tracy-Widom). Read the source for the exact wording, the meaning of T_n and of the convergence.

Prior internal work to reuse (internal only, never cite publicly): our runs D0040 (nested models, Question 2 of the same paper)
and D0041 (spiked edges); their folders are not available here, so re-derive what you need.

Do this, in order, saving as you go:
1. Literature first. Get arXiv:1804.06953 into sources/ (plain text only). State Conjecture 5 exactly. Search:
   Krishnapur-Rider-Virag ("Universality of the stochastic Airy operator", CPAM 2016), Ramirez-Rider-Virag, Bloemendal-Virag,
   Claeys-Its-Krasovsky (higher order analogues of Tracy-Widom), Claeys-Kuijlaars, Bleher-Its (double scaling), Dumaz-Labbe,
   Gorin-Kleptsyn, Lambert, Li-Valko, Edelman-Sutton, Forrester, and 2014-2026 work on "critical edge", "higher order edge",
   "stochastic operator", "beta ensemble critical point". If a printed theorem proves Conjecture 5 for some k >= 1 and all beta
   (or for beta = 2 at the operator level), give the theorem and page and stop with RESOLVED_IN_LITERATURE, stating for which k
   and beta.
2. Understand: write the KRV mechanism for k = 0 (tridiagonal coefficients for potential V, the local behaviour near the edge,
   the convergence criterion of KRV Theorem 1 or Ramirez-Rider-Virag), and compute what changes when the density vanishes like
   x^{2k+1/2}: the scaling exponents, the drift t^{1/(2k+1)} and the noise weight t^{-k/(2k+1)}. Check that the conjectured
   operator is the formal limit (derive the exponents).
3. Prove what you can, with complete proofs: (a) S_{beta,k} is a well-defined self-adjoint operator bounded below with discrete
   spectrum (Riccati or form methods as in Ramirez-Rider-Virag); (b) convergence for a tractable class (for example a tridiagonal
   model whose coefficients have the exact critical profile with independent chi noise, in the KRV operator-convergence
   framework); or (c) a corrected conjecture if the noise exponent or the drift is wrong.
4. Compute (evidence only): sample T_n for a quartic potential at its critical point (k = 1) and for an artificial critical
   profile, n up to 10^4-10^5 (sparse eigensolvers), compare the scaled top eigenvalues with a discretisation of S_{beta,k}, for
   beta in {1, 2, 4}, and for beta = 2 with the higher-order Tracy-Widom law if computable.
Write REPORT.md. Its first line is exactly one of PROVED, COUNTEREXAMPLE, PARTIAL, NO_PROGRESS, RESOLVED_IN_LITERATURE.
Then the statement, the proof, what was checked and how, and the literature result with exact theorem numbers and pages.
Keep LOG.md as you go. Code in code/, data in data/. Source texts may go in sources/ as plain text only; no PDFs kept, no
page images or scans of any paper or book anywhere in this folder. Work only in this directory. At most 4 threads, under
4 GB, nice 10. No publication anywhere, no pushes.

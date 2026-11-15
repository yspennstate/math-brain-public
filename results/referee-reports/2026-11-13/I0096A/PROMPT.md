Open problem I0096. Source: A. S. Bandeira et al., "Randomstrasse101: Open Problems of 2025", arXiv:2603.29571v1, Entry 10
"Injectivity and Stability of Phase Retrieval", Definition 10.1 and Conjecture 20 (a conjecture of R. Balan and Y. Wang, 2013).
For A in R^{N x M}, omega(A) = min over S subset [N] with rank(A_{S^c}) < M of sigma_M(A_S). Conjecture 20: there are universal
constants C > 0 and 0 < beta < 1 such that for every M > 1 and every A in R^{(2M-1) x M} in which any M rows span R^M,
omega(A) <= C max_k ||A_k|| beta^M. (For such A, omega(A) is the minimum over M-row submatrices of the least singular value.)
Open Problem 21 there (the Gaussian value) is answered in print: omega(A) = 4^{-M+o_P(M)} (arXiv:2607.06249, the author) with
polynomial factors in arXiv:2609.28198 (C. E. Haggblom), and the subgaussian extension arXiv:2608.07410. Those are random-matrix
results; the question here is the worst case over all full-spark A.

Do this, in order, saving as you go:
1. Literature first. Get arXiv:2603.29571 (Entry 10), Balan-Wang "Invertibility and robustness of phaseless reconstruction"
   (ACHA 2015, arXiv:1308.4718) and every paper citing it on the lower Lipschitz bound of x -> |Ax| at N = 2M-1, the three
   preprints above, and any 2025-2026 work on deterministic bounds for min_S sigma_min(A_S) (restricted invertibility,
   full-spark frames, Vandermonde/harmonic frames, Plucker relations). If Conjecture 20 is proved or refuted in print, report
   RESOLVED_IN_LITERATURE with exact theorem numbers and pages.
2. Otherwise attack it. Useful facts to check and use: sigma_min(A_S) <= dist(a_k, span{a_j : j in S, j != k}) for k in S;
   Cauchy-Binet gives sum_S det(A_S)^2 = det(A^T A) <= ((2M-1)/M)^M max||A_k||^{2M} against binom(2M-1, M) ~ 4^M terms, so
   some M x M minor has |det| <= c^M with c < 1; the gap is to pass from a small determinant to a small least singular value
   for one subset. Try: choosing S and k jointly by averaging dist(a_k, H_T)^2 over (M-1)-subsets T with a weight
   (volume-weighted / determinantal sampling of T, so that E dist^2 is a ratio of Cauchy-Binet sums); induction on M by
   projecting along one row; Plucker relations among minors. Also look for counterexamples: a family of full-spark
   (2M-1) x M matrices with omega(A) >= exp(-o(M)) max||A_k||; test candidates numerically (exact enumeration of all
   binom(2M-1, M) minors for M up to about 12, optimisation over A to maximise omega(A) for small M, and report the best
   value found per M and its growth rate). A full proof (some explicit beta) is PROVED; a counterexample family is
   COUNTEREXAMPLE; a proof of omega(A) <= C beta^M under one extra natural hypothesis (for example a bound on the condition
   number of A, or unit-norm tight frames) not already in print, or a proof of a weaker bound such as C/M^a, is PARTIAL.
3. Numerics are evidence only; no simulation stands in for a proof.
Write REPORT.md. Its first line is exactly one of PROVED, COUNTEREXAMPLE, PARTIAL, NO_PROGRESS, RESOLVED_IN_LITERATURE.
Then the statement, the proof, what was checked and how, and the literature results with exact theorem numbers and pages.
Keep LOG.md as you go. Code in code/, data in data/. Source texts may go in sources/ as plain text only; no PDFs kept, no
page images or scans of any paper or book anywhere in this folder. Work only in this directory. At most 4 threads, under
4 GB, nice 10. No publication anywhere, no pushes.

Open problem C0083. Source: M. Heydenreich and R. van der Hofstad, "Progress in High-Dimensional Percolation and Random
Graphs" (CRM Short Courses, Springer 2017), Open Problem 15.10, p. 233: show that the critical value of bond percolation on
the Hamming graph K_n^d (with the book's lambda-dependent definition of p_c) satisfies
p_c(K_n^d; lambda) = sum_{i=1}^{d/3} a_i(d) n^{-i} + O(n^{-1-d/3}), with a_1(d) = 1/d; the second-order term was identified by
Federico, van der Hofstad, den Hollander and Hulshof. Read the book's statement and its definitions exactly (text only; the
book is copyrighted: do NOT download or rasterise its pages, use the arXiv lecture-notes version arXiv:1510.03221 or quote).

Do this, in order, saving as you go:
1. Literature first. Read arXiv:1510.03221 around the open problem. Then find and read Federico-van der Hofstad-den
   Hollander-Hulshof, "Expansion of percolation critical points for Hamming graphs" (arXiv:1701.02099, Combin. Probab.
   Comput.), and their related papers (finite-size scaling on Hamming graphs, arXiv:1512.00807?), van der Hofstad-Luczak,
   Borgs-Chayes-van der Hofstad-Slade-Spencer, Slade's expansion of p_c for the hypercube (van der Hofstad-Slade 2005/2006,
   "Expansion in n^-1 for percolation critical values on the n-cube and Z^n"), and any 2017-2026 work citing them. Decide
   precisely what is proved in print: to which order the expansion is established, whether the coefficients are shown to be
   rational functions of d, whether the error term matches O(n^{-1-d/3}). If the full statement is in print, give the exact
   reference and theorem and stop with REPORT.md first line RESOLVED_IN_LITERATURE. If only part is in print, say exactly
   which part and continue.
2. Attack the remaining gap. The hypercube argument (lace expansion, the expansion of Pi in powers of n^-1, the error
   controlled by the number of non-backtracking cycles) is the model; identify which step fails for K_n^d, what the d/3
   cut-off encodes (short cycles of length 3 in K_n), and whether the gap can be closed for small d (d = 3, 4, 5, 6) or for
   the next coefficient a_3(d). Prove what you can rigorously.
3. Compute. Exact or numerical checks for small n and d: e.g. compute the expected cluster size / susceptibility on K_n^d by
   exact enumeration or Monte Carlo (CPU, at most 4 threads), locate the book's p_c(lambda) for n up to what is feasible, and
   fit against the conjectured expansion with the known a_1, a_2. Use this only as a check, never as a proof.
Write REPORT.md. Its first line is exactly one of PROVED, COUNTEREXAMPLE, PARTIAL, NO_PROGRESS, RESOLVED_IN_LITERATURE.
Then the statement, the proof, what was checked and how, and the literature result with exact theorem numbers. Keep LOG.md
as you go. Code in code/, data in data/. No page images or scans of any paper or book anywhere in this folder. Work only in
this directory. At most 4 threads, under 4 GB, nice 10. No publication anywhere, no pushes.

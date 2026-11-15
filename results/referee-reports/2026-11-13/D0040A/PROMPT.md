Open problem D0040. Source: B. Virag, "Operator limits of random matrices" (ICM 2014 proceedings; find it by author and title),
Question 2 (Nested models), PDF p. 6: the top minors of the Dumitriu-Edelman tridiagonal beta-Hermite model give a coupling of
beta-ensembles of all sizes (a nested family whose eigenvalues interlace). Can any other Dyson beta-ensembles (beta-Laguerre,
beta-Jacobi, circular beta, general one-cut potentials) be coupled this way? What about other natural random matrix models?
Read the source for the exact wording and the precise meaning of "coupled this way" (minors of one random tridiagonal or
CMV/Hessenberg matrix; consistency of the joint eigenvalue laws across n; interlacing).

Do this, in order, saving as you go:
1. Literature first. Get the source into sources/ (plain text only). Search: Dumitriu-Edelman (matrix models), Killip-Nenciu
   (CMV models for circular and Jacobi beta-ensembles), Edelman-Sutton, Forrester (beta-corners, Dixon-Anderson),
   Gorin-Shkolnikov (multilevel Dyson Brownian motions), Neretin (Rayleigh triangles), Borodin-Gorin (general beta Jacobi
   corners process), Gorin-Marcus, Assiotis, Sun (matrix models for multilevel Heckman-Opdam), and 2014-2026 work. Determine
   which ensembles are known to have nested (corners / minor-process) couplings and whether those arise as minors of a single
   random tridiagonal or banded matrix. If the question is answered in print for the natural classes, give theorems and pages
   and stop with RESOLVED_IN_LITERATURE.
2. Understand the gap: write the beta-Hermite corners structure (Dixon-Anderson conditional law of interlacing eigenvalues)
   and identify exactly what property of the Gaussian weight makes top-minor consistency hold.
3. Prove what you can, with complete proofs: a nested tridiagonal coupling for beta-Laguerre (for instance via a bidiagonal
   B with B B^T and its top-left minors, checking whether the minors are beta-Laguerre and with which parameters), for
   beta-Jacobi, or a no-go theorem: for which potentials V can all top-left minors of a random Jacobi matrix with independent
   entries be beta-ensembles with potential V (show only the Gaussian works, or classify).
4. Compute (evidence only): Monte Carlo of minors of candidate tridiagonal models, testing eigenvalue marginals against the
   target densities for small n and several beta.
Write REPORT.md. Its first line is exactly one of PROVED, COUNTEREXAMPLE, PARTIAL, NO_PROGRESS, RESOLVED_IN_LITERATURE.
Then the statement, the proof, what was checked and how, and the literature result with exact theorem numbers and pages.
Keep LOG.md as you go. Code in code/, data in data/. Source texts may go in sources/ as plain text only; no PDFs kept, no
page images or scans of any paper or book anywhere in this folder. Work only in this directory. At most 4 threads, under
4 GB, nice 10. No publication anywhere, no pushes.

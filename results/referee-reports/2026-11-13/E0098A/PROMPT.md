Open problem E0098. Source: a 2016 survey on eigenvectors of random matrices (source id eigenvectors_survey_2016; most likely
S. O'Rourke, V. Vu, K. Wang, "Eigenvectors of random matrices: a survey", J. Combin. Theory A 2016, arXiv:1601.03678), the open
question following Corollary 4.8, PDF p. 13: is the limiting distribution of ||v_j(W)||_min, the smallest coordinate in absolute
value of a unit eigenvector of a Wigner matrix W, universal, or does it depend on the atom distributions xi (off-diagonal) and
zeta (diagonal)? Corollary 4.8 gives ||v_i(W)||_min of order n^{-3/2} (log n)^{-c} with high probability. Read the source for the
exact wording (which eigenvectors: bulk and edge, fixed index j or all, normalisation).

Do this, in order, saving as you go:
1. Literature first. Get the source into sources/ (plain text only) and state the question exactly. Search: Bourgade-Yau
   ("The eigenvector moment flow and local quantum unique ergodicity", CMP 2017: asymptotic normality of finitely many coordinates,
   and of growing families), Benigni ("Eigenvectors distribution and quantum unique ergodicity for deformed Wigner matrices";
   "Fermionic eigenvector moment flow", PTRF 2021), Benigni-Lopatto ("Optimal delocalization of generalized Wigner matrices",
   Adv. Math. 2022; "Fluctuations in local quantum unique ergodicity for generalized Wigner matrices", CMP 2022), Marcinek-Yau,
   Cipolloni-Erdos-Schroder (eigenstate thermalisation, Gaussian fluctuations of eigenvector overlaps), Knowles-Yin, Tao-Vu
   ("Random matrices: universal properties of eigenvectors"), Rudelson-Vershynin ("No-gaps delocalization"), Aggarwal-Lopatto-
   Marcinek, and 2016-2026 work on "smallest eigenvector coordinate", "minimum of eigenvector entries", "extreme values of
   eigenvector coordinates". If a printed theorem gives the limit law of n^{3/2} min_k |v_j(k)| (or of the whole extremal process
   of sqrt(n)|v_j(k)| near zero) and shows universality (or dependence on the atoms), give the theorem and page and stop with
   RESOLVED_IN_LITERATURE, stating the hypotheses (moment conditions, bulk/edge, generalized Wigner).
2. Understand: if the n coordinates of sqrt(n) v_j were i.i.d. standard Gaussian, n^{3/2} min |v_j(k)| -> Exponential with rate
   sqrt(2/pi) (compute it). Universality of this limit needs joint Gaussianity of a growing (order n) number of coordinates, or at
   least a Poisson approximation for the number of coordinates below t n^{-3/2}. Say which printed results give that.
3. Prove what you can, with complete proofs: for example, derive the exponential limit from a printed joint-normality theorem for
   up to n^{1-eps} coordinates plus a symmetrization/Poisson argument, or show dependence on the atoms for a specific discrete
   case (e.g. Bernoulli atoms where an eigenvector coordinate can vanish with probability not o(1)? check small cases and the
   known results on exact zeros).
4. Compute (evidence only): sample Wigner matrices (Gaussian, Rademacher, sparse-ish Bernoulli) with n up to a few thousand and
   compare the law of n^{3/2} min_k |v_j(k)| for bulk and edge j with the exponential prediction.
Write REPORT.md. Its first line is exactly one of PROVED, COUNTEREXAMPLE, PARTIAL, NO_PROGRESS, RESOLVED_IN_LITERATURE.
Then the statement, the proof, what was checked and how, and the literature result with exact theorem numbers and pages.
Keep LOG.md as you go. Code in code/, data in data/. Source texts may go in sources/ as plain text only; no PDFs kept, no
page images or scans of any paper or book anywhere in this folder. Work only in this directory. At most 4 threads, under
4 GB, nice 10. No publication anywhere, no pushes.

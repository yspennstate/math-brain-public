Open problem C0002. Source: M. Biskup, "Extrema of the two-dimensional discrete Gaussian free field", in Random Graphs, Phase
Transitions, and the Gaussian Free Field (PIMS-CRM Summer School 2017), Springer Proc. Math. Stat. 304 (2020), 163-407,
arXiv:1712.09972, Problem 16.2 (p. 220 of the volume; find the matching page in the arXiv version): describe the rate of
convergence in Corollary 2.9 (the size of the intermediate level set), identify the limit law of the fluctuations of the level
set around its limit, and study deviations whose probability tends to zero as N -> infinity. (Read the source for the exact
setting: the DGFF in V_N with zero boundary, the level a_N = 2 sqrt(g) lambda log N with lambda in (0,1), the level set size
|{x: h_x >= a_N}| normalised by K_N = N^2 / sqrt(log N) e^{-a_N^2/(2 g log N)}, and the limit in Corollary 2.9, which is
expressed through the Liouville quantum gravity measure Z_lambda.)

Do this, in order, saving as you go:
1. Literature first. Get arXiv:1712.09972 into sources/ (plain text only); read Section 2 (Corollary 2.9 and Theorem 2.7),
   the intermediate level set chapters, and Problem 16.2 exactly. Search 2018-2026 work for answers to any of the three parts:
   Biskup-Louidor "Full extremal process, cluster law and freezing for the two-dimensional discrete Gaussian free field" and
   "On intermediate level sets of two-dimensional discrete Gaussian free field" (AIHP 2019); Junnila-Saksman-Webb on rate of
   convergence of imaginary/complex GMC; Lacoin-Rhodes-Vargas; Garban-Holden-Sepulveda-Sun; Berestycki-Webb-Wong; Lambert;
   Cerf-Dembo; Kim-Lee "Large deviations for intermediate level sets"; Bolthausen-Deuschel-Giacomin; Daviaud; Aru-Lupu-Sepulveda;
   "fluctuations of the level set size" and "moderate deviations" of the DGFF. If any part is answered in print, give exact
   references and theorems for that part.
2. Pick the most tractable part that is still open after step 1 and attack it with full proofs. Candidates: (a) a quantitative
   rate (for instance in a Wasserstein or Kolmogorov distance, or a bound on the second moment of the difference) for a fixed
   lambda in a sub-range such as (0, 1/sqrt2) where L^2 methods work; (b) the order and limit law of
   |level set| / K_N - Z_lambda(D) for small lambda (is it Gaussian after the right normalisation, and what is the order:
   a power of log N?); (c) the speed and rate function for large deviations of |level set| / K_N in some direction (upper
   deviations via the second moment, lower deviations via the entropic repulsion cost).
3. Compute (as evidence and to calibrate conjectures). Sample the DGFF on boxes up to the largest N that fits in 4 GB
   (sparse Cholesky or FFT-based sampling of the Dirichlet GFF), estimate mean, variance and law of the normalised level set
   size for a few lambda, and fit the convergence rate.
Write REPORT.md. Its first line is exactly one of PROVED, COUNTEREXAMPLE, PARTIAL, NO_PROGRESS, RESOLVED_IN_LITERATURE
(RESOLVED_IN_LITERATURE only if all three parts are answered in print). Then the statement, the proof, what was checked and
how, and the literature result with exact theorem numbers and pages. Keep LOG.md as you go. Code in code/, data in data/.
Source texts may go in sources/ as plain text only; no PDFs kept, no page images or scans of any paper or book anywhere in
this folder. Work only in this directory. At most 4 threads, under 4 GB, nice 10. No publication anywhere, no pushes.

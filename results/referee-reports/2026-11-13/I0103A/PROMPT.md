Open problem I0103. Source: the open-problems collection "Randomstrasse101" (A. S. Bandeira and coauthors, 2025; find it on
arXiv, record exact title, authors, arXiv id and version), Conjecture 29: "The Paley Equiangular Tight Frame construction satisfies the
Restricted Isometry Property beyond the square-root bottleneck. In other words, there exists eps > 0 such that, for m ~ p^{1/2+eps},
any matrix formed by picking m (distinct) vectors in the Paley ETF has condition number bounded by a constant independent of p."

What is known (verify each item from the source text before you rely on it):
- Bandeira, Fickus, Mixon, Wong, "The road to deterministic matrices with the restricted isometry property" (J. Fourier Anal.
  Appl. 2013) introduce the Paley ETF and show that RIP beyond sqrt follows from a conjectured bound on the clique number /
  discrepancy of the Paley graph. Bandeira, Mixon, Moreira ("A conditional construction of restricted isometries", find the arXiv id and journal)
  prove RIP beyond sqrt conditional on a Paley graph discrepancy conjecture. arXiv:2011.02907 (RIP of the Paley matrix) is
  conditional on its Conjecture 7.
- Bourgain, Dilworth, Ford, Konyagin, Kutzarova (Duke 2011) give the only unconditional explicit RIP beyond sqrt (eps tiny);
  Mixon's and Bandeira's later notes refine eps.
- arXiv:2611.14475 (submitted 10 Nov 2026), "Explicit restricted isometries with k = m^{2/3-o(1)}": explicit RIP from a large vertex
  set of a strongly regular graph in which every small subset spans few edges (via an incidence bound of Zahl), using only the
  entrywise absolute values of the Gram matrix; it shows the absolute-value barrier is m^{2/3}. It works with a chosen subset,
  not with the whole Paley ETF.
- Kunisky and Yu (CCC 2023, arXiv:2211.02713): degree-4 SoS lower bound Omega(p^{1/3}) for the Paley clique number.

Do this, in order, saving as you go:
1. Literature first. Get the source and each paper above (and any 2025-2026 work citing them on Paley ETF RIP, Paley graph
   discrepancy, or explicit RIP beyond sqrt). If Conjecture 29 is settled in print, report RESOLVED_IN_LITERATURE with theorem
   numbers and pages.
2. Otherwise attack it. Read 2611.14475 closely and decide precisely what its method gives for the Paley ETF itself:
   (a) Does every m-subset of the Paley ETF, or every m-subset avoiding a small structured family, satisfy the hypothesis its
   absolute-value argument needs? Paley cliques of size about log p span many edges, so state exactly which subsets fail and
   whether a signed (not absolute-value) argument, e.g. using quadratic character sums (Weil, Burgess) on the off-diagonal Gram
   entries, can handle them.
   (b) Can its argument be run for a large explicit sub-dictionary of the Paley ETF (a positive fraction of the vectors, or
   p^{1-delta} of them) with sparsity m = p^{1/2+eps}? That is a PARTIAL result if proved, and it must say how many vectors.
   (c) Or show a precise obstruction: a family of m-subsets with m = p^{1/2+eps} whose condition number grows, which would be a
   COUNTEREXAMPLE.
   Full Conjecture 29 is PROVED. A proved weaker statement for the Paley ETF (a sub-dictionary, a smaller eps conditional on a
   named standard conjecture, or a reduction to a cleaner number-theoretic statement with full proof) is PARTIAL.
3. Numerics are evidence only (for example, greedy or local search for badly conditioned m-subsets of the Paley ETF for primes
   p up to a few thousand). Keep runs small: at most 4 threads, under 4 GB.
Write REPORT.md. Its first line is exactly one of PROVED, COUNTEREXAMPLE, PARTIAL, NO_PROGRESS, RESOLVED_IN_LITERATURE.
Then the statement, the proof, what was checked and how, and the literature results with exact theorem numbers and pages.
Keep LOG.md as you go. Code in code/, data in data/. Source texts may go in sources/ as plain text only; no PDFs kept, no
page images or scans of any paper or book anywhere in this folder. Work only in this directory. At most 4 threads, under
4 GB, nice 10. No publication anywhere, no pushes.

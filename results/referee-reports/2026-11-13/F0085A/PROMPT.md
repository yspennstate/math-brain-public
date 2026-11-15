Open problem F0085. Source: C. Hoffman, A. E. Holroyd and Y. Peres, "A stable marriage of Poisson and Lebesgue", Ann. Probab.
34 (2006), arXiv:math/0505668, Section 12, Open problems (iii) Percolation, PDF p. 31: in the Poisson model with appetite
alpha < 1, does the set of unclaimed sites have an infinite component for alpha small enough? Does it fail to have one for
alpha < 1 large enough? The same questions for the claimed sites. The source notes progress in its reference [5]: Freire,
Popov and Vachkovskaia, "Percolation for the stable marriage of Poisson and Lebesgue", Stoch. Proc. Appl. 117 (2007). Read
the source for the exact setting and what [5] proved.

Do this, in order, saving as you go:
1. Literature first. Get arXiv:math/0505668 into sources/ (plain text only) and read Section 12 and the facts about stable
   allocation used later (territories, the radius bound, the subcritical tail). Read Freire-Popov-Vachkovskaia exactly: which
   of the four questions they answer, in which dimensions, under which hypotheses. Search for later work: Deijfen-Holroyd-Peres
   "Stable Poisson graphs"; Holroyd-Pemantle-Peres-Schramm "Poisson matching" (AIHP 2009); Marko-Timar; Hoffman-Holroyd-Peres
   on tail bounds; Chatterjee-Peled-Peres-Romik "Gravitational allocation"; anything 2008-2026 on percolation of territories
   or of the unclaimed set. If all four questions are answered in print, give exact references and theorems and stop with
   REPORT.md first line RESOLVED_IN_LITERATURE.
2. Pick the parts still open after step 1 and attack them with full proofs. Tools: for small alpha every territory lies in a
   ball of radius of order alpha^(1/d), so the claimed set is a union of small sets around centres and the unclaimed set
   contains the complement of a Boolean model; for alpha near 1 use the tail bounds and a renormalisation or finite-range
   comparison (the allocation inside a box depends on far centres only with small probability). Liggett-Schonmann-Stacey
   domination applies once a quantified finite-range dependence is proved.
3. Compute (evidence only). Compute the stable allocation on a large torus (Gale-Shapley on a fine grid of sites) for a range
   of alpha in d = 2, and measure the largest component of the claimed and unclaimed sets; estimate any threshold.
Write REPORT.md. Its first line is exactly one of PROVED, COUNTEREXAMPLE, PARTIAL, NO_PROGRESS, RESOLVED_IN_LITERATURE.
Then the statement, the proof, what was checked and how, and the literature result with exact theorem numbers and pages.
Keep LOG.md as you go. Code in code/, data in data/. Source texts may go in sources/ as plain text only; no PDFs kept, no
page images or scans of any paper or book anywhere in this folder. Work only in this directory. At most 4 threads, under
4 GB, nice 10. No publication anywhere, no pushes.

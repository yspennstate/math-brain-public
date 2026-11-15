Open problem C0113. Source: D. Aldous and J. M. Steele, "The objective method: probabilistic combinatorial optimization and
local weak convergence" (2004, in Probability on Discrete Structures, Encyclopaedia Math. Sci. 110), Section 6, pp. 63-64: for the
minimal spanning forest of a homogeneous Poisson point process in R^d, decide whether it is almost surely connected (a single
tree); known true for d = 2 (Alexander), conjectured false for d large. Read the source for the exact wording (free versus wired
forest, which is meant; what is conjectured for which d).

Do this, in order, saving as you go:
1. Literature first. Get the source into sources/ (plain text only, a public preprint version). Search: Alexander ("Percolation
   and minimal spanning forests in infinite graphs", Ann. Probab. 1995), Lyons-Peres-Schramm ("Minimal spanning forests", Ann.
   Probab. 2006), Newman-Stein (invasion percolation / ground states, high-dimensional MSF), Jackson-Read, Chatterjee-Sen,
   Garban-Pete-Schramm (scaling limit of planar MSF), Aldous-Steele 1992, Benjamini-Lyons-Peres-Schramm (uniform spanning forest
   analogy, d > 4), Duminil-Copin and coauthors on MSF / invasion percolation, Lyons-Peres book "Probability on Trees and Networks"
   (Chapter 11 open questions), and 2004-2026 work. Determine what is known for d >= 3 (equivalence with critical percolation
   having no infinite cluster, connectivity versus number of trees, results on Z^d versus Poisson). If the question is decided in
   print for some d >= 3, give the theorem and page and stop with RESOLVED_IN_LITERATURE.
2. Understand the gap: write Alexander's argument for d = 2 and what it uses (planarity, no infinite cluster at criticality in
   the plane, uniqueness), the Newman-Stein heuristic for infinitely many trees in high d (two-point function decay, d > 8), and
   which known theorems (e.g. lace expansion for continuum percolation, Heydenreich-van der Hofstad-Last-Matzke) could feed a proof.
3. Prove what you can, with complete proofs: a conditional theorem (for example, in high d, a quantitative critical two-point or
   arm-exponent hypothesis implies the MSF has infinitely many trees, with every hypothesis stated precisely and which of them are
   already proved for Poisson Boolean percolation in high d), or a reduction (MSF connected iff some percolation statement), or
   the analogous result for the wired forest.
4. Compute (evidence only): Kruskal-type MSF on large Poisson samples in boxes in d = 3, 4, 5 with periodic and free boundary,
   measuring whether two far-apart points are connected within the box forest as the box grows.
Write REPORT.md. Its first line is exactly one of PROVED, COUNTEREXAMPLE, PARTIAL, NO_PROGRESS, RESOLVED_IN_LITERATURE.
Then the statement, the proof, what was checked and how, and the literature result with exact theorem numbers and pages.
Keep LOG.md as you go. Code in code/, data in data/. Source texts may go in sources/ as plain text only; no PDFs kept, no
page images or scans of any paper or book anywhere in this folder. Work only in this directory. At most 4 threads, under
4 GB, nice 10. No publication anywhere, no pushes.

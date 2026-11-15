Open problem D0017. Source: D. Khoshnevisan, a 2005 survey / problem list on the Brownian sheet and its slices (find it by
author and title words "Brownian sheet", "slices", "open problems"; confirm it by Open Problem 2, Section 8.2, PDF p. 33).
Statement: for the two-parameter Brownian sheet B in R^d and s >= 0, let Y_d(s) = {(t_1, t_2) in R_+^2 : B(s, t_1) = B(s, t_2)},
the double-point set of the slice t -> B(s, t). Is it the case that for d in {4, 5}, outside a single null set,
dim_H Y_d(s) = 0 for all s >= 0? The source conjectures yes, and expects the corresponding statement for d <= 3 to be false
because of continuous intersection local times. Read the source for the exact wording (whether the trivial diagonal t_1 = t_2
is excluded, the Hausdorff dimension convention for an empty set, which slices are exceptional), and the known results it
quotes (Khoshnevisan's earlier work on slices, Mountford's results on slices of the sheet having double points, dimension
of exceptional slices).

Do this, in order, saving as you go:
1. Literature first. Get the source into sources/ (plain text only) and read Section 8 exactly. Search: Dalang-Khoshnevisan-
   Nualart-Wu-Xiao, "Critical Brownian sheet does not have double points" (Ann. Probab. 2012); Khoshnevisan-Wu-Xiao
   ("Sectorial local non-determinism and the geometry of the Brownian sheet"); Dalang-Mueller ("Intersections of random walks
   and Wiener sheets in the lattice" / multiple points of the Brownian sheet in critical dimensions); Mountford ("Double
   points and the Ornstein-Uhlenbeck process on Wiener space"); Rosen; Chen-Xiao; Khoshnevisan-Xiao on hitting probabilities
   of the sheet; Kahane; "exceptional slices", "double points of slices of the Brownian sheet"; and 2005-2026 citers of the
   source. If the question is answered in print, give the exact reference and theorem with page, check that it is the same
   statement (all s simultaneously, d = 4 and 5, the dimension being 0 rather than the set being empty), and stop with REPORT.md
   first line RESOLVED_IN_LITERATURE.
2. Understand the gap if one remains: for a fixed s the slice is a Brownian motion, which has double points iff d <= 3, so for
   d >= 4 a fixed slice has none; the question is about the exceptional random set of s. Derive the expected dimension of the
   set of s for which the slice has double points (codimension counting: the sheet's double-point parameter set in R_+^3), and
   why the dimension of Y_d(s) should be 0 on that set for d = 4, 5 but positive for d <= 3.
3. Prove what you can, with complete proofs: the upper bound dim Y_d(s) = 0 for all s simultaneously for d = 4, 5 (for instance
   via a covering argument on a dyadic grid in (s, t_1, t_2) with sectorial local non-determinism estimates), or the d = 5
   case alone, or a precise reduction.
4. Compute (evidence only). Simulate discretised Brownian sheets on a fine grid in d = 4, 5, find near-double-points of slices,
   and estimate box-counting dimensions of the exceptional s-set and of Y_d(s) on it.
Write REPORT.md. Its first line is exactly one of PROVED, COUNTEREXAMPLE, PARTIAL, NO_PROGRESS, RESOLVED_IN_LITERATURE.
Then the statement, the proof, what was checked and how, and the literature result with exact theorem numbers and pages.
Keep LOG.md as you go. Code in code/, data in data/. Source texts may go in sources/ as plain text only; no PDFs kept, no
page images or scans of any paper or book anywhere in this folder. Work only in this directory. At most 4 threads, under
4 GB, nice 10. No publication anywhere, no pushes.

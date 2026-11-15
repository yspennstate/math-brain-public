Open problem D0051. Source: J. Ding, J. Dubedat and E. Gwynne, "Introduction to the Liouville quantum gravity metric",
arXiv:2109.01252, Problem 5.3, PDF p. 24: let xi > 0 and let P be a D_h-geodesic for the LQG metric. Compute the Hausdorff
dimension of P intersected with the set T^alpha_h of alpha-thick points, for alpha in [-2, 2], with respect to D_h and the
Euclidean metric. More weakly: is there a unique alpha maximising this dimension (a typical thickness of a geodesic point)?
The analogue for the boundary of a metric ball is solved (maximiser alpha = xi Euclidean, alpha = gamma for LQG). Read the
source for the exact conventions (xi, d_gamma, Q, the range of alpha, the subcritical and supercritical phases).

Do this, in order, saving as you go:
1. Literature first. Get arXiv:2109.01252 into sources/ (plain text only) and read Section 5 and Problem 5.3 exactly. Search
   for answers or partial answers: Gwynne-Pfeffer-Sheffield on geodesics and metric ball boundaries in LQG; Gwynne on the
   dimension of the boundary of an LQG metric ball; Miller-Qian; Gwynne-Miller "Confluence of geodesic paths"; Ding-Gwynne-
   Sepulveda; Le Gall on geodesics in the Brownian map; Gwynne-Pfeffer "KPZ formulas for the LQG metric" (the KPZ relation for
   sets independent of h, and why a geodesic is not independent); Fan-Sung; Ang-Falconet-Sung; and 2022-2026 work on thick
   points on LQG geodesics or the Euclidean dimension of an LQG geodesic. If it is answered in print, give the exact reference
   and theorem and stop with REPORT.md first line RESOLVED_IN_LITERATURE.
2. Understand the difficulty. State what is known: the D_h-dimension of a geodesic is 1, bounds on its Euclidean dimension,
   the ball-boundary result and its proof method. Explain why the geodesic case is harder (no independence from h; the
   geodesic seeks thin regions).
3. Prove what you can, with complete proofs: an upper bound on dim(P cap T^alpha) for each alpha (a first-moment bound over
   dyadic squares, using the LQG distance across an alpha-thick square), the absence from geodesics of alpha-thick points for
   alpha above some value, a lower bound for some alpha, or the uniqueness of the maximiser in a sub-range. A rigorous upper
   bound curve together with its maximiser, clearly labelled as a bound, is worth writing up.
4. Compute (evidence only). Sample a discrete GFF on an N x N grid, compute LFPP geodesics (Dijkstra with weights e^{xi h}),
   and estimate the empirical distribution of the circle-average thickness along the geodesic at several scales.
Write REPORT.md. Its first line is exactly one of PROVED, COUNTEREXAMPLE, PARTIAL, NO_PROGRESS, RESOLVED_IN_LITERATURE.
Then the statement, the proof, what was checked and how, and the literature result with exact theorem numbers and pages.
Keep LOG.md as you go. Code in code/, data in data/. Source texts may go in sources/ as plain text only; no PDFs kept, no
page images or scans of any paper or book anywhere in this folder. Work only in this directory. At most 4 threads, under
4 GB, nice 10. No publication anywhere, no pushes.

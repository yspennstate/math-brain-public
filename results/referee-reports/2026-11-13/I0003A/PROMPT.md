Open problem I0003. Source: A. Bou-Rabee and Y. Peres, "The randomly oriented Manhattan lattice in 2D is transient",
arXiv:2609.07621, Section 7, Problem 3: "Which orientation fields give a recurrent walk, and which give a transient one? Theorem
1.1 gives transience for P-almost every environment. A uniform random shift by a vector in {0,1}^2 of the alternating environment
of Section 1.1 gives a stationary ergodic law with mean-zero line orientations under which the walk is recurrent almost surely."
Here each horizontal line y = k carries an orientation e_k in {left, right} and each vertical line x = j an orientation f_j in
{up, down}; the walk at each step moves one unit along the horizontal or the vertical line through its site, in the line's
direction, each with probability 1/2.

Do this, in order, saving as you go:
1. Literature first. Get arXiv:2609.07621 and the papers it builds on: Campanino-Petritis (random walks on randomly oriented
   lattices), Guillotin-Plantard and Le Ny, Bremont (2017 and later, deterministic/quasi-periodic orientations, e.g. rotation
   orientations frac(y alpha) < 1/2 recurrent a.e.), Pene, Castell-Guillotin-Pene-Schapira, Devulder-Pene, and any 2025-2026
   work. If a characterisation (or a substantial class) is in print, report RESOLVED_IN_LITERATURE or record exactly what is known.
2. Otherwise attack it. The walk's horizontal displacement is a random walk in random scenery driven by the vertical coordinate
   (and vice versa); recurrence is governed by the growth of partial sums S_k = sum_{i<=k} e_i and T_j = sum f_j. Aim for a
   sharp sufficient condition and a sharp necessary condition in terms of these partial sums, for example: recurrence if
   |S_n|, |T_n| = O(n^a) with a below an explicit threshold (bounded sums, as in the alternating case, give recurrence), and
   transience if both grow at least like n^{1/2} in a quantitative sense (random i.i.d. is the boundary case Theorem 1.1
   handles). Determine the threshold exponent(s) for deterministic power-law partial sums, and decide mixed cases (one direction
   balanced, the other random). Use local limit theorems for random walk in random scenery and Green function sums
   sum_n P(walk at origin at time n). A theorem settling a natural class (for example all fields with |S_n| ~ n^a, |T_n| ~ n^b,
   or all periodic or quasi-periodic fields) not already in print is PARTIAL; a full characterisation is PROVED.
3. Numerics (exact return probabilities by transfer/convolution for periodic fields, Monte Carlo for others) are evidence only.
Write REPORT.md. Its first line is exactly one of PROVED, COUNTEREXAMPLE, PARTIAL, NO_PROGRESS, RESOLVED_IN_LITERATURE.
Then the statement, the proof, what was checked and how, and the literature results with exact theorem numbers and pages.
Keep LOG.md as you go. Code in code/, data in data/. Source texts may go in sources/ as plain text only; no PDFs kept, no
page images or scans of any paper or book anywhere in this folder. Work only in this directory. At most 4 threads, under
4 GB, nice 10. No publication anywhere, no pushes.

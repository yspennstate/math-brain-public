Open problem I0004. Source: A. Bou-Rabee and Y. Peres, "The randomly oriented Manhattan lattice in 2D is transient", arXiv:2609.07621
(identify title, authors, date and version exactly from the arXiv listing), Section 7 "Open questions", inside Problem 3, attributed
there to Guillotin-Plantard and Le Ny [2008b, Section 4]. The question: "Fix an irrational alpha. Direct the line at height y in Z
to the right if the fractional part of y*alpha is less than 1/2, and to the left otherwise; vertical edges can be crossed in either
direction. Is this walk recurrent or transient?" State the exact walk (discrete or continuous time, the jump probabilities between
horizontal and vertical moves, laziness) as defined in the source and in Guillotin-Plantard--Le Ny, and whether the answer may
depend on alpha (bounded type, Liouville, quadratic irrationals).

Do this, in order, saving as you go:
1. Literature first. Get the source into sources/ as plain text. Find and read N. Guillotin-Plantard and A. Le Ny, "Transient random
   walks on 2d-oriented lattices" (Theory Probab. Appl. 2008) and their other papers on oriented lattices, M. Campanino and
   D. Petritis (Markov Process. Related Fields 2003) on random walks on randomly oriented lattices, Matheron--de Marsily, and any
   later work on deterministic or quasi-periodic orientations (Pene, Devulder, Castell--Guillotin-Plantard--Pene--Schapira, Brice,
   2026 work citing the source). State exactly what is known: which orientation sequences are proved transient or recurrent and by
   what criterion (the vertical walk's local times against the horizontal drift sums; the discrepancy of the rotation). If a printed
   result answers the question for some or all irrational alpha, report it and stop with RESOLVED_IN_LITERATURE.
2. Otherwise attack it. The natural route: the vertical coordinate is a (time-changed) simple random walk Y; the horizontal
   displacement up to time n is approximately sum_y eps_y L_n(y) with eps_y = +-1 the orientation and L_n the local time. For the
   rotation, the partial sums S_k = sum_{y<k} eps_y have discrepancy controlled by the continued fraction of alpha (Ostrowski
   expansion; for bounded type, |S_k| = O(log k); Kesten's theorem says 1/2 is not a bounded remainder interval for irrational alpha).
   Decide whether the horizontal displacement is of order sqrt(n) (as for the alternating environment, recurrent) or larger with
   enough spread to give a summable return probability. Prove recurrence or transience for as broad a class of alpha as you can
   (all irrational alpha; bounded type; a.e. alpha), with every step checked, including the reduction from the 2D walk to the
   local-time functional and the Green function sum. A complete answer for all irrational alpha, or for Lebesgue-a.e. alpha with an
   explicit description, is PROVED; a sharp answer for a natural subclass (bounded type) is PARTIAL with substance.
3. Compute only to check: exact return probabilities or Monte Carlo of the walk and of the functional sum_y eps_y L_n(y) for the
   golden ratio and a Liouville-type alpha. Keep runs small; no simulation stands in for a proof.
Write REPORT.md. Its first line is exactly one of PROVED, COUNTEREXAMPLE, PARTIAL, NO_PROGRESS, RESOLVED_IN_LITERATURE.
Then the statement, the proof, what was checked and how, and the literature results with exact theorem numbers and pages.
Keep LOG.md as you go. Code in code/, data in data/. Source texts may go in sources/ as plain text only; no PDFs kept, no
page images or scans of any paper or book anywhere in this folder. Work only in this directory. At most 4 threads, under
4 GB, nice 10. No publication anywhere, no pushes.

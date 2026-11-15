# Open problem C0132: transience and recurrence of the balanced excited random walks M(d1,d2)

The walk M(d1,d2) on Z^{d1+d2}: on the first visit to a vertex it takes a simple random walk step in the first d1
coordinates; on every later visit, a simple random walk step in the last d2 coordinates. Benjamini, Kozma and Schapira
("A balanced excited random walk", 2011) proved M(2,2) transient (check). QUESTION: prove that M(1,2) and M(2,1) are
transient and that M(1,1) is recurrent.

Check the literature 2011-2026 FIRST (Peres, Popov, Sousi "On recurrence and transience of self-interacting random walks"
(2013); Kosygina-Zerner and later work on excited and self-interacting walks; arXiv searches on "balanced excited random
walk", "M(1,2)", "M(2,1)"). For each of the three cases say whether it is settled in print, by whom, where, and with what
exact statement. If all three are settled, report that and stop.

Source of the problem: Kosygina and Zerner, "Excited random walks: results, methods, open problems" (2012), Remark and
Problem 3.22, pp. 16-17. A previous note (unreviewed): in M(1,1) the first coordinate is SRW on Z run at the rate of new
visits; M(1,1) is recurrent iff, at the infinitely many returns of the first coordinate to 0, the second coordinate returns
to 0 within column 0 before finding a new vertex, which has probability of order 1/(length of the visited interval in
column 0). Its obstruction: the growth of that interval was not controlled.

TASK for whatever remains open, in order:
1. Simulation first: estimate return probabilities and the growth of the range for each open case (up to 10^6-10^7 steps,
   many seeds, under 4 GB), to see which answer to aim for.
2. A proof strategy: the projection to the d2-coordinates is a time-changed SRW run on the times of revisits; the
   d1-coordinates move only on first visits. Control the number of first visits by time t (range of the walk) and combine
   with Green-function or Lyapunov-function arguments for transience; for M(1,1), a recurrence argument (e.g. a
   martingale-type or Lyapunov criterion in Z^2, or comparison with the known 2D results).
3. Prove what you can; state precisely what remains.
Keep peak memory under 4 GB; no worker pools larger than 4 threads.

OUTPUT: REPORT.md whose FIRST LINE is one of PROVED / PARTIAL / COUNTEREXAMPLE / NO_PROGRESS, then the theorem
statement(s), complete proofs written as for a referee, numerical tables with code paths, and what remains open.
Keep a running LOG.md. Save all code and data in this folder. Write like a professional mathematician; no narration of
your process inside the theorem/proof text.

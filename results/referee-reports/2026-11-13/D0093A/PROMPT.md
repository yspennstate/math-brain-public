Open problem D0093. Source: L. T. Rolla, "Activated random walks on Z^d", Probability Surveys 17 (2020); arXiv:1906.05037. Section 6,
Theorem 6.1 (the dichotomy for the total number of topplings T when stabilising activated random walk on the cycle of n sites, fast
phase versus slow phase) and the second Open Problem after Theorem 6.1 (PDF p. 30): improve the estimate
P(T <= kappa n log^2 n) >= 1 - n^{-delta} of (6.3) to one without the log^2 n term, i.e. a bound of order n.
A previous attempt (only notes, no proof) said: the two logarithms come from a union bound over sites and from the number of rounds of
the cyclic toppling procedure of Section 6.1; T <= kappa n without logs is equivalent to a uniform tail bound for the site odometer
in the fast phase. Treat that only as a lead to check.

Do this, in order, saving as you go:
1. Literature first. Get arXiv:1906.05037 into sources/ as plain text. State Theorem 6.1, (6.3), the model, the parameter regime of
   the fast phase and the open problem exactly, with page numbers. Find the paper that proves Theorem 6.1 (the survey cites it;
   likely Basu-Ganguly-Hoffman-Richey "Activated random walk on a cycle", or Rolla-Sidoravicius / Stauffer-Taggi / Hoffman-Richey-Rolla
   / Asselah-Rolla-Schapira / Forien-Gaudilliere / Hoffman-Johnson-Junge on ARW stabilisation time) and get it too. Search 2019-2026
   work on the stabilisation time / number of topplings / odometer of ARW on the cycle and on Z (including "Activated random walk on
   the cycle: fast mixing", "The density conjecture for activated random walk", Hoffman-Hu-Richey-Rizzolo, Bristiel-Salez, Junge-Levine
   and coauthors). If a printed result gives T = O(n) with high probability in the fast phase (or a subset of it), give the theorem and
   page, say exactly which part of the question it answers, and stop with RESOLVED_IN_LITERATURE (or PARTIAL if it covers only part).
2. Read the proof of (6.3) line by line and find exactly where each log factor enters.
3. Try to remove them: a complete proof of P(T <= C n) >= 1 - n^{-delta} (or with probability tending to one, which is a weaker but
   still useful statement; say which you prove), in the whole fast phase or a stated part of it (for example small density, or large
   sleep rate). Possible tools: an abelian-property toppling order that charges each instruction to a site with a geometric number of
   uses, a renewal or stochastic-domination argument for the odometer, a multi-scale argument. Every step checked. If the full answer
   is out of reach, prove a precise partial statement (one log removed, or T = O(n) for a stated subregime) or explain precisely why
   the method cannot give it.
4. Compute (evidence only): simulate ARW on the cycle in the fast phase for n up to about 10^5 (several densities and sleep rates),
   record T/n and its upper tail, and check whether T/n stays bounded or grows like log n.
Write REPORT.md. Its first line is exactly one of PROVED, COUNTEREXAMPLE, PARTIAL, NO_PROGRESS, RESOLVED_IN_LITERATURE.
Then the statement, the proof, what was checked and how, and the literature result with exact theorem numbers and pages.
Keep LOG.md as you go. Code in code/, data in data/. Source texts may go in sources/ as plain text only; no PDFs kept, no
page images or scans of any paper or book anywhere in this folder. Work only in this directory. At most 4 threads, under
4 GB, nice 10. No publication anywhere, no pushes.

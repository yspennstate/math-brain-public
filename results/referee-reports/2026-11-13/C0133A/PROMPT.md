Open problem C0133. Source: E. Kosygina and M. P. W. Zerner, "Excited random walks: results, methods, open problems",
Bull. Inst. Math. Acad. Sin. (N.S.) 8 (2013), 105-157, arXiv:1204.1895, Problem 4.7 (PDF p. 19): for excited random walks
on Z^d with i.i.d. elliptic cookie environments and a direction l, does X_n . l / n converge to 0 almost surely on the
complement of the event {|X_n| -> infinity}? Read the survey for the exact setting (the class of environments, ellipticity,
whether stacks may be infinite) and answer the question exactly as posed there; check the arXiv and journal numbering agree.

Do this, in order, saving as you go:
1. Literature first. Download arXiv:1204.1895 into sources/ and read Section 4 (Problem 4.7 and the results around it:
   the zero-one laws, Kalikow-type and renewal structures, Holmes, Holmes-Salisbury, Menshikov-Popov-Ramirez-Vachkovskaia
   "On a general many-dimensional excited random walk", Kosygina-Zerner directional transience, Amir-Berger-Orenshtein
   zero-one law for d=1, Berard-Ramirez, Kozma, van der Hofstad-Holmes). Search for 2012-2026 papers citing 1204.1895 that
   treat speed on the non-transient event. If the question is already answered in print, give the exact reference and
   theorem and stop with REPORT.md first line RESOLVED_IN_LITERATURE.
2. Reduce. Work out what the non-transient event forces (liminf |X_n| < infinity: some finite set is visited infinitely
   often). Decide which environments make the claim easy (finitely many cookies per site a.s.: after exhaustion the walk is
   simple random walk near that set, use a Borel-Cantelli/ratio argument) and where the difficulty really sits (infinite
   stacks, e.g. stacks whose drift persists or alternates). Prove what you can in full; state precisely the case left open.
3. Try both directions. Either prove X_n . l / n -> 0 a.s. on the complement in general (or in a stated large class), or
   build a counterexample environment law (i.i.d. over sites, elliptic) where with positive probability the walk returns to
   a finite set infinitely often yet X_n . l / n does not tend to 0 (e.g. liminf 0 and limsup > 0 along long excursions).
   Note the survey's own remarks on why this is open; a counterexample must respect i.i.d. and ellipticity exactly.
4. Check numerically any construction (simulate, report the event frequencies and the excursion statistics), but the claim
   rests on proof.
Write REPORT.md. Its first line is exactly one of PROVED, COUNTEREXAMPLE, PARTIAL, NO_PROGRESS, RESOLVED_IN_LITERATURE.
Then the statement, the proof or the construction, what was checked and how, and the literature found. Keep LOG.md as you
go. Code in code/, data in data/. Work only in this directory. At most 4 threads, under 4 GB, nice 10. No publication
anywhere, no pushes.

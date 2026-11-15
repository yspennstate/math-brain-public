Open problem C0130. Source: E. Kosygina and M. Zerner, "Excited random walks: results, methods, open problems",
Bull. Inst. Math. Acad. Sin. (N.S.) 8 (2013) 105-157, arXiv:1204.1895, Problem 3.12 (p. 13 of the arXiv version): compute, for
a transient excited random walk on Z, the probability P_0(X_n != 0 for all n >= 1) of never returning to the starting point.
Read the source for the exact setting around Problem 3.12 (likely bounded cookie stacks, M cookies per site, total drift
delta > 1, maybe identical cookie strengths p) and answer the question exactly as posed there.

Do this, in order, saving as you go:
1. Literature first. Download the source into sources/; read Section 3 around Problem 3.12 and what is known (branching-process
   / Ray-Knight methods of Basdevant-Singh, Kosygina-Zerner 2008, Kosygina-Mountford, Peterson, Toth's generalized Ray-Knight,
   Dolgopyat-Kosygina, Kozma-Orenshtein-Shinkar on excited random walk with periodic cookies, Pinsky?, Collevecchio et al.,
   any 2012-2026 paper computing return/escape probabilities). If computed in print, give exact reference and theorem and stop
   with REPORT.md first line RESOLVED_IN_LITERATURE.
2. Formulate escape probability through the backward branching process (the number of upcrossings of edges by a walk that goes
   to +infinity is a Markov chain / branching process with migration, built from the cookie stacks). Write an exact expression
   (e.g. a series or a fixed point of an explicit operator) and prove it. Determine whether it has a closed form in natural
   cases (one cookie per site with strength p; M identical cookies of strength p; the boundary case delta=1 vs delta>1).
3. Compute it numerically to high precision for several cases by two independent methods (the exact expression and Monte
   Carlo with very long runs or exact finite-volume truncation), and test candidate closed forms (rational functions of p and M,
   expressions in delta). If a closed form fits to many digits, try to prove it.
4. Any rigorous partial result (bounds, monotonicity in p, asymptotics as delta -> 1 or delta -> infinity) with proof.
Write REPORT.md. First line exactly one of PROVED, COUNTEREXAMPLE, PARTIAL, NO_PROGRESS, RESOLVED_IN_LITERATURE (PROVED = an
explicit formula, proved, for the setting as posed). Then statement, proofs, numerics, literature. Keep LOG.md. Code in code/,
data in data/. Work only in this directory. At most 4 threads, under 4 GB, nice 10. No publication, no pushes.

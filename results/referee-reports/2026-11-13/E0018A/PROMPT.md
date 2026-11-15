Open problem E0018. Source: M. Benaim, S. Le Borgne, F. Malrieu, P.-A. Zitt, "Some simple but challenging Markov processes",
Ann. Fac. Sci. Toulouse Math. (6) 24 (2015), arXiv:1412.7516, Open question 3 (Oscillations of the Lyapunov exponent), PDF p. 10:
"Is it possible to choose the two 2x2 matrices A_0 and A_1 in such a way that the set of jump rates r for which the associated
switched linear process is unstable is the union of several intervals?" The process: dX_t/dt = A_{I_t} X_t, where I_t is a
Markov chain on {0,1} switching at rate r in both directions (read the paper for the exact setting, including whether the
rates are symmetric, and answer the question exactly as posed there).

Do this, in order, saving as you go:
1. Literature first. Download arXiv:1412.7516 into sources/ and read Section 4 and Open question 3. Search for later work
   (Lawley-Mattingly-Reed 2014 "Sensitivity to switching rates in stochastically switched ODEs"; Benaim-Lobry-Sari-Strickler;
   Chitour-Mazanti-Sigalotti; Malrieu-Phung; Strickler; any 2015-2026 paper citing 1412.7516 that studies the sign of the top
   Lyapunov exponent as a function of the switching rate). If the question is already answered in print, say so with the
   exact reference and theorem, and stop with REPORT.md first line RESOLVED_IN_LITERATURE.
2. Formula. The top Lyapunov exponent lambda(r) is an integral against the invariant law of the angle process on the
   projective line (a two-state PDMP on the circle); write the formula and the invariant density (it solves a linear ODE
   system) explicitly, with a proof or a precise citation.
3. Search. Over 2x2 pairs (A_0, A_1) (including pairs with both matrices Hurwitz, as in the paper's examples), compute
   lambda(r) on a fine r grid with a reliable method (the invariant-density formula; cross-check with long Monte Carlo
   simulation and with a discretised Markov-chain computation). Look for pairs where {r : lambda(r) > 0} has at least two
   components. Use small integer or rational entries where possible.
4. Certify. For any candidate, prove the sign pattern rigorously: either interval arithmetic (mpmath.iv or a validated ODE
   integrator) at finitely many r values together with a rigorous argument that each component is a nonempty interval, or an
   exact asymptotic argument (r -> 0 and r -> infinity limits: lambda(0+) relates to the averaged single-matrix exponents and
   lambda(inf) to the top eigenvalue real part of (A_0+A_1)/2). Give the explicit matrices and the certified r points.
5. If no example exists in your search, try to prove a reason (e.g. monotonicity or a single sign change of lambda in some
   class) and report what you proved.
Write REPORT.md. Its first line is exactly one of PROVED, COUNTEREXAMPLE, PARTIAL, NO_PROGRESS, RESOLVED_IN_LITERATURE
(here PROVED means an explicit pair with a certified union of at least two intervals of instability; say clearly which).
Then the statement, the matrices, the proof or certificate, what was checked and how, and the literature result. Keep LOG.md
as you go. Code in code/, data in data/. Work only in this directory. At most 4 threads, under 4 GB, nice 10. No publication
anywhere, no pushes.

You are an independent referee. Claim under review (files in claim_files/: REPORT.md, LOG.md, code/, data/ of another run):
open problem E0018, F. Malrieu, "Some simple but challenging Markov processes", Ann. Fac. Sci. Toulouse Math. (6) 24 (2015),
arXiv:1412.7516, Open question 3 (oscillations of the Lyapunov exponent): can the two 2x2 matrices A_0, A_1 be chosen so that
the set of switching rates r for which the switched linear process dX/dt = A_{I_t} X is unstable is a union of several intervals?
The claim: A_0 = [[-3/4,-1],[1,-3/4]], A_1 = diag(5/4,-11/4), with certified lambda(1/10) > 0.18, lambda(5) in
[-0.0714,-0.0097], lambda(20) in [0.0703,0.0850], so {r : lambda(r) > 0} has at least two components. A_1 is NOT Hurwitz.

Break it if it is wrong.
1. Download arXiv:1412.7516 into sources/. Read Section 4 and Open question 3 exactly, with the text around it. Decide, with
   quotations, whether the question as posed requires both matrices Hurwitz (or another restriction, e.g. the example's
   setting) or is unrestricted. If restricted, the claim does not answer it: say so and verdict MAJOR at least.
2. Check the rate convention (generator r[f(x,1-i)-f(x,i)], stationary law 1/2,1/2) and the Lyapunov-exponent formula used.
3. Recompute lambda(r) independently (write your own code; do not reuse claim_files/code): the angle-process invariant
   density on the projective line, plus long Monte Carlo, at r = 1/10, 5, 20 and on a grid. Then check that the certification
   is rigorous: interval arithmetic or validated bounds, how the invariant density is enclosed, error terms, and whether the
   sign at r = 5 is really certified negative. Also check the limits r -> 0 (average of the two top exponents) and r -> inf
   (spectral abscissa of (A_0+A_1)/2) as an independent sanity check.
4. Is the unrestricted statement trivial or already known (e.g. a non-Hurwitz matrix makes it easy)? Search for prior
   examples (Lawley-Mattingly-Reed 2014, Benaim-Le Borgne-Malrieu-Zitt, Chitour-Mazanti-Sigalotti, Strickler, citing papers).
   Say precisely what, if anything, is new, and whether a Hurwitz example remains open.
Write REPORT.md. Its first line is exactly one of ACCEPT, MINOR, MAJOR, WRONG. Then: summary verdict, a numbered list of every
error or gap with location and fix, what you verified and how, the literature result, and your ruling on the wording. Keep
LOG.md as you go. Work only in this directory. At most 4 threads, under 4 GB, nice 10. No publication anywhere, no pushes.

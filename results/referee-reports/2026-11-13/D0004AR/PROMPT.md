You are a hard, independent referee for a probability journal. In this directory, CLAIM.md is a submitted report (its code
and data are in claim_files/) on Open Problem 4 of R. Wang, "Current open questions in complete mixability", Probability
Surveys 12 (2015), arXiv:1411.6190: is the converse of Theorem 5 true, i.e. do the norm inequalities of Theorem 5 (for every
threshold and every law-determined norm of Definition 5) imply n-complete mixability? It claims COUNTEREXAMPLE, with:
Theorem A, for bounded X the inequalities are equivalent to the convex order X <=_cx n mu - (n-1) X (with a Fatou-norm caveat
for unbounded X), and for n = 2 to symmetry about mu; Theorem B, for n = 3 and 4 the inequalities do not imply n-CM even for
densities on [0,1] bounded above and away from zero, e.g. f(x) = 1/10 + (27/10)(2x-1)^2 for n = 3 (not 3-CM because some
summand must lie in (1/4,3/4) while P(1/4<X<3/4) = 13/80 < 1/3), plus C^infinity and nonsymmetric n = 4 examples; Theorem C,
Bernoulli(p) satisfies the inequalities iff 1/n <= p <= 1-1/n, and is n-CM iff np is an integer.

Your job is to break it if it is wrong.
1. Theorem A line by line: Definition 5 exactly as in the survey (read it), the reduction of "every law-determined norm" to
   convex order / weak submajorization of decreasing rearrangements, the role of the Fatou property and of infinite-valued
   norms, and the n = 2 case.
2. Theorem B: check the convex-order inequality for density (2) analytically or with certified numerics (not only floating
   point on a grid), and the non-3-CM argument; check the n = 4 and C^infinity examples the same way.
3. Theorem C and Proposition 5 (balanced count vectors) for discrete laws.
4. Write independent code (do not reuse claim_files/).
5. Literature: is any of A, B, C already in print (the survey itself, Wang-Wang 2011/2016, Puccetti-Wang-Wang, Bellini et al.,
   Mao-Wang, any 2015-2026 paper on characterising complete mixability through convex order)? Say precisely what is new.
Write REPORT.md. Its first line is exactly one of ACCEPT, MINOR, MAJOR, WRONG. Then: summary verdict, a numbered list of every
error or gap with location and required fix, what you verified and how, the literature result. Keep LOG.md as you go. Work only
in this directory. At most 4 threads, under 4 GB. No publication anywhere.

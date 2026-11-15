Open problem C0119. Source: S. Chatterjee, "Chaos, concentration, and multiple valleys" (2008), arXiv:0810.4221,
Section 12, open problem (2), p. 59: prove chaos (sensitivity of the polymer measure, in Chatterjee's sense: the overlap
between polymers sampled under the environment and under a slightly perturbed environment becomes small) for directed
polymers in random environment in dimensions d >= 3 at low temperature. Read the source for the exact definition of chaos
used for polymers, and for what the paper proves (it proves chaos/superconcentration for some polymer models; say exactly
which, e.g. Gaussian environment, d = 1+1, ground states).

Do this, in order, saving as you go:
1. Literature first. Get arXiv:0810.4221 into sources/ (text only), read the polymer sections and Section 12. Search
   2008-2026: Chatterjee's book "Superconcentration and related topics" (2014), Comets' book "Directed polymers in random
   environments" (2017), Chatterjee's "disorder chaos" for polymers, Chen (Wei-Kuo) and coauthors on chaos, Ganguly-Hegde
   and Basu-Ganguly-Hammond for LPP chaos (d = 1), Bates-Chatterjee "The endpoint distribution of directed polymers" and
   "Localization in Gaussian disordered systems at low temperature", Bates on full-path localization, Junk-Lacoin, Lacoin
   on very strong disorder in d >= 3, and anything citing this open problem. If it is answered in print for d >= 3 at low
   temperature, give the exact reference and theorem and stop with REPORT.md first line RESOLVED_IN_LITERATURE. If only
   other regimes are covered (high temperature where chaos fails or holds trivially, d = 1, 2, ground states, Gaussian
   environments only) say so precisely and continue.
2. Attack. The paper's route is superconcentration => chaos via the OU semigroup identity for Gaussian environments:
   Var(log Z) = integral of e^{-t} E[R(t)] dt, so chaos follows from Var(log Z_n) = o(n) (n = polymer length, overlap in
   units of n). So for Gaussian environments, chaos in d >= 3 at low temperature reduces to sublinear variance of the free
   energy. State that reduction exactly and prove it. Then determine what is known about Var(log Z_n) in d >= 3 at low
   temperature (upper bounds: Benaim-Rossignol / Alexander-Zygouras type n/log n bounds for first passage percolation and
   polymers; Graham's superconcentration for polymers?) If an n/log n variance bound is available or provable for Gaussian
   directed polymers in every dimension (e.g. via the Benjamini-Kalai-Schramm / Talagrand L1-L2 inequality with hypercontractivity
   applied to log Z_n), that proves chaos in Chatterjee's sense for every d and every temperature; check carefully whether this
   is already in the literature (Alexander-Zygouras 2013 "Subgaussian concentration and rates of convergence in directed
   polymers"; Chatterjee's book Ch. on polymers) and whether Chatterjee's open problem asks for something stronger (a
   different notion of chaos, non-Gaussian environment, quantitative rate). Answer exactly the question as posed.
3. Compute (optional, modest). Simulate small Gaussian directed polymers in d = 3 at low temperature (transfer matrix in
   1+3 dimensions, n up to what fits) to estimate the overlap under OU perturbation, only as evidence.
Write REPORT.md. Its first line is exactly one of PROVED, COUNTEREXAMPLE, PARTIAL, NO_PROGRESS, RESOLVED_IN_LITERATURE.
Then the statement, the proof, what was checked and how, and the literature result with exact theorem numbers and pages.
Keep LOG.md as you go. Code in code/, data in data/. Source texts may go in sources/ as plain text only; no PDFs kept, no
page images or scans of any paper or book anywhere in this folder. Work only in this directory. At most 4 threads, under
4 GB, nice 10. No publication anywhere, no pushes.

Open problem E0022. Source: a 2019 survey on Hunt's hypothesis (H) for Markov and Levy processes (source id
hunts_hypothesis_survey_2019; most likely Ze-Chun Hu and Wei Sun, a survey or "open problems" paper on Hunt's hypothesis and
Getoor's conjecture, 2019; find it on arXiv by authors and words "Hunt's hypothesis", "semipolar", "Getoor's conjecture",
"Levy processes", "open problems"), Question 1, PDF p. 15: let X be an R^n-valued Levy process. If for every nonempty proper
subspace A of R^n the projection process X_A of X on A satisfies (H) (every semipolar set is polar), does X itself satisfy (H)?
Read the source for the exact wording (what "projection process" means: the image of X under the orthogonal projection onto A,
a Levy process on A; and whether the converse direction is known).

Do this, in order, saving as you go:
1. Literature first. Get the source into sources/ (plain text only). State Question 1 exactly, and every theorem in the source
   about (H) for sums, products, projections and subordination of Levy processes. Search: Hu-Sun ("Hunt's hypothesis (H) and
   Getoor's conjecture for Levy processes", SPA 2012; "Further study on Hunt's hypothesis (H) for Levy processes"), Hu-Sun-Zhang,
   Hu-Sun-Wang, Kanda, Rao ("On polar sets for Levy processes", 1977 / "Hunt's hypothesis for Levy processes" 1988), Glover-Rao,
   Blumenthal-Getoor, Forst, Hawkes, Fitzsimmons, Silverstein, Kesten (polar points, (H) in dimension 1: Kesten-Bretagnolle),
   Jacob, and 2019-2026 work on "Hunt's hypothesis" and "semipolar" for Levy processes. Known facts to pin down with page
   numbers: Kanda/Rao: (H) holds if the symmetric part dominates (sector condition / Re psi >= c |Im psi|); Hu-Sun: (H) is
   preserved under some independent sums; Getoor's conjecture (every "nice" Levy process satisfies (H)) is open; and whether (H)
   for X implies (H) for projections. If a printed theorem answers Question 1, give the theorem and page and stop with
   RESOLVED_IN_LITERATURE.
2. Understand: (H) for a Levy process is equivalent to a condition on the potential theory of the exponent psi (for example
   via Kanda's or Rao's criteria; semipolar = finely thin everywhere except a polar set; for Levy processes semipolar sets are
   polar iff the process and its dual have the same polar sets and quasi-continuity holds). Write down which analytic criteria
   on psi are sufficient for (H) and which are known to be necessary.
3. Prove what you can, with complete proofs: either (a) YES under extra conditions (for example, if each one-dimensional
   projection satisfies a sector-type bound uniformly in the direction then X satisfies (H)); or (b) a COUNTEREXAMPLE: a Levy
   process on R^2 (or R^n) whose every proper projection satisfies (H) but X does not. Natural candidates: processes whose
   projections become symmetric-dominated or have no nontrivial semipolar sets (e.g. projections that are compound Poisson plus
   a symmetric stable part, or one-dimensional projections that hit points), while X itself is a non-symmetric process in the
   plane with a drift-dominated part along a curve; note that a uniform motion (pure drift) in R^n violates (H) (points on its
   path are semipolar, not polar) but so do its projections, so the counterexample must mix. Check the candidates against the
   known criteria in full.
4. Compute (evidence only, if helpful): numerically check sector-type inequalities for the exponents of candidate processes over
   all directions.
Write REPORT.md. Its first line is exactly one of PROVED, COUNTEREXAMPLE, PARTIAL, NO_PROGRESS, RESOLVED_IN_LITERATURE.
Then the statement, the proof, what was checked and how, and the literature result with exact theorem numbers and pages.
Keep LOG.md as you go. Code in code/, data in data/. Source texts may go in sources/ as plain text only; no PDFs kept, no
page images or scans of any paper or book anywhere in this folder. Work only in this directory. At most 4 threads, under
4 GB, nice 10. No publication anywhere, no pushes.

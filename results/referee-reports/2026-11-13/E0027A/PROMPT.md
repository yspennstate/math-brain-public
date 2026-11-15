Open problem E0027. Source: the 2019 survey on Hunt's hypothesis for Levy processes (the problem list records it as
"hunts_hypothesis_survey_2019, Question 7, PDF p. 25"; identify it exactly: likely Ze-Chun Hu and Wei Sun, "Hunt's hypothesis (H)
and Getoor's conjecture for Levy processes" or their survey "Some open problems on Hunt's hypothesis (H)", check authors, title,
journal, year, arXiv id). Question 7 asks whether Hunt's hypothesis (H) (every semipolar set is polar) is stable under independent
sums: if X and Y are independent Levy processes on R^d each satisfying (H), does X + Y satisfy (H)?
A previous first pass (notes only, unreviewed) said: the Kanda-Forst sector-type condition |Im psi| <= M(1 + Re psi) is stable under
independent sums, so the answer is yes inside that class. Treat it only as a lead to check.

Do this, in order, saving as you go:
1. Literature first. Get the survey into sources/ as plain text; state Question 7, the definitions of (H), polar and semipolar sets,
   and the known sufficient conditions (Kanda-Forst, Rao, Hu-Sun results on (H) for sums, subordinators, Getoor's conjecture) exactly,
   with page numbers. Search 2019-2026 work (Hu, Sun, Zhang, Glover-Rao, Kanda, Hawkes, "Hunt's hypothesis" "sum of independent Levy
   processes", "Getoor's conjecture"). If a printed result answers Question 7 (fully or for a stated class), give the theorem and page
   and stop with RESOLVED_IN_LITERATURE (or PARTIAL if it covers only part).
2. Check the lead: prove (with every step) that the Kanda-Forst condition passes to independent sums and implies (H) for the sum; say
   exactly what class this covers and whether it is already stated in print (then it is not new).
3. Try for the full answer: a proof that (H) for X and Y implies (H) for X + Y, or a counterexample (a pair of Levy processes, for
   example on R or R^2, with (H) each, whose sum fails (H); natural places: processes with a nontrivial drift component, compound
   Poisson plus subordinator, processes on different subspaces of R^2, the Hawkes / Rao criteria via the potential density and
   the symmetric part). If the full answer is out of reach, prove a precise partial statement for a new class (beyond what is in
   print) or explain precisely where each method breaks.
4. Compute only if it helps (for example, numerical checks of a potential-density criterion for a candidate counterexample).
Write REPORT.md. Its first line is exactly one of PROVED, COUNTEREXAMPLE, PARTIAL, NO_PROGRESS, RESOLVED_IN_LITERATURE.
Then the statement, the proof, what was checked and how, and the literature result with exact theorem numbers and pages.
Keep LOG.md as you go. Code in code/, data in data/. Source texts may go in sources/ as plain text only; no PDFs kept, no
page images or scans of any paper or book anywhere in this folder. Work only in this directory. At most 4 threads, under
4 GB, nice 10. No publication anywhere, no pushes.

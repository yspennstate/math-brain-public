Open problem D0071. Source: G. R. Grimmett and Z. Li, survey on self-avoiding walks and connective constants (2017; the problem
list records it as "grimmett_li_saw_2017, Question 3.4, Section 3.2, PDF p. 13"; identify it exactly: likely "Self-avoiding walks
and connective constants", in Sojourns in Probability Theory and Statistical Physics III (2019), arXiv:1704.05884; check authors,
title, venue, year, arXiv id). The golden-mean question: is the connective constant mu(G) >= phi = (1+sqrt5)/2 for every
infinite, connected, cubic, vertex-transitive (or quasi-transitive, as stated there) graph G? State the exact question.

Do this, in order, saving as you go:
1. Literature first. Get the source into sources/ as plain text; state Question 3.4 and the known results exactly, with page
   numbers: Grimmett-Li "Cubic graphs and the golden mean" (arXiv:1610.00107, Discrete Math. 2020?) - the cases proved there
   (graphs with a graph height function, positive first Betti number of the quotient, two-ended graphs, Cayley graphs of
   virtually solvable groups or with a strong graph height function, etc.); Grimmett-Li "Bounds on connective constants", "Strict
   inequalities for connective constants", "Locality of connective constants"; later work 2017-2026 ("golden mean" "connective
   constant" "cubic", Panagiotis, Lindorfer, Bonato, Gilch-Müller). If a printed result proves the conjecture fully, give it and stop
   with RESOLVED_IN_LITERATURE; if for new classes beyond the survey, report them (PARTIAL).
2. Otherwise attempt a proof for a class of cubic transitive graphs not covered in print (for example Cayley graphs of groups
   with infinite abelianisation are covered; consider one-ended amenable graphs without a height function, Cayley graphs of
   Grigorchuk-type groups, or a general argument via unimodularity / bridges / the number of ends), with every step checked;
   or find a cubic transitive graph with mu < phi (a counterexample) and prove the bound. State precisely what remains.
3. Compute (evidence only): exact SAW counts c_n and ratio / Kesten-type upper bounds for explicit cubic transitive graphs not
   covered in print (e.g. cubic Cayley graphs of the lamplighter group, of the Grigorchuk group, of Baumslag-Solitar groups, of
   hyperbolic triangle groups), enough to see whether mu is near phi.
Write REPORT.md. Its first line is exactly one of PROVED, COUNTEREXAMPLE, PARTIAL, NO_PROGRESS, RESOLVED_IN_LITERATURE.
Then the statement, the proof, what was checked and how, and the literature result with exact theorem numbers and pages.
Keep LOG.md as you go. Code in code/, data in data/. Source texts may go in sources/ as plain text only; no PDFs kept, no
page images or scans of any paper or book anywhere in this folder. Work only in this directory. At most 4 threads, under
4 GB, nice 10. No publication anywhere, no pushes.

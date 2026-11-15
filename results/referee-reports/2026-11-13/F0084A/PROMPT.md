Open problem F0084. Source: C. Hoffman, A. E. Holroyd, Y. Peres, "A stable marriage of Poisson and Lebesgue", Ann. Probab. 34
(2006), arXiv:math/0505668, Section 12, Open problems (ii) "Critical tail behavior", PDF p. 31, and the abstract: for the
critical model (Poisson centres of intensity 1 in R^d, each with appetite alpha = 1, so total appetite equals volume), what is
the tail of X, the distance from a typical site to its centre? In particular give ANY quantitative upper bound on P(X > r) for
d >= 2 ("It is an open problem to prove any upper bound in d > 1"). The paper proves E X^d = infinity in the critical case and
power-law lower bounds. (Read the source for the exact definitions: the stable allocation, the site-optimal/centre-optimal
version, X versus the centre-to-site distance X*, Theorem 32 and the lower bounds, and what is proved for d = 1.)

Do this, in order, saving as you go:
1. Literature first. Download arXiv:math/0505668 into sources/ (plain text only) and read Sections 1, 5-7 (the tail results) and
   12 exactly. Search for later work: Hoffman-Holroyd-Peres "Tail bounds for the stable marriage of Poisson and Lebesgue" (Canad.
   J. Math. 2009); Holroyd-Pemantle-Peres-Schramm "Poisson matching"; Chatterjee-Peled-Peres-Romik "Gravitational allocation to
   Poisson points" and "Phase transitions in gravitational allocation"; Markó-Timár "A Poisson allocation of optimal tail";
   Nazarov-Sodin-Volberg transportation; Huesmann-Sturm optimal transport from Lebesgue to Poisson; Holroyd "Geometric properties
   of Poisson matchings"; Freire-Holroyd-Martin; Amir-Angel-Holroyd stable allocations of exponential tails; Deijfen-Holroyd-Peres;
   anything 2006-2026 citing math/0505668 with "critical" or "tail". If an upper bound in d >= 2 is in print, give the exact
   reference and theorem and stop with REPORT.md first line RESOLVED_IN_LITERATURE.
2. Understand the gap. Explain why the d = 1 argument (if any) or the subcritical/supercritical arguments do not give an upper
   bound at criticality in d >= 2, and what a natural conjectured tail is (heuristic from the discrepancy of Poisson points in a
   ball: fluctuations of order r^{d/2}, and how unsatisfied demand must travel).
3. Prove what you can, with complete proofs: any explicit upper bound P(X > r) <= C r^{-s} (any s > 0), or even P(X > r) -> 0 at
   an explicit rate such as 1/log r, for d = 2 or all d >= 2; or an upper bound for a natural variant (X*, or a box/torus version
   with explicit dependence on the box size). Stability and the Gale-Shapley structure, local rules for the allocation, and
   comparison with the subcritical model with appetite alpha slightly below 1 are the natural tools.
4. Compute (as evidence only). Simulate the critical stable allocation on a large torus in d = 2 (discretised Lebesgue measure,
   Poisson centres), measure the empirical tail of X and how it depends on torus size, and fit a power law.
Write REPORT.md. Its first line is exactly one of PROVED, COUNTEREXAMPLE, PARTIAL, NO_PROGRESS, RESOLVED_IN_LITERATURE.
Then the statement, the proof, what was checked and how, and the literature result with exact theorem numbers and pages.
Keep LOG.md as you go. Code in code/, data in data/. Source texts may go in sources/ as plain text only; no PDFs kept, no
page images or scans of any paper or book anywhere in this folder. Work only in this directory. At most 4 threads, under
4 GB, nice 10. No publication anywhere, no pushes.

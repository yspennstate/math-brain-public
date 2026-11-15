Open problem I0079. Source: the paper on exactness for invariant random equivalence relations and Bernoulli Voronoi
tessellations recorded in our intake as "exactness_ire_2025" (find it: search arXiv for "ideal Bernoulli Voronoi tessellation",
"cell selection rule", "invariant random equivalence relation" exactness, 2024-2025; record the exact title, authors and arXiv id),
Question 2: "In what generality can one say that there is a unique ideal Bernoulli Voronoi tessellation on a group?" The source
then defines cell selection rules: measurable equivariant maps phi : E -> (2^Gamma)^Gamma with phi_r(gamma) = [gamma]_r or empty,
trivial if they select all cells or none.

Do this, in order, saving as you go:
1. Literature first. Get the source and state its definitions (ideal Poisson/Bernoulli Voronoi tessellation, IRE, exactness, the
   theorem they prove and the groups it covers) exactly. Get the work it builds on: Bhupatiraju, Budzinski, D'Achille,
   Enriquez, Mellick, Paquette, Fraczyk, Lafont-Raimbault, Mellick-Bhupatiraju-... on ideal Poisson-Voronoi tessellations, and
   any 2025-2026 follow-ups. If uniqueness in a stated generality (all non-amenable groups, all groups with cost > 1, all
   free products, Kazhdan groups, ...) is in print, report RESOLVED_IN_LITERATURE with theorem numbers.
2. Otherwise attack it: prove uniqueness for a natural class of groups beyond what the source proves (for example free groups
   and free products, groups with infinitely many ends, Gamma x Z, lattices in products), or find a group where the limit is
   not unique or not ideal. Be explicit about which limit (low-intensity limit of Bernoulli Voronoi on a Cayley graph) and in
   which topology uniqueness is meant. A theorem for a new class is PARTIAL; full generality is PROVED; a non-uniqueness example
   is COUNTEREXAMPLE.
3. Numerics are evidence only.
Write REPORT.md. Its first line is exactly one of PROVED, COUNTEREXAMPLE, PARTIAL, NO_PROGRESS, RESOLVED_IN_LITERATURE.
Then the statement, the proof, what was checked and how, and the literature results with exact theorem numbers and pages.
Keep LOG.md as you go. Code in code/, data in data/. Source texts may go in sources/ as plain text only; no PDFs kept, no
page images or scans of any paper or book anywhere in this folder. Work only in this directory. At most 4 threads, under
4 GB, nice 10. No publication anywhere, no pushes.

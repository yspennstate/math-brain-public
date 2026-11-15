Open problem E0093. Source: P. Diaconis, "Some things we have learned (about Markov chain Monte Carlo)", Bernoulli 19 (2013),
arXiv:1309.7754, Question 2, PDF p. 9: for an arbitrary finite group G, if a generating set S (of a given size k) is chosen at
random, what is the typical rate of convergence of the random walk it generates? Read Question 2 exactly: the size of S as a
function of |G| (fixed k, k ~ log|G|, k = (log|G|)^c), the walk (lazy or symmetric, uniform on S union S^-1), which speed is
meant (total variation mixing time, spectral gap, cutoff), and what the source says is known (Hildebrand's survey of random
random walks; Babai-Beals-Seress diameter bounds for random Cayley graphs turned into mixing bounds).

Do this, in order, saving as you go:
1. Literature first. Download arXiv:1309.7754 into sources/ (plain text only). Search for later work: Hildebrand "A survey of
   results on random random walks on finite groups" (Probab. Surveys 2005); Dou-Hildebrand; Roichman "On random random walks"
   (Ann. Probab. 1996); Alon-Roichman "Random Cayley graphs and expanders"; Wilson "Random random walks on Z_2^d"; Hough
   "Mixing and cut-off in cycle walks"; Hermon-Olesker-Taylor "Cutoff for almost all random walks on abelian groups" and
   "Geometry of random Cayley graphs of abelian groups" and their nilpotent sequels; Dubail "random walks on random Cayley
   graphs, Heisenberg"; Breuillard-Varju; Helfgott-Seress diameter of symmetric groups; Eberhard-Jezernik "Babai's conjecture
   for high-rank classical groups with random generators"; Breuillard-Gamburd-Green-Guralnick-Tao expansion of random pairs in
   finite simple groups of Lie type; Pak; Lubotzky. If the question is answered in print in a precise form, give the exact
   reference and theorem and stop with REPORT.md first line RESOLVED_IN_LITERATURE.
2. Make it precise. State two or three precise versions (for example: (A) for k >= C log|G| random generators, the walk mixes
   in O(log|G|) steps with high probability, for every finite G - is this the Alon-Roichman / Roichman theorem, and what are the
   exact constants?; (B) for fixed k = 2 or 3, is the typical mixing time polylog(|G|) for every finite group, and what is known
   for abelian, nilpotent, solvable, simple groups; (C) is there cutoff, and at what time, for k ~ log|G| on a general G). Say
   which versions are settled in print, which are open, and which is closest to the source's intent.
3. Prove what you can. Give full proofs for a precise version not already in print, or a clean new proof or sharpening of a
   known one (explicit constants, a lower bound matching an upper bound, a new class of groups, e.g. groups with a large abelian
   normal subgroup or wreath products, or a counterexample family showing a proposed uniform bound fails for fixed k).
4. Compute (as evidence only). For small groups (abelian, dihedral, S_n for n <= 8, PSL(2,p) for small p, Heisenberg groups mod
   p) sample random generating sets of size k, compute exact TV mixing times and spectral gaps, and compare against the bounds.
Write REPORT.md. Its first line is exactly one of PROVED, COUNTEREXAMPLE, PARTIAL, NO_PROGRESS, RESOLVED_IN_LITERATURE.
Then the precise statements, the proofs, what was checked and how, and the literature result with exact theorem numbers and
pages. Keep LOG.md as you go. Code in code/, data in data/. Source texts may go in sources/ as plain text only; no PDFs kept,
no page images or scans of any paper or book anywhere in this folder. Work only in this directory. At most 4 threads, under
4 GB, nice 10. No publication anywhere, no pushes.

Open problem C0092. Source: M. Heydenreich and R. van der Hofstad, "Progress in high-dimensional percolation and random
graphs" (CRM Short Courses, Springer 2017), Open Problem 16.10, p. 254: for the random-cluster (FK) model on Z^d with cluster
weight q > 0, show that the threshold for finite susceptibility equals the threshold for percolation (sharpness of the phase
transition), so that a single p_c(q) is defined. Read the source for the exact statement and which q it means; for q >= 1 the
question is answered (Duminil-Copin, Raoufi, Tassion, "Sharp phase transition for the random-cluster and Potts models via
decision trees", Ann. Math. 2019), so the open part is 0 < q < 1, where the measure is not positively associated.

Do this, in order, saving as you go:
1. Literature first. Get the source text into sources/ (plain text only, the book chapter or its arXiv version) and read
   Section 16 exactly. Search: Duminil-Copin-Raoufi-Tassion (OSSS method, q >= 1), Grimmett's book "The Random-Cluster Model"
   (q < 1 chapter, comparison inequalities, the conjectured negative association), Dubédat?, Lyons-Peres, Kahn ("negative
   association" for q < 1), Pemantle, Hutchcroft ("New critical exponent inequalities for percolation and the random cluster
   model", "Continuity of the Ising phase transition on nonamenable groups"), Duminil-Copin's lecture notes, uniform spanning
   forest limits (q -> 0), arboreal gas / q -> 0 limits (Bauerschmidt-Crawford-Helmuth-Swan, "Percolation transition for random
   forests in d >= 3", 2021-2024), and 2017-2026 work on sharpness for q < 1. If sharpness for some or all q in (0,1) is proved
   in print, give the exact reference and theorem and the range of q and d; stop with RESOLVED_IN_LITERATURE only if all
   q in (0,1) and all d >= 2 are covered.
2. Understand the gap: list exactly which steps of the OSSS / Menshikov / Aizenman-Barsky proofs use positive association
   (FKG) or monotonicity in p for q < 1, and which survive (comparison with Bernoulli percolation, finite-energy, the q < 1
   comparison inequalities). Decide whether monotonicity of the percolation probability in p is itself known for q < 1.
3. Prove what you can, with complete proofs: sharpness for q close to 1 (perturbative), for d large, on trees or nonamenable
   transitive graphs, for q in (0,1) under an assumed negative-correlation inequality, or a precise reduction to such an
   inequality.
4. Compute (evidence only). Exact enumeration / Monte Carlo (Chayes-Machta or Glauber with weights) for q in {0.25, 0.5, 0.75}
   on Z^2 and Z^3 tori: compare the susceptibility blow-up point with the percolation threshold.
Write REPORT.md. Its first line is exactly one of PROVED, COUNTEREXAMPLE, PARTIAL, NO_PROGRESS, RESOLVED_IN_LITERATURE.
Then the statement, the proof, what was checked and how, and the literature result with exact theorem numbers and pages.
Keep LOG.md as you go. Code in code/, data in data/. Source texts may go in sources/ as plain text only; no PDFs kept, no
page images or scans of any paper or book anywhere in this folder. Work only in this directory. At most 4 threads, under
4 GB, nice 10. No publication anywhere, no pushes.

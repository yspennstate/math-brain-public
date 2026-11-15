Open problem F0101. Source: M. Talagrand, the 2016 list of problems with prizes ("Some open problems", his web page; also his
convolution note), Section 4, PDF pp. 2-3: on G = {-1,1}^N with Haar measure lambda, let mu be a biased-coin product measure.
Prove that there is phi: R_+ -> R_+ with t phi(t) -> 0 as t -> infinity such that for every f >= 0 with integral f d lambda = 1
and every t >= 0, lambda({f * mu >= t}) <= phi(t). (Markov gives 1/t; the conjecture asks for o(1/t) uniformly in f.)
Read the source for the exact statement, the finite-dimensional version (uniform in the dimension n), the Gaussian
(Ornstein-Uhlenbeck) analogue, and the prize attached.

Do this, in order, saving as you go:
1. Literature first. Get the source(s) into sources/ (plain text only). Search: Ball-Barthe-Bednorz-Oleszkiewicz-Wolff
   ("L1-smoothing for the Ornstein-Uhlenbeck semigroup", Mathematika 2013: Gaussian case with a loss), Eldan-Lee
   ("Regularization under diffusion and anti-concentration of the information content", Duke 2018: Gaussian case up to
   log log), Lehec ("Regularization in L1 for the Ornstein-Uhlenbeck semigroup", 2016), Gozlan-Li-Madiman-Roberto-Samson
   ("Dimensional improvements of the logarithmic Sobolev, Talagrand and Brascamp-Lieb inequalities" and their discrete-cube
   work on the convolution conjecture), Eldan-Lehec-Shenfeld, Eldan-Kindler-Lifshitz-Minzer, "Talagrand's convolution
   conjecture" on the hypercube (2019-2026: is the cube case proved up to log log, or in full?), and the 2016-2026 citers of
   the prize list. Determine exactly what is proved for the biased-coin convolution on the cube (rate, uniformity in n,
   dependence on the bias). If the conjecture is proved in print, give the exact reference and theorem with page and stop with
   REPORT.md first line RESOLVED_IN_LITERATURE.
2. Understand the gap: explain why the Gaussian proofs (stochastic calculus / Follmer drift, pathwise analysis) do not
   transfer directly to the cube, and what the best cube bound is.
3. Prove what you can, with complete proofs: an o(1/t) bound for a natural class (f monotone, f low-degree, f depending on
   few coordinates with explicit dependence, symmetric f), or the log log rate on the cube if not in print, or a reduction of
   the cube problem to a quantitative Gaussian statement.
4. Compute (evidence only). For small n (up to 20), search numerically (exact computation over the cube) for f maximising
   t * lambda({f * mu >= t}) and record how the supremum behaves in t and n.
Write REPORT.md. Its first line is exactly one of PROVED, COUNTEREXAMPLE, PARTIAL, NO_PROGRESS, RESOLVED_IN_LITERATURE.
Then the statement, the proof, what was checked and how, and the literature result with exact theorem numbers and pages.
Keep LOG.md as you go. Code in code/, data in data/. Source texts may go in sources/ as plain text only; no PDFs kept, no
page images or scans of any paper or book anywhere in this folder. Work only in this directory. At most 4 threads, under
4 GB, nice 10. No publication anywhere, no pushes.

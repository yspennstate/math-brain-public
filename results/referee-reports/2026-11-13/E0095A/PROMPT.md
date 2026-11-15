Open problem E0095. Source: P. Diaconis, "Some things we have learned (about Markov chain Monte Carlo)", Bernoulli 19 (2013),
arXiv:1309.7754, Question 4, PDF p. 9: "One may ask the analogue of Question 3 for random walk on any graph: for a connected
d-regular graph on an even number n of vertices, which edge (or perfect matching) should be added to best speed up the
nearest-neighbour random walk?" Read Question 3 (adding edges/a matching to the cycle, the Chung-Diaconis-Graham and
Hermon-Lacoin-Peres type results on random matchings) and Question 4 exactly, including which speed measure is meant
(spectral gap, relaxation time, total variation mixing time, cutoff) and whether the walk is lazy.

Do this, in order, saving as you go:
1. Literature first. Download arXiv:1309.7754 into sources/ (plain text only). Search for later work: Hermon "Sensitivity of
   mixing times of Cayley graphs" and "adding a matching"; Hermon-Sly-Sousi "Universality of cutoff for graphs with an added
   random matching"; Krivelevich-Reichman-Samotij "smoothed analysis on connected graphs"; Boyd-Diaconis-Xiao "Fastest mixing
   Markov chain on a graph" and its edge-augmentation follow-ups; "spectral gap maximization by adding an edge" (Ghosh-Boyd
   "Growing well-connected graphs", Fiedler value / algebraic connectivity augmentation, Kim-Mesbahi); Ding-Peres
   "Sensitivity of mixing times"; Diaconis' own later papers. If the question is answered in print in a precise form, give the
   exact reference and theorem and stop with REPORT.md first line RESOLVED_IN_LITERATURE.
2. Make it precise. The question is open-ended; state two or three precise versions (for example: (A) for a single added edge,
   characterise the edge maximising the spectral gap of the simple random walk on the resulting graph, to first order in
   perturbation theory, via the Fiedler-type eigenvector; (B) how much can one added edge or one added perfect matching change
   the relaxation time or the TV mixing time of a d-regular graph, as a function of n and d, best and worst case; (C) for the
   cycle and the torus, which perfect matching is optimal). Note that adding an edge breaks regularity, so the stationary
   law changes; handle that.
3. Prove what you can. Give full proofs for the precise versions you can settle: e.g. a first-order perturbation formula and
   when the maximiser is the pair maximising |f(u) - f(v)| for the second eigenvector f (and counterexamples where this
   heuristic fails because of multiplicity or because second-order terms dominate); sharp bounds on how much one edge or one
   matching can improve the gap.
4. Compute. Exhaustively search small d-regular graphs (n up to 12-16 for d = 3, 4, using nauty geng if available, or your own
   generator) for the gap-maximising added edge and matching, compare against the eigenvector heuristic, and record every
   failure of the heuristic with exact certificates (rational or algebraic eigenvalue comparisons, or interval arithmetic).
Write REPORT.md. Its first line is exactly one of PROVED, COUNTEREXAMPLE, PARTIAL, NO_PROGRESS, RESOLVED_IN_LITERATURE.
Then the precise statements, the proofs, what was checked and how, and the literature result with exact theorem numbers and
pages. Keep LOG.md as you go. Code in code/, data in data/. Source texts may go in sources/ as plain text only; no PDFs kept,
no page images or scans of any paper or book anywhere in this folder. Work only in this directory. At most 4 threads, under
4 GB, nice 10. No publication anywhere, no pushes.

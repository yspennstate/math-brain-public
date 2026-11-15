Open problem D0031. Source: R. C. Bradley, "Basic properties of strong mixing conditions. A survey and some open questions",
Probability Surveys 2 (2005), 107-144, arXiv:math/0511078, Question 3, Section 2.6, PDF p. 11: "Does there exist a
nondegenerate strictly stationary, finite-state, rho-mixing, bilaterally deterministic sequence X = (X_k, k in Z)?"
(Bilaterally deterministic: X is measurable with respect to its double tail sigma-field, modulo null sets.)

Do this, in order, saving as you go:
1. Literature first. Download the survey into sources/, read Section 2.6 and the surrounding results (which mixing conditions
   are known to be compatible with bilateral determinism, and for which state spaces: Bradley's own constructions of rho-mixing
   bilaterally deterministic sequences with real or countable state space; Burton-Denker-Smorodinsky; Bradley's 1980s-2000s
   papers; Bradley's three-volume book "Introduction to Strong Mixing Conditions" 2007). Search 2005-2026 for an answer to
   Question 3 (finite state). If it is answered in print, give the exact reference and theorem and stop with REPORT.md first
   line RESOLVED_IN_LITERATURE.
2. Understand the obstruction: why the known constructions need infinitely many states (or why they do not), and which
   standard facts (e.g. rho-mixing plus finite state implies something about the double tail, entropy, Kolmogorov or
   Bernoulli properties) bear on the finite-state case. State precisely what is known.
3. Attempt a construction (e.g. a finite-state factor of a known rho-mixing bilaterally deterministic sequence, a coding of a
   suitable Gaussian or Markov-type process, block or tower constructions) or an impossibility proof. Prove every step; use
   code only to check computations (code/), never as a substitute for proof.
Write REPORT.md. Its first line is exactly one of PROVED, COUNTEREXAMPLE, PARTIAL, NO_PROGRESS, RESOLVED_IN_LITERATURE
(PROVED = a construction answering yes; COUNTEREXAMPLE = a proof that no such sequence exists; say which). Then the statement,
the proof, what was checked and how, and the literature result with exact references. Keep LOG.md as you go. Work only in this
directory. At most 4 threads, under 4 GB, nice 10. No publication anywhere, no pushes.

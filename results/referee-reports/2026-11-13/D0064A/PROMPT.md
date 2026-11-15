Open problem D0064. Source: R. Rhodes and V. Vargas, "Gaussian multiplicative chaos and applications: a review",
Probability Surveys 11 (2014), arXiv:1305.6221, Conjecture 6.4 (Solutions to the star-equation), Section 6.3, PDF p. 52:
classify the solutions M of the star-equation (star-scale invariance) by the parameters alpha and gamma: (1) alpha = 1 and
gamma^2 < 2d gives standard Gaussian multiplicative chaos; (2) alpha = 1 and gamma^2 = 2d gives the derivative martingale;
(3) alpha < 1 and gamma^2 < 2d gives an atomic chaos of the dual phase; (4) alpha < 1 and gamma^2 = 2d gives an atomic chaos
of the frozen phase. Read the source for the exact equation, the class of solutions considered (stationary random measures,
moment or non-degeneracy assumptions), and what is already classified (log-normal solutions).

Do this, in order, saving as you go:
1. Literature first. Get arXiv:1305.6221 into sources/ (plain text only) and read Section 6 exactly. Read Allez-Rhodes-Vargas
   "Lognormal star-scale invariant random measures" (PTRF 2013) and Rhodes-Sohier-Vargas "Levy multiplicative chaos and star
   scale invariant random measures" (Ann. Probab. 2014). Search for later work: Durand, Barral-Jin-Rhodes-Vargas "Gaussian
   multiplicative chaos and KPZ duality" (atomic dual chaos), Madaule-Rhodes-Vargas (critical / frozen phase), Duplantier-
   Rhodes-Sheffield-Vargas (derivative martingale and its uniqueness), Barral-Kupiainen-Nikula-Saksman-Webb, Junnila-Saksman
   (uniqueness of critical chaos), Powell "Critical Gaussian chaos: convergence and uniqueness", Biermé-Durand, Liu's
   fixed points of the smoothing transform (the one-dimensional cascade analogue: Durrett-Liggett, Alsmeyer-Biggins-Meiners
   classify all fixed points of the smoothing transform), and 2014-2026 work citing the star-equation. If the conjecture is
   answered in print, give the exact reference and theorem and stop with REPORT.md first line RESOLVED_IN_LITERATURE.
2. Reduce. Explain the analogy with fixed points of the smoothing transform (where the classification is complete) and which
   step of that classification has no continuous analogue yet.
3. Prove what you can, with complete proofs: one of the four cases in full generality; or the classification under a
   moment assumption beyond log-normality; or for a restricted class (solutions that are Levy chaos, or solutions with a
   given small-scale decomposition); or a counterexample to the stated dichotomy.
4. Compute (evidence only, modest). Simulate a discrete cascade analogue and check numerically which fixed points the
   iteration reaches for parameters in each of the four regimes.
Write REPORT.md. Its first line is exactly one of PROVED, COUNTEREXAMPLE, PARTIAL, NO_PROGRESS, RESOLVED_IN_LITERATURE.
Then the statement, the proof, what was checked and how, and the literature result with exact theorem numbers and pages.
Keep LOG.md as you go. Code in code/, data in data/. Source texts may go in sources/ as plain text only; no PDFs kept, no
page images or scans of any paper or book anywhere in this folder. Work only in this directory. At most 4 threads, under
4 GB, nice 10. No publication anywhere, no pushes.

Open problem D0065. Source: R. Rhodes and V. Vargas, "Gaussian multiplicative chaos and applications: a review" (Probability
Surveys 11 (2014); arXiv:1305.6221), Conjecture 6.5, Section 6.4, PDF p. 53: for a cutoff approximation X_n of a log-correlated
Gaussian field on [0,1]^d, sup_x X_n(x) - sqrt(2d) c_n + (3/(2 sqrt(2d))) ln c_n converges in law to a random variable G_d with
E[exp(-q G_d)] = c^{-q} Gamma(1 + q/sqrt(2d)) E[M'([0,1]^d)^{-q/sqrt(2d)}], M' the derivative martingale (critical chaos). The same
is expected for the discrete Gaussian free field on graphs with mesh going to zero. Read the source for the exact wording (which
cutoff approximations, which c_n, the normalisation of the field and of M').

Do this, in order, saving as you go:
1. Literature first (this one is likely settled in print). Get arXiv:1305.6221 into sources/ (plain text only) and state
   Conjecture 6.5 exactly. Then check, with exact theorem numbers and pages: Madaule ("Maximum of a log-correlated Gaussian field",
   AIHP 2015, star-scale invariant kernels), Ding-Roy-Zeitouni ("Convergence of the centered maximum of log-correlated Gaussian
   fields", Ann. Probab. 2017), Bramson-Ding-Zeitouni (2D DGFF maximum, CPAM 2016), Biskup-Louidor (DGFF extremes, derivative
   martingale representation), Acosta, Duplantier-Rhodes-Sheffield-Vargas (critical chaos, derivative martingale), Junnila-Saksman,
   Schweiger-Zeitouni, Ding-Gwynne-Wirth, and 2014-2026 work on "centered maximum log-correlated". For each: which fields, which
   dimensions, convergence in law yes/no, is the limit a randomly shifted Gumbel with shift given by the derivative martingale (and
   does that match the Laplace transform in the conjecture, including Gamma(1 + q/sqrt(2d))).
2. Decide exactly what is proved: the conjecture as stated (all d, the cutoff class of the review), a subclass, or a different
   normalisation. Check by hand that "Gumbel shifted by (1/sqrt(2d)) log(c M')" has Laplace transform
   c^{-q} Gamma(1 + q/sqrt(2d)) E[M'^{-q/sqrt(2d)}] (sign conventions, which Gumbel: max or min).
   If a printed theorem covers the conjecture, stop with RESOLVED_IN_LITERATURE and state precisely for which fields and d, and what
   (if anything) remains open (e.g. general cutoffs, non-star-scale kernels, the DGFF on general graphs).
3. If something remains open, prove what you can with complete proofs (for instance the Laplace transform identity in step 2, or
   the extension from the printed class to the review's cutoff class), or state clearly the gap.
4. Compute (evidence only, small): simulate a branching random walk / star-scale field in d = 1, 2 and compare the centered maximum
   with the shifted-Gumbel prediction.
Write REPORT.md. Its first line is exactly one of PROVED, COUNTEREXAMPLE, PARTIAL, NO_PROGRESS, RESOLVED_IN_LITERATURE.
Then the statement, the proof, what was checked and how, and the literature result with exact theorem numbers and pages.
Keep LOG.md as you go. Code in code/, data in data/. Source texts may go in sources/ as plain text only; no PDFs kept, no
page images or scans of any paper or book anywhere in this folder. Work only in this directory. At most 4 threads, under
4 GB, nice 10. No publication anywhere, no pushes.

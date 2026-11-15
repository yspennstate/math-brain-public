Open problem F0136. Source: C. Sabot and L. Tournier, "Random walks in Dirichlet environment: an overview" (2016),
arXiv:1601.08219, Section 4, PDF p. 11 (the sentence after Proposition 2) and Remark 7, PDF p. 17: for the random walk in
Dirichlet environment (RWDE) on Z^d with weights alpha_1, ..., alpha_{2d}, drift d_alpha = sum alpha_i e_i and
kappa = 2 sum alpha_i - max_{i<=d} (alpha_i + alpha_{i+d}), Theorem 5 shows that kappa <= 1 is sharp for ballisticity when
d >= 3: if d_alpha != 0 and kappa > 1 then X_n/n -> v != 0. Conjecture: the same holds in dimension d = 2. Read the source for
the exact statement, the annealed and quenched laws, Theorem 1 (directional transience, asymptotic direction), Proposition 2
and Theorem 5, and how the d >= 3 proof works.

Do this, in order, saving as you go:
1. Literature first. Get arXiv:1601.08219 into sources/ (plain text only) and read Sections 2-5. Read the d >= 3 proof
   (Bouchet "Sub-ballistic random walk in Dirichlet environment" and Sabot "Random Dirichlet environment viewed from the
   particle in dimension d >= 3", Ann. Probab. 2013, which uses transience of the walk in d >= 3 to build the invariant
   measure for the environment seen from the particle). Search for d = 2 progress: Bouchet-Sabot-dos Santos, Tournier
   "Integrability of exit times and ballisticity for random walks in Dirichlet environment", Enriquez-Sabot ballisticity
   criteria, Sznitman (T) and (T') conditions, Berger-Drewitz-Ramirez "effective polynomial ballisticity", Guerra-Ramirez,
   Fribergh-Kious, Campos-Ramirez for non-uniformly elliptic RWRE, and 2016-2026 work citing 1601.08219. If it is answered in
   print, give the exact reference and theorem and stop with REPORT.md first line RESOLVED_IN_LITERATURE.
2. Understand the gap. Explain exactly where d >= 3 is used (the walk on the 'time-reversed' environment, Green function
   bounds, transience of a symmetrised walk) and what fails in d = 2.
3. Prove what you can, with complete proofs: the conjecture; or ballisticity in d = 2 for kappa above a larger explicit
   threshold, or under an extra condition on alpha (strong drift, a dominant direction, (T') for kappa large); or the
   existence of the invariant measure for the environment from the particle in d = 2 when kappa > 1; or integrability of
   regeneration times in d = 2 for kappa > K. A precise reduction is worth writing up.
4. Compute (evidence only). Simulate RWDE on Z^2 for several alpha with kappa slightly above 1 and well above 1, measure
   X_n/n and the tail of the time spent in finite traps, and compare with kappa <= 1.
Write REPORT.md. Its first line is exactly one of PROVED, COUNTEREXAMPLE, PARTIAL, NO_PROGRESS, RESOLVED_IN_LITERATURE.
Then the statement, the proof, what was checked and how, and the literature result with exact theorem numbers and pages.
Keep LOG.md as you go. Code in code/, data in data/. Source texts may go in sources/ as plain text only; no PDFs kept, no
page images or scans of any paper or book anywhere in this folder. Work only in this directory. At most 4 threads, under
4 GB, nice 10. No publication anywhere, no pushes.

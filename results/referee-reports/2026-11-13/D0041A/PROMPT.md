Open problem D0041. Source: B. Virag, "Operator limits of random matrices" (ICM 2014 proceedings; arXiv:1804.06953 or find it
by author and title), Problem 3 (Mo's formulas), PDF p. 12: find a way to check that Mo's formulas satisfy equation (10) of the
source, the identity that characterises the edge limit through the corresponding stochastic operator (a PDE / diffusion
characterisation of the distribution function, as in Bloemendal-Virag). Rumanov found a new Painleve representation using the
stochastic operator; the bulk analogue is unknown (Question 9). Read the source for the exact wording: which edge (soft or hard),
which beta, which formulas of Mo (M. Y. Mo, "The rank 1 real Wishart spiked model" / Tracy-Widom beta formulas for even beta, or
another Mo paper: identify it exactly), and what equation (10) is.

Do this, in order, saving as you go:
1. Literature first. Get the source into sources/ (plain text only) and read the section around Problem 3 and equation (10).
   Identify Mo's formulas exactly (paper, theorem, page). Search: Bloemendal-Virag ("Limits of spiked random matrices" I and II),
   Rumanov ("Classical integrability for beta-ensembles and general Fokker-Planck equations", "Painleve representation of
   Tracy-Widom beta distribution for beta = 6", hard-edge papers), Ramirez-Rider-Virag, Ramirez-Rider (stochastic Bessel
   operator), Grava-Its-Kapaev-Mezzadri, Forrester (beta = 4, 6 formulas), Dumaz-Virag, Wang (spiked hard edge), and 2014-2026
   work. If a printed paper already verifies Mo's formulas against (10), give the theorem and page and stop with
   RESOLVED_IN_LITERATURE.
2. Understand the gap: write (10) with its boundary conditions and the uniqueness statement that makes it characterise the
   distribution; write Mo's formulas in the same variables; explain what makes direct substitution hard (Painleve
   transcendents, Riemann-Hilbert data, the extra spike/time variable).
3. Prove what you can, with complete proofs: a verification for the beta values Mo covers (for instance beta = 2 and 4, or the
   even beta in Mo), by showing Mo's function solves (10) and meets the boundary conditions, using the Painleve equations and
   known asymptotics; or a reduction of the check to a finite list of identities, each proved or proved symbolically.
4. Compute (evidence only): solve (10) numerically (finite differences or method of lines) and evaluate Mo's formulas
   numerically (Painleve ODE integration with the right boundary behaviour), and compare at many points, for each beta covered.
Write REPORT.md. Its first line is exactly one of PROVED, COUNTEREXAMPLE, PARTIAL, NO_PROGRESS, RESOLVED_IN_LITERATURE.
Then the statement, the proof, what was checked and how, and the literature result with exact theorem numbers and pages.
Keep LOG.md as you go. Code in code/, data in data/. Source texts may go in sources/ as plain text only; no PDFs kept, no
page images or scans of any paper or book anywhere in this folder. Work only in this directory. At most 4 threads, under
4 GB, nice 10. No publication anywhere, no pushes.

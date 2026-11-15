Open problem D0046. Source: B. Virag, "Operator limits of random matrices" (ICM 2014 proceedings; arXiv:1804.06953),
Question 8 (Dynamics), PDF p. 25: are there operator limits of matrix-valued (say Hermitian) Brownian motion, that is a dynamical
analogue of the stochastic Airy and Sine_beta operators describing the evolution in time of the limiting spectral objects? Read
the source for the exact wording and what Virag means by an operator limit (a random operator-valued process whose spectrum at
each time is the limiting point process, with the right joint law in time).

Prior internal work to reuse (internal only, never cite publicly): our runs D0040 (nested beta ensembles, Question 2 of the same
paper; the Laguerre/Jacobi tridiagonal nesting) and D0043 (higher-order edge operators). Their folders are not available here.

Do this, in order, saving as you go:
1. Literature first. Get arXiv:1804.06953 into sources/ (plain text only). State Question 8 exactly. Search: Allez-Guionnet
   (beta-Dyson Brownian motion tridiagonal models), Allez-Dumaz (tridiagonal "Brownian" dynamics, random matrices in non-confining
   potentials, Sine_beta in time), Holcomb-Valko, Valko-Virag (Brownian carousel, operator level Sine_beta, "The many faces of the
   stochastic zeta function"), Corwin-Hammond (Airy line ensemble), Osada-Tanemura (infinite-dimensional SDEs for Airy and Sine
   processes, dynamical Sine_beta), Tsai (Dyson BM infinite particle), Landon-Sosoe, Gorin-Kleptsyn ("Universal objects of the
   infinite beta random matrix theory"), Edelman, Bloemendal, Li-Valko, and 2014-2026 work on "dynamical stochastic Airy operator",
   "operator-valued process", "Dyson Brownian motion operator limit". If a printed theorem gives an operator-valued process limit
   of Hermitian Brownian motion (any beta) at the edge or in the bulk, give the theorem and page and stop with
   RESOLVED_IN_LITERATURE, stating which regime.
2. Understand: write down why the static tridiagonal approach does not directly give dynamics (the Dumitriu-Edelman tridiagonal
   form of H_t is not a Markov process in t with a nice local form), and which partial routes exist (stationary tridiagonal
   dynamics with the right one-time law; Allez-Guionnet's matrix dynamics; Dyson BM as an SDE for eigenvalues only).
3. Prove what you can, with complete proofs: for example (a) a tridiagonal Markov dynamics with GbetaE stationary law whose edge
   scaling converges (as processes, in a norm-resolvent or form sense at each fixed time, with tightness in time) to a stationary
   stochastic-Airy-operator-valued process, identifying the limit as an operator SDE; or (b) a precise obstruction: show that a
   natural candidate cannot have the Airy line ensemble / Dyson BM edge limit as its spectral process (compare two-time
   correlations), which says what an answer must look like.
4. Compute (evidence only): simulate Hermitian Brownian motion (n up to a few thousand) and any proposed tridiagonal dynamics,
   compare two-time correlations of the top eigenvalues after edge scaling.
Write REPORT.md. Its first line is exactly one of PROVED, COUNTEREXAMPLE, PARTIAL, NO_PROGRESS, RESOLVED_IN_LITERATURE.
Then the statement, the proof, what was checked and how, and the literature result with exact theorem numbers and pages.
Keep LOG.md as you go. Code in code/, data in data/. Source texts may go in sources/ as plain text only; no PDFs kept, no
page images or scans of any paper or book anywhere in this folder. Work only in this directory. At most 4 threads, under
4 GB, nice 10. No publication anywhere, no pushes.

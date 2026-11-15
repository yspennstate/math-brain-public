Open problem F0017. Source: V. H. Vu, "Recent progress in combinatorial random matrix theory" (Probability Surveys 2021,
arXiv:2005.02797), Conjecture 11.6 (Local resilience), Section 11, PDF p. 17: call an n x n {-1,1} matrix M stubborn if all
2^n matrices obtained from M by switching the signs of any subset of the diagonal entries are non-singular. Conjecture: a
uniformly random {-1,1} matrix M_n is stubborn with probability 1 - o(1). Read the source for the exact statement and the
surrounding resilience results (how many entries an adversary must change to make M_n singular).

Do this, in order, saving as you go:
1. Literature first. Get arXiv:2005.02797 into sources/ (plain text only) and read Section 11 exactly. Search for anything
   later: Bourgain-Vu-Wood, Tikhomirov "Singularity of random Bernoulli matrices" (Ann. Math. 2020, P(singular) = (1/2+o(1))^n),
   Jain-Sah-Sawhney (singularity of random symmetric and sparse matrices, "sharp invertibility"), Ferber-Jain-Luh-Samotij
   ("On the counting problem in inverse Littlewood-Offord theory", resilience of singularity), Bandeira-Ferber-Kwan
   ("Resilience for the Littlewood-Offord problem"), Campos-Jenssen-Michelen-Sahasrabudhe, Nguyen on permanent/determinant
   anti-concentration, and 2021-2026 work citing Vu's Conjecture 11.6 or using the words "stubborn" or "diagonal resilience".
   If it is answered in print, give the exact reference and theorem and stop with REPORT.md first line RESOLVED_IN_LITERATURE.
2. Understand the difficulty. det(M) is multilinear in the diagonal entries, so the 2^n switched determinants are the values of
   a multilinear polynomial in the diagonal signs, whose coefficients are the principal minors of the off-diagonal part. A
   union bound with Tikhomirov's estimate gives 2^n (1/2+o(1))^n, which does not go to zero. Explain what anti-concentration
   statement about this multilinear polynomial (a polynomial Littlewood-Offord problem in the diagonal signs, with random
   coefficients) would prove the conjecture, and what Meka-Nguyen-Vu / Razborov-Viola / Kwan-Sauermann polynomial
   anti-concentration gives.
3. Prove what you can, with complete proofs: the conjecture; or stubbornness against all switchings of at most k diagonal
   entries for k = o(n) or k = cn; or a weaker probability bound (stubborn with probability bounded away from 0); or a
   counterexample (show P(stubborn) does not tend to 1, for instance by a second-moment count of singular switchings caused by
   a structured event such as two rows agreeing off the diagonal in a way the diagonal cannot repair).
4. Compute. Exhaustively for n <= 5 or 6 and by Monte Carlo for n up to about 24 (exact integer determinants, 2^n switchings
   via a Gray-code rank-one update or the multilinear expansion), estimate P(stubborn) and the distribution of the number of
   singular switchings; fit the trend and say which way it points.
Write REPORT.md. Its first line is exactly one of PROVED, COUNTEREXAMPLE, PARTIAL, NO_PROGRESS, RESOLVED_IN_LITERATURE.
Then the statement, the proof, what was checked and how, and the literature result with exact theorem numbers and pages.
Keep LOG.md as you go. Code in code/, data in data/. Source texts may go in sources/ as plain text only; no PDFs kept, no
page images or scans of any paper or book anywhere in this folder. Work only in this directory. At most 4 threads, under
4 GB, nice 10. No publication anywhere, no pushes.

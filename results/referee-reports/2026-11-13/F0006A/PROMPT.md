Open problem F0006. Source: V. Vu, "Recent progress in combinatorial random matrix theory", Probability Surveys (2021),
arXiv:2005.02797, Conjecture 6.8 (Determinant), Section 6: "For any x != 0, P(det M_n = x) <= n^{-(1/2+o(1))n}", M_n the
n x n i.i.d. Rademacher (+-1) matrix. The source adds that the best known upper bound is exponential and that even the much
weaker statement "the support of det M_n has super-exponential size" is not known.

Do this, in order, saving as you go:
1. Literature first. Download arXiv:2005.02797 into sources/ and read Section 6. Search for later work (2020-2026) on
   (a) P(det M_n = x) for fixed or growing nonzero x, (b) the number of distinct determinants of n x n +-1 or 0/1 matrices
   (the "determinant spectrum": Craigen, Orrick, Shah, Zivkovic, Brent-Orrick-Osborn-Zimmermann, and any newer paper),
   (c) local limit theorems for det M_n (Tao-Vu, Nguyen-Vu "Random matrices: law of the determinant", Jain-Sah-Sawhney,
   Nguyen-Wood cokernel results). If either the conjecture or the weaker support statement is already settled in print,
   say so with the exact reference and theorem, and stop with REPORT.md first line RESOLVED_IN_LITERATURE.
2. The weaker statement. Try to prove that |{det M : M in {+-1}^{n x n}}| >= n^{c n} for some c > 0 and all large n (or
   at least exp(omega(n))). Note det of an n x n +-1 matrix is 2^{n-1} times the determinant of an (n-1) x (n-1) 0/1
   matrix, so this is the same as counting distinct 0/1 determinants. Try explicit constructions (block/Schur-complement
   gluing with +-1 entries everywhere, bordered matrices, Kronecker/tensor products, matrices whose determinant factors
   as a product of independently chosen pieces) and counting arguments. Check every construction by exact integer
   determinants (sympy/fraction-free Bareiss) for small n, and compute the exact spectrum size for n <= 7 or 8 (known
   values exist in OEIS - find and cite the sequence) to see the growth rate.
3. The conjecture itself. Record what the standard reduction (det = X . v with v the cofactor vector of the first n-1 rows,
   then Littlewood-Offord) gives, and whether any improvement over (1/2+o(1))^n for P(det M_n = x) at fixed x != 0 is
   provable, e.g. by using two rows, or by the 2^{n-1} divisibility plus Nguyen-Wood cokernel statistics. Compute
   P(det M_n = 2^{n-1} k) exactly for small n by enumeration or exact dynamic programming over rows (n <= 6 exact; larger n
   by Monte Carlo with error bars), and compare with n^{-n/2}.
Write REPORT.md. Its first line is exactly one of PROVED, COUNTEREXAMPLE, PARTIAL, NO_PROGRESS, RESOLVED_IN_LITERATURE
(PROVED means the full Conjecture 6.8; if you prove only the weaker super-exponential support statement, write PARTIAL and
say on line 2 "SUPPORT_PROVED" with the bound). Then the statement, the proof, what was checked and how, and the literature
result. Keep LOG.md as you go. Code in code/, data in data/. Work only in this directory. At most 4 threads, under 4 GB,
nice 10. No publication anywhere, no pushes.

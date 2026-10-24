# Quadratic forms with five large eigenvalues have bounded densities

Theorem 1.1. Let X_1, ..., X_n be independent real random variables with densities bounded by K, let A be a real
symmetric matrix with at least five eigenvalues of modulus at least s > 0 (that is, s_5(A) >= s), and let b, c be
arbitrary. Then Q = X^T A X + b^T X + c has a density bounded by 270 K^2 / s.

Theorem 1.2. If A has at least three eigenvalues of modulus at least s, then E|Q - a|^{-1/2} <= 77 K / sqrt(s) for
every real a.

The bounds are uniform in n, in the other eigenvalues, in b and c, and in the laws of the X_i; no moment,
smoothness, support or identical-distribution assumption is made. Every larger multiplicity (s_9(A) >= s,
s_17(A) >= s, ...) is a special case. Three large eigenvalues are necessary for a density bound; whether three or
four suffice is open.

## Files

- `paper.tex`, `paper.pdf`: the paper (16 pages), self-contained, every lemma proved in the text.
- `AUDIT.md`: statement-by-statement audit record, with the Lean theorem and the numerical check attached to each
  statement, the findings made during the audit, and the strongest case against the result.
- `lean/QformFive.lean` (17 theorems): every numerical constant of Sections 6 and 7 and of Remark 8.2.
- `lean/QformFive2.lean` (13 theorems): the random sign argument of Section 6 - the identity A - DAD = 2C, the
  fourth moment of independent signs, the second moment of the sign chaos as an exact sum over all 2^n sign vectors,
  the Frobenius identity and bound of Lemma 6.3, and the existence of a sign vector at or below the average.
- `lean/QformFive3.lean` (70 theorems): Proposition 6.4 in full. It repeats the sign lemma of `QformFive2.lean`,
  proves for approximation numbers the facts of Lemma 2.5 that the proposition uses (compression, the Weyl step) and
  the inequality s_m(A_{I,J}) >= s_{2m-1}(C) of Lemma 6.2(b), and joins both ends to Mathlib's spectral theorem:
  `prop64_spectral_m3` says that a real symmetric A without a pivot and with at least five eigenvalues of modulus at
  least one has a partition with E_3(A_{I,J}) = e_3(A_{I,J} A_{I,J}^T) >= 0.09^6 (and likewise m = 2, 1).
- `lean/*_run.lean`, `lean/run_five1.log`, `lean/run_five2.log`, `lean/run_five3.log`: the files with
  `#print axioms` appended and the compiler output; every theorem depends only on propext, Classical.choice and
  Quot.sound.
- `lean/shared/`: the Lean checks of Sections 2-5, which are the same as in the nine-eigenvalue paper.
- `checks/constants_exact.py` and `.log`: the 41 numerical claims at 50 digits.
- `checks/decoupling_check.py`: the identities of Lemma 6.2 and the exact mean of Lemma 6.3 against Monte Carlo on
  Wigner matrices, stars, a hub with trigonometric leaves and low-rank matrices.
- `checks/verify_five.py` and `.log`: Proposition 6.4 on random and structured matrices without pivots, the example
  of Remark 8.2, and Monte Carlo densities for Theorem 1.1.
- `checks/two_star_affine.py` and `.log`: the two-star example of Remark 8.2 with affine terms (density at most
  4 sqrt(e) for every b and c), on centred coordinates, including the directions where the bound is tightest.
- `checks/constants_opt.py`: the choice of the pivot thresholds eta = 1/12, zeta = 1/256.

## Build and check

    pdflatex paper.tex   (three passes)
    python checks/constants_exact.py
    python checks/decoupling_check.py
    python checks/verify_five.py
    python checks/two_star_affine.py
    lake env lean lean/QformFive.lean ; lake env lean lean/QformFive2.lean ; lake env lean lean/QformFive3.lean
    (Lean 4.29.1 with Mathlib 5e932f97)

## Structure of the proof

After scaling, K = s = 1. With eta = 1/12 and zeta = 1/256, a pivot is a diagonal entry of modulus at least eta or a
principal 2x2 minor of modulus at least zeta. Without a pivot every off-diagonal entry has modulus below
a_0 = 5/48, since eta^2 + zeta = (5/48)^2.

1. Theorem 4.1 (Fourier decay from crossing volumes): for a partition [n] = I u J and M = A_{I,J},
   |E e^{itQ}|^2 <= (sqrt2 pi e)^l (l^l/l!)^{1/2} E_l(M)^{-1/2} |t|^{-l}, where E_l(M) = e_l(M M^T). Order three
   gives a density bound, order two a negative half moment, order one a logarithmic moment.
2. Proposition 6.4 (random signs): if A has no pivot and s_{2m-1}(A) >= 1, m <= 3, then some partition has
   s_m(A_{I,J}) > (44 - 5 sqrt2 (2m - 1))/96. With D = diag(eps) for a sign vector eps, A - DAD is twice the
   off-diagonal block part C; compressing to 2m - 1 eigenvectors of A leaves Lambda - Phi^T diag(A) Phi - Q_eps with
   E ||Q_eps||_F^2 <= 2 a_0^2 (2m - 1)^2, and C has the singular values of A_{I,J}, each twice.
3. Pivots: a diagonal pivot leaves four large eigenvalues in the Schur complement, and Theorem 1.2 controls the
   square-root singularity; a definite pair gives a bounded density directly; an indefinite pair gives a logarithmic
   singularity at a random point, controlled by the logarithmic moment of the Schur complement.

The number five enters only through Proposition 6.4 with m = 3. Two disjoint stars have four eigenvalues of modulus
one, no pivot, and every off-diagonal block of rank at most two (Remark 8.2), so this argument cannot go below five;
their density is nevertheless at most 4 sqrt(e) for every b and c.

# Quadratic forms with nine large eigenvalues have bounded densities

Theorem. Let X_1, ..., X_n be independent real random variables with densities bounded by K, let A be a real
symmetric matrix with at least nine eigenvalues of modulus at least s > 0 (that is, s_9(A) >= s), and let b, c be
arbitrary. Then Q = X^T A X + b^T X + c has a density bounded by 400 K^2 / s.

The bound is uniform in n, in the other eigenvalues, in b and c, and in the laws of the X_i; no moment, smoothness,
support or identical-distribution assumption is made. Any larger multiplicity (s_17(A) >= s, s_33(A) >= s, ...) is a
special case. Three large eigenvalues are necessary; whether three suffice is open.

## Files

- `paper.tex`, `paper.pdf`: the paper (15 pages), self-contained, every lemma proved in the text.
- `AUDIT.md`: statement-by-statement audit record, with the numerical test and the Lean theorem attached to each
  statement.
- `checks/verify.py`: numerical checks of every constant (50-digit arithmetic) and of every lemma and theorem
  (quadrature, exact enumeration, Monte Carlo). `checks/verify_v2.log` and `checks/results_v2.json` are the full run
  with `--skip-t1`. The end-to-end test of Theorem 1.1 is `checks/t1_tight.py` (every coordinate uniform, density
  exactly 1, on adversarial structures), recorded in `checks/t1_tight.log` and `checks/results_t1_tight.json`.
  `checks/remark83.py` and `checks/results_remark83.json` check the example of Remark 8.3.
- `lean/QformNine.lean` ... `lean/QformNine5.lean`: Lean 4 / Mathlib proofs of the numerical constants, the elementary
  inequalities, the finite algebraic and combinatorial steps (including the entropy inequality of Lemma 4.2), the
  integral identities and the antiderivatives behind Lemmas 5.5 and 5.6; `lean/axioms_*.log` holds the
  `#print axioms` output (propext, Classical.choice, Quot.sound only). What is not formalized, and why, is listed in
  `AUDIT.md`.

## Build and check

    pdflatex paper.tex   (three passes)
    python checks/verify.py --skip-t1 --out checks/results.json
    python checks/t1_tight.py 2000000
    lake env lean lean/QformNine.lean   (and QformNine2-5; inside any Lean 4.29 project with Mathlib)

## Structure of the proof

After scaling, K = s = 1. With eta = 3/40 and zeta = 1/400, a pivot is a diagonal entry of modulus at least eta or a
principal 2x2 minor of modulus at least zeta.

1. Theorem 4.1 (Fourier decay from crossing volumes): for a partition [n] = I u J and M = A_{I,J},
   |E e^{itQ}|^2 <= (sqrt2 pi e)^l (l^l/l!)^{1/2} E_l(M)^{-1/2} |t|^{-l}, where E_l(M) = e_l(M M^T) is the sum of
   the squared l x l minors of M. The proof decouples the two blocks, applies Hoelder over l-sets of rows weighted
   by their Gram determinants, and bounds projections of product densities through the geometric Brascamp-Lieb
   inequality; a row carrying more than half of the weight is integrated by Plancherel instead.
2. Proposition 6.4: without pivots, s_{4k-3}(A) >= 1 forces V_k(A) >= (4/625)^k for the sum V_k of squared
   determinants of k x k minors with disjoint row and column sets (k <= 3). A random partition transfers this to
   E_k(A_{I,J}).
3. Without pivots: order 3 gives the density bound 25 C_3 < 375. With a pivot: conditioning on the other
   coordinates leaves a square-root or logarithmic singularity at a quadratic polynomial whose matrix is a Schur
   complement; Proposition 7.2 bounds the negative half moment (by 82 when five eigenvalues of modulus at least one
   remain), using order 2 without pivots, Lemma 5.6 for pairs, and the logarithmic moment of Lemma 5.4 (order 1)
   for a diagonal pivot.

The threshold nine is used only in the case without pivots, through Proposition 6.4 at order three.

## Relation to the other records here

`../fixed-multiplicity-2026-09-24/` holds the 17-eigenvalue manuscript and its reviews; its Sections 5 and 6 (pivots
and disjoint minors) are the basis of Sections 5 and 6 here. The order-three and order-two estimates behind the
nine-eigenvalue threshold also appear, with other constants, in the reviews and improvements filed there under
`improvements/*/B04`, `improvements/account01/B07`, `improvements/account02/B09`, `B10` and `B18`; the separate
thresholds 3/40 and 1/400 and the two-coordinate half potential are those of
`improvements/interactive/20260924T145418Z-nine-400/`.

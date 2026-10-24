# Audit of "Quadratic forms with five large eigenvalues have bounded densities"

Paper: `paper.tex` / `paper.pdf` (16 pages, 25 September 2026).
Result: if the real symmetric matrix A has at least five eigenvalues of modulus at least s, then
Q = X^T A X + b^T X + c has a density at most 270 K^2/s, for independent coordinates with densities at most K.
Under three such eigenvalues, E|Q - a|^{-1/2} <= 77 K / sqrt(s) for every a.

Every statement was checked in three independent ways where the statement allows it: a line-by-line reading
against its proof, a Lean 4 / Mathlib proof (files in `lean/`, compiled with `#print axioms`, which reports only
`propext`, `Classical.choice`, `Quot.sound` for every theorem, so none uses `sorry`), and numerical tests
(`checks/`). Proposition 6.4 is checked in Lean in full, from the hypothesis N_A(1) >= 2m - 1 on Mathlib's
eigenvalues of A to the conclusion E_m(A_{I,J}) = e_m(A_{I,J} A_{I,J}^T) >= gamma^{2m} (`lean/QformFive3.lean`). The
spectral facts it uses (the compression inequality and the Weyl step of Lemma 2.5, and s_m(A_{I,J}) >= s_{2m-1}(C)
from Lemma 6.2(b)) are proved there for approximation numbers, the form in which the proof of Lemma 2.5 states them,
and joined to eigenvalues through Mathlib's spectral theorem. Sections 2 to 5 and the case analysis of Section 7 are
checked in Lean only in their constants and finite steps.

## What is new relative to the nine-eigenvalue argument

Sections 2 to 5 (Fourier analysis, projections of product densities, Theorem 4.1, the one- and two-coordinate
estimates) are unchanged. Section 6 replaces the disjoint-minor sampling argument, which needed 4k - 3 eigenvalues
for a lower bound on the k-th crossing volume, by a random sign argument that needs 2m - 1 eigenvalues for m
singular values of an off-diagonal block:

* flipping the signs of a random set of coordinates, D = diag(eps), gives A - DAD = 2C, where C is the
  off-diagonal block part of A for the partition into {eps = 1} and {eps = -1};
* compressed to 2m - 1 orthonormal eigenvectors with |lambda| >= 1, this reads
  2 Phi^T C Phi = Lambda - Phi^T diag(A) Phi - Q_eps, where the chaos Q_eps has mean square at most
  2 a^2 (2m - 1)^2 when every off-diagonal entry has modulus at most a;
* C has the singular values of A_{I,J}, each twice, so s_{2m-1}(C) = s_m(A_{I,J}).

Without a pivot, a < 5/48, and for 2m - 1 <= 5 this gives s_m(A_{I,J}) > (44 - 5 sqrt2 (2m - 1))/96 > 0 for some
partition. With m = 3 the order-three receiver of Corollary 4.4 bounds the density; with m = 2 the order-two
receiver bounds the negative half moment under three eigenvalues, which the diagonal-pivot branch needs after one
eigenvalue is lost to the Schur complement. The count five is sharp for this route: two disjoint stars have four
eigenvalues of modulus one, no pivot, and every off-diagonal block of rank at most two (Remark 8.2).

## Statement-by-statement record

| Statement | Reading | Lean | Numerics |
|---|---|---|---|
| (6.1)-(6.2): eta^2 + zeta = (5/48)^2 | checked | `QformFive.small_entry_bound` | `constants_exact.py` |
| Lemma 2.5, compression s_j(U^T T V) <= s_j(T), in the form used (U = V with orthonormal columns) | checked (rank argument) | `QformFive.approx_compress` (with `exists_ker`, `nrm_transpose_mulVec_le`, `nsq_mulVec_orth`) | `decoupling_check.py` (lbslack) |
| Lemma 2.5, Weyl step s_k(T - E) >= s_k(T) - norm(E) as used in Prop. 6.4 | checked | `QformFive.compressed_lower` (with `nrm_sub_sub_ge`, `nsq_mulVec_le`, `nrm_diagonal_mulVec_le`) | `verify_five.py` |
| Lemma 2.5, characterization s_k = distance to rank < k, direction used at the end of Prop. 6.4 | checked | `QformFive.card_eig_of_approx` (via Mathlib's spectral theorem) | - |
| Lemma 6.2(a), A - DAD = 2C | checked | `QformFive.sign_identity`, `sign_identity_matrix` | `decoupling_check.py` (id1 = 0) |
| Lemma 6.2(b), s_{2m-1}(C) = s_m(A_{I,J}) | checked (explicit eigenvectors) | direction used, s_m(A_{I,J}) >= s_{2m-1}(C): `QformFive.approx_of_dil`, `offBlock_submatrix`, `rank_dil_le` | `decoupling_check.py` (sv <= 8e-15) |
| Lemma 6.3, fourth moment of signs | checked | `QformFive.fourth_moment` (exact sum over all 2^n sign vectors) | Monte Carlo in `decoupling_check.py` |
| Lemma 6.3, identity for E ||Q_eps||_F^2 | checked | `QformFive.chaos_second_moment`, `frobenius_moment` | exact vs Monte Carlo agree |
| Lemma 6.3, bound 2 a^2 (sum |phi_i|^2)^2 | checked | `QformFive.frobenius_bound` | - |
| Prop. 6.4, existence of good signs | checked | `QformFive.exists_le_average`, `exists_good_signs` | `verify_five.py` |
| Prop. 6.4, (1 - eta - sqrt2 a_0 k)/2 = gamma_m and gamma bounds | checked | `gamma_identity`, `gamma_bounds`, `gamma_rational`, `sqrt_two_lt` | `constants_exact.py` |
| Prop. 6.4, the eigenvector frame from s_{2m-1}(A) >= 1 | checked | `QformFive.eigenframe` (Mathlib's `eigenvectorUnitary`) | - |
| Prop. 6.4, identity 2 Phi^T C Phi = Lambda - Phi^T Delta Phi - Q_eps | checked | `QformFive.compressed_identity` | `decoupling_check.py` |
| Prop. 6.4, conclusion s_m(A_{I,J}) >= gamma_m and E_m(A_{I,J}) >= gamma^{2m}, gamma = 0.09, 0.237, 0.38 | checked | `prop64`, `prop64_m3`, `prop64_m2`, `prop64_m1`, `evol_of_approx`, `prop64_spectral_m3`, `prop64_spectral_m2`, `prop64_spectral_m1` | `verify_five.py`: all structured and random cases |
| Prop. 7.1: C_3/gamma_3 < 167, C_2 gamma_2^{-1/2} < 26 | checked | `C3_lt`, `C2_lt`, `nopivot_density`, `nopivot_half` | `constants_exact.py` |
| Prop. 7.2: 64, sqrt(12)(pi + 4 log 2 + 2 L_0) < 76, < 77 | checked | `pivot_scales`, `log19_lt`, `halfpotential_constants` | `constants_exact.py` |
| Theorem 1.1 branches: sqrt(12) 77 < 267, 16 pi < 51, indefinite < 269, 269 <= 270 | checked | `main_constants`, `indefinite_rewrite` | `constants_exact.py` |
| Theorem 1.2 scaling | checked | - | - |
| Remark 8.2: no pivot for N > 256, spectrum, rank-two blocks, density <= 4 sqrt(e) for every b, c | checked | `two_star_no_pivot`, `bathtub_value`, `two_star_constants` | `verify_five.py` (R82), `two_star_affine.py` |
| Remarks 8.1, 8.3 | unchanged from the nine-eigenvalue paper | - | - |

The statements of Sections 2 to 5 are verbatim those of the nine-eigenvalue paper; their Lean checks are the files
in `lean/shared/` (54 theorems; the lemma numbered 2.8 there is Lemma 2.7 here, because the diagonal-dominance
lemma, used only by the old sampling argument, is removed). `QformNine3.lean` and the Section 6-7 constants of
`QformNine.lean` belong to the old argument and are not needed here.

## Findings during the audit

1. The first draft of Proposition 7.2 and of the indefinite-pair branch used log 19 < 2.9445, which is true but
   needs a fifth-order logarithm bound in Lean. The intermediate bounds were relaxed to use log 19 < 3
   (sum < 21.92 instead of < 21.7; indefinite branch < 269 instead of < 267). The stated constant 270 is unchanged.
2. In Lemma 6.3 the summation indices k, l clashed with the dimension k; they were renamed p, q.
3. The randomized test generator first drew Gaussian star weights, which almost never satisfy the no-pivot
   condition (it forces |a_ij| < 1/16 when the diagonal vanishes); it was replaced by weights of equal modulus.
   This was a defect of the test, not of the paper.
4. The Lean proof of Proposition 6.4 gives the non-strict bounds s_m(A_{I,J}) >= gamma and
   E_m(A_{I,J}) >= gamma^{2m} at the rounded constants gamma = 0.09, 0.237, 0.38, where the text states strict
   inequalities at gamma_m. Section 7 uses only the rounded constants, and C_3/0.09 < 167 and
   C_2 (0.237)^{-1/2} < 26 hold as stated, so nothing downstream changes.
5. Two independent reviews by the scheduled workers (account01/B07 and account02/B05, 24 September, both on
   paper.tex blob f3e5fc17) found the same presentation gap in the proof of Lemma 5.3: the coordinate chosen large
   for u need not be large for u' (witness u = (1/sqrt2, 0), u' = (0, 1/sqrt2)), so the negative tail needs its
   own coordinate i' with |u'_{i'}| >= rho_0/sqrt2. Since |u| = |u'|, the cutoffs and the constants are unchanged.
   The proof now chooses i and i' separately. The nine-eigenvalue paper, which this paper supersedes, has the same
   wording and is left as published.
6. account01/B07 observed that the two-star example of Remark 8.2 has a bounded density for every b, not only for
   b = 0, with the same bound 4 sqrt(e). The remark now proves this: given the centre U_k = u, the rest of the k-th
   summand is a linear form in direction v(u) = 2uw + beta_k, and |v(u)| >= |2u + r| where r = beta_k . w.
   `checks/two_star_affine.py` samples five affine choices on centred coordinates, including beta_k parallel to w
   with v(u) vanishing inside the support; the largest empirical density is 2.52 (at b = 0), against 4 sqrt(e) = 6.59.

No mathematical error was found in the final text.

## The strongest case against the result, and the check that answers it

The new lemma looks too easy: a four-page sampling argument with rank bookkeeping is replaced by one averaging.
The places it could fail are (i) the expectation of the sign chaos, if the signs were not independent or the
diagonal were not removed; (ii) the passage from 2m - 1 eigenvalues of A to m singular values of the block; and
(iii) the smallness of Q_eps, which uses only |a_ij| < a_0 and not the row structure of A. Check (i) is the Lean
theorem `chaos_second_moment`, an exact identity over all 2^n sign vectors, with the diagonal excluded by
definition. Check (ii) is Lemma 6.2(b), verified to 8e-15 on every tested partition; the direction the proof
uses, s_m(A_{I,J}) >= s_{2m-1}(C), and the whole passage from N_A(1) >= 2m - 1 to E_m(A_{I,J}) >= gamma^{2m}, are
the Lean theorems `approx_of_dil` and `prop64_spectral_m3`, `prop64_spectral_m2`, `prop64_spectral_m1`. Check (iii): the bound
E ||Q||_F^2 <= 2 a^2 k^2 holds for every matrix with off-diagonal entries at most a, whatever its structure,
and `decoupling_check.py` compares the exact mean with Monte Carlo on stars, a hub with trigonometric leaves,
Wigner matrices and low-rank matrices. The four-eigenvalue example of Remark 8.2 is the natural counterexample
to a result that is too strong: it satisfies every hypothesis except the fifth eigenvalue, and there the block
rank is two for every partition, exactly as the lemma permits.

## Files

* `paper.tex`, `paper.pdf`
* `lean/QformFive.lean` (17 theorems), `lean/QformFive2.lean` (13 theorems), `lean/QformFive3.lean` (70 theorems:
  the 13 of `QformFive2.lean` repeated so that the file compiles alone, and 57 more for the spectral steps and
  Proposition 6.4), `lean/*_run.lean`, `lean/run_*.log`
* `lean/shared/` - the checks of Sections 2-5 carried over from the nine-eigenvalue paper
* `checks/constants_exact.py` + log (41 claims at 50 digits), `checks/decoupling_check.py`,
  `checks/verify_five.py` + log, `checks/two_star_affine.py` + log, `checks/constants_opt.py` (choice of eta and zeta)

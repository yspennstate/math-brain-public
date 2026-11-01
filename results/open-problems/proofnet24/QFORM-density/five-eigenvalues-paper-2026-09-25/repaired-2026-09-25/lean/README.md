# Lean files for the repaired five-singular-value paper

Target: `../paper.tex` (git blob 98e45d53, commit 4e530247). Coverage, item by item: `../LEAN_COVERAGE.md`.

| File | Paper | Theorems |
|---|---|---|
| `FiveS4.lean` | Section 4: Lemma 4.2 in full; the stopping procedure and constant of Theorem 4.1; Steps 4-5 of Lemma 4.3 | 14 |
| `FiveS4Thm.lean` | Theorem 4.1 from Lemma 4.3, and its cases l = 1, 2, 3 (namespace `QformFiveB.Thm41`) | 20 |
| `FiveS5.lean` | Section 5: the constants and elementary steps of Lemmas 5.1-5.6, including the coefficient 19 of Lemma 5.4 | 35 |
| `FiveS5Partition.lean` | Lemma 5.4, the off-diagonal case: a partition with norm(S_{I,J})_F >= L/4 | 10 |
| `FiveS5Square.lean` | Lemma 5.1, second assertion: the measure of {y : a y^2 + beta y + gamma in U} | 3 |
| `FiveS5Density.lean` | Lemma 5.1, the density formula of a(Y-m)^2 + v and its bound 1/sqrt(abs(a) abs(z-v)) | 10 |
| `FiveS5Bounded.lean` | Lemma 5.6, display (5.6): a density bounded by M gives E abs(Z-a)^{-1/2} <= 2 sqrt(2M) | 6 |
| `FiveS5Rearrange.lean` | Lemma 5.5, (5.5): the rearrangement inequality, with the layer-cake formula | 10 |
| `FiveS5Kernel.lean` | Lemma 5.5, (5.4): J(d) <= pi + 4 log 2 + 2 log+(1/abs d) (namespace `QformFiveB.Kernel`) | 10 |
| `FiveS5Pairhalf.lean` | Lemma 5.6 from the density bounds of Lemmas 5.2 and 5.3: both cases, with the rearrangement and (5.6) repeated (namespace `QformFiveB.Pairhalf`) | 37 |
| `FiveS5Concentration.lean` | Lemma 5.4: the diagonal case of (5.2) by conditioning, and (5.3) by the layer-cake formula (namespace `QformFiveB.Concentration`) | 13 |
| `FiveS5Fourier.lean` | Lemma 5.4: the off-diagonal case of (5.2) from the bound of Corollary 4.4(c), with the constant c54 < 19 (namespace `QformFiveB.Fourier54`) | 14 |
| `FiveS5Definite.lean` | Lemma 5.2 in full: polar coordinates, the linear change of variables and completing the square (namespace `QformFiveB.Definite`) | 8 |
| `FiveS5DefHalf.lean` | Lemma 5.6, the definite case, from its hypotheses (namespace `QformFiveB.DefHalf`) | 18 |
| `FiveS5Hyper.lean` | Lemma 5.3 in full: null coordinates, the hyperbolic change of variables, the bound along each branch, and the paper's form of the density bound (namespace `QformFiveB.Hyper`) | 37 |
| `FiveS5PairFull.lean` | Lemma 5.6, the indefinite case, from its hypotheses: `FiveS5Hyper` and `FiveS5Pairhalf` repeated and joined (namespace `QformFiveB.PairFull`) | 79 |
| `FiveS5Reduce.lean` | Lemma 5.4, the diagonal case, from its hypotheses: the product law split at one coordinate (namespace `QformFiveB.Reduce`) | 12 |
| `FiveS7.lean` | Section 7: Propositions 7.1 and 7.2, the four cases and the scaling of Theorem 1.1, Remark 7.3 | 18 |
| `FiveS7Remark.lean` | Remark 7.4 in full: the counterexample with four eigenvalues of modulus one, no pivot and E_3 = 0 in every block | 18 |
| `FiveS6.lean` | Section 6: `../../lean/QformFive3.lean` repeated, and Proposition 6.4 as stated in the repaired text (namespace `QformFiveB.Signs`) | 79 |
| `FiveS2Schur.lean` | Lemma 2.6 in full (the Schur-complement count), with the spectral toolkit from `../../lean/QformFive3.lean` | 17 |
| `FiveS2Gram.lean` | Lemma 2.7(b) and the projection facts of Lemma 4.3 | 7 |
| `FiveS2Minors.lean` | Lemma 2.7(a) in full: the principal-minor expansion, e_m of the eigenvalues as the sum of principal minors, and Cauchy-Binet for Gram matrices | 17 |
| `FiveS2Gamma.lean` | the Gamma integrals of Lemmas 2.3 and 5.4 | 5 |
| `FiveS2Fourier.lean` | Lemma 2.1(c), the Gaussian identity for E e^{-v(Z-a)^2}, and the bound used later | 4 |
| `FiveS2Smooth.lean` | Lemma 2.1(b) in the form used and Lemma 2.2: density bounds from the characteristic function by Gaussian smoothing (namespace `QformFiveB.Smooth`) | 23 |
| `FiveS2Halfmoment.lean` | Lemma 2.3 in full, in [0, inf] (repeats the Gamma and Fourier lemmas so as to compile alone) | 18 |
| `FiveS2Condition.lean` | Lemma 2.4 in full: the law of Q, its density and the bound on E k(Q) | 4 |
| `FiveS2Weyl.lean` | Lemma 2.5 in approximation-number form (with the norm and rank lemmas it needs) | 25 |
| `FiveS2Envelope.lean` | the envelope integrals of Lemmas 2.2 and 2.3 and the constants they give | 4 |
| `FiveS3.lean` | Section 3: the finite and one-variable steps of Theorem 3.1 and Lemmas 3.2-3.3 | 14 |
| `FiveS3Diff.lean` | Lemma 3.3: Y - Y' has a density bounded by one | 1 |
| `FiveS3Fpower.lean` | Lemma 3.3 from Lemma 3.2: int phi <= 2 pi K for a nonnegative characteristic function, the law of Z as a convolution power, and the L^p bound (namespace `QformFiveB.Fpower`) | 13 |
| `FiveS3Ball.lean` | Theorem 3.1: Ball's determinant inequality, the determinant step of the transport proof (namespace `QformFiveB.Ball`) | 8 |
| `FiveS3BL.lean` | Theorem 3.1 in full, by Barthe's transport argument, for continuous positive, then lower semicontinuous, bounded, and general measurable h_i (Ball's inequality repeated from `FiveS3Ball`; namespace `QformFiveB.BL`) | 67 |
| `FiveS3Lemma32.lean` | Lemma 3.2 in full: (a) from Theorem 3.1 through the orthonormal completion of U and a fibre bound, then (b) and the last assertion from (a) (`FiveS3BL` and `FiveS3Proj` repeated; namespaces `QformFiveB.ProjA` and `QformFiveB.Lemma32`) | 94 |
| `FiveS3Lemma33.lean` | Lemma 3.3 from its hypothesis: the law of Z is the image of a product law under a linear form (characteristic functions), so Lemma 3.2 bounds its density (`FiveS3Lemma32` and `FiveS3Fpower` repeated; namespace `QformFiveB.Lemma33`) | 114 |
| `FiveS3Proj.lean` | Lemma 3.2(b) and its last assertion from Lemma 3.2(a), through the square root of BB^T (namespace `QformFiveB.Proj`) | 12 |
| `FiveS4Cor.lean` | Corollary 4.4: the constants C_3 and C_2 and their comparisons | 12 |
| `FiveS4CorA.lean` | Corollary 4.4 (a) and (c) from the bound of Theorem 4.1 (namespace `QformFiveB.CorA`) | 39 |
| `FiveS4CorB.lean` | Corollary 4.4 (b) from the bound of Theorem 4.1 (namespace `QformFiveB.CorB`) | 32 |

Lean 4.29.1 and Mathlib 5e932f97 (Lean's `lake env lean` in any project that depends on that Mathlib):

    lake env lean FiveS4.lean
    python ../../lean/mkrun.py FiveS4.lean      # writes FiveS4_run.lean: the source plus #print axioms
    lake env lean FiveS4_run.lean

`checks/FiveS*_axioms.log` are those runs: every theorem depends on propext, Classical.choice and Quot.sound only.
No `sorry`, no `admit`, no new `axiom`. Each file compiles on its own.

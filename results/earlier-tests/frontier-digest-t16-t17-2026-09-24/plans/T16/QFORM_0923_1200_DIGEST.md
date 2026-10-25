# QFORM research plan, 2026-09-24

His goal (09-22 20:03): prove the full conjecture. The memory lists these as proved: the separable case (three L^3 Fourier factors and Hölder), the exact rank-three case, a localized regime (Prop. 4), the definite-core coarea lemma, and the sharpness of "three". The general case is still open. The difficulty is that the large coordinates Y_j = <r_j, X> depend on the rest of the form.

## 1. Read and audit (first hour)
Read in full the rank-three theorem (claim_e0cc72a6bc354cc9b5087d7612e024b4), Prop. 4 (claim_c7b8ddc8241046e6b12e8087b2b3e297), the L^3 lemma (claim_8bd2ad93a5cb4c5bad5db55fa426702e), the coarea lemma (claim_b75770a236ad4a0998ae27543dfdb15c), the correction saying the constant is not pi (claim_9d24031501b143b6b25e2835abd83eba), and the note calling the Fourier route viable (claim_9b58aeaa6aaf4be48965e51838f04480). Record each one's exact hypotheses: whether linear terms are allowed, and what "localized" means. Re-derive the rank-three proof line by line, since the rest leans on it.

## 2. Reductions
- Bathtub. P(|Q-s|<e) is multilinear in (f_1,...,f_n), and with the other densities fixed the best f_i is the indicator of a set of measure one. So each X_i may be taken uniform on a measure-one set (a finite union of intervals). Unlike in Rogozin's linear case, intervals need not be extremal.
- Sylvester/pigeonhole. Two of the three large eigenvalues share a sign, so a definite 2-plane core always exists.
- Polynomials. Conditioning creates linear terms, so prove the statement for quadratic polynomials whose quadratic part has three eigenvalues of modulus at least 1. Check that the sharpness examples and the separable proof survive shifts.

## 3. Main line: Schur-complement conditioning, graded by the number k of large eigenvalues
If |A_ii| >= c, then exactly Q = A_ii (X_i - u)^2 + S(X_{-i}), where u depends on X_{-i}, S is the Schur complement, and X_i is independent of X_{-i}. At distance r from the vertex, the first term has conditional density at most (|A_ii| |r|)^{-1/2}, uniformly in u. Since S^{-1} is a principal submatrix of A^{-1}, Cauchy interlacing leaves S with at least two eigenvalues of modulus >= 1 (perturb a singular A). Hence

  p_Q(s) <= c^{-1/2} E|s - S|^{-1/2},

which is finite once forms with two large eigenvalues satisfy P(|S-s|<=t) <= C t^a for some a > 1/2. The natural graded statement:

  k=1: C t^{1/2};  k=2: C t log(2/t) (X_1^2 - X_2^2 shows the log is needed);  k=3: C t,

each level following from the one below by the same step. A 2x2 principal block with both eigenvalues of modulus >= c also works. Its kernel is at worst logarithmic and the complement keeps one large eigenvalue, so only the k=1 bound is needed. The induction is over k, not n, so a constant is lost only a bounded number of times. This settles every case in which each Schur complement met along the way has an entry of size >= c.

## 4. The hard residue: delocalization
Model: A = sum_{j<=3} r_j r_j^T with spread-out r_j and all entries O(1/n). Here I would try the decoupled bound

  |phi_Q(t)|^2 <= E_{X_J,X_J'} prod_{i in I} |phi_i(2t (A_IJ (X_J - X_J'))_i)|

for a random split I, J, averaged over t, using that each Y_j is a sum of many small independent pieces.

## 5. What I will avoid
- Pointwise decay of each phi_i. A measure-one set spread out periodically makes |phi_i(s_0)| close to 1 at a chosen large s_0; this is the continuous form of arithmetic structure. Fourier arguments must average over t.
- Conditioning on the complement of the definite plane. The bound becomes an integral of a sup over planes, of the order of the cube's projected volume, which grows like n.
- CLT machinery (Bentkus-Götze, Götze-Tikhomirov) as the engine. It needs moments that densities <= 1 do not supply, bounds Kolmogorov distance rather than density, and wants several comparable eigenvalues. Kwan-Sauermann covers only Rademacher variables; ideas only.
- Any induction on n that loses a constant at each step.

## 6. Numerics alongside
For n <= 6, maximize the density over A and unions of intervals to find the extremal case.

## First concrete step
Read Prop. 4 and the rank-three proof in full. Then write out the one-coordinate Schur step with every constant, and test the interlacing claim on random matrices.

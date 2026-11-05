# an independent reading check of T357's Theorem 5

Agent H, 4 Nov 2026 21:5x. This is a reading-only check that closes the residual risk named at the end of
`REVIEW_agent_H.md`. The source is `T357_GAUSSIAN_COMPLETE_PROOF.md` lines 566-662, from `results/frontier-2026-10/2026-10-23-t228-closure-30-agents/fullproof/`.

Theorem 5 verifies that the random-feature matrix A_0 meets Wang-Zhong-Fan's sufficient matrix conditions (Prop. D.1(b)).
I re-derived each step by hand. I did not reopen the arXiv text of WZF itself. The claim that items 1-4 are exactly
D.1(b)'s conditions rests on the package's own source audit and on B05's review.

## What I re-derived, and it holds

1. **Signed-permutation invariance (item 4).** Flipping the sign of row i of A_0 is the same as replacing input x_i by
   -x_i. That leaves the Gaussian law unchanged, and tanh is odd. Permuting rows permutes i.i.d. inputs. Columns work the
   same way through the feature rows. The clipping P_R commutes with orthogonal maps, and signed permutations are
   orthogonal, so the clipped B keeps the invariance. It follows that every off-diagonal entry of (BB^T)^k and every
   entry of (BB^T)^k B has mean zero: flipping the sign of row i flips that entry.

2. **The Lipschitz constant (8.7).** After clipping, the operator norms are at most C_X sqrt(d) and C_G sqrt(d). The
   difference of the tanh arguments is then at most C (||X-X'||_F + ||G-G'||_F), and dividing by sqrt(m) gives
   C/sqrt(d). Telescoping with ||B||_op <= C_A bounds each power entry. This is right, and clipping is what makes the
   Lipschitz bound global rather than holding only on a high-probability set.

3. **The rates (8.3)-(8.5).** By Gaussian concentration, a deviation of d^{-1/2+eta} for a C/sqrt(d)-Lipschitz function
   has probability at most exp(-c d^{2 eta}). A union bound over O(d^2) entries keeps the sum finite. The countable union
   over k and over rational epsilon gives the bounds for every k at once, which is what an "eventually almost surely"
   condition needs.

4. **The Hermite remainder in (8.8).** The off-diagonal entries of Sigma_V expand in Hermite order l with weight rho^l,
   where rho = O(sqrt(log d / d)).
   - Because tanh is odd, the l = 0 and l = 2 terms vanish.
   - The remainder therefore starts at l = 3. A row sum of m (log d / d)^{3/2} = O((log d)^{3/2} / sqrt(d)) goes to 0.
   - This step depends on tanh being odd. For an activation with an even part, the l = 2 term alone has row sum about
     log d, so the bound would fail. The proof says "odd" only in the invariance step, so a reader porting it to ReLU
     should know this second use too.
   - The diagonal scaling by a_j -> a costs at most 2 max|a_j - a| ||VV^T||_op, which goes to 0.

5. **The normalization.** A_0 is N x m with entry variance v/m. So (1/N) tr(AA^T) -> v, which gives E D^2 = v; the
   feature-side trace is r v. I recomputed E D^4 for the Gaussian comparison matrix (8.2):
   - The rows are i.i.d. with covariance C_V/m.
   - (1/N) E tr((AA^T)^2) = (tr Sigma)^2 + N tr(Sigma^2).
   - tr Sigma = a^2 + nu = v.
   - tr(Sigma^2) = (1/m)[(a^2+nu)^2 + a^4 gamma], using tr((VV^T)^2) = m(1 + gamma).
   - So E D^4 = v^2 + r(v^2 + a^4 gamma), which matches the package. Var D^2 = r(v^2 + a^4 gamma) > 0, so the
     singular-value law is not constant, as claimed.

6. **The spectral comparison.** For PSD matrices, ||Sigma^{1/2} - C^{1/2}||_op <= ||Sigma - C||_op^{1/2}, because the
   square root is operator monotone. The sample-matrix difference is then at most ||Z||_op / sqrt(m) times that, which
   goes to 0 and leaves the limiting law unchanged. The fixed point (8.9) is unique by the monotonicity argument given
   there, which I checked.

7. **The independent copy.** A_0 is independent of z, h, Y and the mask. That is because it uses only the coordinates
   perpendicular to theta, and Gaussian rotation makes those independent of the theta coordinate. So representing it in
   law as Pi A_0' Pi', with fresh signed permutations, is valid jointly with that side information. The AMP theorem
   needs only the law.

## What Theorem 5 does not carry

- The operator-norm error E_d goes to 0 **in probability**, not almost surely. Passing it through the AMP iterates is a
  stability step for Proposition 4 and Section 9, not part of Theorem 5. Section 9's claim (9.9)-(9.10) was checked by
  B05. I did not reread it.
- Whether D.1(b)'s list matches items 1-4 word for word is taken from the package's source audit, as noted above.

## Verdict

I found no gap in Theorem 5 as written, and every constant and normalization I recomputed agrees. The residual risk in
`REVIEW_agent_H.md` narrows to two things: the causal embedding in Section 9, and a word-for-word match against the
WZF text. Neither is needed to accept T357 internally. Both should be checked before external use.

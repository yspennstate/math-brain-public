# Referee report: nested beta-Laguerre ensembles

Paper: yspennstate/nested-beta-laguerre at 31ca408 (main.tex, 728 lines, 8 pages). Referee: an agent,
14 Nov 2026.
Claim: for beta > 0 and a > -1, with B lower bidiagonal, B_ii = beta^{-1/2} chi_{beta(a+i)}, B_{i+1,i} =
beta^{-1/2} chi_{beta i}, every leading block of L = B B^T has the beta-Laguerre law with the fixed power
theta(a+1) - 1, and L is a.s. essentially self-adjoint, so one spectral measure carries all sizes. This answers the
Laguerre case of Virag's Question 2 (ICM 2014, arXiv:1804.06953). The antisymmetric Gaussian family nests the same
way, and several obstructions are proved under stated hypotheses.

## Verdict

SOUND. No change made. The rebuilt PDF (8 pages, no undefined references) has the same text as the posted one; the
source has no control characters.

## Proofs checked (each re-derived)

- Theorem 1.1, finite blocks: L_n = B_n B_n^T because the first n rows of B vanish past column n; C_n = R_n B_n^T R_n
  is the Dumitriu-Edelman lower bidiagonal with A_n = theta(n + a); A_n - p_n = theta(a+1) - 1 does not depend on n;
  the scale change t = beta x turns e^{-t/2} into e^{-theta x}. Correct.
- Lemma 3.1 (entry density): the triangular Jacobian 2^n d_n prod_{i<n} d_i^2 and the powers beta a - 2,
  beta(a+n) - 2. Correct.
- Lemma 3.2 (essential self-adjointness): E e^{X/4} = 2^{nu/2} for X ~ chi^2_nu, Borel-Cantelli gives c_i = O(i),
  and the boundary-term argument rules out deficiency vectors. Correct.
- The remark E L_11 = a + 1 against E tr L_2 / 2 = a + 2. Correct.
- Corollary 4.1 (antisymmetric): even N is B_m with a = -1/2 after scaling; for odd N the Cholesky recursion, with
  w_j of shape theta/2 by the beta-gamma splitting, gives the Laguerre factor with a = 1/2; the exponents beta/2 - 1
  and 3 beta/2 - 1 after s = lambda^2. Correct.
- Proposition 5.1 (dimension): 2N - 1 < N(N+1)/2 iff (N-1)(N-2) > 0; Lipschitz image of a (2N-1)-dimensional box
  is null. Correct.
- Lemma 5.2 (Dixon-Anderson with general Dirichlet parameters): exponents s_i + s_k - 1 and the normalisation.
  Correct.
- Proposition 5.3 (parameter shift p -> p + theta under the ordinary link), and the R -> infinity passage to
  Laguerre. Correct.
- Proposition 5.4 (reversed Killip-Nenciu): the laws of alpha_{2N-2}, alpha_{2N-3}, alpha_{2N-4} from KN (1.11), the
  mean 1/2 + d/(2(S + beta)) against 1/2 + d/(2S), and for p = q the variance 1/(4(S + beta + 1)) against
  1/(4(S + 1)) (the numerator S(S + 2theta + 1) + theta(theta + 1) factors as (S + theta)(S + theta + 1)). Correct.
- Proposition 5.5 (unitary principal blocks). Correct.
- Proposition 5.6: the Jacobian (lambda_2 - lambda_1)^2 / (2b) (determinant -delta/(2r) with r = sqrt(q(1-q))), the
  entry density C b^{beta-1} e^{-tr V}, the functional equation forcing V'' constant, and the converse. Correct.
- Proposition 5.7: F' = w (m_1 - y m_0), hence Gaussian. Correct.

## Citations checked against the sources

- Virag arXiv:1804.06953: Theorem 4.1 on p. 5 and Question 2 on p. 6, wording as quoted.
- Dumitriu-Edelman arXiv:math-ph/0206043: Theorem 3.4 is the beta-Laguerre bidiagonal model with p = 1 + beta(m-1)/2.
- Killip-Nenciu arXiv:math/0410034: Theorem 2, (1.10) for B(s,t), (1.11) for the alpha laws, (1.12) for b_{k+1}.
- Dumitriu-Forrester arXiv:0904.2216: (1.4) and Theorem 1.1; Section 6 is the proof through a beta-Laguerre ensemble,
  as the paper says.
- Crossref: Bufetov-Kawamoto J. Stat. Phys. 192 (2025) art. 58; Kawamoto-Shibukawa ALEA 23 (2026) 255; Assiotis
  J. Theoret. Probab. 32 (2019) 1880-1891; Dumitriu-Forrester J. Math. Phys. 51 (2010) 093302. All as listed.
- Not opened: Gorin-Shkolnikov, Borodin-Gorin, Neretin, Assiotis-Najnudel, Valko-Virag, Krishnapur-Rider-Virag; they
  are cited for context only, not for steps of a proof.
- Prior-work search (14 Nov): no earlier construction of a nested beta-Laguerre Jacobi matrix turned up.

## Minor (not acted on)

- In the proof of Proposition 5.6, h = q lambda_1 + (1 - q) lambda_2 makes q the weight of lambda_1 at e_1, while the
  text calls q a weight at the deleted endpoint e_2 (where lambda_1 has weight 1 - q). Since Dir(theta, theta) is symmetric this changes nothing.

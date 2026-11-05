# T357, a word-for-word check of the Wang-Zhong-Fan hypotheses

Agent H, 4 Nov 2026 23:1x. This is the last open item from `T357_residuals_check.md`.
- Source text: arXiv:2206.13037v5 (Ann. Appl. Probab. 34(4), 2024), PDF read 4 Nov 2026, extracted with pdftotext.
  Read: Definition 2.20, Assumption 2.17, Theorem 2.22 and Proposition D.1 (Appendix D.2).
- Package: `T357_GAUSSIAN_COMPLETE_PROOF.md` in this repository.

## Proposition D.1(b2) against Theorem 5

D.1 assumes that the empirical singular-value law converges to D almost surely in Wasserstein distance, with D having
finite moments of all orders. Under (b2), W = Pi_U M Pi_V^T, with uniform signed permutations independent of M. For every
integer l >= 0 and eps > 0, condition (D.6) must hold almost surely for all large m and n:
- diagonal entries of (MM^T)^l within n^{-1/2+eps} of their normalized trace, and off-diagonal entries below n^{-1/2+eps};
- the same for (M^TM)^l;
- every entry of (MM^T)^l M below n^{-1/2+eps}.

The conclusion is that W is rectangular generalized invariant (Definition 2.20), with the same limit diagonal law as the
bi-orthogonally invariant matrix of part (a).

| D.1 / Thm 2.22 hypothesis | T357 | match |
|---|---|---|
| (D.6) row block, (MM^T)^l | (8.3) | exact (m^{-1/2+eps} vs n^{-1/2+eps}; m/n proportional) |
| (D.6) column block, (M^TM)^l | (8.4) | exact |
| (D.6) cross block, (MM^T)^l M | (8.5) | exact |
| "almost surely for all large m, n" | "eventually almost surely", via summable Gaussian-concentration bounds plus Borel-Cantelli on the clipped matrix, which equals the original eventually a.s. | yes |
| W = Pi_U M Pi_V^T, M independent of the permutations | item 4 and the independent-copy argument (line 657): A_0 equals Pi A_0' Pi' in law, with A_0' an independent copy | yes; the copy has A_0's law, so (8.3)-(8.5) hold for M = A_0' |
| singular values converge a.s. in W2 to D with all moments | item 2: compact support, operator norm eventually bounded. Note below. | yes |
| Thm 2.22: limit diagonal law equals that of a bi-orthogonally invariant G | D.1(b)'s conclusion, with G as in (8.2) | yes |
| Thm 2.22: operator norm below C a.s. for large m, n | item 1 | yes |
| Thm 2.22: E[D^2] > 0; Omega_t, Sigma_t nonsingular | E D^2 = v > 0; Section 6 positive-definiteness induction, for every c > 0 | yes |
| Thm 2.22: nonlinearities continuous, of polynomial growth, Lipschitz in the first t arguments | Section 9 regularity (affine Q map; sigma is 1/4-Lipschitz; M and Y projected to [0, 1]) | yes |
| Thm 2.22: W independent of initialization and side information | A_0 uses only coordinates perpendicular to theta, so it is independent of (z, h, Y, M); the representation in law holds jointly | yes |
| Assumption 2.17: side information converges in W2 with all moments; E[U_1^2] > 0 | (z, h, Y, M) are Gaussian or bounded; E R_1^2 = p/4 > 0 | yes |

**Note on the singular-value law.** D.1 needs almost-sure convergence. Item 2 states the limit. The almost-sure part
follows from the same machinery as (8.3):
- the operator norm is bounded eventually a.s.;
- each normalized trace (1/N) tr (A A^T)^k of the clipped matrix is O(1/d)-Lipschitz in the Gaussian entries, so it
  concentrates at rate exp(-c d^2 eps^2) and Borel-Cantelli applies;
- its mean converges to the comparison matrix's moment.

Moments then identify the compactly supported limit. The package states the limit and leaves this standard step
implicit. It is not a gap.

**Note on Definition 2.20 versus D.1.** Definition 2.20(b) asks for off-diagonal bounds on every rectangular diagonal
monomial: words in the symmetric embedding, the block projectors and the diagonal-extraction map. That covers nested
expressions such as M Delta(M^T M) M^T, not only plain powers. T357 checks plain powers alone, which is correct, because
D.1(b2) is the stated sufficient condition and its proof (Lemma D.2) does the reduction from monomials to powers. T357
cites D.1(b) and not Definition 2.20 directly, and that is the right citation.

## Verdict

Every WZF hypothesis that T357 uses matches the source text, and the package's claim that "items 1-4 are precisely the
sufficient matrix conditions of Proposition D.1(b)" is correct for part (b2). This closes the last open item on T357. My
review now stands as an independently checked, internally accepted answer in its stated regime, with the summary caveats
in `REVIEW_agent_H.md`.

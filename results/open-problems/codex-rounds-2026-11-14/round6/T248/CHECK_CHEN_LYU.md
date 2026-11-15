# T248: the hypotheses of Chen-Lyu Corollary 1.4 against PROOF.md (checked 15 Nov 2026)

Source read: G. Chen and X. Lyu, "Tracy-Widom law for sample covariance matrices under quadratic form
concentration", arXiv:2610.41416v2, Assumptions 1.1-1.2, Theorem 1.3, Corollary 1.4, Remark 1.5 (PDF text, 15 Nov).

Dictionary: their sample count N is our m; their dimension M is our N-1; their q_i are our z_i = Q^T sigma(U^T w_i);
their Sigma is our T; their H = X X^T with columns q_i / sqrt(N) is our H_P = m^{-1} sum z_i z_i^T.

| Chen-Lyu | PROOF.md | Holds? |
|---|---|---|
| 1.1(i) q_i independent, centered, E q q^T = Sigma (deterministic) | given U, the w_i are independent of U and of each other; E z = 0 from unit columns and E sigma(Z) = 0; T = E zz^T fixed given U | yes, conditionally on U |
| 1.1(ii) M/N -> y in (0, inf) minus {1} | (N-1)/m -> 1/b, b != 1 | yes |
| 1.1(iii) for each fixed p, uniform C_p, every deterministic symmetric A in C^{MxM}: moment bound on q^T A q - Tr(Sigma A) by C_p ||A||_HS | Section 2: the same bound for every REAL symmetric A, uniform on the event G_N | yes after one line: write A = A1 + i A2 with A1, A2 real symmetric; ||A1||_HS, ||A2||_HS <= ||A||_HS, so the complex case holds with 2 C_p |
| 1.2 delta I <= Sigma <= delta^{-1} I and 1 + gamma_1 m_+ >= delta | (17): T uniformly positive and bounded with a uniform right-edge pole margin on G_N | yes, on G_N |
| centering lambda_+ = f(m_+), scale gamma_+ from (1.6), factor N^{2/3} | E_T, gamma_T, factor m^{2/3} in (18) | yes (same definitions with Sigma = T, N -> m) |

Conditioning step (PROOF.md l.384-399): the corollary is applied to deterministic design sequences in G_N with uniform
constants; a violating subsequence of designs would itself be a deterministic sequence meeting the assumptions with the
same y, so the conditional distribution functions converge uniformly on G_N. This is the standard argument and is sound.
(17) moves the centering from E_T to E_0 at cost O(N^{-1/6}).

Verdict: the cited input applies as stated, with the complex-A remark added at the point of use. T248 is clear to be
written up as a paper (PROVED sub-result: TW1 for the projected spherical kernel with deterministic finite-size
centering); the remaining work is the write-up and its own referee audit, not mathematics.

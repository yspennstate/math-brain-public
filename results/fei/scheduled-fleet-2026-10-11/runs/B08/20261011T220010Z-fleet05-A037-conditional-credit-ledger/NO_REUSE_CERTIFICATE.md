# Single-use certificate

Common variables: fixed finite witness W; side information A; stopped transcript L containing every adaptive choice/outcome/stop. Probabilities belong to one joint P. The reference ledger uses a single joint Q or explicit channel/reset corrections.

| Account | Initial resource | Released amount | Terminal remainder | Extra resource if models change |
|---|---|---|---|---|
| Witness entropy | H(W given A) | sum p_h I(W;Y_h given A,h) | sum p_l H(W given A,l) | No free restart: a new witness needs a joint coupling and correction |
| Reference divergence | D(P_W || Q_W) | sum p_h D(P(Y_h given h) || Q(Y_h given h)) | sum p_l D(P(W given l) || Q(W given l)) | sum p_h E_P D(k_h^P || k_h^Q); add signed reset corrections |
| Physical spectral lift | H(S_0) | sum p_h J_h = I(S_0;L) | H(S_0 given L) = sum p_h B_h + E H(f_leaf) | The kernel uses Fourier signs; new witnesses/references need compatibility |

Each row is an equality after adding its extra resource on the initial-resource side. At a cut, the terminal balances become the new initial resources below that cut. Subtracting both the original entropy rebate and its released part double counts the same bits. Replaying a revealed fair bit releases zero; restarting the uniform reference injects one bit rather than obtaining it from the depleted root account.

Analytic checks: entropy chain rule, likelihood-ratio factorization, Bayes rule, Gibbs inequality, Walsh character orthogonality. Executed checks: out/VALIDATION.json, with rational prime-log identities; out/FROZEN_SPEC.md freezes the domains and arithmetic. No float sign is used. The implementation removed unreachable zero-mass states after an initial zero-division failure; that repair is documented in REPORT.md.

Review obligations for A088/A094: verify averaging over updated A, root-to-cut telescoping, mismatch/reset signs, zero fibers and actual fair physical branch probabilities. Verify the terminal physical residual includes erased-label costs even for constant leaves. Independent review is pending. Full FEI remains OPEN.

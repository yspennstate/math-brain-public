# Final independent review of the T357 synthesis

2026-10-23 (America/New_York). Reviewer: B01.

**Verdict: pass for the assigned mathematical scope.** I found no mathematical error in Sections 1–3, Theorem A, or the logical composition in Section 6 of `T357_THEOREM_AND_SYNTHESIS.md`. The numerical implementation has the correct normalization and matrix orientations. I also checked the algebra in the added common-regime corollary. No other author's file was edited.

The final reviewed synthesis `T357_THEOREM_AND_SYNTHESIS.md` is frozen at SHA256 `7b773eba4446340893bd8e67a1397ba06b154bf79b9f89a348e68c1a93282d51`. The comparison reference is the frozen `b01_GD_state_evolution_check.md`, SHA256 `077b6c8134a2780f4ad5132be70fe50ccdfccd7240d00a50b4ea775d1ea0338f`. The inspected numerical script `check_T357_finite_time.py` has SHA256 `d1abb15f3bd638c642690a357f6d38cf12cbfc19e54b235a911f53f90eac5f72`. The final editorial changes were inspected and all requested clarifications are present.

## Mathematical checks

| Item | Finding |
|---|---|
| Model and update (1) | Mean-loss step is $cd/m$ in $b$, or $cd$ in $w=\sqrt m\,b$. The code uses the required factor $cd/(nm)$ multiplying $H^\top$ residuals. |
| Delta-free moments (7) | The training residual moments and derivatives carry the factor $\alpha$. No appended-query fraction remains. |
| Backward formulas (8) | $U\widehat\Phi=\widehat\Phi T$ gives exactly the source-derived memory formula. The factor $1/\gamma$ is correct in both backward memory and covariance. Current column data are not needed because the last column of $\widehat\Phi$ vanishes. |
| Forward formulas (9) | $T\Psi=\Psi U$ gives the frozen formula. Recomputing $T$ after completing the current row of $\Psi$ is necessary and explicitly done. All covariance factors have the correct order. |
| Causal scalar updates | The $q$ recursion contains $s\widehat\ell/\gamma$; the column derivative has diagonal $\lambda$. Row derivatives are differentiated through the entire preceding residual history before taking expectations. |
| Fresh test law (10) | Every training residual vanishes on mask-zero query rows, leaving $s q_tZ+G_t$. This gives $A_t=s q_t$ and $Q_t=A_t^2+\Sigma_{tt}$. |
| First step (11) | Both $ca^2\mu_\beta$ and $c^2[\mu_\beta^2a^2v/\gamma+(a^4+v^2/\gamma)/(4\alpha)]$ match the frozen proof. |
| Positive definiteness | $\Omega\succeq(\nu/\gamma)\widehat\Delta$, invertibility of triangular $\Psi$, and $\Sigma\succeq\nu\Gamma$ establish the induction. Conditional strict monotonicity of the next sigmoid residual closes the next residual Gram matrix. |

Theorem A makes the appropriate distinctions. The full finite path is asserted to converge weakly; the teacher/one-score pairs receive the additional TV conclusion. Positive residual variance supplied by state evolution is exactly the missing hypothesis needed by B04's matched-covariance TV theorem. Its signed-measure argument gives both exact calibration convergence and the integrated regression-curve statement. The risk formula follows by Gaussian regression and truncation using conditional second moments. The bounded TV and calibration errors justify every finite environmental $L^p$ assertion. No environmental $L^p$ claim for unbounded risk is inferred merely from an $O_P(1)$ bound.

Section 6 correctly connects the matrix theorem, causal embedding, deterministic-to-empirical teacher-overlap comparison, removal of the operator-small RF remainder, and query extraction. The source theorem is applied to the perpendicular matrix with independent side information. Memory terms cancel from the actual training update. The uniform-time conclusion uses B02's one-event geometric tail and sequentially uniform TV approximation; it is not obtained by taking an infinite union of fixed-time state-evolution limits. The transfer of the scalar overconfidence theorem uses bounded measurable observables for signed confidence and a separate integrability argument for risk.

The common-regime corollary is also correct: $\beta<\log(3)/B_0$ implies $p_1>p_0/8$, hence $C_*(\beta)\le C_0$. Moreover $\mu_\beta\le\beta/4$ and $\tau^2\ge v^2/(4\alpha\gamma)$ imply
\[
c_*<\frac{\beta a^2\mu_\beta}{a^4\mu_\beta^2+\tau^2}
\le\frac{a^2\alpha\gamma\beta^2}{v^2}
<\frac{\gamma}{64L^2}<\frac{\gamma}{2\Lambda}.
\]
It supplies one common fixed model without extending the uniform-time theorem beyond its stated sample/step regime.

## Numerical implementation and documentation

The script integrates the label conditional on the teacher coordinate exactly, retaining the same label branch across all updates. It propagates the full row derivative history. Its shared normal coordinates and successive Cholesky factors implement the consistent joint Gaussian history, rather than replacing the reused-sample process by independent time steps.

I independently ran three steps with a new Sobol scramble and $2^{16}$ points. First-step absolute errors were at most $1.30\times10^{-7}$, and the third-step moments agreed with the saved five-step run to the displayed numerical precision. From the saved JSON, the maximum differences between its two $2^{18}$-point scrambles are $3.216\times10^{-7}$ and $3.319\times10^{-7}$. The largest dimension-1000 discrepancy in reported standard-error units is respectively $0.7463$ and $1.8225$. These verify the numerical statements in Section 7 and are not proof premises.

Two documentation clarifications were sent to the author:

1. The finite-network numerical $A,Q$ values are the asymptotically equivalent covariance proxies $a(F^\top b)_1$ and $a^2\|F^\top b\|^2+\nu\|b\|^2$, not exact finite-dimensional fresh-test moments. This clarification is now present in Section 7.
2. Explicitly use B04's full TV norm convention $\|\mu-\nu\|_{\rm TV}=\sup_{|f|\le1}|\int f\,d(\mu-\nu)|$ when stating the constant-one calibration bound. Also update the introductory sentence about compatibility of the optimal first-step scale with the small-step theorem to reflect the new common-regime corollary. Both clarifications are present in the final frozen synthesis. The normalized coefficient symbol is also consistently $w=\sqrt m\,b$, avoiding collision with the score-variance notation.

This review does not certify publication novelty, replace the source-level matrix audits, or establish a uniform-time result outside the theorem's explicit regime.

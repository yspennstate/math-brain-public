# T357, two of the three remaining items are already proved inside the package

Agent H, 4 Nov 2026 22:5x. Reading only. Source: `T357_GAUSSIAN_COMPLETE_PROOF.md` in this repository (the combined file). This follows `T357_sec9_check.md`, which left three items open. Two of them have
proofs written out in later sections of the same combined file, and I checked both. The Section 9 text points to them as
"the companion proof" and "the same finite-time stability estimate", which is why they first read as missing.

## 1. Nondegeneracy (Section 6 of the B01 module, lines 1072-1087): no regularization is needed, and the proof holds

Section 9 mentions a fallback that adds fresh Gaussian perturbations if the source theorem needs nondegenerate covariances.
The package does not use it. Section 6 proves the covariances are positive definite for every c > 0.

- From the boxed form (16) of the state recursion: Omega_t = gamma^{-1}{nu delta Delta_t + PSD} >= (delta/gamma) nu
  Delta_t = r nu Delta_t, and Sigma_t = nu Gamma_t + PSD >= nu Gamma_t. This uses nu = E tanh^2 - a^2 > 0 (0.0274 at the
  standard normal input).
- Delta_1 = p/4 > 0. If Delta_t > 0 then Omega_t > 0. Psi_t is triangular with diagonal lambda > 0, so Gamma_t > 0 and
  Sigma_t > 0.
- The step to Delta_{t+1}: condition on (Z, Y, M, G_1..G_{t-1}). On M = 1 the earlier residuals are fixed. G_t has
  positive conditional variance because Sigma_t > 0. R_{t+1} = Y - sigma(G_t + fixed) is a strictly monotone, nonconstant
  function of a nondegenerate Gaussian, so it cannot lie almost surely in the span of R_1..R_t.
- c = 0 is trivial (every score is zero) and is kept out of the theorem's use.

I checked each inequality, including the scalings delta Delta and r = delta/gamma. No gap.

## 2. The E_d / parameter-drift stability step (Section 7 of the B01 module, lines 1102-1121): written out, and it holds

- Comparing GD with the auxiliary AMP gives (20): e^Q_t <= e^Q_{t-1} + C e^R_t + o_P(1) and e^R_{t+1} <= C e^Q_t + o_P(1),
  starting from zero error. Both use Lip(sigma) = 1/4 and Cauchy-Schwarz on the overlap errors. This is the same pair I
  re-derived as (9.9)-(9.10).
- Replacing (s_d, lambda_d, r_d) by their limits adds terms of the form |s_d - s| times bounded normalized norms, all
  o_P(1).
- The step back to the actual tanh matrix uses ||E_d||_op = o_P(1) together with ||Q_t||/sqrt m = O_P(1) and
  ||R_t||/sqrt N <= 1.
  - The first bound follows by induction from Q_t = Q_{t-1} + lambda[A^T R_t + ...], since
    ||A^T R_t||/sqrt m <= ||A||_op sqrt(N/m) ||R_t||/sqrt N.
  - The second holds because the residuals lie in [-1, 1].
  - So E_d Q_t and E_d^T R_t are o_P(1) in normalized norm, and the same finite induction carries them.
- One remark. E_d -> 0 only in probability, so the conclusion is convergence in probability at each fixed time, which is
  what Theorem A states. Nothing claims almost-sure convergence through the iterates.

## Verdict

The only remaining check on T357 is a word-for-word comparison of Theorem 5's items 1-4 and the Section 8 algorithm
hypotheses against the text of Wang-Zhong-Fan (Prop. D.1(b), Thm 2.22). That needs the arXiv text. It is a check on the
package's own source audit, not a gap in the mathematics. T357 is accepted internally in its stated regime, with the
summary caveats in `REVIEW_agent_H.md` (the early-stopping answer only in the strongly underparameterized regime;
Theorem C at the first step only).

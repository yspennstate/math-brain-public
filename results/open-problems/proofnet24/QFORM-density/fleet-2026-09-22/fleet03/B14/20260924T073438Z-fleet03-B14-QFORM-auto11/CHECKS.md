# Checks — fleet03/B14 canonical-core localization

Run: `20260924T073438Z-fleet03-B14-QFORM-auto11`.

## Algebraic checks

1. **Exact cap saturation.** If `Z` has density `f` with `k=||f||_infinity in (0,1]` and `Y=kZ`, then
   `p_Y(y)=k^(-1)f(y/k)` and `||p_Y||_infinity=1`. For `k>0`, lower quantiles scale by `q_p(Y)=k q_p(Z)`, so median zero is preserved.

2. **Affine identity after recentering/scaling.** For `W=r+K^(-1)Y`,
   `W^T A W = Y^T K^(-1) A K^(-1)Y + 2(K^(-1)Ar)^T Y + r^TAr`.
   No moment or bound on `r` is involved.

3. **Spectral threshold after saturation.** Since every cap `k_i<=1`, `S=K^(-1)>=I`. On the positive spectral subspace of `A` above threshold `t`, the pullback `S^(-1)E_+` satisfies
   `x^T SAS x >= t||Sx||^2 >= t||x||^2`; the negative subspace gives the reversed inequality. Hence protected signed eigenvalue counts cannot decrease.

4. **Strict genericisation.** From `s_3(A_m^0)>=1`,
   `s_3((1+eta)A_m^0)>=1+eta`. Choosing a symmetric perturbation of operator norm at most `eta/4` leaves `s_3>1` by Weyl. Simple spectrum, nonzero principal minors and nonzero off-diagonal entries are simultaneous open-dense conditions because their failures are finite unions of zero sets of nonzero polynomials. Rational symmetric matrices are dense, so the perturbation may be rational.

5. **No-moment matrix approximation.** The generic perturbation is made only after the source law has compact support. With support radius `R_m`, the deterministic error is
   `|Y^T(G_m-A_m^0)Y| <= ||G_m-A_m^0|| R_m^2`.
   The construction chooses the perturbation after observing finite `R_m`, so the error tends to zero without any uniform support radius or moment.

6. **Weak closure of height.** Product `L^1` convergence implies product total-variation convergence. Pushforward under the fixed quadratic map contracts total variation. Adding the deterministic `o(1)` perturbation in item 5 gives weak convergence of the canonical outputs to the original output. Portmanteau on bounded open intervals gives the lower-semicontinuity of the height functional used in the report.

7. **Affine homogenisation.** For
   `B_T=[[G,b/(2T)],[b^T/(2T),0]]`,
   the perturbation from `diag(G,0)` has operator norm exactly `||b||/(2T)`. Because `s_3(G)>1`, the three protected eigenvalues remain outside `[-1,1]` for large `T`. With independent `V_T=T+U`, `U~Unif[0,1]`,
   `(Y,V_T)^TB_T(Y,V_T)=Y^TGY+(V_T/T)b^TY -> Y^TGY+b^TY` almost surely.

## Partner application check

Designated partner source:
`yspennstate/math-open-problems@deb713bc8e6df3f7e0ac5398e8cccbf00d1e7513`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B14/20260924T001624Z-fleet04-B14-scaled-schur-localization-r10/REPORT.md`.

It gives `6 sqrt(pi)/sigma` for an invertible physical `3x3` block with `sigma=min |lambda|`, uniformly in affine leakage. Translating coordinates changes only affine terms and constants, so the same estimate applies for every deterministic translation vector.

For `B_*=I_3-(2/3)11^T`, `B_*^2=I`, hence `spec(B_*)={1,1,-1}` and `sigma=1`. Numerically,

`6 sqrt(pi) = 10.634723105433096...`.

The source-pinned fleet04/B15 theorem at `7b2b0f54db9acbd23a5f69f715178ab666e22d8e` upgrades the already-paid interval bound to a canonical `C_0(R)` density with the same height because the ambient matrix has rank at least three.

## Scope checks

- No Gaussian, log-concavity, moment, bounded-support-diameter, fixed-fragment-count, connected-extremality or diagonal-basis hypothesis is introduced.
- Connected support is used only for approximating members of the canonical core; interval length is not uniformly bounded and the positive bridge floor may tend to zero.
- No independence is asserted after a spectral rotation.
- The theorem is an equality of optimal height constants between the full homogeneous target and a restricted **affine** canonical core. It does not say one may median-center and then discard the affine term.
- The full universal QFORM height theorem remains OPEN.
- The weak-limit localization itself carries essential height, not continuity. The separate fixed-instance `C_0` compiler is invoked only after an interval bound is established.

STATUS=PASS

SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B08, 2026-09-23T12:20:51Z.
attacking: the leakage-stable low-rank survivor — pay a physical hub whose star is transverse to a diffuse child direction by the newest mixed-Fresnel theorem, and route failure to alignment or a localized second coordinate.

# Early substantive checkpoint

Programme: `QFORM-DENSITY-3EIG-20260922`; owner control revision `2026-09-22.15`. Full target OPEN. Original independent coordinates only; no moments, support regularity, rotation-independence, arbitrary-joint coarea, pointwise law-uniform Fresnel decay, or pre/post-Schur currency transfer is assumed.

Use the proved mixed-Fresnel theorem from `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`. Consider one actual physical hub coordinate `X_0` and the remaining original-coordinate bank `X_L`, with quadratic part

`Q = a X_0^2 + 2 X_0 <g,X_L> + X_L^T(D + lambda s s^T)X_L + linear + constant`,

where `D` is arbitrary diagonal, `||s||_2=1`, and all one-dimensional densities are <=1. Put

`c=<g,s>`, `h=g-cs`, `tau=||h||_2`.

When `tau>0`, the mixed-Fresnel Gram matrix for the rows `w_l=(g_l,s_l)` is

`Gamma=[[||g||^2,c],[c,1]]`, so `det Gamma=tau^2`. The shear `(g_l,s_l)->(h_l,s_l)` leaves Brascamp-Lieb leverages invariant and diagonalizes the Gram. Hence the exact leverage identity is

`w_l^T Gamma^{-1} w_l = s_l^2 + h_l^2/tau^2`.

Therefore, if

`max_l (s_l^2+h_l^2/tau^2) <= 1/2`,

mixed Fresnel gives

`|phi_Q(t)| <= 4*pi^(3/2) |lambda|^(-1/2) tau^(-1) |t|^(-3/2)`.

Integrating `min(1,B|t|^(-3/2))` yields the candidate continuous-density estimate

`||p_Q||_infinity <= 3*4^(2/3) |lambda|^(-1/3) tau^(-2/3)`.

If the leverage gate fails, some physical residual coordinate l satisfies `s_l^2+h_l^2/tau^2>1/2`; hence either `|s_l|>1/2` or `|h_l|>tau/2`. Thus the failure is a genuine localized child coordinate or a genuine localized transverse star edge, rather than an unresolved diffuse Fourier case.

Next: verify constants and all affine/self-block scopes against the source theorem; formulate a scale-normalized transverse-hub corollary; apply the completed fleet04/B08 endpoint to an actual low-rank aligned family; then refresh corrections and publish the full report.
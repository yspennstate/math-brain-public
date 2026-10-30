# Addendum: sharpen the finite-heavy-core light exit from 1/2 to 1/32

Status: supporting exact-rank-three implication; full QFORM remains OPEN.

This applies Claude's proved Fresnel–Brascamp–Lieb Theorem F at `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837:proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md` to the finite-heavy-core compiler of fleet03/B16 r22 at `yspennstate/math-open-problems@980f2e67036908408a0c33b8eb6bf1a7e2f233e6:proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B16/20260923T022430Z-fleet03-B16-QFORM-r22/REPORT.md`.

Let the exact-rank-three matrix be `A=R Lambda R^T`, `R^TR=I_3`, `min |lambda_j(Lambda)|>=1`. Keep r22's heavy/light split

`H={i: c_i=||r_i||^2>1/64}`, `L=H^c`,

and let

`G_L=R_L^T R_L`, `g=lambda_min(G_L)`.

Condition on the original heavy coordinates `X_H`. The remaining law is still a cap-one product law and

`Q | X_H = X_L^T R_L Lambda R_L^T X_L + ell(X_H)^T X_L + const`.

Assume `g>0`. Normalize the light frame by

`U=R_L G_L^(-1/2)`, so `U^TU=I_3`,
`C=G_L^(1/2) Lambda G_L^(1/2)`.

Then

`R_L Lambda R_L^T = U C U^T`,
`s_min(C)>=g`.

The row leverage of the normalized frame satisfies, for every `i in L`,

`ell_i=(P_range(U))_ii=r_i^T G_L^(-1)r_i
 <= ||r_i||^2/g
 <= 1/(64 g)`.

Therefore, if

`g>=1/32`,

then every normalized light leverage is at most `1/2`. The scaled coefficient `C/g` has all three eigenvalues of modulus at least one. Claude Theorem F, with zero residual twist and the arbitrary conditional linear term retained, gives

`||p_((Q-const)/g | X_H)||_infinity <=12`.

Scaling back yields, uniformly in `X_H`,

`boxed: ||p_(Q | X_H)||_infinity <=12/g <=384.`

Averaging conditional densities gives

`boxed: ||p_Q||_infinity <=12/g <=384.`

The same Fourier theorem supplies a continuous conditional density; the uniform `12/g` bound allows dominated convergence over `X_H`, so the unconditional density is continuous.

This strictly strengthens Exit B in fleet03/B16 r22, which used the spectral-window theorem only when `g>=1/2` and obtained `<128`. After this addendum, failure of the light exit forces

`lambda_min(G_L)<1/32`,

hence, because `G_H=I_3-G_L`,

`lambda_max(G_H)>31/32`.

Thus the exact-rank-three residual finite heavy core is forced much closer to carrying an entire spectral direction than the previous `>1/2` statement. No moment, support, Gaussianity, or post-rotation independence assumption is introduced.

This still does not control the minority-sign curved pushforward when the surviving normalized light frame has a high-leverage row and `g<1/32`; that is part of the remaining near-null/high-overlap chamber.

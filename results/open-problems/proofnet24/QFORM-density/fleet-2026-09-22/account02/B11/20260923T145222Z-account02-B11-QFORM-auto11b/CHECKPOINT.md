# account02/B11 checkpoint — actual cross-cut from approximate null rulings

Programme: QFORM-DENSITY-3EIG-20260922. Status: substantive checkpoint only; full target open.

First unpaid implication attacked: `QFORM-NULL-RULING-TO-PRODUCT-CUT-v1` from the preceding account02/B11 run. Work in the exact-rank-three two-plane chamber

`R_S^T R_S=diag(1,rho,0)`, `R_T^T R_T=diag(0,1-rho,1)`, `m_22=0`, `A=RMR^T`, `s=min|eig(M)|`, and put `tau=min(rho,1-rho)`.

The preceding proved null-ruling lemma supplies nearest-line projections `r_i^*` with four projected line-cluster masses at least `rho/12,rho/12,(1-rho)/12,(1-rho)/12`, the two S-line angle satisfying `sin^2(theta_S)>=rho/9`, the two T-line angle satisfying `sin^2(theta_T)>=(1-rho)/9`, and total covariance errors controlled by `eta_S=2sqrt(2)*sqrt(D_S/kappa_S)+D_S/kappa_S` and the reflected `eta_T`.

New calculation: if `h=max_i ||r_i||^2 <= tau^3/165888` and `eta_S+eta_T <= tau^3/82944`, partition each of the four projected line clusters by its projected squared masses into two original-coordinate pieces. Since every projected weight is at most `h`, each piece has mass at least one quarter of its parent, hence at least `rho/48` or `(1-rho)/48`. For either resulting cut `C=I,J`, the projected S-plane Gram has

`lambda_min >= (rho/48)^2*(rho/9)/2 = rho^3/41472`,

and the projected T-plane Gram has the reflected bound. Therefore the full projected Gram is at least `tau^3/41472 I_3`. The actual-row covariance differs by at most `eta_S+eta_T`, so

`G_I,G_J >= gamma I_3`, `gamma=tau^3/82944`.

Moreover every constrained-side row leverage is at most `h/gamma<=1/2`. For the ACTUAL original-coordinate cross block `C=A[I,J]=R_I M R_J^T`, rank three gives

`Z=e_3(C^T C)=det(M)^2 det(G_I) det(G_J) >= s^6 gamma^6`.

Hence Claude's completed volume-sampling Theorem D at `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837` applies to the actual quadratic form, not a projected-row surrogate, and yields the provisional bound

`||p_Q||_infinity <= 6 sqrt(e)/(s gamma) = 497664 sqrt(e)/(s tau^3)`.

This is the first product-preserving compiler from quantitative approximate null-ruling clusters. It uses only an ORIGINAL-coordinate partition; no replacement of random quadratic coefficients by a small perturbation occurs. The row-diffuse hypothesis is still a real gap. A later full report will verify the volume-marginal identity, sign-specific ruled splice, and a matrix-cross-tail stability corollary.

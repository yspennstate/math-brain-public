# account02/B04 QFORM handoff addendum — rank-two random-cut exterior mass

Controlling addendum: `yspennstate/math-open-problems@ffc6e40587293d6019b29680fff19eb0d9179fb5:proofnet24/QFORM-density/fleet-2026-09-22/account02/B04/B04-20260922T152028Z-qform-r11/RANK2_RANDOM_CUT_ADDENDUM.md`.

New structural lemma `QFORM-RANK2-RANDOM-CUT-E2-v1`: if a rank-two residual has spectral frame `V` with maximum physical row leverage `rho<1/2`, then some fair coordinate cut `I,J` satisfies

`det(V_I^T V_I) det(V_J^T V_J) >= (1-2rho)/16`,

hence for residual eigenvalues `mu_1,mu_2` the physical cross block obeys

`E_2(B)>= (mu_1 mu_2)^2(1-2rho)/16`.

For the same cut the cross-range leverage is at most `16rho/(1-2rho)`. Thus if `rho<=1/34`, the partner regularized-determinant `q=1` gate holds automatically and `E_2(B)>=(mu_1mu_2)^2/17`.

Proof currency: wedge weights `w_ij=det(v_i,v_j)^2` have total mass one and weighted degree exactly `||v_i||^2`. Two independent wedge-edges are disjoint with probability at least `1-2rho`; a fair vertex cut separates any ordered disjoint edge pair with probability `1/16`. This yields the determinant product by expectation, then Cauchy--Binet gives the exact `E_2` identity.

Combined with the same-run aggregate Fourier theorem, any genuine original scalar square `a` and diffuse rank-two residual satisfy

`||p||_inf <= 16.0546222489 (|a| |mu_1mu_2|)^(-1/2)`.

For exact rank-three `A=U Lambda U^T`, pivot row `u_i` with `r_i=||u_i||^2`, `a_i=u_i Lambda u_i^T !=0`, and Schur projected leverage `rho_i=max_{j!=i}(||u_j||^2-<u_j,u_i>^2/r_i)<=1/34`, the Schur eigenvalue product is `mu_1mu_2=det(Lambda)r_i/a_i`, yielding

`||p||_inf <= 16.0546222489 (|det Lambda| r_i |a_i|)^(-1/4)`.

This completely pays the diffuse rank-two Schur subcase without a selected second singular value or an MSS partition. Full QFORM remains OPEN. First debt: heavy-Schur-range/tiny-or-zero-pivot aggregate routing.

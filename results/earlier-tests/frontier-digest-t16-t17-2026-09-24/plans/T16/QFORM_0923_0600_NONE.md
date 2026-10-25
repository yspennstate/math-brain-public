# Plan: bounded density of Q(X) with three large eigenvalues

## Orientation

For Gaussian X, |E e^{isQ}| ≤ (1 + 4s²)^{−3/4}, integrable. With two eigenvalues of opposite sign the density blows up logarithmically (2X₁X₂, X_i uniform), so three is sharp; the target is |φ_Q(s)| ≲ |s|^{−3/2} or a physical-space substitute. Reductions: by the bathtub principle X is uniform on E₁ × … × E_n with |E_i| = 1; and the statement should be proved for every quadratic polynomial with Hessian A, uniformly in the linear part. Translation and conditioning both create linear terms; uniformity in them makes conditioning free.

## First: the two extreme cases, in full (hours 1–2)

(a) Localized. In dimension m the density is at most C m^{3/2}. Cover R^m by the regions where |∂_iQ| ≥ |∇Q|/√m and use the coarea formula along e_i. Given X_{−i} there are at most two roots; |∇Q| ≥ 2 dist(P_V x, z₀), V spanned by three large eigenvectors; and moving x_i moves P_V x only along P_V e_i. The bound reduces to E|W − w|^{−1} for a two-dimensional projection W of X_{−i}: bounded density by Rudelson–Vershynin, and |w|^{−1} is integrable in two dimensions. That is where three enters. So if a principal block A_SS with |S| ≤ m₀ has three eigenvalues of modulus ≥ c, condition on X_{S^c} and stop.

(b) Delocalized. One Cauchy–Schwarz over a partition I ∪ J gives |φ_Q(s)|² ≤ E ∏_{i∈I} |φ_i(2s(A_IJ Z)_i)|, Z = X_J − X′_J; the diagonal blocks drop out. If A_IJ = U_I Λ U_Jᵀ with both halves well conditioned (a random partition, for spread eigenvectors), W = ΛU_JᵀZ has bounded density on R³, and Ball's geometric Brascamp–Lieb inequality with p_i = 1/c_i ≥ 2 (c_i the row leverages of U_I), together with ∫|φ_i|^p ≤ C p^{−1/2} (Rogozin, even p), gives |φ_Q(s)| ≲ s^{−3/2}. One Cauchy–Schwarz costs exactly a square root, and 3/2 > 1.

## Then the general matrix (hours 2–5)

(i) Remainder. A_IJ is rarely rank three, and W and the rest of A_IJ Z are dependent images of Z. I would instead write the decoupled quantity as one Brascamp–Lieb form on R^J, ∫ ∏_j g_j(z_j) ∏_i h_i(⟨b_i, z⟩) dz: g_j the density of Z_j, usable in every L^q; b_i the rows of A_IJ; h_i = |φ_i(2s·)| in L^{p_i}, ∑ 1/p_i = 3. Lieb's theorem reduces the constant to Gaussian inputs, where the analogous quantity det(I + 8s²BBᵀ)^{−1/2} depends only on the singular values of B = A_IJ, and extra ones help. Left over: a determinant inequality uniform in n, a partition keeping three spread singular values of order one, and rows of leverage above 1/2.

(ii) Mixed localization. Split by leverage: H = {i : |P_V e_i|² ≥ δ}, at most 3/δ coordinates. Conditionally on X_{H^c}, the heavy block should give a pointwise majorant centred at its vertex value (|t − c|^{−1/2} for one direction, logarithmic for two), and the vertex value is a Schur-complement quadratic in X_{H^c}. Inertia additivity (Haynsworth) is why the remaining directions pass to it; decoupling should give it a density in the dual L^p, and Hölder joins the two.

## Trying to break it, in parallel

Maximize P(Q ∈ [t, t+ε])/ε numerically for n ≤ 6 by coordinate ascent: with the other sets fixed, the best E_i is a superlevel set of x ↦ P(Q ∈ [t, t+ε] | X_i = x). Test lattice-like sets with integer A, a spread top eigenspace beside a huge fourth eigenvalue, and mixed localization.

## What I would avoid

Double Cauchy–Schwarz: it gives s^{−r/4} and needs five directions. Carbery–Wright: ε^{1/2} for quadratics, never a density. Using only bounded densities of projections: a uniform shell of radius R and thickness 1/(4πR²) in R³ has bounded density and marginals, yet |Y|² has density near 2πR, so product structure must enter explicitly. Rogozin-type rearrangement to intervals: the best position of E_i depends on the other coordinates (the vertex moves). CLT or Lindeberg: no moments, and a density needs every scale.

## First concrete step

Write (a) with constants and see whether the weights (∂_iQ)²/|∇Q|² improve m^{3/2}; write (b) including rows of leverage above 1/2; then state the form in (i) exactly and compute its Gaussian constant on an explicit rank-three-plus-remainder example.

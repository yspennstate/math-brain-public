# Plan: bounded density of quadratic forms with three large eigenvalues

Target. A statement that survives conditioning: for independent X_i with densities at most 1 and any p(x) = xᵀAx + bᵀx + c, the density of p(X) is at most C/σ₃(A), where σ₃ is the third largest |eigenvalue|. Conditioning on coordinates creates linear terms, so they are in from the start; the conjecture is the case b = c = 0.

Calibration. Three is sharp: 2X₁X₂ (eigenvalues ±1) has a logarithmic singularity at 0. The Gaussian case holds: by Ostrowski's theorem D^{1/2}AD^{1/2} (D ≥ I/2π the covariance) keeps three eigenvalues ≳ 1, a mean shift only lowers |φ|, and ∫(1 + cs²)^{-3/4} ds < ∞. Each large direction is worth |s|^{-1/2} of Fourier decay, equivalently a density in weak L², and three such densities convolve into L^∞ (O'Neil: L^{2,∞} * L^{2,1} ⊂ L^∞). I check every step against this bookkeeping.

Reductions. The probability of a window is multilinear in (f₁, …, fₙ), so by the bathtub principle each X_i may be uniform on a set of measure 1. Grid step functions and weak limits (a limit of laws with density ≤ C has density ≤ C) reduce further to finite unions of intervals.

First concrete step: the localized case. For n = 3 (all |λ| ≥ 1) write f(t) = ∫_{p=t} F/|∇p| dH², cut the level surface according to which partial derivative is largest, project each piece onto the other two coordinates (at most two preimages; |∂ₖp| ≥ |∇p|/√3 ≥ 2σ_min|x − x₀|/√3), drop fₖ ≤ 1 and rearrange each remaining variable. This should give f ≤ 12√3 log(1+√2)/σ_min(A) ≈ 18.3/σ_min(A). Then extend it to a large eigenspace carried by a bounded set H of heavy coordinates (at most 3/τ coordinates have leverage ≥ τ): condition on the light ones, which only moves the linear part, and handle blocks A_HH that are not uniformly invertible with Schur complements (Haynsworth inertia; the inverse of a Schur complement is a block of A⁻¹).

Delocalized case: Fourier. Split the coordinates at random into I and J and apply Cauchy–Schwarz once, duplicating X_I:

    |φ_p(s)|² ≤ E_U ∏_{j∈J} |φ_j(2s(A_JI U)_j)|,   U = X_I − X_I′.

If A_JI has three singular values ≳ 1 and light rows, the Rudelson–Vershynin bound for densities of projections of U, Ball's geometric Brascamp–Lieb inequality and the estimate ∫|φ_j|^q ≲ q^{-1/2} for q ≥ 2 (to be re-proved) give O(|s|⁻³), so φ_p is integrable. Expected obstacle: the small eigenvalues give A_JI extra singular values, and the projection density is not bounded fiberwise (for the cube that mixed norm is a zonotope volume, of order n^{3/2}). Plan: Brascamp–Lieb on all of U-space, with Lieb's theorem turning the constant into a determinant inequality over Gaussian inputs, tested numerically first.

Mixed case, probably the crux: some large directions on heavy coordinates, the rest delocalized, coupled by cross terms. Here I would prove the hierarchy P(|p(X) − t| ≤ ε) ≲ √ε, ε log(e/ε), ε for one, two, three large eigenvalues by induction: complete the square in a heavy direction and integrate the conditional bound (≤ |u|^{-1/2}) against the law of the Schur complement form, which carries the remaining directions.

In parallel, try to break it: alternating bathtub ascent (given the other sets, the best set for one coordinate is an exact super-level set) on forms in 3 to 8 variables, including zero-diagonal ones such as x₁x₂ + x₂x₃ + x₃x₁, lattice-like sets and heavy/light mixtures. If the supremum drifts upward with n, that is where a counterexample would live.

What I will avoid. Carbery–Wright: ε^{1/2} whatever the eigenvalue count, and only for log-concave laws. Invariance principles: they control distribution functions, not densities, and need small influences. A second Cauchy–Schwarz, to reach a genuine bilinear characteristic function: it halves the decay again and would need five large eigenvalues. Bounding ∫|φ| without Hölder: this fails already for one uniform variable, where |φ| ~ 1/|s|. Rearranging to intervals: δ(p − t) is not monotone. Conditioning on linear functionals: it destroys the product structure, and the sections can be needles along lines of the cone.

Order for the next hours: the n = 3 proof and the ascent code, then the heavy-coordinate extension, then the Fourier lemma with its Gaussian test, then the mixed hierarchy.

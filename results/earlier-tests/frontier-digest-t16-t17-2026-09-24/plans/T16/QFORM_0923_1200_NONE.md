# Plan: bounded density of quadratic forms with three large eigenvalues

Target: the full conjecture, ‖p_Q‖_∞ ≤ C uniformly in n, the laws and Q.

## 0. Set-up (first 30 minutes)
- Check what is published on densities of quadratic forms in vectors with bounded-density coordinates.
- By scaling the claim is ‖p_Q‖_∞ ≤ C/|λ_(3)|. I aim at the sign-blind Fourier form ∫|φ_Q| ≤ C/|λ_(3)|. For Gaussian X, |φ_Q(s)| = Π(1+4λ_j²s²)^{-1/4}: three large eigenvalues give integrable |s|^{-3/2}, two give |s|^{-1}, matching the log singularity of Y_1² − Y_2². The hypothesis ignores signs, which points to Fourier decay rather than a same-sign geometric argument.
- Sup density is convex in each law and the extreme densities f ≤ 1 are indicators of measure-one sets, so X_i may be uniform on finite unions of intervals. Rogozin's rearrangement has no known quadratic analogue, so lattice-like unions of short intervals stay in the test set.

## 1. First step: rank three, Ball's method with a chirp
Let Q = Σ_{j≤3} λ_j Y_j², Y = RᵀX, u_i ∈ R³ the rows of R; then Σ u_i u_iᵀ = I_3 and φ_Y(η) = Π_i φ_i(⟨u_i,η⟩). The Fresnel transform of e^{isq(y)} has constant modulus π^{3/2}|s|^{-3/2}Λ^{-1/2}, Λ = |λ_1λ_2λ_3| (Parseval via Gaussian damping), so |φ_Q(s)| ≤ (2π)^{-3}π^{3/2}|s|^{-3/2}Λ^{-1/2}‖φ_Y‖_1. If all |u_i|² ≤ 1/2, geometric Brascamp–Lieb with p_i = |u_i|^{-2} gives ‖φ_Y‖_1 ≤ Π_i (|u_i|^{-1}∫|φ_i|^{p_i})^{|u_i|²}, and ∫|φ_i|^p ≤ C p^{-1/2} for p ≥ 2: at p = 2k it is 2π times the density at 0 of a sum of 2k independent variables with densities ≤ 1, at most 2πk^{-1/2} (Rogozin plus Ball, in Bobkov–Chistyakov's form); interpolate. Expected outcome: the product is ≤ C³, so ‖p_Q‖_∞ ≲ Λ^{-1/3} ≤ 1/|λ_(3)|.

Heavy coordinates (|u_i|² > 1/2, at most five): conditioning on them only translates the chirp; directions the light rows miss are coordinate-like and go through Hausdorff–Young, since the density g of X_i² has g ≤ u^{-1/2} and ∫g = 1, so ‖g‖_{3/2} ≤ 2. This alone gives the diagonal case with constant 8.

Check numerically for n ≤ 10 (cube, unions of intervals). The argument should extend to every Q whose nonzero eigenvalues all have modulus ≥ 1: integrating min(1, C^k|s|^{-k/2}) absorbs C^k.

## 2. The real difficulty: eigenvalues of small modulus
At frequency s, put the directions with |sλ_j| ≥ π into the chirp (the top three are there once |s| ≳ 1/|λ_(3)|) and call the rest R_s. What is missing is a twisted bound ∫|E e^{isR_s(X) + i⟨η,PX⟩}| dη ≤ C^{dim}. It fails for an arbitrary unimodular function of the complementary projection (take the conjugate chirp of the fibre centres), so the proof must use that R_s is quadratic. Routes: (a) localised structure: condition on a 2×2 block and complete the square; an indefinite block leaves a log singularity at the saddle value, which is a Schur-complement form in the other coordinates, integrated against that form's density by induction (to check: the constant does not grow, and the complement keeps three large eigenvalues, which Haynsworth's inertia formula alone does not give); (b) spread structure: a random split of the coordinates making the phase linear in one half, then Brascamp–Lieb in that half.

In parallel, a counterexample search: the cube, n ≤ 12, with a remainder built to cancel q_E along the fibres.

## 3. What I would avoid
- Conditioning on the complement of the large eigenspace: the fibre-supremum bound costs Σ|2×2 minors| ~ n, and a fibre of the cube has diameter ~ n^{-1/2}, so the conditional density is ~ √n and the argument is circular.
- Marginal bounds for P_E X alone (Ball, Livshyts–Paouris–Pivovarov, Rudelson–Vershynin): a bounded density with bounded marginals can sit on a thin spherical shell.
- Decoupling, quadratic Littlewood–Offord, Carbery–Wright: they lose powers of ε.
- Invariance principles: macroscopic scales only, and they need moments the hypothesis does not give.
- The Gaussian proof, which uses independence of the Y_j.

Checkpoints: step 1 with constants in about 90 minutes; a route through step 2 chosen by hour three. A partial result is reported as partial.

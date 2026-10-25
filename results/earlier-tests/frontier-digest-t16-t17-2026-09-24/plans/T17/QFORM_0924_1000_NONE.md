# Research plan: bounded density of Q(X), three large eigenvalues

**Stance.** This is an open problem. I'll push toward the full proof the owner asks for, but I'll keep a ledger (proved / reduced / conjectural) and report only what is verified. Realistic session target: complete proofs in the "localized" regime, plus an isolated core lemma for the rest.

**0. Calibration (≈30 min).** Why first: these checks fix the mechanism. Each independent square has a weak-L² density, and L^{2,∞}∗L^{2,∞}⊄L^∞ explains why three are needed.
- Sharpness: 2U₁U₂ (eigenvalues ±1) has density ½log(2/s), and U² ~ s^{-1/2}. So three is necessary.
- Gaussians: |φ_Q(ξ)| ≲ (1+ξ²)^{-3/4} is integrable; two factors give only (1+ξ²)^{-1/2}.
- Diagonal A: λX_i² has density ≤|s|^{-1/2}, so it lies in L^q for q<2. Young and Hölder bound g₁∗g₂∗g₃, and the other eigenvalues enter as an independent convolution.
- Warning: a bounded density on ℝ³ can concentrate on a thin shell of radius R. So a bounded density for (⟨X,r_j⟩)_{j≤3} (Rudelson–Vershynin) is insufficient, and the product structure must enter through coordinate conditioning.

**1. Lossless reductions.**
- Mollify, and pass to limits by Portmanteau. This covers singular A and linear terms: Q+⟨b,x⟩ is a limit of forms in shifted variables, and shifts preserve the hypothesis.
- Complete the square on a block I: Q = (x_I+My)ᵀA_II(x_I+My) + S_I(y), where S_I is the Schur complement. Given y = X_{I^c}, this is the same problem for A_II. So a proper principal block with three large eigenvalues inherits the constant, and a minimal counterexample has none.
- S_I⁻¹ is a compression of A⁻¹, so Cauchy interlacing shows S_I keeps ≥3−|I| eigenvalues of modulus ≥1.

**2. Main line: a graded hierarchy.**
(H1) one large eigenvalue ⇒ sup_s E log₊(1/|Q−s|) ≤ C; (H2) two ⇒ sup_s E|Q−s|^{-1/2} ≤ C; (H3) three ⇒ bounded density.

Pivot building blocks, i.e. the conditional density of the pivot term, uniform in shifts:
- a 1×1 pivot gives |A_ii u|^{-1/2};
- a definite 2×2 pivot gives ≤π/√det (annulus area);
- an indefinite 2×2 pivot gives a log singularity (to prove).

A pivot of size p composed with level ℓ for S_I gives level ℓ+p.

(H1) in general: either some |A_ii| ≳ ‖A‖, a one-variable computation, or the off-diagonal part dominates. Then a random split I⊔J has ‖A_IJ‖ ≳ ‖A‖, and Costello–Tao–Vu decoupling with the √2 linear-form bound (Ball; Rogozin; Bobkov–Chistyakov) gives small-ball exponent ¼. That loss is harmless here.

Target theorem: (H3) with constant C_k whenever some k×k principal block has three eigenvalues ≥1. Inside the block, use Bunch–Kaufman-style 1×1/2×2 pivoting, with growth depending only on k.

**3. The crux: delocalized regime.**
Here no k×k block has three eigenvalues ≥c, so the large eigenvectors are spread and every pivot is weak. Ideas:
- (a) One Weyl differencing, |φ_Q(ξ)|² ≤ E_V|φ_{X_I}(2ξA_IJV)| with V = X_J−X_J′, costs only a square root. It closes if the linear forms have Gaussian-like Fourier decay and A_IJ has three large singular values. Get that decay from a local CLT for block sums of coordinates. Handle high frequencies with Plancherel (∫|φ_{X_i}|² ≤ 2π) and the Livshyts–Paouris–Pivovarov projection bounds.
- (b) Heavy tails, since no moments are assumed: use mixtures/conditioning, or show they only help.
- (c) Hunt for counterexamples here: rank 3, Hadamard eigenvectors, eigenvalues (1,1,−1), Cantor-like or heavy-tailed X_i. If the conjecture is false, it fails here.

**Approaches to avoid.**
- Carbery–Wright or polynomial Littlewood–Offord: degree 2 gives at best ε^{1/2}.
- Cauchy–Schwarz decoupling as a final step: it loses a power.
- Plain Esseen/Fourier: rough densities have no pointwise decay.
- Götze-type double symmetrization: it loses a square root per step and likely needs ≳5 large directions; sub-case tool only.
- Invariance principles: they need moments and control CDFs, not densities.
- Anything that sees only the top-3 projection density, which the shell example refutes.

**First concrete step.** Fully prove the block-conditioning/interlacing lemma, the three pivot building blocks (especially the log bound for indefinite 2×2 blocks under arbitrary shifts), and (H1). Assemble the k-block theorem. Then run the pipeline on the Hadamard rank-3 model to see exactly where it fails.

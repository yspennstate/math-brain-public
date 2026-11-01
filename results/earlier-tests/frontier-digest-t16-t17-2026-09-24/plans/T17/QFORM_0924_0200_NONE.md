# Research plan: bounded-density conjecture for quadratic forms

**Goal and ground rules.** The owner wants a full proof. I will push for one, keeping a ledger of proven versus conjectural steps, and will report that ledger as it stands. No step counts as proven until it is written out with explicit constants.

## 1. Orientation (first hour)
- **Gaussian model.** For Gaussian X, |φ_Q(t)| = ∏(1+4λ_j²t²)^{-1/4}, so three factors with |λ_j| ≥ 1 already give ∫|φ_Q| ≤ C. Each big eigenvalue buys half a power of decay: Y² alone has a t^{-1/2} singularity, and 2X₁X₂ a log one. So "three" is sharp, and the proof must count half-powers.
- **Reformulation.** The density at t equals ∫_{Q=t} ∏f_i(x_i) dσ/(2|Ax|). This is a curved analogue of cube slicing; the linear case is the Bobkov–Chistyakov √2 bound.
- **Reductions.** An extreme-point argument reduces to X_i uniform on sets of measure 1. Perturbing A on its kernel makes it invertible, and density bounds pass to weak limits.

## 2. Results to build on
- Ball's cube slicing; the geometric Brascamp–Lieb inequality (Ball, Barthe).
- Rogozin and Bobkov–Chistyakov: a unit linear form of X has density ≤ √2.
- Rudelson–Vershynin: rank-d projections of X have density ≤ C^d, independent of n (sharp constants: Livshyts–Paouris–Pivovarov).
- Schur complement tools: Haynsworth inertia additivity, Cauchy interlacing (S⁻¹ is a principal submatrix of A⁻¹), and Bunch–Kaufman 1×1/2×2 pivoting.

## 3. First line of attack: pivot induction on n
**Why first:** it is cheap, gives a dimension-free constant, and isolates the real difficulty.

Pivot on a coordinate with a = a_ii ≠ 0. Then Q = a(X_i+β(X'))² + S(X'), where S is the Schur complement and X_i is independent of X'. Expected bound: M_Q ≤ |a|^{-1/2} sup_t E|t−S(X')|^{-1/2} ≤ 4√(M_S/|a|). The square root makes the induction self-improving. If M_S ≤ C and |a| ≥ 16/C, then M_Q ≤ C, so constants do not pile up with n. A 2×2 pivot on a large off-diagonal entry (a log-singular product term) should give a similar bound, with log M_S in place of √M_S.

Interlacing shows that S loses at most one big eigenvalue. So I will prove a hierarchy simultaneously: k big eigenvalues ⇒ P(|Q−t| ≤ ε) ≤ C_k ψ_k(ε), with ψ₁ = √ε, ψ₂ = ε·log(e/ε), ψ₃ = ε. The pivot term contributes √ε, uniformly in its shift.

Target: reduce the conjecture to the **flat regime** max|a_ij| < δ₀, with δ₀ fixed by the final constant.

## 4. The crux: flat matrices
With every entry small, pivoting is useless, and heuristically Q(X) behaves like the Gaussian model. Plan:
1. Condition on a random half J of the coordinates: Q = X_Iᵀ A_II X_I + ⟨2A_IJ X_J, X_I⟩ + c.
2. Apply the projection bounds to the random coefficient vector.
3. Compare with the Gaussian model by Lindeberg replacement, down to a scale ε₀(δ₀).
4. Handle smaller scales separately.

Risks: heavy tails (a bounded density gives no moments) and the smallest scales. If the conjecture is false, a counterexample should live here. So I will first run small-n numerics on flat, mixed-sign forms with X_i uniform on unions of intervals.

## 5. Approaches to avoid
- **Rotating to eigen-coordinates.** It destroys independence and works only for Gaussians.
- **Pointwise Fourier decay and Esseen.** Bounded densities give no pointwise decay of φ, and Esseen loses a log even for linear forms. Use only L^p Fourier bounds (Hölder, Hausdorff–Young, Brascamp–Lieb).
- **Decoupling (Costello–Tao–Vu style) and Carbery–Wright.** They lose a square root or need log-concavity, and give only ε^{1/2}.
- **Inductions that lose a constant factor per step.**

## 6. First concrete step
Write out the 1×1 pivot lemma rigorously, with explicit constants, and test it on x₁²+x₂²+x₃² and x₁²+2x₂x₃. Next, prove the diagonal case as a warm-up: ∫|φ₁φ₂φ₃| ≤ ∏‖φ_j‖₃ ≲ ∏‖g_j‖_{3/2}, where g_j is the density of λ_jX_j², and the product is bounded uniformly when |λ_j| ≥ 1. Then prove the interlacing bookkeeping lemma for 1×1 and 2×2 pivots.

If the flat regime does not close, I will deliver the reduction and special cases, clearly labeled, without claiming a full proof.

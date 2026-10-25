# Plan: bounded-density conjecture for quadratic forms

**Goal (owner's):** a complete proof. I will push for it, but I will only write down steps I have checked. If the full statement does not fall this session, I will hand over rigorous partial theorems plus an exact description of the remaining gap.

## 0. Calibration: why three
- 2X₁X₂ (eigenvalues ±1) with uniform inputs has a log-singular density, so two large eigenvalues are not enough.
- For Gaussian X, |E e^{isQ}| = ∏(1+4λ_j²s²)^{-1/4}. This is integrable iff at least 3 eigenvalues are nonzero, and uniformly so once three have |λ| ≥ 1.
- Heuristic: each large direction gives s^{-1/2} of Fourier decay, i.e. a |w|^{-1/2} singularity. Two directions give a log singularity; three give a bounded density.

## 1. Reductions (first hour)
- P(|Q−t|≤ε) is multilinear in (f_k), so WLOG each X_k is uniform on a set of measure 1.
- Translating X_k keeps the hypotheses, so linear terms in range(A) are free. I will work with quadratic *polynomials*, which conditioning needs. I still have to check that linear terms in ker A cannot hurt.
- Independent summands can be dropped, since convolution does not raise the sup of the density.
- Graded family, proved jointly (k = number of eigenvalues with |λ| ≥ 1):
  - **P₁:** sup_t P(|Q−t|<η) ≤ C√η
  - **P₂:** ≤ Cη·log(e/η)
  - **P₃:** ≤ Cη

## 2. Line A: localized directions (try first; it is elementary and gives the induction)
- **Elimination.** Suppose |a_ii| ≥ c. Condition on X_{−i} and complete the square in x_i.
  - The fiber {y : |a_ii y² − u| ≤ ε} has measure ≲ min(√(ε/|a_ii|), ε/√(|a_ii||u|)).
  - So P_k(A) reduces to a bound on E|S(X_{−i})−u|^{−1/2}, where S is the Schur complement.
  - Courant–Fischer (S is a min/max over x_i) shows S keeps at least (number of large eigenvalues − 1). So P_{k−1}(S) ⇒ P_k(A).
  - This covers diagonal forms and forms that stay localized after each elimination.
- **Coarea lemma.** Suppose a principal submatrix A_II with |I| ≤ k₀ has all |eigenvalues| ≥ c.
  - Condition on X_{I^c} and use |∇Q| ≥ 2c|x|.
  - Write the level set as graphs over coordinate hyperplanes, and use E|X_{I∖i}|^{−1} < ∞ (dimension ≥ 2).
  - This covers zero-diagonal forms such as xᵀ(J−I)x and 2X₁X₂+2X₃X₄.

## 3. Line B: spread case (all |a_ii| small)
By Esseen's inequality, it is enough to get averaged decay of φ_Q.
- **Rank-3 core.** Fresnel (Hubbard–Stratonovich) linearization of the three large directions gives |φ_Q(s)| ≲ |s|^{−3/2}∫_{ℝ³}∏_k|φ_k(⟨u,R_k⟩)|du.
  - Bound the integral with geometric Brascamp–Lieb (weights ℓ_k = |R_k|²), Plancherel, and the Ball-type bound ∫|φ_k|^p ≤ Cp^{−1/2} for p ≥ 2 (from Rogozin plus the √2 bound of Ball / Bobkov–Chistyakov).
  - This needs ℓ_k ≤ ½. At most five coordinates break that; condition on them or treat them with Line A.
- **General case.** Decoupling gives |φ_Q|² ≤ E_W∏_{k∈I}|φ_k(2s(A_IJ W)_k)|. Combine this with marginal-density bounds for linear images of product measures (Rudelson–Vershynin; Livshyts–Paouris–Pivovarov).

## 4. Expected obstacles
- **Mixed regime**, e.g. X₁² + ⟨X,u⟩² + ⟨X,v⟩² with u, v delocalized. Plan: Line A on X₁, then Line B for P₂ of S.
- **Extra eigen-directions** beyond the three stay inside the expectation in the Fresnel route.
- **Small singular values of A_IJ.** Conditional densities of projections can be unbounded.
- **Squaring loses a square root.** For 2X₁X₂+2X₃X₄+2X₅X₆ it only gives |φ| ≲ s^{−3/4}. Rule: never decouple in localized regimes.
- **Main missing piece:** a dichotomy lemma saying every A splits into a coordinate-localized block plus a leverage-spread block, with controlled interaction.

## 5. Approaches to avoid
- **Carbery–Wright and log-concave tools:** they give η^{1/2}, not η, and the inputs here are not log-concave.
- **Rearrangement (Rogozin, Brascamp–Lieb–Luttinger):** the level sets of Q are shells or hyperboloids, not convex.
- **CLT, Berry–Esseen, Lindeberg:** they see nothing at small scales, and comb-like densities break them.
- **Pointwise decay of a single φ_k:** false for rough densities. Only averaged decay can be used.
- **Combinatorial quadratic Littlewood–Offord methods:** built for discrete atoms and too lossy for sharp density bounds.

## 6. First concrete step
Write out and check the elimination lemma in full, with explicit constants:
- the fiber bound;
- the count of large eigenvalues kept by the Schur complement;
- the chain P₁→P₂→P₃ for diagonal forms.

In parallel, run a small numerical search over grid-indicator densities (n = 3–6) for xᵀ(J−I)x and the mixed example. The aim is to find any counterexample before investing in Line B.

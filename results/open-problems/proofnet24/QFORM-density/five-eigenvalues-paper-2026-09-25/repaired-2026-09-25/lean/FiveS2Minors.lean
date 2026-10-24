import Mathlib.Tactic
import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.LinearAlgebra.Matrix.SchurComplement
import Mathlib.RingTheory.Polynomial.Vieta
import Mathlib.Data.Fintype.Powerset
import Mathlib.GroupTheory.Perm.Sign
import Mathlib.Analysis.Matrix.Spectrum
import Mathlib.Algebra.Polynomial.Coeff

/-!
Lemma 2.7(a) of "Quadratic forms with five large singular values have bounded densities" (repaired text,
sha256 90f859b7): for `M ∈ ℝ^{I×J}` and `ℓ ≥ 1`,
`e_ℓ(M Mᵀ) = ∑_{|T| = ℓ} Θ(T) = ∑_{|S| = |T| = ℓ} det(M_{S,T})²`, with `Θ(T) = det(M_T M_Tᵀ)`.

Mathlib has neither the principal-minor expansion nor the Cauchy-Binet formula, so both are proved here.

* `det_diagonal_add`: `det(diag d + M) = ∑_T (∏_{i ∉ T} d_i) det(M_{TT})` over any commutative ring, from the
  Leibniz formula: a permutation contributes to the `T`-term only if it fixes every point outside `T`, and those
  permutations are exactly the permutations of `T` (`perm_fix_compl_mem_range`).
* `det_one_add_X_smul`: `det(1 + X K) = ∑_T det(K_{TT}) X^{|T|}` in `R[X]`, so the coefficient of `X^m` is the sum of
  the principal `m × m` minors (`coeff_sum_card`).
* `det_one_add_X_smul_hermitian`: for real symmetric `G` with eigenvalues `λ_i`, `det(1 + X G) = ∏_i (λ_i X + 1)`,
  from `G = U diag(λ) Uᵀ` with `U Uᵀ = 1`.
* `sum_principal_minors_eq_esymm`: the sum of the principal `m × m` minors of `G` is `e_m(λ)`.
* `lemma27a_first`: `e_m(M Mᵀ) = ∑_{|T| = m} det(M_T M_Tᵀ)`; the left side is literally the quantity `Evol M hG m` of
  `../../lean/QformFive3.lean`, where Proposition 6.4 ends.
* `cauchy_binet_gram`: `det(A Aᵀ) = ∑_{S ⊆ κ, |S| = |τ|} det(A_{·S}ᵀ A_{·S})` for `A ∈ R^{τ×κ}`, from
  `det(1 + X A Aᵀ) = det(1 + X Aᵀ A)` (Sylvester, `Matrix.det_one_add_mul_comm`) and the coefficient of `X^{|τ|}`.
* `det_transpose_mul_self_eq_sq`: for `|S| = |τ|` and any identification `e : τ ≃ S` of rows with columns,
  `det(A_{·S}ᵀ A_{·S}) = det(A_{·S})²`; the right side is the paper's `det(M_{T,S})²`, whatever order is used on `S`.
* `lemma27a_full`: `e_m(M Mᵀ) = ∑_{|T| = m} ∑_{|S| = m} det(M_{T,S}ᵀ M_{T,S})`, the whole of Lemma 2.7(a).
-/

open Matrix Finset Polynomial

namespace QformFiveB

section Expansion

variable {n : Type*} [Fintype n] [DecidableEq n] {R : Type*} [CommRing R]

/-- One Leibniz term of `det(diag d + M)`, expanded over the set `T` of the factors taken from `M`. -/
theorem perm_prod_expand (d : n → R) (M : Matrix n n R) (σ : Equiv.Perm n) :
    ∏ i, (diagonal d + M) (σ i) i
      = ∑ T : Finset n, (∏ i ∈ T, M (σ i) i) * ∏ i ∈ Tᶜ, diagonal d (σ i) i := by
  calc ∏ i, (diagonal d + M) (σ i) i = ∏ i, (M (σ i) i + diagonal d (σ i) i) :=
        Finset.prod_congr rfl (fun i _ => by rw [Matrix.add_apply, add_comm])
    _ = ∑ T : Finset n, (∏ i ∈ T, M (σ i) i) * ∏ i ∈ Tᶜ, diagonal d (σ i) i := by
        rw [Finset.prod_add, Finset.powerset_univ]
        simp only [Finset.compl_eq_univ_sdiff]

/-- A permutation fixing every point outside `T` is the extension of a permutation of `T`. -/
theorem perm_fix_compl_mem_range (T : Finset n) (σ : Equiv.Perm n) (hfix : ∀ i ∈ Tᶜ, σ i = i) :
    σ ∈ Set.range (fun τ : Equiv.Perm T => Equiv.Perm.ofSubtype τ) := by
  have h₁ : ∀ x, σ x ∈ T ↔ x ∈ T := by
    intro x
    constructor
    · intro hx
      by_contra hxT
      have h := hfix x (Finset.mem_compl.mpr hxT)
      rw [h] at hx
      exact hxT hx
    · intro hx
      by_contra hσx
      have h2 := hfix (σ x) (Finset.mem_compl.mpr hσx)
      have h3 : σ x = x := σ.injective h2
      rw [h3] at hσx
      exact hσx hx
  refine ⟨σ.subtypePerm h₁, ?_⟩
  exact Equiv.Perm.ofSubtype_subtypePerm h₁ (fun x hx => by
    by_contra hxT
    exact hx (hfix x (Finset.mem_compl.mpr hxT)))

/-- **Principal-minor expansion.** `det(diag d + M) = ∑_T (∏_{i ∉ T} d_i) det(M_{TT})`. -/
theorem det_diagonal_add (d : n → R) (M : Matrix n n R) :
    (diagonal d + M).det
      = ∑ T : Finset n, (∏ i ∈ Tᶜ, d i) * (M.submatrix ((↑) : T → n) ((↑) : T → n)).det := by
  rw [det_apply']
  simp_rw [perm_prod_expand d M, Finset.mul_sum]
  rw [Finset.sum_comm]
  refine Finset.sum_congr rfl (fun T _ => ?_)
  rw [det_apply', Finset.mul_sum]
  symm
  refine Fintype.sum_of_injective (fun τ : Equiv.Perm T => Equiv.Perm.ofSubtype τ)
    Equiv.Perm.ofSubtype_injective _ _ ?_ ?_
  · intro σ hσ
    dsimp only
    have hex : ∃ i ∈ Tᶜ, σ i ≠ i := by
      by_contra hcon
      push Not at hcon
      exact hσ (perm_fix_compl_mem_range T σ hcon)
    obtain ⟨i, hi, hσi⟩ := hex
    have hz : ∏ j ∈ Tᶜ, diagonal d (σ j) j = 0 :=
      Finset.prod_eq_zero hi (diagonal_apply_ne d hσi)
    rw [hz, mul_zero, mul_zero]
  · intro τ
    dsimp only
    have h1 : ∏ i ∈ Tᶜ, diagonal d (Equiv.Perm.ofSubtype τ i) i = ∏ i ∈ Tᶜ, d i := by
      refine Finset.prod_congr rfl (fun i hi => ?_)
      rw [Equiv.Perm.ofSubtype_apply_of_not_mem τ (Finset.mem_compl.mp hi), diagonal_apply_eq]
    have h2 : ∏ i ∈ T, M (Equiv.Perm.ofSubtype τ i) i
        = ∏ j : T, M.submatrix ((↑) : T → n) ((↑) : T → n) (τ j) j := by
      rw [← Finset.prod_coe_sort T (fun i => M (Equiv.Perm.ofSubtype τ i) i)]
      refine Finset.prod_congr rfl (fun j _ => ?_)
      simp only [Equiv.Perm.ofSubtype_apply_coe, Matrix.submatrix_apply]
    rw [Equiv.Perm.sign_ofSubtype, h1, h2]
    ring

/-- The coefficient of `X^m` in `∑_T C(a_T) X^{|T|}` is the sum of `a_T` over the `m`-element sets `T`. -/
theorem coeff_sum_card (a : Finset n → R) (m : ℕ) :
    (∑ T : Finset n, C (a T) * X ^ T.card).coeff m = ∑ T ∈ (univ : Finset n).powersetCard m, a T := by
  rw [Polynomial.finset_sum_coeff, Finset.powersetCard_eq_filter, Finset.powerset_univ,
    Finset.sum_filter]
  refine Finset.sum_congr rfl (fun T _ => ?_)
  rw [Polynomial.coeff_C_mul_X_pow]
  by_cases h : T.card = m
  · rw [if_pos h.symm, if_pos h]
  · rw [if_neg (fun h' => h h'.symm), if_neg h]

/-- `det(1 + X K) = ∑_T det(K_{TT}) X^{|T|}` in `R[X]`. -/
theorem det_one_add_X_smul (K : Matrix n n R) :
    (1 + (X : R[X]) • K.map C).det
      = ∑ T : Finset n, C (K.submatrix ((↑) : T → n) ((↑) : T → n)).det * X ^ T.card := by
  have h := det_diagonal_add (fun _ => (1 : R[X])) ((X : R[X]) • K.map C)
  rw [diagonal_one] at h
  rw [h]
  refine Finset.sum_congr rfl (fun T _ => ?_)
  have hs : ((X : R[X]) • K.map C).submatrix ((↑) : T → n) ((↑) : T → n)
      = (X : R[X]) • (K.submatrix ((↑) : T → n) ((↑) : T → n)).map C := by
    ext i j
    simp
  simp only [Finset.prod_const_one, one_mul]
  rw [hs, det_smul, Fintype.card_coe, ← RingHom.mapMatrix_apply, ← RingHom.map_det]
  ring

end Expansion

section Spectral

variable {n : Type*} [Fintype n] [DecidableEq n]

theorem minors_star_eq_transpose (M : Matrix n n ℝ) : star M = Mᵀ := by
  rw [Matrix.star_eq_conjTranspose, Matrix.conjTranspose_eq_transpose_of_trivial]

theorem minors_orth (A : Matrix n n ℝ) (hA : A.IsHermitian) :
    (hA.eigenvectorUnitary : Matrix n n ℝ) * (hA.eigenvectorUnitary : Matrix n n ℝ)ᵀ = 1 := by
  have h := Unitary.coe_mul_star_self hA.eigenvectorUnitary
  rw [Unitary.coe_star, minors_star_eq_transpose] at h
  exact h

/-- The spectral theorem in the form `A U = U diag(λ)`. -/
theorem minors_eigen (A : Matrix n n ℝ) (hA : A.IsHermitian) :
    A * (hA.eigenvectorUnitary : Matrix n n ℝ)
      = (hA.eigenvectorUnitary : Matrix n n ℝ) * diagonal hA.eigenvalues := by
  ext i j
  have h := congrFun (hA.mulVec_eigenvectorBasis j) i
  simp only [Matrix.mulVec, dotProduct, Pi.smul_apply, smul_eq_mul] at h
  rw [Matrix.mul_diagonal, Matrix.mul_apply]
  simp only [IsHermitian.eigenvectorUnitary_apply]
  rw [h, mul_comm]

/-- If `G = U diag(λ) Uᵀ` with `U Uᵀ = 1`, then `det(1 + X G) = ∏_i (λ_i X + 1)`. -/
theorem det_one_add_X_smul_of_decomp (G U : Matrix n n ℝ) (lam : n → ℝ) (hUU : U * Uᵀ = 1)
    (hG : G = U * diagonal lam * Uᵀ) :
    (1 + (X : ℝ[X]) • G.map C).det = ∏ i, (C (lam i) * X + 1) := by
  subst hG
  have hVW : U.map C * Uᵀ.map C = 1 := by
    rw [← Matrix.map_mul, hUU, Matrix.map_one _ (map_zero C) (map_one C)]
  have hsplit : 1 + (X : ℝ[X]) • (U * diagonal lam * Uᵀ).map C
      = U.map C * (1 + (X : ℝ[X]) • diagonal (fun i => C (lam i))) * Uᵀ.map C := by
    rw [Matrix.map_mul, Matrix.map_mul, diagonal_map (map_zero C), Matrix.mul_add, Matrix.add_mul,
      Matrix.mul_one, hVW, Matrix.mul_smul, Matrix.smul_mul]
  have hdiag : (1 : Matrix n n ℝ[X]) + (X : ℝ[X]) • diagonal (fun i => C (lam i))
      = diagonal (fun i => C (lam i) * X + 1) := by
    ext i j
    by_cases h : i = j
    · subst h
      simp only [Matrix.add_apply, Matrix.one_apply_eq, Matrix.smul_apply, diagonal_apply_eq,
        smul_eq_mul]
      ring
    · simp only [Matrix.add_apply, Matrix.one_apply_ne h, Matrix.smul_apply, diagonal_apply_ne _ h,
        smul_zero, add_zero]
  have hdet : (U.map C).det * (Uᵀ.map C).det = 1 := by rw [← det_mul, hVW, det_one]
  rw [hsplit, det_mul, det_mul, hdiag, det_diagonal]
  linear_combination (∏ i, (C (lam i) * X + 1)) * hdet

/-- For real symmetric `G` with eigenvalues `λ_i`: `det(1 + X G) = ∏_i (λ_i X + 1)`. -/
theorem det_one_add_X_smul_hermitian (G : Matrix n n ℝ) (hG : G.IsHermitian) :
    (1 + (X : ℝ[X]) • G.map C).det = ∏ i, (C (hG.eigenvalues i) * X + 1) := by
  apply det_one_add_X_smul_of_decomp G (hG.eigenvectorUnitary : Matrix n n ℝ) hG.eigenvalues
    (minors_orth G hG)
  calc G = G * ((hG.eigenvectorUnitary : Matrix n n ℝ) * (hG.eigenvectorUnitary : Matrix n n ℝ)ᵀ) := by
        rw [minors_orth G hG, Matrix.mul_one]
    _ = G * (hG.eigenvectorUnitary : Matrix n n ℝ) * (hG.eigenvectorUnitary : Matrix n n ℝ)ᵀ := by
        rw [Matrix.mul_assoc]
    _ = _ := by rw [minors_eigen G hG]

/-- `∏_i (λ_i X + 1) = ∑_t (∏_{i ∈ t} λ_i) X^{|t|}`. -/
theorem prod_C_mul_X_add_one (lam : n → ℝ) :
    ∏ i, (C (lam i) * X + 1) = ∑ t : Finset n, C (∏ i ∈ t, lam i) * X ^ t.card := by
  rw [Finset.prod_add, Finset.powerset_univ]
  refine Finset.sum_congr rfl (fun t _ => ?_)
  rw [Finset.prod_const_one, mul_one, Finset.prod_mul_distrib, Finset.prod_const, map_prod C lam t]

/-- **The sum of the principal `m × m` minors of a real symmetric matrix is `e_m` of its eigenvalues.** -/
theorem sum_principal_minors_eq_esymm (G : Matrix n n ℝ) (hG : G.IsHermitian) (m : ℕ) :
    ∑ T ∈ (univ : Finset n).powersetCard m, (G.submatrix ((↑) : T → n) ((↑) : T → n)).det
      = ∑ t ∈ (univ : Finset n).powersetCard m, ∏ i ∈ t, hG.eigenvalues i := by
  have h1 := det_one_add_X_smul G
  rw [det_one_add_X_smul_hermitian G hG, prod_C_mul_X_add_one] at h1
  have h2 : (∑ t : Finset n, C (∏ i ∈ t, hG.eigenvalues i) * X ^ t.card).coeff m
      = (∑ T : Finset n, C (G.submatrix ((↑) : T → n) ((↑) : T → n)).det * X ^ T.card).coeff m := by
    rw [h1]
  rw [coeff_sum_card, coeff_sum_card] at h2
  exact h2.symm

end Spectral

section Gram

/-- `(M Mᵀ)_{TT} = M_T M_Tᵀ`. -/
theorem gram_submatrix_eq {ι κ α : Type*} [Fintype κ] (M : Matrix ι κ ℝ) (e : α → ι) :
    (M * Mᵀ).submatrix e e = M.submatrix e id * (M.submatrix e id)ᵀ := by
  ext i j
  simp [Matrix.mul_apply]

/-- **Lemma 2.7(a), first equality.** `e_m(M Mᵀ) = ∑_{|T| = m} Θ(T)` with `Θ(T) = det(M_T M_Tᵀ)`. The left side is
`Evol M hG m` of `QformFive3.lean`. -/
theorem lemma27a_first {ι κ : Type*} [Fintype ι] [DecidableEq ι] [Fintype κ] (M : Matrix ι κ ℝ)
    (hG : (M * Mᵀ).IsHermitian) (m : ℕ) :
    ∑ t ∈ (univ : Finset ι).powersetCard m, ∏ i ∈ t, hG.eigenvalues i
      = ∑ T ∈ (univ : Finset ι).powersetCard m,
          (M.submatrix ((↑) : T → ι) id * (M.submatrix ((↑) : T → ι) id)ᵀ).det := by
  rw [← sum_principal_minors_eq_esymm (M * Mᵀ) hG m]
  refine Finset.sum_congr rfl (fun T _ => ?_)
  rw [gram_submatrix_eq]

variable {R : Type*} [CommRing R]

/-- **Cauchy-Binet, Gram form.** For `A ∈ R^{τ×κ}`, `det(A Aᵀ) = ∑_{S ⊆ κ, |S| = |τ|} det(A_{·S}ᵀ A_{·S})`. -/
theorem cauchy_binet_gram {τ κ : Type*} [Fintype τ] [DecidableEq τ] [Fintype κ] [DecidableEq κ]
    (A : Matrix τ κ R) :
    (A * Aᵀ).det = ∑ S ∈ (univ : Finset κ).powersetCard (Fintype.card τ),
      ((A.submatrix id ((↑) : S → κ))ᵀ * A.submatrix id ((↑) : S → κ)).det := by
  have hsyl : (1 + (X : R[X]) • (A * Aᵀ).map C).det = (1 + (X : R[X]) • (Aᵀ * A).map C).det := by
    have e1 : (X : R[X]) • (A * Aᵀ).map C = ((X : R[X]) • A.map C) * Aᵀ.map C := by
      rw [Matrix.map_mul, Matrix.smul_mul]
    have e2 : (X : R[X]) • (Aᵀ * A).map C = Aᵀ.map C * ((X : R[X]) • A.map C) := by
      rw [Matrix.map_mul, Matrix.mul_smul]
    rw [e1, e2]
    exact det_one_add_mul_comm _ _
  rw [det_one_add_X_smul, det_one_add_X_smul] at hsyl
  have h2 : (∑ T : Finset τ, C ((A * Aᵀ).submatrix ((↑) : T → τ) ((↑) : T → τ)).det * X ^ T.card).coeff
        (Fintype.card τ)
      = (∑ S : Finset κ, C ((Aᵀ * A).submatrix ((↑) : S → κ) ((↑) : S → κ)).det * X ^ S.card).coeff
        (Fintype.card τ) := by
    rw [hsyl]
  rw [coeff_sum_card, coeff_sum_card] at h2
  have hL : (univ : Finset τ).powersetCard (Fintype.card τ) = {univ} := by
    rw [← Finset.card_univ, Finset.powersetCard_self]
  rw [hL, Finset.sum_singleton] at h2
  have hU : ∀ M' : Matrix τ τ R,
      (M'.submatrix (Subtype.val : {x // x ∈ (univ : Finset τ)} → τ) Subtype.val).det = M'.det :=
    fun M' => det_submatrix_equiv_self (Equiv.subtypeUnivEquiv Finset.mem_univ) M'
  rw [hU] at h2
  rw [h2]
  refine Finset.sum_congr rfl (fun S _ => ?_)
  congr 1

/-- For `|S| = |τ|` and any identification `e : τ ≃ S` of the rows with the columns, `det(Bᵀ B) = det(B)²`, where
`B` is read as a square matrix through `e`. -/
theorem det_transpose_mul_self_eq_sq {τ σ : Type*} [Fintype τ] [DecidableEq τ] [Fintype σ]
    [DecidableEq σ] (B : Matrix τ σ R) (e : τ ≃ σ) :
    (Bᵀ * B).det = (B.submatrix id e).det ^ 2 := by
  rw [← det_submatrix_equiv_self e (Bᵀ * B)]
  have h : (Bᵀ * B).submatrix e e = (B.submatrix id e)ᵀ * B.submatrix id e := by
    ext i j
    simp [Matrix.mul_apply]
  rw [h, det_mul, det_transpose, sq]

/-- **Lemma 2.7(a).** `e_m(M Mᵀ) = ∑_{|T| = m} Θ(T) = ∑_{|T| = m} ∑_{|S| = m} det(M_{T,S}ᵀ M_{T,S})`, and each
summand of the double sum is `det(M_{T,S})²` (`det_transpose_mul_self_eq_sq`). -/
theorem lemma27a_full {ι κ : Type*} [Fintype ι] [DecidableEq ι] [Fintype κ] [DecidableEq κ]
    (M : Matrix ι κ ℝ) (hG : (M * Mᵀ).IsHermitian) (m : ℕ) :
    ∑ t ∈ (univ : Finset ι).powersetCard m, ∏ i ∈ t, hG.eigenvalues i
      = ∑ T ∈ (univ : Finset ι).powersetCard m, ∑ S ∈ (univ : Finset κ).powersetCard m,
          ((M.submatrix ((↑) : T → ι) ((↑) : S → κ))ᵀ * M.submatrix ((↑) : T → ι) ((↑) : S → κ)).det := by
  rw [lemma27a_first M hG m]
  refine Finset.sum_congr rfl (fun T hT => ?_)
  have hcard : Fintype.card T = m := by
    rw [Fintype.card_coe]
    exact (Finset.mem_powersetCard.mp hT).2
  rw [cauchy_binet_gram, hcard]
  rfl

end Gram

end QformFiveB

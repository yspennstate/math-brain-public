import Mathlib.Analysis.Matrix.Spectrum
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.Convex.SpecificFunctions.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Data.Real.StarOrdered
import Mathlib.Tactic

/-!
Theorem 3.1 of "Quadratic forms with five large singular values have bounded densities" (repaired text, sha256
90f859b7), the geometric Brascamp-Lieb inequality: the determinant inequality behind the transport proof.

If `u_1, …, u_N ∈ ℝ^d` are unit vectors and `c_i > 0` with `∑ c_i u_i u_iᵀ = I_d`, then for all `λ_i > 0`
`det(∑ c_i λ_i u_i u_iᵀ) ≥ ∏ λ_i^{c_i}` (K. Ball). Write `V` for the `d × N` matrix with columns `u_i`, so the frame is
`V diag(c) Vᵀ = I` and `M = V diag(cλ) Vᵀ`. In an orthonormal eigenbasis `e_k` of `M` (`M e_k = μ_k e_k`) put
`a_{ki} = ⟨e_k, u_i⟩`; then `∑_k a_{ki}² = 1`, `∑_i c_i a_{ki}² = 1` and `∑_i c_i λ_i a_{ki}² = μ_k`. With
`s_i = ∑_k a_{ki}²/μ_k`, concavity of the logarithm gives `∑_k a_{ki}² log μ_k ≥ -log s_i`, hence
`log det M = ∑_k log μ_k ≥ -∑_i c_i log s_i`, and a second use of concavity, with weights `c_i/d` and
`∑_i c_i λ_i s_i = d`, gives `∑_i c_i log(λ_i s_i) ≤ 0`. No Cauchy-Binet formula is needed.

* `ball_det_log`: `∑ c_i log λ_i ≤ log det(V diag(cλ) Vᵀ)`;
* `ball_det`: `∏ λ_i^{c_i} ≤ det(V diag(cλ) Vᵀ)`.

The spectral lemmas `eigU_orth`, `eigU_orth'`, `eigU_eigen` are repeated from `FiveS3Proj.lean`.
-/

open Matrix
open scoped BigOperators

namespace QformFiveB

namespace Ball

section Spectral

variable {n : Type*} [Fintype n] [DecidableEq n]

theorem real_star_eq_transpose (M : Matrix n n ℝ) : star M = Mᵀ := by
  rw [Matrix.star_eq_conjTranspose, Matrix.conjTranspose_eq_transpose_of_trivial]

theorem eigU_orth (A : Matrix n n ℝ) (hA : A.IsHermitian) :
    (hA.eigenvectorUnitary : Matrix n n ℝ)ᵀ * (hA.eigenvectorUnitary : Matrix n n ℝ) = 1 := by
  have h := Unitary.coe_star_mul_self hA.eigenvectorUnitary
  rw [real_star_eq_transpose] at h
  exact h

theorem eigU_orth' (A : Matrix n n ℝ) (hA : A.IsHermitian) :
    (hA.eigenvectorUnitary : Matrix n n ℝ) * (hA.eigenvectorUnitary : Matrix n n ℝ)ᵀ = 1 := by
  have h := Unitary.coe_mul_star_self hA.eigenvectorUnitary
  rw [Unitary.coe_star, real_star_eq_transpose] at h
  exact h

theorem eigU_eigen (A : Matrix n n ℝ) (hA : A.IsHermitian) :
    A * (hA.eigenvectorUnitary : Matrix n n ℝ)
      = (hA.eigenvectorUnitary : Matrix n n ℝ) * diagonal hA.eigenvalues := by
  ext i j
  have h := congrFun (hA.mulVec_eigenvectorBasis j) i
  simp only [Matrix.mulVec, dotProduct, Pi.smul_apply, smul_eq_mul] at h
  rw [Matrix.mul_diagonal, Matrix.mul_apply]
  simp only [IsHermitian.eigenvectorUnitary_apply]
  rw [h, mul_comm]

end Spectral

/-- The diagonal entries of `A diag(w) Aᵀ`. -/
theorem diag_conj_apply {κ ι : Type*} [Fintype ι] [DecidableEq ι] (A : Matrix κ ι ℝ) (w : ι → ℝ) (k : κ) :
    (A * diagonal w * Aᵀ) k k = ∑ i, w i * A k i ^ 2 := by
  rw [Matrix.mul_apply]
  apply Finset.sum_congr rfl
  intro i _
  rw [Matrix.mul_diagonal, Matrix.transpose_apply]
  ring

/-- The diagonal entries of `Aᵀ A`. -/
theorem gram_diag_apply {κ ι : Type*} [Fintype κ] (A : Matrix κ ι ℝ) (i : ι) :
    (Aᵀ * A) i i = ∑ k, A k i ^ 2 := by
  rw [Matrix.mul_apply]
  apply Finset.sum_congr rfl
  intro k _
  rw [Matrix.transpose_apply]
  ring

/-- **Ball's determinant inequality, in logarithmic form.** For `V ∈ ℝ^{κ×ι}` with unit columns (`(VᵀV)_{ii} = 1`) and
`c_i > 0` with `V diag(c) Vᵀ = I`, and `λ_i > 0`: `det(V diag(cλ) Vᵀ) > 0` and
`∑ c_i log λ_i ≤ log det(V diag(cλ) Vᵀ)`. -/
theorem ball_det_log {ι κ : Type*} [Fintype ι] [DecidableEq ι] [Fintype κ] [DecidableEq κ] [Nonempty κ]
    (V : Matrix κ ι ℝ) (c l : ι → ℝ) (hc : ∀ i, 0 < c i) (hl : ∀ i, 0 < l i)
    (hframe : V * diagonal c * Vᵀ = 1) (hunit : ∀ i, (Vᵀ * V) i i = 1) :
    0 < (V * diagonal (fun i => c i * l i) * Vᵀ).det
      ∧ ∑ i, c i * Real.log (l i) ≤ Real.log (V * diagonal (fun i => c i * l i) * Vᵀ).det := by
  set M := V * diagonal (fun i => c i * l i) * Vᵀ with hMdef
  have hM : M.IsHermitian := by
    show Mᴴ = M
    rw [Matrix.conjTranspose_eq_transpose_of_trivial, hMdef, Matrix.transpose_mul, Matrix.transpose_mul,
      Matrix.transpose_transpose, Matrix.diagonal_transpose, Matrix.mul_assoc]
  set U : Matrix κ κ ℝ := (hM.eigenvectorUnitary : Matrix κ κ ℝ) with hU
  set μ := hM.eigenvalues with hμ
  set a : Matrix κ ι ℝ := Uᵀ * V with ha
  -- the three identities
  have hi : ∀ i, ∑ k, a k i ^ 2 = 1 := by
    intro i
    rw [← gram_diag_apply, ha, Matrix.transpose_mul, Matrix.transpose_transpose,
      show Vᵀ * U * (Uᵀ * V) = Vᵀ * (U * Uᵀ) * V by simp only [Matrix.mul_assoc], hU, eigU_orth' M hM,
      Matrix.mul_one]
    exact hunit i
  have hii : ∀ k, ∑ i, c i * a k i ^ 2 = 1 := by
    intro k
    rw [← diag_conj_apply, ha, Matrix.transpose_mul, Matrix.transpose_transpose,
      show Uᵀ * V * diagonal c * (Vᵀ * U) = Uᵀ * (V * diagonal c * Vᵀ) * U by simp only [Matrix.mul_assoc],
      hframe, Matrix.mul_one, hU, eigU_orth M hM, Matrix.one_apply_eq]
  have hiii : ∀ k, ∑ i, (c i * l i) * a k i ^ 2 = μ k := by
    intro k
    have hdiag : Uᵀ * M * U = diagonal μ := by
      rw [Matrix.mul_assoc, hU, eigU_eigen M hM, ← Matrix.mul_assoc, eigU_orth M hM, Matrix.one_mul]
    have h1 : (Uᵀ * M * U) k k = μ k := by rw [hdiag, Matrix.diagonal_apply_eq]
    rw [← h1, ← diag_conj_apply, ha, Matrix.transpose_mul, Matrix.transpose_transpose, hMdef]
    simp only [Matrix.mul_assoc]
  -- positivity of the eigenvalues
  have hμpos : ∀ k, 0 < μ k := by
    intro k
    rw [← hiii k]
    obtain ⟨i, -, hi0⟩ : ∃ i ∈ (Finset.univ : Finset ι), (0 : ℝ) < c i * a k i ^ 2 := by
      apply Finset.exists_lt_of_sum_lt
      rw [Finset.sum_const_zero, hii k]
      exact one_pos
    apply Finset.sum_pos' (fun j _ => by have := hc j; have := hl j; positivity)
    refine ⟨i, Finset.mem_univ _, ?_⟩
    have : c i * l i * a k i ^ 2 = l i * (c i * a k i ^ 2) := by ring
    rw [this]
    exact mul_pos (hl i) hi0
  -- the determinant
  have hdet : M.det = ∏ k, μ k := by
    have h := hM.det_eq_prod_eigenvalues
    rw [h]
    simp [hμ]
  have hlogdet : Real.log M.det = ∑ k, Real.log (μ k) := by
    rw [hdet, Real.log_prod]
    intro k _
    exact (hμpos k).ne'
  -- s_i
  set s : ι → ℝ := fun i => ∑ k, a k i ^ 2 * (μ k)⁻¹ with hs
  have hspos : ∀ i, 0 < s i := by
    intro i
    obtain ⟨k, -, hk⟩ : ∃ k ∈ (Finset.univ : Finset κ), (0 : ℝ) < a k i ^ 2 := by
      apply Finset.exists_lt_of_sum_lt
      rw [Finset.sum_const_zero, hi i]
      exact one_pos
    apply Finset.sum_pos' (fun j _ => by have := hμpos j; positivity)
    exact ⟨k, Finset.mem_univ _, mul_pos hk (inv_pos.2 (hμpos k))⟩
  -- Step 1: ∑_k a_{ki}² log μ_k ≥ -log s_i
  have step1 : ∀ i, -Real.log (s i) ≤ ∑ k, a k i ^ 2 * Real.log (μ k) := by
    intro i
    have hJ := (strictConcaveOn_log_Ioi.concaveOn).le_map_sum (t := Finset.univ) (w := fun k => a k i ^ 2)
      (p := fun k => (μ k)⁻¹) (fun k _ => sq_nonneg _) (hi i) (fun k _ => Set.mem_Ioi.2 (inv_pos.2 (hμpos k)))
    simp only [smul_eq_mul, Real.log_inv] at hJ
    have e : ∑ k, a k i ^ 2 * -Real.log (μ k) = -∑ k, a k i ^ 2 * Real.log (μ k) := by
      rw [← Finset.sum_neg_distrib]
      apply Finset.sum_congr rfl
      intro k _
      ring
    rw [e] at hJ
    linarith
  -- Step 2: log det M ≥ -∑ c_i log s_i
  have step2 : -∑ i, c i * Real.log (s i) ≤ Real.log M.det := by
    rw [hlogdet]
    have e : ∑ k, Real.log (μ k) = ∑ i, c i * ∑ k, a k i ^ 2 * Real.log (μ k) := by
      calc ∑ k, Real.log (μ k) = ∑ k, (∑ i, c i * a k i ^ 2) * Real.log (μ k) := by
            apply Finset.sum_congr rfl
            intro k _
            rw [hii k, one_mul]
        _ = ∑ i, c i * ∑ k, a k i ^ 2 * Real.log (μ k) := by
            simp only [Finset.sum_mul, Finset.mul_sum]
            rw [Finset.sum_comm]
            apply Finset.sum_congr rfl
            intro i _
            apply Finset.sum_congr rfl
            intro k _
            ring
    rw [e, ← Finset.sum_neg_distrib]
    apply Finset.sum_le_sum
    intro i _
    have h := mul_le_mul_of_nonneg_left (step1 i) (hc i).le
    linarith
  -- ∑ c_i = d
  have hcsum : ∑ i, c i = (Fintype.card κ : ℝ) := by
    calc ∑ i, c i = ∑ i, c i * ∑ k, a k i ^ 2 := by
          apply Finset.sum_congr rfl
          intro i _
          rw [hi i, mul_one]
      _ = ∑ k, ∑ i, c i * a k i ^ 2 := by
          simp only [Finset.mul_sum]
          rw [Finset.sum_comm]
      _ = ∑ _k : κ, (1 : ℝ) := by
          apply Finset.sum_congr rfl
          intro k _
          exact hii k
      _ = (Fintype.card κ : ℝ) := by
          rw [Finset.sum_const, Finset.card_univ, nsmul_eq_mul, mul_one]
  have hd : (0 : ℝ) < Fintype.card κ := by exact_mod_cast Fintype.card_pos
  -- ∑ c_i λ_i s_i = d
  have hsum_ls : ∑ i, c i * l i * s i = (Fintype.card κ : ℝ) := by
    calc ∑ i, c i * l i * s i = ∑ k, (∑ i, (c i * l i) * a k i ^ 2) * (μ k)⁻¹ := by
          simp only [hs, Finset.mul_sum, Finset.sum_mul]
          rw [Finset.sum_comm]
          apply Finset.sum_congr rfl
          intro k _
          apply Finset.sum_congr rfl
          intro i _
          ring
      _ = ∑ _k : κ, (1 : ℝ) := by
          apply Finset.sum_congr rfl
          intro k _
          rw [hiii k, mul_inv_cancel₀ (hμpos k).ne']
      _ = (Fintype.card κ : ℝ) := by
          rw [Finset.sum_const, Finset.card_univ, nsmul_eq_mul, mul_one]
  -- Step 3: ∑ c_i log(λ_i s_i) ≤ 0
  have step3 : ∑ i, c i * Real.log (l i * s i) ≤ 0 := by
    have hJ := (strictConcaveOn_log_Ioi.concaveOn).le_map_sum (t := Finset.univ)
      (w := fun i => c i / (Fintype.card κ : ℝ)) (p := fun i => l i * s i)
      (fun i _ => div_nonneg (hc i).le hd.le)
      (by rw [← Finset.sum_div, hcsum, div_self hd.ne'])
      (fun i _ => Set.mem_Ioi.2 (mul_pos (hl i) (hspos i)))
    simp only [smul_eq_mul] at hJ
    have e : ∑ i, c i / (Fintype.card κ : ℝ) * (l i * s i) = 1 := by
      rw [show ∑ i, c i / (Fintype.card κ : ℝ) * (l i * s i) = (∑ i, c i * l i * s i) / (Fintype.card κ : ℝ) by
        rw [Finset.sum_div]
        apply Finset.sum_congr rfl
        intro i _
        ring]
      rw [hsum_ls, div_self hd.ne']
    rw [e, Real.log_one] at hJ
    have e2 : ∑ i, c i / (Fintype.card κ : ℝ) * Real.log (l i * s i)
        = (∑ i, c i * Real.log (l i * s i)) / (Fintype.card κ : ℝ) := by
      rw [Finset.sum_div]
      apply Finset.sum_congr rfl
      intro i _
      ring
    rw [e2] at hJ
    exact (div_nonpos_iff.1 hJ).elim (fun h => by linarith [h.1, h.2]) (fun h => h.1)
  -- Step 4
  have e4 : ∑ i, c i * Real.log (l i) = ∑ i, c i * Real.log (l i * s i) - ∑ i, c i * Real.log (s i) := by
    rw [← Finset.sum_sub_distrib]
    apply Finset.sum_congr rfl
    intro i _
    rw [Real.log_mul (hl i).ne' (hspos i).ne']
    ring
  refine ⟨?_, ?_⟩
  · rw [hdet]
    exact Finset.prod_pos (fun k _ => hμpos k)
  · rw [e4]
    linarith

/-- **Ball's determinant inequality.** `∏ λ_i^{c_i} ≤ det(V diag(cλ) Vᵀ)`. -/
theorem ball_det {ι κ : Type*} [Fintype ι] [DecidableEq ι] [Fintype κ] [DecidableEq κ] [Nonempty κ]
    (V : Matrix κ ι ℝ) (c l : ι → ℝ) (hc : ∀ i, 0 < c i) (hl : ∀ i, 0 < l i)
    (hframe : V * diagonal c * Vᵀ = 1) (hunit : ∀ i, (Vᵀ * V) i i = 1) :
    ∏ i, l i ^ c i ≤ (V * diagonal (fun i => c i * l i) * Vᵀ).det := by
  obtain ⟨hpos, h⟩ := ball_det_log V c l hc hl hframe hunit
  have e : ∏ i, l i ^ c i = Real.exp (∑ i, c i * Real.log (l i)) := by
    rw [Real.exp_sum]
    apply Finset.prod_congr rfl
    intro i _
    rw [Real.rpow_def_of_pos (hl i), mul_comm]
  rw [e, ← Real.exp_log hpos]
  exact Real.exp_le_exp.2 h

end Ball

end QformFiveB

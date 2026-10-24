import Mathlib.LinearAlgebra.Matrix.SchurComplement
import Mathlib.LinearAlgebra.Matrix.NonsingularInverse
import Mathlib.Data.Matrix.Block
import Mathlib.Tactic

/-!
Lemma 2.7(b) of "Quadratic forms with five large singular values have bounded densities" (repaired text,
sha256 90f859b7), and the facts about the projection `Π` that the proof of Lemma 4.3 uses.

For `M_H` (rows `m_h`, `h ∈ H`) with Gram matrix `G = M_H M_Hᵀ` invertible (`Θ(H) = det G > 0`), put
`Π = M_Hᵀ G⁻¹ M_H` and `C_T = M_T (1 - Π)` (rows `c_i = (1 - Π) m_i`; `Π` is symmetric). The Gram matrix of the rows
in `H ∪ T` is the block matrix `[[M_H M_Hᵀ, M_H M_Tᵀ], [M_T M_Hᵀ, M_T M_Tᵀ]]`, and
`gram_det_factor`: its determinant is `Θ(H) · det(C_T C_Tᵀ)`.
`proj_symm`, `proj_idem`, `proj_fixes`, `rows_orth`: `Π` is a symmetric idempotent fixing the rows of `M_H`, and the
rows of `C_T` are orthogonal to them (used in Step 4 of Lemma 4.3).
-/

open Matrix

namespace QformFiveB

variable {H T J : Type*} [Fintype H] [Fintype T] [Fintype J] [DecidableEq H] [DecidableEq T] [DecidableEq J]

theorem gram_symm (MH : Matrix H J ℝ) : (MH * MHᵀ)ᵀ = MH * MHᵀ := by
  rw [Matrix.transpose_mul, Matrix.transpose_transpose]

theorem proj_symm (MH : Matrix H J ℝ) : (MHᵀ * (MH * MHᵀ)⁻¹ * MH)ᵀ = MHᵀ * (MH * MHᵀ)⁻¹ * MH := by
  rw [Matrix.transpose_mul, Matrix.transpose_mul, Matrix.transpose_transpose, Matrix.transpose_nonsing_inv,
    gram_symm, Matrix.mul_assoc]

theorem proj_idem (MH : Matrix H J ℝ) (hG : IsUnit (MH * MHᵀ).det) :
    (MHᵀ * (MH * MHᵀ)⁻¹ * MH) * (MHᵀ * (MH * MHᵀ)⁻¹ * MH) = MHᵀ * (MH * MHᵀ)⁻¹ * MH := by
  have hGG : (MH * MHᵀ)⁻¹ * (MH * MHᵀ) = 1 := Matrix.nonsing_inv_mul _ hG
  have e : (MHᵀ * (MH * MHᵀ)⁻¹ * MH) * (MHᵀ * (MH * MHᵀ)⁻¹ * MH)
      = MHᵀ * ((MH * MHᵀ)⁻¹ * (MH * MHᵀ)) * (MH * MHᵀ)⁻¹ * MH := by
    simp only [Matrix.mul_assoc]
  rw [e, hGG, Matrix.mul_one]

theorem proj_fixes (MH : Matrix H J ℝ) (hG : IsUnit (MH * MHᵀ).det) :
    (MHᵀ * (MH * MHᵀ)⁻¹ * MH) * MHᵀ = MHᵀ := by
  have hGG : (MH * MHᵀ)⁻¹ * (MH * MHᵀ) = 1 := Matrix.nonsing_inv_mul _ hG
  rw [Matrix.mul_assoc, Matrix.mul_assoc, hGG, Matrix.mul_one]

/-- The rows of `C_T = M_T (1 - Π)` are orthogonal to the rows of `M_H`. -/
theorem rows_orth (MH : Matrix H J ℝ) (MT : Matrix T J ℝ) (hG : IsUnit (MH * MHᵀ).det) :
    MT * (1 - MHᵀ * (MH * MHᵀ)⁻¹ * MH) * MHᵀ = 0 := by
  rw [Matrix.mul_assoc, Matrix.sub_mul, Matrix.one_mul, proj_fixes MH hG, sub_self, Matrix.mul_zero]

/-- **Lemma 2.7(b).** `Θ(H ∪ T) = Θ(H) det(C_T C_Tᵀ)`, with the Gram matrix of the rows in `H ∪ T` written in
blocks. -/
theorem gram_det_factor (MH : Matrix H J ℝ) (MT : Matrix T J ℝ) (hG : IsUnit (MH * MHᵀ).det) :
    (fromBlocks (MH * MHᵀ) (MH * MTᵀ) (MT * MHᵀ) (MT * MTᵀ)).det
      = (MH * MHᵀ).det * ((MT * (1 - MHᵀ * (MH * MHᵀ)⁻¹ * MH)) * (MT * (1 - MHᵀ * (MH * MHᵀ)⁻¹ * MH))ᵀ).det := by
  haveI : Invertible (MH * MHᵀ) := invertibleOfIsUnitDet _ hG
  have h1P : (1 - MHᵀ * (MH * MHᵀ)⁻¹ * MH)ᵀ = 1 - MHᵀ * (MH * MHᵀ)⁻¹ * MH := by
    rw [Matrix.transpose_sub, Matrix.transpose_one, proj_symm]
  have hidem : (1 - MHᵀ * (MH * MHᵀ)⁻¹ * MH) * (1 - MHᵀ * (MH * MHᵀ)⁻¹ * MH)
      = 1 - MHᵀ * (MH * MHᵀ)⁻¹ * MH := by
    rw [Matrix.sub_mul, Matrix.mul_sub, Matrix.mul_sub, Matrix.one_mul, Matrix.mul_one, Matrix.one_mul,
      proj_idem MH hG]
    abel
  have key : MT * MTᵀ - MT * MHᵀ * ⅟(MH * MHᵀ) * (MH * MTᵀ)
      = (MT * (1 - MHᵀ * (MH * MHᵀ)⁻¹ * MH)) * (MT * (1 - MHᵀ * (MH * MHᵀ)⁻¹ * MH))ᵀ := by
    rw [Matrix.invOf_eq_nonsing_inv, Matrix.transpose_mul, h1P]
    calc MT * MTᵀ - MT * MHᵀ * (MH * MHᵀ)⁻¹ * (MH * MTᵀ)
        = MT * (1 - MHᵀ * (MH * MHᵀ)⁻¹ * MH) * MTᵀ := by
          rw [Matrix.mul_sub, Matrix.sub_mul, Matrix.mul_one]
          simp only [Matrix.mul_assoc]
      _ = MT * ((1 - MHᵀ * (MH * MHᵀ)⁻¹ * MH) * (1 - MHᵀ * (MH * MHᵀ)⁻¹ * MH)) * MTᵀ := by rw [hidem]
      _ = MT * (1 - MHᵀ * (MH * MHᵀ)⁻¹ * MH) * ((1 - MHᵀ * (MH * MHᵀ)⁻¹ * MH) * MTᵀ) := by
          simp only [Matrix.mul_assoc]
  rw [det_fromBlocks₁₁, key]

/-- Lemma 4.3, Step 4: the rows `m_h` (`h ∈ H`) and `c_i` (`i ∈ T'`) have Gram determinant `Θ(H) θ(T')`, since the two
groups are orthogonal. -/
theorem gram_orth_blocks (MH : Matrix H J ℝ) (MT : Matrix T J ℝ) (hG : IsUnit (MH * MHᵀ).det) :
    (fromBlocks (MH * MHᵀ) (MH * (MT * (1 - MHᵀ * (MH * MHᵀ)⁻¹ * MH))ᵀ)
        ((MT * (1 - MHᵀ * (MH * MHᵀ)⁻¹ * MH)) * MHᵀ)
        ((MT * (1 - MHᵀ * (MH * MHᵀ)⁻¹ * MH)) * (MT * (1 - MHᵀ * (MH * MHᵀ)⁻¹ * MH))ᵀ)).det
      = (MH * MHᵀ).det * ((MT * (1 - MHᵀ * (MH * MHᵀ)⁻¹ * MH)) * (MT * (1 - MHᵀ * (MH * MHᵀ)⁻¹ * MH))ᵀ).det := by
  have h0 : (MT * (1 - MHᵀ * (MH * MHᵀ)⁻¹ * MH)) * MHᵀ = 0 := rows_orth MH MT hG
  have h0' : MH * (MT * (1 - MHᵀ * (MH * MHᵀ)⁻¹ * MH))ᵀ = 0 := by
    rw [← Matrix.transpose_transpose (MH * _), Matrix.transpose_mul, Matrix.transpose_transpose, h0,
      Matrix.transpose_zero]
  rw [h0, h0', Matrix.det_fromBlocks_zero₂₁]

end QformFiveB

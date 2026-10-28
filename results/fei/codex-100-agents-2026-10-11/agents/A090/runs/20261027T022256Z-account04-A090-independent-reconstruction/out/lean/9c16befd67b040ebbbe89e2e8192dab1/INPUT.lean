import Mathlib

open scoped BigOperators

/-- Finite active-floor tangent certificate, on positive reference atoms.
Zero-reference/zero-true atoms are handled separately in the prose proof. -/
theorem floor_tangent {n : ℕ} (p x y : Fin n → ℝ) (k : ℝ)
    (hx : ∀ i, 0 < x i)
    (hsum : (∑ i, (y i - x i)) = 0)
    (hactive : ∀ i, p i = k⁻¹ * x i ∨
      (p i ≤ k⁻¹ * x i ∧ x i ≤ y i)) :
    (∑ i, p i * (y i - x i) / x i) ≤ 0 := by
  calc
    (∑ i, p i * (y i - x i) / x i) ≤
        ∑ i, k⁻¹ * (y i - x i) := by
      apply Finset.sum_le_sum
      intro i _
      apply (div_le_iff₀ (hx i)).2
      rcases hactive i with h | ⟨h, hy⟩
      · rw [h]
        ring_nf
      · have hd : 0 ≤ y i - x i := sub_nonneg.mpr hy
        have hmul := mul_le_mul_of_nonneg_right h hd
        nlinarith only [hmul]
    _ = 0 := by rw [← Finset.mul_sum, hsum, mul_zero]

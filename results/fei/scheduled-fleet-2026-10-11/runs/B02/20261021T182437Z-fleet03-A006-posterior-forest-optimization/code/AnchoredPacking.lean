import Mathlib

theorem anchored_packing (n : Nat) (p b : ℝ)
    (a lam pi q : Fin n → ℝ) (hp : 0 ≤ p)
    (hbudget : (∑ i, a i * lam i) ≤ b)
    (hid : ∀ i, q i = pi i * lam i * p)
    (hpi : ∀ i, pi i ≠ 0) :
    (∑ i, (a i / pi i) * q i) ≤ b * p := by
  calc
    (∑ i, (a i / pi i) * q i) = (∑ i, a i * lam i) * p := by
      simp_rw [hid]
      rw [Finset.sum_mul]
      apply Finset.sum_congr rfl
      intro i hi
      field_simp [hpi i]
    _ ≤ b * p := mul_le_mul_of_nonneg_right hbudget hp

#print axioms anchored_packing

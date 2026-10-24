import Mathlib.Tactic

theorem w338_majority_arithmetic :
    (393 / 64 : ℚ) / 9 = 131 / 192 ∧
    (131 / 192 : ℚ) < 25 / 36 ∧
    ((25 / 4 : ℚ) - 393 / 64) / (25 / 4) = 7 / 400 := by
  norm_num

theorem w338_two_job_ratio
    (r₁ r₂ a b v : ℝ) (h : 0 < r₁ + r₂)
    (hB : v * (r₁ + r₂) ≤ 2 + r₁ * a + r₂ * b) :
    v ≤ (2 + r₁ * a + r₂ * b) / (r₁ + r₂) := by
  exact (le_div_iff₀ h).2 hB

theorem w338_checked_core :
    ((393 / 64 : ℚ) / 9 = 131 / 192 ∧
     (131 / 192 : ℚ) < 25 / 36 ∧
     ((25 / 4 : ℚ) - 393 / 64) / (25 / 4) = 7 / 400) ∧
    (∀ (r₁ r₂ a b v : ℝ), 0 < r₁ + r₂ →
      v * (r₁ + r₂) ≤ 2 + r₁ * a + r₂ * b →
      v ≤ (2 + r₁ * a + r₂ * b) / (r₁ + r₂)) := by
  exact ⟨w338_majority_arithmetic, w338_two_job_ratio⟩

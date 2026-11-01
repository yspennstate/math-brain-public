import Mathlib.Tactic

-- Only the normalization identity for the deletion mixture, not the FEI bridge.
theorem deletion_mixture_normalizes (A B : ℝ) (h : A * B - 1 ≠ 0) :
    (A - 1) / (A * B - 1) + A * (B - 1) / (A * B - 1) = 1 := by
  field_simp
  <;> ring

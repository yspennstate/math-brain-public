import Mathlib.Tactic

-- This scalar identity is only one part of the analytic proof.
-- Admission was held; this source has NOT been compiled or certified.
theorem A044_tail_band (M : ℚ) (hM : M ≠ 0) :
    2 * (1 / M - 1 / (2 * M)) = 1 / M := by
  field_simp
  <;> ring

import Mathlib.Analysis.SpecialFunctions.Exp

-- Prepared only. No Lean verification is claimed for this file.
-- This is the algebraic step, not the conditional-probability argument.
theorem survival_hazard_factor (p : ℝ) : (1 - p) * Real.exp p ≤ 1 := by
  have h : 1 - p ≤ Real.exp (-p) := by
    simpa [sub_eq_add_neg, add_comm] using Real.add_one_le_exp (-p)
  calc
    (1 - p) * Real.exp p ≤ Real.exp (-p) * Real.exp p :=
      mul_le_mul_of_nonneg_right h (le_of_lt (Real.exp_pos p))
    _ = 1 := by rw [← Real.exp_add]; simp

#print axioms survival_hazard_factor

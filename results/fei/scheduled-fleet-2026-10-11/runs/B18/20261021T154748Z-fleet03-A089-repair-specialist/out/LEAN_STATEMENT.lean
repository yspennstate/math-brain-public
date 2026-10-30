-- Exact statement argument submitted to lean_check.py; RUNTIME_UNVERIFIED.
-- This file is evidence of the attempted check, not a compilation certificate.
import Mathlib
example (B W T : ℝ) (hW : 0 ≤ W) (h : T ≤ B + W) : 0 ≤ max 0 (T - B) ∧ max 0 (T - B) ≤ W ∧ T - min T B = max 0 (T - B) := by constructor; exact le_max_left _ _; constructor; exact max_le hW (by linarith); by_cases ht : T ≤ B; · rw [min_eq_left ht, max_eq_left (by linarith : T - B ≤ 0)]; ring; · rw [min_eq_right (le_of_not_ge ht), max_eq_right (by linarith : 0 ≤ T - B)]; ring

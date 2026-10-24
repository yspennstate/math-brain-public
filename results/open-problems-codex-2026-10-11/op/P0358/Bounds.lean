import Mathlib.Analysis.Real.Sqrt
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp

-- Algebraic part of the optimized upper bound only.
theorem block_bound (c d z : ℝ) (hc : 0 ≤ c) (hd : 0 ≤ d) (hz : 0 < z) :
    2 * Real.sqrt (c * d) ≤ d / z + c * z := by
  have hs : (Real.sqrt (c * d)) ^ 2 = c * d :=
    Real.sq_sqrt (mul_nonneg hc hd)
  have hn := sq_nonneg (c * z - Real.sqrt (c * d))
  have hn2 := sq_nonneg (d / z - Real.sqrt (c * d))
  have hid : (d / z) * (c * z) = c * d := by
    field_simp
  have hpos : 0 ≤ d / z + c * z :=
    add_nonneg (div_nonneg hd (le_of_lt hz)) (mul_nonneg hc (le_of_lt hz))
  have hspos : 0 ≤ Real.sqrt (c * d) := Real.sqrt_nonneg _
  have hsq : 0 ≤ (d / z - c * z) ^ 2 := sq_nonneg _
  nlinarith

theorem block_equality (c d z : ℝ) (hc : 0 < c) (hd : 0 < d)
    (hz : 0 < z) (hopt : c * z ^ 2 = d) :
    d / z + c * z = 2 * Real.sqrt (c * d) := by
  have hcz : 0 ≤ c * z := le_of_lt (mul_pos hc hz)
  have hs : Real.sqrt (c * d) = c * z := by
    apply (Real.sqrt_eq_iff_mul_self_eq (le_of_lt (mul_pos hc hd)) hcz).2
    nlinarith [hopt]
  have hdiv : d / z = c * z := by
    apply (div_eq_iff (ne_of_gt hz)).2
    nlinarith [hopt]
  rw [hdiv, hs]
  ring

#print axioms block_bound
#print axioms block_equality

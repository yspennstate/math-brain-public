import Mathlib

theorem calibration_rescaling_cancel (a x q : ℝ) (ha : a ≠ 0)
    (hx : 1-x ≠ 0) :
    (1-q)*a/(a*(1-x))=(1-q)/(1-x) := by
  field_simp <;> ring

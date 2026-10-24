import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Data.Real.Basic

/- Algebraic checks only, not a formalization of the probabilistic argument. -/
theorem trap_exponent_identity (A a b : ℝ) :
    2 * A - (a + b) = (A - a) + (A - b) := by
  ring

theorem trap_exponent_positive (A a b : ℝ)
    (ha : a < A) (hb : b < A) : 0 < 2 * A - (a + b) := by
  linarith

theorem reinforced_backward_drift (A p q n : ℝ)
    (hA : 0 < A) (hn : 0 ≤ n) (hloops : p - q < n) :
    (p - q - n) / (A + n) < 0 := by
  apply div_neg_of_neg_of_pos
  · linarith
  · linarith

theorem rectangle_cut_lower_bound (P Q w h : ℝ)
    (hP : 0 ≤ P) (hQ : 0 ≤ Q)
    (hw : 1 ≤ w) (hh : 1 ≤ h) (hnontrivial : 2 ≤ w ∨ 2 ≤ h) :
    min (P + 2 * Q) (2 * P + Q) ≤ h * P + w * Q := by
  rcases hnontrivial with hw2 | hh2
  · apply le_trans (min_le_left _ _)
    nlinarith [mul_nonneg (sub_nonneg.mpr hh) hP,
      mul_nonneg (sub_nonneg.mpr hw2) hQ]
  · apply le_trans (min_le_right _ _)
    nlinarith [mul_nonneg (sub_nonneg.mpr hh2) hP,
      mul_nonneg (sub_nonneg.mpr hw) hQ]

import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith

theorem signed_payment (S A e omega : ℝ) (hS : 2 ≤ S)
    (hmargin : 1 ≤ S - (A + e)) (hbook : omega ≤ 1/4) :
    3/4 ≤ S - max (A + e) 0 - omega := by
  rcases le_total (A + e) 0 with h | h
  · rw [max_eq_right h]
    linarith
  · rw [max_eq_left h]
    linarith

import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith

theorem payment (A D R M H0 Hf : ?) (hA : A ? M-H0)
    (hD : D=H0-Hf) (hR : 0?R) (h0 : 2?H0) (hf : 2?Hf) :
    A + max (D-4*R) 0 ? M-2 := by
  rcases le_total (D-4*R) 0 with h | h
  ? rw [max_eq_right h]; linarith
  ? rw [max_eq_left h]; linarith

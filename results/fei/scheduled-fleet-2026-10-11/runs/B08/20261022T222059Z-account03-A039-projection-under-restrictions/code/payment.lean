import Mathlib

-- This scalar algebra is only one step of the prose theorem.
-- No claim of Lean certification until a trusted compiler checks it.
example (S A D R Sroot : ℝ) (h : S - D + 4 * R = Sroot) :
    S - (A + max (D - 4 * R) 0) = min (S - A) (Sroot - A) := by
  rcases le_total (D - 4 * R) 0 with hle | hge
  · rw [max_eq_right hle, add_zero, min_eq_left (by linarith)]
  · rw [max_eq_left hge, min_eq_right (by linarith)]
    linarith

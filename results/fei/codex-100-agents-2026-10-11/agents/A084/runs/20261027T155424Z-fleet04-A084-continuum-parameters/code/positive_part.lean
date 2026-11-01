import Mathlib.Tactic

theorem A084_positive_part_budget (a b e : Real) (h : a <= b+e)
    (he : 0 <= e) : max a 0 <= max b 0+e := by
  apply max_le
  · linarith [le_max_left b (0 : Real)]
  · linarith [le_max_right b (0 : Real)]

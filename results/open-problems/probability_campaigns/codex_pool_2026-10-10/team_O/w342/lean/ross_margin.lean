import Mathlib.Tactic.NormNum

theorem ross_margin_bound :
    (2491 : ℚ) / 1612800 < (137 : ℚ) / 46080 - (27 : ℚ) / 19994 := by
  norm_num

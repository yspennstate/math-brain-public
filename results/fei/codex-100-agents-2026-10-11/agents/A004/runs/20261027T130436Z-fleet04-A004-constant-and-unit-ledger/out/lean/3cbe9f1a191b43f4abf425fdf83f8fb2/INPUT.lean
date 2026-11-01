import Mathlib

theorem max_fluctuation_bound (x y : ?) :
    max x y ? Real.sqrt (x^2 + y^2) := by
  have hp : 0 ? x^2 + y^2 := by positivity
  have hs := Real.sq_sqrt hp
  have hn := Real.sqrt_nonneg (x^2 + y^2)
  apply max_le
  ? nlinarith [sq_nonneg y]
  ? nlinarith [sq_nonneg x]

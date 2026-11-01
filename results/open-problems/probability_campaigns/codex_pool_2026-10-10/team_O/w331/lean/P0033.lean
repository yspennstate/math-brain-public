import Mathlib.Tactic

theorem w331_disagreement_bound (d : Real) (h0 : 0 <= d) (h1 : d <= 1) :
    (9/10 : Real)*d - (3/5 : Real)*d^2 + (1/10 : Real)*d^3 <= (9/10 : Real)*d := by
  nlinarith [sq_nonneg d, mul_nonneg (sq_nonneg d) (sub_nonneg.mpr h1)]

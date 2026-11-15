import Mathlib.Data.Real.Basic
import Mathlib.Tactic

namespace C36

theorem quartic_lower_bound (x : ℝ) (hx : 0 ≤ x) :
    (39 : ℝ) / 4 ≤ 48*x^4 + 240*x^3 + 600*x^2 - 2125*x + 1250 := by
  by_cases h : x ≤ 1
  · have hu : 0 ≤ 1 - x := sub_nonneg.mpr h
    have h2 : 0 ≤ (1-x)^2 := sq_nonneg (1-x)
    have h4 : 0 ≤ (1-x)^4 := by positivity
    have hm : 0 ≤ 432*(1-x)^2*x := by positivity
    nlinarith [hu, h2, h4, hm]
  · have ht : 0 ≤ x - 1 := le_of_lt (sub_pos.mpr (lt_of_not_ge h))
    have h2 : 0 ≤ (x-1)^2 := sq_nonneg (x-1)
    have h3 : 0 ≤ (x-1)^3 := pow_nonneg ht 3
    have h4 : 0 ≤ (x-1)^4 := pow_nonneg ht 4
    have hs : 0 ≤ (x-(3:ℝ)/2)^2 := sq_nonneg (x-(3:ℝ)/2)
    nlinarith [h2, h3, h4, hs]

def F (x : ℝ) : ℝ :=
  (2/5:ℝ)*(1+(4/5:ℝ)*x+(12/25:ℝ)*x^2+(24/125:ℝ)*x^3+(24/625:ℝ)*x^4)

theorem uniform_drift (x : ℝ) (hx : 0 ≤ x) :
    x + (39:ℝ)/12500 ≤ F x := by
  have h := quartic_lower_bound x hx
  dsimp [F]
  nlinarith [h]

end C36

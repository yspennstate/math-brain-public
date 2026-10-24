import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

-- Algebra only: these statements do not assert any LQG arm estimate.
theorem critical_exponent_identity (a b s : ℝ) :
    (1 - a + b) + a*s - b*s^2 - 1 = (s-1)*(a-b*(s+1)) := by
  ring

theorem thickness_identity (xi Q t : ℝ) :
    t^2/4 - xi*t + xi*Q + (1-xi*Q+xi^2) - 1
      = (t/2-xi)^2 := by
  ring

theorem positive_gap (a b e : ℝ) (he : 0 < e)
    (hmargin : 0 < a - 2*b - b*e) :
    0 < (1-a+b) + a*(1+e) - b*(1+e)^2 - 1 := by
  have hp : 0 < e * (a - 2*b - b*e) := mul_pos he hmargin
  nlinarith

theorem small_epsilon_margin (a b e : ℝ)
    (hgap : 0 < a - 2*b) (heq : 2*b*e = a - 2*b) :
    0 < a - 2*b - b*e := by
  nlinarith

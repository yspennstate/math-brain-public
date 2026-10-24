import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Positivity

theorem concavity_numerator (z : Real) :
    (1 - 3*z) - (1 - 6*z)*(1+z)^3 = z^2*(15+17*z+6*z^2) := by
  ring

theorem concavity_numerator_nonnegative (z : Real) (hz : LE.le 0 z) :
    LE.le 0 ((1 - 3*z) - (1 - 6*z)*(1+z)^3) := by
  rw [concavity_numerator]
  positivity

theorem free_first_coefficient (m3 : Real) :
    2*(-2*m3)+m3 = -3*m3 := by ring

theorem free_second_coefficient (m2 m3 m5 : Real) :
    2*(3*m5-14*m2*m3)-2*m2*(-2*m3)+2*m2*m3-m5 =
      5*m5-22*m2*m3 := by ring

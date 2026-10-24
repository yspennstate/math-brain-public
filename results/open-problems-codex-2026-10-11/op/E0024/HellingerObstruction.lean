import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

/-- Least squared distance of two intensities' square roots to a common value. -/
theorem symmetric_hellinger_lower (p q s : Real) :
    (p-q)^2 <= 2*((p-s)^2+(q-s)^2) := by
  nlinarith [sq_nonneg (p+q-2*s)]

theorem symmetric_hellinger_identity (p q s : Real) :
    2*((p-s)^2+(q-s)^2)-(p-q)^2 = (p+q-2*s)^2 := by
  ring

theorem symmetric_hellinger_optimum (p q : Real) :
    2*((p-(p+q)/2)^2+(q-(p+q)/2)^2) = (p-q)^2 := by
  ring

#print axioms symmetric_hellinger_lower
#print axioms symmetric_hellinger_identity
#print axioms symmetric_hellinger_optimum

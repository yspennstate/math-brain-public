import Mathlib.Tactic.Ring

-- This is the denominator certificate used in the weighted chi-square step.
-- It certifies only the scalar polynomial identity, not the entropy proof.
theorem contrast_denominator (p a c : ℚ) :
    p * a^2 + (1-p) * c^2 - p*(1-p)*(a+c)^2 =
      (p*a-(1-p)*c)^2 := by
  ring

theorem contrast_marginal (u v b : ℚ) :
    (u+b*v)^2 + (1-b^2)*v^2 = u^2+2*b*u*v+v^2 := by
  ring

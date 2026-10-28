import Mathlib

-- Algebraic numerator check for kappa^-1-1 <= h/2.
-- NOT executed: memory admission refused. This file is not a certificate.
example (h x : ℚ) (hh : 0 ≤ h) (hh2 : h ≤ 1/2)
    (hx : x ≤ 1/2) : 2*h*(2*x-h) ≤ h*(2-h)^2 := by
  have hp : 0 ≤ h*(2-2*h+h^2) :=
    mul_nonneg hh (by nlinarith [sq_nonneg h])
  have hq : 0 ≤ 4*h*(1/2-x) := mul_nonneg (by positivity) (by linarith)
  nlinarith

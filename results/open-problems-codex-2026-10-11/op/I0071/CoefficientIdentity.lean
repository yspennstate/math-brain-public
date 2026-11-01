import Mathlib.Tactic.Ring

-- This exact exponent identity gives the factor (theta_i theta_j)^(-2)
-- in the square of each normalized mixed Hessian coefficient.
theorem normalized_hessian_exponent_identity (a b : ℕ) :
    2 * ((a + 1)^2 + (b + 1)^2) + 4 =
      (a + 2)^2 + a^2 + (b + 2)^2 + b^2 := by
  ring

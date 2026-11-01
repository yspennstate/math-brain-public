import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring

-- Exact cancellation after splitting the Volterra integral at a.
-- z represents F(u,v); j represents the unshifted integral.
theorem threshold_residual_identity (a c z u v j : ℝ) :
    -(a / 2 + c * z)^2
      + ((a + c * u)^2 + (a + c * v)^2) / 4
      + a * c * (z - (u + v) / 2) - a^2 / 4 + c^2 * j
    = c^2 * (-z^2 + (u^2 + v^2) / 4 + j) := by
  ring

theorem below_threshold_residual (r s : ℝ) :
    -(s / 2)^2 + (r^2 + s^2) / 4 - r^2 / 4 = 0 := by
  ring

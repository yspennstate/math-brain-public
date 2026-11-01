import Mathlib.Data.Real.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

-- Algebraic checks only; the Poisson and measure-theoretic proofs are in ATTEMPT.md.
theorem endpoint_scaling (e x r : ℝ) :
    e * x + e * r = e * (x + r) := by
  ring

theorem mass_scaling (e r : ℝ) :
    (e * r) ^ 2 = e ^ 2 * r ^ 2 := by
  ring

-- In (x,r) coordinates the intensity is 2 dx dr / r^2.
-- The Jacobian of (x,r) -> (e*x,e*r) is e^2.
theorem intensity_scaling (e r : ℝ) (he : e ≠ 0) (hr : r ≠ 0) :
    (2 / (e * r) ^ 2) * e ^ 2 = 2 / r ^ 2 := by
  field_simp
  <;> ring

theorem laplace_cross_identity (a b : ℝ) :
    (1 - a) + (1 - b) - (1 - a * b) = (1 - a) * (1 - b) := by
  ring

theorem positive_laplace_cross (a b : ℝ)
    (ha : 0 < 1 - a) (hb : 0 < 1 - b) :
    0 < (1 - a) + (1 - b) - (1 - a * b) := by
  rw [laplace_cross_identity]
  exact mul_pos ha hb

#print axioms endpoint_scaling
#print axioms mass_scaling
#print axioms intensity_scaling
#print axioms laplace_cross_identity
#print axioms positive_laplace_cross

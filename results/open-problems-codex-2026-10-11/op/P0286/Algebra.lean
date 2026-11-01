import Mathlib.Tactic.Ring
import Mathlib.Data.Real.Basic

-- Algebra behind the cumulative-density covariance constraint.
theorem projection_covariance_constraint
    (a b z c11 c12 c21 c22 : ℝ)
    (h1 : c11 = -a * (1-a) * z)
    (h2 : c11 + c12 + c21 + c22 = -b * (1-b) * z) :
    c12 + c21 + c22 = (a * (1-a) - b * (1-b)) * z := by
  calc
    c12 + c21 + c22 = (c11 + c12 + c21 + c22) - c11 := by ring
    _ = -b * (1-b) * z - (-a * (1-a) * z) := by rw [h2, h1]
    _ = (a * (1-a) - b * (1-b)) * z := by ring

theorem queue_drift_identity (a b : ℝ) :
    (1-a)*b - a*(1-b) = b-a := by ring

-- Normalization denominator in the TASEP continuous spectral density.
theorem spectral_denominator_identity (p q x : ℝ) :
    q*q - q*(x-(1-p-q)) + p*q = q*(1-x) := by ring
